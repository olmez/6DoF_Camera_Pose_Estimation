import yaml
import os
from pathlib import PurePath
from .printer_functions import Bcolors


def list_directories(path: str):
    directory_list = []
    for directory_name in os.listdir(str(PurePath(path))):
        directory_list.append(str(PurePath(path, directory_name)))
    return directory_list


def read_dict_from_yaml(path: PurePath):
    try:
        with open(str(path), "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except (FileNotFoundError, FileExistsError, TypeError):
        Bcolors.fail(f"Could not read the file:{str(path)}")
        return
