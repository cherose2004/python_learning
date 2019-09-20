from flask import Flask, render_template, redirect, jsonify, send_file, request
from flask import session

# 创建Flask实例 == app应用
import user

app = Flask(__name__)
# app.secret_key = "#$%^&*(^%$#$%^&*%$%^&*^%$%^*^TYUH^TYUGYUGHTYUG"

app.debug = True # 自动重启 透传错误信息 Log级别较低 Debug 级别
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "%^(&^%&(*^%&*^&Y"
app.config["PERMANENT_SESSION_LIFETIME"] = 30
app.config["SESSION_COOKIE_NAME"] = "I am Not Session"
app.config["JSONIFY_MIMETYPE"] = "alex/DSB" # jsonify Content-Type中的值

app.config # 非常重要




app.default_config

# @app.route("/login", methods=["get", "PoSt"],
#            endpoint="my_login",strict_slashes=True)  # 默认Get 请求方式
# def login():
#     # return "HelloWorld" # HttpResponse
#     if request.method == "GET":
#         return render_template("login.html")
#     # return redirect("/index")
#     # response location:http://127.0.0.1:9527/index
#     d = {
#         "name": "Alexander.DSB.Li"
#     }
#     print(session.get("user"))  # session["user"] KeyError
#     session["user"] = "Alexander.DSB.Li"
#     print(session.get("user"))
#     # eyJ1c2VyIjoiQWxleGFuZGVyLkRTQi5MaSJ9.XYGQYw.xfdW99lweDQQPVvg7himbdbDt_4
#     # return jsonify(d)
#     # return send_file("2.png")
#     # return d  # == jsonify(d)
#
#     request.method  # 请求方式
#     # print(request.args.get("id")) # 获取 URL 中的请求参数 /login?id=1 字典
#     # print(request.args.to_dict()) # 将获取的数据转化为字典
#     # print(request.form.get("u")) # FormData中的数据 POST 请求提交 form == args
#     # print(request.form.to_dict())
#     request.json  # 请求头中带有 Content-Type:application/json
#     request.data  # 请求头中不带有 Form or FormData 保存请求体中的原始信息 b""
#     request.url  # 自己试
#     request.path  # 自己试
#     request.host  # 自己试
#     request.host_url  # 自己试
#
#     print(request.files)  # file_storage 直接保存文件
#     file = request.files.get("my_file")
#     # file file_storage
#     filename = file.filename
#     print(filename)
#     file.save("当前文件名或者文件路径.png")
#
#     return "200 ok!"


@app.route("/home/<string:username>") # 默认动态参数 为string
def home(username):
    return f"123 200 Ok!{username}"

app.register_blueprint(user.user_bp)

@app.before_request
def be1():
    print("I am Be1")
    # return "返回Be1"

@app.before_request
def be2():
    print("I am Be2")
    # return "你废了"

@app.before_request
def be3():
    print("I am Be3")

@app.after_request
def af7086(resp):
    print("I am A1")
    return resp

@app.after_request
def af3721(resp):
    print("I am A2")
    return resp

@app.after_request
def af9527(resp):
    print("I am A3")
    return resp

@app.errorhandler(404)
def error404(errorMessage):
    print(errorMessage)
    return "当前页面不存在正在跳转.....10s后自动跳转" # Flask 5种响应方式
    # return redirect("")

from flask import views
from flask.views import MethodView

class Login(MethodView):
    def get(self):
        request.method # 请求下文
        return render_template("login.html")

    def post(self):
        if request.form.get("username") == "alex":
            return redirect("/index")

    def alexdsb(self): # views 中 追加 "alexdsb" 请求方式
        pass

app.add_url_rule("/login",view_func=Login.as_view(name="login"))


if __name__ == '__main__':
    app.run("0.0.0.0", 9527)  # 127.0.0.1:5000

    app.__call__
    app.wsgi_app
