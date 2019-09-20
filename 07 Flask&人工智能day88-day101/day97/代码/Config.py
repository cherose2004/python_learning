# 静态文件存放路径
MUSIC_PATH = "Music"
COVER_PATH = "Cover"
QRCODE_PATH = "QRcode"


# 数据库配置
from pymongo import MongoClient
MC = MongoClient("localhost",27017)
MongoDB = MC["Angela"]


# 返回配置
RET = {
    "CODE":0,
    "MSG":"",
    "DATA":{}
}


# 外部API接口
# 联图二维码接口
LT_URL = "http://qr.liantu.com/api.php?text=%s"