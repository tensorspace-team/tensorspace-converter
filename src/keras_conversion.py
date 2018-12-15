
from file_utility import remove_file, valid_file, valid_directory


def show_summary(model):
    model.summary()


def show_summary_model(path_model):
    print("show summary of keras saved model...")
    model = load_from_saved_model(path_model)
    show_summary(model)


def show_summary_weights(path_topology, path_weights):
    print("show summary of keras saved topology + weights...")
    model = load_from_saved_weights(path_topology, path_weights)
    show_summary(model)


def load_from_saved_model(path_model):
    from keras.models import load_model
    model = load_model(path_model)
    return model


def load_from_saved_weights(path_topology, path_weights):
    from keras.models import model_from_json
    structure = open(path_topology, "r")
    model = model_from_json(structure)
    model.load_weights(path_weights)
    return model


def generate_encapsulate_model(model, output_layer_names=None):
    """Generate an encapsulate model
        The new encapsulate model includes:
        1. model.inputs from original model as enc_model.inputs
        2. enc_model.outputs has two parts:
            2.1 transferred identity tensors from original inputs (implemented by Lambda)
            2.2 tensors from original model
                2.2.1 default to all tensors from original model
                2.2.2 based on provided output_layer_names to look up specified layer.output tensors
    """
    from keras.models import Model
    from keras.layers import Lambda

    transfer_inputs = list(map(lambda input: Lambda(lambda x: x)(input), model.inputs))
    if output_layer_names is None:
        transfer_outputs = list(map(lambda layer: layer.output, model.layers[1:]))
    else:
        transfer_outputs = list(map(lambda oln: model.get_layer(oln).output, output_layer_names))

    enc_model = Model(
        inputs=model.inputs,
        outputs=transfer_inputs+transfer_outputs
    )
    return enc_model


def split_layer_name_list(output_node_names):
    return output_node_names.split("/")


def save_enc_model(path_output_dir, enc_model):
    from keras.models import save_model
    print("Saving enc_model...")
    save_model(enc_model, path_output_dir+"/enc_model.h5")


def convert_tfjs(path_output_dir):
    from tensorflowjs.converters.converter import dispatch_keras_h5_to_tensorflowjs_conversion
    print("Saving converted tfjs model...")
    dispatch_keras_h5_to_tensorflowjs_conversion(
        path_output_dir + "/enc_model.h5",
        path_output_dir
    )


def clean_temp_file(path_output_dir):
    print("Remove enc_model file...")
    remove_file(path_output_dir + "/enc_model.h5")


def preprocess_from_model(path_model, path_output_dir, output_node_names=None):
    if (not valid_file(path_model)):
        print('Aboard converting... INVALID input file.')
        return
    if (not valid_directory(path_output_dir)):
        print('Aboard converting... INVALID output directory.')
        return

    model = load_from_saved_model(path_model)
    enc_model = generate_encapsulate_model(model, split_layer_name_list(output_node_names))

    # Generate temp Keras enc_model for further processing
    save_enc_model(path_output_dir, enc_model)
    convert_tfjs(path_output_dir)
    clean_temp_file(path_output_dir)
    print("Mission Complete!!!")
