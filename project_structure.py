import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

source_path = "src"

list_files = [
    ".github/workflows/.gitkeep",
    "notebook/experiments.ipynb",
    "configuration/config.yaml",
    "configuration/params.yaml",
    f"{source_path}/__init__.py",
    f"{source_path}/config/__init__.py",
    f"{source_path}/config/configuration_manager.py",
    f"{source_path}/common/__init__.py",
    f"{source_path}/common/utils.py",
    f"{source_path}/entities/__init__.py",
    f"{source_path}/entities/config_entity.py",
    f"{source_path}/components/__init__.py",
    f"{source_path}/components/data_ingestion.py",
    f"{source_path}/components/data_transformer.py",
    f"{source_path}/components/model_builder.py",
    f"{source_path}/components/model_trainer.py",
    f"{source_path}/pipeline/__init__.py",
    f"{source_path}/pipeline/training_pipeline/__init__.py",
    f"{source_path}/pipeline/prediction_pipeline/__init__.py",
    f"{source_path}/pipeline/prediction_pipeline/model_prediction_pipeline.py",
    #"dvc.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "templates/index.html"
]


for filepath in list_files:
    filepath = Path(filepath)

    if os.path.exists(filepath):
        logging.info(f"{filename} is already exists")
    else:
        filedir, filename = os.path.split(filepath)

        if filedir!="":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")