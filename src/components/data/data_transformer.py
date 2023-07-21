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
    def __init__(self, config: DataConfig):
        self.config = config


    def get_data_transformer(self, num_columns: list[str], cat_columns: list[str]) -> object:
        try:
            numerical_columns=num_columns
            categorical_columns=cat_columns

            numerical_pipeline=Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy="median")),#median when there are outliers
                    ('scaler', StandardScaler())
                ]
            )

            categorical_pipeline=Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            data_transformer=ColumnTransformer(
                [
                    ('pipe_numerical', numerical_pipeline, numerical_columns),
                    ('pipe_categorical', categorical_pipeline, categorical_columns)
                ]
            )

            return data_transformer

        except Exception as e:
            logger.exception(e)
            raise e        
    

    def transform_data(self):
        try:
            df_train=pd.read_csv(self.config.data_train_path)
            df_test=pd.read_csv(self.config.data_test_path)

            target_column=self.config.data_target_column
            X_train=df_train.drop(columns=[target_column], axis=1)
            y_train=df_train[target_column]
            X_test=df_test.drop(columns=[target_column], axis=1)
            y_test=df_test[target_column]

            numerical_cols = X_train.select_dtypes(exclude="object").columns
            categorical_cols = X_train.select_dtypes(include="object").columns

            data_transformer=self.get_data_transformer(numerical_cols, categorical_cols)
            data_transformer.fit(X_train)
            save_object(data_transformer, self.config.data_transformer_path)

            X_train_arr=data_transformer.transform(X_train)
            X_test_arr=data_transformer.transform(X_test)

            np.save(self.config.data_transformed_X_train_array_path, X_train_arr)
            np.save(self.config.data_transformed_X_test_array_path, X_test_arr)
            np.save(self.config.data_transformed_y_train_array_path, np.array(y_train))
            np.save(self.config.data_transformed_y_test_array_path, np.array(y_test))
            
        except Exception as e:
            logger.exception(e)
            raise e      