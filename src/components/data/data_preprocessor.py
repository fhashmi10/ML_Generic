"""Module to define data preprocessing steps"""
import pandas as pd
# import numpy as np
from src import logger


# def times_of_the_day(hour_day: int) -> str:
#     """Method to return times of the day"""
#     try:
#         if 6 >= hour_day <= 10:
#             return "Morning"
#         if 11 >= hour_day <= 16:
#             return "Day"
#         if 17 >= hour_day <= 21:
#             return "Evening"
#         return "Night"
#     except Exception:
#         return "Night"


def preprocess_data(data_frame) -> pd.DataFrame:
    """Method to perform data preprocessing"""
    try:
        # # Drop unneccessary columns
        # drop_columns_list = ["policy_number",
        #                      "incident_location",
        #                      "insured_occupation",
        #                      "insured_hobbies",
        #                      "incident_city",
        #                      "total_claim_amount",
        #                      "auto_model",
        #                      "auto_make",
        #                      "insured_zip",
        #                      "_c39"]
        # for col_name in drop_columns_list:
        #     data_frame.drop(col_name, axis=1, inplace=True)

        # # Datetime Handling
        # data_frame[["policy_bind_date", "incident_date"]] = data_frame[[
        #     "policy_bind_date", "incident_date"]].apply(pd.to_datetime)
        # data_frame["incident_days_since_inception"] = (
        #     data_frame["incident_date"] - data_frame["policy_bind_date"])/pd.Timedelta(days=1)
        # data_frame["incident_days_since_inception"].apply(pd.to_numeric)
        # data_frame.drop("incident_date", axis=1, inplace=True)
        # data_frame.drop("policy_bind_date", axis=1, inplace=True)

        # # Derived Metrics
        # data_frame[["policy_csl_low", "policy_csl_high"]
        #            ] = data_frame["policy_csl"].str.split("/", expand=True)
        # data_frame[["policy_csl_low", "policy_csl_high"]] = data_frame[[
        #     "policy_csl_low", "policy_csl_high"]].apply(pd.to_numeric)
        # data_frame.drop("policy_csl", axis=1, inplace=True)

        # data_frame["out_of_state"] = data_frame.apply(
        #     lambda x: "NO" if x["incident_state"] == x["policy_state"] else "YES", axis=1)
        # data_frame.drop("incident_state", axis=1, inplace=True)

        # data_frame["cap_gains"] = data_frame["capital-gains"] + \
        #     data_frame["capital-loss"]
        # data_frame.drop("capital-gains", axis=1, inplace=True)
        # data_frame.drop("capital-loss", axis=1, inplace=True)
        # # Ideally needs below preprocessing as well
        # # auto year - derive how old
        # # insured_zip - make it categorical - deleted for now
        # # incident_hour_of_the_day- make eve, morn, day, night
        # data_frame["incident_hour_of_the_day"] = data_frame["incident_hour_of_the_day"].apply(
        #     lambda x: times_of_the_day(x))

        # # Replace bad characters with nan
        # data_frame.replace("?", np.nan, inplace=True)

        # # Bad data handling
        # data_frame["umbrella_limit"] = data_frame["umbrella_limit"].apply(
        #     lambda x: 1000000 if x == -1000000 else x)

        # # Empty data handling
        # data_frame["authorities_contacted"].fillna("None", inplace=True)
        # data_frame["police_report_available"] = data_frame["police_report_available"].apply(
        #     lambda x: "NO" if x is np.nan else x)

        # Outlier handling
        return data_frame
    except Exception as ex:
        logger.exception("Exception occured while pre-processing data %s", ex)
        raise ex
