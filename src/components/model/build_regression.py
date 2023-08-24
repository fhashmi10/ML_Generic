
"""
Module to build models
This class can be extended to add more models or make changes to models
You can also choose to save the built base models and separate out training
"""
from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor,
                              RandomForestRegressor)
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src import logger

def build_regression_models(selected_model: str) -> list:
    """Method to build regression models"""
    try:
        models = [LinearRegression(),
                  ElasticNet(),
                  DecisionTreeRegressor(),
                  RandomForestRegressor(),
                  AdaBoostRegressor(),
                  GradientBoostingRegressor(),
                  XGBRegressor(),
                  CatBoostRegressor(verbose=False)]
        if selected_model is not None:
            if selected_model.strip()!="":
                models = [model for model in models if selected_model in type(model).__name__]
        return models
    except Exception as ex:
        logger.exception("Exception occured: %s", ex)
        raise ex
