"""
Module to read configuration from yaml files
"""
from src import logger
from src.configuration import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.utils.common import read_yaml_configbox, read_yaml_dict
from src.entities.config_entity import DataConfig, ModelConfig, EvalConfig

class ConfigurationManager:
    """Configuration manager class to read configuration files"""

    def __init__(self):
        try:
            self.config = read_yaml_configbox(CONFIG_FILE_PATH)
            self.params_dict = read_yaml_dict(PARAMS_FILE_PATH)
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_data_config(self) -> DataConfig:
        """Method to map data configurations"""
        try:
            config = self.config.data
            data_config = DataConfig(input_path=config.input_path,
                                     train_split_path=config.train_split_path,
                                     test_split_path=config.test_split_path,
                                     target_column=config.target_column,
                                     transformer_path=config.transformer_path)
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
            model_config = ModelConfig(model_task=config.model_task,
                                       trained_models_path=config.trained_models_path,
                                       final_model_path=config.final_model_path,
                                       model_params=params)
            return model_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex

    def get_evaluation_config(self) -> EvalConfig:
        """Method to map evaluation configurations"""
        try:
            config = self.config.evaluation
            eval_config = EvalConfig(eval_metrics=config.eval_metrics,
                                     eval_metric_selection=config.eval_metric_selection,
                                     eval_scores_path=config.eval_scores_path,
                                     mlflow_uri=config.mlflow_uri)
            return eval_config
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
