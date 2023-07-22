"""
Module to read configuration from yaml files
"""
from src.utils.common import read_yaml_configbox, read_yaml_dict
from src.configuration import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.entities.config_entity import (DataConfig, ModelConfig)
from src import logger

from ensure import EnsureError


class ConfigurationManager:
    """Configuration manager class to read configuration files"""

    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):
        try:
            self.config = read_yaml_configbox(config_file_path)
            self.params_file_path = params_file_path
        except EnsureError as ex:
            logger.exception("Problem reading parameters yaml file: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    def get_data_config(self) -> DataConfig:
        """Method to map data configurations"""
        try:
            config = self.config.data
            data_config = DataConfig(data_original_path=config.data_original_path,
                                     data_train_path=config.data_train_path,
                                     data_test_path=config.data_test_path,
                                     data_target_column=config.data_target_column,
                                     data_transformer_path=config.data_transformer_path,
                                     data_transformed_x_train_array_path=config.data_transformed_x_train_array_path,
                                     data_transformed_x_test_array_path=config.data_transformed_x_test_array_path,
                                     data_transformed_y_train_array_path=config.data_transformed_y_train_array_path,
                                     data_transformed_y_test_array_path=config.data_transformed_y_test_array_path)
            return data_config
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    @staticmethod
    def get_model_params(params_file_path: str) -> dict:
        """Method to get model parameters"""
        try:
            params_dict = read_yaml_dict(params_file_path)
            return params_dict
        except EnsureError as ex:
            logger.exception("Problem reading parameters yaml file: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    def get_model_config(self) -> ModelConfig:
        """Method to map model configurations"""
        try:
            config = self.config.model
            params = self.get_model_params(self.params_file_path)
            model_config = ModelConfig(
                model_trained_path=config.model_trained_path,
                model_params=params)
            return model_config
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
        except Exception as ex:
            raise ex
