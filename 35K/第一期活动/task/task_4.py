"""
    Created on 2020/5/18 9:51
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_4.py
    @Author         :  Frank
    @Description    :  输入3个数a,b,c，按大小顺序输出。
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

num = 3
input_data = []
res = []

for i in range(num):
    input_data.append(float(input("输入第 %d 个数 ：" %(i+1))))

# 方法1，内置函数法
input_data.sort()

"""
# 方法2，冒泡排序
pos_x = len(input_data)-1
pos_y = 0
tmp = 0
while pos_x > 0:
    pos_y = 0
    while pos_y < pos_x:
        if (input_data[pos_y] > input_data[pos_y+1]):
            tmp = input_data[pos_y]
            input_data[pos_y] = input_data[pos_y+1]
            input_data[pos_y+1] = tmp
            
        pos_y += 1
    pos_x -= 1
"""


print("从大到小的排列顺序为：", end='\t')

for i in input_data:
    print(i, end='\t')
