# -*- coding: utf-8 -*-
import scrapy
from imgPro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/daxuemeinv/']
    url = 'http://www.521609.com/daxuemeinv/list8%d.html'
    pageNum = 1
    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_src = 'http://www.521609.com'+li.xpath('./a[1]/img/@src').extract_first()
            item = ImgproItem()
            item['src'] = img_src

            yield item

        # if self.pageNum < 3:
        #     self.pageNum += 1
        #     new_url = format(self.url%self.pageNum)
        #     yield scrapy.Request(new_url,callback=self.parse)