import subprocess

input_format_config = '--input_format=tf_frozen_model'


def preprocess_frozen_model(input_path, output_path, output_node_names):
    print("preprocessing tensorflow frozen model...")
    subprocess.check_call([
        "tensorflowjs_converter",
        input_format_config,
        "--output_node_names=" + output_node_names,
        "--saved_model_tags=serve",
        input_path,
        output_path
    ])
