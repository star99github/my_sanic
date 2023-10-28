# 服务器上的sanic服务启动脚本


# ===> 启动方式1: 用py脚本启动
python sanic_test.py


# ===> 启动方式2: 用命令行启动
python -m sanic anic_test.sanic_app --host=0.0.0.0 --port=8005 --workers=4


# ===> 启动方式3: 直接用 gunicorn 启动
gunicorn sanic_test:sanic_app --bind 0.0.0.0:8005 --worker-class sanic.worker.GunicornWorker


# ===> 启动方式4: 用 supervisor 启动 gunicorn 脚本
supervisor_run.ini
