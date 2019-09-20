import asyncio
import requests
import time
start = time.time()
urls = [
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo'
]
#无法实现异步的效果:是因为requests模块是一个不支持异步的模块
async def req(url):
    page_text = requests.get(url).text
    return page_text

tasks = []
for url in urls:
    c = req(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start)