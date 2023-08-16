"""Module to define all evaluation metrics"""
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, \
    classification_report, confusion_matrix, accuracy_score
from src import logger


class EvalMetrics():
    """Class to define all evaluation metrics"""

    def __init__(self):
        pass

    @staticmethod
    def get_best_score(scores: dict, metric_name: str):
        """Method to get the best score"""
        try:
            if metric_name == "r2_score":
                return max(sorted(scores.values()))
            return min(sorted(scores.values()))
        except Exception as ex:
            raise ex

    @staticmethod
    def r2_score(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = r2_score(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def mean_squared_error(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = np.sqrt(mean_squared_error(actual, predicted))
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def mean_absolute_error(actual, predicted):
        """Method to calculate r2_score"""
        try:
            score = mean_absolute_error(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def classification_report(actual, predicted):
        """Method to calculate classification report"""
        try:
            score = classification_report(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def confusion_matrix(actual, predicted):
        """Method to calculate confusion matrix"""
        try:
            score = confusion_matrix(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    @staticmethod
    def accuracy_score(actual, predicted):
        """Method to calculate accuracy score"""
        try:
            score = accuracy_score(actual, predicted)
            return score
        except Exception as ex:
            raise ex

    def evaluate_metric(self, eval_metric: str, actual, predicted):
        """Method to invoke evaluation"""
        try:
            return getattr(self, eval_metric)(actual, predicted)
        except AttributeError as ex:
            logger.exception("Error getting metric function: %s", ex)
            raise ex
        except Exception as ex:
            raise ex
