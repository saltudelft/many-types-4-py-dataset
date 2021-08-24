# Creates a compressed file of the dataset for releasing a new version.
# $1: Path to the JSON files of processed projects (complete version)
# $2: Path to the JSON files of processed projects (clean version)
# $3: A release tag, e.g., v0.6

mkdir "./ManyTypes4PyDataset-$3"
cp -a "../data/." "./ManyTypes4PyDataset-$3"
cp "../CHANGELOG.md" "./ManyTypes4PyDataset-$3"

cp -a "$1" "./ManyTypes4PyDataset-$3"
mv "./ManyTypes4PyDataset-$3/processed_projects" "./ManyTypes4PyDataset-$3/processed_projects_complete"
cp -a "$2" "./ManyTypes4PyDataset-$3"
mv "./ManyTypes4PyDataset-$3/processed_projects" "./ManyTypes4PyDataset-$3/processed_projects_clean"

tar -czvf "ManyTypes4PyDataset-$3.tar.gz" "./ManyTypes4PyDataset-$3"