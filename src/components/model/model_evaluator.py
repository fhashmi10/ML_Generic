"""Module to evaluate models"""
import numpy as np
from pathlib import Path
from sklearn.metrics import r2_score
from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src.utils.common import get_file_paths_in_folder, save_object, load_object, save_json
from src import logger


class ModelEvaluator:
    """Class to evaluate models"""

    def __init__(self, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.data_config = data_config
        self.model_config = model_config

    def evaluate(self, eval_metric: str, actual, predicted):
        """Method to invoke model evaluation"""
        try:
            return getattr(self, eval_metric)(actual, predicted)
        except AttributeError as ex:
            logger.error("Error getting metric function: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    @staticmethod
    def r2_score(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = r2_score(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    def load_test_data(self):
        """Method to load test data"""
        try:
            x_test = np.load(
                self.data_config.data_transformed_x_test_array_path)
            y_test = np.load(
                self.data_config.data_transformed_y_test_array_path)
            return x_test, y_test
        except Exception as ex:
            raise ex

    def evaluate_model(self):
        """Method to evaluate models"""
        try:
            trained_models = {}
            result = {}
            # load test data
            x_test, y_test = self.load_test_data()
            file_paths = get_file_paths_in_folder(
                self.model_config.model_trained_path)

            for i, file_path in enumerate(file_paths):
                model = load_object(file_path=file_path)
                model_name = type(model).__name__
                logger.info("loaded %s successfully.", model_name)
                y_test_pred = model.predict(x_test)
                test_model_score = self.evaluate(
                    eval_metric=self.model_config.evaluation_metric, actual=y_test, predicted=y_test_pred)
                logger.info("Evaluated %s with %s: %s", model_name,
                            self.model_config.evaluation_metric, test_model_score)
                trained_models[model_name] = model
                result[model_name] = test_model_score

            logger.info("Saving Results to json file")
            # todo: scores json path in config file
            save_json(file_path=Path("scores.json"), data=result)
            best_model_score = max(sorted(result.values()))
            best_model_name = list(result.keys())[list(
                result.values()).index(best_model_score)]
            best_model = trained_models[best_model_name]
            save_object(
                file_path=self.model_config.final_model_path, obj=best_model)
            logger.info("%s is the best model with %s as %s",
                        best_model_name, self.model_config.evaluation_metric, best_model_score)
        except Exception as ex:
            raise ex
