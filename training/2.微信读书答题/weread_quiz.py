# encoding:utf-8

import requests
import base64
from PIL import ImageGrab, Image, ImageDraw
import os
import time

searchEngine = {'百度':"https://www.baidu.com/s?wd=", '搜狗':"https://www.sogou.com/web?query=" }

# tmpPos1 = (1442, 359, 1832, 455)
# tmpPos1 = (731, 345, 1185, 473)
tmpPos1 = (1440, 376, 1868, 505)
# tmpPos2 = (1442, 456, 1832, 790)
tmpPos2 = (440, 495, 868, 837)

def GetPic(pos=(1383, 433, 1826, 543), ans=tmpPos2):
  im = ImageGrab.grab(bbox=pos)
  im.save('new.png')
  im = ImageGrab.grab(bbox=ans)
  im.save('ans.png')

def DiffImg():
  # 二进制方式打开图片文件，新旧图片比对
  with open('old.png', 'rb') as f1:
    imgOld = base64.b64encode(f1.read())
  with open('new.png', 'rb') as f2:
    img = base64.b64encode(f2.read())
  if img == imgOld:
    # print("Success")
    return True
  else:
    # print("Fail")
    im = Image.open('new.png')
    draw = ImageDraw.Draw(im)
    im.save('old.png')
    return False


# client_id 为官网获取的AK， client_secret 为官网获取的SK
# 获取百度 AI 库的钥匙
def BaiduAIKey():
  host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XbWfYu0FpxSA3lnoqtrMVOmm&client_secret=mSxFQyp4xZDuhfn8vsGk7HZXk8rKPIr1'
  response = requests.get(host)
  if response:
    value = response.json()
    with open('key.txt', 'w') as f:
      f.write(response.content.decode('utf-8'))
    return value

# # 图片识别, 图片识别
def BaiduOCR(pic):
  request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
  with open(pic, 'rb') as f2:
    img = base64.b64encode(f2.read())
  params = {"image":img}
  # access_token = '[调用鉴权接口获取的token]'
  access_token = BaiduAIKey()["access_token"]
  request_url = request_url + "?access_token=" + access_token
  headers = {'content-type': 'application/x-www-form-urlencoded'}
  response = requests.post(request_url, data=params, headers=headers)
  if response:
    # print (response.json())
    # text = response.json()["words_result"][0]["words"]
    text = response.json()["words_result"]
    # with open('content.txt', 'w') as f:
    #   f.write(response.content.decode('utf-8'))
  return text


def QuizSearch(s):
  url = searchEngine[s]
  ans = []
  res = {}
  for i in BaiduOCR('new.png'):
    url += i["words"]
    # print(i)

  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
  }
  response = requests.get(url, headers=headers)
  quest = response.text

  for i in BaiduOCR('ans.png'):
    ans.append(i["words"])
    # print(ans)

  for i in ans:
    res[i] = quest.count(i)

  # print(res)

  max = 0
  tmp = 1
  pos = 0
  for i in res.values():
    if max < i:
      max = i
      pos = tmp
    tmp += 1

  print("选择结果是：" + str(pos))


  # 浏览器直接调用打开，人工浏览筛选
  # cmd = "start /B \"\" \"%s\" -kiosk %s" % ("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", url)
  # print (cmd)
  # os.system(cmd)


def fun():
  # 自动循环调用，截图比对检索
  # 存在一定的问题，vsor 投屏后同一张图会轻微的波动，出现比对的变化
  while True:
    # QuizSearch()
    time.sleep(0.5)
    GetPic(tmpPos1)
    if DiffImg() == True:
      time.sleep(0.1)
    else:
      QuizSearch('搜狗')
      
  # 手动按键调用检索
  
  # adb 手机截图比对检索


if __name__ == '__main__':
  # GetPic()  # 可以给出具体的坐标
  # DiffImg()
  # QuizSearch('搜狗')
  fun()


