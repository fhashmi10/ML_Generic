"""Module to define frequently used functions that are not too generic to fall under common.py"""
from pathlib import Path
import pandas as pd
import numpy as np
from src import logger
from src.utils.common import load_object

def load_split_data(data_path: Path, target_column: str):
    """Method to load split data"""
    try:
        data_frame = pd.read_csv(data_path)
        x_data = data_frame.drop(columns=[target_column], axis=1)
        y_data = data_frame[target_column]
        return x_data, y_data
    except OSError as ex:
        logger.exception("Error reading data file.")
        raise ex
    except AttributeError as ex:
        raise ex
    except Exception as ex:
        raise ex


def perform_data_transformation(transformer_path: Path, input_data: pd.DataFrame):
    """Method to transform data using transformer"""
    try:
        preprocessor = load_object(file_path=transformer_path)
        logger.info("Loaded data transformer successfully.")
        transformed_data = preprocessor.transform(input_data)
        return transformed_data
    except OSError as ex:
        raise ex
    except AttributeError as ex:
        raise ex
    except Exception as ex:
        raise ex


def sample_data(x_train, y_train, sample_size: int):
    """Method to sample data"""
    try:
        data_array = np.concatenate((x_train, y_train.array.reshape(-1,1)), axis=1)
        data_frame = pd.DataFrame.from_records(data_array)
        data_frame = data_frame.sample(sample_size, random_state=42)
        x_data = data_frame.drop(columns=data_frame.columns[-1], axis=1)
        y_data = data_frame[data_frame.columns[-1]]
        return x_data, y_data
    except OSError as ex:
        logger.exception("Error reading data file.")
        raise ex
    except AttributeError as ex:
        raise ex
    except Exception as ex:
        raise ex
