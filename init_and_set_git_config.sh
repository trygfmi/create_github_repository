#!/bin/bash
# ./init_and_set_git_config.sh
# "$(find . -type f -name "init_and_set_git_config.sh")"


shopt -s expand_aliases
source ~/.bash_profile

echo '---------------- init_and_set_git_config ----------------'
START_TIME="$(date +%s.%N)"
set_remote="$1"
project_root_directory="$(pwd)"

cd "$project_root_directory"
git init
eval "$set_remote"

END_TIME="$(date +%s.%N)"
ELAPSED_TIME="$(echo "$END_TIME - $START_TIME" | bc)"
echo "実行時間:""$ELAPSED_TIME""s"
