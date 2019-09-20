from flask import Blueprint

car_bp = Blueprint("app02",__name__,url_prefix="/car")

@car_bp.route("/add_user")
def add_user():
    return "car添加用户"

@car_bp.route("/find_user")
def find_user():
    return "car查看用户"

@car_bp.route("/drop_user")
def drop_user():
    return "car删除用户"

@car_bp.route("/up_user")
def up_user():
    print("I am vf")
    return "car修改用户"


