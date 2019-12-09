# Requires "requests" to be installed (see python-requests.org)
import random
import time

import numpy
import requests
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog
from my_gui import Ui_Form
from PIL import Image
import cv2 as cv


class MyMainWindow(QMainWindow, Ui_Form):
  path = ''
  key = '9fwbrTfbKfFVtpy9NGN5zeRG'
  def __init__(self, parent=None):
    super(MyMainWindow, self).__init__(parent)
    self.setupUi(self)
    self.col = QColor(255, 255, 255)
    self.frame.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())
    self.path = './pic'
    # 设置信号与槽
    self.CreateSignalSlot()
  
  def CreateSignalSlot(self):
    self.comboBox.currentIndexChanged.connect(self.ChColor)
    self.lineEdit.textEdited.connect(self.chKey)
    # self.pushButton.clicked.connect(self.openfile)
    self.pushButton_2.clicked.connect(self.RemoveAllFilesBg)
    
  def chKey(self):
    self.key = self.lineEdit.text()
    print("当前秘钥为：{1}".format(self.key))

  # def openfile(self):
  #   try:
  #     openfile_name = QFileDialog.getOpenFileNames(self, '选择文件', '', 'files()')
  #     # print(openfile_name)
  #     self.path = openfile_name[0]
  #     self.lineEdit.setText(self.path[0])
  #   except:
  #     self.path = '.'

  def ChColor(self):
    if self.comboBox.currentIndex() == 0:
      self.col = QColor(255, 255, 255)
    if self.comboBox.currentIndex() == 1:
      self.col = QColor(211, 4, 4)
    if self.comboBox.currentIndex() == 2:
      self.col = QColor(0, 0, 0)
    if self.comboBox.currentIndex() == 3:
      self.col = QColor(28, 4, 211)
    if self.comboBox.currentIndex() == 4:
      self.col = QColor(242, 150, 31)
    if self.comboBox.currentIndex() == 5:
      self.col = QColor(193, 31, 242)
    if self.comboBox.currentIndex() == 6:
      self.col = QColor(0, 127, 125)
      
    self.frame.setStyleSheet("QWidget { background-color: %s }" %
                               self.col.name())

  def RemoveBg(self, fileName, key):
    saveFile = fileName.split('.')[0] + '_rm.' + fileName.split('.')[-1]
    response = requests.post(
      'https://api.remove.bg/v1.0/removebg',
      files={'image_file': open(fileName, 'rb')},
      data={'size': 'auto'},
      headers={'X-Api-Key': key},
    )
    if response.status_code == requests.codes.ok:
      with open(saveFile, 'wb') as out:
        out.write(response.content)
        print("sucess")
        self.label_2.setText("处理成功")
        im = Image.open(saveFile, mode='r')
        print(saveFile)
        return saveFile
    else:
     print("Error:", response.status_code, response.text)
  
  def ChgBg(self, fileName, bg):
    saveFile = fileName.split('.')[0] + '_mod.' + fileName.split('.')[-1]
    im = cv.imread(fileName)
    for i in range(im.shape[0]):
      for j in range(im.shape[1]):
        if (im[i, j] == numpy.array([0, 0, 0])).all():
          im[i, j] = bg
    # cv.imshow("Noize", im)
    cv.imwrite(saveFile, im)
    
  def RemoveAllFilesBg(self):
    # 判断是否是文件夹
    if os.path.isdir(self.path):
      print(self.path)
      os.chdir(self.path)
      files = os.listdir(os.getcwd())
      for i in files:
        if os.path.splitext(i)[-1] == '.png' or os.path.splitext(i)[-1] == '.jpg':
          print("start")
          self.ChgBg(self.RemoveBg(i), self.col.getRgb()[:3], self.key)
      
if __name__ == '__main__':
  # RemoveAllFilesBg('.')
  app = QApplication(sys.argv)
  w = MyMainWindow()
  # w.
  w.show()
  sys.exit(app.exec_())