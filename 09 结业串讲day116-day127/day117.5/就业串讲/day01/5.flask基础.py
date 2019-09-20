# -*- coding: utf-8 -*-
# __author__ = "maple"

from flask import Flask,request

app = Flask(__name__)

@app.route('/index')
def index():
    print(request.args)
    print(request.form)
    return "123"

if __name__ == '__main__':
    app.run()
