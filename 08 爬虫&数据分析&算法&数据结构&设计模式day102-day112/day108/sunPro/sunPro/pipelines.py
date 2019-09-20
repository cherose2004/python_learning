# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SunproPipeline(object):
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'SunproItem':
            content = item['content']
            num = item['num']
            print(content,num)
        else:
            title = item['title']
            status = item['status']
            num = item['num']

            print(title,status,num)
        return item
