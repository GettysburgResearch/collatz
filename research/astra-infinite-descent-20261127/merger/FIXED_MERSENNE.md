# The 192 supplied Mersenne parents

For $1\le k\le192$, put $m=12\cdot2^{18k}-1$ and $z=(2^{m+7}-271)/81$. Each of these **specific ordinary sources** meets a strictly smaller positive $Y\equiv17\bmod48$ for which $3Y$ reaches one using exactly three odd departures and at a shortcut clock at most $m$. The source $Y$ is canonical in the sense of PR206's predicate CanonicalReturn. Two sources meet if their ordinary trajectories share some value, allowing different clocks. This does not establish that each lower source $z$ itself reaches one. At $k=1$, PR206 separately verified its full convergence. [PR206 definitions and prior 183 cases](https://github.com/GettysburgResearch/collatz/blob/640bf7e511831a0ffc4f00462f12df81f8a8a619/research/clock-itineraries/ReturnDescentFixed.lean) · [PR206 first parent](https://github.com/GettysburgResearch/collatz/blob/640bf7e511831a0ffc4f00462f12df81f8a8a619/research/clock-itineraries/ReturnDescent.md)

PR206's table supplied the required canonical return for 183 of the first 192 positive parameters. The remaining nine now have direct counted meetings with earlier Mersenne peaks. The table gives $d=m-t$ and the prefix clock $h$ of the exact postpeak comparison. The final column is the prior row-specific upper budget added to $t$ in constructing $Y$.

| $k$ | $d$ | $h$ | Augmented grade | Earlier row charge |
|---:|---:|---:|---:|---:|
| 1 | 27 | 127896 | 64108 | 12 |
| 80 | 720 | 100726 | 50666 | 444 |
| 113 | 1017 | 70020 | 35045 | 380 |
| 130 | 1170 | 18284 | 9151 | 432 |
| 135 | 1243 | 14025 | 7029 | 373 |
| 138 | 1243 | 12359 | 6213 | 373 |
| 150 | 1350 | 19333 | 9526 | 438 |
| 159 | 1431 | 18823 | 9354 | 1009 |
| 180 | 1620 | 20599 | 10286 | 7 |

For each row let $b$ be the least residue of $3^t$ modulo $2^h$. Evaluate $T^h(3^d b-1)$ and $T^h(b-1)$ on the ordinary nonnegative representatives. The endpoint values agree exactly. The earlier arm has the displayed grade and the larger arm has that grade minus $d$. Writing $3^t=b+2^h u$, the lifts of the two endpoints acquire the same additive term $3^{\text{augmented grade}}u$. Thus the astronomical original peaks $3^m-1$ and $3^t-1$ actually meet after $h$ steps. Each $2^s-1$ reaches $3^s-1$ after its first $s$ odd steps, so this is also a meeting of the two positive Mersenne sources. All original exponents satisfy $m\equiv11\bmod162$. The displayed charges are at most $d$, allowing PR206's priced representative theorem to furnish the claimed strictly cheaper canonical $Y$. This uses neither hypothetical leastness nor an empirical projection between different source parameters. [Prior ordinary lift and price consumer](https://github.com/GettysburgResearch/collatz/blob/640bf7e511831a0ffc4f00462f12df81f8a8a619/research/clock-itineraries/ReturnDescentFixed.lean)

The search computed one modular power per supplied $k$ and search horizon. It tracked a common upper representative and many lower exponents in 32-step blocks. A separate scalar Python program recomputes each $b$ at its own $h$ using built-in modular exponentiation, performs every individual ordinary step on both representatives, checks the first simultaneous equality of endpoints and augmented grades there, and reads the price directly from the pinned 81-row Lean table. These comparisons concern one finite preassigned list. A proof for every positive $k$ remains open.


The kernel theorem Collatz.Itinerary.ReturnDescent.Supplied.all_192 proves the displayed CanonicalReturn for every integer $k$ between one and 192 inclusive. Lean 4.34.1 reports only propext and Quot.sound. The six exact PR206 dependency modules and their upstream Git blob hashes appear in the source ledger. Strict scratch builds of TernaryItinerary, BasinTransport, TowerFrontierAffine, ReturnDescent, ReturnDescentRows, ReturnDescentFixed, and the new module took respectively 10.713, 0.646, 1.165, 3.855, 36.499, 109.521, and 37.836 seconds on the initial serial run. [Kernel theorem](FixedMersenneRows.lean) · [Pinned dependency ledger](../imports/pr206/SOURCES.json) · [Independent scalar verifier](check_fixed_mersenne.py)

A separate written deduction retains the price margin in the actual witnesses. If the row-specific charge is $c$, the prior construction gives $H\le m-d+c$, $Y<2^H$, and $z>2^m$, so $2^{d-c}Y<z$. In the nine new rows, the bit savings $d-c$ are 15, 276, 637, 738, 870, 870, 912, 422, and 1613, in table order. Evaluating that same price on the 183 pinned rows gives savings of at least 15 on all 192, at least 40 on 185 rows, and at least 200 on 134 rows. The uniform stronger margin is a deduction from the actual priced construction and row arithmetic. The all_192 kernel statement itself retains the original CanonicalReturn predicate.
