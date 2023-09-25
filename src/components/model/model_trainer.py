"""Module to train models"""
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from imblearn import over_sampling, under_sampling, pipeline
from src.entities.config_entity import DataConfig, ModelConfig
from src.utils.common import save_object
from src.utils.helper import load_split_data, perform_data_transformation, sample_data
from src import logger


class ModelTrainer:
    """Class to train models"""

    def __init__(self, models: list,
                 data_config: DataConfig,
                 model_config: ModelConfig):
        self.models = models
        self.data_config = data_config
        self.model_config = model_config

    def perform_grid_search(self, model, param, x_train, y_train) -> any:
        """Method to perform grid search cv"""
        try:
            logger.info(
                "Training GSV to find best parameters for %s", type(model).__name__)
            if self.model_config.randomize_grid_search is True:
                gsv = RandomizedSearchCV(model, param, n_iter=10,
                    cv=self.model_config.model_params['CrossValidation']['cv'],
                    n_jobs=-2, verbose=2)
            else:
                gsv = GridSearchCV(model, param,
                    cv=self.model_config.model_params['CrossValidation']['cv'],
                    n_jobs=-2, verbose=2)

            if x_train.shape[0]<=self.model_config.gsv_max_data_size:
                gsv.fit(x_train, y_train)
            else:
                x_train_sample, y_train_sample = sample_data(
                    x_train=x_train,
                    y_train=y_train,
                    sample_size=self.model_config.gsv_max_data_size)
                gsv.fit(x_train_sample, y_train_sample)
            return gsv.best_params_
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def train(self):
        """Method to train the models one by one"""
        try:
            # Load training data
            x_train, y_train = load_split_data(data_path=self.data_config.train_split_path,
                                               target_column=self.data_config.target_column)

            # Transform training data
            x_train_transformed = perform_data_transformation(
                transformer_path=self.data_config.transformer_path,
                input_data=x_train)

            # Balance data in case of classification
            if self.model_config.model_task == "classification":
                # Oversample minority class to 40% of majority class
                over_sample = over_sampling.SMOTE(sampling_strategy=0.4,
                                                  random_state=42)
                # Undersample majority class to be double of minority class
                under_sample = under_sampling.RandomUnderSampler(sampling_strategy=0.5,
                                                                 random_state=42)
                resampler_pipeline = pipeline.make_pipeline(over_sample, under_sample)
                x_train_transformed, y_train = resampler_pipeline.fit_resample(
                    x_train_transformed, y_train)

            # Train all models
            for model in self.models:
                try:
                    model_name = type(model).__name__
                    param = self.model_config.model_params[model_name]
                except KeyError:
                    # When there are no model parameters
                    param = {}

                # Get best params using grid search
                best_params = self.perform_grid_search(
                    model=model, param=param, x_train=x_train_transformed, y_train=y_train)

                # Use gsv best params to train model
                model.set_params(**best_params)
                logger.info("Training started for %s", model_name)
                model.fit(x_train_transformed, y_train)
                logger.info("Training completed for %s", model_name)

                # Save the model
                model_save_path = self.model_config.trained_models_path+"/"+model_name+".pkl"
                save_object(file_path=model_save_path, obj=model)
                logger.info("%s  model saved to disk", model_name)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
