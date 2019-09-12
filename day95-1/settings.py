# 目录相关配置
AVATAR_PATH = "Avatar"
RECO_PATH = "Reco"

# 数据库配置
# MongoDB
from pymongo import MongoClient
MC = MongoClient("127.0.0.1",27017)
MongoDB = MC["WuLiaoApp"]


# 返回协议
RET = {
    "code":0,
    "msg":"",
    "data":[]
}

