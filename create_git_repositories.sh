#!/bin/bash
# ./create_git_repositories.sh
# "$(find . -type f -name "create_git_repositories.sh")"
# create_git_repositories


shopt -s expand_aliases
source ~/.bash_profile

echo '---------------- create_git_repositories ----------------'
START_TIME="$(date +%s.%N)"

file_absolute_path="$(readlink -f "$0")"
project_root_directory="$(dirname "$file_absolute_path")"

cd ~/Desktop/running-terminal-commands/github/$(date +%Y%m%d_zip)
while IFS= read -r repository; do
    python "$project_root_directory""/main.py" "$repository"
done <<< "$(find . -type d ! -name "zip_folder" ! -name "." -maxdepth 1 | xargs -I {} basename {} | sort)"

END_TIME="$(date +%s.%N)"
ELAPSED_TIME="$(echo "$END_TIME - $START_TIME" | bc)"
echo "実行時間:""$ELAPSED_TIME""s"
