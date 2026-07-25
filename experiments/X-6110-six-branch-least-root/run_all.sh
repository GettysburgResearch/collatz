#!/bin/sh
# Reproduce the published X-6110 table: bound 2^256, depth cap 16, six parallel branches.
set -e
E=${1:-256}
D=${2:-16}
make >/dev/null
mkdir -p results
for b in 0 1 2 3 4 5; do
    ./lr "$E" "$D" "$b" > "results/branch_$b.txt" &
done
wait
cat results/branch_*.txt > "results/deep_bound2p${E}_raw.txt"
python3 merge.py > results/least_roots.txt
cat results/least_roots.txt
