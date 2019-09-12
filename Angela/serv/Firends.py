import os
import time

from bson import ObjectId
from flask import Blueprint, jsonify, send_file, request

from BaiduAi import text2audio
from Config import RET, MongoDB, COVER_PATH, MUSIC_PATH
from redis_msg import get_msg_one

friends = Blueprint("friends", __name__)


@friends.route("/friend_list", methods=["POST"])
def friend_list():
    user_id = request.form.get("_id")
    user_info = MongoDB.Users.find_one({"_id": ObjectId(user_id)})

    RET["CODE"] = 0
    RET["MSG"] = "好友查询"
    RET["DATA"] = user_info.get("friend_list")

    return jsonify(RET)


@friends.route("/chat_list", methods=["POST"])
def chat_list():
    chat_info = request.form.to_dict()
    print(chat_info)
    chat_id = ObjectId(chat_info.get("chat_id"))
    # 查询聊天窗口
    chat_window = MongoDB.Chats.find_one({"_id": chat_id})
    # 获取聊天记录
    chat_window_list = chat_window.get("chat_list")[-5:]
    # 返回聊天记录 条目[-5:]
    RET["CODE"] = 0
    RET["MSG"] = "好友查询"
    RET["DATA"] = chat_window_list

    get_msg_one(chat_info.get("from_user"),chat_info.get("to_user"))
    return jsonify(RET)


@friends.route("/recv_msg", methods=["POST"])
def recv_msg():
    chat_info = request.form.to_dict()
    sender = chat_info.get("from_user")
    receiver = chat_info.get("to_user")

    count,sender = get_msg_one(sender, receiver)

    user_list = [sender, receiver]

    chat_window = MongoDB.Chats.find_one({"user_list": {"$all": user_list}})

    # 收最后一条数据
    ch = chat_window.get("chat_list")[-count:]  # type:list
    ch.reverse()

    # 当收取消息时 - 不知道是谁发的
    # xxtx2 = "以下是来自xxx的消息"
    remark = "小伙伴"
    toy = MongoDB.Toys.find_one({"_id": ObjectId(receiver)})
    for friend in toy.get("friend_list"):
        if friend.get("friend_id") == sender:
            remark = friend.get("friend_remark")
    xxtx = text2audio(f"以下是来自{remark}的{count}条消息")

    xxtx_dict = {
        "from_user": sender,
        "to_user": receiver,
        "chat": xxtx,
        "createTime": time.time()
    }

    ch.append(xxtx_dict)

    return jsonify(ch)


@friends.route("/add_req", methods=["POST"])
def add_req():
    req_info = request.form.to_dict()
    req_info["status"] = 0
    toy = MongoDB.Toys.find_one({"_id": ObjectId(req_info.get("toy_id"))})

    if req_info.get("add_type") == "toy":
        user_info = MongoDB.Toys.find_one({"_id": ObjectId(req_info.get("add_user"))})
    else:
        user_info = MongoDB.Users.find_one({"_id": ObjectId(req_info.get("add_user"))})

    req_info["avatar"] = user_info.get("avatar")
    req_info["nickname"] = user_info.get("nickname") if user_info.get("nickname") else user_info.get("toy_name")
    req_info["toy_name"] = toy.get("toy_name")

    MongoDB.Request.insert_one(req_info)

    RET["CODE"] = 0
    RET["MSG"] = "添加好友请求成功"
    RET["DATA"] = {}

    return jsonify(RET)


@friends.route("/req_list", methods=["POST"])
def req_list():
    # print(request.form.get("user_id"))
    _id = request.form.get("user_id")  # user_id
    user_info = MongoDB.Users.find_one({"_id": ObjectId(_id)})
    print(user_info)
    bind_toys = user_info.get("bind_toys")

    toy_req_list = list(MongoDB.Request.find({"toy_id": {"$in": bind_toys}}))

    for index, req in enumerate(toy_req_list):
        toy_req_list[index]["_id"] = str(req.get("_id"))

    RET["CODE"] = 0
    RET["MSG"] = "查询好友请求"
    RET["DATA"] = toy_req_list

    return jsonify(RET)


@friends.route("/ref_req", methods=["POST"])
def ref_req():
    req_id = request.form.get("req_id")
    MongoDB.Request.update_one({"_id": ObjectId(req_id)}, {"$set": {"status": 2}})

    RET["CODE"] = 0
    RET["MSG"] = "拒绝添加好友"
    RET["DATA"] = {}

    return jsonify(RET)


@friends.route("/acc_req", methods=["POST"])
def acc_req():
    req_id = request.form.get("req_id")
    remark = request.form.get("remark")

    # 查询 好友请求 的数据
    req_info = MongoDB.Request.find_one({"_id": ObjectId(req_id)})

    # 添加好友 - 双方通讯录中 相互交换名片
    # 名片
    """
    a = {
        "friend_id": "5d54e5afb54198bf97b734fb",
        "friend_nick": "用户名称",
        "friend_remark": "爸爸",
        "friend_avatar": "baba.jpg",
        "friend_chat": "5d563059be4fc768fe573601",
        "friend_type": "app"
    }
    """
    # 查询接收方(toy)的信息  -  request数据表中 toy_id
    toy_info = MongoDB.Toys.find_one({"_id":ObjectId(req_info.get("toy_id"))})

    # 创建聊天窗口 - add_user toy_id
    chat_window = MongoDB.Chats.insert_one({"user_list":[req_info.get("add_user"),req_info.get("toy_id")],"chat_list":[]})

    # 1.制作名片 add_user  add  toy
    add_user_add_toy = {
        "friend_id": req_info.get("toy_id"),
        "friend_nick": toy_info.get("toy_name"),
        "friend_remark": req_info.get("remark"), # 接收方的备注 - 发起方在发起请求时添加的接收方备注
        "friend_avatar": toy_info.get("avatar"),
        "friend_chat": str(chat_window.inserted_id), # chat_window 新建聊天窗口
        "friend_type": "toy" # 接收方永远是Toy
    }
    # 2.将名片添加到add_user的friend_list中
    if req_info.get("add_type") == "toy":
        MongoDB.Toys.update_one({"_id":ObjectId(req_info.get("add_user"))},{"$push":{"friend_list":add_user_add_toy}})
    else:
        MongoDB.Users.update_one({"_id": ObjectId(req_info.get("add_user"))},{"$push":{"friend_list":add_user_add_toy}})


    # 获取 add_user 的数据 - toy app
    # if req_info.get("add_type") == "toy":
    #     user_info = MongoDB.Toys.find_one({"_id":ObjectId(req_info.get("add_user"))})
    # else:
    #     user_info = MongoDB.Users.find_one({"_id": ObjectId(req_info.get("add_user"))})


    # 2.制作名片 toy add  add_user
    toy_add_add_user = {
        "friend_id": req_info.get("add_user"),
        "friend_nick": req_info.get("nickname"),
        "friend_remark": remark,  # 发起方的备注 - 接收方在同意之后给发起方添加的备注信息
        "friend_avatar": req_info.get("avatar"),
        "friend_chat": str(chat_window.inserted_id),  # chat_window 新建聊天窗口
        "friend_type": req_info.get("add_type")  # 接收方永远是Toy
    }

    MongoDB.Toys.update_one({"_id": ObjectId(req_info.get("toy_id"))}, {"$push": {"friend_list": toy_add_add_user}})

    # request_info - status 更新 1同意
    MongoDB.Request.update_one({"_id": ObjectId(req_id)}, {"$set": {"status": 1}})
    RET["CODE"] = 0
    RET["MSG"] = "同意"
    RET["DATA"] = {}

    return jsonify(RET)
