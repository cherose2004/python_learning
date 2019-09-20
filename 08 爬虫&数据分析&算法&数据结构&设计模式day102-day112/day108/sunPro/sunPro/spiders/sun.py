# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem_second,SunproItem
#没有实现深度爬取：爬取的只是每一个页码对应页面中的数据
# class SunSpider(CrawlSpider):
#     name = 'sun'
#     # allowed_domains = ['www,xxx,com']
#     start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
#     #链接提取器
#     link = LinkExtractor(allow=r'type=4&page=\d+')
#     rules = (
#         #实例化一个Rule（规则解析器）的对象
#         Rule(link, callback='parse_item', follow=True),
#     )
#
#     def parse_item(self, response):
#         tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
#         for tr in tr_list:
#             title = tr.xpath('./td[2]/a[2]/@title').extract_first()
#             status = tr.xpath('./td[3]/span/text()').extract_first()
#
#             print(title,status)


#实现深度爬取
class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www,xxx,com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    #链接提取器
    link = LinkExtractor(allow=r'type=4&page=\d+')
    #http://wz.sun0769.com/html/question/201908/426393.shtml
    link_detail = LinkExtractor(allow=r'question/\d+/\d+\.shtml')
    rules = (
        #实例化一个Rule（规则解析器）的对象
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_detail'),
    )

    def parse_item(self, response):
        tr_list = response.xpath('//*[@id="morelist"]/div/table[2]//tr/td/table//tr')
        for tr in tr_list:
            title = tr.xpath('./td[2]/a[2]/@title').extract_first()
            status = tr.xpath('./td[3]/span/text()').extract_first()
            num = tr.xpath('./td[1]/text()').extract_first()
            item = SunproItem_second()
            item['title'] = title
            item['status'] = status
            item['num'] = num
            yield item

    def parse_detail(self,response):
        content = response.xpath('/html/body/div[9]/table[2]/tbody/tr[1]//text()').extract()
        content = ''.join(content)
        num = response.xpath('/html/body/div[9]/table[1]/tbody/tr/td[2]/span[2]/text()').extract_first()
        if num:
            num = num.split(':')[-1]
            item = SunproItem()
            item['content'] = content
            item['num'] = num
            yield item

