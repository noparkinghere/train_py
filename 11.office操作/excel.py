"""
    Created on 2019/12/4 9:14
    ————————————————————————————————————————————————————————————————————
    @File Name      :  excel.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import xlrd
import xlwt
xlsx = xlrd.open_workbook("1w.xls")
table = xlsx.sheet_by_index(0)
print(table.cell_value(5, 1))
print(table.cell(5, 1).value)

new_work = xlwt.Workbook()
worksheet = new_work.add_sheet("111")
worksheet.write(0, 0, 'test')
new_work.save("位置.xls")
