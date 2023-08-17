"""Module to define all evaluation metrics"""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src import logger


class MetricsClassification():
    """Class to define all classification evaluation metrics"""

    def __init__(self, is_binary: bool, pos_label: str):
        self.is_binary = is_binary
        self.pos_label = pos_label

    def evaluate_metric(self, eval_metric: str, actual, predicted):
        """Method to invoke evaluation"""
        try:
            return getattr(self, eval_metric)(actual, predicted)
        except AttributeError as ex:
            logger.exception("Error getting metric function: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    @staticmethod
    def get_best_score(scores: dict, metric_name: str):
        """Method to get the best score"""
        try:
            if metric_name != "":
                return max(sorted(scores.values()))
            return min(sorted(scores.values()))
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

    def precision_score(self, actual, predicted):
        """Method to calculate precision score"""
        try:
            if self.is_binary:
                score = precision_score(actual, predicted, pos_label=self.pos_label)
            else:
                score = precision_score(
                    actual, predicted, average="weighted")
            return score
        except Exception as ex:
            raise ex

    def recall_score(self, actual, predicted):
        """Method to calculate recall score"""
        try:
            if self.is_binary:
                score = recall_score(actual, predicted, pos_label=self.pos_label)
            else:
                score = recall_score(
                    actual, predicted, average="weighted")
            return score
        except Exception as ex:
            raise ex

    def f1_score(self, actual, predicted):
        """Method to calculate f1 score"""
        try:
            if self.is_binary:
                score = f1_score(actual, predicted, pos_label=self.pos_label)
            else:
                score = f1_score(actual, predicted, average="weighted")
            return score
        except Exception as ex:
            raise ex
