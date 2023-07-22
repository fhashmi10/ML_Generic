"""Module to create pipeline to train models"""
from src import logger
from src.components.model.model_builder import ModelBuilder
from src.configuration.configuration_manager import ConfigurationManager


class ModelTrainerPipeline():
    """Class to create pipeline to train models"""

    def __init__(self):
        pass

    def train(self):
        """Method to invoke model training"""
        try:
            config = ConfigurationManager()
            model_builder_trainer = ModelBuilder(
                data_config=config.get_data_config(), model_config=config.get_model_config())
            model_builder_trainer.train_models()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    try:
        STAGE_NAME = "Model Training stage"
        logger.info("%s started", STAGE_NAME)
        model_trainer_pipe = ModelTrainerPipeline()
        model_trainer_pipe.train()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as e:
        logger.exception(e)
