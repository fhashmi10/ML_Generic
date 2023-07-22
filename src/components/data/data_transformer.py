"""Module to transform data"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src import logger
from src.utils.common import (save_object)
from src.entities.config_entity import DataConfig


class DataTransformer():
    """Class to transform data"""

    def __init__(self, config: DataConfig):
        self.config = config

    @staticmethod
    def get_data_transformer(num_columns: list[str], cat_columns: list[str]) -> object:
        """Method to get data transformer object holding transformation pipeline"""
        try:
            numerical_pipeline = Pipeline(
                steps=[
                    # median when there are outliers
                    ('imputer', SimpleImputer(strategy="median")),
                    ('scaler', StandardScaler())
                ]
            )
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            data_transformer = ColumnTransformer(
                [
                    ('pipe_numerical', numerical_pipeline, num_columns),
                    ('pipe_categorical', categorical_pipeline, cat_columns)
                ]
            )
            return data_transformer
        except Exception as ex:
            raise ex

    def transform_data(self):
        """Method to invoke data transformation"""
        try:
            #todo: split this function
            df_train = pd.read_csv(self.config.data_train_path)
            df_test = pd.read_csv(self.config.data_test_path)

            target_column = self.config.data_target_column
            x_train = df_train.drop(columns=[target_column], axis=1)
            y_train = df_train[target_column]
            x_test = df_test.drop(columns=[target_column], axis=1)
            y_test = df_test[target_column]

            numerical_cols = x_train.select_dtypes(exclude="object").columns
            categorical_cols = x_train.select_dtypes(include="object").columns

            data_transformer = self.get_data_transformer(
                numerical_cols, categorical_cols)
            data_transformer.fit(x_train)
            save_object(data_transformer, self.config.data_transformer_path)
            logger.info("Saved data transformer object: %s", self.config.data_transformer_path)

            np.save(self.config.data_transformed_x_train_array_path,
                    data_transformer.transform(x_train))
            np.save(self.config.data_transformed_x_test_array_path,
                    data_transformer.transform(x_test))
            np.save(self.config.data_transformed_y_train_array_path,
                    np.array(y_train))
            np.save(self.config.data_transformed_y_test_array_path,
                    np.array(y_test))
            logger.info("Transformed data arrays are saved to disk")
        except AttributeError as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
        except Exception as ex:
            raise ex
