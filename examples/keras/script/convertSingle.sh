#!/usr/bin/env bash
tensorspacejs_converter \
--input_type="keras" \
--input_format="keras_saved_model" \
--output_node_names='Conv2D_1,MaxPooling2D_1,Conv2D_2,MaxPooling2D_2,Dense_1,Dense_2,Softmax' \
../singleModel/mnist.h5 \
../generatedModel/