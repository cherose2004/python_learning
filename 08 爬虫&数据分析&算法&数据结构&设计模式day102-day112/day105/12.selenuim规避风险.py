# -*- coding: utf-8 -*-
# __author__ = "maple"


from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

#实例化一个浏览器对象
bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\day04\chromedriver.exe',options=option)
bro.get('https://www.taobao.com/')

