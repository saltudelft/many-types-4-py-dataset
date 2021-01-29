# Scripts

`./prepare_dataset.sh [dataset]`
- Runs the scripts in the directory on a target `dataset` to prepare & zip it. See dataset preparation section for more info.

`python3 analyze_dataset.py [pickle_path] [dataset]`
- Analyzes the dataset by showing the size distribution for each file extension. Reads a dataframe from `pickle_path`, and if the dataframe does not exist, reads all files from the `dataset` and creates a dataframe with columns `file` and `size`, covering all the dataset's files.

`python3 collect_dupes.py [token_path] [duplicate_out]` 

- Ingests a tokens zip file generated from `cd4py` given by `token_path`, and outputs a text file of the paths to duplicate files to `duplicate_out`.

`python3 count_files.py [dir]`

- Counts number of files & Python code files in the specified directory

`python3 count_lines.py [path]`

- Counts number of lines in the specified text file

`python3 process_dataset.py [dataset] [duplicate_list] [copy_target]`

- Creates a copy of the provided `dataset`, with all files in `duplicate_list` removed from the new dataset. All non-existent (empty) files (i.e. such that show `False` on `os.path.exists`) are also filtered out in the new dataset. The new dataset is output to the `copy_target` path.

`python3 remove_extensions.py [dataset] [extension_list]`
- Removes all files with the extension list defined in `extension_list` from directory `dataset` (and all it's subdirectories)

`python3 split_dataset.py [dataset] --od [output_path] --test [test] --valid [valid]`

- Splits the dataset's `.py` files into test, train and validation sets. `test` defines the ratio (from 0.0 to 1.0) to use for the test set, while `valid` defines this ratio for the validation set. The script outputs a CSV file to `output_path`, where each row is in shape: `type,path`, where `type` equals one of: `{train, test, valid}`.

`./reset_commits.sh [spec file] [dataset]`

- Resets commits on all projects in the `dataset` folder to the commit hashes given in the provided `spec file`. Commits are reset by means of `git reset --hard [hash]`.