import subprocess

def main():
    # subprocess.call(["ls", "-l"])
    # subprocess.call(["echo", "Hello World~"])
    subprocess.check_call(["echo", "Hello World~"])
    subprocess.check_call(["pwd"])

    main_js_path = "/Users/zchholmes/PycharmProjects/tensorspacejs/src/tfjs/main.js"
    output_names = "--output_layer_names='myPadding/myConv1/myMaxPooling1/myConv2/myMaxPooling2/myDense1/myDense2/myDense3'"
    path_input = "/Users/zchholmes/PycharmProjects/tensorspacejs/src/tfjs/test/sequential/mnist.json"
    path_output = "/Users/zchholmes/PycharmProjects/tensorspacejs/src/tfjs/test"
    subprocess.check_call(["node", main_js_path, output_names, path_input, path_output])



if __name__ == '__main__':
    main()