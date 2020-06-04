'''
慎用，会直接对 windows 的注册表操作，测试不充分，在不同的电脑上可能会造成意向不到的后果
需要通过 ipconfig -all 查看网卡描述信息，逐个和 4D36E972-E325-11CE-BFC1-08002BE10318
中目录下的 DriverDesc 值进行对比，找到自己需要配置的网卡是哪个
这边我的无线网卡通过比对在 0013 中。
'''

import string
import random
import os


delRegCmd = r'reg delete HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0013\ /v NetworkAddress /f'
queRegCmd = r'reg query HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0013\ /v NetworkAddress '
AddRegCmd = r'reg add HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0013\ /v NetworkAddress /t REG_SZ /d '

'''
改类负责随机生成合法可用的 mac 地址
mac 地址例如："16B936405872"
'''
class GenSerialNum():
  field = string.digits + 'ABCDEF'
  secField = ('2', '6', 'A', 'E')

  def genRandomSingle(self, num, field=field):
    rand_data = ''.join(random.sample(field, num))
    return rand_data

  def genMacAddr(self):
    res = self.genRandomSingle(1) + self.genRandomSingle(1, field=self.secField) + self.genRandomSingle(10)
    return res

# 文件内测试调用
if __name__ == '__main__':
  a = GenSerialNum()
  mac = a.genMacAddr()
  os.system(delRegCmd)
  os.system(AddRegCmd+mac)
  print(mac)




