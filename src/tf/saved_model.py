import subprocess

input_format_config = '--input_format=tf_saved_model'


def preprocess_saved_model(input_path, output_path, output_node_names):
    print("preprocess tensorflow saved model...")
    subprocess.check_call([
        "tensorflowjs_converter",
        input_format_config,
        "--output_node_names=" + output_node_names,
        "--saved_model_tags=serve",
        input_path,
        output_path
    ])
