import os

from bson import ObjectId
from flask import Blueprint, jsonify, send_file, request
from Config import RET, MongoDB, COVER_PATH, MUSIC_PATH

devices = Blueprint("devices", __name__)


@devices.route("/scan_qr", methods=["POST"])
def scan_qr():
    device_key = request.form.to_dict()
    device = MongoDB.Devices.find_one(device_key)
    if device:
        RET["CODE"] = 0
        RET["MSG"] = "二维码扫描成功"
        RET["DATA"] = device_key

        toy = MongoDB.Toys.find_one(device_key)
        if toy:
            RET["CODE"] = 2
            RET["MSG"] = "设备已经进行绑定"
            RET["DATA"] = {"toy_id":str(toy.get("_id"))}

    else:
        RET["CODE"] = 1
        RET["MSG"] = "请扫描玩具二维码"
        RET["DATA"] = {}

    # 蜜汁逻辑: 第三种情况
    """
    //3.二维码扫描成功,但设备已经进行绑定
    {
        "code":2,
        "msg":"设备已经进行绑定",
        "data":
        {
            "toy_id":toy_id
        }
    }
    """

    return jsonify(RET)


@devices.route("/bind_toy", methods=["POST"])
def bind_toy():
    toy_info = request.form.to_dict()
    user_id = toy_info.pop("user_id")
    user_info = MongoDB.Users.find_one({"_id": ObjectId(user_id)})
    # 进行绑定?
    # 1.玩具不存在 创建玩具
    # 在数据库中创建一条数据 Toys 数据存储结构
    toy_info["avatar"] = "toy.jpg"
    toy_info["bind_user"] = user_id
    toy_info["friend_list"] = []
    # 如果 friend_list 空的 要不要创建 Toy
    """
        toy 添加 App 为好友
        { // 通讯录信息
            "friend_id" : "app_id", // 好友id
            "friend_nick" : "app nickname", // 好友的昵称
            "friend_remark" : "request.remark", // 好友备注
            "friend_avatar" : "app avatar", // 好友头像
            "friend_chat" : "当前toy 没有被创建 没有 toy_id 没有toy_id 就真的没法创建chatwindow吗?", // 私聊窗口ID 聊天数据表对应值 ?
            "friend_type" : "app" // 好友类型
        },

        """
    # 创建聊天窗口
    # "friend_chat" : "5ca17c7aea512d26281bcb8c",私聊窗口ID
    #  chat_window = MongoDB.Chats.insert_one({user_list:[appid toy_id],chat_list:[]})
    # chat_window.inserted_id ObjectId

    chat_window = MongoDB.Chats.insert_one({"user_list":[],"chat_list":[]})
    chat_id = str(chat_window.inserted_id) # 获取创建的 空chat id

    # 如果没有toy_id 能不能创建一个空的 user_list:[]

    # 创建 user 在 toy_friend_list 中的 名片儿
    toy_add_user = {
        "friend_id": user_id,
        "friend_nick": user_info.get("nickname"),
        "friend_remark": toy_info.pop("remark"),
        "friend_avatar": user_info.get("avatar"),
        "friend_chat": chat_id,
        "friend_type": "app"
    }

    # 将user 的名片 存放在 toy_friend_list 中
    toy_info["friend_list"].append(toy_add_user)

    # 写入数据库 toy = MongoDB.Toys.insert_one(toy_info) .inserted_id
    toy = MongoDB.Toys.insert_one(toy_info)
    toy_id = str(toy.inserted_id) # 创建玩具的 toy_id

    # 2.建立和 app的绑定关系 user["bind_toy"]append(toy_id)
    # 1.方式一 查询 用户信息 , 更改用户信息user["bind_toy"]append(toy_id) 更新用户信息update_one
    # 2.方式二 直接更新 用户信息表中的 bind_toy
    user_info["bind_toys"].append(toy_id)

    # 3.双方的关系 好友通讯录 添加名片 成为好友关系?
    # app 可以与 toy 沟通
    # user[friend_list] toy_info["friend_list"] 互相交换名片?
    # 名片 =  ? user 添加 toy 的名片到 firend_lsit
    """
    { // 通讯录信息
        "friend_id" : "toy的ID  toy_id ", // 好友id
        "friend_nick" : "baby_name", // 好友的昵称
        "friend_remark" : "toy_name", // 好友备注
        "friend_avatar" : "toy_info["avatar"]", // 好友头像
        "friend_chat" : "5ca17c7aea512d26281bcb8c", // 私聊窗口ID 聊天数据表对应值 ?
        "friend_type" : "toy" // 好友类型
    },
    """

    # 名片儿创建
    user_add_toy = {
        "friend_id": toy_id,
        "friend_nick": toy_info.get("baby_name"),
        "friend_remark": toy_info.get("toy_name"),
        "friend_avatar": toy_info.get("avatar"),
        "friend_chat": chat_id,
        "friend_type": "toy"
    }

    # 名片属于通讯录 friend_list
    user_info["friend_list"].append(user_add_toy)

    # 更新用户user_info的数据?
    MongoDB.Users.update_one({"_id": ObjectId(user_id)},{"$set":user_info})

    # 聊天窗口 chat_window 没有主人呢
    user_list = [toy_id,user_id]
    MongoDB.Chats.update_one({"_id":chat_window.inserted_id},{"$set":{"user_list":user_list}})


    RET["CODE"] = 0
    RET["MSG"] = "OK"
    RET["DATA"] = {}

    return jsonify(RET)


@devices.route("/toy_list", methods=["POST"])
def toy_list():
    user_id = request.form.get("_id")

    user_bind_toy_list = list(MongoDB.Toys.find({"bind_user":user_id}))

    for index,item in enumerate(user_bind_toy_list):
        user_bind_toy_list[index]["_id"] = str(item.get("_id"))

    RET["CODE"] = 0
    RET["MSG"] = "获取Toy列表"
    RET["DATA"] = user_bind_toy_list


    return jsonify(RET)


@devices.route("/open_toy", methods=["POST"])
def open_toy():
    device_key = request.form.to_dict()
    # 1.设备处于绑定状态, 正常启动
    # 2.设备未绑定
    # Toys 表中是否存在 Toy的信息 用DeviceKey查询toy
    toy = MongoDB.Toys.find_one(device_key)
    if toy:
        # 已经绑定
        ret = {
            "code": 0,
            "music": "Success.mp3",
            "toy_id": str(toy.get("_id")),
            "name": toy.get("toy_name")
        }
    else:
        # 还未绑定?
        is_device = MongoDB.Devices.find_one(device_key)
        if is_device:
            ret = {
                "code":1,
                "music":"Nobind.mp3"
            }
        # 3.设备未授权
        else:
            ret = {
                "code": 2,
                "music": "Nolic.mp3"
            }


    return jsonify(ret)