import os

from bson import ObjectId
from flask import Flask, request, jsonify, send_file
from settings import MongoDB

app = Flask(__name__)
app.debug = True

@app.route("/reg",methods=["POST"])
def reg():
    user_info = request.form.to_dict()
    MongoDB.usertest.insert_one(user_info)

    return jsonify({"code":0,"msg":"注册成功"})

@app.route("/login",methods=["POST"])
def login():
    user_info = request.form.to_dict()
    user_dict = MongoDB.usertest.find_one(user_info)
    if user_dict:
        user_dict["_id"] = str(user_dict.get("_id"))
        return jsonify({"code": 0, "msg": "登录成功","data":user_dict})
    else:
        return jsonify({"code": 9999, "msg": "登陆失败"})


@app.route("/auto_login",methods=["POST"])
def auto_login():
    user_info = request.form.to_dict()
    user_info["_id"] = ObjectId(user_info.pop("user_id"))
    user_dict = MongoDB.usertest.find_one(user_info)
    if user_dict:
        user_dict["_id"] = str(user_dict.get("_id"))
        return jsonify({"code": 0, "msg": "登录成功","data":user_dict})
    else:
        return jsonify({"code": 9999, "msg": "登陆失败"})

@app.route("/uploader",methods=["POST"])
def uploader():
    file = request.files.get("my_avatar")
    if not file :
        file = request.files.get("my_audio")
        file.save(file.filename)
        os.system(f"ffmpeg -i {file.filename} {file.filename}.mp3")
        os.remove(file.filename)

        ret = {
            "code":0,
            "filename":f"{file.filename}.mp3",
            "msg":"上传成功"
        }
    else:
        file.save(file.filename)
        ret = {
            "code":0,
            "filename":file.filename,
            "msg":"上传成功"
        }

    return jsonify(ret)


@app.route("/get_avatar/<avatar_name>",methods=["GET"])
def get_avatar(avatar_name):
    return send_file(avatar_name)


@app.route("/get_chat/<avatar_name>",methods=["GET"])
def get_chat(avatar_name):
    return send_file(avatar_name)



if __name__ == '__main__':
    app.run("0.0.0.0",9527)
