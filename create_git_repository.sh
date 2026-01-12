#!/bin/bash
# ./create_git_repository.sh
# "$(find . -type f -name "create_git_repository.sh")"
# create_git_repository


shopt -s expand_aliases
source ~/.bash_profile

echo '---------------- create_git_repository ----------------'
START_TIME="$(date +%s.%N)"

file_absolute_path="$(readlink -f "$0")"
project_root_directory="$(dirname "$file_absolute_path")"
repository_name="$1"

python "$project_root_directory""/main.py" "$repository_name"
result="$(python "$project_root_directory""/get_url.py" "$repository_name")"
echo "$result"
"$project_root_directory""/""set_remote_git.sh" "$result"

END_TIME="$(date +%s.%N)"
ELAPSED_TIME="$(echo "$END_TIME - $START_TIME" | bc)"
echo "実行時間:""$ELAPSED_TIME""s"
