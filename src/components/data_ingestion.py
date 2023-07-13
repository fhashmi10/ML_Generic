import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src import logger
from src.common.utils import create_directories, remove_directories
from src.entities.config_entity import DataConfig


class DataIngestion():
    def __init__(self, config: DataConfig):
        self.config = config


    def train_test_split(self):
        try:
            data_frame=pd.read_csv(self.config.data_original_path)
            logger.info('Input data file loaded.')

            train_set, test_set=train_test_split(data_frame, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.config.data_train_path, index=False, header=True)
            test_set.to_csv(self.config.data_test_path, index=False, header=True)
            logger.info('Train and test data created.')

        except Exception as e:
            logger.exception(e)
            raise e

    def ingest_data(self, skip_existing=True):
        try:
            if os.path.exists(self.config.data_train_path) and os.path.exists(self.config.data_test_path):
                if skip_existing:
                    logger.info('Data already exists. Skipping ingestion.')
                    return
                else:
                    logger.info('Data already exists. Deleting existing data.')
                    remove_directories([self.config.data_train_path, self.config.data_test_path])
                    self.train_test_split()
            else:
                self.train_test_split()
                    
        except Exception as e:
            logger.exception(e)
            raise e