# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two_chanell-1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.ID_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID_le.sizePolicy().hasHeightForWidth())
        self.ID_le.setSizePolicy(sizePolicy)
        self.ID_le.setObjectName("ID_le")
        self.gridLayout.addWidget(self.ID_le, 2, 0, 1, 1)
        self.read1_chbox = QtWidgets.QCheckBox(self.centralwidget)
        self.read1_chbox.setObjectName("read1_chbox")
        self.gridLayout.addWidget(self.read1_chbox, 0, 0, 1, 1)
        self.send2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send2_btn.setObjectName("send2_btn")
        self.gridLayout.addWidget(self.send2_btn, 13, 0, 1, 1)
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_1.sizePolicy().hasHeightForWidth())
        self.textBrowser_1.setSizePolicy(sizePolicy)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.gridLayout.addWidget(self.textBrowser_1, 0, 1, 10, 1)
        self.read2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.read2_btn.setObjectName("read2_btn")
        self.gridLayout.addWidget(self.read2_btn, 12, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 12, 1, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.data_le = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_le.sizePolicy().hasHeightForWidth())
        self.data_le.setSizePolicy(sizePolicy)
        self.data_le.setObjectName("data_le")
        self.gridLayout.addWidget(self.data_le, 4, 0, 1, 1)
        self.send1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send1_btn.setObjectName("send1_btn")
        self.gridLayout.addWidget(self.send1_btn, 5, 0, 1, 1)
        self.send_chbox = QtWidgets.QCheckBox(self.centralwidget)
        self.send_chbox.setObjectName("send_chbox")
        self.gridLayout.addWidget(self.send_chbox, 6, 0, 1, 1)
        self.periodic_change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.periodic_change_btn.setObjectName("periodic_change_btn")
        self.gridLayout.addWidget(self.periodic_change_btn, 7, 0, 1, 1)
        self.periodic_change_id_chbox = QtWidgets.QCheckBox(self.centralwidget)
        self.periodic_change_id_chbox.setObjectName("periodic_change_id_chbox")
        self.gridLayout.addWidget(self.periodic_change_id_chbox, 8, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Message"))
        self.read1_chbox.setText(_translate("MainWindow", "Читать 1 канал"))
        self.send2_btn.setText(_translate("MainWindow", "отправить во 2 канал"))
        self.read2_btn.setText(_translate("MainWindow", "читать 2 канал"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.send1_btn.setText(_translate("MainWindow", "Отправить в 1 канал"))
        self.send_chbox.setText(_translate("MainWindow", "Отправлять\n"
"постоянно"))
        self.periodic_change_btn.setText(_translate("MainWindow", "Перебор ID"))
        self.periodic_change_id_chbox.setText(_translate("MainWindow", "Перебирать\n"
"постоянно"))
