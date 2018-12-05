
from file_utility import remove_temp_file, valid_file, valid_directory
from keras import Model


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


def preprocess_from_model(path_model, path_output_dir, output_node_names):
    if (not valid_file(path_model)):
        print('Aboard converting... INVALID input file.')
        return
    if (not valid_directory(path_output_dir)):
        print('Aboard converting... INVALID output directory.')
        return

    model = load_from_saved_model(path_model)
    enc_model: Model = generate_encapsulate_model_with_output_layer_names(model, split_layer_name_list(output_node_names))

    # Generate temp Keras enc_model for further processing
    print("Saving enc_model...")
    save_enc_model(path_output_dir, enc_model)
    print("Saving converted tfjs model...")
    convert_tfjs(path_output_dir)
    print("Remove enc_model file...")
    remove_temp_file(path_output_dir+"/enc_model.h5")
    print("Mission Complete!!!")


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


def generate_encapsulate_model_with_output_layer_names(model, output_layer_names):
    from keras.models import Model
    enc_model = Model(
        inputs=model.input,
        outputs=list(map(lambda oln: model.get_layer(oln).output, output_layer_names))
    )
    return enc_model


def split_layer_name_list(output_node_names):
    return output_node_names.split("/")


def save_enc_model(path_output_dir, enc_model):
    from keras.models import save_model
    save_model(enc_model, path_output_dir+"/enc_model.h5")


def convert_tfjs(path_output_dir):
    from tensorflowjs.converters.converter import dispatch_keras_h5_to_tensorflowjs_conversion
    dispatch_keras_h5_to_tensorflowjs_conversion(
        path_output_dir+"/enc_model.h5",
        path_output_dir
    )
