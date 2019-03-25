<h1 align=center>通过 Docker 运行 TensorSpace-Converter</h1>

配置一个适合 `tensorspacejs` 运行 Python 环境有点复杂？不妨试试在 Docker 中运行吧！

TensorSpace-Converter 提供了一个 [Dockerfile](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/Dockerfile)，你可以通过它快速创建一个开箱即用的 TensorSpace-Converter 镜像。为了让这个 `tensorspacejs` 镜像更易用，我们提供了脚本来 `创建` ([init_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/init_docker_converter.sh)) 与 `运行` ([run_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/run_docker_converter.sh)) 它。

## 创建

创建一个 `tensorspacejs` Docker 镜像 (确保在初始化镜像前已经启动了 Docker):
```shell
bash init_docker_converter.sh
```

## 运行

* 运行 `tensorspacejs` Docker 镜像

将 TensorSpace-Converter 脚本和模型文件都放在一个工作目录 (`WORK_DIR`) 下，然后执行 `run_docker_converter.sh` 脚本来运行 `tensorspacejs` 镜像：

```shell
bash run_docker_converter.sh --work_dir ./example
```

## WORK_DIR

`WORK_DIR` 是 TensorSpace-Converter 的工作目录，converter.sh 脚本和模型文件都放置在这个目录下，在执行 `tensorspacejs` Docker 镜像后，也会将经过转化的文件生成在该目录下。

* 配置

在通过 `run_docker_converter.sh` 脚本运行 `tensorspacejs` Docker 镜像时，需要配置 `WORK_DIR`。在这个例子中，将 `WORK_DIR` 配置成 `./example`。

* converter.sh

将 TensorSpace-Converter 转化代码放在 `converter.sh` 文件中，`tensorspacejs` 镜像将会执行这个文件来对模型进行转换。将 `converter.sh` 放置于 `WORK_DIR` 的个目录中，并且保持 `converter.sh` 这个文件的文件名不变。

* `input` 和 `output` 设置

将需要转换的模型放在 `WORK_DIR` 文件夹中，在 `converter.sh` 中设置 `input_path` 和 `output_path` 时，都设置成相对于 `WORK_DIR` 的相对路径。在这个例子中，`input_path` 是 `./input/keras_model.h5`，`output_path` 是 `./output`。
