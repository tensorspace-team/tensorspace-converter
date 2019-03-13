<p align="center">
<img width=400 src="./img/tfjs.png">
</p>
<h1 align=center>TensorFlow.js 教程</h1>
<p align=center><b>使用 TensorSpace 和 TensorSpace-Converter 可视化 TensorFlow.js 模型</b></p>

## 简介

本教程展示如何使用 TensorSpace 和 TensorSpace-Converter 可视化 TensorFlow.js 模型。在接下来的教程中，可视化一个使用 MNIST 数据集和 LeNet 神经网络结构 构建的 TensorFlow.js 模型。

## 文件

以下为本篇教程所使用的代码及模型文件:

* TensorFlow.js 模型 ([mnist.json](https://github.com/tensorspace-team/tensorspace-converter/blob/master/examples/tfjs/originalModel/mnist.json) 和 [mnist.weight.bin](https://github.com/tensorspace-team/tensorspace-converter/blob/master/examples/tfjs/originalModel/mnist.weights.bin))
* [TensorSpace-Converter 预处理脚本](https://github.com/tensorspace-team/tensorspace-converter/blob/master/examples/tfjs/script/converter.sh)
* [TensorSpace 可视化代码](https://github.com/tensorspace-team/tensorspace-converter/blob/master/examples/tfjs/index.html)

## 预处理

首先我们将会使用 TensorSpace-Converter 对一个 TensorFlow.js 模型进行预处理:

```shell
$ tensorspacejs_converter \
    --input_model_from="tfjs" \
    --output_layer_names='myPadding,myConv1,myMaxPooling1,myConv2,myMaxPooling2,myDense1,myDense2,myDense3' \
    ../originalModel/mnist.json \
    ../generatedModel/
```

以上 TensorSpace-Converter 预处理脚本将会在 `generatedModel` 文件夹中生成经过预处理的模型。在本教程中，我们已经生成了经过预处理的模型，模型文件可以在 [这个文件夹](https://github.com/tensorspace-team/tensorspace-converter/tree/master/examples/tfjs/generatedModel) 中找到。

经过转化后，我们将会得到经过预处理的模型：
<p align="center">
<img src="./img/tfjs_created_model.png" alt="models" width="400" >
<br/>
<b>Fig. 1</b> - 经过预处理的模型
</p>

* 我们将会得到2种不同类型的文件：
    * `.json` 包含神经网络结构。
    * `.bin` 包含所训练得到的权重。

## 载入并可视化

通过 TensorSpace API 构建 TensorSpace 可视化模型。
```javascript
let model = new TSP.models.Sequential( modelContainer );

model.add( new TSP.layers.GreyscaleInput( { shape: [ 28, 28, 1 ] } ) );
model.add( new TSP.layers.Padding2d( { padding: [ 2, 2 ] } ) );
model.add( new TSP.layers.Conv2d( { kernelSize: 5, filters: 6, strides: 1 } ) );
model.add( new TSP.layers.Pooling2d( { poolSize: [ 2, 2 ], strides: [ 2, 2 ] } ) );
model.add( new TSP.layers.Conv2d( { kernelSize: 5, filters: 16, strides: 1 } ) );
model.add( new TSP.layers.Pooling2d( { poolSize: [ 2, 2 ], strides: [ 2, 2 ] } ) );
model.add( new TSP.layers.Dense( { units: 120 } ) );
model.add( new TSP.layers.Dense( { units: 84 } ) );
model.add( new TSP.layers.Output1d( {
    units: 10,
    outputs: [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
} ) );
```

载入经过 TensorSpace-Converter 预处理的模型，然后将模型进行初始化：
```javascript
model.load( {
    type: "tfjs",
    url: './generatedModel/model.json'
} );

model.init();
```

## 结果显示

若至此一切顺利，在浏览器中打开 `index.html`，将会看到以下模型：
<p align="center">
<img src="https://github.com/tensorspace-team/tensorspace/blob/master/assets/HelloWorld_5.jpg" alt="models" width="100%" >
<br/>
<b>图2</b> - TensorSpace LeNet 预测 "5"
</p>