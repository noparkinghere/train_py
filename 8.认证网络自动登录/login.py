import json
# -- coding : UTF-8
import os
import re
import time

import requests
from set_random_mac import SetMacAddr


class IntAuthLogin:
  outVisit = 'ping www.baidu.com'
  inVisit = 'ping 192.168.18.1'
  
  def __init__(self):
    pass
  
  def VisitSite(self):
    url = 'http://114.114.114.114:90/p/30247dd99271a6806206be0598a1cf9e/index.html?d3d3LmdzdGF0aWMuY29tL2dlbmVyYXRlXzIwNA=='
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
      'Host': '114.114.114.114:90',
      'If-None-Match': "3387953655",
      'Connection': 'keep - alive',
    }
    r = requests.get(url, headers=headers)
    # print(r.request.headers)
    # with open('tmp1.html', 'w') as f:
    #   f.write(r.content.decode('utf-8'))
  
  def LoginSite(self):
    postUrl = 'http://114.114.114.114:90/login'
    s = requests.Session()  # 为了保存登入信息
    PayloadData = {
      'terminal': 'pc',
      'login_type': 'login',
      'username': 'guest',
      'password1': '123456',
      'password':'%B9x%FB%1A%9D%5C',
    }
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Origin': "http://114.114.114.114:90",
      'Referer': "http://114.114.114.114:90/p/30247dd99271a6806206be0598a1cf9e/index.html?d3d3LmdzdGF0aWMuY29tL2dlbmVyYXRlXzIwNA==",
    }
    # 注意这边不用 json.dumps(PayloadData)，这个地址提交的并不是 json
    r = s.post(postUrl, data=PayloadData, headers=headers)
    # print(r.content.decode('utf-8'))
    
    # with open('tmp2.html', 'w') as f:
    #   f.write(r.content.decode('utf-8'))
  
  def IsVisitable(self, visit):
    res = os.popen(visit).read()
    if re.search(r'无法访问目标主机|传输失败', res) is not None:
      print(res)
      return False
    else:
      # print(res)
      return True
    
  def SetNet(self):
    if not self.IsVisitable(self.inVisit):
      print("内网异常")
      a = SetMacAddr()
      mac = a.genMacAddr()
      print(mac)
      # 更换 MAC 地址
      a.setAddr(mac=mac)
      # 重启无线网卡，系统更新 mac 地址
      os.system("netsh interface set interface wlan0 disabled")
      os.system("netsh interface set interface wlan0 enabled")
      # 载入无线网的配置文件
      os.system("netsh wlan add profile filename=\"wlan0-YANFA.xml\"")
      time.sleep(2)
      os.system("netsh interface ip set address \"wlan0\" static 192.168.18.123 255.255.255.0 192.168.18.1 1")
      os.system("netsh interface ip set dns \"wlan0\" static 8.8.8.8")
      time.sleep(5)
      self.VisitSite()
      self.LoginSite()
    elif not requests.get('http://www.baidu.com').headers.__contains__('Connection'):
      print("外网异常")
      self.VisitSite()
      self.LoginSite()
    else:
      print("所有网络连接正常")


if __name__ == '__main__':
  cnt = 0
  while True:
  # while cnt != 1:
    a = IntAuthLogin()
    a.SetNet()
    print(cnt)
    cnt += 1
    with open('record', 'w') as f:
      content = '第 ' + str(cnt) + ' 次自动登录！'
      f.write(content)
    time.sleep(10)

'''
参考链接：https://www.jianshu.com/p/50f5e1fa11b3
netsh wlan add profile filename="wlan0-YANFA.xml"
netsh wlan delete profile name="YANFA"
netsh wlan export profile key=clear


netsh interface ip set address "本地连接" static 192.168.0.1 255.255.255.0 192.168.0.254 1
netsh interface ip set dns "本地连接" static 202.194.40.1
'''
