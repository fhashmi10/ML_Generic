"""Module to hold all common util methods"""
import os
import shutil
from pathlib import Path
import json
import pickle
import yaml
from box import ConfigBox, exceptions

from src import logger


@staticmethod
def read_yaml_dict(path_to_yaml: Path) -> dict:
    """Method to read yaml and return a dict instance"""
    try:
        with open(path_to_yaml, encoding='utf8') as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            if yaml_content is None:
                raise IOError
            logger.info("yaml file loaded successfully: %s", path_to_yaml)
            return yaml_content
    except FileNotFoundError as ex:
        logger.exception("yaml file not found: %s", path_to_yaml)
        raise ex
    except IOError as ex:
        logger.exception("yaml file is empty: %s", path_to_yaml)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def read_yaml_configbox(path_to_yaml: Path) -> ConfigBox:
    """Method to read yaml and return a ConfigBox instance
    A configbox helps in accessing yaml contents with . syntax"""
    try:
        with open(path_to_yaml, encoding='utf8') as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            logger.info("yaml file loaded successfully: %s", path_to_yaml)
            return ConfigBox(yaml_content)
    except exceptions.BoxValueError as ex:
        logger.exception("yaml file is empty: %s", path_to_yaml)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def create_directories(path_to_directories: list, is_file_path=False):
    """Method to create directories"""
    try:
        for dir_path in path_to_directories:
            if not os.path.exists(dir_path):
                if is_file_path:
                    dir_path = os.path.dirname(os.path.abspath(dir_path))
                os.makedirs(dir_path, exist_ok=True)
                logger.info("created directory at %s:", dir_path)
    except IOError as ex:
        logger.exception("Error creating directories: %s", path_to_directories)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def remove_directories(path_to_directories: list):
    """Method to remove directories"""
    try:
        for path in path_to_directories:
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    logger.info("removed directory at %s:", path)
                elif os.path.isfile(path):
                    os.remove(path)
                    logger.info("removed file at %s:", path)
    except IOError as ex:
        logger.exception("Error removing directories: %s", path_to_directories)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def save_object(obj, file_path: Path):
    """Method to save an object to a file"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except IOError as ex:
        logger.exception("Error saving object at: %s", file_path)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def load_object(file_path: Path):
    """Method to load an object from a file"""
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except IOError as ex:
        logger.exception("Error loading object from: %s", file_path)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def save_json(file_path: Path, data: dict):
    """Method to dump data to a json file"""
    try:
        create_directories([file_path], is_file_path=True)
        with open(file_path, "w", encoding="utf8") as file:
            json.dump(data, file, indent=4)
        logger.info("json file saved at: %s", file_path)
    except IOError as ex:
        logger.exception("Error loading object from: %s", file_path)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def load_json(file_path: Path) -> ConfigBox:
    """Method to load data from a json file"""
    try:
        with open(file_path, encoding="utf8") as file:
            content = json.load(file)
        logger.info("json file loaded succesfully from: %s", file_path)
        return ConfigBox(content)
    except IOError as ex:
        logger.exception("Error loading json from: %s", file_path)
        raise ex
    except Exception as ex:
        raise ex


@staticmethod
def get_file_paths_in_folder(folder_path: Path) -> list:
    """Method to get all file paths in a folder"""
    try:
        file_paths = [os.path.join(folder_path,f) for f in os.listdir(folder_path)]
        return file_paths
    except IOError as ex:
        logger.exception("Error getting file names from: %s", folder_path)
        raise ex
    except Exception as ex:
        raise ex
