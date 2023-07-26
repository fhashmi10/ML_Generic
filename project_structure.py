"""Module to generate a project structure"""
import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

SOURCE_PATH = "src"

list_files = [
    ".github/workflows/.gitkeep",
    "notebook/experiments.ipynb",
    "config/config.yaml",
    "config/params.yaml",
    f"{SOURCE_PATH}/__init__.py",
    f"{SOURCE_PATH}/configuration/__init__.py",
    f"{SOURCE_PATH}/configuration/configuration_manager.py",
    f"{SOURCE_PATH}/utils/__init__.py",
    f"{SOURCE_PATH}/utils/common.py",
    f"{SOURCE_PATH}/entities/__init__.py",
    f"{SOURCE_PATH}/entities/config_entity.py",
    f"{SOURCE_PATH}/components/__init__.py",
    f"{SOURCE_PATH}/components/data/__init__.py",
    f"{SOURCE_PATH}/components/data/data_ingestion.py",
    f"{SOURCE_PATH}/components/data/data_transformer.py",
	f"{SOURCE_PATH}/components/model/__init__.py",
    f"{SOURCE_PATH}/components/model/model_builder.py",
    f"{SOURCE_PATH}/components/model/model_trainer.py",
    f"{SOURCE_PATH}/pipeline/__init__.py",
    f"{SOURCE_PATH}/pipeline/training_pipeline/__init__.py",
    f"{SOURCE_PATH}/pipeline/prediction_pipeline/__init__.py",
    f"{SOURCE_PATH}/pipeline/prediction_pipeline/model_prediction_pipeline.py",
    # "dvc.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "templates/index.html"
]


for filepath in list_files:
    filepath = Path(filepath)

    if os.path.exists(filepath):
        logging.info("%s is already exists", filepath)
    else:
        filedir, filename = os.path.split(filepath)
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info("Creating directory; %s for the file: %s",
                         filedir, filename)
        with open(filepath, "w", encoding="utf8") as f:
            logging.info("Creating empty file: %s", filepath)
