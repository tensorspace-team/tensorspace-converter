#!/usr/bin/env bash
python ./src/tsp_converters.py \
--input_type="tensorflow" \
--input_format="tf_saved_model" \
--output_node_names="MyConv2D_1,MyMaxPooling2D_1,MyConv2D_2,MyMaxPooling2D_2,MyDense_1,MyDense_2,MySoftMax" \
./test/tensorflow/savedModel \
./test/tensorflow