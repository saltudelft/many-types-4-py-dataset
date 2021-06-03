# Dataset Description

- `processed_projects`: Contains JSON-formatted processed projects. See this [file](https://github.com/saltudelft/libsa4py/blob/master/JSONOutput.md) for info about the JSON fields.
- `dataset_split_files.csv`: Contains source files' path for the training, validation, test sets (split randomly by files).
- `dataset_split_projects.csv`: Contains source files' path for the training, validation, test sets (split randomly by projects).
- `duplicate_files.txt`: Contains the list of duplicate source files in the original dataset.
- `ManyTypes4PyDataset.spec`: Contains the GitHub URL of the projects and their commit hash at clone time.
- `MT4Py_VTHs.csv`: Contains extracted visible type hints and their frequency for the whole dataset.
- `mypy-dependents-by-stars.json`: Contains Python projects on GitHub, which depend on `mypy`.