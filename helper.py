"""
всякие вспомогательные функции
"""
import struct
import traceback

from PyQt5.QtCore import QTimer, Qt, QRegExp
from PyQt5.QtGui import QFont, QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QDialog

import Dialog_params
import my_dialog

NewParamsList = 'Новый список'


class InfoMessage(QDialog, Dialog_params.Ui_Dialog_params):

    def __init__(self, info: str):
        super().__init__()
        self.setupUi(self)
        self.info_lbl.setText(info)
        self.info_lbl.setFont(QFont('MS Shell Dlg 2', 10))
        self.setWindowFlag(Qt.FramelessWindowHint)
        QTimer.singleShot(1700, self.close)


class DialogChange(QDialog, my_dialog.Ui_value_changer_dialog):

    def __init__(self, value_name: str, value):
        super().__init__()
        self.setupUi(self)
        self.value_name_lbl.setText(value_name)
        self.lineEdit.setText(value)
        reg_ex = QRegExp("[+-]?([0-9]*[.])?[0-9]+")
        self.lineEdit.setValidator(QRegExpValidator(reg_ex))



# Если при ошибке в слотах приложение просто падает без стека,
# есть хороший способ ловить такие ошибки:
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


def zero_del(s):
    return f'{round(s, 5):>8}'.rstrip('0').rstrip('.')


def int_to_hex_str(x: int):
    return hex(x)[2:].zfill(2).upper()


def float_to_int(f):
    return int(struct.unpack('<I', struct.pack('<f', f))[0])


def bytes_to_float(b: list):
    return struct.unpack('<f', bytearray(b))[0]


def dw2float(dw_array):
    assert (len(dw_array) == 4)
    dw = int.from_bytes(dw_array, byteorder='little', signed=False)
    s = -1 if (dw >> 31) == 1 \
        else 1  # Знак
    e = (dw >> 23) & 0xFF  # Порядок
    m = ((dw & 0x7FFFFF) | 0x800000) if e != 0 \
        else ((dw & 0x7FFFFF) << 1)  # Мантисса
    m1 = m * (2 ** (-23))  # Мантисса в float
    return s * m1 * (2 ** (e - 127))
