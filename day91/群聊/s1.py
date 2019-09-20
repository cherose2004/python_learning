from flask import Flask, request, render_template
from geventwebsocket.handler import WebSocketHandler  # 请求处理 WSGI HTTP
from geventwebsocket.server import WSGIServer  # 替换Flask原来的WSGI服务
from geventwebsocket.websocket import WebSocket  # 语法提示

app = Flask(__name__)

socket_list = []

@app.route("/ws")
def my_ws():
    # print(request.environ)

    ws_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    socket_list.append(ws_socket)
    print(len(socket_list),socket_list)
    while True:
        msg = ws_socket.receive()
        print(msg)
        for usocket in socket_list:
            if usocket == ws_socket:
                continue
            try:
                usocket.send(msg)
            except:
                continue

    # {'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_SOFTWARE': 'gevent/1.4 Python/3.6', 'SCRIPT_NAME': '', 'wsgi.version': (1, 0), 'wsgi.multithread': False, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'SERVER_NAME': 'DESKTOP-649CJ1L', 'SERVER_PORT': '9527', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/ws', 'QUERY_STRING': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '59994', 'HTTP_HOST': '127.0.0.1:9527', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_PRAGMA': 'no-cache', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'HTTP_COOKIE': 'session=9b38767b-63ea-4e94-9b4d-5bb274856fe9', 'wsgi.input': <gevent.pywsgi.Input object at 0x000001FEFD4E7528>, 'wsgi.input_terminated': True, 'werkzeug.request': <Request 'http://127.0.0.1:9527/ws' [GET]>}
    # {'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_SOFTWARE': 'gevent/1.4 Python/3.6', 'SCRIPT_NAME': '', 'wsgi.version': (1, 0), 'wsgi.multithread': False, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'SERVER_NAME': 'DESKTOP-649CJ1L', 'SERVER_PORT': '9527', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/ws', 'QUERY_STRING': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '60393', 'HTTP_HOST': '127.0.0.1:9527', 'HTTP_CONNECTION': 'Upgrade', 'HTTP_PRAGMA': 'no-cache', 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_UPGRADE': 'websocket', 'HTTP_ORIGIN': 'file://', 'HTTP_SEC_WEBSOCKET_VERSION': '13', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9', 'HTTP_COOKIE': 'session=9b38767b-63ea-4e94-9b4d-5bb274856fe9', 'HTTP_SEC_WEBSOCKET_KEY': '+XlqBnhqwEekZTYcz4I+tg==', 'HTTP_SEC_WEBSOCKET_EXTENSIONS': 'permessage-deflate; client_max_window_bits', 'wsgi.input': <gevent.pywsgi.Input object at 0x00000120281075E8>, 'wsgi.input_terminated': True, 'wsgi.websocket_version': '13', 'wsgi.websocket': <geventwebsocket.websocket.WebSocket object at 0x00000120280E54C0>, 'werkzeug.request': <Request 'http://127.0.0.1:9527/ws' [GET]>}


@app.route("/wechat")
def wechat():
    return render_template("ws.html")


if __name__ == '__main__':
    # app.run()
    http_serv = WSGIServer(("0.0.0.0", 9527), app,
                           handler_class=WebSocketHandler)  # handler_class=WSGIHandler / HTTPHandler
    http_serv.serve_forever()
