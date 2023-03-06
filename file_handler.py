import json
import os


def read_json_file(dir_location, file_name):
    file_path = os.path.join(dir_location, file_name)

    if os.path.exists(file_path) and os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Data read from file '{file_name}' at '{dir_location}'.")
            return data
    else:
        print(f"File '{file_name}' does not exist or is not readable. Cancelling operation.")
        return None



def write_json_file(dir_location, file_name, data, overwrite_file):
    file_path = os.path.join(dir_location, file_name)

    if os.path.exists(file_path) and os.access(file_path, os.R_OK):
        if os.path.isfile(file_path):
            if not overwrite_file:
                print(f"File '{file_name}' already exists and overwrite_file is False. Cancelling operation.")
                return False
        else:
            print(f"'{file_path}' is not a file. Cancelling operation.")
            return False

    with open(file_path, 'w' if overwrite_file else 'x') as file:
        json.dump(data, file)
        print(f"Data written to file '{file_name}' at '{dir_location}'.")
        return True
