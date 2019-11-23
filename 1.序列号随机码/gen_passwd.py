import collections
import string
import random
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QDesktopWidget, QHBoxLayout, QVBoxLayout, \
  QGridLayout, QLineEdit, QTextEdit, QMainWindow, QLCDNumber, QSlider
from my_gui import Ui_MainWindow

symbol = {'digital': string.digits, 'lowerLetter': string.ascii_lowercase,
          'upperLetter': string.ascii_uppercase, 'specSym': string.punctuation}


class MyMainWindow(QMainWindow, Ui_MainWindow):
  field = ''
  fieldlist = []

  def genRandomSingle(self, num):
    rand_data = ''.join(random.sample(self.field, num))
    return rand_data
  
  def ModeSel(self):
    self.checkBox_2

  def __init__(self, *args, parent=None):
    super(MyMainWindow, self).__init__(parent)
    self.setupUi(self)
    for i in args:
      self.field += i
    # 设置信号与槽
    self.CreateSignalSlot()
    
  def CreateSignalSlot(self):
    self.checkBox.stateChanged.connect(self.AddDigtal)
    self.checkBox.stateChanged.connect(self.Addlowercase)
    self.checkBox.stateChanged.connect(self.Adduppercase)
    self.checkBox.stateChanged.connect(self.Addpunctuation)
    # self.checkBox.isDown.connect(self.RmDigtal)
    # self.checkBox.isDown.connect(self.Rmlowercase)
    # self.checkBox.isDown.connect(self.Rmuppercase)
    # self.checkBox.isDown.connect(self.Rmpunctuation)

  def AddDigtal(self, state):
    self.fieldlist.append(state)
    
  def Addlowercase(self, state):
    self.fieldlist.append(state)

  def Adduppercase(self, state):
    self.fieldlist.append(state)


  def Addpunctuation(self, state):
    self.fieldlist.append(state)

  def RmDigtal(self, state):
    self.fieldlist.remove(state)

  def Rmlowercase(self, state):
    self.fieldlist.remove(state)

  def Rmuppercase(self, state):
    self.fieldlist.remove(state)

  def Rmpunctuation(self, state):
    self.fieldlist.remove(state)
  

# 文件内测试调用
if __name__ == '__main__':
  # 创建应用程序和对象
  app = QApplication(sys.argv)
  w = MyMainWindow(symbol['digital'], symbol['specSym'])
  print(w.genRandomSingle(10))
  w.show()
  sys.exit(app.exec_())

# class Example(QMainWindow):
#
#   def __init__(self):
#     super().__init__()
#
#     self.initUI()
#
#   def initUI(self):
#     btn1 = QPushButton("Button 1", self)
#     btn1.move(30, 50)
#
#     btn2 = QPushButton("Button 2", self)
#     btn3 = QPushButton("Button 2", self)
#     btn2.move(150, 50)
#
#     text = QTextEdit(self)
#
#     text.setGeometry(QtCore.QRect(40, 30, 281, 241))
#     text.setObjectName("textEdit")
#
#     btn2.move(350, 50)
#
#     btn1.clicked.connect(text.textChanged)
#     btn2.clicked.connect(self.buttonClicked)
#
#     self.statusBar()
#
#     self.setGeometry(300, 300, 590, 500)
#     self.setWindowTitle('Event sender')
#     self.show()
#
#   def buttonClicked(self):
#     sender = self.sender()
