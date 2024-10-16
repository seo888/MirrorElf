一键安装

```
cd /www && git clone https://github.com/seo888/MirrorElf.git Mirror-Elf && cd Mirror-Elf/app && bash ips.sh && cd ../ && docker compose up -d
```

一键删除

```
cd /www/Mirror-Elf && docker compose down --rmi all --volumes && rm -rf /www/Mirror-Elf
```
