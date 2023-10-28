FROM sanicframework/sanic:3.8-latest
MAINTAINER ZHANGKUANKUAN <jj99whxn_star@163.com>
LABEL version=1.0.1

WORKDIR /my_sanic
VOLUME ["/my_sanic/datas"]

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8005/tcp

HEALTHCHECK --interval = 5s --timeout = 30s  --retries = 3 CMD curl -fs http://localhost/ || exit 1

# 启动方法1: 脚本启动
#RUN chmod 777 run_server.sh
#CMD ./run_server.sh

# 启动方法2: 直接启动
CMD ["python", "sanic_test.py"]
