from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image #用作于图片的裁剪
from ChaoJiYing import Chaojiying_Client
from time import sleep
bro = webdriver.Chrome(executable_path=r'C:\Users\oldboy-python\Desktop\爬虫+数据\day04\chromedriver.exe')
bro.get('https://kyfw.12306.cn/otn/login/init')
sleep(5)
#验证码图片进行捕获(裁剪)
bro.save_screenshot('main.png')
#定位到了验证码图片对应的标签
code_img_ele = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
location = code_img_ele.location #验证码图片基于当前整张页面的左下角坐标
size = code_img_ele.size #验证码图片的长和宽
#裁剪的矩形区域(左下角和右上角两点的坐标)
rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))

i = Image.open('main.png')
frame = i.crop(rangle)
frame.save('code.png')

#使用打码平台进行验证码的识别
chaojiying = Chaojiying_Client('bobo328410948', 'bobo328410948', '899370')	#用户中心>>软件ID 生成一个替换 96001
im = open('code.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
result = chaojiying.PostPic(im, 9004)['pic_str']
print(result)#x1,y1|x2,y2|x3,y3  ==> [[x1,y1],[x2,y2],[x3,y3]]
all_list = []#[[x1,y1],[x2,y2],[x3,y3]] 每一个列表元素表示一个点的坐标,坐标对应值的0,0点是验证码图片左下角
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)

# action = ActionChains(bro)
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y).click().perform()
    sleep(1)

sleep(3)
bro.quit()





