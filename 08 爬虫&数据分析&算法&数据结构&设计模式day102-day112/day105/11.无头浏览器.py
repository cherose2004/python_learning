from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#实例化一个浏览器对象
bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\day04\chromedriver.exe',chrome_options=chrome_options)
bro.get('https://www.baidu.com')
sleep(2)
bro.save_screenshot('1.png')
print(bro.page_source)
sleep(2)
bro.quit()