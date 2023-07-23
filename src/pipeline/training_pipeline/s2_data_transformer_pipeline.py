"""
Module to create a pipeline to transform data
"""
from src import logger
from src.components.data.data_transformer import DataTransformer
from src.configuration.configuration_manager import ConfigurationManager


class DataTransformerPipeline():
    """Class to create a pipeline to transform data"""
    def __init__(self):
        pass

    def transform(self):
        """Method to read configuration and transform data"""
        try:
            config=ConfigurationManager()
            data_transformer=DataTransformer(data_ingestion_config=config.get_data_ingestion_config(),
                                             config=config.get_data_transformation_config())
            data_transformer.transform_data()
        except Exception as ex:
            logger.error("Error in data transformation: %s", ex)


if __name__ == '__main__':
    STAGE_NAME = "Data Transformation stage"
    logger.info("%s started <<<<<<", STAGE_NAME)
    data_tranformer_pipe = DataTransformerPipeline()
    data_tranformer_pipe.transform()
    logger.info("%s completed\nx==========x", STAGE_NAME)
    