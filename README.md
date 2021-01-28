# many-types-4-py-dataset
ManyTypes4Py: A benchmark dataset for machine learning-based type inference

To generate the manifest file of the dataset, use the following command:
```bash
find . -type d -mindepth 3 -maxdepth 3 -execdir sh -c 'echo "$(git config --get remote.origin.url) $(git log -n1 --format=format:"%H")"' \; | uniq > ManyTypes4PyDataset.spec
```

## Dataset preparation
**Pre-requisites:**
* Python dependencies from `scripts/requirements.txt` installed (run `pip install -r scripts/requirements.txt`)
* A repositories folder (dataset), where git projects are stored in format `[dataset path]/author/repo`

Run `./prepare_dataset.sh [dataset path]` in order to generate & prepare:
* A de-duplicated dataset
* Spec file for each project of the dataset (git url + commit)
* Train/test/validation split of the project (python code) files
* List of found duplicate files (that were also removed in the de-duped dataset)

### Steps

1. Generate spec-file - a CSV file, where rows consist of an URL and hash commit of the repository.

    - `find . -type d -mindepth 3 -maxdepth 3 -execdir sh -c 'echo "$(git config --get remote.origin.url) $(git log -n1 --format=format:"%H")"' \; | uniq > ManyTypes4PyDataset.spec`


2. Generate duplicate tokens for dataset using `cd4py`

    - `cd4py --p $1 --ot tokens --od py_dataset_duplicates.jsonl.gz --d 1024`

3. Gather duplicate files from the `cd4py` output tokens, and output as a single text file (using `collect_dupes.py`)

    - `python3 scripts/collect_dupes.py [output path]`

4. Create a copy dataset with duplicates removed from the duplicate files collected prior (using `process_dataset.py`)

    - `python3 scripts/process_dataset.py [dataset path] [duplicate files path] [new dataset path]`

5. Split dataset into test, train and validation data (using `split_dataset.py`)

    - `python3 scripts/split_dataset.py [dataset path] [output path]`

6. Create a tar of the full dataset & artifacts in one folder

    - `tar -czvf [output path] [dataset artifacts path]`
