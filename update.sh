#!/bin/bash

# 切换到项目目录
cd /www/Mirror-Elf

# 执行更新脚本
docker exec mirror_elf python update.py

# 停止 Docker Compose
docker compose down

# 删除指定镜像
docker rmi mirror-elf-mirror_elf || true  # 如果镜像不存在则忽略错误
docker rmi $(docker images -q mirror-elf-celery_worker*) || true  # 同样忽略错误

# 重新启动 Docker Compose
docker compose up -d

# 从 repo 目录复制最新的 update.sh 文件，覆盖现有文件
cp /www/Mirror-Elf/repo/update.sh /www/Mirror-Elf/update.sh