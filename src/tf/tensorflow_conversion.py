import subprocess


def show_tf_model_summary(path_model):
    print(path_model)
    print("tensorflow Model Summary...")


def preprocess_tensorflow_model(input_format, path_model, path_output_dir, output_node_names=None):
    if input_format == "tf_saved_model":
        preprocess_saved_model(path_model, path_output_dir, output_node_names)
    elif input_format == "frozen_model":
        preprocess_frozen_model()
    elif input_format == "tf_keras_saved_model":
        preprocess_tf_keras_saved_model()
    elif input_format == "tf_keras_saved_weight":
        preprocess_tf_keras_weights_model()
    else:
        print("Preprocess nothing for tensorflow model.")


def preprocess_saved_model(input_path, output_path, output_node_names):
    print("preprocess tensorflow saved model...")
    input_format_config = '--input_format=tf_saved_model'
    subprocess.check_call([
        "tensorflowjs_converter",
        input_format_config,
        "--output_node_names=" + output_node_names,
        "--saved_model_tags=serve",
        input_path,
        output_path
    ])


def preprocess_frozen_model():
    print("preprocess frozen model")


def preprocess_tf_keras_saved_model():
    print("preprocess tf.keras saved model")


def preprocess_tf_keras_weights_model():
    print("preprocess tf.keras weights model")
