from flask import Flask, request

app = Flask(__name__)
# app = object()
app.__call__
@app.route("/")
def index():
    request.method
    return "200OK"

app.run()


# from werkzeug.wrappers import Response,Request
# from werkzeug.serving import run_simple
#
# @Request.application
# def app(req):
#     print(req.method)
#     return Response("200 OK!")
#
# run_simple("0.0.0.0",9527,app)