import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ... import logger
from ...utils.common import remove_directories
from ...entities.config_entity import DataConfig


class DataIngestion():
    """Class to ingest data"""

    def __init__(self, config: DataConfig):
        self.config = config

    def train_test_split(self):
        """Method to split data into train and test"""
        try:
            data_frame = pd.read_csv(self.config.data_original_path)
            logger.info('Input data file loaded.')

            train_set, test_set = train_test_split(
                data_frame, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.data_train_path,
                             index=False, header=True)
            test_set.to_csv(self.config.data_test_path,
                            index=False, header=True)
            logger.info('Train and test data created.')
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
        except Exception as ex:
            raise ex

    def ingest_data(self, skip_existing=False):
        """Method to be invoked to ingest data"""
        try:
            if os.path.exists(self.config.data_train_path) and os.path.exists(self.config.data_test_path):
                if skip_existing:
                    logger.info('Data already exists. Skipping ingestion.')
                else:
                    logger.info('Data already exists. Deleting existing data.')
                    remove_directories(
                        [self.config.data_train_path, self.config.data_test_path])
                    self.train_test_split()
            else:
                self.train_test_split()
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
        except Exception as ex:
            raise ex
