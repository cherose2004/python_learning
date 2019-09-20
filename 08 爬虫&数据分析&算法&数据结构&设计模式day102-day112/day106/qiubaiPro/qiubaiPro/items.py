# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiproItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field() #Field可以将其理解成是一个万能的数据类型
    content = scrapy.Field()
