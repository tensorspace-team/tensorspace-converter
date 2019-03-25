<h1 align=center>Running with Docker</h1>

Establishing `tensorflowjs` Python environment is a tedious topic? Dockerize it!

Here is a TensorSpace-Converter [Dockerfile](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/Dockerfile), you can use it to build a out-of-box TensorSpace-Converter `image`. We also provide some easy to use scripts to init ([init_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/init_docker_converter.sh)) and run ([run_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/run_docker_converter.sh)) `tensorspacejs` docker image. 

## Init

To init `tensorspacejs` Docker image (make sure start Docker daemon before init the image):
```shell
bash init_docker_converter.sh
```

## Run

To run docker image. Put TensorSpace-Converter script and model assets in a `WORK_DIR`, and execute `run_docker_converter.sh` to run `tensorspacejs` image:
```shell
bash run_docker_converter.sh --work_dir ./example
```

## WORK_DIR

`WORK_DIR` is where to place converter.sh and input model assets, meanwhile, `tensorspacejs` Docker image will save generated model files into this DIR.

* Configuration

Configure `WORK_DIR` when run the `tensorspacejs` Docker image through `run_docker_converter.sh`. In this example, configure `WORK_DIR` to be `./example`

* converter.sh

`converter.sh` contains TensorSpace-Converter conversion code, `tensorspacejs` image will execute this script. Place `converter.sh` at the root of `WORK_DIR`, make sure the file name is `converter.sh` (should not be renamed). 

* `input` and `output` setting

Place input model under `WORK_DIR`, the path of input model and output folder are relative to `WORK_DIR`. In this example, set `input_path` to be `./input/keras_model.h5` and `output_path` to be `./output` in `converter.sh`.