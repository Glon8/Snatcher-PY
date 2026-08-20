import copy
import os
import sys
import json

from pathlib import Path

from .values import op


# ===================================< SWITCH
# dic - dictionary to use
# key - from the dictionary to flip
def switch(dic, key):
    dic[key] = 1 - dic[key]


# ===================================< FILES COUNT
def files_count(file_path):
    return sum(len(files) for _, _, files in os.walk(file_path))


# ===================================< GET DIRECTORY
def getDir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.executable))

    return str(Path(__file__).resolve().parent.parent)


# ===================================< WRITE FILE
def write_file(file_path, file_name, data):
    if not isinstance(file_path, str) or not os.path.exists(file_path):
        return None

    with open(f'{file_path}/{file_name}', 'w') as file:
        json.dump(data, file, indent=4)


# ===================================< READ FILE
# file_path - to read from
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None


# ===================================< PATH MTIME (snt)
# folder_path - to check mtime for
def dir_mtime(folder_path):
    newest = 0

    for root, dirs, files in os.walk(folder_path):
        try:
            newest = max(newest, os.path.getmtime(root))
        except OSError:
            pass;

        for file in files:
            path = os.path.join(root, file)
            try:
                mtime = os.path.getmtime(path)
                if mtime > newest:
                    newest = mtime
            except OSError:
                pass

    return newest


# ===================================< CONFIG PARSER
# string - to pars in to config
def config_parse(string):
    if string == '' or string is None:
        write_file(getDir(), 'config.json', op)
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    for name, value in config_pack.items():
        for key, val in value.items():
            if key != 'name' and name != 'ks':
                op[name][key] = val


# ===================================< CONFIG PARSER ON REREAD
# string - to pars in to config
def config_parse_reread(string):
    if string == '' or string is None:
        return

    config_pack = json.loads(string)

    copy_op = copy.deepcopy(op)
    copy_op['ks'].pop('stat')

    copy_conf = copy.deepcopy(config_pack)
    copy_conf['ks'].pop('stat')

    if copy_op == copy_conf:
        return

    valid_keys = ['display', '.positive_emoji', '.negative_emoji', 'key_trigger', 'path_from', 'path_to',
                  'self_replace']

    for name, value in config_pack.items():
        for key, val in value.items():
            if key in valid_keys and op[name][key] != val and name != 'ks':
                op[name][key] = val


# ===================================< UNICODE CONVERT

def unicode_convert(unicode):
    return chr(int(unicode[2:], 16))
