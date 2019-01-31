from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
msg = MIMEText('this is test by python! please do not reply', 'plain', 'utf-8')
msg['From'] = _format_addr('kinghao<%s>' % from_addr)
msg['To'] = _format_addr('zhangsan<%s>' % to_addr)
msg['Subject'] = Header('this is test', 'utf-8').encode()
# 输入SMTP地址
smtp_server = 'smtp.qq.com'
import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()