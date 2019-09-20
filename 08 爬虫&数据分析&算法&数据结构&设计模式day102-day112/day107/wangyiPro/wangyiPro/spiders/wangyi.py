# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com']
    five_model_urls = []
    bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\tools\chromedriver.exe')
    #用来解析五个板块对应的url，然后对其进行手动请求发送
    def parse(self, response):
        model_index = [3,4,6,7,8]
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        for index in model_index:
            li = li_list[index]
            #获取了五个板块对应的url
            model_url = li.xpath('./a/@href').extract_first()
            self.five_model_urls.append(model_url)
            #对每一个板块的url进行手动i请求发送
            yield scrapy.Request(model_url,callback=self.parse_model)
    #解析每一个板块页面中的新闻标题和新闻详情页的url
    #问题：response（不满足需求的response）中并没有包含每一个板块中动态加载出的新闻数据
    def parse_model(self,response):
        div_list = response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            if detail_url:
                item = WangyiproItem()
                item['title'] = title
                #对详情页发起请求解析出新闻内容
                yield scrapy.Request(detail_url,callback=self.parse_new_content,meta={'item':item})
    def parse_new_content(self,response): #解析新闻内容
        item = response.meta['item']
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)

        item['content'] = content

        yield item

    #最后执行
    def closed(self,spider):
        self.bro.quit()