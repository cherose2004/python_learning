import os

from aip import AipSpeech, AipNlp

""" 你的 APPID AK SK """
APP_ID = '16981685'
API_KEY = '9yjA1ijtDpy6SNzxOrsFFlns'
SECRET_KEY = 'o4GrQeXlUDWmGFefntxdU1cCKiVj9y3k'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    cmd_str = f"ffmpeg -y  -i {filePath}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm"
    os.system(cmd_str)
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

# 识别本地文件
res = client.asr(get_file_content('wyn.m4a'), 'pcm', 16000, {
    'dev_pid': 1536,
})

Q = res.get("result")[0]
print(Q)

# A = "我不知道你在说什么"
# if Q == "你的名字叫什么":
#     A = "我叫小猪武沛齐,哼哼哼"

A = "我不知道你在说什么"
if nlp_client.simnet(Q,"你的名字叫什么").get("score") >= 0.6:
    A = "我叫小猪武沛齐,哼哼哼"

else:
    # if nlp_client.simnet(Q,"今天天气怎么样").get("score") >= 0.6:
    #     A = "狂风暴雨,电闪雷鸣"

    # 问答机器人 - 图灵机器人

    tl_url = "http://openapi.tuling123.com/openapi/api/v2"

    import requests

    tl_data = {
        "perception": {
            "inputText": {
                "text": "北京今天天气怎么样"
            }
        },
        "userInfo": {
            "apiKey": "51ff3d2dd9464ba6bba97ff1bb9427ab",
            "userId": "123456789123"
        }
    }

    tl_data["perception"]["inputText"]["text"] = Q

    res = requests.post(tl_url,json=tl_data)

    res_json = res.json()
    A = res_json.get("results")[0].get("values").get("text")

print(A)


result = client.synthesis(A, 'zh', 1,
                          {
                              'vol': 5,
                              "spd": 4,
                              "pit": 6,
                              "per": 4
                          })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('Answer.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)


os.system("ffplay Answer.mp3")