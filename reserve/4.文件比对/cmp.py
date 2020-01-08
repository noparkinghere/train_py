import hashlib
import sys

from my_gui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication


class MyMainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super(MyMainWindow, self).__init__(parent)
    self.setupUi(self)
    # 设置信号与槽
    self.CreateSignalSlot()
    self.textBrowser.insertPlainText('显示输出结果：')
    cursor = self.textBrowser.textCursor()
    pos = len(self.textBrowser.toPlainText())
    cursor.setPosition(pos)
    self.textBrowser.insertPlainText('\n')
  
  def cmp(self):
    with open(self.lineEdit.text(), 'rb') as f:
      i1 = f.read()
    with open(self.lineEdit_2.text(), 'rb') as f:
      i2 = f.read()
    md1 = hashlib.md5()
    md1.update(i1)
    cmp1 = md1.hexdigest()
    print(cmp1)
    self.showcase(cmp1)
    md2 = hashlib.md5()
    md2.update(i2)
    cmp2 = md2.hexdigest()
    print(cmp2)
    self.showcase(cmp2)
    if cmp2 == cmp1:
      print("两文件相同")
      self.showcase("两文件相同")
    else:
      print("两文件不相同")
      self.showcase("两文件不相同")

  def showcase(self, str):
    self.textBrowser.insertPlainText(str)
    cursor = self.textBrowser.textCursor()
    pos = len(self.textBrowser.toPlainText())
    cursor.setPosition(pos)
    self.textBrowser.ensureCursorVisible()
    self.textBrowser.setTextCursor(cursor)
    self.textBrowser.insertPlainText('\n')
    
  def CreateSignalSlot(self):
    self.pushButton.clicked.connect(self.openfile1)
    self.pushButton_2.clicked.connect(self.openfile2)
    self.pushButton_3.clicked.connect(self.cmp)
    
  def openfile1(self):
    openfile_name1 = QFileDialog.getOpenFileName(self, '选择文件', '', 'files(*)')
    self.lineEdit.setText(openfile_name1[0])
    print(self.lineEdit.text())
    
  def openfile2(self):
    openfile_name2 = QFileDialog.getOpenFileName(self, '选择文件', '', 'files(*)')
    self.lineEdit_2.setText(openfile_name2[0])
    print(self.lineEdit_2.text())

if __name__ == '__main__':
  # RemoveAllFilesBg('.')
  app = QApplication(sys.argv)
  w = MyMainWindow()
  # w.
  w.show()
  sys.exit(app.exec_())

#
# src = 'adsglaskdfjklsdfgdfgddggd'
# mnew = hashlib.md5()
# mnew.update(src.encode('utf8'))
# print(mnew.hexdigest())
