"""Module to transform data"""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src import logger
from src.utils.common import save_object
from src.utils.helper import load_split_data
from src.entities.config_entity import DataConfig


class DataTransformer():
    """Class to transform data"""

    def __init__(self, data_config: DataConfig):
        self.data_config = data_config

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
    def create_transformation_pipeline(column_types: dict) -> object:
        """Method to create data transformer object holding transformation pipeline"""
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

    def build_data_transformer(self):
        """Method to build a data transformer"""
        try:
            # Load train data
            x_train, _ = load_split_data(data_path=self.data_config.train_split_path,
                                         target_column=self.data_config.target_column)

            # Create transformation pipeline
            column_types = self.get_column_types(x_train)
            data_transformer = self.create_transformation_pipeline(
                column_types=column_types)
            data_transformer.fit(x_train)

            # Save data transformer object
            save_object(data_transformer,
                        self.data_config.transformer_path)
            logger.info("Saved data transformer object.")
        except AttributeError as ex:
            logger.exception("Error finding attribute: %s", ex)
            raise ex
        except Exception as ex:
            logger.exception("Exception occured: %s", ex)
            raise ex
