#!/usr/bin/env bash
python ./src/tsp_converters.py \
    --input_model_from="tensorflow" \
    --input_model_format="tf_keras_separated" \
    --output_layer_names="reshape_1,Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,flatten_1,Dense_1,Dense_2,Softmax" \
    ./test/tensorflow/separatedKeras/topology.json,./test/tensorflow/separatedKeras/weights.h5 \
    ./test/tensorflow