
from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor,
                              RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.components.model.model_trainer import ModelTrainer
from src.entities.config_entity import DataConfig, ModelConfig
from src.configuration.parameters_manager import ParametersManager


class ModelBuilder:
    def __init__(self, data_config=DataConfig, model_config=ModelConfig):
        self.data_config=data_config
        self.model_config=model_config
        params_manager = ParametersManager()
        self.params=params_manager.get_params()


    def build_models(self):
        self.models={
            "LinearRegression": LinearRegression(),
            "DecisionTreeRegressor": DecisionTreeRegressor(),
            "RandomForestRegressor": RandomForestRegressor(),
            "AdaBoostRegressor": AdaBoostRegressor(),
            "GradientBoostRegressor": GradientBoostingRegressor(),
            "XGBRegressor": XGBRegressor(),
            "CatBoostRegressor": CatBoostRegressor(verbose=False),
        }
    
    
    def train_models(self):
        model_trainer=ModelTrainer(models=self.models, params=self.params, data_config=self.data_config, model_config=self.model_config)
        model_trainer.train_models()

