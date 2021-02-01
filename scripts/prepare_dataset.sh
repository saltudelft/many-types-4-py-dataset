# ./prepare_dataset.sh <dataset dir>

# 0. Prepare output directory
mkdir ManyTypes4Py

# 1. Generate spec file (git_repo_url hash)
cd $1
find . -type d -mindepth 3 -maxdepth 3 -execdir sh -c 'echo "$(git config --get remote.origin.url) $(git log -n1 --format=format:"%H")"' \; | uniq > ManyTypes4PyDataset.spec
cd -
mv $1/ManyTypes4PyDataset.spec ManyTypes4Py/ManyTypes4PyDataset.spec

# 2. Generate duplicate tokens for dataset, output in 'tokens' dir
cd4py --p $1 --ot tokens --od py_dataset_duplicates.jsonl.gz --d 1024

# 3. Collect duplicates into a single 'duplicate_files.txt' file
python3 collect_dupes.py duplicate_files.txt
mv duplicate_files.txt ManyTypes4Py/duplicate_files.txt

# 4. Make copy of dataset without duplicates
mv $1 repos_
python3 process_dataset.py repos_ ManyTypes4Py/duplicate_files.txt repos

# 5. Split dataset files into train, test, validate
python3 split_dataset.py repos --od ManyTypes4Py/dataset_split.csv
mv repos ManyTypes4Py/repos

# 6. Zip contents
tar -czvf dataset.tar.gz ManyTypes4Py
