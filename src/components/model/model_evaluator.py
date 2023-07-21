from sklearn.metrics import r2_score
from src import logger

class ModelEvaluator:
    def __init__(self, metric: str, actual, predicted):
        self.metric = metric
        self.actual = actual
        self.predicted = predicted


    def evaluate(self):
        return getattr(self, str(self.metric))()


    def r2_score(self):
        score = r2_score(self.actual, self.predicted)
        return score
