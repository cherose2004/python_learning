import os

from flask import Blueprint, jsonify, send_file
from Config import RET, MongoDB, COVER_PATH, MUSIC_PATH

content = Blueprint("content",__name__)

@content.route("/content_list",methods=["POST"])
def content_list():

    con_list = list(MongoDB.Content.find({}))

    for index,cont in enumerate(con_list):
        con_list[index]["_id"] = str(cont.get("_id"))

    RET["CODE"] = 0
    RET["MSG"] = "获取内容资源列表"
    RET["data"] = con_list

    return jsonify(RET)


@content.route("/get_cover/<filename>",methods=["GET"])
def get_cover(filename):
    file_path = os.path.join(COVER_PATH,filename)
    return send_file(file_path)

@content.route("/get_music/<filename>",methods=["GET"])
def get_music(filename):
    file_path = os.path.join(MUSIC_PATH,filename)
    return send_file(file_path)
