# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from redis import Redis
class QiubaiproPipeline(object):
    fp = None
    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('qiushibaike.txt','w',encoding='utf-8')

    #使用来接收爬虫文件提交过来的item,然后将其进行任意形式的持久化存储
    #参数item:就是接收到的item对象
    #该方法每接收一个item就会调用一次
    def process_item(self, item, spider):
        author = item['author']
        content= item['content']

        self.fp.write(author+':'+content+'\n')
        return item #item是返回给了下一个即将被执行的管道类

    def close_spider(self,spider):
        print('结束爬虫!')
        self.fp.close()

#负责将数据存储到mysql
class MysqlPL(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123',db='spider',charset='utf8')
        print(self.conn)
    def process_item(self,item,spider):
        author = item['author']
        content = item['content']

        sql = 'insert into qiubai values ("%s","%s")'%(author,content)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class RedisPL(object):
    conn = None
    def open_spider(self,spider):
        self.conn = Redis(host='127.0.0.1',port=6379)
        print(self.conn)
    def process_item(self,item,spider):
        self.conn.lpush('all_data',item)
        #注意:如果将字典写入redis报错:pip install -U redis==2.10.6

