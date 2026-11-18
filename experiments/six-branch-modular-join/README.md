# An exact modular join for the least positive six-branch root

**Evidence level: exact finite enumeration.** Every row of [roots.jsonl](roots.jsonl) records the minimum ordinary source, its word and endpoint at the indicated depth. The positives surviving all depths form a subset of each finite level. Thus the last minimum is a lower bound for any such source. It decides neither existence nor escape.

The completed partitioned run covers depths 28, 29 and 30. All 4,096 right-bucket partitions completed for each filter. The prefix filter emitted 2,737,829 pairs and gave 42 in-cap one-digit extensions. The fused two-digit filter emitted exactly 9,000 pairs, of which two gave in-cap physical extensions. A separate forward-affine verifier reproduced the minimum and extension count in every individual partition. Restoring the compact ledgers in new scratch directories reproduced all three final records byte-for-byte. The respective least sources have 138, 143 and 149 decimal digits. [Depth 28/29 ledger](receipts-28-29.jsonl) · [Depth 30 ledger](receipts-30.jsonl)

## Why two independent lists suffice

With the notation of [L-0041](../../claims/lemmas/L-0041-six-branch-root-cap-recurrence.md), let M=Q^n and put

    c(i,d) = [−a_d Q^i P^(−i−1)] mod M.

The least residue of the ordinary source of a word is the sum of its n contributions modulo M. Indeed, telescoping Qx'=Px+a gives this congruence. Conversely the congruence reduced successively modulo Q, Q², ... forces each prescribed step to be integral. The digits are positive and less than Q, so the intermediate values are the ordinary ceiling iterates. All nonempty words have nonzero source residue because none of their first digits vanishes modulo Q.

Split the positions into two halves. The minimum is a circular nearest-pair problem on independent lists, of lengths 6^floor(n/2) and 6^ceil(n/2). One can sort full residues and walk the two lists. The implementation uses a 64-bit filter and reconstructs every candidate exactly, including wraparound, to reduce memory.

## The interval certificate

Write U=2^64. Replace each c by the integer key floor(U c/M). For a word, the exact scaled root U x/M is its summed key plus an error in [0,n), reduced modulo U. Let H be a trial upper bound in key units. If U x/M≤H then the modular key lies in [0,H] or [U−n,U). The C++ join enumerates this entire enclosing set. The Python driver recomputes exact residues and accepts a minimum only after its scaled value is at most H. That candidate proves nothing smaller was omitted. At depths 23 and 24 the minimum itself needs the upper wraparound interval.

The left list contains the negative of the summed left keys and the right list contains the summed right keys. Each right key z belongs to exactly one bucket [f,f+w). Its candidate mates q are visited in [f−H,f+w+n), interpreted circularly. Within the bucket the exact unsigned difference z−q is tested against both enclosing intervals. Word indices are retained for colliding keys. To generate the buckets without storing the entire half-list, the program sorts the first few positions of each half and sweeps translated ranges for the remaining positions. Each worker owns consecutive buckets and retains a cyclic cursor per translation. It advances that cursor by the nonoverlapping bucket width before checking the extra boundary interval. The local bin count follows the expected right-side occupancy. Neither the sweep nor the bins discard repeated keys.

## Replay and controls

From this directory, with a C++17 compiler and Python 3.8 or newer:

    g++ -O3 -std=c++17 -Wall -Wextra -fopenmp join.cpp -o /tmp/collatz-modjoin
    OMP_NUM_THREADS=2 python -B check.py /tmp/collatz-modjoin
    OMP_NUM_THREADS=2 python -B search.py /tmp/collatz-modjoin 16 17 18 19 20 21 22 23 24
    OMP_NUM_THREADS=4 python -B search.py /tmp/collatz-modjoin --base-length 10 25 26 27

The arithmetic requires no external Python package. The controls compare against physical source-cylinder lifting through depth 7 and brute-force every word for six adversarial circular joins. They exercise equality at both endpoints, word collisions, wraparound and bucket boundaries. Independent prior enumeration at commit `8fa408b843554b15f15ca1bc1c9ad6951fdfb4f7` gave depths 1 to 16. Every overlapping root and word at depths 2 through 16 agreed. The new finite calculation is separate from the proposed recognizable-set theorems.

