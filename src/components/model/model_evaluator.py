"""Module to evaluate models"""
from urllib.parse import urlparse
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import mlflow
from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src.utils.common import get_file_paths_in_folder, \
    save_object, load_object, save_json
from src import logger


class ModelEvaluator:
    """Class to evaluate models"""

    def __init__(self, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.data_config = data_config
        self.model_config = model_config

    @staticmethod
    def r2_score(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = r2_score(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def mean_squared_error(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = np.sqrt(mean_squared_error(actual, predicted))
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def mean_absolute_error(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = mean_absolute_error(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    def evaluate_metric(self, eval_metric: str, actual, predicted):
        """Method to invoke model evaluation"""
        try:
            return getattr(self, eval_metric)(actual, predicted)
        except AttributeError as ex:
            logger.exception("Error getting metric function: %s", ex)
            raise ex
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
                # Predict
                model = load_object(file_path=file_path)
                model_name = type(model).__name__
                logger.info("loaded %s successfully.", model_name)
                y_test_pred = model.predict(x_test)

                # Evaluate
                eval_metrics: list = self.model_config.evaluation_metric.split(
                    ',')
                test_model_scores = {}
                for metric in eval_metrics:
                    metric = metric.strip()
                    test_model_score = self.evaluate_metric(
                        eval_metric=metric,
                        actual=y_test, predicted=y_test_pred)
                    test_model_scores[metric] = test_model_score
                    logger.info("Evaluated %s with %s: %s", model_name,
                                metric, test_model_score)

                # Prepare return values
                trained_models[model_name] = model
                result[model_name] = test_model_scores
            return trained_models, result
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def log_mlflow(self, model, model_score: dict):
        """Method to log to MLflow"""
        try:
            mlflow.set_registry_uri(self.model_config.mlflow_uri)
            tracking_url_type_store = urlparse(
                mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metric("r2_score", model_score["r2_score"])
                mlflow.log_metric("mean_squared_error",
                                  model_score["mean_squared_error"])
                mlflow.log_metric("mean_absolute_error",
                                  model_score["mean_absolute_error"])

                # Model registry does not work with file store
                if tracking_url_type_store != "file":
                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(
                        model, "model", registered_model_name=type(model).__name__)
                else:
                    mlflow.sklearn.log_model(model, "model")
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def save_best_model(self, trained_models, result):
        """Method to save best model and result"""
        try:
            # Save all results to json
            logger.info("Saving Results to json file")
            save_json(
                file_path=self.model_config.evaluation_score_json_path, data=result)

            # Build a new dictionary with only desired metric to get best model
            result_dict = {}
            for key, value in result.items():
                for key_2, value_2 in value.items():
                    if key_2 == self.model_config.evaluation_metric_best_model:
                        result_dict[key] = value_2

            # Save best model
            best_model_score = max(sorted(result_dict.values()))
            best_model_name = list(result_dict.keys())[list(
                result_dict.values()).index(best_model_score)]
            best_model = trained_models[best_model_name]
            save_object(
                file_path=self.model_config.final_model_path, obj=best_model)
            logger.info("%s is the best model with %s as %s",
                        best_model_name,
                        self.model_config.evaluation_metric_best_model,
                        best_model_score)

            # Log ml flow
            self.log_mlflow(best_model, result[best_model_name])
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
