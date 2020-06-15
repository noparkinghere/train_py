"""
    Created on 2020/6/9 20:40
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_18-20.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import re
import xlrd
import xlwt

class ConvertDate(object):
    def __init__(self):
        pass
    
    @classmethod
    def date_convert(cls, in_date):
        pass

       

class MemStatistics(object):
    
    def __init__(self, input_data):
        self.input_data = input_data
        self.date_data = []         # 过滤出来的基础数据，需要进一步整理
        self.pattern_date = r"【Day ([0-9]{1,2}) ([0-9]{1}月[0-9]{1,2}日)】"
        self.pattern_mem = r"[0-9]{1}\.\ (.*)"
        
    def filter_data(self):
        """
        简单地清洗出数据，统计出每天的打卡成员
        :return:
        """
        for i,e in enumerate(self.input_data.split("#接龙")[1:]):
            self.date_data.append({})
            tmp = re.search(self.pattern_date, e)
            self.date_data[i]['日期'] = tmp.group(2)
            self.date_data[i]['第几天'] = tmp.group(1)
            self.date_data[i]['当日打卡用户'] = re.findall(self.pattern_mem, e)
        # print(self.date_data)
        
    def get_mem_data(self):
        """
        数据筛选，获取有哪些成员
        :return:
        """
        user = []
        for i in self.date_data:
            for j in i["当日打卡用户"]:
                if j not in user:
                    user.append(j)
        # print(user)
        return user

    def find_n_sub_str(self, src, sub, pos, start):
        index = src.find(sub, start)
        if index != -1 and pos > 0:
            return self.find_n_sub_str(src, sub, pos - 1, index + 1)
        return index
    
    def insert_str(self, src, sub, pos):
        tmp = list(src)
        tmp.insert(pos, sub)
        return ''.join(tmp)
    
    def gen_mem_stat(self, save_file):
        """
        生成成员打卡数据统计
        :return:
        """
        self.col_1 = "成员"+','
        for i,e in enumerate([i["日期"] for i in self.date_data]):
            self.col_1 += e+','
            if i > 1 and (i+1) % 7 == 0:
                self.col_1 += '考察情况'+','
        with open(save_file, 'w', encoding='utf-8') as f:
            f.write(self.col_1+'\n')
        # print(self.get_mem_data())
        # print(self.date_data)
        for i in self.get_mem_data():
            mem_check = []
            for j in self.date_data:
                if i in j["当日打卡用户"]:
                    mem_check.append('√')
                else:
                    mem_check.append('×')
            cnt = 0
            col_mem = i+','
            for j,e in enumerate(mem_check):
                col_mem += e+','
                if e == '√':
                    cnt += 1
                
                if j > 1 and (j + 1) % 7 == 0:
                    if cnt >= 5:
                        col_mem += '合格'+','
                    else:
                        col_mem += '不合格'+','
                if (j + 1) % 7 == 0:
                    cnt = 0
            col_mem += '\n'
            # print(col_mem)
            with open(save_file, 'a', encoding='utf-8') as f:
                f.write(col_mem)

    def setStyle(self, name, height, color, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
    
        font = xlwt.Font()  # 为样式创建字体
        # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
        font.name = name
        # 设置字体颜色
        font.colour_index = color
        # 字体大小
        font.height = height
        # 定义格式
        style.font = font
    
        return style
    
    def covert_excel(self, input_data, out_file, sheet):
        with open(input_data, "r", encoding='utf-8') as f:
            input_data = f.read()
            print(input_data)
        self.new_work = xlwt.Workbook()
        format = self.setStyle('Times New Roman', 200, 47, False)
        self.worksheet = self.new_work.add_sheet(sheet)

        for i,e1 in enumerate(input_data.split('\n')[:-1]):
            # 创建一个样式----------------------------
            # 为指定单元格设置样式
            tmp = 40    # 临时记录扣款
            for j,e2 in enumerate(e1.split(',')):
                if i == 0:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 22; font: bold on')
                elif e2 == "×":
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 45; font: bold on')
                elif e2 == "√":
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 42; font: bold on')
                elif e2 == '不合格':
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 53; font: bold on')
                    tmp -= 10
                elif e2 == '合格':
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 50; font: bold on')
                else:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 44; font: bold on')
                if j == 0:
                    self.worksheet.write(i, j, e2, style)
                else:
                    self.worksheet.write(i, j+1, e2, style)
            else:
                if i == 0:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 22; font: bold on')
                    self.worksheet.write(0, 1, "所剩余额", style)
                else:
                    style = xlwt.easyxf('pattern: pattern solid, fore_colour 52; font: bold on')
                    self.worksheet.write(i, 1, tmp, style)

        self.new_work.save(out_file)


if __name__ == '__main__':
    with open("打卡统计.txt", 'r', encoding='utf-8') as f:
        tmp = f.read()
    test_ob = MemStatistics(tmp)
    test_ob.filter_data()
    test_ob.get_mem_data()
    test_ob.gen_mem_stat("打卡统计.csv")
    test_ob.covert_excel("打卡统计.csv", "打卡统计.xls", "打卡统计")
    
    
    
    