
"""
Module to build models
This class can be extended to add more models or make changes to models
You can also choose to save the built base models and separate out training
"""
from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor,
                              RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.components.model.model_trainer import ModelTrainer
from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src import logger


class ModelBuilder:
    """Class to build models"""

    def __init__(self, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.data_config = data_config
        self.model_config = model_config

    def build_models(self):
        """Method to invoke model training"""
        try:
            models = [
                      LinearRegression(),
                      DecisionTreeRegressor(),
                      RandomForestRegressor(),
                      AdaBoostRegressor(),
                      GradientBoostingRegressor(),
                      XGBRegressor(),
                      CatBoostRegressor(verbose=False),
                      ]
            # todo: only define models here and separate out trainer
            model_trainer = ModelTrainer(models=models,
                                         data_config=self.data_config, model_config=self.model_config)
            model_trainer.train_models()
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
