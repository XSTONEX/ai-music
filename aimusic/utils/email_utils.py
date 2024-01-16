# -*- coding:utf-8 -*-
import socks
import smtplib
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER = "sqwstone123@gmail.com"
ACCOUNT_INFO = {'username': "sqwstone123@gmail.com", 'password': 'fprmngkcyyhoirbu'}


def send_mail(receivers, subject, text, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, sender=SENDER, account_info=ACCOUNT_INFO):
    """
    :param receivers:接收邮箱列表
    :param subject:发送邮件主题
    :param text:发送邮件正文
    :param filename:发送邮件附件
    :param smtp_server:smtp服务器地址
    :param smtp_port:smtp TLS/STARTTLS 端口
    :param sender:发送者
    :param account_info:发送者邮箱账号密码
    :return:
    """

    # 正文
    msg_root = MIMEMultipart()    # 创建一个带附件的实例
    msg_root['SUBJECT'] = subject
    msg_root['To'] = COMMASPACE.join(receivers)
    msg_text = MIMEText(text, 'html', 'utf-8')
    msg_root.attach(msg_text)

    # 附件
    # att = MIMEApplication(open(filename,'rb').read())
    # att.add_header('Content-Disposition', 'attachment', filename=filename)
    # msg_root.attach(att)
    # 增加socks5代理
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'x.x.x.x', 29900, True)
    # socks.wrapmodule(smtplib)

    smtp = smtplib.SMTP(f'{smtp_server}:{smtp_port}')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(account_info['username'], account_info['password'])
    smtp.sendmail(sender, receivers, msg_root.as_string())
    smtp.close()


if __name__=="__main__":
    send_mail(["2179837317@qq.com"], "test email", "love you")
