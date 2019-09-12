import os

from flask import Flask, request, render_template

# request 请求上下文管理

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def login():
    # print(request.args.to_dict())
    # print(request.host)
    # print(request.path)
    # print(request.url)
    # print(request.cookies)
    # 优先判断 请求方式
    # 如果是 GET 请求 返回登录页面
    if request.method == "GET":
        return render_template("login.html")
    # 如果是 POST 请求 获取用户名密码 校验
    else: # 405 请求方式不被允许
        my_file = request.files.get("my_file")
        filename = my_file.filename # 获取原始文件名
        file_path = os.path.join("avatar",filename)
        my_file.save(file_path)
        print(request.form.to_dict()) # form - FormData
        if request.form.get("username") == "YWB":
            return "Login OK!"

    return "Login 不OK!"




if __name__ == '__main__':
    app.run()
