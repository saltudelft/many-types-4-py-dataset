# ./reset_commits.sh [spec file] [repos dir]

while IFS= read -r line
do
  split=( $line )
  url=${split[0]}
  commit=${split[1]}

  author=$(basename $(dirname $url))
  repo=$(basename $url .git)

  cd $2/$author/$repo
  git reset --hard $commit
  cd -

  break
done < "$1"