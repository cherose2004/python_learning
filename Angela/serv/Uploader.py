import os
import time
from uuid import uuid4

from bson import ObjectId
from flask import Blueprint, jsonify, send_file, request

from BaiduAi import text2audio, my_nlp_lowB, audio2text
from Config import RET, MongoDB, COVER_PATH, MUSIC_PATH, CHAT_PATH, AUDIO_CLIENT
from redis_msg import set_msg

uploader = Blueprint("uploader", __name__)


@uploader.route("/app_uploader", methods=["POST"])
def app_uploader():
    app_info = request.form.to_dict()
    # 接收app 传递的参数

    # user_id == sender  to_user = receiver
    # 通过 user_list 子集查询 $all  可以获取到 当前的聊天窗口 如果查询的话,会将所有的聊天数据全部查询到,能不能不查询直接更新数据呢?
    user_list = [app_info.get("user_id"), app_info.get("to_user")]

    # chat_window = MongoDB.Chats.find_one({"user_list": {"$all": user_list}})
    #
    # print(chat_window)

    # 获取文件数据 request.files

    # 保存文件 .amr

    # amr 浏览器无法播放  转换成 MP3 - ffmpeg -i amr mp3

    # 删除 amr 的原始文件

    # 创建聊天记录信息 MongoDB数据存储结构文档中查询

    # 更新chat_list 数据

    # RET 响应数据 api文档

    # filename 是 转换后的 mp3 文件
    file = request.files.get("reco_file")
    file_path = os.path.join(CHAT_PATH, file.filename)
    file.save(file_path)

    os.system(f"ffmpeg -i {file_path} {file_path}.mp3")
    os.remove(file_path)

    print(app_info, file)

    chat_info = {
        "from_user": app_info.get("user_id"),
        "to_user": app_info.get("to_user"),
        "chat": f"{file.filename}.mp3",
        "createTime": time.time()
    }

    MongoDB.Chats.update_one({"user_list": {"$all": user_list}},{"$push":{"chat_list":chat_info}})

    set_msg(app_info.get("user_id"), app_info.get("to_user"))


    # 替换返回值中的filename 可以以让toy 播放不同的内容
    # "Nolic.mp3" 替换成 "你有一条未读消息.MP3"
    # xxtx = text2audio("你有一条未读消息") # 没有提示 是谁的消息?

    # 从users表中查询 user_id 用户 - 用户的 nickname
    # 1.nickname 姓名 不能直呼长辈姓名
    # 2.如果发消息的 user_id 是 Toy

    # 收取语音消息的 永远是玩具
    remark = "小伙伴"
    toy = MongoDB.Toys.find_one({"_id":ObjectId(app_info.get("to_user"))})
    for friend in toy.get("friend_list"):
        if friend.get("friend_id") == app_info.get("user_id"):
            remark = friend.get("friend_remark")

    xxtx = text2audio(f"收到来自{remark}的新消息")

    RET["CODE"] = 0
    RET["MSG"] = "上传成功"
    RET["DATA"] = {
        "filename": xxtx,
        "friend_type": "app"
    }

    return jsonify(RET)


@uploader.route("/toy_uploader", methods=["POST"])
def toy_uploader():
    toy_info = request.form.to_dict()
    print(toy_info)
    reco = request.files.get("reco")

    # 查询聊天窗口 - 没有chat_id ?


    # 文件数据 保存 - 没有文件名 (uuid)

    filename = f"{uuid4()}.wav"
    filepath = os.path.join(CHAT_PATH,filename)
    reco.save(filepath)

    chat_list = {
        "from_user": toy_info.get("user_id"),
        "to_user": toy_info.get("to_user"),
        "chat": filename,
        "createTime": time.time()
    }

    user_list = [toy_info.get("user_id"), toy_info.get("to_user")]

    MongoDB.Chats.update_one({"user_list": {"$all": user_list}}, {"$push": {"chat_list": chat_list}})
    set_msg(toy_info.get("user_id"),toy_info.get("to_user"))

    # 获取自己的好友类型 app / toy
    if MongoDB.Toys.find_one({"_id":ObjectId(toy_info.get("user_id"))}):
        friend_type = "toy"
    else:
        friend_type = "app"

    # 合成语音提示 - 接收语音消息必须是toy
    if toy_info.get("friend_type") == "toy":
        remark = "小伙伴"
        toy = MongoDB.Toys.find_one({"_id": ObjectId(toy_info.get("user_id"))})
        for friend in toy.get("friend_list"):
            if friend.get("friend_id") == toy_info.get("to_user"):
                remark = friend.get("friend_remark")

        filename = text2audio(f"收到来自{remark}的新消息")

    # RET 返回值
    # JSON:
    ret = {
        "code": 0,
        "msg": "上传成功",
        "data":
            {
                "filename": filename,
                "friend_type": friend_type
            }
    }


    return jsonify(ret)



@uploader.route("/ai_uploader", methods=["POST"])
def ai_uploader():
    toy_info = request.form.to_dict()
    reco = request.files.get("reco")

    filename = f"{uuid4()}.wav"
    filepath = os.path.join(CHAT_PATH,filename)
    reco.save(filepath)

    # ai 人工智能操作
    Q = audio2text(filepath) # 语音识别 - ASR
    # 点播音乐 - 我想听幸福一家 我想听祖国我爱你 文本相似度实现
    ret = my_nlp_lowB(Q,toy_info.get("toy_id"))
    # AI对话

    # 主动发起消息

    return jsonify(ret)