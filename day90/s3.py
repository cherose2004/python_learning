from flask import Flask,request,session

from flask_session import Session
from redis import Redis

app = Flask(__name__)

# app.secret_key = "#$%^&*(*&^%$#$%^&*%$#$%^&*^%$#$%^&^$#$%&"
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(host="192.168.12.87",port=6379,db=10)
# app.session_interface # Flask 利用 session_interface 选择 Session 的存放位置 和 存放机制
# app.default_config

Session(app)


@app.route("/sets")
def sets():
    session["key"] = "Alexander.DSB.Li"
    return  "Set OK"

@app.route("/gets")
def gets():
    return session.get("key")


if __name__ == '__main__':
    app.run("0.0.0.0",9527)