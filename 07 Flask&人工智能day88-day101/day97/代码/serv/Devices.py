import os

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
    # 进行绑定?
    # 1.玩具不存在 创建玩具
    # 在数据库中创建一条数据 Toys 数据存储结构
    toy_info["avatar"] = "toy.jpg"
    toy_info["bind_user"] = toy_info.pop("user_id")
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
    # 如果没有toy_id 能不能创建一个空的 user_list:[]

    # 写入数据库 toy = MongoDB.Toys.insert_one(toy_info) .inserted_id


    # 2.建立和 app的绑定关系 user["bind_toy"]append(toy_id)
    # 1.方式一 查询 用户信息 , 更改用户信息user["bind_toy"]append(toy_id) 更新用户信息update_one
    # 2.方式二 直接更新 用户信息表中的 bind_toy

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

    RET["CODE"] = 0
    RET["MSG"] = "OK"
    RET["DATA"] = {}

    return jsonify(RET)
