"""
@author zchholmes / https://github.com/zchholmes
@author syt123450 / https://github.com/syt123450
"""

import argparse
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            __file__, os.pardir
        )
    )
)

from tf.tensorflow_conversion import show_tf_model_summary, preprocess_tensorflow_model
from krs.keras_conversion import show_keras_model_summary, preprocess_keras_model
from tfjs.tfjs_conversion import show_tfjs_model_summary, process_tfjs_model
from install import install
from version import version
from version import python_version
from version import node_version
from version import tensorflowjs_version


def print_hello_world():
    print("Hello World from converter")


def main():
    parser = argparse.ArgumentParser('TensorSpace.js model converter/preprocessor.')
    parser.add_argument(
        'input_path',
        nargs='?',
        type=str,
        help='Path to the input file or directory. For input format "keras", '
             'an HDF5 (.h5) file or structure (.json) and weight (.hdf5) directory '
             'is expected.'
    )
    parser.add_argument(
        'output_path', nargs='?', type=str, help='Path for all output artifacts.'
    )
    parser.add_argument(
        '--input_model_from',
        type=str,
        required=False,
        default='keras',
        choices=set(['tensorflow', 'keras', 'tfjs']),
        help='Input model type.\n'
             'It could be "tensorflow", "keras", "tfjs"'
    )
    parser.add_argument(
        '--input_model_format',
        type=str,
        required=False,
        choices=set(['topology_weights_combined',
                     'topology_weights_separated',
                     'tf_saved',
                     'tf_frozen',
                     'tf_keras',
                     'tf_keras_separated']),
        help='Input format.\n'
             'For "topology_weights_combined", config for Keras model, input is .h5 saved by .save().\n'
             'For "topology_weights_separated", config for Keras model, inputs are topology+weights.\n'
             'For "tf_saved", config for TensorFlow model, input is TensorFlow saved model.\n'
             'For "tf_frozen", config for TensorFlow model, input is TensorFlow frozen model.\n'
             'For "tf_keras", config for TensorFlow model, input is .h5 model.\n'
             'For "tf_keras_separated", config for TensorFlow model, input is topology+weights.'
    )
    parser.add_argument(
        '--output_layer_names',
        type=str,
        help='The names of the output nodes, separated by slash. '
             'E.g., "logits/activations".')
    parser.add_argument(
        '--version',
        '-v',
        '-V',
        dest='show_version',
        action='store_true',
        help='Show versions of tensorspacejs and its dependencies'
    )
    parser.add_argument(
        '-init',
        dest='init',
        action='store_true',
        help='Init TensorSpace Converter'
    )
    parser.add_argument(
        '--summary',
        '-s',
        dest='show_model_summary',
        action='store_true',
        help='Show summray of loaded model'
    )

    flags = parser.parse_args()

    if flags.show_version:
        print('\ntensorspacejs %s\n' % version)
        print('Dependency versions:')
        print('python %s' % python_version)
        print('node %s' % node_version)
        print('tensorflowjs %s' % tensorflowjs_version)
        return

    if flags.init:
        install()
        return

    if flags.input_path is None:
        raise ValueError(
            'Error: The input_path argument must be set. '
            'Run with --help flag for usage information.')

    if flags.input_model_from not in ('tensorflow', 'keras', 'tfjs'):
        raise ValueError(
            'The --input_model_from flag can only be set to '
            '"tensorflow", "keras", "tfjs" '
            'but the current input type is "%s".' % flags.input_model_from)

    if flags.input_model_from == 'keras'\
            and flags.input_model_format not in (
            'topology_weights_combined',
            'topology_weights_separated'):
        raise ValueError(
            'For input_model_from == "keras", the --input_model_format flag can only be set to'
            '"topology_weights_combined" and "topology_weights_separated" '
            'but the current input model format is "%s".' % flags.input_model_format)

    if flags.input_model_from == 'tensorflow'\
            and flags.input_model_format not in (
            'tf_saved',
            'tf_frozen',
            'tf_keras',
            'tf_keras_separated'):
        raise ValueError(
            'For input_model_from == "tensorflow", the --input_model_format flag can only be set to'
            '"tf_saved", "tf_frozen", "tf_checkpoint_model", "tf_keras", "tf_keras_separated" '
            'but the current input model format is "%s".' % flags.input_model_format)

    if flags.show_model_summary:
        if flags.input_model_from == 'keras':
            show_keras_model_summary(flags.input_path)
            return
        if flags.input_model_from == 'tensorflow':
            show_tf_model_summary(flags.input_path)
            return
        if flags.input_model_from == "tfjs":
            show_tfjs_model_summary(flags.input_path)
            return
        return

    if flags.input_model_from == 'tensorflow':
        preprocess_tensorflow_model(
            flags.input_model_format,
            flags.input_path,
            flags.output_path,
            flags.output_layer_names
        )
        return

    if flags.input_model_from == 'keras':
        preprocess_keras_model(
            flags.input_model_format,
            flags.input_path,
            flags.output_path,
            flags.output_layer_names
        )
        return

    if flags.input_model_from == 'tfjs':
        process_tfjs_model(
            flags.input_path,
            flags.output_path,
            flags.output_layer_names
        )
        return

    print("Nothing happened...")


if __name__ == '__main__':
    main()
