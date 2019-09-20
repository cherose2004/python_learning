import os

from flask import Flask, render_template, send_file

app = Flask(__name__,template_folder="templatess",static_folder="static",static_url_path="/futeng")
# static == 你的家
# /static == 回家路
# /futeng == 富腾路

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/futeng/<filename>")
# def get_img(filename):
#     filepath = os.path.join("static",filename)
#     return send_file(filepath)

if __name__ == '__main__':
    app.run()