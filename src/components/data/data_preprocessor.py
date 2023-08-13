"""Module to define data preprocessing steps"""
import pandas as pd
from src import logger


@staticmethod
def preprocess_data(data_frame) -> pd.DataFrame:
    """Method to perform data preprocessing"""
    try:
        # Drop unneccessary columns
        # data_frame.drop('col_name', axis=1, inplace=True)

        # Datetime Handling
        # data_frame[['date_col_1', 'date_col_2']] = data_frame[
        #    ['date_col_1', 'date_col_2']].apply(pd.to_datetime)
        # data_frame['derived_col'] = (
        #    data_frame['date_col_1'] - data_frame['date_col_2'])/pd.Timedelta(days=1)
        # data_frame['derived_col'].apply(pd.to_numeric)
        # data_frame.drop('date_col_1', axis=1, inplace=True)
        # data_frame.drop('date_col_2', axis=1, inplace=True)

        # Derived Metrics
        # data_frame[['col_1', 'col_2']
        #            ] = data_frame['org_col'].str.split('/', expand=True)
        # data_frame[['col_1', 'col_2']] = data_frame[
        #    ['col_1', 'col_2']].apply(pd.to_numeric)
        # data_frame.drop('org_col', axis=1, inplace=True)

        # Replace bad characters with nan
        # data_frame.replace('?', np.nan, inplace=True)
        return data_frame
    except Exception as ex:
        logger.exception("Exception occured while pre-processing data %s", ex)
        raise ex
