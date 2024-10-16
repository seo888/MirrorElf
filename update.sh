#!/bin/bash

# 切换到项目目录
cd /www/Mirror-Elf

# 执行更新脚本
docker exec mirror_elf python update.py

# 停止 Docker Compose
docker compose down

# 删除指定镜像
docker rmi mirror-elf-mirror_elf

# 重新启动 Docker Compose
docker compose up -d



