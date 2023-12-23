import json
import os
from sanic import Request, response, Sanic, redirect
from sanic.views import HTTPMethodView
from sanic_cors import CORS
import sqlalchemy


sanic_app = Sanic("my_sanic")
CORS(sanic_app)

# =====> sanic声明接口的方式一：@sanic_app.route()(常用)，路由路径开头可不加斜杠/，会自动补充；methods的方法名不分大小写，不指定此字段则默认为GET请求
@sanic_app.route("sanic_test", methods=["get", "post"])
async def sanic_test(request):
    print("这是一个sanic测试视图")
    return response.text("this is my sanic_test")

# =====> sanic声明接口的方式二：直接用sanic_app.add_route()方法
# 这种方法跟用@sanic_app.route()效果一样,因为route()方法只是add_route()的一个包装器
sanic_app.add_route(sanic_test, uri="/test_sanic", name="test_sanic", methods=["post", "get"])


# =====> sanic声明接口的方式三：@sanic_app.post()，使用已封装好的具体的HTTP请求方法
@sanic_app.route("/record_log", methods=["post", "get"])
async def write_file(request):
    file_content = request.json.get("file_content")
    print(f"-----> start write log file: {file_content}")
    res = {"status": "failed", "detail": "write log file failed"}
    logs_file = os.path.join(os.path.dirname(__file__), "logs/sanic_log.log")
    with open(logs_file, "wb") as f:
        f.write(f"sanic写入一些内容: {file_content}".encode())
        res["status"] = "success"
        res["detail"] = "write log file success"
    return response.json(body=res)
    # return response.text(json.dumps(res))


# =====> sanic声明接口的方式四：使用类视图(推荐)，from sanic.views import HTTPMethodView
class HomePage(HTTPMethodView):
    """类视图"""

    async def get(self, request):
        return response.json({"status": "success", "msg": "你好: class view for get request"})

    async def post(self, request):

        return response.json({"status": "success", "msg": "你好: class view for post request"})


sanic_app.add_route(HomePage.as_view(), uri="/homepage/", name="homepage")


# =====> sanic声明接口的方式五：from sanic.views import CompositionView  # 用CompositionView动态添加路由
# from sanic.views import CompositionView
# async def post_handler(request):
#     print(request.json)
#     return response.text('这是动态路由响应结果')
#
# view = CompositionView()
# view.add(["POST"], post_handler)
# sanic_app.add_route(view, "/post_info")


# ===> 重定向:Sanic提供了一个url_for基于处理程序方法名称生成URL的方法,可避免将URL路径硬编码到应用程序当中
# 路由的名称为程序处理方法名称，即函数.__name__生成的，用于传递一个name参数到装饰器中来修改它的名称
# url_for使用注意：第一个参数为重定向URL的路由名称(默认为函数名称)，并非URL名称。重定向时可将请求参数指派到url_for方法中
# 示例中重定向后的路径为: /homepage/to_home/
@sanic_app.get("/before_redirect_url/")
async def test_redirect(request):
    print(f"的原始请求body: {request.json}")
    url = sanic_app.url_for("homepage", name="to_home", _method="post")
    print(f"重定向后的url是: {url}")
    return redirect(url)


# =====> sanic的唯一url: 在路由route()方法或蓝图Blueprint()方法中用参数 strict_slashes 指定,默认为False-不唯一url,true-唯一url
# 唯一url: 即严格匹配路由定义,末尾有无斜杠/将影响访问,非唯一url,末尾有无斜杠/都可访问
# 若需要将所有的URL都设置成为唯一URL,可以这样: app = Sanic(strict_slashes=True)

# ====> 静态文件url: 一般用于返回静态HTML页面
sanic_app.static("/static", "./templates/html/my_home.html")


if __name__ == "__main__":
    print("-----> my_sanic 服务开始启动")
    sanic_app.run(host="0.0.0.0", port=8005, workers=2, debug=True, auto_reload=True)

    print("-----> my_sanic 服务运行完成")
