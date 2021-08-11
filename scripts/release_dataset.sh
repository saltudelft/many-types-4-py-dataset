# Creates a compressed file of the dataset for releasing a new version.
# $1: Path to the JSON files of processed projects
# $2: A release tag, e.g., v0.6

mkdir "./ManyTypes4PyDataset-$2"
cp -a "../data/." "./ManyTypes4PyDataset-$2"
cp "../CHANGELOG.md" "./ManyTypes4PyDataset-$2"
cp -a "$1" "./ManyTypes4PyDataset-$2"

tar -czvf "ManyTypes4PyDataset-$2.tar.gz" "./ManyTypes4PyDataset-$2"