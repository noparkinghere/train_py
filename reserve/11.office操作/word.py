"""
    Created on 2019/12/4 9:14
    ————————————————————————————————————————————————————————————————————
    @File Name      :  word.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""
from xlutils.copy import copy
import xlrd
import xlwt

tem_excel = xlrd.open_workbook('2019.xls', formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()
font = xlwt.Font()
font.name = "微软雅黑"
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
style.alignment = alignment

new_sheet.write(20, 5, "我知道", style)
new_sheet.write(20, 6, "2222", style)
new_sheet.write(21, 5, "2222", style)
new_sheet.write(22, 5, "2222", style)
new_excel.save("2019_1.xls")