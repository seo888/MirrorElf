#!/bin/bash

# 获取 CPU 核心数
NUM_WORKERS=$(nproc)

WORKER_LOOP=""
for i in $(seq 1 $NUM_WORKERS); do
    WORKER_LOOP+="  celery_worker_$i:
    network_mode: host
    build: ./task
    container_name: celery_worker_$i
    cpus: '0.6'
    restart: on-failure
    command: celery -A tasks worker -l info -P gevent -c 512 --prefetch-multiplier=1 --time-limit=600 -n celery_worker_$i@%h
    environment:
      - CELERY_BROKER_URL=amqp://admin:mirrorelf@localhost//
      - CELERY_RESULT_BACKEND=rpc://
      - CELERY_RESULT_EXPIRES=300
      - CELERYD_PREFETCH_MULTIPLIER=1
    depends_on:
      - rabbitmq

"
done

# 打印 WORKER_LOOP 的内容
echo "$WORKER_LOOP"

export WORKER_LOOP
envsubst < docker-compose.template.yml > docker-compose.yml
