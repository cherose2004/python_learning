from flask import Blueprint
from app01.models import Users
from app01 import db

user = Blueprint("user",__name__)

@user.route("/reg/<username>")
def reg(username):
    u = Users(name=username)
    db.session.add(u)
    db.session.commit()

    return "reg 200 OK"


@user.route("/user_list")
def user_list():
    res = Users.query.filter(Users.id>1).all()
    print(res)

    return f"当前有{len(res)}个用户"

