"""
    Created on 2020/6/8 13:04
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_16.py
    @Author         :  Frank
    @Description    :
    实现一个密码生成器，支持多种，字母、数字、特殊字符等多种组合。
    说明：这题类似于上周的优惠码生成，也是一个有实用场景的例子，相当于在那题的基础上面
    再扩充。
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import string
import random

def input_sel():
    while True:
        mode = int(input("""选择需要输入的密码模式：
        1.数字
        2.大小写字母
        3.特殊字符
        4.数字+大小写字母
        5.数字+特殊字符
        6.大小写字母+特殊字符
        7.三种模式混合:
        """))
        if mode in range(1, 8):
            break
    while True:
        len = int(input("需要生成的密码长度"))
        if len > 0:
            break
    return mode, len
    
def gen_passwd(mode, len):
    symbol = {'digital': string.digits, 'lowerLetter': string.ascii_letters, 'specSym': string.punctuation}
    str_src = ''
    passwd = ''
    if mode == 1:
        str_src = symbol['digital']
    if mode == 2:
        str_src = symbol['lowerLetter']
    if mode == 3:
        str_src = symbol['specSym']
    if mode == 4:
        str_src = symbol['digital']+symbol['lowerLetter']
    if mode == 5:
        str_src = symbol['digital']+symbol['specSym']
    if mode == 6:
        str_src = symbol['lowerLetter']+symbol['specSym']
    if mode == 7:
        str_src = symbol['digital']+symbol['lowerLetter']+symbol['specSym']
    passwd = ''.join(random.choices(str_src, k=len))
    return passwd

print(gen_passwd(*input_sel()))
