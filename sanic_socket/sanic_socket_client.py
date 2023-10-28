"""sanic websocket 客户端代码："""

import asyncio
import websockets


async def hello():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        # 发送给服务端的信息
        message = input('input: ')
        print(f"发送给服务端的信息：{message}")
        await websocket.send(message)

        # 接收服务端的信息
        bytes_data = await websocket.recv()

        # bytes 转 string
        str_data = str(bytes_data)
        print("接收来自服务端的信息:{}".format(str_data))


if __name__ == '__main__':
    r = hello()
    asyncio.run(r)
