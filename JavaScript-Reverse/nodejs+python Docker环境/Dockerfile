# Python3.7官网镜像
FROM python:3.7.3

# 设置工作目录
WORKDIR /app

# 复制当前目录下的文件到工作目录
COPY . /app

# 安装pip库
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/ &&\
    wget https://nodejs.org/dist/v10.16.0/node-v10.16.0-linux-x64.tar.xz &&\
    tar xf node-v10.16.0-linux-x64.tar.xz -C /opt/
ENV PATH=$PATH:/opt/node-v10.16.0-linux-x64/bin

# 容器启动后执行命令, 运行example
CMD ["python", "example.py"]
