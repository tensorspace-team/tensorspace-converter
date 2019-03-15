"""
@author syt123450 / https://github.com/syt123450
"""

import os
import subprocess
import tensorflow as tf


temp_model_name = '/enc_model.h5'


def preprocess_hdf5_separated_model(input_path, output_path, output_node_names):
    print("Preprocessing hdf5 separated model.")
    model = load_separate_model(input_path)

    temp_enc_model_path = output_path + temp_model_name
    enc_model = generate_encapsulate_model(model, output_node_names)
    save(enc_model, temp_enc_model_path)
    convert_h5_to_tfjs(temp_enc_model_path, output_path)
    remove_temp_enc_model(temp_enc_model_path)


def load_separate_model(input_path):
    print("Loading model into memory...")
    model_paths = input_path.split(",")
    with open(model_paths[0], 'r') as f:
        model = tf.keras.models.model_from_json(f.read())
    model.load_weights(model_paths[1])
    return model


def generate_encapsulate_model(model, output_layer_names):
    print("Generating multi-output encapsulated model...")
    layer_name_list = output_layer_names.split(",")
    display_model = tf.keras.models.Model(
        inputs=model.input,
        outputs=list(map(lambda oln: model.get_layer(oln).output, layer_name_list))
    )
    return display_model


def save(enc_model, output_path):
    print("Saving temp multi-output .h5 model...")
    enc_model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
    tf.keras.models.save_model(
        enc_model,
        output_path,
        overwrite=True,
        include_optimizer=True
    )


def convert_h5_to_tfjs(model_path, output_path):
    print("Converting .h5 to web friendly format...")
    subprocess.check_call([
        "tensorflowjs_converter",
        "--input_format=keras",
        model_path,
        output_path
    ])


def remove_temp_enc_model(model_path):
    print("Deleting temp .h5 model...")
    os.remove(model_path)
