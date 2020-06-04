"""
    Created on 2020/5/27 11:52
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_8.py
    @Author         :  Frank
    @Description    :  按照你喜欢的格式来打印九九乘法表。
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

print("九九乘法表：")
for i in range(1, 10):
    for j in range(1, i+1):
        print("%dx%d=%d" % (j, i, i*j), end='\t')
    print('')
