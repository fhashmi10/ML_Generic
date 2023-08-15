
"""
Module to build models
"""
from components.model.build_regression import build_regression_models
from components.model.build_classification import build_classification_models
from src import logger

def build_models_list(model_objective: str) -> list:
    """Method to invoke model training"""
    try:
        if model_objective=="classification":
            models=build_classification_models()
        elif model_objective=="regression":
            models=build_regression_models()
        else:
            logger.exception("Model objective is not recognized.")
            raise ValueError
        return models
    except ValueError as ex:
        raise ex
    except Exception as ex:
        logger.exception("Exception occured: %s", ex)
        raise ex
