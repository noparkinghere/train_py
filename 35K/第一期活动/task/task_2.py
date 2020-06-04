"""
    Created on 2020/5/18 9:45
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_2.py.py
    @Author         :  Frank
    @Description    :  统计 1 到 100 之和。
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

res = 0
for i in range(1, 100+1):
    res += i
    
print("累加结果为：%d" % res)
