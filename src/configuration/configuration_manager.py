import os

from src.utils.common import read_yaml
from src.configuration import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.entities.config_entity import (DataConfig)


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        
    def get_data_config(self)-> DataConfig:
        config=self.config.data
        data_config=DataConfig(data_original_path=config.data_original_path,
                               data_train_path=config.data_train_path,
                               data_test_path=config.data_test_path,
                               data_target_column=config.data_target_column,
                               data_transformer_path=config.data_transformer_path,
                               data_transformed_train_array_path=config.data_transformed_train_array_path,
                               data_transformed_test_array_path=config.data_transformed_test_array_path,)
        return data_config
