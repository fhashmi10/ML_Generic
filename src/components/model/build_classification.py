
"""
Module to build models classification models
This class can be extended to add more models or make changes to models
You can also choose to save the built base models and separate out training
"""
# from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
#from xgboost import XGBClassifier

from src import logger


def build_classification_models(selected_model: str) -> list:
    """Method to build classification models"""
    try:
        # LogisticRegression, -implement later as it predicts probabilities
        # and then need to find optimal cutoff
        models = [DecisionTreeClassifier(),
                  RandomForestClassifier(),
                  AdaBoostClassifier(),
                  GradientBoostingClassifier(),
                  #XGBClassifier()
                  ]
        if selected_model is not None:
            if selected_model.strip()!="":
                models = [model for model in models if selected_model in type(model).__name__]
        return models
    except Exception as ex:
        logger.exception(
            "Exception occured in building classification models: %s", ex)
        raise ex
