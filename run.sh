#!/bin/bash

# Build Dockerfile
docker build -t mlrdb:1  --build-arg MYSQL_ROOT_PASSWORD=test1234   --build-arg MYSQL_DATABASE=mlr-dev-db-tlb   --build-arg MYSQL_USER=test   --build-arg MYSQL_PASSWORD=test1234 .

# Run Docker container
docker run -d -p 3306:3306 --name mlrdb-container mlrdb:1

pip install -r requirements.txt

sleep 15

python init_seasonal.py

python init_recipe.py

