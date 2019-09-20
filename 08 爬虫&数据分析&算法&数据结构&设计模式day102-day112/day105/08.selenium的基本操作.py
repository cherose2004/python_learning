from selenium import webdriver
from time import sleep
#实例化一个浏览器对象
bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\day04\chromedriver.exe')
url = 'https://www.jd.com/'
bro.get(url) #用户发起请求
#定位标签
search_input = bro.find_element_by_id('key')
#对指定标签进行数据交互
search_input.send_keys('macPro')

btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()
sleep(2)
#执行js代码
jsCode = 'window.scrollTo(0,document.body.scrollHeight)'
bro.execute_script(jsCode)

sleep(3)
bro.quit()