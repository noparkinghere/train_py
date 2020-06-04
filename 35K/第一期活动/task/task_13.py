"""
    Created on 2020/6/3 9:57
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_13.py
    @Author         :  Frank
    @Description    :
    一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.
    编程找出1000以内的所有完数。
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

def find_digit(num):
    res = []
    for i in range(2, num+1):
        tmp = 0
        for j in range(1, (i+1)//2+1):
            if i % j == 0:
                tmp += j
        if tmp == i:
            res.append(i)
    return res

if __name__ == '__main__':
    print(find_digit(1000))
    

