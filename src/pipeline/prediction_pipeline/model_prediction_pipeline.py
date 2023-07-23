"""Module to create prediction pipeline"""
import os
import pandas as pd
from src.utils.common import load_object
from src.configuration.configuration_manager import ConfigurationManager
from src import logger


class ModelPredictionPipeline:
    """Class to create prediction pipeline"""

    def __init__(self):
        pass

    def predict(self, features_dict: dict):
        """Method to predict"""
        try:
            config = ConfigurationManager()
            data_config=config.get_data_transformation_config() 
            model_config=config.get_model_config()
            
            preprocessor = load_object(file_path=data_config.data_transformer_path)
            logger.info("loaded data transformer successfully.")
            features_df=pd.DataFrame(features_dict, index=[0])
            tranformed_data = preprocessor.transform(features_df)

            model = load_object(file_path=model_config.final_model_path)
            logger.info("loaded model successfully.")
            prediction = round(model.predict(tranformed_data)[0],0)
            logger.info("Predicted %s", prediction)

            return prediction
        except Exception as ex:
            raise ex
