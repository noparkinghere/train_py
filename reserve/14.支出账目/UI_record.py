# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_record.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_desp = QtWidgets.QTextEdit(self.centralwidget)
        self.text_desp.setObjectName("text_desp")
        self.verticalLayout.addWidget(self.text_desp)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_cash = QtWidgets.QLabel(self.centralwidget)
        self.label_cash.setObjectName("label_cash")
        self.horizontalLayout_2.addWidget(self.label_cash)
        self.line_cash = QtWidgets.QLineEdit(self.centralwidget)
        self.line_cash.setObjectName("line_cash")
        self.horizontalLayout_2.addWidget(self.line_cash)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_all = QtWidgets.QLabel(self.centralwidget)
        self.label_all.setObjectName("label_all")
        self.horizontalLayout.addWidget(self.label_all)
        self.line_all = QtWidgets.QLineEdit(self.centralwidget)
        self.line_all.setObjectName("line_all")
        self.horizontalLayout.addWidget(self.line_all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_cash.setText(_translate("MainWindow", "记录金额："))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_all.setText(_translate("MainWindow", "总共金额："))
