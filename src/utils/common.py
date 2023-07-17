import os
import pickle
import shutil
import sys
from pathlib import Path

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from src import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")


@ensure_annotations
def remove_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
                if verbose:
                    logger.info(f"removed directory at: {path}")
            else:
                if os.path.isfile(path):
                    os.remove(path)
                    if verbose:
                        logger.info(f"removed file at: {path}")
                        

def save_object(obj, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
            
    except Exception as e:
        logger.exception(e)
        raise e


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logger.exception(e)
        raise e
