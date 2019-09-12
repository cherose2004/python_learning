# 静态文件存放路径
from aip import AipSpeech

MUSIC_PATH = "Music"
COVER_PATH = "Cover"
QRCODE_PATH = "QRcode"
CHAT_PATH = "Chat"

# 数据库配置
from pymongo import MongoClient

MC = MongoClient("localhost", 27017)
MongoDB = MC["Angela"]

# Redis
from redis import Redis
RDB = Redis("127.0.0.1",6379)


# 返回配置
RET = {
    "CODE": 0,
    "MSG": "",
    "DATA": {}
}

# 外部API接口
# 联图二维码接口
LT_URL = "http://qr.liantu.com/api.php?text=%s"
TL_URL = "http://openapi.tuling123.com/openapi/api/v2"
TL_DATA = {
    "perception": {
        "inputText": {
            "text": "文本内容"
        }
    },
    "userInfo": {
        "apiKey": "51ff3d2dd9464ba6bba97ff1bb9427ab",
        "userId": "替换成ToyId"
    }
}

# 百度AI - API

APP_ID = '16981685'
API_KEY = '9yjA1ijtDpy6SNzxOrsFFlns'
SECRET_KEY = 'o4GrQeXlUDWmGFefntxdU1cCKiVj9y3k'

AUDIO_CLIENT = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
VOICE = {
    'vol': 5,
    "spd": 4,
    "pit": 6,
    "per": 4
}
