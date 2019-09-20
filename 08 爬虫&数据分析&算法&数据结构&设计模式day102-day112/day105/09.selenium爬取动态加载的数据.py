from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象
page_text_list = []
bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\day04\chromedriver.exe')
url = 'http://125.35.6.84:81/xk/'
bro.get(url)
sleep(2)
#page_source返回的就是当前浏览器打卡页面对应的页面源码数据
page_text = bro.page_source
page_text_list.append(page_text)


for i in range(2):
    bro.find_element_by_id('pageIto_next').click()
    sleep(2)
    page_text = bro.page_source
    page_text_list.append(page_text)

for page_text in page_text_list:
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        name = li.xpath('./dl/@title')[0]
        print(name)


sleep(3)
bro.quit()