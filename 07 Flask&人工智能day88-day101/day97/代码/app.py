from flask import Flask

from serv.Content import content
from serv.Devices import devices
from serv.Users import user

app = Flask(__name__)
app.debug = True

app.register_blueprint(content)
app.register_blueprint(user)
app.register_blueprint(devices)

if __name__ == '__main__':
    app.run("0.0.0.0",9527)