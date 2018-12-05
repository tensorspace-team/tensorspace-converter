import os

def remove_temp_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(file_path + ' DNE.')