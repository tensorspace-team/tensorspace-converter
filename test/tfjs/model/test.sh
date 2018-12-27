#!/usr/bin/env bash
python ./src/tsp_converters.py \
--input_type="tfjs" \
--output_node_names='myPadding,myConv1,myMaxPooling1,myConv2,myMaxPooling2,myDense1,myDense2,myDense3' \
./test/tfjs/model/mnist.json \
./test/tfjs