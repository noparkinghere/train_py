"""
    Created on 2020/6/3 10:10
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_15.py
    @Author         :  Frank
    @Description    :
    ### 题干
    分析仓库根目录的 words.txt 文件里的词频，按照出现频率由高到低排列结果，
    不区分大小写，过滤掉标点（可以使用正则表达式）。结果类似ok：234，
    play：122，funny：78
    ### 思路分析
    具备实际应用场景的一种操作，大家如果想要做词频统计的话，可以在这题上面
    进一步完善。推荐使用正则表达式，使用正则进行筛选的话，可以让这边的
    操作非常简单。
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import re

with open("task_15_test.txt", 'r') as f:
    find_res = re.findall(r'[a-zA-Z]+', f.read())

res_dict = {}
for i in find_res:
    if i not in res_dict:
        res_dict[i] = 1
    else:
        res_dict[i] += 1
print(res_dict)
key=lambda s:s[5]
print(sorted(res_dict.items(), key=lambda s:s[1], reverse=True))

