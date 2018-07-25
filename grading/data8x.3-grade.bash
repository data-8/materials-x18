#!/bin/bash
# Grade data8x.3 in a loop
set -euo pipefail
while 1; do
    docker pull yuvipanda/materials-x18
    echo 'Grading lab01 on prod-fileserver-01'
    python3 rungrader.py \
        '/mnt/prod-fileserver-01/{user_id}/materials-x18/materials/x18/lab/3/{lab}/{lab}.ipynb' \
        '/srv/repo/materials/x18/lab/3/{lab}/{lab}.ipynb' \
        lab01 \
        courses.edx.org-adcc1672ebcb43b7b62b72abaa434e9c

    echo 'Grading lab02 on prod-fileserver-02'
    python3 rungrader.py \
        '/mnt/prod-fileserver-01/{user_id}/materials-x18/materials/x18/lab/3/{lab}/{lab}.ipynb' \
        '/srv/repo/materials/x18/lab/3/{lab}/{lab}.ipynb' \
        lab01 \
        courses.edx.org-adcc1672ebcb43b7b62b72abaa434e9c

    sleep 1;
done
