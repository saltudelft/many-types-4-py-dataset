# ManyTypes4Py: A Benchmark Python Dataset for Machine Learning-based Type Inference
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4719447.svg)](https://doi.org/10.5281/zenodo.4719447)

- [Intro](#intro)
- [Download](#downloading-dataset)
- [Preparation](#dataset-preparation)
- [Citing MT4Py](#citing-the-dataset)
- [Roadmap](#roadmap)

# Intro
- It has *clean* and *complete* versions (from v0.7):
  - The clean version has 5.1K **type-checked** Python repositories and 1.2M type annotations.
  - The complete version has 5.2K Python repositories and 3.3M type annotations.
- Its source files are type-checked using mypy (clean version).
- Its projects were processed in JSON-formatted files using the [LibSA4Py](https://github.com/saltudelft/libsa4py) pipeline.
- Its source files were already split into training, validation, and test sets for training ML models.
- It is de-duplicated using [CD4Py](https://github.com/saltudelft/CD4Py).
- It contains **Visible Type Hints** (VTHs), which is a deep, recursive, and dynamic analysis of types from the import statements of source files and their dependencies.
- It is published in the Data Showcase of the **MSR'21** conference.

# Downloading dataset
The latest version of the dataset is publicly available on [zenodo](https://doi.org/10.5281/zenodo.4044635).

# Dataset preparation
We highly recommend downloading the latest version of the dataset as described above. If you want to manually prepare the dataset, follow below instructions.

## Requirements

* Python 3.5 or newer
* Python dependencies from `scripts/requirements.txt` installed (run `pip install -r scripts/requirements.txt`)
* Install the `libsa4py` package (run `git clone https://github.com/saltudelft/libsa4py.git && cd libsa4py && pip install .`)

## Steps

0. Clone the dataset:

    ```
    python -m repo_cloner -i ./mypy-dependents-by-stars.json -o repos
    ```
    
1. To change the state of the cloned repositories to the ManyType4Py's, run the following command on the `ManyTypes4PyDataset.spec`:
    
    ```
    ./scripts/reset_commits.sh  ./ManyTypes4PyDataset.spec repos
    ``` 

2. Generate duplicate tokens for dataset using `cd4py`

    ```
    cd4py --p repos --ot tokens --od manytypes4py_dataset_duplicates.jsonl.gz --d 1024
    ```

3. Gather duplicate files from the `cd4py` output tokens, and output as a single text file (using `collect_dupes.py`)

    ```
    python3 scripts/collect_dupes.py manytypes4py_dataset_duplicates.jsonl.gz manytypes4py_dup_files.txt
    ```

4. Create a copy dataset with duplicates removed from the duplicate files collected prior (using `process_dataset.py`)

    ```
    python3 scripts/process_dataset.py repos manytypes4py_dup_files.txt [new dataset path]
    ```

5. Split dataset into test, train and validation data (using `split_dataset.py`)

    ```
    python3 scripts/split_dataset.py [new dataset path] manytypes4py_split.csv
    ```

6. To process the Python repositories and produce JSON output files, run the `libsa4py` pipeline as follows:

    ```
    libsa4py process --p [new dataset path] --o [processed projects path] --s manytypes4py_split.csv --j [WORKERS COUNT]
    ```

    Check out the `libsa4py` [README](https://github.com/saltudelft/libsa4py#usage) for more info on its usage.
    
6. Create a tar of the full dataset & artifacts in one folder

    ```
    tar -czvf [output path] [dataset artifacts path]
    ```

# Citing the dataset
If you have used the dataset in your research work, please consider citing it.

```
@inproceedings{mt4py2021,
author = {A. M. Mir and E. Latoskinas and G. Gousios},
booktitle = {IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)},
title = {ManyTypes4Py: A Benchmark Python Dataset for Machine Learning-Based Type Inference},
year = {2021},
pages = {585-589},
doi = {10.1109/MSR52588.2021.00079},
publisher = {IEEE Computer Society},
month = {May}
}
```

# Roadmap
- Gathering Python projects that depend on type-checkers other than mypy, i.e., pyre, pytype, and pyright.
- Apply type annotations from [typeshed](https://github.com/python/typeshed) to the dataset.