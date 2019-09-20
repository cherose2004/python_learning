from flask import Flask, render_template, send_file, session, jsonify,redirect
from setting import DebugConfig,TestConfig
from users import bp
from car_users import car_bp

app = Flask(__name__,template_folder="templatess")

app.config.from_object(DebugConfig)

app.register_blueprint(bp)
app.register_blueprint(car_bp)

@app.before_request
def be1():
    print("I am Be1")
    # return "第一个请求你就过不去"  # 5种

@app.before_request
def be2():
    print("I am Be2")
    # return "第二个请求过不去了" # 5种


@app.after_request
def af1(res):
    print("I am af1")
    return res


@app.after_request
def af2(res):
    print("I am af2")
    return res


# app.config.from_object(TestConfig)

# app.config["DEBUG"] = True
# app.secret_key = "@#$%^&#@$%^&@#$%^&*@#$%^&*#%&*@#%&)(*^%$#"
# app.session_cookie_name = "I am Not session"
# app.permanent_session_lifetime = 20
#
# app.config["JSONIFY_MIMETYPE"] = "Dragon/Fire"


# app.config
# app.default_config

@app.route("/set_session")
def set_session():
    session["key"] = "123"
    return "200OK"

@app.route("/get_session")
def get_session():
    return {"k1":"v1"}

# @app.errorhandler(404)
# def error404(error_message):
#     print(error_message)
#     return "你的页面被哥斯拉吃了" # 5种类型

@app.errorhandler(404)
def error404(error_message):
    print(error_message)
    # return redirect("https://www.autohome.com.cn/111232130/#pvareaid=33112794r5454") # 5种类型

    return send_file("music/1.mp3")

if __name__ == '__main__':
    app.run()