from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16981685'
API_KEY = '9yjA1ijtDpy6SNzxOrsFFlns'
SECRET_KEY = 'o4GrQeXlUDWmGFefntxdU1cCKiVj9y3k'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('消息已成功发送', 'zh', 1,
                          {
                              'vol': 5,
                              "spd": 4,
                              "pit": 6,
                              "per": 4
                          })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    print(result)
    with open('SendOK.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)