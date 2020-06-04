# 统计打卡情况：

import re
from collections import Counter

pattern = r"[0-9]{1,2}\.\ (.*)"
mem_list = []
res = {}

with open("打卡统计.txt", 'r', encoding='utf-8') as f:
    in_file = f.read()
    print(re.findall(r"\n[0-9]{1,2}.*", in_file))
    for i in re.findall(r"\n[0-9]{1,2}.*", in_file):
        # print(i.split()[1])
        mem_list.append(i.split()[1])
        
# print(Counter(mem_list).most_common)

for i in mem_list:
    res[i] = 0

for i in mem_list:
    res[i] += 1

for k in res:
    print("%s 本周打开天数为：%d" %(k, res[k]))

print("*"*10)
