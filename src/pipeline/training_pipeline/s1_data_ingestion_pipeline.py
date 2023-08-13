"""
Module to create a pipeline to ingest data
"""
from src import logger
from src.components.data.data_ingestion import DataIngestion
from src.configuration.configuration_manager import ConfigurationManager


class DataIngestionPipeline:
    """Class to create a pipeline to ingest data"""

    def __init__(self):
        pass

    def ingest(self):
        """Method to read configuration and ingest data"""
        try:
            config = ConfigurationManager()
            data_config = config.get_data_config()
            data_ingestion = DataIngestion(data_config=data_config)
            data_ingestion.ingest_data()
        except Exception as ex:
            raise ex

if __name__ == '__main__':
    try:
        STAGE_NAME = "Data Ingestion stage"
        logger.info("%s started", STAGE_NAME)
        data_ingestion_pipe = DataIngestionPipeline()
        data_ingestion_pipe.ingest()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as exc:
        logger.exception("Exception occured: %s", exc)
