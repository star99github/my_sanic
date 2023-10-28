"""sanic websocket 服务端代码："""
from sanic import Sanic
from sanic.websocket import WebSocketProtocol

app = Sanic(__name__)


@app.websocket('/ws')
async def feed(request, ws):
    while True:
        receive_data = await ws.recv()
        print('服务端接收客户端: ' + receive_data)

        send_data = 'hello!'
        print('服务端发给客户端: ' + send_data)
        await ws.send(send_data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, protocol=WebSocketProtocol)