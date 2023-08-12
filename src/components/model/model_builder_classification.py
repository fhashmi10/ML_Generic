
"""
Module to build models classification models
This class can be extended to add more models or make changes to models
You can also choose to save the built base models and separate out training
"""
from sklearn.tree import DecisionTreeClassifier

from src import logger

def build_classification_models() -> list:
    """Method to build classification models"""
    try:
        models = [
                    DecisionTreeClassifier()
                    ]
        return models
    except Exception as ex:
        logger.exception("Exception occured in building classification models: %s", ex)
        raise ex
