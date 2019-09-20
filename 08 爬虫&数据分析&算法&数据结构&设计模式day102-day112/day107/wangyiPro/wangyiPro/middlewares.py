# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from time import sleep
from scrapy import signals
from scrapy.http import HtmlResponse


class WangyiproDownloaderMiddleware(object):

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):#spider就是爬虫文件中爬虫类实例化的对象
        #进行所有响应对象的拦截
        #1.将所有的响应中那五个不满足需求的响应对象找出
            #1.每一个响应对象对应唯一一个请求对象
            #2.如果我们可以定位到五个响应对应的请求对象后，就可以通过该i请求对象定位到指定的响应对象
            #3.可以通过五个板块的url定位请求对象
            #总结： url==》request==》response

        #2.将找出的五个不满足需求的响应对象进行修正（替换）
        #spider.five_model_urls:五个板块对应的url
        bro = spider.bro
        if request.url in spider.five_model_urls:
            bro.get(request.url)
            sleep(1)
            page_text = bro.page_source #包含了动态加载的新闻数据
            #如果if条件程利则该response就是五个板块对应的响应对象
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            return new_response


        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
