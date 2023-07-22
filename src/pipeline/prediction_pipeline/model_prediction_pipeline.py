"""Module to create prediction pipeline"""
import os
import pandas as pd
from src.utils.common import load_object
from src import logger


class ModelPredictionPipeline:
    """Class to create prediction pipeline"""

    def __init__(self):
        pass

    def predict(self, features_dict: dict):
        """Method to predict"""
        try:
            preprocessor_path = os.path.join(
                'artifacts', 'data/transformed_data/data_transformer.pkl')
            preprocessor = load_object(file_path=preprocessor_path)
            logger.info("loaded data transformer successfully.")
            features_df=pd.DataFrame(features_dict, index=[0])
            tranformed_data = preprocessor.transform(features_df)

            model_path = os.path.join("artifacts", "models/trained_model/model.h5")
            model = load_object(file_path=model_path)
            logger.info("loaded model successfully.")
            prediction = model.predict(tranformed_data)

            return prediction
        except Exception as ex:
            raise ex
