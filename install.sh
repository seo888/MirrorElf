#!/bin/bash

# 设置项目根目录
PROJECT_DIR="/www/Mirror-Elf"

# 切换到项目目录
cd "$PROJECT_DIR" || exit 1

# 创建需要的目录
mkdir -p ./data/postgres_data ./data/rabbitmq_data ./data/garnet_data ./data/libretranslate_data

# 生成 ips.txt 文件
cd "$PROJECT_DIR/app" && bash ips.sh || exit 1

# 生成 docker-compose.yml 文件
cd "$PROJECT_DIR" && bash generate_compose.sh || exit 1

# 启动容器
docker compose up -d || exit 1
