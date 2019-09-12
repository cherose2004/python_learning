import json

from flask import Flask,request

from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.server import WSGIServer
from geventwebsocket.websocket import WebSocket

ws_app = Flask(__name__)

user_socket_dict = {}

@ws_app.route("/app_ws/<user_id>")
def app_ws(user_id):
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    if user_socket:
        user_socket_dict[user_id] = user_socket
    print(user_socket_dict)
    while 1:
        user_msg = user_socket.receive()
        user_msg_dict = json.loads(user_msg)
        receiver_id = user_msg_dict.get("receiver")
        receiver_socket = user_socket_dict.get(receiver_id)
        receiver_socket.send(user_msg)


if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9528),ws_app,handler_class=WebSocketHandler)
    http_serv.serve_forever()
