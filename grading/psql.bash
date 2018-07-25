#!/bin/bash
# Connect to prod NFS or hub sharder db
set -euo pipefail
DB=${1:-hubshard}
psql -h /var/run/csql/data8x-scratch:us-central1:prod-${DB}-db-instance -U  prod-db-proxyuser prod-${DB}-sharder-db
