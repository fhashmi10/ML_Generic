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
            config = ConfigurationManager()
            schema_config = config.get_schema_config()
            data_config = config.get_data_config()
            data_transformer = DataTransformer(schema_config=schema_config,
                                               data_config=data_config)
            data_transformer.build_data_transformer()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    try:
        STAGE_NAME = "Data Transformation stage"
        logger.info("%s started <<<<<<", STAGE_NAME)
        data_tranformer_pipe = DataTransformerPipeline()
        data_tranformer_pipe.transform()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
