import os, sys
from dataclasses import dataclass
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from pathlib import Path
from src.utils.common import save_object, save_json
from src.entities.config_entity import DataConfig, ModelConfig

from src import logger

class ModelTrainer:
    def __init__(self, models: dict, params: dict, data_config=DataConfig, model_config=ModelConfig):
        self.models=models
        self.params=params
        self.data_config=data_config
        self.models_config=model_config

        self.X_train=np.load(self.data_config.data_transformed_X_train_array_path)
        self.X_test=np.load(self.data_config.data_transformed_X_test_array_path)
        self.y_train=np.load(self.data_config.data_transformed_y_train_array_path)
        self.y_test=np.load(self.data_config.data_transformed_y_test_array_path)


    def train_models(self):
        try:
            trained_models={}
            result={}

            for i in range(len(list(self.models))):
                model=list(self.models.values())[i]
                try:
                    model_name=list(self.models.keys())[i]
                    param=self.params[model_name]
                except KeyError:
                    param={}

                logger.info(f"Training GSV to find best parameters for {model_name}")
                gsv = GridSearchCV(model,param,cv=self.params['CrossValidation']['cv'])
                gsv.fit(self.X_train,self.y_train)

                #use gsv best params to train model
                logger.info(f"Training {model_name} on training data")
                model.set_params(**gsv.best_params_)
                model.fit(self.X_train,self.y_train)
                
                #y_train_pred = model.predict(self.X_train)
                #train_model_score = r2_score(self.y_train, y_train_pred)
                
                y_test_pred = model.predict(self.X_test)
                test_model_score = r2_score(self.y_test, y_test_pred)
                logger.info(f"Evaluating {model_name} with r2_score: {test_model_score}")

                trained_models[list(self.models.keys())[i]] = model
                result[list(self.models.keys())[i]] = test_model_score


            logger.info("Saving Results to json file")
            save_json(path=Path("scores.json"), data=result)
            
            best_model_score = max(sorted(result.values()))
            best_model_name = list(result.keys())[list(result.values()).index(best_model_score)]
            best_model = trained_models[best_model_name]

            if best_model_score<0.6:
                raise Exception("No models found with acceptable scores")
            
            save_object(file_path=self.models_config.model_trained_path, obj=best_model)

            logger.info(f"{best_model_name} is the best model with r2_score as {best_model_score}")

        except Exception as e:
            logger.exception(e)
            raise e
