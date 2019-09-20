# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from zjs_moviePro.items import ZjsMovieproItem
class MovieSpider(CrawlSpider):
    name = 'movie'
    conn = Redis(host='127.0.0.1',port=6379)
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567tv.tv/index.php/vod/show/id/6.html']

    rules = (#/index.php/vod/show/id/6/page/2.html
        Rule(LinkExtractor(allow=r'id/6/page/\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            name = li.xpath('./div/div/h4/a/text()').extract_first()
            detail_url = 'https://www.4567tv.tv'+li.xpath('./div/div/h4/a/@href').extract_first()
            ex = self.conn.sadd('movie_detail_urls',detail_url)
            if ex == 1:#向redis的set中成功插入了detail_url
                print('有最新数据可爬......')
                item = ZjsMovieproItem()
                item['name'] = name
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
            else:
                print('该数据已经被爬取过了！')
    def parse_detail(self,response):
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item['desc'] = desc

        yield item