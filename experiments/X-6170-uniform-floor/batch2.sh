#!/bin/sh
# wait for batch 1 (up to 7.2e11) to drain, then cover [7.2e11+1, 1.1e12]
while pgrep -x fastscan > /dev/null; do sleep 20; done
LO=720000000001
HI=1100000000000
W=$(( (HI - LO + 1) / 4 ))
for s in 0 1 2 3; do
  A=$(( LO + s * W ))
  B=$(( LO + (s+1) * W - 1 ))
  if [ $s -eq 3 ]; then B=$HI; fi
  ./fastscan $B $A > results/fastscan-b2-shard$s.txt 2>&1 &
done
wait
echo BATCH2-DONE
