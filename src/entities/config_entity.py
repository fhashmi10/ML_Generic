"""
Module to hold all data classes
"""
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    """Data class for data configurations"""
    input_path: Path
    train_split_path: Path
    test_split_path: Path
    target_column: str
    transformer_path: Path


@dataclass(frozen=True)
class ModelConfig:
    """Data class for Model configuration"""
    model_task: str
    trained_models_path: Path
    final_model_path: Path
    selected_model: str
    model_params: dict


@dataclass(frozen=True)
class EvalConfig:
    """Data class for Evaluation configuration"""   
    is_binary: bool
    pos_label: str
    eval_metrics: list
    eval_metric_selection: str
    eval_scores_path: Path
    mlflow_uri: str
