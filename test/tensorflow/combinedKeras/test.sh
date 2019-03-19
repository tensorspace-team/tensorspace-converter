#!/usr/bin/env bash
python ./tensorspacejs/tsp_converters.py \
    --input_model_from="tensorflow" \
    --input_model_format="tf_keras" \
    --output_layer_names="conv_1,maxpool_1,conv_2,maxpool_2,dense_1,dense_2,softmax" \
    ./test/tensorflow/combinedKeras/tf_keras_model.h5 \
    ./test/output