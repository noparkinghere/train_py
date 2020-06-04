"""
    Created on 2019/12/20 14:21
    ————————————————————————————————————————————————————————————————————
    @File Name      :  record.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""
import csv
import os
import string
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from UI_record import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
  readdata = {'desp':'', 'money':''}
  data = []
  file_name = "output.csv"
  
  def __init__(self, *args, parent=None):
    super(MyMainWindow, self).__init__(parent)
    self.setupUi(self)

    # 设置信号与槽
    self.CreateSignalSlot()
    self.InitDataFile(self.file_name, ['描述', '金额'])
    
  def CreateSignalSlot(self):
    self.pushButton.clicked.connect(self.opt)
    
    
  def readalldata(self, filename):
    with open(filename, 'r') as f:
      reader = csv.reader(f)
      # rows = [row for row in reader]    # 必须转换下 reader 才行
      rows = list(reader)
    # if
    self.data = [float(row[1]) for row in rows[1:]]  # 去除文件头部分
    
  def opt(self):
    self.readdata['desp'] = self.text_desp.toPlainText()
    self.readdata['money'] = self.line_cash.text()
    if self.readdata['money'] == '':
      self.readdata['money'] = '0'
    self.text_desp.clear()
    self.line_cash.clear()
    self.SaveDataToCSV(self.file_name, [self.readdata['desp'], self.readdata['money']])
    self.readalldata(self.file_name)
    res = 0
    for i in self.data:
      res += i
    self.line_all.setText(str(res))


  def InitDataFile(self, fileName, value=[]):
    if not os.path.exists(fileName):
      with open(fileName, 'w+', newline="") as f:
        write = csv.writer(f)
        write.writerow(value)
  
  def SaveDataToCSV(self, fileName, value):
    with open(fileName, 'a+', newline="") as f:
      write = csv.writer(f)
      write.writerow(value)

if __name__ == '__main__':
  # 创建应用程序和对象
  app = QApplication(sys.argv)
  w = MyMainWindow()
  w.show()
  sys.exit(app.exec_())