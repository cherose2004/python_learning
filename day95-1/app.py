from flask import Flask,request

from serv.file_manager import fm
from serv.users import user

app = Flask(__name__)
app.debug = True
app.register_blueprint(fm)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run("0.0.0.0",9527)
