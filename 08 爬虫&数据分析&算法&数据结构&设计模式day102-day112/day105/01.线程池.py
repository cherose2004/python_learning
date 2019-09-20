from multiprocessing.dummy import Pool
import requests
import time
#同步代码
# start = time.time()
# pool = Pool(3)
#
# urls = ['http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom']
# for url in urls:
#     page_text = requests.get(url).text
#     print(page_text)
# print('总耗时:',time.time()-start)

#异步代码
start = time.time()
pool = Pool(3)
urls = ['http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom']
def get_request(url):
    return requests.get(url).text

response_list = pool.map(get_request,urls)
print(response_list)

#解析
def parse(page_text):
    print(len(page_text))

pool.map(parse,response_list)
print('总耗时:',time.time()-start)