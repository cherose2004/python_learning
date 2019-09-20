# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '17164366'
API_KEY = 'iwypmYNvMzwPgG3BKlV093an'
SECRET_KEY = 'btKA8A0ODRHGdfTUCZuZZARBjUPvqMia'
class WangyiproPipeline(object):
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    def process_item(self, item, spider):
        title = item['title']
        title = title.replace(u'\xa0',u' ')
        content = item['content']
        content = content.replace(u'\xa0',u' ')
        wd_dic = self.client.keyword(title, content)
        tp_dic = self.client.topic(title, content)
        print(wd_dic,tp_dic)
        return item
