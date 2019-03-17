#!/usr/bin/env bash
python ./tensorspacejs/tsp_converters.py \
    --input_model_from="keras" \
    --input_model_format="topology_weights_combined" \
    ./test/keras/combined/keras_seq_model.h5 \
    ./test/keras