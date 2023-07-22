"""
Module to read configuration from yaml files
"""
from src.utils.common import read_yaml_configbox
from src.configuration import CONFIG_FILE_PATH
from src.entities.config_entity import (DataConfig, ModelConfig)
from .. import logger


class ConfigurationManager:
    """Configuration manager class to read configuration files"""

    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config = read_yaml_configbox(config_file_path)

    def get_data_config(self) -> DataConfig:
        """Method to map data configurations"""
        try:
            config = self.config.data
            data_config = DataConfig(data_original_path=config.data_original_path,
                                     data_train_path=config.data_train_path,
                                     data_test_path=config.data_test_path,
                                     data_target_column=config.data_target_column,
                                     data_transformer_path=config.data_transformer_path,
                                     data_transformed_X_train_array_path=config.data_transformed_X_train_array_path,
                                     data_transformed_X_test_array_path=config.data_transformed_X_test_array_path,
                                     data_transformed_y_train_array_path=config.data_transformed_y_train_array_path,
                                     data_transformed_y_test_array_path=config.data_transformed_y_test_array_path)
            return data_config
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    def get_model_config(self) -> ModelConfig:
        """Method to map model configurations"""
        try:
            config = self.config.model
            model_config = ModelConfig(
                model_trained_path=config.model_trained_path)
            return model_config
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
        except Exception as ex:
            raise ex
