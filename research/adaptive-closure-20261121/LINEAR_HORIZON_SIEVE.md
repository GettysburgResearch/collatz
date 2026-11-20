# Extending the least-failure sieve to a linear parity horizon

**PROPOSED elementary extension of a source-qualified reduction. Full
Collatz closure remains OPEN.** The new statement is an exact sufficient
test on each ordinary source. No improved universal counting exponent is
claimed.

Source: PR146 at `fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`. Its least-failure
height and constructive smaller-comparison reduction use PR163 at
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
`research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md`.
The exact 71-path cover is an imported source-pinned result here, not
reproved by this note's finite arithmetic checker.

## LHS1. An affine-remainder bound at the first coefficient crossing

For the shortcut Collatz map T, set

\[
n_i=T^i(n),\qquad b_i=\#\{0\le j<i:n_j\text{ odd}\},\qquad
c_i=3^{b_i}/2^i.
\]

Fix a positive integer B. Suppose i is the first positive clock with
`c_i<2^(-B)`. Then

\[
\boxed{n_i<2^{-B}n+b_i/3.}                              \tag{L1}
\]

Indeed direct composition gives

\[
n_i=c_i n+\sum_{\substack{0\le j<i\\n_j\text{ odd}}}
                  \frac{c_i}{2c_{j+1}}
    =c_i n+\sum_{\substack{0\le j<i\\n_j\text{ odd}}}
                  \frac{c_i}{3c_j}.
\]

For every earlier j, including j=0, `c_j>=2^(-B)`. Each displayed
summand is therefore strictly below 1/3, and `c_i n<2^(-B)n`.
The case b_i=0 is included. There is no independent resampling of
parities: all quantities belong to the one actual ordinary trajectory.

The first crossing also satisfies

\[
b_i<i\log_3 2<2i/3,                                    \tag{L2}
\]

using `3^(2/3)>2`, equivalently 9>8. A crossing can occur only on an
even input, but this extra fact is not needed for L1.

## LHS2. A new sufficient test through floor(k/1024) clocks

Use the same eligible comparison as the source:

\[
X=128k+1,\quad Y=64k+1,\quad n=27k+1=T^6(Y),
\qquad k>0,\quad4\nmid k.
\]

Retain k only if it passes BOTH tests:

1. The source test: `2^16 3^(b_i)>=2^i` through
   `1<=i<=floor(log_2 k)`.
2. The added test: `2^17 3^(b_i)>=2^i` through
   `1<=i<=floor(k/1024)`.

If the new test fails, take its first crossing i. Since `n<=28k`,
L1 and L2 imply

\[
176106n_i
<176106\left(\frac{28}{131072}+\frac{2}{9\cdot1024}\right)k
<76k<\frac58X.                                          \tag{L3}
\]

The middle inequality is exact rational arithmetic. Thus the source's
constructive directed reduction applies to the actual integer n_i.
It supplies a computable finite list of smaller adjacent implications,
all with upper antecedents below 5X/8, whose joint validity proves Y in C.
The list has O(log(2k)) members, as in the source theorem. Finding this
particular new witness may inspect O(k) actual parity steps; no logarithmic
search-time bound is asserted.

If X were the globally least failed eligible antecedent, every required
smaller implication would hold. Therefore a least failure passes the
added test. As a result, full Collatz is equivalent to the source's
directed implications restricted to the inputs retained by the conjunction.
An induction on the upper antecedent gives the forward sufficient
direction; full Collatz trivially implies every retained comparison.

The extended test includes the old one, so its retained set inherits
the old uniform-interval upper estimate

\[
O\!\left(N^{\rho}/\log(2N)^{3/2}\right),\qquad
\rho=h_2(\log_3 2)=0.949955527\ldots .
\]

The old matching lower bound concerns the old test only. It cannot be
carried over to this stronger conjunction. Conversely, the finite census
below does not establish a smaller asymptotic exponent for the new set.

## Why this does not yet close the theorem

The improvement uses the first-crossing condition to control the affine
remainder linearly in the observed odd count, in place of the source's
cruder bound by 2^i. It thereby extends a useful parity test far beyond
the initial log_2(k) binary horizon on each fixed ordinary input.

Counting those longer words uniformly over k in a short ordinary interval
is the first unsupported step. At length h, parity words are in bijection
with residue classes modulo 2^h. For h of order k, an interval of N ordinary
indices samples a very sparse specified portion of those classes. The
uniform binary-word ballot count used at h about log_2(N) does not apply
again to that portion without an additional distribution theorem.

This is also why the source's lower amplification bounds for the whole
failure basin cannot immediately contradict its sparse least-failure
sieve: they count different sets. A larger failure may reduce to a smaller
retained failure. The number and weights of its preimages must be
controlled before transferring either counting estimate.

The rank-five Mersenne witnesses in the source remain an explicit limit
to the old logarithmic test: they have a long forced initial ascent.
The linear test can inspect beyond that ascent, but convergence or a
guaranteed coefficient crossing in the available budget is not proved
for every exponent. No GRH assertion supplies the missing distribution
or fixed-source crossing in this note.

## Finite execution scope

`check_linear_horizon_sieve.py` independently iterates ordinary T, verifies
L1 at first crossings by exact integer arithmetic, verifies L3, compares
the two tests on a stated finite interval, and rejects malformed or
non-first crossing witnesses. The same source integer is retained at
every step. Its finite counts are observations, not extrapolated bounds.

The closing target remains a universally successful source-dependent
reduction, or a sufficiently strong count/weighted transfer estimate
on the extended retained set together with correct failure-set
quantifiers. Neither target is established here.
