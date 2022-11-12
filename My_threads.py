import datetime
import os
import time

import pandas as pd
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QEventLoop
from pandas import ExcelWriter

from CANAdater import CANAdapter
from EVONode import EVONode
from Parametr import Parametr
from helper import empty_par

invertor_command_dict = {
    'POWER_ON': (0x200100, "ОСТОРОЖНО!!! Высокое напряжение ВКЛЮЧЕНО!"),
    'POWER_OFF': (0x200101, "Высокое напряжение выключено!"),
    'RESET_DEVICE': (0x200200, "Инвертор перезагружен"),
    'RESET_PARAMETERS': (0x200201, "Параметры инвертора сброшены на заводские настройки"),
    'APPLY_PARAMETERS': (0x200202, "Текущие параметры сохранены в ЕЕПРОМ Инвертора"),
    'BEGIN_POSITION_SENSOR_CALIBRATION': (0x200203,  "Идёт калибровка Инвертора"),
    'INVERT_ROTATION': (0x200204, "Направление вращения двигателя инвертировано"),
    'RESET_FAULTS': (0x200205, "Ошибки Инвертора сброшены")}


# поток для сохранения в файл настроек блока
# возвращает сигналу о процентах выполнения, сигнал ошибки - не пустая строка и сигнал окончания сохранения - булево
class SaveToFileThread(QThread):
    SignalOfReady = pyqtSignal(int, str, bool)
    err_thread_signal = pyqtSignal(str)
    max_iteration = 1000
    iter_count = 1
    current_params_list = []
    ready_persent = 0
    adapter = None  # CANAdapter()

    def __init__(self):
        super().__init__()
        self.max_errors = 30
        self.node_to_save = EVONode
        self.finished.connect(self.finished_tread)

    def finished_tread(self):
        self.killTimer(self.num_timer)

    def run(self):
        self.errors_counter = 0
        self.params_counter = 0

        def request_param():
            param = all_params_list[self.params_counter]
            # я проверяю, если параметр уже известен, его опрашивать не надо,
            # но если они все известны, возникает выход за пределы словаря
            # while param.value:
            #     self.params_counter += 1
            #     param = all_params_list[self.params_counter]
            if not param.value:
                if param.address and int(param.address, 16) > 0:  # нужно чтоб параметр группы не проскочил
                    param = all_params_list[self.params_counter].get_value(self.adapter)

                    while isinstance(param, str):
                        self.errors_counter += 1
                        param = all_params_list[self.params_counter].get_value(self.adapter)
                        if self.errors_counter >= self.max_errors:
                            self.errors_counter = 0
                            self.params_counter = 0
                            self.SignalOfReady.emit(self.ready_persent,
                                                    f'{param} \n'
                                                    f'поток сохранения прерван,повторите ', False)
                            timer.stop()
                            return

            self.errors_counter = 0
            self.params_counter += 1
            self.ready_persent = int(90 * self.params_counter / len_param_list)
            self.SignalOfReady.emit(self.ready_persent, '', False)
            if self.params_counter >= len_param_list:
                timer.stop()
                self.save_file(all_params_list)

        send_delay = 3  # задержка отправки в кан сообщений
        all_params_list = []
        param_dict = self.node_to_save.group_params_dict.copy()
        for group_name, param_list in param_dict.items():
            e_par = Parametr()
            e_par.name = f'group {group_name}'
            all_params_list.append(e_par)
            for param in param_list:
                all_params_list.append(param)
        len_param_list = len(all_params_list)

        timer = QTimer()
        timer.timeout.connect(request_param)
        self.num_timer = timer.start(send_delay)

        loop = QEventLoop()
        loop.exec_()

    def save_file(self, all_params_list):
        self.errors_counter = 0
        self.params_counter = 0
        save_list = []
        l = 10 / len(all_params_list)
        for p in all_params_list:
            if 'group' in p.name:
                par = empty_par.copy()
                par['name'] = p.name
            else:
                par = p.to_dict().copy()
            self.ready_persent += l
            self.SignalOfReady.emit(self.ready_persent, '', False)

            save_list.append(par.copy())

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f'ECU_Settings/{self.node_to_save.name}_{self.node_to_save.serial_number}_{now}.xlsx'
        df = pd.DataFrame(save_list, columns=p.to_dict().keys())
        df.to_excel(file_name, index=False, sheet_name=self.node_to_save.name)
        # вместо строки ошибки отправляем название файла,куда сохранил настройки
        self.SignalOfReady.emit(100, file_name, True)


