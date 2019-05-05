#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Page:
    def __init__(self, total_count, current_page, per_page_count=10):
        self.total_count = total_count
        self.per_page_count = per_page_count
        self.current_page = current_page
    @property
    def start_index(self):
        return (self.current_page - 1) * self.per_page_count
    @property
    def end_index(self):
        return self.current_page * self.per_page_count


USER_LIST = []
for i in range(321):
    USER_LIST.append('alex-%s' % (i,))

# 请实现分页展示：
current_page = int(input('请输入要查看的页码：'))
p = Page(321, current_page)
data_list = USER_LIST[p.start_index:p.end_index]
for item in data_list:
    print(item)