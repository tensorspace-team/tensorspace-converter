#!/usr/bin/env bash
python ./src/tsp_converters.py \
--input_type="keras" \
--input_format="keras_saved_model" \
--output_node_names='Conv2D_1/MaxPooling2D_1/Conv2D_2/MaxPooling2D_2/flatten_1/Dense_1/Dense_2/Softmax' \
./test/keras/savedModel/keras_model.h5 \
./test/keras/savedModel