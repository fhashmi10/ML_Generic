"""Module to train models"""
from pathlib import Path
import numpy as np
from sklearn.model_selection import GridSearchCV
from src.utils.common import save_object, save_json
from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src.components.model.model_evaluator import ModelEvaluator
from src import logger


class ModelTrainer:
    """Class to train models"""

    def __init__(self, models: list, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.models = models
        self.data_config = data_config
        self.model_config = model_config
        # todo: load separately
        self.x_train = np.load(
            self.data_config.data_transformed_x_train_array_path)
        #self.x_test = np.load(
        #    self.data_config.data_transformed_x_test_array_path)
        self.y_train = np.load(
            self.data_config.data_transformed_y_train_array_path)
        #self.y_test = np.load(
        #    self.data_config.data_transformed_y_test_array_path)

    def perform_grid_search(self, model, param) -> any:
        """Method to perform grid search cv"""
        try:
            logger.info(
                "Training GSV to find best parameters for %s", type(model).__name__)
            gsv = GridSearchCV(
                model, param, cv=self.model_config.model_params['CrossValidation']['cv'])
            gsv.fit(self.x_train, self.y_train)
            return gsv.best_params_
        except Exception as ex:
            raise ex

    def train_models(self):
        """Method to train the models one by one"""
        try:
            # trained_models = {}
            # result = {}

            for i, model in enumerate(self.models):
                try:
                    model_name = type(model).__name__
                    param = self.model_config.model_params[model_name]
                except KeyError:
                    # to handle when there are no model parameters
                    param = {}

                best_params = self.perform_grid_search(
                    model=model, param=param)

                # use gsv best params to train model
                model.set_params(**best_params)
                logger.info("Training started for %s", model_name)
                model.fit(self.x_train, self.y_train)
                logger.info("Training completed for %s", model_name)
                # todo: save models and only do training here - move evaluation
                model_save_path=self.model_config.model_trained_path+"/"+model_name+".h5"
                save_object(file_path=model_save_path, obj=model)
                logger.info("%s  model saved to disk", model_name)
                # model prediction
            #     y_test_pred = model.predict(self.x_test)
            #     eval_metric = 'r2_score'
            #     model_evaluator = ModelEvaluator(
            #         eval_metric, self.y_test, y_test_pred)
            #     test_model_score = model_evaluator.evaluate()
            #     logger.info("Evaluated %s with %s: %s", model_name,
            #                 eval_metric, test_model_score)

            #     trained_models[self.models[i]] = model
            #     result[self.models[i]] = test_model_score

            # logger.info("Saving Results to json file")
            # # todo: scores json path in config file
            # save_json(file_path=Path("scores.json"), data=result)

            # best_model_score = max(sorted(result.values()))
            # best_model_name = list(result.keys())[list(
            #     result.values()).index(best_model_score)]
            # best_model = trained_models[best_model_name]

            # save_object(
            #     file_path=self.model_config.model_trained_path, obj=best_model)

            # logger.info("%s is the best model with %s as %s",
            #             best_model_name, eval_metric, best_model_score)

        except Exception as ex:
            logger.exception(ex)
            raise ex
