"""
    Created on 2020/5/18 8:59
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_1.py.py
    @Author         :  Frank
    @Description    :  数字比较，输入 a，b 值，输出两者中多的那个值。
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

# 注意输入的为 str 类型
a = float(input("输入第一个值："))
b = float(input("输入第二个值："))

if a > b:
    print("较大的值是 a:%s", a)
elif a == b:
    print("a 和 b 相等，是 %s" % a)
else:
    print("较大的值是 b:%s", b)


