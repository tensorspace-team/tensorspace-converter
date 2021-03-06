<p align="center">
<img width=150 src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/logo_tsConverter.png">
</p>
<h1 align="center">TensorSpace Converter</h1>

<p align="center">
<a href="https://github.com/tensorspace-team/tensorspace-converter/blob/master/README.md"><strong>English</strong></a> | <strong>中文</strong>
</p>

<p align="center">
关于 TensorSpace 🤔:  <a href="https://github.com/tensorspace-team/tensorspace">TensorSpace Github</a>
</p>

<p align="center">
<a href="https://badge.fury.io/py/tensorspacejs"><img src="https://badge.fury.io/py/tensorspacejs.svg" alt="PyPI version" height="18"></a>
  <a href="https://www.python.org/downloads/release/python-360/"><img src="https://img.shields.io/badge/python-3.6-blue.svg" alt="Python 3.6"></a>
  <a href="https://github.com/tensorspace-team/tensorspace-converter/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-green.svg" alt="license badge"></a>
<a href="https://github.com/tensorflow/tensorflow"><img src="https://img.shields.io/badge/dependencies-tensorflow-brightgreen.svg" alt="dependencies badge"></a>
<a href="https://github.com/keras-team/keras"><img src="https://img.shields.io/badge/dependencies-keras-brightgreen.svg" alt="dependencies badge"></a>
<a href="https://github.com/tensorflow/tfjs-node"><img src="https://img.shields.io/badge/dependencies-tfjs_node-brightgreen.svg" alt="dependencies badge"></a>
<a href="https://github.com/tensorflow/tfjs-converter"><img src="https://img.shields.io/badge/dependencies-tfjs_converter-brightgreen.svg" alt="dependencies badge"></a>
  <a href="https://gitter.im/tensorspacejs/Lobby#"><img src="https://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg" alt="gitter"></a>
</p>

TensorSpace-Converter 是 TensorSpace 预处理工具，提供对预训练的 TensorFlow、Keras、TensorFlow.js 模型开箱即用的支持。在使用 TensorSpace-Converter 对预训练模型进行预处理的过程中，TensorSpace-Converter 将提取出模型中隐藏层的数据、并生成一个新的模型，新的模型可以被 TensorSpace 载入并3D可视化。TensorSpace-Converter 简化了 TensorSpace 的使用，降低了 TensorSpace 的学习曲线。作为可视化应用开发工具，TensorSpace-Converter 有助于分离 `后端模型训练` 与 `前端模型可视化` 的工作。

## 目录

