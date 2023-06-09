from src import logger
from src.components.data_ingestion import DataIngestion
from src.config.configuration_manager import ConfigurationManager


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion=DataIngestion(config=config.get_data_config())
        data_ingestion.ingest_data()


if __name__ == '__main__':
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e