from lxml import etree
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
#实例化一个浏览器对象
page_text_list = []
bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\day04\chromedriver.exe')
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
bro.get(url)
#如果定位的标签是存在于iframe对应的子页面中的话,在进行标签定位前一定要执行一个switch_to的操作
bro.switch_to.frame('iframeResult')
div_tag = bro.find_element_by_id('draggable')

#1.实例化动作链对象
action = ActionChains(bro)
action.click_and_hold(div_tag)

for i in range(5):
    #让动作链立即执行
    action.move_by_offset(17,0).perform()
    sleep(0.5)

action.release()

sleep(3)

bro.quit()