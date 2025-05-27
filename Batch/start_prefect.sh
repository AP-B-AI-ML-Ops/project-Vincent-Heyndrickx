#!/bin/bash

sleep 30

prefect work-pool create --type process batch --overwrite
prefect worker start -p batch &

python /app/monitoring.py
