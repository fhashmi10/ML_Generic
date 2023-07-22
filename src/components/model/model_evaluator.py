"""Module to evaluate models"""
from sklearn.metrics import r2_score
from src import logger

class ModelEvaluator:
    """Class to evaluate models"""
    def __init__(self, metric: str, actual, predicted):
        self.metric = metric
        self.actual = actual
        self.predicted = predicted

    def evaluate(self):
        """Method to invoke model evaluation"""
        try:
            return getattr(self, str(self.metric))()
        except AttributeError as ex:
            logger.error("Error getting metric function: %s", ex)
            raise ex
        except Exception as ex:
            raise ex

    def r2_score(self):
        """Method to calculate r2_score"""
        try:
            score = r2_score(self.actual, self.predicted)
            return score
        except Exception as ex:
            raise ex

