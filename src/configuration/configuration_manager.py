"""
Module to read configuration from yaml files
"""
from src.utils.common import read_yaml_configbox, read_yaml_dict
from src.configuration import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.entities.config_entity import (
    DataIngestionConfig, DataTransformationConfig, ModelConfig)
from src import logger

class ConfigurationManager:
    """Configuration manager class to read configuration files"""

    def __init__(self):
        try:
            self.config = read_yaml_configbox(CONFIG_FILE_PATH)
            self.params_dict = read_yaml_dict(PARAMS_FILE_PATH)
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Method to map data configurations"""
        try:
            config = self.config.data_ingestion
            data_config = DataIngestionConfig(data_original_path=config.data_original_path,
                                              data_train_path=config.data_train_path,
                                              data_test_path=config.data_test_path)
            return data_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Method to map data configurations"""
        try:
            config = self.config.data_transformation
            data_config = DataTransformationConfig(
                data_target_column=config.data_target_column,
                data_transformer_path=config.data_transformer_path,
                data_transformed_x_train_array_path=config.data_transformed_x_train_array_path,
                data_transformed_x_test_array_path=config.data_transformed_x_test_array_path,
                data_transformed_y_train_array_path=config.data_transformed_y_train_array_path,
                data_transformed_y_test_array_path=config.data_transformed_y_test_array_path)
            return data_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_model_config(self) -> ModelConfig:
        """Method to map model configurations"""
        try:
            config = self.config.model
            params = self.params_dict
            model_config = ModelConfig(
                model_objective=config.model_objective,
                model_trained_path=config.model_trained_path,
                final_model_path=config.final_model_path,
                evaluation_metric=config.evaluation_metric,
                evaluation_score_json_path=config.evaluation_score_json_path,
                evaluation_metric_best_model=config.evaluation_metric_best_model,
                model_params=params,
                mlflow_uri=config.mlflow_uri)
            return model_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
