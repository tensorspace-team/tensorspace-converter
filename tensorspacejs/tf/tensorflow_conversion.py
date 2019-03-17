"""
@author syt123450 / https://github.com/syt123450
"""

from tf.saved_model import preprocess_saved_model
from tf.frozen_model import preprocess_frozen_model
from tf.hdf5_combined_model import preprocess_hdf5_combined_model
from tf.hdf5_separated_model import preprocess_hdf5_separated_model


def show_tf_model_summary(path_model):
    print(path_model)
    print("tensorflow Model Summary...")


def preprocess_tensorflow_model(input_format, path_model, path_output_dir, output_node_names=None):
    if input_format == "tf_saved":
        preprocess_saved_model(
            path_model,
            path_output_dir,
            output_node_names
        )
    elif input_format == "tf_frozen":
        preprocess_frozen_model(
            path_model,
            path_output_dir,
            output_node_names
        )
    elif input_format == "tf_keras":
        preprocess_hdf5_combined_model(
            path_model,
            path_output_dir,
            output_node_names
        )
    elif input_format == "tf_keras_separated":
        preprocess_hdf5_separated_model(
            path_model,
            path_output_dir,
            output_node_names
        )
    else:
        print("Preprocess nothing for tensorflow model.")

    print("Mission Complete!!!")
