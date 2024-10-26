#!/bin/bash

# 切换到项目目录
cd /www/Mirror-Elf

# 创建需要的目录
mkdir -p ./data/postgres_data
mkdir -p ./data/rabbitmq_data
mkdir -p ./data/garnet_data

# 执行更新脚本
docker exec mirror_elf python update.py
rm -rf /www/Mirror-Elf/app/core

# 从 repo 目录复制最新的 update.sh 文件，覆盖现有文件
cp /www/Mirror-Elf/app/repo/update.sh /www/Mirror-Elf/update.sh
cp /www/Mirror-Elf/app/repo/docker-compose.yml /www/Mirror-Elf/docker-compose.yml

# 停止 Docker Compose
docker compose down
# docker compose down --rmi all --volumes

# 删除指定镜像
docker rmi rabbitmq:3-management  || true  # 如果镜像不存在则忽略错误
docker rmi mirror-elf-mirror_elf || true  # 如果镜像不存在则忽略错误
docker rmi $(docker images -q mirror-elf-celery_worker*) || true  # 同样忽略错误

# 删除 rabbitmq_data 卷
# docker volume rm mirror-elf_rabbitmq_data || true  # 如果卷不存在则忽略错误

docker system prune -a -f


# 重新启动 Docker Compose
docker compose up -d --remove-orphans