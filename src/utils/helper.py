"""Module to define frequently used functions that are not too generic to fall under common.py"""
from pathlib import Path
import pandas as pd
from src import logger
from src.utils.common import load_object

@staticmethod
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


@staticmethod
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
