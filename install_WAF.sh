#!/bin/bash

# 创建必要的目录
mkdir -p "/www/safeline"

# 进入 Safeline 目录
cd "/www/safeline"

# 下载最新的 Docker Compose 配置文件
wget "https://waf-ce.chaitin.cn/release/latest/compose.yaml"

# 使用 echo 命令逐行写入 .env 文件
echo "SAFELINE_DIR=/www/safeline" > .env
echo "IMAGE_TAG=latest" >> .env
echo "MGT_PORT=9443" >> .env
echo "POSTGRES_PASSWORD=mirrorelf" >> .env
echo "SUBNET_PREFIX=172.22.222" >> .env
echo "IMAGE_PREFIX=swr.cn-east-3.myhuaweicloud.com/chaitin-safeline" >> .env

# 确保 /www/safeline 目录存在
mkdir -p "/www/safeline"

# 进入 /www/safeline 目录
cd "/www/safeline"

# 启动 Safeline Docker 容器
docker compose -f /www/safeline/compose.yaml up -d

# 检查 Docker Compose 启动情况
if [ $? -eq 0 ]; then
    echo "Safeline started successfully!"
else
    echo "Failed to start Safeline with Docker Compose. Please check the logs."
fi
