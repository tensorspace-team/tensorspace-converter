import sys

from keras_conversion import process_keras_model


def print_hello_world():
    print("Hello World from converter")


def main():
    print_hello_world()
    process_keras_model(sys.argv[1])


if __name__ == '__main__':
    main()