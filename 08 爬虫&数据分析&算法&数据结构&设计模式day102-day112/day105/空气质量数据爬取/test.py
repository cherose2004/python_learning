import execjs
import requests
node = execjs.get()

# Params
method = 'GETDETAIL'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'

# Compile javascript
file = 'js.js'
ctx = node.compile(open(file,encoding='utf-8').read())

# Get params
js = 'getPostParamCode("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)
# print(params)


url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
pm = {
    'd':params
}
#text就是请求到的加密的响应数据
text = requests.post(url,data=pm).text

js = 'decodeData("{0}")'.format(text)
data = ctx.eval(js)
print(data)