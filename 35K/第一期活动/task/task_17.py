"""
    Created on 2020/6/8 15:14
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_17.py
    @Author         :  Frank
    @Description    :
    敏感词文本文件 task_17_filtered_words.txt，里面的内容为以下内容，则变成 *（*号与字母个数对应） ，否则打印出原文。
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

def filter(word, src):
    for i in word.split():
        src = src.replace(i, '*'*len(i))
    return src

if __name__ == '__main__':
    with open("task_17_filter_test.txt", 'r', encoding='utf-8') as f:
        test_file = f.read()
    with open("task_17_filtered_words.txt", 'r', encoding='utf-8') as f:
        filter_words = f.read()
    with open("task_17_filter_file.txt", 'w', encoding='utf-8') as f:
        f.write(filter(filter_words, test_file))
        print(filter(filter_words, test_file))