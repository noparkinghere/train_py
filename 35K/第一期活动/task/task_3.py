"""
    Created on 2020/5/18 9:48
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_3.py.py
    @Author         :  Frank
    @Description    :  在"skdjflajowuerjlxcvjuoiufjxcuv"，中找出 j 出现的次数。
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

input = 'skdjflajowuerjlxcvjuoiufjxcuv'
find_char = 'j'
cnt = 0

for i in input:
    if i == 'j':
        cnt += 1

print("工找到 %s 出现的次数为 %d 次" % (find_char, cnt))