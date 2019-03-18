#! /usr/bin/env bash

base_dir=""

if [ $1 == "--base_dir" ]
then
    shift
    base_dir=$1
fi

echo "Start converting model..."

docker rm -f ts-converter

docker run -it \
    --mount type=bind,source="$(pwd)"/$base_dir,target=/data \
    --name ts-converter \
    tensorspacejs

docker logs ts-converter

echo "Model is saved to output folder"
echo "Finished converting model!"