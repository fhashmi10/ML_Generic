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

    def main(self):
        """Main method to read configuration and ingest data"""
        try:
            config = ConfigurationManager()
            data_ingestion = DataIngestion(config=config.get_data_config())
            data_ingestion.ingest_data()
        except Exception as ex:
            raise ex


if __name__ == '__main__':
    try:
        STAGE_NAME = "Data Ingestion stage"
        logger.info("%s started", STAGE_NAME)
        data_ingestion_pipe = DataIngestionPipeline()
        data_ingestion_pipe.main()
        logger.info("%s completed\nx==========x", STAGE_NAME)
    except Exception as e:
        logger.exception(e)
        raise e
