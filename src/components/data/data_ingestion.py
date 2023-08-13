"""Module to ingest data"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split

from src import logger
from src.entities.config_entity import DataConfig
from src.components.data.data_preprocessor import preprocess_data
from src.utils.common import create_directories, remove_directories


class DataIngestion():
    """Class to ingest data"""

    def __init__(self, data_config: DataConfig):
        self.data_config = data_config
        self.data_frame = pd.DataFrame()

    @staticmethod
    def skip_processing(train_path: str, test_path: str, skip_existing: bool) -> bool:
        """Method to return True if ingestion needs to be skipped"""
        try:
            skip_process: bool = False
            if os.path.exists(train_path) and os.path.exists(test_path):
                if skip_existing:
                    logger.info("Data already exists. Skipping ingestion.")
                    skip_process = True
                else:
                    logger.info("Data already exists. Deleting existing data.")
                    remove_directories(
                        [train_path, test_path])
            elif os.path.exists(train_path) or os.path.exists(test_path):
                logger.info("Partial data exists. Deleting existing data.")
                remove_directories(
                    [train_path, test_path])
            return skip_process
        except OSError as ex:
            logger.exception("Error in checking data file on disk.")
            raise ex
        except Exception as ex:
            raise ex

    def load_input_data(self):
        """Method to load the input data"""
        try:
            # Read data from csv
            self.data_frame = pd.read_csv(self.data_config.input_path)
            logger.info("Input data file loaded.")
        except OSError as ex:
            logger.exception("Error reading data file.")
            raise ex
        except Exception as ex:
            raise ex

    def train_test_split(self, train_path, test_path):
        """Method to split data into train and test"""
        try:
            create_directories([train_path, test_path], is_file_path=True)
            train_set, test_set = train_test_split(
                self.data_frame, test_size=0.2, random_state=42)
            train_set.to_csv(train_path, index=False, header=True)
            test_set.to_csv(test_path, index=False, header=True)
            logger.info("Train and test data saved to csv files on disk.")
        except OSError as ex:
            logger.exception("Error saving train test data files.")
            raise ex
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def ingest_data(self, skip_existing=False):
        """Method to invoke data ingestion"""
        try:
            train_path = self.data_config.train_split_path
            test_path = self.data_config.test_split_path
            skip_processing = self.skip_processing(train_path=train_path,
                                                   test_path=test_path,
                                                   skip_existing=skip_existing)
            if not skip_processing:
                # Load data
                self.load_input_data()
                # Preprocess data
                self.data_frame = preprocess_data(self.data_frame)
                # Train test split
                self.train_test_split(
                    train_path=train_path, test_path=test_path)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
