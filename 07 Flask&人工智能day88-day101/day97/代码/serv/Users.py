import os

from bson import ObjectId
from flask import Blueprint, jsonify, send_file, request
from Config import RET, MongoDB, COVER_PATH, MUSIC_PATH

user = Blueprint("user",__name__)

@user.route("/reg",methods=["POST"])
def reg():
    user_info = request.form.to_dict()
    user_info["avatar"] = "baba.jpg" if user_info.get("gender") == "2" else "mama.jpg"
    user_info["bind_toys"] = []
    user_info["friend_list"] = []
    MongoDB.Users.insert_one(user_info)


    RET["CODE"] = 0
    RET["MSG"] = "注册成功"
    RET["DATA"] = {}

    return jsonify(RET)

@user.route("/login",methods=["POST"])
def login():
    user_dict = request.form.to_dict()
    user_info = MongoDB.Users.find_one(user_dict,{"password":0})
    user_info["_id"] = str(user_info.get("_id"))

    RET["CODE"] = 0
    RET["MSG"] = "登录成功"
    RET["DATA"] = user_info

    return jsonify(RET)


@user.route("/auto_login",methods=["POST"])
def auto_login():
    user_dict = request.form.to_dict()
    user_dict["_id"] = ObjectId(user_dict.get("_id"))
    user_info = MongoDB.Users.find_one(user_dict,{"password":0})
    user_info["_id"] = str(user_info.get("_id"))

    RET["CODE"] = 0
    RET["MSG"] = "登录成功"
    RET["DATA"] = user_info

    return jsonify(RET)