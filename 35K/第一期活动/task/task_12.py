"""
    Created on 2020/6/2 15:08
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_12.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import re

pattern = r"(.*?)\<\/a\>.*\"\"\>(.*?)\<\/td\>.*\<span\>(.*?)\<\/span\>.*class\=\"tag\"\>(.*?)\<\/span\>.*tag\-\-.+?\"\>(.*?)\<\/span\>.*tag\-\-.+?\"\>(.*?)\<\/span\>"

def get_mem_info(input_str):
    global pattern
    handle_list = []
    handle_str = input_src.split('<th key="was_checkin_remind"')[1].split('<ul unselectable="unselectable"')[0]
    handle_list += handle_str.split('class="nickname">')[1:]
    items = ['小组成员', '贡献值', '组龄', '打卡率', '昨天打卡情况', '今天打卡情况']
    res = []
    for i,e1 in enumerate(handle_list):
        search_content = re.search(pattern, e1, re.S)
        res.append({})
        for j,e2 in enumerate(items):
            res[i][e2] = search_content.group(j+1).strip()
    return res
    

if __name__ == '__main__':
    with open("task_12.html", 'r', encoding='utf-8') as f:
        input_src = f.read()
    for i in get_mem_info(input_src):
        print(i)
    
    
    