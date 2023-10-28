"""接口实现远程电脑截图或者录像"""


import datetime
import time
from logging import log
from sanic import Sanic
from sanic.response import json
from PIL import ImageGrab
import datetime
import time
import cv2.cv2 as cv2
import os

app = Sanic(__name__)


@app.get("/screenshot")
async def screenshot(request):
    """实现屏幕截图"""
    log.info("IP: {} 进行截图".format(request.ip))

    # 参数说明  电脑屏幕的长和高
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    bbox = (0, 0, 1920, 1080)
    im = ImageGrab.grab(bbox)

    now = str(time.time())[:10]

    print("多少时间后开始截图操作：{}秒。".format(request.args))

    try:
        waiting_time = int(request.args["waiting"][0])
    except:
        waiting_time = 0.001

    if waiting_time <= 20:
        time.sleep(waiting_time)
    else:
        log.info("设置的等待截图时间过长，默认最高30秒")
        time.sleep(30)

    # 参数 保存截图文件的路径
    im.save(r'./tempdir/screenhost/{}.png'.format(now))

    return json({
        "time": str(datetime.datetime.now())[:19],
        "IP": request.ip,
        "mes": "screenshot",
        "waiting_time": waiting_time,
        "fileName": "{}.png".format(now),
    })


@app.get("/record_screen")
async def record_screen(request):
    """
    实现录屏
    Python开发需要用到 Camera 或者 视频设备时，可以使用OpenCV来创建视频文件，
    创建视频文件的类是VideoWriter。OpenCV 底层是用 FFMEPG 进行多媒体开发的。
    pip install opencv-python
    import cv2
    """
    log.info("IP: {} 进行录像".format(request.ip))

    cam = cv2.VideoCapture(0)
    time_now = time.time()
    os.makedirs('capture', exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    video_out = None

    video_time = 10

    while True:
        ret, frame = cam.read()
        if video_out:
            video_out.write(frame)
        cv2.imshow("Video", frame)
        cv2.waitKey(1)
        if video_out is None or time.time() - time_now > video_time:
            if video_out:
                video_out.release()
                video_out = None
            time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            video_path = os.path.join('./tempdir/capture/') + time_str + '.avi'
            video_out = cv2.VideoWriter(video_path, fourcc, 30.0, (640, 480))
            time_now = time.time()
        if time.time() - time_now > video_time + 1:
            break

    return json({
        "time": str(datetime.datetime.now())[:19],
        "IP": request.ip,
        "mes": "save_video",
        "each_video_time": video_time,
    })


if __name__ == '__main__':
    app.run(port=3031, auto_reload=True)
