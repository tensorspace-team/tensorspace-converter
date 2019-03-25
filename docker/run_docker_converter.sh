#! /usr/bin/env bash

work_dir=""

if [ $1 == "--work_dir" ]
then
    shift
    work_dir=$1
fi

echo "Start converting model..."

docker rm -f tsp-converter

docker run -it \
    --mount type=bind,source="$(pwd)"/$work_dir,target=/data \
    --name tsp-converter \
    tensorspacejs

docker logs tsp-converter