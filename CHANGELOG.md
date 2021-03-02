# Changelog
All notable changes to the ManyTypes4Py dataset will be documented in this file.

## [0.4] - 2021-03-01
- Added type annotations coverage for processed projects and their source code files. See the `type_annot_cove` field in JSON files.
 
## [0.3] - 2021-01-29
- Fixed the path issue in `dataset_split.csv` file for some file paths that contains non-ASCII characters.
- With the new fixes to the [LibSA4py](https://github.com/saltudelft/libsa4py) tool, more source code files were processed for included Python projects.

## [0.2] - 2021-01-14
- Using the [LibSA4py](https://github.com/saltudelft/libsa4py) tool, all the Python projects were processed in JSON-formatted files.
- Using the [CD4Py](https://github.com/saltudelft/CD4Py) tool, the list of duplicate files in the dataset is provided in `duplicate_files.txt` file.
- The dataset is split into train, validation and test sets by source code files. The list of files and their corresponding set is provided in `dataset_split.csv` file.

## [0.1] - 2020-09-22
- Added a manifest file (`ManyTypes4PyDataset.spec`) that contains the URL and hash commits of 5.4K Python projects that were cloned on Sep. 17th 2020 from GitHub.
