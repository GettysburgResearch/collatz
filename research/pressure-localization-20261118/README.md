# Source localization for the finite-clock diagonal moment

**PROPOSED.** The claims below concern the ordinary positive odd map
`U(x)=(3x+1)/2^v₂(3x+1)`. They continue PR 144, head
`df756794e1d8de5cabff148ef433df505e3b68b4`, specifically D1 and D4
in [the parent proof](https://github.com/GettysburgResearch/collatz/blob/df756794e1d8de5cabff148ef433df505e3b68b4/research/pressure-diagonal-20261031/PROOF.md) and T3–T4 in
[its trace](https://github.com/GettysburgResearch/collatz/blob/df756794e1d8de5cabff148ef433df505e3b68b4/research/pressure-diagonal-20261031/TRACE.md). All visits to positive
cycles are retained. The global moment bound and the conjecture remain open.

For odd source x and q odd steps write t=U^q(x), A for the sum of the q
valuations and J=3^q/2^A. The exact positive affine formula t≥Jx gives

    d_q(x) = J^4/t² ≤ J²/x²,          D_q = ∑_x d_q(x).

## 1. All nonminimal representatives have exponentially small total weight

A valuation word (a₁,…,a_q), all aᵢ≥1, of total length A occurs on exactly
one odd class modulo 2^(A+1). Indeed, its raw shortcut parity prefix consists
of q ones separated and followed by their prescribed zero runs, followed by
a terminal one. Every length-m parity word specifies one residue modulo 2^m:
at depth k the two lifts of a legal residue have T^k values differing by an
odd power of 3, so choose opposite next bits.

Let r be the positive representative below 2^(A+1). The sum of d_q over
the other sources r+ℓ2^(A+1), ℓ≥1, is at most

    (π²/24) 9^q 16^(−A).

There are binom(A−1,q−1) words of total A. Summing the negative-binomial
series gives, for q≥1,

    0 ≤ D_q − ∑_{valuation words} d_q(r) ≤ (π²/24)(3/5)^q.          (1)

Thus even the sum of these errors over *all* odd clocks is finite. This
removes the nonminimal lifts from the parent's polynomial and its Cesàro
moment targets. The canonical representatives still form an infinite sum
at each q. Controlling their moment in q is the unsupported step.

## 2. A finite source bank with Fibonacci cardinality

For x≥3 let k=floor(log₂ x) and let p be its number of odd raw steps among
its first k shortcut steps. This associates to x its parity word of length
k, starting odd. Every such word is associated to exactly one ordinary
source in [2^k,2^(k+1)), by the two-lift argument above. Charge one per
odd bit and two per even bit, giving total cost w=2k−p. Include x=1
separately at cost zero. If F₀=0, F₁=1 denote the Fibonacci numbers,
there are F_w sources at cost w≥1, since after the compulsory first odd
bit the remaining cost is any composition into ones and twos. The number
of sources at cost at most L, including 1, is F_(L+2).

For q≥p the q-th odd clock occurs at raw time A≥k. At least k−p even
steps have occurred by then. Thus A≥q+k−p, giving the uniform bound

    d_q(x) ≤ (9/4)^q 4^(−w).                                         (2)

If q<p then A<k, so x≥2^(A+1) is a nonminimal representative in (1).
This gives one bound for all omitted sources of this type. An alternative
bound that can be smaller at very large L uses k≥k₀=max(q+1,⌊(L+3)/2⌋).
In each shell, average the completed-prefix value J² over its 2^(k−1)
odd residues. Each q-word of total A<k has frequency 2^(−A) among
these residues, with the initial odd bit fixed. Extending the sum to all
words gives the upper average (∑_(a≥1) 9·8^(−a))^q=(9/7)^q.
Using x^(−2)≤4^(−k) and summing shells k≥k₀ bounds the contribution by
(9/7)^q 2^(−k₀).

Let B(q,L) be the sum of d_q over the finite cost bank. Summing (2) and
using π²/24<1/2 in (1) gives the rational enclosure

    0 ≤ D_q − B(q,L)
      ≤ (9/4)^q (4F_(L+1)+F_L)/(11·4^L)
          + min((3/5)^q/2, (9/7)^q 2^(−k₀)).                         (3)

The Fibonacci factor is the exact tail of ∑ F_w/4^w. The q<p and q≥p
parts above have disjoint source populations.

For fixed absolute error ε>0, the second term is ≤ε/2 for all sufficiently
large q. Write φ=(1+√5)/2. Taking
L=q log(9/4)/log(4/φ)+O_ε(1) bounds the first term by ε/2. Enumerating
the bank and computing each prefix requires O_ε(q·b^q) odd steps, with

    b=φ^[log(9/4)/log(4/φ)] < 1.540.

This counts arithmetic operations. Integers have O(q+L) bits: the product
formula gives 2^A ≤4^q x, and each odd image y satisfies U(y)+1≤3(y+1)/2.
O(q+L+log(1/ε)) fractional bits suffice to bound total rounding error.
The earlier two-table method enumerates 3^q ternary residues and gives
several traces together. Formula (3) addresses D_q alone.

## 3. Finite ordinary trace

A run with L=30 used all 2,178,309 sources in the cost bank and rounded
each contribution down in units of 2^(−96). For each clock the upper
endpoint adds one unit per source and the outward-rounded right side of
(3). The displayed intervals are rounded outward again.

| Odd clock q | Lower bound for D_q | Upper bound for D_q |
|---:|---:|---:|
| 12 | 0.23595 | 0.23627 |
| 16 | 0.68951 | 0.68966 |
| 20 | 0.59765 | 0.59768 |
| 24 | 2.44922 | 2.44937 |
| 28 | 11.86498 | 11.86855 |
| 30 | 12.84700 | 12.86503 |
| 32 | 14.38440 | 14.47566 |
| 34 | 0.50237 | 0.96434 |
| 36 | 0.06149 | 2.40016 |

The q=12 enclosure overlaps PR 144's tighter interval. The change between
32 and 34 includes the complete source measure. At q=32 the single source
27 contributes more than 13. Its finite excursion accounts for most of
that clock's moment.

The verifier independently inverts the affine congruence at each new bit
and replays the ordinary raw shortcut map. It also checks exhaustive shell
membership for budgets 1 through 12. Both programs are author-side code.
From the repository root run

```sh
python -B experiments/pressure-localization-20261118/trace.py --budget 30 --clocks 12 16 20 24 28 30 32 34 36 > /tmp/pressure-trace.json
python -B experiments/pressure-localization-20261118/check.py /tmp/pressure-trace.json
```

[Exact integer endpoints](../../reports/pressure-localization-20261118/trace.json).

[Signed logarithmic pressure](LOGARITHMIC.md) gives a power-moment-free
dissipation inequality, a division-count target and polynomial-cost
finite-clock enclosures.

[Coefficient occupation](OCCUPATION.md) bounds the all-time weight of
low multipliers on simple paths and gives a separate cycle-retaining
telescope.
