# 给多个视图函数 增加 校验登录的装饰器
import os

STUDENT = {'name': 'Old', 'age': 38, 'gender': '中'}

STUDENT_LIST = [
    {'name': 'Old', 'age': 38, 'gender': '中'},
    {'name': 'Boy', 'age': 73, 'gender': '男'},
    {'name': 'EDU', 'age': 84, 'gender': '女'}
]

STUDENT_DICT = {
    1: {'name': 'Old', 'age': 38, 'gender': '中'},
    2: {'name': 'Boy', 'age': 73, 'gender': '男'},
    3: {'name': 'EDU', 'age': 84, 'gender': '女'},
}


from flask import Flask, render_template, Markup, request, session, redirect, url_for, send_file

app = Flask(__name__)
# app.config["DEBUG"] = True
app.debug = True
app.secret_key = "!@#$%^(*&^%$#@#$%&*(^$WQ*(^EWET*^EWEU"


# def war(func): # func = home
#     def inner(*args,**kwargs):
#         # 校验session
#         if session.get("user"):
#             # session["req_count"] += 1
#             ret = func(*args,**kwargs) # func = home
#             return ret
#         else:
#             return redirect("/login")
#     return inner


@app.route("/")
# @war           # war(home) -> inner
# 先要经过一次校验 才能执行或不执行视图函数
def home(): # {"home":"/","homea":"/a"}
    # 校验用户登录 session
    #如果session。get（“user”） 存在
    # 如果不存在 返回Login
    return "我是 杠"

@app.route("/a/<ty>_<page>_<id>",methods=["GET","PoSt","options","abc"],endpoint="end_homea" ,strict_slashes=True) # 反向URL
# @war        # war(func=homeend_homeaa) --> inner
def homea(ty,page,id):
    # count = request.args.get("count",count)
    print(type(page))
    return f"200OK!{page}"

@app.route("/get_music/<filename>")
def get_music(filename):
    filename = "1.mp3"
    filepath = os.path.join("music",filename)
    return send_file(filepath)

@app.route("/get_img/<filename>")
def get_img(filename):
    filepath = os.path.join("img", filename)
    return send_file(filepath)


@app.route("/login",methods=["GET","POST"])
def login():
    # 当请求方式为 GET 的时候
    if request.method == "GET":
        # eyJ1c2VyIjoiYWxleGFuZGVyLmRzYi5saSJ9.XUfYMw.o8oZX2GMC-kjZPWBkyRuUeSMp4M
        # .eJyrViotTi1SslJKzEmtSMxLSS3SSylO0svJVNIByxjiljLCLWWMW8oEt5Qpbikz3FLmuKUssEnVAgDhbFGU.XUfcCg.NqZTYMyH51z_ywmWl5E_EFp8GLY
        # .eJw1zjEKwzAMBdC7aC5BlmXH7lmy2LGGQuiQYCiU3r2Ooiwa3hdf-kI_ZIcnlE0-5d1kn9pRp-0FD03ciJYeHKcxxTVjuphcXTqLK8ZeOc5URuj5ZlZOiOu5TXdJUGZZz-1M2TgqZwx-cKM8CmsiC2c7jNEgWQnqJ5jh9wdRFz4I.XUfcdg.DKdyhxVMHlNDv7_ZNwZV9xtT-sk
        #  交由客户端保管机制
        # {"user":"alexander.dsb.li"}
        # Flask理念 - 一切从简 为服务器减轻压力
        return render_template("login.html")
    else:
        user_info = request.form.to_dict()
        session["user"] = user_info.get("username")
        session["req_count"] = 1
        print(session.get("user"))
        return "login OK!"

if __name__ == '__main__':
    app.run("0.0.0.0",9527)

