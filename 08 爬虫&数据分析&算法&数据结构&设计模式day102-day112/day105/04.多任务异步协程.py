import asyncio
from time import sleep
import time
start = time.time()
urls = [
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo',
    'http://localhost:5000/bobo'
]
#在待执行的代码块中不可以出现不支持异步模块的代码
#在该函数内部如果有阻塞操作必须使用await关键字进行修饰
async def get_request(url):
    print('正在请求:',url)
    await asyncio.sleep(2)
    print('请求结束:',url)
    return 'hello bobo'

tasks = [] #放置所有的任务对象
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start)