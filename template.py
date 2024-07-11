import os
from pathlib import Path

list_of_files = [
    ".github/workflows.gitkeep",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipline/__init__.py",
    "src/pipline/training.py",
    "src/pipline/predictionni.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logger.py",
    "src/exceptions/exceptions.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.tml",
    "tox.ini",
    "experiment/experiments.ipynb"


]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        #logging.info("Creating directory {file_dir} for the file : {}".format(file_dir, filename))

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass