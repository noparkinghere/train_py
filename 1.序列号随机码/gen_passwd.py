import collections
import string
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from my_gui import Ui_MainWindow

symbol = {'digital': string.digits, 'lowerLetter': string.ascii_lowercase,
          'upperLetter': string.ascii_uppercase, 'specSym': string.punctuation}


class MyMainWindow(QMainWindow, Ui_MainWindow):
  field = ''
  fieldlist = []

  def genRandomSingle(self, num):
    rand_data = ''.join(random.choices(self.field, k=num))
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
    self.pushButton.clicked.connect(self.gen)

  def gen(self):
    if self.checkBox.checkState()  == Qt.Checked:
      self.AddField(symbol['digital'])
    if self.checkBox_2.checkState() == Qt.Checked:
      self.AddField(symbol['lowerLetter'])
    if self.checkBox_3.checkState() == Qt.Checked:
      self.AddField(symbol['upperLetter'])
    if self.checkBox_4.checkState() == Qt.Checked:
      self.AddField(symbol['specSym'])
    if self.checkBox.checkState() == Qt.Unchecked:
      self.RmField(symbol['digital'])
    if self.checkBox_2.checkState() == Qt.Unchecked:
      self.RmField(symbol['lowerLetter'])
    if self.checkBox_3.checkState() == Qt.Unchecked:
      self.RmField(symbol['upperLetter'])
    if self.checkBox_4.checkState() == Qt.Unchecked:
      self.RmField(symbol['specSym'])
      
    if self.checkBox.checkState() == Qt.Unchecked \
        and self.checkBox_2.checkState() == Qt.Unchecked \
        and self.checkBox_3.checkState() == Qt.Unchecked \
        and self.checkBox_4.checkState() == Qt.Unchecked:
      QMessageBox.critical(self, '严重错误', '至少需要勾选一种字符！')
    else:
      self.field = ''.join(self.fieldlist)
      self.textEdit.setText(self.genRandomSingle(self.spinBox.value()))
    
  def AddField(self, state):
    if state not in self.fieldlist:
      self.fieldlist.append(state)

  def RmField(self, state):
    if state in self.fieldlist:
      self.fieldlist.remove(state)

  
# 文件内测试调用
if __name__ == '__main__':
  # 创建应用程序和对象
  app = QApplication(sys.argv)
  w = MyMainWindow(symbol['digital'], symbol['specSym'])
  # print(w.genRandomSingle(10))
  w.show()
  sys.exit(app.exec_())
