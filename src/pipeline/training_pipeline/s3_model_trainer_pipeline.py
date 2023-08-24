"""Module to create pipeline to train models"""
from src import logger
from src.components.model.model_builder import build_models_list
from src.components.model.model_trainer import ModelTrainer
from src.configuration.configuration_manager import ConfigurationManager


class ModelTrainerPipeline():
    """Class to create pipeline to train models"""

    def __init__(self):
        pass

    def train(self):
        """Method to invoke model training"""
        try:
            config = ConfigurationManager()
            data_config = config.get_data_config()
            model_config = config.get_model_config()

            # Get list of models to train
            models = build_models_list(
                model_task=model_config.model_task,
                selected_model=model_config.selected_model)

            # Train models
            model_trainer = ModelTrainer(models=models,
                                         data_config=data_config,
                                         model_config=model_config)
            model_trainer.train()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    try:
        STAGE_NAME = "Model Training stage"
        logger.info("%s started", STAGE_NAME)
        model_trainer_pipe = ModelTrainerPipeline()
        model_trainer_pipe.train()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
