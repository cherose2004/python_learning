import os

from flask import Blueprint, request, jsonify, send_file
from settings import AVATAR_PATH,RECO_PATH

fm = Blueprint("fm",__name__)

@fm.route("/upload_file",methods=["POST"])
def upload_file():
    print(request.files)
    avatar = request.files.get("avatar")
    avatar_file_path = os.path.join(AVATAR_PATH,avatar.filename)
    avatar.save(avatar_file_path)

    RET ={
        "code":0,
        "filename":avatar.filename
    }

    return jsonify(RET)


@fm.route("/upload_file_reco",methods=["POST"])
def upload_file_reco():
    print(request.files)
    reco = request.files.get("reco")
    reco_file_path = os.path.join(RECO_PATH,reco.filename)
    reco.save(reco_file_path)

    RET ={
        "code":0,
        "filename":reco.filename
    }

    return jsonify(RET)


@fm.route("/get_avatar/<filename>",methods=["GET"])
def get_avatar(filename):
    file_path = os.path.join(AVATAR_PATH,filename)
    return send_file(file_path)


@fm.route("/get_chat/<filename>",methods=["GET"])
def get_chat(filename):

    file_path = os.path.join(RECO_PATH,filename)

    os.system(f"ffmpeg -i {file_path} {file_path}.mp3")
    return send_file(f"{file_path}.mp3")