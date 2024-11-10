一键安装

```
mkdir -p /www && apt update -y && apt install -y curl vim jq tar && cd /www && curl -O https://raw.githubusercontent.com/seo888/MirrorElf/main/install.sh && bash install.sh
```

一键删除

```
cd /www/Mirror-Elf && docker compose down --rmi all --volumes && rm -rf /www/Mirror-Elf
```
