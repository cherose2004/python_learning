from flask import Flask, render_template, redirect, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return "hello World I am Flask"
    # return None

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return redirect("/index")

@app.route("/get_file")
def get_file():
    return send_file("2.exe") # 返回文件内容，自动识别文件类型，Content-type中添加文件类型，Content-type:文件类型


@app.route("/get_json")
def get_json():
    d = {"k":"v"}
    return d
    # return jsonify(d) # 返回标准Json格式字符串 API接口






app.run()


