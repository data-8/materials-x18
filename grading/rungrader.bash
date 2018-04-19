#!/bin/bash
set -uxo pipefail
LAB=${1}
IMAGE=yuvipanda/materials-x18

gcloud compute ssh prod-fileserver-01 -- "cd /export/pool0/homes && sudo rm -f ${LAB}.csv && sudo docker pull ${IMAGE} && sudo find . -name ${LAB}.ipynb | awk -F / '{ print \$2; }'  | xargs -L1 -P 32 sudo ./grade.bash ${LAB} 2> /dev/null"
echo "Finished fileserver-01 $?"
gcloud compute ssh prod-fileserver-02 -- "cd /export/pool0/homes && sudo rm -f ${LAB}.csv && sudo docker pull ${IMAGE} && sudo find . -name ${LAB}.ipynb | awk -F / '{ print \$2; }'  | xargs -L1 -P 32 sudo ./grade.bash ${LAB} 2> /dev/null"
echo "Finished fileserver-02 $?"

gcloud compute scp  prod-fileserver-01:/export/pool0/homes/${LAB}.csv prod-fileserver-01-${LAB}.csv
gcloud compute scp  prod-fileserver-02:/export/pool0/homes/${LAB}.csv prod-fileserver-02-${LAB}.csv

python grading/csvgrade.py ${LAB}-launch-info.csv prod-fileserver-01-${LAB}.csv
python grading/csvgrade.py ${LAB}-launch-info.csv prod-fileserver-02-${LAB}.csv
