import json
from ftplib import FTP
import os

class FTP_Opetate():
  # 参考网址 https://blog.csdn.net/ouyang_peng/article/details/79271113
  
  def __init__(self):
    self.ftp = FTP()
    with open('../../config', 'r') as f:
      ftp_list = json.loads(f.read())
    print(ftp_list)
    
    self.ftp.connect(ftp_list['35k']['ip'])  # 使用默认端口 21
    self.ftp.login(ftp_list['35k']['account'], ftp_list['35k']['password'])
    print(self.ftp.getwelcome())
  
    # self.ftp.mlsd()
    self.ftp.dir()
    a = next(self.ftp.mlsd())
    print(a)
    # 上传文件
    # fp = open('download/.gitignore', 'rb')
    # cmd = 'STOR test_dir/.gitignore'
    # ftp.storbinary(cmd, fp)
    # ftp.mkd('test_dir') #新建远程目录
    
    # 删除文件
    # ftp.delete('test_dir/.gitignore') #删除远程文件
    # ftp.rmd('test_dir') #删除远程非空目录
  
  
  # 递归下载所有文件以及文件中子文件的内容
  def downrecallfiles(self, ftpPath ='.', savePath ='../../download'):
    # fileList = ftp.nlst()
    retDir = '..'
    filesDetail = []
    self.ftp.cwd(ftpPath)
    self.ftp.dir(filesDetail.append)
  
    for i in os.listdir(savePath[0:savePath.find(savePath.split('/')[-1])]):
      if i == savePath.split('/')[-1]:
        os.chdir(savePath)  # 迁移到指定目录
        break
    else:
      os.mkdir(savePath)
      os.chdir(savePath)  # 迁移到指定目录
  
    for i in self.ftp.mlsd():
      if i[1]['type'] == 'dir':    # 如果是目录则递归进入遍历查找
        self.downrecallfiles(i[0], './'+i[0])  # 递归下载所有文件夹中的文件
      else:
        print(i)
        with open(i[0].encode('iso-8859-1').decode('utf-8'), 'wb') as fileHandler:
          self.ftp.retrbinary('RETR %s' %i[0], fileHandler.write) # 下载文件
        pass
  
    self.ftp.cwd(retDir)  # ftp 返回上册目录
    os.chdir(retDir)    # 本地返回上层目录
    
  def EndFtp(self):
    self.ftp.quit()  # 退出ftp服务器


# downrecallfiles()
    # ftp.set_debuglevel(0)


# print([i.encode('iso-8859-1').decode('utf-8') for i in fileList])     # 注意 ftp 默认用的 'iso-8859-1' 编码方式
# a = []
# ftp.dir('Archive', a.append)
# print(a)
#
# for i in fileList:
#   # ftp.cwd('xxx/xxx/')
#   with open('download/'+i.encode('iso-8859-1').decode('utf-8'), 'wb') as file_handle:
#     if i != 'Archive':
#       print(i)
#       # ftp.retrbinary('RETR %s' %i, file_handle.write) # 下载文件
#       pass
#   # ftp.set_debuglevel(0)

if __name__=='__main__':
  obj1 = FTP_Opetate()
  obj1.downrecallfiles()
  obj1.EndFtp()

