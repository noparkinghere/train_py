"""
    Created on 2020/6/3 10:10
    ————————————————————————————————————————————————————————————————————
    @File Name      :  task_14.py
    @Author         :  Frank
    @Description    :
    ### 题干
    应用场景：娱乐整蛊，头像换成有微信未读信息的头像
    将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果，不用太注重细节，只要求位置和大小相似即可，图片尺寸要求为 300*300
    ### 思路分析
    使用 PIL 这种基础通用的图形处理库，算法实现很简单，只要会使用 PIL 中几个基础的库函数就可以完成这道题。
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""

from PIL import Image, ImageFont, ImageDraw


def handle_img():
    image = Image.open('0.png')
    w, h = image.size
    font = ImageFont.truetype('arial.ttf', 50)
    draw = ImageDraw.Draw(image)
    draw.text((4 * w / 5, h / 5), '5', fill=(255, 10, 10), font=font)
    image.save('0.0.png', 'png')
    

if __name__ == '__main__':
    handle_img()



