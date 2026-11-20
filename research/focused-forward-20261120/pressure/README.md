# Ordinary root potential: exact finite depth and the unresolved limit

The [proof](PROOF.md) gives an exact finite-height reduction for the all-word
inverse potential at `1`, its finite transfer to terminating sources, a
stopping-time consequence of hypothetical root finiteness, and a necessary
local oscillation of any finite all-action certificate. **It does not prove
Collatz or finiteness of the infinite-depth root potential.**

The inverse letters are `I_g(z)=(2^g z-1)/3`, with positive odd units as all
states and every legal positive exponent allowed. A word with `k` letters
and exponent sum `A` has score `8k-5A`. Let `W_N(1)` maximize this score and
zero over words of length at most `N`.

## Mathematical results

| Claim | Exact statement and boundary |
|---|---|
| H1 | `W_N(1)` is the maximum first-hit score among positive odd units at most `H_N=floor fifth-root(floor((256^N-1)/(2*243^N)))` that hit `1` by odd time `N`, together with zero. Every exponent is covered; sources outside the bound cannot have positive score at this horizon. |
| H2 | `W_L(1)=0` transfers to `W_(L-h)(n)<=5A-8h` along an actual first-hit path from `n` to `1` of odd length `h` and exponent sum `A`. The available horizon decreases by `h`. |
| H3 | `W(1)<=B` forces a uniform logarithmic first-hit bound on its terminating basin, with leading coefficient `5/(8-5 log_2(3))`. This makes explicit the extra quantitative obligation in root finiteness. |
| O1-local | Any finite nonnegative all-action potential has downward oscillations of order `log X` even between sources whose ratio is at most `16`: the limsup coefficient is at least `8/log_2(3)-5`. This excludes regular or nearly monotone certificates, not arbitrary irregular ones. |
| O2 | The same local oscillation satisfies `D_16(X)>=beta_12 log_2 X-O(1)` at every sufficiently large height, with `beta_12≈0.00831750>1/125`. This is an all-scale lower bound; O1-local retains the larger limsup coefficient. |

The starting potential is source-pinned to PR149 at
`92c0129e794dde3ec55ceec470a12d51ba3f7e2f`; its exact source paths and
logical boundary are in the proof. None of the new arguments needs an
external analytic theorem.

## Completed finite computations

| Horizon `N` | Exact cutoff `H_N` | Odd unit candidates | `W_N(1)` | Maximum first-hit odd depth |
|---:|---:|---:|---:|---:|
| 1,000 | 29,277 | 9,759 | 0 | 113 in the C++ replay |
| 1,500 | 5,369,100 | 1,789,700 | 0 | 218 |
| 2,000 | 984,624,609 | 328,208,203 | 0 | 364 |

All candidates in these three reported intervals reached `1` within their
respective horizons. The maximum nonroot first-hit score in each interval
was `-12`, at `5`. The theorem therefore proves `W_N(1)=0` at each stated
horizon, even though there are infinitely many possible inverse exponents.
This is a finite certificate of a quantitative cost bound, not a claimed
improvement to the largest verified Collatz starting-value range.

The saved receipts are [the independent Python replay at depth 1,000](height-1000-independent-python.json),
[depth 1,500](height-1500.json), and [depth 2,000](height-2000.json).
The depth-2,000 replay computed `553,488,373` actual odd edges and reused
exact cached tails. Its largest computed odd state was
`471,412,148,906,647,493`; arithmetic was checked before each multiplication.

## Reproduction and independent controls

Run these commands from the repository root. The C++ implementation uses
the GCC/Clang `unsigned __int128` extension. Its maximum cache allocation
at horizon `2,000` is about `3.94 GB`; use the smaller independent replay
for a quick check.

```sh
mkdir -p /tmp/collatz-pressure
g++ -std=c++17 -O3 -Wall -Wextra -Wconversion research/focused-forward-20261120/pressure/height_replay.cpp -o /tmp/collatz-pressure/height_replay
python -X utf8 -B research/focused-forward-20261120/pressure/height_certificate.py --horizon 1000 --python --controls
python -X utf8 -B research/focused-forward-20261120/pressure/check_review.py --executable /tmp/collatz-pressure/height_replay
python -X utf8 -B research/focused-forward-20261120/pressure/height_certificate.py --horizon 1500 --executable /tmp/collatz-pressure/height_replay
python -X utf8 -B research/focused-forward-20261120/pressure/height_certificate.py --horizon 2000 --executable /tmp/collatz-pressure/height_replay
```

`height_certificate.py` calculates the cutoff with arbitrary integers,
checks both neighboring fifth powers, and invokes either uncached Python
or memoized C++ trajectories. Its independent inverse-tree controls agree
at horizons `0`, `1`, `10`, `20`, `30`, and `40`.

`check_review.py` contains a separate direct implementation, including a
different valuation loop. It compares nine result fields against the C++
implementation at `54` cutoff/horizon combinations, including empty
domains, zero horizon, sources that fail to hit within the horizon, and
paths that encounter cached suffixes. The [review receipt](review-check.json)
records `3,420` candidate cases. It also replays `10,100` legal inverse-one
letters and `199` local-ratio comparisons used in O1-local. These finite
controls supplement the proofs; they do not establish an asymptotic claim.
The positive coefficient in O2 is checked separately by exact rational
arithmetic using `3^41<2^65`.

## Independent audit and exact remaining step

The independent mathematical and implementation reconstruction is recorded
in [AUDIT.md](AUDIT.md), with source digests in [audit-snapshot.json](audit-snapshot.json).
The reviewer reran both implementations at horizon `1,000`, matched the
compiled binary hash to the larger saved receipts, and ran the separate
`54`-case comparison. The reviewer did not repeat the large horizon-`2,000`
computation; that receipt records the originating run.

The root condition still asks for one uniform bound on

\[
\sup_{m\text{ a terminating positive odd unit}}
\bigl(8h(m)-5A_*(m)\bigr).
\]

H1 gives exact finite maxima while its candidate height grows exponentially
with the horizon. None of the checked finite maxima bounds the remaining
ones. O1-local imposes irregularity on a proposed certificate, but supplies
no such certificate. Extending the zero scores from every checked horizon
to all horizons is the first unsupported inference. Even a proof of root
finiteness would still have to be combined with an argument covering any
hypothetical component outside the basin of `1`.
