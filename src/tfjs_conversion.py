import subprocess

def main():
    # subprocess.call(["ls", "-l"])
    # subprocess.call(["echo", "Hello World~"])
    subprocess.check_call(["echo", "Hello World~"])
    subprocess.check_call(["pwd"], shell=True)

    # main_js_path = "/Users/zchholmes/PycharmProjects/tensorspacejs/src/tfjs/main.js"
    # output_names = "--output_layer_names='myPadding/myConv1/myMaxPooling1/myConv2/myMaxPooling2/myDense1/myDense2/myDense3'"
    # path_input = "/Users/zchholmes/PycharmProjects/tensorspacejs/test/tfjs/model/mnist.json"
    # path_output = "/Users/zchholmes/PycharmProjects/tensorspacejs/test/tfjs"
    # subprocess.check_call(["node", main_js_path, output_names, path_input, path_output])

    subprocess.check_call(['sh', './test/tfjs/model/test'])





if __name__ == '__main__':
    main()