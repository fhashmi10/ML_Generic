"""Module to train models"""
import numpy as np
from sklearn.model_selection import GridSearchCV
from src.utils.common import save_object
from src.entities.config_entity import DataTransformationConfig, ModelConfig
from src import logger


class ModelTrainer:
    """Class to train models"""

    def __init__(self, models: list, data_config=DataTransformationConfig, model_config=ModelConfig):
        self.models = models
        self.data_config = data_config
        self.model_config = model_config

    def load_train_data(self):
        """Method to load test data"""
        try:
            x_train = np.load(
                self.data_config.data_transformed_x_train_array_path)
            y_train = np.load(
                self.data_config.data_transformed_y_train_array_path)
            return x_train, y_train
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex
        
    def perform_grid_search(self, model, param, x_train, y_train) -> any:
        """Method to perform grid search cv"""
        try:
            logger.info(
                "Training GSV to find best parameters for %s", type(model).__name__)
            gsv = GridSearchCV(
                model, param, cv=self.model_config.model_params['CrossValidation']['cv'])
            gsv.fit(x_train, y_train)
            return gsv.best_params_
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def train_models(self):
        """Method to train the models one by one"""
        try:
            # Load training data
            x_train, y_train = self.load_train_data()

            # Train the models
            for model in self.models:
                try:
                    model_name = type(model).__name__
                    param = self.model_config.model_params[model_name]
                except KeyError:
                    # When there are no model parameters
                    param = {}

                # Get best params using grid search
                best_params = self.perform_grid_search(
                    model=model, param=param, x_train=x_train, y_train=y_train)

                # Use gsv best params to train model
                model.set_params(**best_params)
                logger.info("Training started for %s", model_name)
                model.fit(x_train, y_train)
                logger.info("Training completed for %s", model_name)

                # Save the model
                model_save_path=self.model_config.model_trained_path+"/"+model_name+".pkl"
                save_object(file_path=model_save_path, obj=model)
                logger.info("%s  model saved to disk", model_name)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
