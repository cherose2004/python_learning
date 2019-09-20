# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import  ImagesPipeline
import scrapy
# class ImgproPipeline(object):
#     def process_item(self, item, spider):
#         return item
class ImgproPipeline(ImagesPipeline):

    #对某一个媒体资源进行请求发送
    #item就是接收到的spider提交过来的item
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    #制定媒体数据存储的名称
    def file_path(self, request, response=None, info=None):
        name = request.url.split('/')[-1]
        print('正在下载：',name)
        return name

    #将item传递给下一个即将给执行的管道类
    def item_completed(self, results, item, info):
        return item

