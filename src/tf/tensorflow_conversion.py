import sys

sys.path.insert(0, "./src/tf")

from saved_model import preprocess_saved_model
from frozen_model import preprocess_frozen_model
from checkpoint_model import preprocess_checkpoint_model
from hdf5_combined_model import preprocess_hdf5_combined_model
from hdf5_separated_model import preprocess_hdf5_separated_model


def show_tf_model_summary(path_model):
    print(path_model)
    print("tensorflow Model Summary...")


def preprocess_tensorflow_model(input_format, path_model, path_output_dir, output_node_names=None):
    if input_format == "tf_saved_model":
        preprocess_saved_model(
            path_model,
            path_output_dir,
            output_node_names
        )
    elif input_format == "tf_frozen_model":
        preprocess_frozen_model()
    elif input_format == "tf_checkpoint_model":
        preprocess_checkpoint_model()
    elif input_format == "tf_hdf5_model":
        preprocess_hdf5_combined_model()
    elif input_format == "tf_hdf5_separated_model":
        preprocess_hdf5_separated_model()
    else:
        print("Preprocess nothing for tensorflow model.")

    print("Mission Complete!!!")
