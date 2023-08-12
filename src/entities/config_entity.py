"""
Module to hold all data classes
"""
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """Data class for data configurations"""
    data_original_path: Path
    data_train_path: Path
    data_test_path: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    """Data class for data transform configurations"""
    data_target_column: str
    data_transformer_path: Path
    data_transformed_x_train_array_path: Path
    data_transformed_x_test_array_path: Path
    data_transformed_y_train_array_path: Path
    data_transformed_y_test_array_path: Path


@dataclass(frozen=True)
class ModelConfig:
    """Data class for Model configuration"""
    model_objective: str
    model_trained_path: Path
    final_model_path: Path
    evaluation_metric: list
    evaluation_score_json_path: Path
    evaluation_metric_best_model: str
    model_params: dict
    mlflow_uri: str
