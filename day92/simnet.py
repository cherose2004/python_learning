from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '16981685'
API_KEY = '9yjA1ijtDpy6SNzxOrsFFlns'
SECRET_KEY = 'o4GrQeXlUDWmGFefntxdU1cCKiVj9y3k'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

res = client.simnet("你叫什么名字","你的名字叫什么")
print(res.get("score"))
