"""Module to create prediction pipeline"""
from src.configuration.configuration_manager import ConfigurationManager
from src.components.model.model_predictor import ModelPredictor
from src import logger


class ModelPredictionPipeline:
    """Class to create prediction pipeline"""

    def __init__(self):
        pass

    def predict(self, features_dict: dict) -> int:
        """Method to predict"""
        try:
            config = ConfigurationManager()
            data_config = config.get_data_transformation_config()
            model_config = config.get_model_config()
            model_predictor = ModelPredictor(data_config=data_config, model_config=model_config)
            prediction = model_predictor.predict(features_dict=features_dict)
            return prediction
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
