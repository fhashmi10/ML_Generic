"""
Module to hold all data classes
"""
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    """Data class for data configurations"""
    data_original_path: Path
    data_train_path: Path
    data_test_path: Path
    data_target_column: str
    data_transformer_path: Path
    data_transformed_X_train_array_path: Path
    data_transformed_X_test_array_path: Path
    data_transformed_y_train_array_path: Path
    data_transformed_y_test_array_path: Path


@dataclass(frozen=True)
class ModelConfig:
    """Data class for Model configuration"""
    model_trained_path: Path
