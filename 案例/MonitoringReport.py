#! /usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

Mail_Host = "smpt.163.com"
Mail_User = "monitoringdevops@163.com"
Mail_Pass = "123456Qww"

Sender = "monitoringdevops@163.com"
Receivers = "961363629@qq.com"

Messages = MIMEText("Python邮件发送测试...","plain","UTF-8")
Messages["From"] = Header("菜鸟教程","UTF-8")
Messages["To"] = Header("测试","UTF-8")

Subject = "Python SMTP邮件测试"
Messages["Subject"] = Header(Subject,"UTF-8")

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(Mail_Host,25)
    smtpObj.login(Mail_User,Mail_Pass)
    smtpObj.sendmail(Sender,Receivers,Messages.as_string())
    print("邮件发送成功!")
except smtplib.SMTPException:
    print("无法发送邮件!")


