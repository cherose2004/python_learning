from flask import Blueprint, request, jsonify, send_file
from settings import MongoDB,RET

user = Blueprint("user",__name__)

@user.route("/reg",methods=["POST"])
def reg():
    user_info = request.form.to_dict()
    MongoDB.users.insert_one(user_info)

    RET["code"] = 0
    RET["msg"] = "注册成功"
    RET["data"] = []

    return jsonify(RET)


@user.route("/login",methods=["POST"])
def login():
    user_info = request.form.to_dict()
    user_info_dict = MongoDB.users.find_one(user_info)
    user_info_dict["_id"] = str(user_info_dict.get("_id"))
    user_info_dict.pop("password")

    RET["code"] = 0
    RET["msg"] = "登录成功"
    RET["data"] = user_info_dict

    return jsonify(RET)