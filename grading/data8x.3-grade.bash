#!/bin/bash
# Grade data8x.3 in a loop
# Explicitly no '-e', since we want grading to continue even if rungrader barfs
set -uo pipefail
while 1; do
    docker pull yuvipanda/materials-x18
    echo 'Grading lab01'
    python3 rungrader.py \
        '/mnt/prod-3-fileserver/{user_id}/materials-x18/materials/x18/lab/3/{lab}/{lab}.ipynb' \
        '/srv/repo/materials/x18/lab/3/{lab}/{lab}.ipynb' \
        lab01 \
        courses.edx.org-adcc1672ebcb43b7b62b72abaa434e9c


    sleep 1;
done
