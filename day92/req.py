import requests

#模拟发起HTTP请求 8

res = requests.get("http://www.baidu.com")
requests.post(json={"k":"v"})
print(res.text)