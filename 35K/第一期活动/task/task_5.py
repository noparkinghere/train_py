"""
    Created on 2020/5/18 14:28
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_5.py
    @Author         :  Frank
    @Description    :  编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…+1/n
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

def fun(num):
    """
    输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…+1/n
    :param num:
    :return:
    """
    res = 0
    if num % 2 == 0:
        for i in range(1, num+1):
            if i % 2 == 0:
                res += 1.0 / i
    else:
        for i in range(1, num+1):
            if i % 2 == 1:
                res += 1.0 / i
    return res

if __name__ == '__main__':
    print("计算结果为： %f" % fun(int(input("输入整数 n ："))))