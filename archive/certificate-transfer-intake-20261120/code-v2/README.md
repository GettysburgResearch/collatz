# Code for "Collatz: 16k+1 => 32k+1 — proofs, results and the open part"

Every number in the write-up can be reproduced with these programs.
Python 3 (standard library only) and a C compiler with `__int128` (gcc or clang) are enough.

## Build

```
gcc -O2 -o merge_dfs merge_dfs.c
gcc -O2 -o dstat dstat.c
gcc -O2 -o landing landing.c -lm
gcc -O2 -o consec consec.c
```

## What each program does

| Program | Run | What it computes | Section |
| --- | --- | --- | --- |
| `chain.py` | `python3 chain.py exact 30` / `python3 chain.py mc 4000 20000` | The relation chain (a, e): exact merged share by depth; Monte Carlo to large depth | 4, 6, 10 |
| `merge_dfs.c` | `./merge_dfs 30 7` | Direct enumeration of residue classes of k mod 2^s; second argument lists merging classes up to that modulus exponent | 5, 10 |
| `verify.py` | `python3 verify.py` | Theorem 1 dictionary (k <= 60000); chain vs D(k) (k <= 6000); explicit merging classes | 3, 5, 8 |
| `research3.py` | `python3 research3.py` | Lemma 5.1, Proposition 5.2, Example 5.4; reference points with D = -2, -1, +1, +2; Theorem 5 | 5, 8 |
| `drift.py` | `python3 drift.py` | One-step inequality of Lemma 6.1 and the drift of ln|z| between departures | 6 |
| `consts.py` | `python3 consts.py` | Constants gamma, C_1, K, z_0; simulated E[W^(1/2)] and E[max(S,-K)] | 6 |
| `research2.py` | `python3 research2.py` | Theorem 4 on other pairs; n and n+1 for random n up to 3000 bits | 7 |
| `consec.c` | `./consec 27` | Share of n with B bits whose total stopping time equals that of n+1 | 7 |
| `research4.py` | `python3 research4.py 600` | Merging links along the powers of 3 | 7 |
| `dstat.c` | `./dstat 3000000` | Distribution of D(k) | 8, 9 |
| `landing.c` | `./landing 3000000` | Landing data: lead a, value Y*, types A and B | 9 |
| `problem2.py` | `python3 problem2.py` | Section 13: certificates for E, the certificate map in the merging case, the explicit family in the class 257, the link to 3^(27s-2) | 13 |
| `conv.c` | `gcc -O2 -o conv conv.c && ./conv 3000000` | Section 13: shares of merging / landed / still-running cases for x = 128m+1 | 13 |
| `conv_dfs.c` | `gcc -O2 -o conv_dfs conv_dfs.c && ./conv_dfs 28 9` | Section 13: merging residue classes inside x = 129, 257, 385 (mod 512) | 13 |

## Conventions

* `A(n) = n/2` for even n and `(3n+1)/2` for odd n (one halving per step).
* `X_0 = 9k+1` is `16k+1` after 4 halvings; `Y_0 = 27k+2` is `32k+1` after 5 halvings.
* State `(a, e)`: for `a >= 0` it means `Y = 3^a X + e`; for `a < 0` it means `X = 3^(-a) Y + e`.
* The start state is `(1, -1)`; `(0, 0)` means the two orbits have merged on a whole residue class.
* `D(k) = lambda(32k+1) - lambda(16k+1) + 1`, with `lambda(N) = 2*(triplings) - (halvings)` on the way to 1.

## Expected headline outputs

* `./merge_dfs 30 0` and `python3 chain.py exact 30` both end with merged share `0.2912563905` at depth 30.
* `python3 chain.py mc 4000 20000` gives an unmerged share near 0.35 at depth 1000 and 0.10 at depth 20000 (seeded).
* `./dstat 3000000`: D = 0 for 38.50%, D > 0 for 36.02%, D < 0 for 25.48% of k.
* `./landing 3000000`: no sign mismatch between a and D; a ranges over [-44, 27].
