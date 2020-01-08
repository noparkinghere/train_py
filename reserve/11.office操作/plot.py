"""
    Created on 2019/12/4 20:22
    ————————————————————————————————————————————————————————————————————
    @File Name      :  plot.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

import matplotlib.pyplot as plt

# 用于正常显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

date = ['2018/7/21', '2018/7/22', '2018/7/23', '2018/7/24', '2018/7/25', '2018/7/26', '2018/7/27', '2018/7/28']
hebei = range(len(date))
shaxi = [1,2,4,45,6,7,8,2]

# 折线图
plt.plot(date, hebei, color='red', label="河北")
plt.plot(date, shaxi, color='red', label="山西")
plt.title("每日入库对比")
plt .xlabel("日期")
plt .xlabel("车次")

plt.legend()
plt.show()

# 柱状图
plt.bar(date, hebei, color='red', label="河北")
plt.bar(date, shaxi, color='red', label="山西")
plt.legend()
plt.show()

# 饼图
number = [666, 543]
province = ['山西', '河北']
colors = ['#999fff', '#fff999']
plt.pie(x=number, labels=province, colors=colors)
plt.legend()
plt.show()
