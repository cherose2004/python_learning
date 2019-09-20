# -*- coding: utf-8 -*-
import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse)
    #基于终端指令的持久化存储操作
    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content-left"]/div')
    #     all_data = []
    #     for div in div_list:
    #         #scrapy中的xpath返回的列表的列表元素一定是Selector对象,我们最终想要的解析的
    #         #数据一定是存储在该对象中
    #         #extract()将Selector对象中data参数的值取出
    #         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         #列表直接调用extract表示的是将extract作用到每一个列表元素中
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data
    #基于管道的持久化存储
    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content-left"]/div')
    #     all_data = []
    #     for div in div_list:
    #         #scrapy中的xpath返回的列表的列表元素一定是Selector对象,我们最终想要的解析的
    #         #数据一定是存储在该对象中
    #         #extract()将Selector对象中data参数的值取出
    #         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         #列表直接调用extract表示的是将extract作用到每一个列表元素中
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #
    #         #将解析的数据存储到item对象
    #         item = QiubaiproItem()
    #         item['author'] = author
    #         item['content'] = content
    #
    #         #将item提交给管道
    #         yield item #item一定是提交给了优先级最高的管道类

    #将多个页码对应的页面数据进行爬取和解析的操作
    url = 'https://www.qiushibaike.com/text/page/%d/'#通用的url模板
    pageNum = 1
    #parse第一次调用表示的是用来解析第一页对应页面中的段子内容和作者
    def parse(self, response):
        div_list = response.xpath('//*[@id="content-left"]/div')
        all_data = []
        for div in div_list:
            # scrapy中的xpath返回的列表的列表元素一定是Selector对象,我们最终想要的解析的
            # 数据一定是存储在该对象中
            # extract()将Selector对象中data参数的值取出
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            # 列表直接调用extract表示的是将extract作用到每一个列表元素中
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            # 将解析的数据存储到item对象
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            # 将item提交给管道
            yield item  # item一定是提交给了优先级最高的管道类

        if self.pageNum <= 5:
            self.pageNum += 1
            new_url = format(self.url%self.pageNum)
            #手动请求(get)的发送
            yield scrapy.Request(new_url,callback=self.parse)




