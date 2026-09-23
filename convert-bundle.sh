#!/bin/bash
set -euo pipefail

curl -s -O "https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"

tar -xzf lab3-bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

DATA_ROWS=$(($(wc -l < cleaned.csv) -1))
echo "$DATA_ROWS"

tar -czf converted-archive.tar.gz cleaned.csv
