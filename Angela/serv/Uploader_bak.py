import os
import time

from bson import ObjectId
from flask import Blueprint, jsonify, send_file, request
from Config import RET, MongoDB, COVER_PATH, MUSIC_PATH, CHAT_PATH

uploader = Blueprint("uploader", __name__)


@uploader.route("/app_uploader", methods=["POST"])
def app_uploader():
    # 接收app 传递的参数

    # user_id == sender  to_user = receiver
    # 通过 user_list 子集查询 $all  可以获取到 当前的聊天窗口 如果查询的话,会将所有的聊天数据全部查询到,能不能不查询直接更新数据呢?

    # chat_window = MongoDB.Chats.find_one({"user_list": {"$all": user_list}})
    # print(chat_window)

    # 获取文件数据 request.files

    # 保存文件 .amr

    # amr 浏览器无法播放  转换成 MP3 - ffmpeg -i amr mp3

    # 删除 amr 的原始文件

    # 创建聊天记录信息 MongoDB数据存储结构文档中查询

    # 更新chat_list 数据

    # RET 响应数据 api文档

    # filename 是 转换后的 mp3 文件


    # 问题
    # 直接返回消息 会导致用户体验极差
    # 将直接播放消息,改为间接手动播放消息 消息提醒
    # 语音合成消息提醒 思考问题: 你有未读消息 - 你有来自xx的消息  - xx 怎么获得呢?  - xx 是用户昵称吗?
    # 文件名称 最终返回值


    RET["CODE"] = 0
    RET["MSG"] = "上传成功"
    RET["DATA"] = {}

    return jsonify(RET)


@uploader.route("/toy_uploader", methods=["POST"])
def toy_uploader():
    print(request.form.to_dict())
    print(request.files)

    # 查询聊天窗口 - 没有chat_id ?


    # 文件数据 保存 - 没有文件名 (uuid)


    # chat_list = {}


    # RET 返回值
    # JSON:
    ret = {
        "code": 0,
        "msg": "上传成功",
        "data":
            {
                "filename": "filename",
                "friend_type": "app"
            }
    }


    return jsonify(ret)
