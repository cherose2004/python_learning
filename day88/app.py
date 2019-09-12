from flask import Flask, render_template, redirect, send_file,request

app = Flask(__name__)

@app.route("/")
def index():
    # return ""
    # return render_template()
    # return redirect("/login")

    # 封装方法
    # return send_file() # 打开并返回文件内容 自动识别文件类型 Content-Type：文件类型
    # return jsonify() # 返回标准格式的json字符串 Content-Type:application/json
    # Flask 1.1.1 直接返回dict格式 自动执行 jsonify

    # request.method
    # request.path #/login
    # request.url # http://127.0.0.1:5000/login?id=1
    # request.host # 127.0.0.1:5000
    # request.cookies # cookie
    # request.files # request中的文件 返回 FileStorage 中存在 save 保存文件 filename 原始文件名
    # request.form # FormData中的数据
    # request.args # url中的数据
    # request.data # 请求头中不含有 Form FormData 保存原始请求体中的数据 b""
    # request.json # 请求中带有 content-type:application/json
    pass


if __name__ == '__main__':
    app.run()