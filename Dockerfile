# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖项文件到容器中
COPY requirements.txt .

# 安装依赖项
RUN pip install -r requirements.txt

# 复制应用程序代码到容器中
COPY . .

# 暴露应用程序的端口
EXPOSE 8080

# 运行应用程序
CMD ["python", "app/server.py"]
