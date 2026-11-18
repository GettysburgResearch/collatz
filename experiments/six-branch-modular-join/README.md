# An exact modular join for the least positive six-branch root

**Evidence level: exact finite enumeration.** Every row of [roots.jsonl](roots.jsonl) records the minimum ordinary source, its word and endpoint at the indicated depth. The positives surviving all depths form a subset of each finite level. Thus the last minimum is a lower bound for any such source. It decides neither existence nor escape.

## Why two independent lists suffice

With the notation of [L-0041](../../claims/lemmas/L-0041-six-branch-root-cap-recurrence.md), let M=Q^n and put

    c(i,d) = [−a_d Q^i P^(−i−1)] mod M.

The least residue of the ordinary source of a word is the sum of its n contributions modulo M. Indeed, telescoping Qx'=Px+a gives this congruence. Conversely the congruence reduced successively modulo Q, Q², ... forces each prescribed step to be integral. The digits are positive and less than Q, so the intermediate values are the ordinary ceiling iterates. All nonempty words have nonzero source residue because none of their first digits vanishes modulo Q.

Split the positions into two halves. The minimum is a circular nearest-pair problem on independent lists, of lengths 6^floor(n/2) and 6^ceil(n/2). One can sort full residues and walk the two lists. The implementation uses a 64-bit filter and reconstructs every candidate exactly, including wraparound, to reduce memory.

## The interval certificate

Write U=2^64. Replace each c by the integer key floor(U c/M). For a word, the exact scaled root U x/M is its summed key plus an error in [0,n), reduced modulo U. Let H be a trial upper bound in key units. If U x/M≤H then the modular key lies in [0,H] or [U−n,U). The C++ join enumerates this entire enclosing set. The Python driver recomputes exact residues and accepts a minimum only after its scaled value is at most H. That candidate proves nothing smaller was omitted. At depths 23 and 24 the minimum itself needs the upper wraparound interval.

The left list contains the negative of the summed left keys and the right list contains the summed right keys. Each right key z belongs to exactly one bucket [f,f+w). Its candidate mates q are visited in [f−H,f+w+n), interpreted circularly. Within the bucket the exact unsigned difference z−q is tested against both enclosing intervals. Word indices are retained for colliding keys. To generate the buckets without storing the entire half-list, the program sorts the first few positions of each half and visits translated ranges for all remaining positions. Subdivision into smaller bins inside a bucket only accelerates the range lookup.

## Replay and controls

From this directory, with a C++17 compiler and Python 3.8 or newer:

    g++ -O3 -std=c++17 -Wall -Wextra -fopenmp join.cpp -o /tmp/collatz-modjoin
    OMP_NUM_THREADS=2 python -B check.py /tmp/collatz-modjoin
    OMP_NUM_THREADS=2 python -B search.py /tmp/collatz-modjoin 16 17 18 19 20 21 22 23 24

The arithmetic requires no external Python package. The controls compare against physical source-cylinder lifting through depth 7 and brute-force every word for six adversarial circular joins. They exercise equality at both endpoints, word collisions, wraparound and bucket boundaries. Independent prior enumeration at commit `8fa408b843554b15f15ca1bc1c9ad6951fdfb4f7` gave depths 1 to 16. Every overlapping root and word at depths 2 through 16 agreed. The new finite calculation is separate from the proposed recognizable-set theorems.