# поток для опроса параметров и ошибок
class MainThread(QThread):
    # сигнал со списком параметров из текущей группы
    threadSignalAThread = pyqtSignal(list)
    # сигнал с ошибками
    err_thread_signal = pyqtSignal(dict)
    max_iteration = 1000
    iter_count = 1
    current_params_list = []
    current_node = EVONode()
    adapter = None  # CANAdapter()
    magic_word = 100794368

    def __init__(self):
        super().__init__()
        self.current_nodes_list = []

    def run(self):
        def emitting():  # передача заполненного списка параметров
            self.threadSignalAThread.emit(self.ans_list)
            self.params_counter = 0
            self.errors_counter = 0
            self.ans_list = []
            self.iter_count += 1
            if self.iter_count > self.max_iteration:  # это нужно для периода опроса от 1 до 1000 и снова
                self.iter_count = 1

        def request_node():
            if not self.len_param_list:
                self.threadSignalAThread.emit(['Пустой список \n Сюда можно добавить параметры двойным кликом по '
                                               'названию нужного параметра'])
                return
            current_param = self.current_params_list[self.params_counter]
            if not self.iter_count == 1:
                while not self.iter_count % current_param.period == 0:
                    # если период опроса текущего параметра не кратен текущей итерации,
                    # заполняем его нулями, чтоб в таблице осталось его старое значение
                    # и запрашиваем следующий параметр. Это ускоряет опрос параметров с малым периодом опроса
                    self.ans_list.append(bytearray([0, 0, 0, 0, 0, 0, 0, 0]))
                    self.params_counter += 1
                    if self.params_counter >= self.len_param_list:
                        self.params_counter = 0
                        emitting()
                        return
            if current_param.node.name in (node.name for node in self.current_nodes_list):
                param = current_param.get_value(self.adapter)
                # если строка - значит ошибка
                if isinstance(param, str):
                    self.errors_counter += 1
                    if self.errors_counter >= self.max_errors:
                        self.threadSignalAThread.emit([param])
                        return
                else:
                    self.errors_counter = 0
                    if param == self.magic_word:
                        current_param.period = 1001
                        current_param.value = 'Параметр \nотсутствует'
            else:
                param = 'Блок не подключен'
                current_param.value = param
            # тут всё просто, собираем весь список и отправляем кучкой
            # какая-то херня. мне, по-факту этот список вообще нахер не нужен, сюда можно чисто ошибки пихать
            # , значения всё равно в текущем списке параметров
            self.ans_list.append(param)
            self.params_counter += 1
            if self.params_counter >= self.len_param_list:
                self.params_counter = 0
                emitting()

        def request_errors():
            # опрос ошибок, на это время опрос параметров отключается
            timer.stop()
            err_dict = {}
            has_new_err = False
            for nd in self.current_nodes_list:
                old_e_len = len(nd.current_errors_list)
                old_w_len = len(nd.current_warnings_list)

                nd.current_errors_list = nd.check_errors(self.adapter).copy()
                nd.current_warnings_list = nd.check_errors(self.adapter, 'warnings').copy()
                if len(nd.current_errors_list) != old_e_len or len(nd.current_warnings_list) != old_w_len:
                    has_new_err = True
                err_dict[nd.name] = sorted(list(nd.current_errors_list.union(nd.current_warnings_list)))

            if has_new_err:
                self.err_thread_signal.emit(err_dict)
            timer.start(send_delay)

        send_delay = 13  # задержка отправки в кан сообщений методом подбора с таким не зависает
        err_req_delay = 500
        self.max_errors = 3
        self.len_param_list = len(self.current_params_list)
        if self.len_param_list < self.max_errors:
            self.max_errors = self.len_param_list
        self.ans_list = []
        self.params_counter = 0
        self.errors_counter = 0

        timer = QTimer()
        timer.timeout.connect(request_node)
        timer.start(send_delay)

        err_timer = QTimer()
        err_timer.timeout.connect(request_errors)
        err_timer.start(err_req_delay)

        loop = QEventLoop()
        loop.exec_()

    def invertor_command(self, command: str):
        problem_str = 'Команда не прошла'
        if command not in invertor_command_dict.keys():
            return 'Неверная Команда', problem_str
        if self.isRunning():
            self.wait(100)
        for node in self.current_nodes_list:
            if node.name == 'Инвертор_МЭИ':
                # передавать надо исключительно в первый кан
                if node.request_id in self.adapter.id_nodes_dict.keys():
                    adapter_can1 = self.adapter.id_nodes_dict[node.request_id]
                    answer = node.send_val(invertor_command_dict[command][0], adapter_can1)
                    if not answer:
                        suc = invertor_command_dict[command][1]
                    else:
                        suc = problem_str
                    return answer, suc
                else:
                    answer = 'Нет связи с CAN1-адаптером'
                return answer + ' Для калибровки и инверсии инвертора\n нужно ВЫКЛЮЧИТЬ высокое напряжение', problem_str


