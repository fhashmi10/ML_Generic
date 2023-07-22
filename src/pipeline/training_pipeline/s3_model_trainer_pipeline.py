from src import logger
from src.components.model.model_builder import ModelBuilder
from src.configuration.configuration_manager import ConfigurationManager


class ModelTrainerPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_builder_trainer = ModelBuilder(
            data_config=config.get_data_config(), model_config=config.get_model_config())
        model_builder_trainer.build_models()
        #model_builder_trainer.train_models()


if __name__ == '__main__':
    try:
        STAGE_NAME = "Model Training stage"
        logger.info("%s started", STAGE_NAME)
        model_trainer_pipe = ModelTrainerPipeline()
        # temp-model_trainer_pipe.main()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as e:
        logger.exception(e)
        raise e
