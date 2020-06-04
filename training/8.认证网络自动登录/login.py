import json
# -- coding : UTF-8
import os
import random
import re
import time

import requests
from set_random_mac import SetMacAddr

IP_ADDR = "192.168.2."
WEB_GATE = '192.168.2.1'

class IntAuthLogin:
  outVisit = 'ping www.baidu.com'
  inVisit = "ping "+ WEB_GATE
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Host': '114.114.114.114:90',
    'If-None-Match': "3387953655",
    'Connection': 'keep - alive',
  }

  def __init__(self):
    pass
  
  def log(self, content):
    with open('log', 'a+') as f:
      out = time.asctime()+'***'+content+'\n'
      f.write(out)
      print(out)
  
  def VisitSite(self):
    url = 'http://114.114.114.114:90/p/30247dd99271a6806206be0598a1cf9e/index.html?d3d3LmdzdGF0aWMuY29tL2dlbmVyYXRlXzIwNA=='
    r = requests.get(url, headers=self.headers)
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
    print(res)
    if re.search('字节=.+时间=.+TTL=.+', res) is None:
    # if re.search(r'无法访问目标主机|传输失败|请求超时', res) is not None:
      # print(res)
      return False
    else:
      # print(res)
      return True
      print("内网工作正常！")
    
  def SetNet(self):
    try:
      if not self.IsVisitable(self.inVisit):
        """
          内网访问判断
        """
        self.log("内网异常")
        a = SetMacAddr()
        mac = a.genMacAddr()
        self.log("更换 mac 地址："+mac)
        # 更换 MAC 地址
        a.setAddr(mac=mac)
        # 重启无线网卡，系统更新 mac 地址
        os.system("netsh interface set interface wlan0 disabled")
        os.system("netsh interface set interface wlan0 enabled")
        # 载入无线网的配置文件
        os.system("netsh wlan add profile filename=\"wlan0-YANFA.xml\"")
        while True:
          if re.search('字节=.+时间=.+', os.popen(self.inVisit).read()) is None:
            print(os.popen('ipconfig /all').read()\
              .split('以太网适配器 eth0:')[0].split('无线局域网适配器 wlan0:')[1]\
              .split('IPv4 地址')[1].split('首选')[0])
            os.system("netsh interface ip set address \"wlan0\" static "+IP_ADDR+""\
                      + str(random.choice(range(123, 255))) + " 255.255.255.0 " + WEB_GATE + " 1")
            os.system("netsh interface ip set dns \"wlan0\" static 8.8.8.8")
            time.sleep(3)
          else:
            print("内网配置成功！")
            break
            
        time.sleep(3)
        self.VisitSite()
        self.LoginSite()
        print("内网外网配置完成！")
  
      elif requests.get('http://www.baidu.com').headers.__contains__('Connection') == False:
        """
          外网访问判断
        """
        self.log("外网异常")
        self.VisitSite()
        self.LoginSite()
        print("外网配置完成！")
      else:
        self.log("所有网络连接正常")
    except ConnectionResetError:
      print("远程主机强迫关闭了一个现有的连接。")


if __name__ == '__main__':
  cnt = 0
  while True:
  # while cnt != 1000:
    a = IntAuthLogin()
    a.SetNet()
    # print(cnt)
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