class WaitCanAnswerThread(QThread):
    SignalOfProcess = pyqtSignal(str)
    adapter = None  # CANAdapter()
    id_for_read = 0x18FF87A7
    answer_byte = 0
    answer_dict = {
        0: 'принята команда привязки',
        1: 'приемник переведен в режим привязки, ожидание включения пульта ДУ',
        2: 'привязка завершена',
        254: 'ошибка',
        255: 'команда недоступна'
    }
    wait_time = 10000   # максимальное время, через которое поток отключится

    def __init__(self):
        super().__init__()
        self.start_time = time.perf_counter()

    def run(self):
        self.err_count = 0
        def request_ans():

            if (time.perf_counter() > self.start_time + self.wait_time) or self.err_count > 10:
                self.quit()
                self.wait()
                return
            ans = self.adapter.can_read(self.id_for_read)
            if not isinstance(ans, str):
                byte_a = ans[self.answer_byte]
                self.err_count = 0
                if byte_a in self.answer_dict:
                    ans = self.answer_dict[byte_a]
                    if byte_a == 2:
                        self.err_count = 11
                else:
                    ans = 'Ошибочный байт, нет в словаре'
            else:
                self.err_count += 1
            self.SignalOfProcess.emit(ans)

        timer = QTimer()
        timer.timeout.connect(request_ans)
        timer.start(10)

        loop = QEventLoop()
        loop.exec_()


def save_params_dict_to_file(param_d: dict, file_name: str, sheet_name=None):
    if sheet_name is None:
        sheet_name = 'Избранное'
    all_params_list = []
    param_dict = param_d.copy()
    for group_name, param_list in param_dict.items():
        par = empty_par.copy()
        par['name'] = f'group {group_name}'
        all_params_list.append(par)
        for param in param_list:
            all_params_list.append(param.to_dict().copy())

    df = pd.DataFrame(all_params_list, columns=empty_par.keys())
    with ExcelWriter(file_name, mode="a" if os.path.exists(file_name) else "w", if_sheet_exists='overlay') as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)


def fill_compare_values(node: EVONode, dict_for_compare: dict):
    for group_name, group_params in node.group_params_dict.items():
        if group_name in dict_for_compare.keys():
            for param in group_params:
                if param.name in dict_for_compare[group_name].keys():
                    param.compare_value = dict_for_compare[group_name][param.name]
    node.has_compare_params = True
