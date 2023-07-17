import os, sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor 
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

from src.components.model_evaluation import Model_Evaluation
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object



class ModelBuilder:
    def __init__(self) -> None: 
        pass

    def build_model(self, X_train_arr, y_train_arr, X_test_arr, y_test_arr):
        models={
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest": RandomForestRegressor(),
            "AdaBoost Regressor": AdaBoostRegressor(),
            "Gradient Boosting": GradientBoostingRegressor(),
            "XGBRegressor": XGBRegressor(),
            "CatBoosting Regressor": CatBoostRegressor(verbose=False),
        }
        params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
            }
        model_evaluation=Model_Evaluation()
        best_model_name, best_model_score=model_evaluation.evaluate_models(X_train_arr, y_train_arr, X_test_arr, y_test_arr, models, params)
        print(best_model_name, best_model_score)

