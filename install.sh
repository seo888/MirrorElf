#!/bin/bash

cd /www

# 检查是否已经存在 "Mirror-Elf" 目录
if [ -d "Mirror-Elf" ]; then
  echo "目录 'Mirror-Elf' 已经存在，退出。"
  exit 0
fi

# 安装 jq 和 tar，如果它们尚未安装
sudo apt install -y jq tar

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

# 解压下载的 tar 文件，并将解压后的目录命名为 "Mirror-Elf"
echo "正在解压 $TAR_FILE..."
tar -xzf "$TAR_FILE" --one-top-level=Mirror-Elf --strip-components=1

# 检查解压是否成功
if [ $? -eq 0 ]; then
  echo "解压成功！"
else
  echo "解压失败！"
  exit 1
fi

echo "'镜像精灵 Mirror-Elf $(echo "$RELEASE_JSON" | jq -r .tag_name) 下载成功'"

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

# 安装防火墙
bash install_WAF.sh