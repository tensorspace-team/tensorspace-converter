"""
@author syt123450 / https://github.com/syt123450
"""

import subprocess
import os
import shutil
from tf.pb2json.pb2json_conversion import convert


input_format_config = '--input_format=tf_frozen_model'


def preprocess_frozen_model(input_path, output_path, output_node_names):
    print("preprocessing tensorflow frozen model...")
    if not os.path.isdir:
        os.mkdir(output_path + '/tmp')
    subprocess.check_call([
        "tensorflowjs_converter",
        input_format_config,
        "--output_node_names=" + output_node_names,
        "--saved_model_tags=serve",
        input_path,
        output_path + '/tmp'
    ])
    path_now = os.getcwd()
    os.chdir(output_path)
    absolute_output_path = os.getcwd()
    absolute_output_path_temp = absolute_output_path + '/tmp/'
    os.chdir(path_now)
    convert(
        absolute_output_path_temp,
        absolute_output_path
    )
    shutil.rmtree(absolute_output_path_temp)
