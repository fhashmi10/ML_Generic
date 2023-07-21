from src import logger
from src.components.data.data_transformer import DataTransformer
from src.configuration.configuration_manager import ConfigurationManager


class DataTransformerPipeline():
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_transformer=DataTransformer(config=config.get_data_config())
        data_transformer.transform_data()


if __name__ == '__main__':
    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataTransformerPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e