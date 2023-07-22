"""
main module
"""
from src import logger
from src.pipeline.training_pipeline.s1_data_ingestion_pipeline import \
    DataIngestionPipeline
from src.pipeline.training_pipeline.s2_data_transformer_pipeline import \
    DataTransformerPipeline
from src.pipeline.training_pipeline.s3_model_trainer_pipeline import \
    ModelTrainerPipeline


try:
    STAGE_NAME = "Data Ingestion stage"
    logger.info("%s started", STAGE_NAME)
    data_ingestion_pipe = DataIngestionPipeline()
    data_ingestion_pipe.main()
    logger.info("%s completed\nx==========x", STAGE_NAME)

    STAGE_NAME = "Data Transformation stage"
    logger.info("%s started <<<<<<", STAGE_NAME)
    data_tranformer_pipe = DataTransformerPipeline()
    data_tranformer_pipe.main()
    logger.info("%s completed\nx==========x", STAGE_NAME)

    STAGE_NAME = "Model Training stage"
    logger.info("%s started", STAGE_NAME)
    model_trainer_pipe = ModelTrainerPipeline()
    model_trainer_pipe.main()
    logger.info("%s completed\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
