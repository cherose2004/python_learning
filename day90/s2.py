# Flask 启动
# pip install Flask
from flask import Flask, render_template, redirect, Markup, request

app = Flask(__name__)
app.config.from_object()

@app.route("/",strict_slashes=,defaults=,)
def index():
    # return ""
    # return render_template("index.html") # 默认存放路径 templates
    # return redirect("/login")



app.run("0.0.0.0",9527) # 监听地址 监听端口

# #wsgi - b""
# """ bytes - environment
# GET /login HTTP/1.1
# host:127.0.0.1
# port:9527
# content-type: None
#
# request_body
# """

