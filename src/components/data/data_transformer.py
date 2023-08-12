"""Module to transform data"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src import logger
from src.utils.common import (save_object)
from src.entities.config_entity import DataIngestionConfig, DataTransformationConfig


class DataTransformer():
    """Class to transform data"""

    def __init__(self, ingestion_config: DataIngestionConfig,
                 transformation_config: DataTransformationConfig):
        self.ingestion_config = ingestion_config
        self.transformation_config = transformation_config

    def get_input_data(self):
        """Method to get input data"""
        try:
            df_train = pd.read_csv(self.ingestion_config.data_train_path)
            df_test = pd.read_csv(self.ingestion_config.data_test_path)
            target_column = self.transformation_config.data_target_column
            x_train = df_train.drop(columns=[target_column], axis=1)
            y_train = df_train[target_column]
            x_test = df_test.drop(columns=[target_column], axis=1)
            y_test = df_test[target_column]
            return x_train, y_train, x_test, y_test
        except AttributeError as ex:
            raise ex
        except Exception as ex:
            raise ex

    @staticmethod
    def get_column_types(data_frame) -> dict:
        """Method to determine the column types"""
        try:
            column_types = {}
            column_types['numerical'] = data_frame.select_dtypes(
                exclude="object").columns
            column_types['categorical'] = data_frame.select_dtypes(
                include="object").columns
            return column_types
        except Exception as ex:
            raise ex

    @staticmethod
    def get_data_transformer(column_types: dict) -> object:
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
                    ('pipe_numerical', numerical_pipeline,
                     column_types['numerical']),
                    ('pipe_categorical', categorical_pipeline,
                     column_types['categorical'])
                ]
            )
            return data_transformer
        except Exception as ex:
            raise ex

    def transform_data(self):
        """Method to invoke data transformation"""
        try:
            x_train, y_train, x_test, y_test = self.get_input_data()
            column_types = self.get_column_types(x_train)
            data_transformer = self.get_data_transformer(
                column_types=column_types)
            data_transformer.fit(x_train)
            save_object(data_transformer,
                        self.transformation_config.data_transformer_path)
            logger.info("Saved data transformer object: %s",
                        self.transformation_config.data_transformer_path)

            np.save(self.transformation_config.data_transformed_x_train_array_path,
                    data_transformer.transform(x_train))
            np.save(self.transformation_config.data_transformed_x_test_array_path,
                    data_transformer.transform(x_test))
            np.save(self.transformation_config.data_transformed_y_train_array_path,
                    np.array(y_train))
            np.save(self.transformation_config.data_transformed_y_test_array_path,
                    np.array(y_test))
            logger.info("Transformed data arrays are saved to disk")
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
