import sys
import argparse


# from keras_conversion import process_keras_model
from version import version


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
        '--input_type',
        type=str,
        required=False,
        default='keras',
        choices=set(['keras']),
        help='Input model type.\n'
             'It could be "keras", ... for now.'
    )
    parser.add_argument(
        '--input_format',
        type=str,
        required=False,
        default='keras_saved_model',
        choices=set(['keras_saved_model, keras_saved_weight']),
        help='Input format.\n'
             'For "keras_saved_model", input is .h5 saved by .save().\n'
             'For "keras_saved_weight", inputs are topology+weights.'
     )
    parser.add_argument(
        '--version',
        '-v',
        dest='show_version',
        action='store_true',
        help='Show versions of tensorspacejs and its dependencies'
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
        print('(TBD)')
        # print('  keras %s' % keras.__version__)
        # print('  tensorflow %s' % tf.__version__)
        return

    if FLAGS.input_path is None:
        raise ValueError(
            'Error: The input_path argument must be set. '
            'Run with --help flag for usage information.')

    print_hello_world()
    process_keras_model(sys.argv[1])


if __name__ == '__main__':
    main()