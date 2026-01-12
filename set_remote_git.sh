#!/bin/bash
# ./set_remote_git.sh
# "$(find . -type f -name "set_remote_git.sh")"


shopt -s expand_aliases
source ~/.bash_profile

echo '---------------- set_remote_git ----------------'
START_TIME="$(date +%s.%N)"
set_remote="$1"
project_root_directory="$(pwd)"

cd "$project_root_directory"
eval "$set_remote"

END_TIME="$(date +%s.%N)"
ELAPSED_TIME="$(echo "$END_TIME - $START_TIME" | bc)"
echo "実行時間:""$ELAPSED_TIME""s"
