# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VMU_monitor_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 761)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(369, 10, 821, 741))
        self.groupBox_3.setObjectName("groupBox_3")
        self.errors_browser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.errors_browser.setGeometry(QtCore.QRect(280, 590, 531, 141))
        self.errors_browser.setObjectName("errors_browser")
        self.reset_faults = QtWidgets.QPushButton(self.groupBox_3)
        self.reset_faults.setEnabled(False)
        self.reset_faults.setGeometry(QtCore.QRect(10, 640, 261, 41))
        self.reset_faults.setObjectName("reset_faults")
        self.connect_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.connect_btn.setGeometry(QtCore.QRect(10, 587, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_btn.sizePolicy().hasHeightForWidth())
        self.connect_btn.setSizePolicy(sizePolicy)
        self.connect_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.connect_btn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.connect_btn.setFont(font)
        self.connect_btn.setObjectName("connect_btn")
        self.vmu_param_table = QtWidgets.QTableWidget(self.groupBox_3)
        self.vmu_param_table.setGeometry(QtCore.QRect(280, 30, 531, 551))
        self.vmu_param_table.setObjectName("vmu_param_table")
        self.vmu_param_table.setColumnCount(3)
        self.vmu_param_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.vmu_param_table.setHorizontalHeaderItem(2, item)
        self.blocks_list = QtWidgets.QListWidget(self.groupBox_3)
        self.blocks_list.setGeometry(QtCore.QRect(12, 28, 256, 551))
        self.blocks_list.setObjectName("blocks_list")
        self.reset_faults_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.reset_faults_2.setEnabled(False)
        self.reset_faults_2.setGeometry(QtCore.QRect(10, 690, 261, 41))
        self.reset_faults_2.setObjectName("reset_faults_2")
        self.command_box = QtWidgets.QGroupBox(self.centralwidget)
        self.command_box.setGeometry(QtCore.QRect(10, 10, 351, 741))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.command_box.sizePolicy().hasHeightForWidth())
        self.command_box.setSizePolicy(sizePolicy)
        self.command_box.setMinimumSize(QtCore.QSize(0, 650))
        self.command_box.setObjectName("command_box")
        self.steer_mode_box = QtWidgets.QGroupBox(self.command_box)
        self.steer_mode_box.setEnabled(False)
        self.steer_mode_box.setGeometry(QtCore.QRect(170, 40, 81, 111))
        self.steer_mode_box.setObjectName("steer_mode_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.steer_mode_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.front_mode_rb = QtWidgets.QRadioButton(self.steer_mode_box)
        self.front_mode_rb.setChecked(True)
        self.front_mode_rb.setObjectName("front_mode_rb")
        self.verticalLayout_3.addWidget(self.front_mode_rb)
        self.crab_mode_rb = QtWidgets.QRadioButton(self.steer_mode_box)
        self.crab_mode_rb.setObjectName("crab_mode_rb")
        self.verticalLayout_3.addWidget(self.crab_mode_rb)
        self.circle_mode_rb = QtWidgets.QRadioButton(self.steer_mode_box)
        self.circle_mode_rb.setObjectName("circle_mode_rb")
        self.verticalLayout_3.addWidget(self.circle_mode_rb)
        self.power_box = QtWidgets.QGroupBox(self.command_box)
        self.power_box.setEnabled(False)
        self.power_box.setGeometry(QtCore.QRect(258, 411, 81, 321))
        self.power_box.setObjectName("power_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.power_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.power_slider = QtWidgets.QSlider(self.power_box)
        self.power_slider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_slider.sizePolicy().hasHeightForWidth())
        self.power_slider.setSizePolicy(sizePolicy)
        self.power_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.power_slider.setMinimum(-100)
        self.power_slider.setMaximum(100)
        self.power_slider.setProperty("value", 0)
        self.power_slider.setOrientation(QtCore.Qt.Vertical)
        self.power_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.power_slider.setObjectName("power_slider")
        self.verticalLayout_2.addWidget(self.power_slider)
        self.power_spinbox = QtWidgets.QSpinBox(self.power_box)
        self.power_spinbox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.power_spinbox.setFont(font)
        self.power_spinbox.setMinimum(-100)
        self.power_spinbox.setMaximum(100)
        self.power_spinbox.setObjectName("power_spinbox")
        self.verticalLayout_2.addWidget(self.power_spinbox)
        self.front_steer_box = QtWidgets.QGroupBox(self.command_box)
        self.front_steer_box.setEnabled(False)
        self.front_steer_box.setGeometry(QtCore.QRect(170, 160, 81, 271))
        self.front_steer_box.setObjectName("front_steer_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.front_steer_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.front_steer_slider = QtWidgets.QSlider(self.front_steer_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.front_steer_slider.sizePolicy().hasHeightForWidth())
        self.front_steer_slider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.front_steer_slider.setFont(font)
        self.front_steer_slider.setMinimum(-1000)
        self.front_steer_slider.setMaximum(1000)
        self.front_steer_slider.setSingleStep(10)
        self.front_steer_slider.setPageStep(100)
        self.front_steer_slider.setTracking(False)
        self.front_steer_slider.setOrientation(QtCore.Qt.Vertical)
        self.front_steer_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.front_steer_slider.setObjectName("front_steer_slider")
        self.verticalLayout_4.addWidget(self.front_steer_slider)
        self.front_steer_spinbox = QtWidgets.QSpinBox(self.front_steer_box)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.front_steer_spinbox.setFont(font)
        self.front_steer_spinbox.setFrame(False)
        self.front_steer_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.front_steer_spinbox.setReadOnly(False)
        self.front_steer_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.front_steer_spinbox.setKeyboardTracking(False)
        self.front_steer_spinbox.setMinimum(-1000)
        self.front_steer_spinbox.setMaximum(1000)
        self.front_steer_spinbox.setSingleStep(10)
        self.front_steer_spinbox.setObjectName("front_steer_spinbox")
        self.verticalLayout_4.addWidget(self.front_steer_spinbox)
        self.rear_steer_box = QtWidgets.QGroupBox(self.command_box)
        self.rear_steer_box.setEnabled(False)
        self.rear_steer_box.setGeometry(QtCore.QRect(170, 430, 81, 301))
        self.rear_steer_box.setObjectName("rear_steer_box")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.rear_steer_box)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rear_steer_slider = QtWidgets.QSlider(self.rear_steer_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rear_steer_slider.sizePolicy().hasHeightForWidth())
        self.rear_steer_slider.setSizePolicy(sizePolicy)
        self.rear_steer_slider.setMinimum(-1000)
        self.rear_steer_slider.setMaximum(1000)
        self.rear_steer_slider.setSingleStep(10)
        self.rear_steer_slider.setPageStep(100)
        self.rear_steer_slider.setSliderPosition(0)
        self.rear_steer_slider.setOrientation(QtCore.Qt.Vertical)
        self.rear_steer_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rear_steer_slider.setObjectName("rear_steer_slider")
        self.verticalLayout_5.addWidget(self.rear_steer_slider)
        self.rear_steer_spinbox = QtWidgets.QSpinBox(self.rear_steer_box)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.rear_steer_spinbox.setFont(font)
        self.rear_steer_spinbox.setWrapping(False)
        self.rear_steer_spinbox.setFrame(False)
        self.rear_steer_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.rear_steer_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.rear_steer_spinbox.setMinimum(-1000)
        self.rear_steer_spinbox.setMaximum(1000)
        self.rear_steer_spinbox.setSingleStep(10)
        self.rear_steer_spinbox.setObjectName("rear_steer_spinbox")
        self.verticalLayout_5.addWidget(self.rear_steer_spinbox)
        self.power_rb = QtWidgets.QRadioButton(self.command_box)
        self.power_rb.setGeometry(QtCore.QRect(260, 51, 72, 20))
        self.power_rb.setChecked(True)
        self.power_rb.setAutoExclusive(True)
        self.power_rb.setObjectName("power_rb")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.power_rb)
        self.suspesion_box = QtWidgets.QGroupBox(self.command_box)
        self.suspesion_box.setEnabled(False)
        self.suspesion_box.setGeometry(QtCore.QRect(10, 340, 151, 391))
        self.suspesion_box.setObjectName("suspesion_box")
        self.fl_sus_box = QtWidgets.QGroupBox(self.suspesion_box)
        self.fl_sus_box.setEnabled(False)
        self.fl_sus_box.setGeometry(QtCore.QRect(12, 18, 61, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fl_sus_box.setFont(font)
        self.fl_sus_box.setAlignment(QtCore.Qt.AlignCenter)
        self.fl_sus_box.setObjectName("fl_sus_box")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fl_sus_box)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fl_sus_slider = QtWidgets.QSlider(self.fl_sus_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fl_sus_slider.sizePolicy().hasHeightForWidth())
        self.fl_sus_slider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.fl_sus_slider.setFont(font)
        self.fl_sus_slider.setMinimum(-1000)
        self.fl_sus_slider.setMaximum(1000)
        self.fl_sus_slider.setSingleStep(10)
        self.fl_sus_slider.setPageStep(100)
        self.fl_sus_slider.setTracking(False)
        self.fl_sus_slider.setOrientation(QtCore.Qt.Vertical)
        self.fl_sus_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.fl_sus_slider.setObjectName("fl_sus_slider")
        self.verticalLayout_7.addWidget(self.fl_sus_slider)
        self.fl_sus_spinbox = QtWidgets.QSpinBox(self.fl_sus_box)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.fl_sus_spinbox.setFont(font)
        self.fl_sus_spinbox.setFrame(False)
        self.fl_sus_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.fl_sus_spinbox.setReadOnly(False)
        self.fl_sus_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.fl_sus_spinbox.setKeyboardTracking(False)
        self.fl_sus_spinbox.setMinimum(-1000)
        self.fl_sus_spinbox.setMaximum(1000)
        self.fl_sus_spinbox.setSingleStep(10)
        self.fl_sus_spinbox.setObjectName("fl_sus_spinbox")
        self.verticalLayout_7.addWidget(self.fl_sus_spinbox)
        self.rl_sus_box = QtWidgets.QGroupBox(self.suspesion_box)
        self.rl_sus_box.setEnabled(False)
        self.rl_sus_box.setGeometry(QtCore.QRect(10, 200, 61, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rl_sus_box.setFont(font)
        self.rl_sus_box.setAlignment(QtCore.Qt.AlignCenter)
        self.rl_sus_box.setObjectName("rl_sus_box")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.rl_sus_box)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rl_sus_slider = QtWidgets.QSlider(self.rl_sus_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rl_sus_slider.sizePolicy().hasHeightForWidth())
        self.rl_sus_slider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.rl_sus_slider.setFont(font)
        self.rl_sus_slider.setMinimum(-1000)
        self.rl_sus_slider.setMaximum(1000)
        self.rl_sus_slider.setSingleStep(10)
        self.rl_sus_slider.setPageStep(100)
        self.rl_sus_slider.setTracking(False)
        self.rl_sus_slider.setOrientation(QtCore.Qt.Vertical)
        self.rl_sus_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rl_sus_slider.setObjectName("rl_sus_slider")
        self.verticalLayout_8.addWidget(self.rl_sus_slider)
        self.rl_sus_spinbox = QtWidgets.QSpinBox(self.rl_sus_box)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.rl_sus_spinbox.setFont(font)
        self.rl_sus_spinbox.setFrame(False)
        self.rl_sus_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.rl_sus_spinbox.setReadOnly(False)
        self.rl_sus_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.rl_sus_spinbox.setKeyboardTracking(False)
        self.rl_sus_spinbox.setMinimum(-1000)
        self.rl_sus_spinbox.setMaximum(1000)
        self.rl_sus_spinbox.setSingleStep(10)
        self.rl_sus_spinbox.setObjectName("rl_sus_spinbox")
        self.verticalLayout_8.addWidget(self.rl_sus_spinbox)
        self.rr_sus_box = QtWidgets.QGroupBox(self.suspesion_box)
        self.rr_sus_box.setEnabled(False)
        self.rr_sus_box.setGeometry(QtCore.QRect(80, 200, 61, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rr_sus_box.setFont(font)
        self.rr_sus_box.setAlignment(QtCore.Qt.AlignCenter)
        self.rr_sus_box.setObjectName("rr_sus_box")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.rr_sus_box)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.rr_sus_slider = QtWidgets.QSlider(self.rr_sus_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rr_sus_slider.sizePolicy().hasHeightForWidth())
        self.rr_sus_slider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.rr_sus_slider.setFont(font)
        self.rr_sus_slider.setMinimum(-1000)
        self.rr_sus_slider.setMaximum(1000)
        self.rr_sus_slider.setSingleStep(10)
        self.rr_sus_slider.setPageStep(100)
        self.rr_sus_slider.setTracking(False)
        self.rr_sus_slider.setOrientation(QtCore.Qt.Vertical)
        self.rr_sus_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.rr_sus_slider.setObjectName("rr_sus_slider")
        self.verticalLayout_9.addWidget(self.rr_sus_slider)
        self.rr_sus_spinbox = QtWidgets.QSpinBox(self.rr_sus_box)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.rr_sus_spinbox.setFont(font)
        self.rr_sus_spinbox.setFrame(False)
        self.rr_sus_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.rr_sus_spinbox.setReadOnly(False)
        self.rr_sus_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.rr_sus_spinbox.setKeyboardTracking(False)
        self.rr_sus_spinbox.setMinimum(-1000)
        self.rr_sus_spinbox.setMaximum(1000)
        self.rr_sus_spinbox.setSingleStep(10)
        self.rr_sus_spinbox.setObjectName("rr_sus_spinbox")
        self.verticalLayout_9.addWidget(self.rr_sus_spinbox)
        self.fr_sus_box = QtWidgets.QGroupBox(self.suspesion_box)
        self.fr_sus_box.setEnabled(False)
        self.fr_sus_box.setGeometry(QtCore.QRect(80, 20, 61, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fr_sus_box.setFont(font)
        self.fr_sus_box.setAlignment(QtCore.Qt.AlignCenter)
        self.fr_sus_box.setObjectName("fr_sus_box")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.fr_sus_box)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fr_sus_slider = QtWidgets.QSlider(self.fr_sus_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_sus_slider.sizePolicy().hasHeightForWidth())
        self.fr_sus_slider.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.fr_sus_slider.setFont(font)
        self.fr_sus_slider.setMinimum(-1000)
        self.fr_sus_slider.setMaximum(1000)
        self.fr_sus_slider.setSingleStep(10)
        self.fr_sus_slider.setPageStep(100)
        self.fr_sus_slider.setTracking(False)
        self.fr_sus_slider.setOrientation(QtCore.Qt.Vertical)
        self.fr_sus_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.fr_sus_slider.setObjectName("fr_sus_slider")
        self.verticalLayout_11.addWidget(self.fr_sus_slider)
        self.fr_sus_spinbox = QtWidgets.QSpinBox(self.fr_sus_box)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.fr_sus_spinbox.setFont(font)
        self.fr_sus_spinbox.setFrame(False)
        self.fr_sus_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.fr_sus_spinbox.setReadOnly(False)
        self.fr_sus_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.fr_sus_spinbox.setKeyboardTracking(False)
        self.fr_sus_spinbox.setMinimum(-1000)
        self.fr_sus_spinbox.setMaximum(1000)
        self.fr_sus_spinbox.setSingleStep(10)
        self.fr_sus_spinbox.setObjectName("fr_sus_spinbox")
        self.verticalLayout_11.addWidget(self.fr_sus_spinbox)
        self.speed_box = QtWidgets.QGroupBox(self.command_box)
        self.speed_box.setEnabled(False)
        self.speed_box.setGeometry(QtCore.QRect(258, 81, 81, 321))
        self.speed_box.setObjectName("speed_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.speed_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.speed_slider = QtWidgets.QSlider(self.speed_box)
        self.speed_slider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider.sizePolicy().hasHeightForWidth())
        self.speed_slider.setSizePolicy(sizePolicy)
        self.speed_slider.setMinimum(-5000)
        self.speed_slider.setMaximum(8000)
        self.speed_slider.setSingleStep(100)
        self.speed_slider.setPageStep(500)
        self.speed_slider.setOrientation(QtCore.Qt.Vertical)
        self.speed_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.speed_slider.setObjectName("speed_slider")
        self.verticalLayout.addWidget(self.speed_slider)
        self.speed_spinbox = QtWidgets.QSpinBox(self.speed_box)
        self.speed_spinbox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.speed_spinbox.setFont(font)
        self.speed_spinbox.setMinimum(-5000)
        self.speed_spinbox.setMaximum(8000)
        self.speed_spinbox.setSingleStep(100)
        self.speed_spinbox.setObjectName("speed_spinbox")
        self.verticalLayout.addWidget(self.speed_spinbox)
        self.speed_rb = QtWidgets.QRadioButton(self.command_box)
        self.speed_rb.setGeometry(QtCore.QRect(260, 20, 81, 20))
        self.speed_rb.setChecked(False)
        self.speed_rb.setAutoExclusive(True)
        self.speed_rb.setObjectName("speed_rb")
        self.steer_allow_cb = QtWidgets.QCheckBox(self.command_box)
        self.steer_allow_cb.setGeometry(QtCore.QRect(170, 20, 62, 20))
        self.steer_allow_cb.setObjectName("steer_allow_cb")
        self.suspesion_allow_cb = QtWidgets.QCheckBox(self.command_box)
        self.suspesion_allow_cb.setGeometry(QtCore.QRect(20, 320, 141, 20))
        self.suspesion_allow_cb.setObjectName("suspesion_allow_cb")
        self.free_box = QtWidgets.QGroupBox(self.command_box)
        self.free_box.setGeometry(QtCore.QRect(10, 20, 151, 291))
        self.free_box.setObjectName("free_box")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Теневая для диностенда"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Параметры"))
        self.reset_faults.setText(_translate("MainWindow", "Сброс ошибок"))
        self.connect_btn.setText(_translate("MainWindow", "Подключиться"))
        item = self.vmu_param_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Параметр"))
        item = self.vmu_param_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Значение"))
        item = self.vmu_param_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Размерность"))
        self.reset_faults_2.setText(_translate("MainWindow", "Пустая кнопка"))
        self.command_box.setTitle(_translate("MainWindow", "Управление "))
        self.steer_mode_box.setTitle(_translate("MainWindow", "Режим"))
        self.front_mode_rb.setText(_translate("MainWindow", "Перед"))
        self.crab_mode_rb.setText(_translate("MainWindow", "КРАБ"))
        self.circle_mode_rb.setText(_translate("MainWindow", "КРУГ"))
        self.power_box.setTitle(_translate("MainWindow", "Момент"))
        self.front_steer_box.setTitle(_translate("MainWindow", "Передний"))
        self.rear_steer_box.setTitle(_translate("MainWindow", "Задний"))
        self.power_rb.setText(_translate("MainWindow", "Момент"))
        self.suspesion_box.setTitle(_translate("MainWindow", "Высота"))
        self.fl_sus_box.setTitle(_translate("MainWindow", "FL"))
        self.rl_sus_box.setTitle(_translate("MainWindow", "RL"))
        self.rr_sus_box.setTitle(_translate("MainWindow", "RR"))
        self.fr_sus_box.setTitle(_translate("MainWindow", "FR"))
        self.speed_box.setTitle(_translate("MainWindow", "Скорость"))
        self.speed_rb.setText(_translate("MainWindow", "Скорость"))
        self.steer_allow_cb.setText(_translate("MainWindow", "Рулим"))
        self.suspesion_allow_cb.setText(_translate("MainWindow", "Активная подвеска"))
        self.free_box.setTitle(_translate("MainWindow", "Пустое место"))
