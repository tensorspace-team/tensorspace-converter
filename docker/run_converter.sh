#! /usr/bin/env bash

base_dir=""

if [ $1 == "--base_dir" ]
then
    shift
    base_dir=$1
fi

echo "Start converting model..."

docker run -d -it --mount type=bind,source="$(pwd)"/$base_dir,target=/data tensorspacejs

echo "Model is saved to output folder"
echo "Finished converting model!"