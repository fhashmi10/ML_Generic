"""Module to hold all common util methods"""
import os
import pickle
import shutil
from pathlib import Path
import json
import yaml
from box import ConfigBox, exceptions
from ensure import ensure_annotations

from src import logger


@ensure_annotations
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
        logger.exception(ex)
        raise ex
    except IOError as ex:
        logger.exception("yaml file is empty: %s", path_to_yaml)
        raise ex
    except Exception as ex:
        raise ex


@ensure_annotations
def read_yaml_configbox(path_to_yaml: Path) -> ConfigBox:
    """Method to read yaml and return a ConfigBox instance
    A configbox helps in accessing yaml contents with . syntax"""
    try:
        with open(path_to_yaml, encoding='utf8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file loaded successfully: %s", path_to_yaml)
            return ConfigBox(content)
    except exceptions.BoxValueError as ex:
        logger.exception("yaml file is empty: %s", path_to_yaml)
        raise ex
    except Exception as ex:
        raise ex


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Method to create directories"""
    try:
        for path in path_to_directories:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
                if verbose:
                    logger.info("created directory at %s:", path)
    except IOError as ex:
        logger.exception("Error creating directories: %s", path_to_directories)
        raise ex
    except Exception as ex:
        raise ex


@ensure_annotations
def remove_directories(path_to_directories: list, verbose=True):
    """Method to remove directories"""
    try:
        for path in path_to_directories:
            if os.path.exists(path):
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    if verbose:
                        logger.info("removed directory at %s:", path)
                elif os.path.isfile(path):
                    os.remove(path)
                    if verbose:
                        logger.info("removed file at %s:", path)
    except IOError as ex:
        logger.exception("Error removing directories: %s", path_to_directories)
        raise ex
    except Exception as ex:
        raise ex


def save_object(obj, file_path):
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


def load_object(file_path):
    """Method to load an object from a file"""
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except IOError as ex:
        logger.exception("Error loading object from: %s", file_path)
        raise ex
    except Exception as ex:
        raise ex


@ensure_annotations
def save_json(file_path: Path, data: dict):
    """Method to dump data to a json file"""
    try:
        with open(file_path, "w", encoding="utf8") as file:
            json.dump(data, file, indent=4)
        logger.info("json file saved at: %s", file_path)
    except IOError as ex:
        logger.exception("Error loading object from: %s", file_path)
        raise ex
    except Exception as ex:
        raise ex
    