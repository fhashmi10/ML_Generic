"""Module to ingest data"""
import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src import logger
from src.utils.common import create_directories, remove_directories
from src.entities.config_entity import DataIngestionConfig


class DataIngestion():
    """Class to ingest data"""

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    @staticmethod
    def skip_processing(train_path: str, test_path: str, skip_existing: bool) -> bool:
        """Method to return True if ingestion needs to be skipped"""
        try:
            skip_process: bool = False
            if os.path.exists(train_path) and os.path.exists(test_path):
                if skip_existing:
                    logger.info('Data already exists. Skipping ingestion.')
                    skip_process = True
                else:
                    logger.info('Data already exists. Deleting existing data.')
                    remove_directories(
                        [train_path, test_path])
            elif os.path.exists(train_path) or os.path.exists(test_path):
                logger.info('Partial data exists. Deleting existing data.')
                remove_directories(
                    [train_path, test_path])
            return skip_process
        except IOError as ex:
            logger.exception("Error in checking data file on disk.")
            raise ex
        except Exception as ex:
            raise ex

    def train_test_split(self):
        """Method to split data into train and test"""
        try:
            data_frame = pd.read_csv(self.config.data_original_path)
            logger.info('Input data file loaded.')

            train_set, test_set = train_test_split(
                data_frame, test_size=0.2, random_state=42)
            create_directories([os.path.dirname(self.config.data_train_path),
                                os.path.dirname(self.config.data_test_path)])
            train_set.to_csv(self.config.data_train_path,
                             index=False, header=True)
            test_set.to_csv(self.config.data_test_path,
                            index=False, header=True)
            logger.info('Train and test data saved to csv files on disk.')
        except IOError as ex:
            logger.exception("Error saving train test data files.")
            raise ex
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def ingest_data(self, skip_existing=False):
        """Method to be invoked to ingest data"""
        try:
            skip_processing = self.skip_processing(
                train_path=self.config.data_train_path, test_path=self.config.data_test_path, skip_existing=skip_existing)
            if not skip_processing:
                self.train_test_split()
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
