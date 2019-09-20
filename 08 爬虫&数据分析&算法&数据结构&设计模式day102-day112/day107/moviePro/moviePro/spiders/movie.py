# -*- coding: utf-8 -*-
import scrapy

from moviePro.items import MovieproItem
class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/class/动作/id/1.html']

    url = 'https://www.4567tv.tv/index.php/vod/show/class/动作/id/1/page/%d.html'
    pageNum = 1
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div[1]/a/@title').extract_first()
            detail_url = 'https://www.4567tv.tv'+li.xpath('./div[1]/a/@href').extract_first()
            item = MovieproItem()
            item['title'] = title
            #meta参数是一个字典，该字典就可以传递给callback指定的回调函数
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.pageNum < 5:
            self.pageNum += 1
            new_url = format(self.url%self.pageNum)
            yield scrapy.Request(new_url,callback=self.parse)

    def parse_detail(self,response):
        #接收meta：response.meta
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc
        yield item