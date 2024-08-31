# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到容器中
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将当前目录中的所有文件复制到容器中的 /app 目录
COPY . .

# 暴露应用运行的端口
EXPOSE 5000

# 定义容器启动时运行的命令
CMD ["python", "app.py"]