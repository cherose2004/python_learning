from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 创建db 时一定要注意导入蓝图的顺序
from app01.views import user

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SESSION_COOKIE_NAME"] = "I am Not SESSION"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/s21?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.register_blueprint(user.user)

    db.init_app(app=app)  # app = Flask
    return app