## Resumable prefix and two-digit extension search

The depth-28 join uses 4,096 disjoint intervals of right-key buckets. Each worker writes its range, every candidate pair, and a terminal count to a temporary file; it closes and renames the file only after finishing every bucket in that range. The independent Python pass checks the range, footer, bucket ownership, modular filters, exact root and physical itinerary. Each compact ledger line records its partition index, candidate count, in-cap extension count, best prefix witness, best extension witness, and SHA-256 of the complete raw partition. A witness contains its exact root, the two base-six half-word indices, and its appended digits. The header binds the input and search parameters. A partial ledger explicitly says `"complete": false`; its completed parts can be reused after a restart. Full minima require every range and at least one legal in-cap witness at each certified depth. A digest authenticates the bytes against a replay; finite completeness rests on the join and the disjoint bucket cover.

The 28/29 calculation uses depth-28 prefix cap $H=8192$ in $2^{64}$ key units. Every candidate under the corresponding physical cap is smaller than $M=Q^{28}$. A depth-29 or depth-30 source below such a cap must therefore equal its own least positive depth-28 residue. Reconstruct the prefix sum exactly modulo $MQ^e$, where $e$ is the number of appended digits. Every contribution from the final $e$ positions is a multiple of $M$. The high quotient of the reconstructed sum must cancel one of the $6^e$ suffix quotients modulo $Q^e$. This tests all extensions without enumerating a half-list of length $6^{15}$.

For two appended digits the primary cap is widened to $H=100000000$. The fused mode also uses the per-position key $\lfloor2^{32} c_{30}/Q^{30}\rfloor$. Any physical source under the wider prefix cap has auxiliary scaled value at most $2^{32}H/(2^{64}Q^2)<1$. Its full summed auxiliary key, including suffix, lies in the circular range $[-30,1]$ modulo $2^{32}$. The C++ pass enumerates all 36 suffix sums when building that filter. Its high-16-bit test only accelerates exact membership lookup. The ensuing exact reconstruction decides which candidates lie under the physical cap. The narrower prefix output is still collected independently. Either job can have complete coverage before the other.

From this directory, using separate scratch directories outside the checkout:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -fopenmp join.cpp -o /tmp/collatz-modjoin
OMP_NUM_THREADS=2 python -B check.py /tmp/collatz-modjoin
OMP_NUM_THREADS=2 python -B check_partition.py /tmp/collatz-modjoin
OMP_NUM_THREADS=4 python -B partition.py run /tmp/collatz-prefix --binary /tmp/collatz-modjoin --wide 100000000 --suffix-directory /tmp/collatz-30
python -B partition.py checkpoint /tmp/collatz-prefix --archive receipts-28-29.jsonl
python -B partition.py checkpoint /tmp/collatz-prefix --wide 100000000 --suffix-directory /tmp/collatz-30 --archive receipts-30.jsonl
python -B partition.py finish /tmp/collatz-prefix
python -B partition.py finish /tmp/collatz-prefix --wide 100000000 --suffix-directory /tmp/collatz-30
```

For a resumed run use `restore` in place of `checkpoint` with the ledger and matching job options before running the search. Existing verified ranges are skipped, while incomplete temporary files are ignored. For independent full replay, start with empty scratch directories and do not restore any ledger. The controls check both filters against brute force, independent physical minima, interruption on different partitions, checkpoint restoration and refusal to certify missing coverage. An additional verifier reconstructs the ordinary forward affine offset $A_w$ from the raw word indices, derives $x=-P^{-28}A_w\bmod Q^{28}$ and $y=(P^{28}x+A_w)/Q^{28}$, and tests the unique legal next digits directly, independently of the search's high-quotient suffix calculation. Run it on either matching raw directory and ledger:

```sh
python -B verify_ledgers.py /tmp/collatz-prefix receipts-28-29.jsonl
python -B verify_ledgers.py /tmp/collatz-30 receipts-30.jsonl
```
