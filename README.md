<p align="center">
<img width=150 src="https://raw.githack.com/tensorspace-team/tensorspace/master/assets/logo_christmasHat.png">
</p>
<h1 align="center">TensorSpace Converter</h1>

<p align="center">
<strong>English</strong> | <a href="https://github.com/tensorspace-team/tensorspace/blob/master/README_zh.md"><strong>中文</strong></a>
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

TensorSpace-Converter is a TensorSpace preprocess tool for pre-trained model from TensorFlow, Keras, TensorFlow.js. TensorSpace-Converter can extract hidden layer value from a pre-trained model and generate a new multi-output model for TensorSpace 3D visualization. TensorSpace-Converter steeps the learning curve of TensorSpace preprocessing. Using TensorSpace-Converter in development, it is possible to separate the work of model training and model visualization.

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

TensorSpace is a 3D visualization framework for pre-trained deep learning models from TensorFlow, Keras, TensorFlow.js. Before applying TensorSpace, there is an important pipeline —— preprocessing the pre-trained model ( Checkout this [article](https://tensorspace.org/html/docs/preIntro.html) for more information about TensorSpace preprocessing ). TensorSpace-Converter is designed for TensorSpace users to quickly accomplish the TensorSpace Preprocessing.

TensorSpace-Converter out-of-the-box supports preprocessing different formats of pre-trained model from TensorFlow, Keras, TensorFlow.js. It only takes several lines of TensorSpace-Converter codes to preprocess a pre-trained model. Before TensorSpace-Converter, to preprocess a pre-trained model for TensorSpace, developers shall master some frameworks, such as TensorFlow, Keras, tfjs-converter. For example, before TensorSpace-Converter, when preprocessing a Keras model, developers need to prepare a pre-trained Keras model, write some Keras codes to get a new multi-output model, and then use tfjs-converter to convert the multi-output model to a TensorSpace compatible format. By applying TensorSpace-Converter, it just takes [6 lines](#keras) of TensorSpace-Converter commands to do the same thing.

As a component of TensorSpace ecosystem, TensorSpace-Converter simplify the TensorSpace preprocessing, steeps the learning curve of TensorSpace. As a development tool, TensorSpace-Converter makes it possible to separate the work of `backend model training` and `frontend model visualization`.

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

If successfully downloading `tensorspacejs`, you can check the TensorSpace-Converter version in command line:
```shell
$ tensorspacejs_converter -v
```

* **Note**

TensorSpace-Converter must run under Python 3.6, Node 11.3+. If you have other pre-installed Python version in your local environment, we suggest you to use `Conda` to create a pure Python 3.6 virtual environment.

```shell
$ conda create -n envname python=3.6
```

### <div id="usage">Usage</div>

Then we will introduce the usage and workflow of using TensorSpace and TensorSpace-Converter to convert a pre-trained model and visualizing pre-processed model with TensorSpace. And we will preprocess and visualize a MNIST-digit Keras model.

The sample files used in this tutorial includes [pre-trained Keras model](), [TensorSpace-Converter script]() and [TensorSpace visualization code]().

#### Step 1: Use TensorSpace-Converter preprocess pre-trained model

```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    --output_layer_names="Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,Dense_1,Dense_2,Softmax" \
    ./PATH/TO/MODEL/keras_MNIST_model.h5 \
    ./PATH/TO/SAVE/DIR
```

#### Step 2: Load preprocessed into TensorSpace visualization model

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

A pre-trained model built with TensorFlow, may be saved as saved model, frozen model, checkpoint model, combined HDF5 model or separated HDF5 model. Use different TensorSpace-Converter commands for different kinds of TensorFlow model formats. A TensorFlow graph may not have `layer` concept, however, a specific `tensor` can be corresponding a `layer` for TensorSpace visualization, collect all these tensor names and set the name list to `output_layer_names`.

For a TensorFlow saved model. Set `input_model_format` to be `tf_saved_model`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_saved_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    input_path \
    ./PATH/TO/SAVE/DIR
```

For a TensorFlow frozen model. Set `input_model_format` to be `tf_frozen_model`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_frozen_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    input_path \
    ./PATH/TO/SAVE/DIR
```

For a TensorFlow checkpoint model. Set `input_model_format` to be `tf_checkpoint_model`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_checkpoint_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    input_path \
    ./PATH/TO/SAVE/DIR
```

For a combined HDF5 model, topology and weights are saved in a combined HDF5 file `xxx.h5`. Set `input_model_format` to be `tf_hdf5_model`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_hdf5_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.h5 \
    ./PATH/TO/SAVE/DIR
```

For a separated HDF5 model, topology and weights are saved in separate files, topology file `xxx.json` and weights file `xxx.hdf5`. Set `input_model_format` to be `tf_hdf5_separated_model`. In this case, the model have two input files, merge two file's paths and separate them with comma (.json first, .hdf5 last), and then set the combined path to positional argument `input_path`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="tensorflow" \
    --input_model_format="tf_hdf5_separated_model" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json,./PATH/TO/MODEL/eee.hdf5 \
    ./PATH/TO/SAVE/DIR
```
Checkout this [TensorFlow Tutorial](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tensorflow) for more practical usage of TensorSpace-Converter for TensorFlow models.

### <div id="keras">Keras</div>

A pre-trained model built with Keras, may have two formats: topology and weights in a combined HDF5 file or topology and weights in separated files. Use different TensorSpace-Converter commands for these two keras model formats.

For a Keras model, topology and weights are saved in a combined HDF5 file `xxx.h5`. Set `input_model_format` to be `topology_weights_combined`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.h5 \
    ./PATH/TO/SAVE/DIR
```

For a Keras model, topology and weights are saved in separated files, a topology file `xxx.json` and a weights file `xxx.hdf5`. Set `input_model_format` to be `topology_weights_separated`, in this case, the model have two input files, merge two file's paths and separate them with comma (.json first, .hdf5 last), and then set the combined path to positional argument `input_path`. Demo converter script:
```shell
$ tensorspacejs_converter \
    --input_model_from="keras" \
    --input_model_format="topology_weights_separated" \
    --output_layer_names="layer1Name,layer2Name,layer3Name" \
    ./PATH/TO/MODEL/xxx.json,./PATH/TO/MODEL/eee.hdf5 \
    ./PATH/TO/SAVE/DIR
```
Checkout this [Keras Tutorial](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/keras) for more practical usage of TensorSpace-Converter for Keras models.

### <div id="tensorflowjs">TensorFlow.js</div>

A pre-trained model built with TensorFlow.js, may have a topology file `xxx.json` and a weights file `xxx.weight.bin`. To converter the model with TensorSpace-Converter, put two files in the same folder and set topology file's path to `input_path`. Demo converter script:

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