# Edit distance from mechanical factors in a primitive positive cycle

**PROPOSED / SOURCE-QUALIFIED for the period-only floor.** Cut a primitive
positive ordinary shortcut cycle of length L>=2 at any phase, and read
one full tour of its parity word w. Let e be its Levenshtein distance
(unit-cost substitutions, insertions and deletions) from any finite factor
of any mechanical binary sequence

    v_j = floor((j+1) alpha + beta) - floor(j alpha + beta),

with real 0<=alpha<=1 and real intercept beta. The target factor need not
have length L. Writing c=log_2 3, one has

    L <= (e+2) [1 + 16 log_2 L + c(e+2)].                     (1)

In particular e >= (1/sqrt(c) - o(1)) sqrt(L) as L grows, uniformly over
cuts, slopes, phases and factor lengths. The same proof gives the version

    L <= (e+k+1) [1 + 16 log_2 L + c(e+2k)]                   (2)

when the target is a concatenation of k>=1 finite factors with the same
slope and independent phases. The results impose no prior fixed block
decomposition on the ordinary cycle itself.

## Two finite-word facts

For a factor from one mechanical sequence the number of ones in any
length-j substring differs from alpha j by less than one, by telescoping
the floors. This includes alpha=0 and alpha=1, with discrepancy zero.
For fixed alpha, there are at most h+1 different length-h words over
*all* intercepts. To see this, normalize beta to [0,1). The h integers
floor(j alpha+beta) at j=1,...,h change only at at most h thresholds.
Their consecutive differences, with floor(beta)=0, determine the word.
At thresholds the floor convention assigns the value on the right.

For an ordinary primitive cycle with largest value M, set
h=floor(log_2 M)+1. The length-h parity words from its L distinct phases
are pairwise distinct, since equal words would give a nonzero difference
divisible by 2^h>M. This is an ordinary spacing fact; it fails for general
orbits in odd-denominator rationals.

## Controlling the height under edits

Fix an alignment of w with a target consisting of k same-slope factors
using e edits. In each column, subtract its target contribution v-alpha
from its source contribution b-alpha, assigning zero contribution to
a missing bit. A matching column has zero error, and every individual
edit has absolute error at most one. Let E be the sum of these errors.
Choose monotone alignment cuts at each source index (the outer cuts span
the whole alignment). For any linear source interval I of length j, let
E_I sum the errors in its aligned columns. The target bits between the cuts
form a contiguous interval. Their deviation from slope alpha has magnitude
at most k, and so does the analogous deviation for the whole target.

Subtracting j/L times the full source deviation from the interval's
source deviation centers it at the actual density q/L. The contribution
from target deviations has absolute value at most 2k. The remaining
contribution is

    E_I - (j/L) E = (1-j/L) E_I - (j/L) (E-E_I),

whose absolute value is at most the total variation of all error columns,
at most e. Thus the centered cumulative parity height on w has oscillation
B<=e+2k. Cyclic intervals have the same bound because a wrapping
interval is the complement of a linear one and the full centered sum is
zero. Equation (1) in the [height note](HEIGHT_AND_ALMOST_PERIODS.md)
now gives h<=1+16 log_2 L+c(e+2k).

## Counting clean factors

If h>L, inequality (2) already follows. Otherwise there are L-h+1
linear starting positions in w. An edit consuming a source bit can spoil
at most h length-h windows containing that bit. An edit consuming only a
target bit can spoil only windows crossing its gap, again at most h.
Each of the k-1 internal cuts between target factors can additionally
spoil at most h such windows (among already unspoiled windows, only a
window with matched bits on both sides of that cut can be affected).
All remaining windows occur inside a single mechanical factor and have
at most h+1 possible words, independently of which phase supplied them.
Since the ordinary windows are distinct,

    L-h+1 <= (e+k-1)h + (h+1),      hence L <= (e+k+1)h.

This proves (2), and k=1 gives (1). Solving the quadratic inequality in
e+2, using log L=o(sqrt(L)), gives the displayed asymptotic floor.

The same counting argument before the period-only height substitution
gives L<=(e+k+1)(floor(log_2 M)+1), with no logarithmic-form input.
The source qualification in (1) and (2) comes from Rhin's estimate for
the cycle minimum, as documented in the [main note](README.md).
The [finite checker](shape_check.py) tests insertion, deletion and
substitution alignments, including mismatched word lengths.
A cycle far from this template class remains possible.
