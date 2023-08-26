"""Module to transform data"""
import itertools
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

from src import logger
from src.utils.common import save_object
from src.utils.helper import load_split_data
from src.entities.config_entity import SchemaConfig, DataConfig


class DataTransformer():
    """Class to transform data"""

    def __init__(self, schema_config: SchemaConfig, data_config: DataConfig):
        self.schema_config = schema_config
        self.data_config = data_config

    def get_column_types(self, data_frame) -> dict:
        """Method to determine the column types"""
        try:
            # Define column type dictionary
            column_types = {
                "numerical": [],
                "ordinal_cols": [],
                "date_columns": [],
                "categorical": []
            }

            # Set numerical columns
            column_types["numerical"] = data_frame.select_dtypes(
                exclude="object").columns

            # Set ordinal categorical and date columns
            if self.schema_config.ordinal_cols is not None:
                column_types["ordinal_cols"] = \
                    [col_name.strip()
                     for col_name in self.schema_config.ordinal_cols.split(',')]
            if self.schema_config.date_columns is not None:
                column_types["date_columns"] = \
                    [col_name.strip()
                     for col_name in self.schema_config.date_columns.split(',')]

            # Set one hot categorical columns
            predefined_categorical_cols = list(itertools.chain(column_types["ordinal_cols"],
                                                               column_types["date_columns"]))
            all_categorical_cols = data_frame.select_dtypes(
                include="object").columns
            column_types["categorical"] = [col_name for col_name in all_categorical_cols
                                           if col_name not in predefined_categorical_cols]
            return column_types
        except Exception as ex:
            raise ex

    @staticmethod
    def create_transformation_pipeline(column_types: dict) -> object:
        """Method to create data transformer object holding transformation pipeline"""
        try:
            numerical_pipeline = make_pipeline(
                SimpleImputer(strategy="median"),
                StandardScaler()
            )
            one_hot_pipeline = make_pipeline(
                SimpleImputer(strategy="most_frequent"),
                OneHotEncoder(),
                StandardScaler(with_mean=False)
            )
            ordinal_pipeline = make_pipeline(
                SimpleImputer(strategy="most_frequent"),
                OrdinalEncoder(),
                StandardScaler(with_mean=False)
            )

            # date columns are ignored on assumption that
            # features are derived using them during data preprocessing
            data_transformer = make_column_transformer(
                (numerical_pipeline, column_types['numerical']),
                (one_hot_pipeline, column_types['categorical']),
                (ordinal_pipeline, column_types['ordinal_cols'])
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
