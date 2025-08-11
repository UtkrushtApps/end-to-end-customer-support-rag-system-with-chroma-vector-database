#!/bin/bash
set -e
if ! command -v docker &> /dev/null
then
    echo "[ERROR] Docker is not installed. Please install Docker before running this script."
    exit 1
fi
if ! command -v docker-compose &> /dev/null
then
    echo "[ERROR] docker-compose is not installed. Please install docker-compose before running this script."
    exit 1
fi
if [ "$1" == "--fresh" ]; then
  docker-compose down -v
else
  docker-compose down
fi
echo "[INFO] Starting Chroma DB service on localhost:8000 ..."
docker-compose up -d chroma-db
echo "[INFO] Chroma DB service is running at http://localhost:8000"