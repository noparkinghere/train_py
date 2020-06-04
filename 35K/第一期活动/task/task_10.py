"""
输入 n 个学生（用户输入），用户一次全部输入一组学习信息（包含：学号、姓名、性别、语文成绩、数学成绩、英语成绩）有 n 个学生就输入 n 条信息，将所有信息保存到一个 txt 文件中。
"""

num = int(input("输入学生个数："))

stu_items = ['学号', '姓名', '性别', '语文成绩', '数学成绩', '英语成绩']
data = [[]]

for i in range(num):
    data.append([])
    for j in stu_items:
        data[i].append(input("请输入第%d个学生的%s信息:"%(i+1, j)))
    print('')

with open('stu_data.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(stu_items)+'\n')
    

with open('stu_data.txt', 'a', encoding='utf-8') as f:
    for i in range(num):
        f.write(','.join(data[i])+'\n')