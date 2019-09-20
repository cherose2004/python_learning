#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import re

def parser_page(par,content):
    res = par.finditer(content)
    for i in res:
        yield {'id': i.group('id'),
               'title': i.group('title'),
               'score': i.group('score'),
               'com_num': i.group('comment_num')}

def get_page(url):
    ret = requests.get(url)
    return  ret.text

def write_file(file_name):
    with open(file_name,mode = 'w',encoding='utf-8') as f:
        while True:
            dic = yield
            f.write('%s\n' % json.dumps(dic, ensure_ascii=False))

pattern = '<div class="item">.*?<em class="">(?P<id>\d+)</em>.*?<span class="title">(?P<title>.*?)</span>.*?' \
              '<span class="rating_num".*?>(?P<score>.*?)</span>.*?<span>(?P<comment_num>.*?)人评价</span>'
par = re.compile(pattern,flags=re.S)
num = 0
f = write_file('move2')
next(f)
for i in range(10):
    content = get_page('https://movie.douban.com/top250?start=%s&filter=' % num)
    g = parser_page(par,content)
    for dic in g:
        f.send(dic)
    num += 25
f.close()


# def func():
#     print(123)
#     n = yield 'aaa'
#     print('-->',n)
#     yield 'bbb'
#
# g = func()
# print(g)
# n = next(g)
# print(n)
# print('-'*20)
# next(g)   # g.send('uysdfhfoiusyg')




