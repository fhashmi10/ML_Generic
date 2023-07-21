from src import logger
from src.components.model.model_builder import ModelBuilder
from src.configuration.configuration_manager import ConfigurationManager


class ModelTrainerPipeline():
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_builder_trainer=ModelBuilder(data_config=config.get_data_config(), model_config=config.get_model_config())
        model_builder_trainer.build_models()
        model_builder_trainer.train_models()


if __name__ == '__main__':
    STAGE_NAME = "Model Training stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e