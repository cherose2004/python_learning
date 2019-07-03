#!/usr/bin/env python
# -*- coding:utf-8 -*-

msg = MIMEText('导演，我想演男一号，你想怎么着都行。', 'plain', 'utf-8')
msg['From'] = formataddr(["李奇航", 'mercury047@126.com'])
msg['To'] = formataddr(["导演", '344522251@qq.com'])
msg['Subject'] = "情爱的导演"


server = smtplib.SMTP("smtp.126.com", 25)
server.login("mercury047@126.com", "liqihang19970416")
server.sendmail('mercury047@126.com', ['344522251@qq.com', ], msg.as_string())
server.quit()