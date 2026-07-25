#!/bin/sh
# =====================================================================
# X-9903 -- verified floor sweep for the Collatz map
# Agent: fable-02-p10
#
# Reproduces every number recorded in README.md and results/.
#
#   ./run.sh                 full run  (F = 10^12, K = 22, 4 threads)
#   ./run.sh 1000000000 20   smaller F / different sieve modulus
#
# Stages 1-6 are the correctness gates and take about a minute in total.
# Stage 7 is the main sweep; its cost scales linearly in F (see README,
# "Calibration and choice of F").  Stage 6 (the total-stopping-time DP)
# allocates 2 bytes per integer up to 10^9, i.e. 2 GB of RAM.
# =====================================================================
set -e

F=${1:-1000000000000}
K=${2:-22}
NT=${3:-4}
TSTL=${4:-1000000000}

R=results
mkdir -p "$R"

# ---- 0. environment ---------------------------------------------------
{
  echo "X-9903 environment record"
  echo "date (UTC)      : $(date -u '+%Y-%m-%d %H:%M:%S')"
  echo "uname -a        : $(uname -a)"
  echo "os              : $(grep -m1 PRETTY_NAME /etc/os-release | cut -d'"' -f2)"
  echo "cpu             : $(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2- | sed 's/^ //')"
  echo "cores (nproc)   : $(nproc)"
  echo "memory total    : $(grep -m1 MemTotal /proc/meminfo | awk '{print $2" "$3}')"
  echo "compiler        : $(gcc --version | head -1)"
  echo "python          : $(python3 --version 2>&1)"
  echo "parameters      : F=$F K=$K threads=$NT tst_L=$TSTL"
} > "$R/environment.txt"
cat "$R/environment.txt"

# ---- 1. build ---------------------------------------------------------
echo
echo "=== 1. build ==="
set -x
gcc -O2 -march=native -pthread -Wall -Wextra -o sweep sweep.c
set +x

# ---- 2. self tests ----------------------------------------------------
echo
echo "=== 2. self tests ==="
./sweep selftest | tee "$R/selftest.txt"

# ---- 3. sieve table ---------------------------------------------------
echo
echo "=== 3. sieve statistics ==="
./sweep sieve 1 2 3 4 5 6 7 8 10 12 14 16 18 20 22 24 | tee "$R/sieve_table.txt"

# ---- 4. cross-check A: three independent stopping-time implementations -
echo
echo "=== 4. cross-check A: naive vs DP vs Python bigint ==="
{
  echo "--- Python 3, arbitrary-precision ints, no memoisation, no shortcut (n <= 10^5)"
  python3 naive_ref.py 100000
  echo
  echo "--- C, unsigned __int128, no memoisation, no shortcut (n <= 10^5)"
  ./sweep naive 100000 | tail -6
  echo
  echo "--- C, unsigned __int128, no memoisation, no shortcut (n <= 10^6)"
  ./sweep naive 1000000 | tail -6
  echo
  echo "--- C, exact descent DP with uint64 fast path (n <= 10^6)"
  ./sweep tst 1000000 | tail -7
} | tee "$R/crosscheck_stopping_times.txt"

# ---- 5. cross-check B: sieved sweep vs unsieved sweep -----------------
echo
echo "=== 5. cross-check B: sieved vs unsieved, and sieve-modulus independence ==="
{
  echo "--- unsieved (every n iterated), F = 10^6"
  ./sweep verifyall 1000000 | tail -7
  echo
  echo "--- unsieved (every n iterated), F = 10^7"
  ./sweep verifyall 10000000 | tail -7
  for k in 8 12 16 20 22; do
    echo
    echo "--- sieved, F = 10^7, K = $k"
    ./sweep verify 10000000 $k $NT | grep -E 'total n iterated|max descent|max C-orbit'
  done
} | tee "$R/crosscheck_sieve.txt"

# ---- 6. exact total stopping times up to TSTL (needs 2*TSTL bytes) ----
echo
echo "=== 6. exact total C-stopping times up to $TSTL ==="
./sweep tst "$TSTL" | tee "$R/delay_records.txt"

# ---- 7. MAIN SWEEP ----------------------------------------------------
echo
echo "=== 7. main sweep: F = $F, K = $K, threads = $NT ==="
./sweep verify "$F" "$K" "$NT" 850 0 | tee "$R/digest.txt"

# ---- 8. record-holder spot checks ------------------------------------
echo
echo "=== 8. record-holder spot checks (independently re-runnable) ==="
{
  for n in 27 703 837799 704511 6631675 8088063 63728127 80049391 319804831 \
           670617279 8528817511 12235060455 77566362559; do
    ./sweep check $n
  done
} | tee "$R/record_holders.txt"

echo
echo "X-9903 run complete."
