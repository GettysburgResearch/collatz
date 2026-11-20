# The one-sided problem already contains an unbounded target problem at known depth two

**PROPOSED elementary theorem; not Collatz convergence.** All integers below are positive and ordinary.

**Source refresh:** while this independent reconstruction was being reviewed,
PR146 advanced to `e238c63a5d57f96bb063b7472498d1977df51951`.
Its `WITNESS_TRANSFER.md` and `BASIN_PHASE.md` also contain the depth-two
classification and Mersenne reduction, and its `BOUNDED_RANK_TRANSFER.md`
gives stronger general restrictions on lifted certificates. The family and
rank-only obstruction below are therefore not presented as new relative to
that refreshed source. The explicit complete-orbit separation and independent
replays are retained. See [the precise comparison](LATEST_146_COMPARISON.md).

Define

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n\text{ odd}).
\]

The source is PR146 at `6863d298187af8b2619efbf78cc4b0aa8e627393`,
`research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`. Its one-sided criterion says that full Collatz follows from

\[
16k+1\in C\ \Longrightarrow\ 32k+1\in C\qquad(k\ge0),
\tag{D0}
\]

where C is the actual basin of 1. The same source identifies the upper arm with the component of `3(16k+1)`. We do not reprove or strengthen the global equivalence here.

The attempted new architecture was to induct on the finite terminating certificate supplied by the good arm. The theorem below precisely limits a uniform implementation of that architecture: even when the good arm has first hitting depth **two in the accelerated odd map**, the necessary target clock is unbounded. These are explicit convergent good arms, unlike finite positive shadows whose full behavior is not known.

## D2-1. Complete classification of the depth-two good arms in the required class

For m≥1 put

\[
B=64^m,\qquad k_m=\frac{B-1}{9},\qquad
n_m=16k_m+1=\frac{16B-7}{9},\qquad
z_m=32k_m+1=2n_m-1=\frac{32B-23}{9}.
\]

Then k_m is a positive integer, n_m is 1 modulo 16, and

\[
U(n_m)=\frac{4B-1}{3},\qquad U^2(n_m)=1.
\tag{D1}
\]

The division exponents are exactly 2 and 6m+2. Consequently the first ordinary shortcut hitting time is exactly 6m+4, while the first odd-event hitting depth is exactly two.

Conversely these are **all** positive n congruent to 1 modulo 16 whose first odd-event hitting depth is two. Indeed v₂(3n+1)=2, so u=(3n+1)/4 is odd. If U(u)=1, then 3u+1=2^b and

\[
n=\frac{2^{b+2}-7}{9}.
\]

The powers of 2 modulo 9 have exact period six, and integrality requires b≡2 modulo 6. The choice b=2 gives the base n=1, whose first hitting depth is zero; every later choice is b=6m+2 with m≥1. Formula (D1) also shows u>1 and n>1 for those m, so the first depth really is two.

## D2-2. The residual target is an exponential Mersenne family

The first four parities of z_m are odd, even, odd, even, and

\[
\boxed{T^4(z_m)=2^{6m+1}-1.}
\tag{D2}
\]

For completeness, writing the intermediate values in B gives

\[
z_m\longmapsto\frac{16B-10}{3}
\longmapsto\frac{8B-5}{3}
\longmapsto4B-2\longmapsto2B-1.
\]

All integrality and parity claims follow from B=64^m. Thus the restriction of (D0) to its entire first-depth-two stratum is **exactly** the assertion

\[
2^{6m+1}-1\in C\qquad(m\ge1).
\tag{D3}
\]

This packet does not prove (D3), and does not assert that (D3) alone implies full Collatz. It shows why the known finite certificate on the first arm does not itself close the one-sided criterion.

## D2-3. Separation from the complete known orbit

The entire forward orbit of n_m is contained below

\[
H_m=\frac{8B-2}{3}.
\]

In fact its first four values are

\[
\frac{16B-7}{9},\quad \frac{8B-2}{3},\quad
\frac{4B-1}{3},\quad 2B,
\]

after which it halves to 1 and repeats `1,2`. The second listed value is the maximum for B≥64.

The tripled arm has the exact beginning

\[
3n_m=\frac{16B-7}{3}\longmapsto 8B-3
\longmapsto12B-4\longmapsto6B-2\longmapsto3B-1.
\]

After that, for 0≤ℓ≤6m,

\[
T^{4+\ell}(3n_m)=3^{\ell+1}2^{6m-\ell}-1.
\tag{D4}
\]

For every ℓ<6m the displayed input is odd, proving legality of the formula. These values increase with ℓ. The whole tripled prefix therefore lies at least at 3B−1, and

\[
3B-1-H_m=\frac{B-1}{3}>0.
\]

We obtain the stronger independently clocked statement

\[
\boxed{
T^i(n_m)\ne T^j(3n_m)
\quad\text{for every }i\ge0\text{ and }0\le j\le6m+4.
}
\tag{D5}
\]

No search in the known arm, even at an arbitrarily large clock, can meet this target prefix. No unknown orbit fact was used: the whole known arm was explicitly enumerated in closed form.

## D2-4. The obstruction remains in odd-event time

This is not just delay caused by halving a large even number. The first two odd steps of the tripled arm are

\[
U(3n_m)=8B-3,\qquad U^2(3n_m)=3B-1,
\]

with division exponents 1 and 3. For 0≤ℓ<6m, the next odd states are

\[
U^{2+\ell}(3n_m)=3^{\ell+1}2^{6m-\ell}-1.
\]

The first 6m−1 transitions in this displayed stretch have division exponent one. At its last state, since 6m+1 is odd,

\[
v_2(3^{6m+1}-1)=1,
\qquad
U^{6m+2}(3n_m)=\frac{3^{6m+1}-1}{2}>1.
\tag{D6}
\]

Every odd state through this clock is greater than one. If the tripled arm converges, its first odd-event hitting depth is at least 6m+3; otherwise that depth is infinite.

Hence **no finite function of the good arm's odd-event first hitting depth alone can bound a universal target convergence or merger clock for the one-sided tripling problem**, even restricted to n≡1 modulo 16. The good depth is always two while the verified target delay tends to infinity.

This does not exclude a compiler with height-dependent work, an unbounded recursive proof, a different well-founded rank, or an argument proving all the exponential targets at once. The missing implication is still actual target convergence for every fixed m, not an existence claim for a different m at each finite deadline.

## An alternative attempted bridge, retained as an open target

PR146's `STABILIZED_CORE_DESCENT.md` proves that eventual success of its still thinner `1 mod4096` family gives finitely many components. In that argument the stabilized label F obeys multiplication invariance by 2 and 3 and the ordinary odd-step law on odd ternary units. Beyond some fixed exponent J it also obeys

\[
F(3^j w+1)=F(w)\qquad(w\text{ positive odd},\ j\ge J).
\tag{D7}
\]

One possible strengthening would prove that these laws force F constant **uniformly for every finite J**. The source's finite affine descent uses exponents 6 through 10, so simply increasing the exceptional cutoff does not establish that conclusion for the finitely many small inputs. Algebraic operations on rationals cannot discard the odd-input and integrality domains of (D7). Our exploration did not derive the low-exponent laws from (D7), and no uniform-in-J rigidity theorem is claimed here.

## Exact replay

`check_directed_depth.py` independently iterates the shortcut and odd maps, checks the complete convergent source orbit, reconstructs the Mersenne reduction and all target prefixes, and rejects damaged witness fields. Its finite replay is evidence for the formulas and code; the universal statements are proved above. The checker uses explicit failures and remains active under optimized Python.
