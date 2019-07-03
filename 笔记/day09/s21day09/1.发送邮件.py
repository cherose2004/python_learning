#!/usr/bin/env python
# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('导演，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
msg['From'] = formataddr(["李邵奇", '15776556369@163.com'])
msg['To'] = formataddr(["导演", '344522251@qq.com'])
msg['Subject'] = "情爱的导演"

server = smtplib.SMTP("smtp.163.com", 25)
server.login("15776556369@163.com", "qq1105400511")
server.sendmail('15776556369@163.com', ['344522251@qq.com', ], msg.as_string())
server.quit()