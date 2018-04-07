#!/bin/bash
set -euo pipefail

IPYNB_PATH=${1}

cat /dev/stdin > $IPYNB_PATH

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python3 ${DIR}/grade.py ${IPYNB_PATH}