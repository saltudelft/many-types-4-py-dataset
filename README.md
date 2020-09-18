# many-types-4-py-dataset
ManyTypes4Py: A benchmark dataset for machine learning-based type inference

To generate the manifest file of the dataset, use the following command:
```bash
find . -type d -mindepth 3 -maxdepth 3 -execdir sh -c 'echo "$(git config --get remote.origin.url) $(git log -n1 --format=format:"%H")"' \; | uniq > ManyTypes4PyDataset.spec
```
