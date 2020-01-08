"""
    Created on 2019/12/16 16:45
    ————————————————————————————————————————————————————————————————————
    @File Name      :  filter.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""
import re


def fun():
  with open("test1.txt", 'r+') as f:
    text = f.read()
  res = ''
  i = 0
  

  # while i < len(text):
  #   """
  #     手动筛选实现法
  #   """
  #   if text[i] == '<':
  #     while text[i] != '>':
  #       i += 1
  #     else:
  #       i += 1
  #   else:
  #     res += text[i]
  #     i += 1
  
  # 正则方法一步解决
  res = re.sub(r'\<.*?\>', '\n', text)
  
  with open("test2.txt", 'w+') as f:
    f.write(res)


fun()
