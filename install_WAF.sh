#!/bin/bash

# 创建 Safeline 目录
mkdir -p "/www/safeline"
cd "/www/safeline" || exit

# 下载 compose.yaml 文件
wget "https://waf-ce.chaitin.cn/release/latest/compose.yaml"

# 检查是否成功下载 compose.yaml
if [ ! -f "compose.yaml" ]; then
    echo "Failed to download compose.yaml. Exiting..."
    exit 1
fi

# 创建 .env 文件并写入环境变量
cat <<EOL > .env
SAFELINE_DIR=/www/safeline
IMAGE_TAG=latest
MGT_PORT=9443
POSTGRES_PASSWORD=mirrorelf
SUBNET_PREFIX=172.22.222
IMAGE_PREFIX=swr.cn-east-3.myhuaweicloud.com/chaitin-safeline
EOL

# 确保 /data/safeline 目录存在
mkdir -p "/data/safeline"
cd "/data/safeline" || exit

# 启动 Safeline Docker 容器
docker compose up -d

# 检查 Docker Compose 是否启动成功
if [ $? -ne 0 ]; then
    echo "Failed to start Safeline with Docker Compose. Please check the logs."
    exit 1
else
    echo "Safeline has been successfully started."
fi
