from flask import Flask

app = Flask(__name__) # template_folder=,static_folder=,static_url_path=

# FBV
@app.route("/")
def index():
    return "200 OK!"

# Django views.View

from flask import views

@app.before_request
def is_login():
    return 1

#cbv - fbv be1-be2-vf-af2-af1

@app.after_request
def login_ok(res):
    return res

class Login(views.MethodView): # 继承 MethodView 让我当前的 class 可以成为视图类

    # methods = ["POST"]
    # decorators = [is_login]

    def get(self,*args,**kwargs):
        return "I am Get"

    def post(self,*args,**kwargs):
        pass

    # def dragonfire(self,*args,**kwargs):
    #     pass

view_func = Login.as_view(name="loginlogin")
# view_func.__name__ = "loginlogin"

app.add_url_rule("/login",
                 # endpoint="my_login",
                 view_func=view_func # view_func.__name__ = "loginlogin"
                )


if __name__ == '__main__':
    app.run()


