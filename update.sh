#!/bin/bash

# 切换到项目app目录
cd /www/Mirror-Elf/app

# 创建需要的目录
mkdir -p ../data/postgres_data ../data/rabbitmq_data ../data/garnet_data

# 从 GitHub API 获取最新的发布信息
RELEASE_JSON=$(curl -s https://api.github.com/repos/seo888/MirrorElf/releases/latest)

# 从 JSON 响应中提取 tarball URL
TAR_URL=$(echo "$RELEASE_JSON" | jq -r .tarball_url)

# 检查 TAR URL 是否为空
if [ -z "$TAR_URL" ]; then
  echo "从 GitHub API 获取 TAR URL 失败"
  exit 1
fi

# 定义基于版本标签的输出 tar 文件名
TAR_FILE="MirrorElf-$(echo "$RELEASE_JSON" | jq -r .tag_name).tar.gz"

# 使用 curl 下载 tarball
echo "从 $TAR_URL 下载发布版本..."
curl -L -o "$TAR_FILE" "$TAR_URL"

# 检查下载是否成功
if [ $? -eq 0 ]; then
  echo "下载成功！"
else
  echo "下载失败！"
  exit 1
fi

# 解压下载的 tar 文件，并将解压后的目录命名为 "repo"
echo "正在解压 $TAR_FILE..."
tar -xzf "$TAR_FILE" --one-top-level=repo --strip-components=1

# 检查解压是否成功
if [ $? -eq 0 ]; then
  echo "解压成功！"
  rm -rf $TAR_FILE
else
  echo "解压失败！"
  exit 1
fi

echo "'镜像精灵 Mirror-Elf $(echo "$RELEASE_JSON" | jq -r .tag_name) 下载成功'"

# 执行更新脚本
docker exec mirror_elf python update.py

rm -rf /www/Mirror-Elf/app/core*

# 从 repo 目录复制最新的文件，覆盖现有文件
cp -rf /www/Mirror-Elf/app/repo/task /www/Mirror-Elf
cp /www/Mirror-Elf/app/repo/generate_compose.sh /www/Mirror-Elf/generate_compose.sh
cp /www/Mirror-Elf/app/repo/install_WAF.sh /www/Mirror-Elf/install_WAF.sh
cp /www/Mirror-Elf/app/repo/install.sh /www/Mirror-Elf/install.sh
cp /www/Mirror-Elf/app/repo/update.sh /www/Mirror-Elf/update.sh
cp /www/Mirror-Elf/app/repo/docker-compose.template.yml /www/Mirror-Elf/docker-compose.template.yml

# 生成docker-compose.yml
bash generate_compose.sh

# 停止 Docker Compose
docker compose down
# docker compose down --rmi all --volumes

# 删除指定镜像
docker rmi rabbitmq:3-management  || true  # 如果镜像不存在则忽略错误
docker rmi mirror-elf-mirror_elf || true  # 如果镜像不存在则忽略错误
docker rmi $(docker images -q mirror-elf-celery_worker*) || true  # 同样忽略错误

# 删除 rabbitmq_data 卷
docker volume rm mirror-elf_rabbitmq_data || true  # 如果卷不存在则忽略错误

docker system prune -a -f

# 重新启动 Docker Compose
docker compose up -d --remove-orphans