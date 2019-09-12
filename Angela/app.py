from flask import Flask, render_template

from serv.Content import content
from serv.Devices import devices
from serv.Firends import friends
from serv.Uploader import uploader
from serv.Users import user

app = Flask(__name__)
app.debug = True

app.register_blueprint(content)
app.register_blueprint(user)
app.register_blueprint(devices)
app.register_blueprint(friends)
app.register_blueprint(uploader)





@app.route("/")
def toy():
    return render_template("WebToy.html")


if __name__ == '__main__':
    app.run("0.0.0.0",9527)