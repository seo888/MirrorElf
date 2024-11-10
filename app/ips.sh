#!/bin/bash

# 定义输出文件
IPS_TXT="./config/IPS.txt"

# 获取所有 IP 地址并排除 127.0.0.1 和局域网 IP 地址
ips=$(ip addr | grep 'inet ' | awk '{print $2}' | cut -d/ -f1 | \
    grep -v '^127.0.0.1$' | \
    grep -vE '^10\.|^172\.(1[6-9]|2[0-9]|3[0-1])\.|^192\.168\.')
    
# 将 IP 地址写入文件
echo "$ips" > "$IPS_TXT"