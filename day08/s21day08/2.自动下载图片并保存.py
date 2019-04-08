#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
# 1. python模拟浏览器向 https://www.autohome.com.cn/news/ 发送请求
r1 = requests.get('https://www.autohome.com.cn/news/')

# 2. 去字符串中找我想要的东西（先将二进制转换成字符串）
data = r1.content.decode('gb2312')

soup = BeautifulSoup(data,features='html.parser')
container = soup.find(id='auto-channel-lazyload-article')

li_list = container.find_all(name='li')
for item in li_list:
    tag = item.find(name='h3')
    if not tag:
        continue
    img_url = "https:"+item.find(name='img').get('src')
    print(item.find(name='h3').text,img_url)
    print('==========================')







