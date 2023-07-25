
"""Module to perform prediction"""
import pandas as pd

from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src.utils.common import load_object
from src import logger


class ModelPredictor:
    """Class to perform prediction"""

    def __init__(self, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.data_config = data_config
        self.model_config = model_config

    def transform_input_data(self, features_dict: dict):
        """Method to transform input data"""
        try:
            preprocessor = load_object(
                file_path=self.data_config.data_transformer_path)
            logger.info("loaded data transformer successfully.")
            features_df = pd.DataFrame(features_dict, index=[0])
            transformed_data = preprocessor.transform(features_df)
            return transformed_data
        except Exception as ex:
            raise ex
        
    def predict(self, features_dict: dict) -> int:
        """Method to invoke prediction"""
        try:
            # Transform input data
            transformed_data = self.transform_input_data(features_dict=features_dict)
            # Load the model
            model = load_object(file_path=self.model_config.final_model_path)
            logger.info("loaded model successfully.")
            # Predict
            prediction = int(round(model.predict(transformed_data)[0], 0))
            logger.info("Predicted %s", prediction)
            return prediction
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
