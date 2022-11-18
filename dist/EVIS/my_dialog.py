# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_value_changer_dialog(object):
    def setupUi(self, value_changer_dialog):
        value_changer_dialog.setObjectName("value_changer_dialog")
        value_changer_dialog.resize(533, 326)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(value_changer_dialog.sizePolicy().hasHeightForWidth())
        value_changer_dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(value_changer_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.value_name_lbl = QtWidgets.QLabel(value_changer_dialog)
        self.value_name_lbl.setObjectName("value_name_lbl")
        self.gridLayout.addWidget(self.value_name_lbl, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(value_changer_dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.param_table = QtWidgets.QTableWidget(value_changer_dialog)
        self.param_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.param_table.sizePolicy().hasHeightForWidth())
        self.param_table.setSizePolicy(sizePolicy)
        self.param_table.setFrameShape(QtWidgets.QFrame.Panel)
        self.param_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.param_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.param_table.setObjectName("param_table")
        self.param_table.setColumnCount(4)
        self.param_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.param_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.param_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.param_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.param_table.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.param_table, 2, 0, 1, 3)
        self.text_browser = QtWidgets.QTextBrowser(value_changer_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_browser.sizePolicy().hasHeightForWidth())
        self.text_browser.setSizePolicy(sizePolicy)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 3, 0, 1, 3)
        self.process_bar = QtWidgets.QProgressBar(value_changer_dialog)
        self.process_bar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.process_bar.setProperty("value", 0)
        self.process_bar.setTextVisible(False)
        self.process_bar.setInvertedAppearance(False)
        self.process_bar.setObjectName("process_bar")
        self.gridLayout.addWidget(self.process_bar, 4, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(value_changer_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.r_btn1 = QtWidgets.QRadioButton(value_changer_dialog)
        self.r_btn1.setObjectName("r_btn1")
        self.gridLayout.addWidget(self.r_btn1, 5, 1, 1, 1)
        self.r_btn2 = QtWidgets.QRadioButton(value_changer_dialog)
        self.r_btn2.setObjectName("r_btn2")
        self.gridLayout.addWidget(self.r_btn2, 5, 2, 1, 1)

        self.retranslateUi(value_changer_dialog)
        self.buttonBox.accepted.connect(value_changer_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(value_changer_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(value_changer_dialog)

    def retranslateUi(self, value_changer_dialog):
        _translate = QtCore.QCoreApplication.translate
        value_changer_dialog.setWindowTitle(_translate("value_changer_dialog", "Введи новое значение"))
        self.value_name_lbl.setText(_translate("value_changer_dialog", "TextLabel"))
        item = self.param_table.horizontalHeaderItem(0)
        item.setText(_translate("value_changer_dialog", "Параметр"))
        item = self.param_table.horizontalHeaderItem(1)
        item.setText(_translate("value_changer_dialog", "Описание"))
        item = self.param_table.horizontalHeaderItem(2)
        item.setText(_translate("value_changer_dialog", "Значение"))
        item = self.param_table.horizontalHeaderItem(3)
        item.setText(_translate("value_changer_dialog", "Размерность"))
        self.r_btn1.setText(_translate("value_changer_dialog", "RadioButton"))
        self.r_btn2.setText(_translate("value_changer_dialog", "RadioButton"))