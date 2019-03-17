#!/usr/bin/env bash
python ./tensorspacejs/tsp_converters.py \
    --input_model_from="tfjs" \
    ./test/tfjs/sequential/mnist.json \
    ./test/tfjs