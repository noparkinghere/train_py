"""
    Created on 2019/12/4 20:42
    ————————————————————————————————————————————————————————————————————
    @File Name      :  email_test.py
    @Author         :  Frank
    @Description    :
    
    ————————————————————————————————————————————————————————————————————
    @Change Activity:
  
"""


# 注意这个程序的文件名不能叫 email 否则无法导入这些库
# 注意腾讯云等邮箱使用了邮箱令牌需要手机申请授权码，替代密码
# import smtplib
from smtplib import SMTP_SSL                        # 邮件的协议，发送加密

# 构建邮件
# import email
from email.mime.text import MIMEText                # 邮件正文
from email.mime.multipart import MIMEMultipart      # 各部分组装邮件的主体
from email.header import Header                     # 邮件头


host_server = 'smtp.sina.com'  # sina 邮箱 smtp 服务器
sender_sina = 'pythonauto12@sina.com' # 发件人邮箱
pwd = 'python1234'  # 邮箱密码

sender_sina_mail = 'pythonauto12@sina.com' # 收件人邮箱
receiver = 'pythonauto12@sina.com'    # 接收人邮箱

mail_title = 'python 办公自动化'
mail_content = '你好，正式使用 python 自动化发送的一份邮件， 一份测试文件，感谢阅读'

msg = MIMEMultipart()  # 邮件主体
msg["Subject"] = Header(mail_title, 'utf-8')
msg['from'] = sender_sina_mail
msg['To'] = Header('测试邮箱', 'utf-8')
msg.attach(MIMEMultipart(mail_content, 'plain', 'utf-8'))  # 邮件正文内容加入主体中

# 登录
smtp = SMTP_SSL(host_server)
smtp.login(sender_sina, pwd)
smtp.sendmail(sender_sina_mail, receiver, msg.as_string())
smtp.quit()