from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    data_original_path: Path
    data_train_path: Path
    data_test_path: Path
    data_target_column: str
    data_transformer_path: Path
    data_transformed_train_array_path: Path
    data_transformed_test_array_path: Path
