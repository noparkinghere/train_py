"""
    Created on 2020/5/25 22:03
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_6.py
    @Author         :  Frank
    @Description    :  猜数字游戏：随机选择一个三位以内的数字作为答案。
    用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import random

num = random.randint(0, 999)

usr_input = int(input("输入你的数字："))

while num != usr_input:
    if num > usr_input:
        print("输入数据太小")
    else:
        print("输入数据太大")
    usr_input = int(input("输入你的数字："))

else:
    print("恭喜，你猜中了！")
