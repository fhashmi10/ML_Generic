"""Module to define data preprocessing steps"""
import pandas as pd
from src import logger

@staticmethod
def preprocess_data(data_frame) -> pd.DataFrame:
    """Method to perform data preprocessing"""
    try:
        # Perform required data cleanup here
        return data_frame
    except Exception as ex:
        logger.exception("Exception occured while pre-processing data %s", ex)
        raise ex
