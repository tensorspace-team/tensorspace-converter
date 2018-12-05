import os

def remove_temp_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(file_path + ' does not exist.')


def valid_file(file_path):
    if not os.path.exists(file_path):
        print(file_path + ' does not exist.')
        return False
    if not os.path.isfile(file_path):
        print(file_path + ' is not a file.')
        return False
    return True


def valid_directory(dir_path):
    if not os.path.exists(dir_path):
        print(dir_path + ' does not exist.')
        return False
    if not os.path.isdir(dir_path):
        print(dir_path + ' is not a directory.')
        return False
    return True