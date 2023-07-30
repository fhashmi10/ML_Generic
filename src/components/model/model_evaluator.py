"""Module to evaluate models"""
import numpy as np
from sklearn.metrics import r2_score
from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src.utils.common import get_file_paths_in_folder, \
    save_object, load_object, save_json
from src import logger


class ModelEvaluator:
    """Class to evaluate models"""

    def __init__(self, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.data_config = data_config
        self.model_config = model_config

    def evaluate_metric(self, eval_metric: str, actual, predicted):
        """Method to invoke model evaluation"""
        try:
            return getattr(self, eval_metric)(actual, predicted)
        except AttributeError as ex:
            logger.exception("Error getting metric function: %s", ex)
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
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def evaluate_models(self, file_paths: list, x_test, y_test):
        """Method to evaluate models"""
        try:
            trained_models = {}
            result = {}

            for file_path in file_paths:
                model = load_object(file_path=file_path)
                model_name = type(model).__name__
                logger.info("loaded %s successfully.", model_name)
                y_test_pred = model.predict(x_test)
                test_model_score = self.evaluate_metric(
                    eval_metric=self.model_config.evaluation_metric,
                    actual=y_test, predicted=y_test_pred)
                logger.info("Evaluated %s with %s: %s", model_name,
                            self.model_config.evaluation_metric, test_model_score)
                trained_models[model_name] = model
                result[model_name] = test_model_score
            return trained_models, result
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def save_best_model(self, trained_models, result):
        """Method to save best model and result"""
        try:
            logger.info("Saving Results to json file")
            save_json(
                file_path=self.model_config.evaluation_score_json_path, data=result)
            best_model_score = max(sorted(result.values()))
            best_model_name = list(result.keys())[list(
                result.values()).index(best_model_score)]
            best_model = trained_models[best_model_name]
            save_object(
                file_path=self.model_config.final_model_path, obj=best_model)
            logger.info("%s is the best model with %s as %s",
                        best_model_name, self.model_config.evaluation_metric, best_model_score)
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def evaluate(self):
        """Method to evaluate models"""
        try:
            # Load test data
            x_test, y_test = self.load_test_data()
            # Evaluate models
            file_paths = get_file_paths_in_folder(
                self.model_config.model_trained_path)
            trained_models, result = self.evaluate_models(file_paths=file_paths,
                                                          x_test=x_test, y_test=y_test)
            # Save the best model
            self.save_best_model(trained_models=trained_models, result=result)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
