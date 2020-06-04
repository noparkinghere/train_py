import string
import random

class GenSerialNum():
  field = string.digits + string.ascii_letters

  def genRandomSingle(self, num):
    rand_data = ''.join(random.sample(self.field, num))
    return rand_data

  def genRandomCode(self, len, num):
    res = '-'.join([self.genRandomSingle(num) for i in range(len)])
    return res

# 文件内测试调用
if __name__ == '__main__':
  a = GenSerialNum()
  print(a.genRandomCode(10, 10))