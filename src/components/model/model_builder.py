
"""Module to build models"""
from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor,
                              RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.components.model.model_trainer import ModelTrainer
from src.entities.config_entity import DataTransformationConfig, ModelConfig


class ModelBuilder:
    """Class to build models"""

    def __init__(self, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.data_config = data_config
        self.model_config = model_config

    def train_models(self):
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
            model_trainer = ModelTrainer(models=models,
                                         data_config=self.data_config, model_config=self.model_config)
            model_trainer.train_models()
        except Exception as ex:
            raise ex
