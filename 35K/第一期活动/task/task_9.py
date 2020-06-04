"""
    Created on 2020/5/28 21:04
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_9.py
    @Author         :  Frank
    @Description    :
    厂家促销搞优惠券。为你的应用生成激活码（或者优惠券），使用 Python
    随机生成 200 个类似（1f32d-232xx-dsfw2-fjsk30）这种形式的 ，
    激活码（或者优惠券），将其保存在 coupon.txt 文件中，要求每行一个优惠券号
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import random
import string

random_src = string.digits+string.ascii_letters

# print(random.choices(random_src, k=5))

def gen_coupon(arr, cnt):
    """
    arr : 代表组，表示有 arr-1 个 -
    cnt ：表示每组是多少个字符
    """
    return '-'.join([''.join(random.choices(random_src, k=cnt)) for i in range(arr)])

def gen_n_coupon(num, arr, cnt):
    """
    num : 共生成 num 组优惠码
    arr : 代表组，表示有 arr-1 个 -
    cnt ：表示每组是多少个字符
    """
    ret = ''
    for i in range(num):
        ret += gen_coupon(arr, cnt)+'\n'
    print(ret)
    return ret

data = gen_n_coupon(200, 4, 5)
print(data)
with open('coupon.txt', 'a') as f:
    f.write(data)