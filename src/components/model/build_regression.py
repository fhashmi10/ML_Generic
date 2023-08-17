
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

def build_regression_models() -> list:
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
        return models
    except Exception as ex:
        logger.exception("Exception occured: %s", ex)
        raise ex
