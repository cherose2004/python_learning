from functools import wraps

from flask import Flask

app = Flask(__name__)

# 基于 functools 更改内部函数的属性 __name__

def war(func): # func = home
    @wraps(func)
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs) # func = home
        return ret
    return inner


@app.route("/a")
@war
def a():
    pass

@app.route("/b")
@war
def b():
    pass

app.run()