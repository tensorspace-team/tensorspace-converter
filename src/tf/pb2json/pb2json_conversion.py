from utility.file_utility import valid_file, valid_directory, show_invalid_message

TS_NODE_BIN_PATH = './src/tf/pb2json/node_modules/.bin/ts-node'
CONVERTER_SCRIPT_PATH = './src/tf/pb2json/tools/pb2json_converter.ts'


def convert(path_input, path_output):
    print('pb to json')
    import subprocess
    subprocess.check_call(["node", TS_NODE_BIN_PATH, CONVERTER_SCRIPT_PATH, path_input, path_output])
