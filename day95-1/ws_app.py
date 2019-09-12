import json

from flask import Flask,request

from geventwebsocket.server import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket

ws_app = Flask(__name__)

user_socket_dict = {}

@ws_app.route("/<user_id>")
def ws(user_id):
    user_socket = request.environ.get("wsgi.websocket") #type:WebSocket
    if user_socket:
        user_socket_dict[user_id] = user_socket
    print(user_socket_dict)

    while 1:
        msg = user_socket.receive() # {sender,receiver,data}
        msg_dict = json.loads(msg)
        receiver = msg_dict.get("receiver")
        receiver_socket = user_socket_dict.get(receiver)
        receiver_socket.send(msg)

if __name__ == '__main__':
    http_serv = WSGIServer(("0.0.0.0",9528),ws_app,handler_class=WebSocketHandler)
    http_serv.serve_forever()