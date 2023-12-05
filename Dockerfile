# 使用一个官方 Python 运行时作为父镜像
FROM python:3.8-slim-buster

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 的容器中
COPY . /app

# 安装 requirements.txt 中指定的任何所需软件包
RUN pip install --no-cache-dir -r requirements.txt

# 使端口 8000 可供此应用程序使用
EXPOSE 8000

# 定义环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 运行 app.py 时，容器启动时运行
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]