"""
    Created on 2020/1/8 15:46
    ————————————————————————————————————————————————————————————————————
    @File Name      :  main.py.py
    @Author         :  Frank
    @Description    :
    应用场景：厂家促销搞优惠券。为你的应用生成激活码（或者优惠券）
    任务要求：使用 Python 随机生成 200 个类似（1f32d-232xx-dsfw2-fjsk30）这种形式的 激活码
    （或者优惠券），将其保存在 coupon.txt 文件中，要求每行一个优惠券号。
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import random
import string

field = string.ascii_letters + string.digits

def gen_code(cnt):
  """
  产生单段字符如：0b7cc
  :param cnt:
  :return:
  """
  # res = ''
  # for i in range(cnt):
  #   res += random.choice(field)
  res = ''.join(random.choices(field, k=cnt))
  return res

def gen_arr_code(cnt):
  """
  产生多组字符，存到一个列表中
  :param cnt:
  :return:
  """
  res = [gen_code(5) for i in range(cnt)]
  return res
  
def gen_coupon():
  """
  用 - 链接所有字符
  :param cnt:
  :return:
  """
  res = '-'.join(gen_arr_code(4))
  return res


if __name__=='__main__':
  print(gen_coupon())