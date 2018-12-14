#!/usr/bin/env bash
python ./src/tsp_converters.py \
--input_type="keras" \
--input_format="keras_saved_model" \
./test/keras/savedModel/keras_seq_model.h5 \
./test/keras/savedModel