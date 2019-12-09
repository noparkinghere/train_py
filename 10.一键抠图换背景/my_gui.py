# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(392, 351)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 140, 201, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(238, 248, 51, 31))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(-110, 250, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 50, 69, 22))
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(200, 50, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(40, 250, 71, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "填入 API KEY，默认不填，出错无法使用时获取填写"))
        self.label.setText(_translate("Form", "图片放在软件同级的 pic 目录下"))
        self.label_2.setText(_translate("Form", "等待处理"))
        self.comboBox.setItemText(0, _translate("Form", "白"))
        self.comboBox.setItemText(1, _translate("Form", "红"))
        self.comboBox.setItemText(2, _translate("Form", "黑"))
        self.comboBox.setItemText(3, _translate("Form", "蓝"))
        self.comboBox.setItemText(4, _translate("Form", "橙"))
        self.comboBox.setItemText(5, _translate("Form", "紫"))
        self.comboBox.setItemText(6, _translate("Form", "绿"))
        self.pushButton_2.setText(_translate("Form", "处理输出"))
