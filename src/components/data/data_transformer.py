"""Module to transform data"""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src import logger
from src.utils.common import save_object
from src.entities.config_entity import DataConfig


class DataTransformer():
    """Class to transform data"""

    def __init__(self, data_config: DataConfig):
        self.data_config = data_config

    def get_input_data(self):
        """Method to get input data"""
        try:
            df_train = pd.read_csv(self.data_config.train_split_path)
            target_column = self.data_config.target_column
            x_train = df_train.drop(columns=[target_column], axis=1)
            y_train = df_train[target_column]
            return x_train, y_train
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
            x_train,_ = self.get_input_data()
            column_types = self.get_column_types(x_train)
            data_transformer = self.get_data_transformer(
                column_types=column_types)
            data_transformer.fit(x_train)
            save_object(data_transformer,
                        self.data_config.transformer_path)
            logger.info("Saved data transformer object: %s",
                        self.data_config.transformer_path)
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
