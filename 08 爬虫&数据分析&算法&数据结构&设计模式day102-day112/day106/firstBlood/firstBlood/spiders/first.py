# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称:爬虫文件的唯一标识(在spiders子目录下是可以创建多个爬虫文件)
    name = 'first'
    #允许的域名
    # allowed_domains = ['www.baidu.com']
    #起始的url列表:列表中存放的url会被scrapy自动的进行请求发送
    start_urls = ['https://www.baidu.com/','https://www.sogou.com/']
    #用作于数据解析:将start_urls列表中对应的url请求成功后的响应数据进行解析
    def parse(self, response):
        print(response)
