from sanic_main import *


@sanic_app.route("/to_homepage/", methods=["GET", "POST"])
async def to_homepage(request):
    return response.text("这是首页")


# 服务启动前
@sanic_app.listener('before_server_start')
async def setup_db(app, loop):
    pass


# 服务关闭前
@sanic_app.listener('before_server_stop')
async def close_db(app, loop):
    pass


# 异常监听
# @sanic_app.exception(ExpiredSignatureError)
# async def handleSignatureError(request, exception):
#     return response.json()


# sanic中间件
@sanic_app.middleware('request')
async def zhongjianjian(request):
    pass
