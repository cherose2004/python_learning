from flask import Blueprint

bp = Blueprint("app01",__name__)

@bp.route("/add_user")
def add_user():
    return "添加用户"

@bp.route("/find_user")
def find_user():
    return "查看用户"

@bp.route("/drop_user")
def drop_user():
    return "删除用户"

@bp.route("/up_user")
def up_user():
    return "修改用户"


