# gunicorn_config.py 内容如下:
debug = True
loglevel = 'debug'
bind = '127.0.0.1:8998'   # 内部端口
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
workers = 2  # 指定进程数量
worker_class = 'sanic.worker.GunicornWorker'
