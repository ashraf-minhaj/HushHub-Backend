#!/bin/bash

VERSION_TAG=$1

cd ../app
# docker build -t ashraftheminhaj/hushhub-backend:$1 .
# docker tag ashraftheminhaj/hushhub-backend:$1 ashraftheminhaj/hushhub-backend:latest

docker buildx create --use --platform=linux/arm64,linux/amd64 --name multiplatform-builder
# docker buildx inspect --bootstrap
# docker buildx build --platform linux/arm64,linux/amd64 --push  -t ashraftheminhaj/hushhub-backend:$1 .

docker buildx build --platform=linux/arm64,linux/amd64 --push --tag ashraftheminhaj/hushhub-backend:$1 .

# docker push ashraftheminhaj/hushhub-backend:$1 