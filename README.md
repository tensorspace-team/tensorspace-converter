<p align="center">
<img width=150 src="https://raw.githack.com/tensorspace-team/tensorspace/master/assets/logo_tsConverter.png">
</p>
<h1 align="center">TensorSpace Converter</h1>

<p align="center">
<strong>English</strong> | <a href="https://github.com/tensorspace-team/tensorspace-converter/blob/master/README_zh.md"><strong>中文</strong></a>
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

TensorSpace-Converter is a tool used to generate a TensorSpace compatible model from a pre-trained model built by TensorFlow, Keras and TensorFlow.js. TensorSpace-Converter includes the functions of: extracting information from hidden layers, matching intermediate data based on the configurations and exporting preprocessed TensorSpace compatible model. TensorSpace simplifies the preprocess and helps developers to focus on the development of model visualization.

## Table of Content

* [Motivation](#motivation)
* [Getting Started](#start)
    * [Install](#install)
    * [Usage](#usage)
* [Converter API](#api)
* [Converter Usage Examples](#examples)
    * [TensorFlow](#tensorflow)
    * [Keras](#keras)
    * [TensorFlow.js](#tensorflowjs)
* [Contributors](#contributors)
* [Contact](#contact)
* [License](#license)

## <div id="motivation">Motivation</div>

TensorSpace is a JavaScript framework used to 3D visualize pre-trained deep learning models built by TensorFlow, Keras and TensorFlow.js. Before applying TensorSpace to the pre-trained model, there is an important pipeline - TensorSpace model preprocessing ( Checkout this [article](https://tensorspace.org/html/docs/preIntro.html) for more information about TensorSpace preprocessing ). TensorSpace-Converter is designed to simplify the model preprocessing and generate a TensorSpace compatible model easily and quickly.

Without TensorSpace-Converter, the developer needs to be expert on the pre-trained model and machine learning library the model used. For example, if the developer has an LeNet pre-trained model built by Keras, it is required to know the structure of the LeNet network as well as how to implement a new multi-output model by Keras. Now, with TensorSpace-Converter, it only needs some commands to complete the preprocessing process. For example, the developer only needs to use the [commands](#keras) to preprocess a Keras pre-trained model.

As a component of TensorSpace ecosystem, TensorSpace-Converter simplifies the TensorSpace preprocess, release the workloads from learning how to generate TensorSpace compatible model. As a development tool, TensorSpace-Converter helps to separate the work of `model training` and `model visuailization`.

<p align="center">
<img width="100%" src="https://raw.githack.com/tensorspace-team/tensorspace/master/assets/tensorspace_lenet.gif">
</p>
<p align="center">
<b>Fig. 1</b> - TensorSpace LeNet
</p>

<p align="center">
<img width="100%" src="https://tensorspace.org/assets/img/docs/General/intro_preprocess_m.png">
</p>
<p align="center">
<b>Fig. 2</b> - TensorSpace Preprocess Concept
</p>

## <div id="start">Getting Started</div>

### <div id="install">Install</div>

Install the tensorspacejs pip package:

```shell
$ pip install tensorspacejs
```

If `tensorspacejs` is installed successfully, you can check the TensorSpace-Converter version by using the command:
```shell
$ tensorspacejs_converter -v
```

* **Note**

TensorSpace-Converter requires to run under Python 3.6, Node 11.3+. If you have other pre-installed Python version in your local environment, we suggest you to create a new virtual environment. For example, the <a href="https://anaconda.org/anaconda/conda">conda</a> commands is like:
```shell
$ conda create -n envname python=3.6
$ source activate envname
$ pip install tensorspacejs
```

### <div id="usage">Usage</div>
The following part introduces the usage and workflow on:
* how to use TensorSpace-Converter to convert a pre-trained model;
* how to apply TensorSpace to the converted model for model visualization.

An MNIST-digit Keras model is used as an example in the tutorial. The sample files used in the tutorial includes [pre-trained Keras model](), [TensorSpace-Converter script]() and [TensorSpace visualization code]().

#### Step 1: Use TensorSpace-Converter to preprocess pre-trained model

```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    --output_layer_names="Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,Dense_1,Dense_2,Softmax" \
    ./PATH/TO/MODEL/keras_MNIST_model.h5 \
    ./PATH/TO/SAVE/DIR
```
#### Step 2: Apply TensorSpace for model visualization

```javascript
model.load({
    type: "keras",
    url: "/PATH/TO/MODEL/model.json"
});
```

## <div id="api">Converter API</div>

Sample TensorSpace-Converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="XXX" \
    --input_model_format="YYY" \
    --output_layer_names="EEE1,EEE2,EEE3" \
    input_path \
    output_path
```

Arguments explanation:

|Positional Arguments | Description |
|---|---|
|`input_path`  | Full path of the saved model directory, session bundle directory, frozen model file or TensorFlow Hub module handle or path.|
|`output_path` | Path for all output artifacts.|


| Options | Description
|---|---|
|`--input_model_from`     | Configure the training library for pre-trained model, use: `tensorflow` for TensorFlow, `keras` for Keras, `tfjs` for TensorFlow.js |
|`--input_model_format`     | The format of input model, use |
|<nobr>`--output_layer_names`</nobr>| The names of the layer which will be visualized in TensorSpace, separated by comma ",". If not set, converter will export all layers. |

## <div id="examples">Converter Usage Examples</div>

This section introduces the usage of TensorSpace-Converter for different types of pre-trained model from TensorFlow, Keras, TensorFlow.js.

### <div id="tensorflow">TensorFlow</div>

A pre-trained model built by TensorFlow can be saved as saved model, frozen model, combined HDF5 model or separated HDF5 model. Use different TensorSpace-Converter commands for different kinds of TensorFlow model formats. TensorSpace-Converter collects the data from `tensor`, then use the outputs as the inputs of `layer` of TensorSpace visualization. The developer can collect all necessary tensor names and set the name list as `output_layer_names`.

For a combined HDF5 model, topology and weights are saved in a combined HDF5 file `xxx.h5`. Set `input_model_format` to be `tf_hdf5_model`. The sample command script should be like:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_hdf5_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.h5 \
    ./PATH/TO/SAVE/DIR
```

For a separated HDF5 model, topology and weights are saved in separate files, topology file `xxx.json` and weights file `xxx.hdf5`. Set `input_model_format` to be `tf_hdf5_separated_model`. In this case, the model have two input files, merge two file's paths and separate them with comma (.json first, .hdf5 last), and then set the combined path to positional argument `input_path`. The sample command script should be like:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_hdf5_separated_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json,./PATH/TO/MODEL/eee.h5 \
    ./PATH/TO/SAVE/DIR
```

For a TensorFlow saved model. Set `input_model_format` to be `tf_saved_model`. The sample command script should be like:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_saved_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/SAVED/MODEL/FOLDER \
    ./PATH/TO/SAVE/DIR
```

For a TensorFlow frozen model. Set `input_model_format` to be `tf_frozen_model`. The sample command script should be like:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_frozen_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.pb \
    ./PATH/TO/SAVE/DIR
```

Checkout this [TensorFlow Tutorial](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tensorflow) for more practical usage of TensorSpace-Converter for TensorFlow models.

### <div id="keras">Keras</div>

A pre-trained model built by Keras, may have two formats: topology and weights are saved in a single HDF5 file, or topology and weights are saved in separated files. Use different TensorSpace-Converter commands for these two saved Keras models.

For a Keras model, topology and weights are saved in a single HDF5 file, i.e. `xxx.h5`. Set `input_model_format` to be `topology_weights_combined`. The sample command script should be like:
```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.h5 \
    ./PATH/TO/SAVE/DIR
```

For a Keras model, topology and weights are saved in separated files, i.e. a topology file `xxx.json` and a weights file `xxx.hdf5`. Set `input_model_format` to be `topology_weights_separated`. In this case, the model have two input files, merge two file's paths and separate them with comma (.json first, .hdf5 last), and then set the combined path to positional argument `input_path`. The sample command script should be like:
```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_separated" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json,./PATH/TO/MODEL/eee.h5 \
    ./PATH/TO/SAVE/DIR
```
Checkout this [Keras Tutorial](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/keras) for more practical usage of TensorSpace-Converter for Keras models.

### <div id="tensorflowjs">TensorFlow.js</div>

A pre-trained model built by TensorFlow.js, may have a topology file `xxx.json` and a weights file `xxx.weight.bin`. To converter the model with TensorSpace-Converter, the two files should be put in the same folder and set topology file's path to `input_path`. The sample command script should be like:

```shell
$ tensorspacejs_converter \
    --input_model_from="tfjs" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json \
    ./PATH/TO/SAVE/DIR
```
Checkout this [TensorFlow.js tutorial](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tfjs) for more practical usage of TensorSpace-Converter for TensorFlow.js models.

## <div id="contributors">Contributors</div>

Thanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars3.githubusercontent.com/u/4524339?v=4" width="100px;"/><br /><sub><b>Chenhua Zhu</b></sub>](https://github.com/zchholmes)<br />[💻](https://github.com/tensorspace-team/tensorspace-converter/commits?author=zchholmes "Code") [🎨](#design-zchholmes "Design") [📖](https://github.com/tensorspace-team/tensorspace-converter/commits?author=zchholmes "Documentation") [💡](#example-zchholmes "Examples") | [<img src="https://avatars2.githubusercontent.com/u/7977100?v=4" width="100px;"/><br /><sub><b>syt123450</b></sub>](https://github.com/syt123450)<br />[💻](https://github.com/tensorspace-team/tensorspace-converter/commits?author=syt123450 "Code") [🎨](#design-syt123450 "Design") [📖](https://github.com/tensorspace-team/tensorspace-converter/commits?author=syt123450 "Documentation") [💡](#example-syt123450 "Examples") |
| :---: | :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

## <div id="contact">Contact</div>

If you have any issue or doubt, feel free to contact us by:
* Email: tensorspaceteam@gmail.com
* GitHub Issues: [create issue](https://github.com/tensorspace-team/tensorspace-converter/issues/new)
* Slack: [#questions](https://tensorspace.slack.com/messages/CDSB58A5P)
* Gitter: [#Lobby](https://gitter.im/tensorspacejs/Lobby#)

## <div id="license">License</div>

[Apache License 2.0](https://github.com/tensorspace-team/tensorspace-converter/blob/master/LICENSE)
