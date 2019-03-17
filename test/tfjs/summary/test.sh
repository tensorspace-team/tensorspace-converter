#!/usr/bin/env bash
python ./tensorspacejs/tsp_converters.py \
    --input_model_from="tfjs" \
    --summary \
    ./test/tfjs/summary/mnist.json