"""
SMTP发送邮件
"""
from email.mime.text import MIMEText  # 构建纯文本邮件
import getpass

mail_msg = MIMEText('hello python', 'plain', 'utf-8')

# 发送邮件
from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
# 输入SMTP地址
smtp_server = 'smtp.qq.com'
import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], mail_msg.as_string())
server.quit()

