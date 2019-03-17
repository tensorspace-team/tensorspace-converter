import subprocess
import os


def install():
    print('Initializing TensorSpace Converter...')
    path_now = os.getcwd()
    tfjs_workspace = os.path.abspath(
        os.path.join(__file__, os.pardir, 'tfjs')
    )
    os.chdir(tfjs_workspace)
    subprocess.check_call([
        "npm",
        "install"
    ])
    os.chdir(path_now)
    pb2json_workspace = os.path.abspath(
        os.path.join(__file__, os.pardir, 'tf', 'pb2json')
    )
    os.chdir(pb2json_workspace)
    subprocess.check_call([
        "npm",
        "install"
    ])
    os.chdir(path_now)
    print('TensorSpace Converter Initialization Completed!')
