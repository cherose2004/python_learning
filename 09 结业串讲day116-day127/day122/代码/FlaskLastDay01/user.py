from flask import Blueprint
user_bp = Blueprint("user_bp",__name__,url_prefix="/ubp")

@user_bp.route("/user_bp")
def user():
    return "i am user user_bp"