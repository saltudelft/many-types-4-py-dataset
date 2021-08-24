# Dataset Description

- `processed_projects_complete`: Contains JSON-formatted processed projects (complete version). See this [file](https://github.com/saltudelft/libsa4py/blob/master/JSONOutput.md) for info about the JSON fields.
- `processed_projects_clean`: Contains JSON-formatted processed projects (clean version).
- `dataset_split.csv`: Contains source files' path for the training, validation, test sets.
- `duplicate_files.txt`: Contains the list of duplicate source files in the original dataset.
- `ManyTypes4PyDataset.spec`: Contains the GitHub URL of the projects and their commit hash at clone time.
- `MT4Py_VTHs.csv`: Contains extracted visible type hints and their frequency for the whole dataset.
- `mypy-dependents-by-stars.json`: Contains Python projects on GitHub, which depend on `mypy`.
- `type_checked_files.txt`: Contains a list of type-checked Python source files in the dataset (using `mypy`).