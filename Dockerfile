FROM python:3.7-alpine3.8

MAINTAINER paddington <tonexus.lee@gmail.com>

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# 配置默认放置 App 的目录
RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8888
CMD ["sh"]