* [TensorSpace-Converter 使用场景](#motivation)
* [开始使用](#start)
    * [下载](#install)
    * [使用](#usage)
* [通过 Docker 运行](#docker)
* [Converter API](#api)
* [Converter 使用样例](#examples)
    * [TensorFlow](#tensorflow)
    * [Keras](#keras)
    * [TensorFlow.js](#tensorflowjs)
* [对比](#comparison)
* [开发设置](#development)
* [开发人员](#contributors)
* [联系方式](#contact)
* [许可证](#license)

## <div id="motivation">TensorSpace-Converter 使用场景</div>

[TensorSpace](https://github.com/tensorspace-team/tensorspace) 可以用于 TensorFlow, Keras, TensorFlow.js 模型3D可视化，而在应用 TensorSpace 可视化之前，需要完成一个重要的步骤————对预训练模型进行预处理（通过 [这篇介绍](https://tensorspace.org/html/docs/preIntro_zh.html) 可以了解更多有关 TensorSpace 预处理的概念与原理）。TensorSpace-Converter 可以帮助开发者快速完成 TensorSpace 预处理过程的辅助工具。

TensorSpace-Converter 对 TensorFlow、Keras、TensorFlow.js 提供开箱即用的支持，只需要几行简单的 TensorSpace-Converter 代码就可以完成 TensorSpace 预处理过程。在 TensorSpace-Converter 之前，对模型进行预处理，需要开发者熟悉掌握多个框架（TensorFlow，keras，tfjs-converter等）。举个小栗子，在没有 TensorSpace-Converter 的情况下，对 tf.keras 模型进行预处理时，除了需要准备一个预训练的 tf.keras 模型之外，还需要编写 tf.keras 代码将模型转化成多输出，以及使用 tfjs-converter 将模型转化为 TensorSpace 兼容的格式。而现在有了 TensorSpace-Converter 之后，只需要 [几行](#tensorflow) 简单的 TensorSpace-Converter 代码，就可以完成之前这个较为繁琐的工作。

作为 TensorSpace 的生态组件，TensorSpace-Converter 简化了 TensorSpace 的开发过程，降低了 TensorSpace 学习曲线。作为可视化应用开发工具，TensorSpace-Converter 有助于分离 `后端模型训练` 与 `前端模型可视化` 的工作。

<p align="center">
<img width="80%" src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/hello_converter.gif">
</p>
<p align="center">
<b>图1</b> - 使用 TensorSpace-Converter
</p>

## <div id="start">开始使用</div>

### <div id="install">下载</div>

通过 pip 下载 `tensorspacejs` 包:

```shell
$ pip install tensorspacejs
```

如果成功下载了 `tensorspacejs` 包，可以查看下载的 TensorSpace-Converter 版本：
```shell
$ tensorspacejs_converter -v
```

然后初始化 TensorSpace Converter:
```shell
$ tensorspacejs_converter -init
```

* **注意**

TensorSpace-Converter 必须运行在 `Python 3.6`, `Node 11.3+`, `NPM 6.5+` 的环境中。如果在本地环境中已经下载了其他的 Python 版本，我们建议使用 <a href="https://anaconda.org/anaconda/conda">conda</a> 来创建一个纯净的 `Python 3.6` 环境：
```shell
$ conda create -n envname python=3.6
$ source activate envname
$ pip install tensorspacejs
```

### <div id="usage">使用</div>

接下来将使用 TensorSpace-Converter 预处理一个预训练模型（该模型是使用 tf.keras 训练的 lenet），然后使用 TensorSpace 载入经过预处理的模型。

以下为使用的代码及文件：[tf.keras 模型](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tensorflow/rawModel/keras), [TensorSpace-Converter 脚本](https://github.com/tensorspace-team/tensorspace-converter/blob/master/examples/tensorflow/script/convertKeras.sh) and [TensorSpace 可视化代码](https://github.com/tensorspace-team/tensorspace-converter/blob/master/examples/tensorflow/index.html).

<p align="center">
<img width="100%" src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/workflow_zh.png">
</p>
<p align="center">
<b>图2</b> - TensorSpace-Converter 使用流程
</p>

#### 第一步：使用 TensorSpace-Converter 处理预训练的模型

TensorSpace-Converter 将会将一个模型转化并生成一个多输出模型，通过 [这篇介绍](https://tensorspace.org/html/docs/preIntro_zh.html) 可以了解更多有关 TensorSpace 预处理的概念与原理。

```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_keras" \
    --output_layer_names="conv_1,maxpool_1,conv_2,maxpool_2,dense_1,dense_2,softmax" \
    ./PATH/TO/MODEL/tf_keras_model.h5 \
    ./PATH/TO/SAVE/DIR
```

<p align="center">
<img width="100%" src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/multi-output_zh.png">
</p>
<p align="center">
<b>图3</b> - 经过 TensorSpace-Converter 转化生成的多输出模型
</p>

#### 第二步: 使用 TensorSpace 载入经过处理的模型

```javascript
model.load({
    type: "tensorflow",
    url: "/PATH/TO/MODEL/model.json"
});
```

<p align="center">
<img width="100%" src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/demo.gif">
</p>
<p align="center">
<b>图4</b> - LeNet 模型 TensorSpace 可视化
</p>

## <div id="docker">通过 Docker 运行 TensorSpace-Converter</div>

<p align="center">
<img width=200 src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/docker.png">
</p>

配置一个适合 `TensorSpace-Converter` 运行环境有点复杂？不妨试试在 Docker 中运行吧！

TensorSpace-Converter 提供了一个 [Dockerfile](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/Dockerfile) 来创建 `tensorspacejs` Docker镜像。`tensorspacejs` 镜像是一个开箱即用的 TensorSpace-Converter 运行环境。为了让这个 `tensorspacejs` 镜像更易用，我们提供了脚本来 `创建` ([init_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/init_docker_converter.sh)) 与 `运行` ([run_docker_converter.sh](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/run_docker_converter.sh)) 它。

* 创建一个 `tensorspacejs` Docker 镜像 (确保在初始化镜像前已经启动了 Docker):
```shell
cd ./docker
bash init_docker_converter.sh
```

* 运行 `tensorspacejs` Docker 镜像

将 TensorSpace-Converter 脚本和模型文件都放在一个工作目录 (`WORK_DIR`) 下，然后执行 `run_docker_converter.sh` 脚本来运行 `tensorspacejs` 镜像：

```shell
cd ./docker
bash run_docker_converter.sh --work_dir PATH/TO/WORK_DIR
```

这篇 [Docker 教程](https://github.com/tensorspace-team/tensorspace-converter/blob/master/docker/README_zh.md)，通过一个实际的例子，介绍了如何通过 Docker 运行 TensorSpace-Converter。

## <div id="api">TensorSpace-Converter API</div>

TensorSpace-Converter 示例脚本：
```shell
$ tensorspacejs_converter \
    --input_model_from="XXX" \
    --input_model_format="YYY" \
    --output_layer_names="EEE1,EEE2,EEE3" \
    input_path \
    output_path
```

参数介绍：

|Positional Arguments | 介绍 |
|---|---|
|`input_path`  | 模型输入路径，在 [使用样例](#examples) 部分将介绍如何设置该属性。|
|`output_path` | 模型输出路径（文件夹），TensorSpace-Converter 会将经过转化的模型输出到该路径中 |


| 可选参数 | 介绍
|---|---|
|`--input_model_from`     | 配置模型是使用哪种深度学习库训练并保存的，如果模型是使用TensorFlow 训练并保存的的，配置 `tensorflow`，如果模型是使用 Keras 训练并保存的，配置 `keras`，如果模型是使用 TensorFlow.js 训练并保存的，配置 `tfjs` |
|`--input_model_format`     | 模型的格式，在 [使用样例](#examples) 部分将介绍如何设置该属性。 |
|<nobr>`--output_layer_names`</nobr>| 输出希望在TensorSpace 中可视化的 layer，使用英文半角逗号“,”分割。 |

## <div id="examples">TensorSpace-Converter 使用样例</div>

这部分将介绍如何使用 TensorSpace-Converter 来处理不同类型的模型。TensorSpace 支持预处理使用 TensorFlow, Keras, TensorFlow.js 训练的模型。

### <div id="tensorflow">TensorFlow</div>

<p align="center">
<img width=60% src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/converter_logo_tf.png">
</p>

当使用 TensorFlow 训练并保存一个模型时，TensorSpace-Converter 支持转化以下格式的模型：saved model，frozen model，模型结构权重合并的 HDF5，模型结构和权重分开保存的 HDF5。TensorSpace-Converter 使用不同的转换指令来转换这四种模型。在 TensorFlow 的图结构中，可能没有 `layer` 的概念，不过，一个特定的 `tensor` 可以对应一个 `layer` 的输出，在这种情况下，可以取出相对应的 `tensor` 名称，然后设置到 TensorSpace-Converter 的 `output_layer_names` 参数中。

对于模型结构和权重合并保存的 HDF5 模型，会有一个 `xxx.h5` 文件。在配置 TensorSpace-Converter 转换脚本时，将 `input_model_format` 设置成 `tf_keras`。示例转化脚本：
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_keras" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.h5 \
    ./PATH/TO/SAVE/DIR
```

对于模型结构和权重分开保存的 HDF5 模型，会有一个模型结构文件 `xxx.json` 和一个权重文件 `eee.h5`。在配置 TensorSpace-Converter 转换脚本时，将 `input_model_format` 设置成 `tf_keras_separated`。对于这种模型类型，因为由两个模型文件，在设置 TensorSpace-Converter 的 `input_path` 时，合并两个文件的路径，并用英文半角逗号“,”分开，将 `.json` 文件的路径在前，`.h5` 文件的路径在后。示例转化脚本：
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_keras_separated" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json,./PATH/TO/MODEL/eee.h5 \
    ./PATH/TO/SAVE/DIR
```

对于 TensorFlow saved model。在配置 TensorSpace-Converter 转换脚本时，将 `input_model_format` 设置成 `tf_saved`。示例转化脚本：
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_saved" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/SAVED/MODEL/FOLDER \
    ./PATH/TO/SAVE/DIR
```

对于 TensorFlow frozen model。在配置 TensorSpace-Converter 转换脚本时，将 `input_model_format` 设置成 `tf_frozen`。示例转化脚本：
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_frozen" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.pb \
    ./PATH/TO/SAVE/DIR
```
这篇 [TensorFlow 教程](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tensorflow/README_zh.md)，通过一个实际的例子，介绍了如何使用 TensorSpace-Converter 来预处理 TensorFlow 模型。

### <div id="keras">Keras</div>

<p align="center">
<img width=60% src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/converter_logo_keras.png">
</p>

当使用 Keras 训练并生成一个模型时，模型有两种保存形式：模型结构和权重保存在一个HDF5文件，模型结构和权重保存在不同的文件中。TensorSpace-Converter 使用不同的转换指令来转换这两种模型。

对于一个 Keras 模型，如果模型结构和权重保存在同一个 HDF5 文件中，模型将会是 `xxx.h5`。在配置 TensorSpace-Converter 转换脚本时，将 `input_model_format` 设置成 `topology_weights_combined`。示例转换代码：
```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.h5 \
    ./PATH/TO/SAVE/DIR
```

对于一个 Keras 模型，如果模型结构和权重分开保存，那么会有一个模型结构文件 `xxx.json` 和一个模型权重文件 `xxx.h5`。在配置 TensorSpace-Converter 转换脚本时，将 `input_model_format` 设置成 `topology_weights_separated`。对于这种模型类型，因为由两个模型文件，在设置 TensorSpace-Converter 的 `input_path` 时，合并两个文件的路径，并用英文半角逗号“,”分开，将 `.json` 文件的路径在前，`.h5` 文件的路径在后。示例转换代码：
```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_separated" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json,./PATH/TO/MODEL/eee.h5 \
    ./PATH/TO/SAVE/DIR
```
这篇 [Keras 教程](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/keras/README_zh.md)，通过一个实际的例子，介绍了如何使用 TensorSpace-Converter 来预处理 Keras 模型。

### <div id="tensorflowjs">TensorFlow.js</div>

<p align="center">
<img width=60% src="https://raw.githack.com/tensorspace-team/tensorspace-converter/master/assets/converter_logo_tfjs.png">
</p>

当使用 TensorFlow.js 训练并保存一个模型后，会得到一个模型结构文件 `xxx.json` 和一些权重文件 `xxx.weight.bin`。当使用 TensorSpace-Converter 来预处理这类模型时，需要将模型结构文件（xxx.json）和权重文件（xxx.weight.bin）放在同一个目录下，然后将模型结构文件的路径设置为 `input_path`。示例转换代码：

```shell
$ tensorspacejs_converter \
    --input_model_from="tfjs" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json \
    ./PATH/TO/SAVE/DIR
```
这篇 [TensorFlow.js 教程](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tfjs/README_zh.md)，通过一个实际的例子，介绍了如何使用 TensorSpace-Converter 来预处理 TensorFlow.js 模型。

## <div id="comparison">对比</div>

<table align="center" width="95%">
   <tr>
      <th>使用框架</th>
      <th>不使用TensorSpace_Converter</th>
      <th>使用 TensorSpace_Converter</th>
   </tr>
   <tr>
      <td>tf.keras</td>
      <td>安装 TensorFlow ，构建环境<br />① 训练/加载模型<br />② 添加中间层输出<br />③ 保存嵌入后的多输出模型<br />④ 转换为 TensorSpace 适配的模型</td>
      <td rowspan="4">① 理解模型结构，对每一层输出进行命名<br />② 使用 TensorSpace_Converter <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;快速输出 TensorSpace 适配的模型</td>
   </tr>
   <tr>
      <td>TensorFlow</td>
      <td>① 训练/加载模型<br />② 找出中间层 tensor 名称 <br />③ 转换为 TensorSpace 适配的模型</td>
   </tr>
   <tr>
      <td>Keras</td>
      <td>① 训练/加载模型<br />② 添加中间层输出<br />③ 保存嵌入的多输出模型<br />④ 转换为 TensorSpace 适配的模型</td>
   </tr>
   <tr>
      <td>TensorFlow.js</td>
      <td>① 训练 TensorSpace 适配的模型<br />② 转换 tfjs 模型以适配 TensorSpace</td>
   </tr>
</table>

## <div id="development">开发设置</div>

* 配置一个 `python=3.6`, `node>=11.3`, `npm>=6.5`, `tensorflowjs=0.8.0` 环境。

### 开发环境创建

* 通过以下方式可以快速创建一个 TensorSpace-Converter 开发环境：
```shell
git clone https://github.com/tensorspace-team/tensorspace-converter.git
cd tensorspace-converter
bash init-converter-dev.sh
npm install
```

### 构建 pip 包

* 执行 build-pip-package.sh 来编译 TensorSpace-Converter `pip` 包（文件将会生成在 `dist` 目录下）：
```shell
bash build-pip-package.sh
```

* 安装测试生成的 `pip` 包：
```shell
pip install dist/tensorspacejs-VERSION-py3-none-any.whl
tensorspacejs_converter -v
```

### 测试

* 在执行测试之前，赋予测试脚本执行权限：

```shell
bash ./test/grandPermission.sh
```

* 执行 `test` 文件夹中的 end-to-end 测试脚本 （测试脚本需要在之前设置的开发环境中运行）：
```shell
npm run test
```

## <div id="contributors">开发人员</div>

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars3.githubusercontent.com/u/4524339?v=4" width="100px;"/><br /><sub><b>Chenhua Zhu</b></sub>](https://github.com/zchholmes)<br />[💻](https://github.com/tensorspace-team/tensorspace-converter/commits?author=zchholmes "Code") [🎨](#design-zchholmes "Design") [📖](https://github.com/tensorspace-team/tensorspace-converter/commits?author=zchholmes "Documentation") [💡](#example-zchholmes "Examples") | [<img src="https://avatars2.githubusercontent.com/u/7977100?v=4" width="100px;"/><br /><sub><b>syt123450</b></sub>](https://github.com/syt123450)<br />[💻](https://github.com/tensorspace-team/tensorspace-converter/commits?author=syt123450 "Code") [🎨](#design-syt123450 "Design") [📖](https://github.com/tensorspace-team/tensorspace-converter/commits?author=syt123450 "Documentation") [💡](#example-syt123450 "Examples") | [<img src="https://avatars2.githubusercontent.com/u/19629037?v=4" width="100px;"/><br /><sub><b>Qi(Nora)</b></sub>](https://github.com/lq3297401)<br />[🎨](#design-lq3297401 "Design") | [<img src="https://avatars3.githubusercontent.com/u/25629006?s=400&v=4" width="100px;"/><br /><sub><b>BoTime</b></sub>](https://github.com/BoTime)<br />[💻](https://github.com/tensorspace-team/tensorspace-converter/commits?author=BoTime "Code") [💡](#example-BoTime "Examples") | [<img src="https://avatars0.githubusercontent.com/u/21956621?v=4" width="100px;"/><br /><sub><b>YaoXing Liu</b></sub>](https://charlesliuyx.github.io/)<br />[📖](https://github.com/tensorspace-team/tensorspace-converter/commits?author=CharlesLiuyx "Documentation") [🎨](#design-CharlesLiuyx "Design") |
| :---: | :---: | :---: | :---: | :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

## <div id="contact">联系方式</div>

若有任何疑问，欢迎通过以下方式联系我们：
* Email: tensorspaceteam@gmail.com
* GitHub Issues: [create issue](https://github.com/tensorspace-team/tensorspace-converter/issues/new)
* Slack: [#questions](https://tensorspace.slack.com/messages/CDSB58A5P)
* Gitter: [#Lobby](https://gitter.im/tensorspacejs/Lobby#)

## <div id="license">许可证</div>

[Apache License 2.0](https://github.com/tensorspace-team/tensorspace-converter/blob/master/LICENSE)