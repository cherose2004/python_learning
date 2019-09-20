import asyncio
import requests
import time
import aiohttp
from lxml import etree
urls = [
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
]
#无法实现异步的效果:是因为requests模块是一个不支持异步的模块
async def req(url):
    async with aiohttp.ClientSession() as s:
        async with await s.get(url) as response:
            #response.read():byte
            page_text = await response.text()
            return page_text

    #细节:在每一个with前面加上async,在每一步的阻塞操作前加上await

def parse(task):
    page_text = task.result()
    tree = etree.HTML(page_text)
    name = tree.xpath('//p/text()')[0]
    print(name)
if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = req(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(parse)
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time()-start)