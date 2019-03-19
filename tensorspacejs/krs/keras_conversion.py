"""
@author zchholmes / https://github.com/zchholmes
@author syt123450 / https://github.com/syt123450
"""

import os
from krs.keras_model import show_keras_model_summary, show_summary_weights, preprocess_from_model, preprocess_from_weights


def preprocess_keras_model(input_format, path_model, path_output_dir, output_node_names=None):
    os.makedirs(path_output_dir, exist_ok=True)
    if input_format == "topology_weights_combined":
        preprocess_from_model(
            path_model,
            path_output_dir,
            output_node_names
        )
    elif input_format == "topology_weights_separated":
        model_paths = path_model.split(",")
        preprocess_from_weights(
            model_paths[0],
            model_paths[1],
            path_output_dir,
            output_node_names
        )

    print("Mission Complete!!!")


def show_keras_model_summary(input_format, path_model):
    if input_format == "topology_weights_combined":
        show_keras_model_summary(path_model)
    elif input_format == "topology_weights_separated":
        model_paths = path_model.split(",")
        show_summary_weights(
            model_paths[0],
            model_paths[1]
        )
