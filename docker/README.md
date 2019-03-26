<p align="center">
<img width=200 src="../assets/docker.png">
</p>
<h1 align=center>Running with Docker</h1>

Establishing `tensorflowjs` environment is a tedious topic? Dockerize it!

Here is a TensorSpace-Converter [Dockerfile](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/Dockerfile), you can use it to build a out-of-box tensorspacejs `image`. We also provide some easy to use scripts to init ([init_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/init_docker_converter.sh)) and run ([run_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/run_docker_converter.sh)) `tensorspacejs` docker image. 

## Step 1: Init

To init `tensorspacejs` Docker image (make sure start Docker daemon before init the image):
```shell
bash init_docker_converter.sh
```

## Step 2: Run

To run docker image. Put TensorSpace-Converter script and model assets in a `work_dir`, and execute `run_docker_converter.sh` to run `tensorspacejs` image:
```shell
bash run_docker_converter.sh --work_dir ./example
```

## Parameters Setting

* work_dir

`work_dir` is where to place converter.sh and input model assets, meanwhile, `tensorspacejs` Docker image will save generated model files into this directory. Configure `work_dir` when run the `tensorspacejs` Docker image through `run_docker_converter.sh`. In this example, configure `work_dir` to be `./example`

* converter.sh

`converter.sh` contains TensorSpace-Converter conversion code, `tensorspacejs` image will execute this script. Place `converter.sh` at the root of `work_dir`, make sure the file name is `converter.sh` (should not be renamed). 

* `input` and `output`

Place input model under `work_dir`, the path of input model and output folder are relative to `work_dir`. In this example, set `input_path` to be `./input/keras_model.h5` and `output_path` to be `./output` in `converter.sh`.