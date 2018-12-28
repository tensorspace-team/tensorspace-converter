def show_tf_model_summary(path_model):
    print(path_model)
    print("tensorflow Model Summary...")


def preprocess_tensorflow_model(input_format, path_model, path_output_dir, output_node_names=None):
    if input_format == "saved_model":
        preprocess_saved_model(path_model, path_output_dir, output_node_names)
    elif input_format == "frozen_model":
        preprocess_frozen_model()
    elif input_format == "tf_keras_saved_model":
        preprocess_tf_keras_saved_model()
    elif input_format == "tf_keras_saved_weight":
        preprocess_tf_keras_weights_model()
    else:
        print("Preprocess nothing for tensorflow model.")


def preprocess_saved_model(path_model, path_output_dir, output_node_names):
    print("preprocess saved model")


def preprocess_frozen_model():
    print("preprocess frozen model")


def preprocess_tf_keras_saved_model():
    print("preprocess tf.keras saved model")


def preprocess_tf_keras_weights_model():
    print("preprocess tf.keras weights model")
