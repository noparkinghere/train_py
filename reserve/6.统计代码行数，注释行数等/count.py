import re

'''
  筛选出两种情况表示注释：
  1. 前面有任意多的空格，之后以 \'\'\' 为开始的段，且需要找到 \'\'\' 的结尾
    1.1 判断从本行开始往后中是否找到 \'\'\' 为终止
  2. \'\'\' 为开始的段， \'\'\' 为的结尾的单行注释
  2. 前面有任意多的空格， 之后以 # 为起始的行
'''

fileName = 'gen_code.txt'

def cnt():
  commentLines = 0
  allLines = 0
  with open(fileName, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  allLines = len(lines)
  
  # 当需要计数器灵活变化的时候，用 while 而不用 for
  pos = 0
  while pos < allLines:
    # 单行注释
    if re.search(r'^\s*#', lines[pos]) is not None:
      commentLines += 1
    # 单行注释
    elif re.match(r'^\s*\'\'\'.+\'\'\'\s*$', lines[pos]) is not None:
      commentLines += 1
    # 多行注释
    elif re.search(r'^\s*\'\'\'', lines[pos]) is not None:
      commentLines += 1
      pos += 1
      while re.search(r'\'\'\'\s*$', lines[pos]) is None:
        commentLines += 1
        pos += 1
      else:  # 多行注释结尾
        commentLines += 1
        pass
    pos += 1

  return allLines, commentLines

if __name__ == '__main__':
  try:
    a, b = cnt()
    print(a)
    print(b)
  except:
    print("注释存在错误")