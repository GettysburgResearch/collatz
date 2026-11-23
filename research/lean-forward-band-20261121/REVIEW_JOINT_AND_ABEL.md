# Independent review of the complete-clock and Abel-envelope arguments

**Scope:** the mathematical statements (TF), (JF), (CFJ), (PD), and the
finite excessive-envelope construction, as written in
`JOINT_CLOCK_MIXING.md` and sections 1–8 of `GLOBAL_RENEWAL_ATTACK.md`.
This review was carried out independently of the latter file's earlier
review. It re-opened the primary published source and reconstructed the
normalizations and ordinary-integer counting arguments.

**Verdict:** no gap found in those stated written arguments. They are not
Lean formalizations. Harmonicization and all-positive extension are valid
with the details below. Global ordinary sublinearity does not follow from
the resulting properties alone; an explicit actual-map obstruction is in
`HARMONIC_RAY_OBSTRUCTION.md`.

## 1. The stronger Fourier input is present in the primary source

Primary source: Terence Tao, *Almost all orbits of the Collatz map attain
almost bounded values*, [DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8).
The passages inspected were Section 6, especially Corollary 6.3, and
Section 7, equations (7.4)–(7.5), Lemma 7.2, and Proposition 7.3,
equation (7.10).

Conditioning on every pair sum, and the last individual letter in odd
length, fixes the **complete** exponent total. A bounded complex test of
that total is therefore constant inside the conditional factorization.
Its modulus can be discarded before using the product of pair-factor
moduli. The primary source bounds the expectation of this nonnegative
envelope, rather than only the final oscillating expectation. Taking the
dual bounded test of the total gives the claimed sum of absolute sliced
Fourier coefficients. A shorter conductor sees only the initial letters;
all remaining clock letters contribute an independent probability
convolution. Both observations preserve the required sliced norm.

At fixed separated prefix length and prefix total, Corollary 6.3 gives
at most one prefix at each residue. The raw Fourier Plancherel bound is
therefore `3^n * 2^(-ell)`, with a polynomial bound at the specified
prefix stopping scale. After truncating the complete clock at `6n`, the
joint total-variation Cauchy–Schwarz loss is only `6n` times that Fourier
quantity. The suffix conductors in the local `m>=0.9n` regime are bounded
below by a fixed positive multiple of `n`. The arbitrarily high polynomial
renewal decay absorbs this loss, the prefix partition, and the discarded
events. The geometric-resolution telescope is contractive in the stated
mixed norm. The projection is exactly `J_m * p_(n-m)`, with the whole
final clock retained.

## 2. Fixed totals and the ordinary population

The clock version of the weighted counting lemma uses
`sup_r sum_u`, with one common clock shift in each fixed-prefix-total
group. It does not exchange this with `sum_u sup_r`.

In the selected-density telescope, the initial cylinder has positive
total clock mass bounded below independently of its chosen level.
A finite subset of its clocks retains half that mass. Its fixed shifts
change the local negative-binomial lower bound only through the onset,
so the lower coefficient can be chosen before making the tail of the
error series small. Early errors receive the `O(1/N)` maximum-atom
factor from a remaining clock convolution; the late errors are
`O(N^(4-K))` after the required normalization. Ending the same telescope
at an intermediate depth handles all sufficiently large depths without
an unsupported finite-window convolution argument. The final unrestricted
suffix has length `O(N)`, so its real offset is still killed by the
`(7/8)^(Theta(N^2))` prefix multiplier. Spreading a fixed cylinder uses
only finitely many initial exponents and a fixed total shift.

For (PD), the interval of `Theta(sqrt(S))` depths is essential. At each
depth the common total places all selected sources in `(X/4,X]`, and the
fixed-total floor gives `Omega(X/(b*sqrt(S)))` distinct sources. The
chosen nonperiodic odd unit parent `b` makes sources at different depths
distinct. Its construction works for even supplied targets too: both
candidates have the same next **odd** value, namely the odd part of the
target, so at most one can be periodic. The onset condition is an absolute
multiple of `b`, and hence of the supplied target. No shrinking-target
rotation estimate or target-dependent onset is left in this counting
step. The map `n -> 4n+1` on nonunit odd sources correctly produces unit
sources with multiplicity at most two, and preserves actual hits to even
targets.

## 3. Abel finiteness and the correct even-target interpretation

For odd ordinary targets, the Cesaro estimate correctly separates the
nonperiodic case from periodic collisions. In the latter case the repeat
weights form the geometric series with the actual positive cycle
multiplier `lambda<1`. The discarded-clock bound is
`3^s * Pr(A_s>6s) <= (64/81)^s`; the moment generating function used in
it is exact. The resulting affine-in-depth Cesaro bound implies finite
Abel averages at every ordinary point. A diagonal subsequence and Fatou
give a finite excessive envelope. The uniform atom floor passes to its
pointwise lower bound. The cycle estimate
`(1-lambda)^(-1) <= 3q+1` also checks.

There are two valid ways to include every positive ordinary target.

First, repeat the same Cesaro/Abel construction on all positive integers.
Write `q=2^E*r`, with `r` odd. A nonempty formal inverse word ending at
`q` corresponds to an accelerated odd history ending at `r` whose last
actual exponent is greater than `E`. Its formal total is the actual total
minus `E`. Fixed-depth injectivity is unchanged. Repeated-depth collisions
are governed by periodicity of **r**, not by an assertion that q is itself
an odd periodic point. The same cycle multiplier for r bounds all
repeated weights; the last-exponent restriction can only discard some
repeats. Thus the Cesaro bound remains valid with `eta_r` in place of
`eta_q`. Depth zero contributes the separate finite term one. In
particular the bound `F(q) <= q(3r+1) log(64/3)` is available after
extraction, and the coarser quadratic bound remains valid.

Second, an already constructed odd harmonic envelope can be extended
directly by the tail formula in section 4 below. This does not require a
fresh all-positive Abel extraction.

## 4. Harmonicization is valid, but requires a new uniform floor

Suppose `F` is the finite excessive envelope, with
`F>=c0*1_unit`. The exact first-depth density is one on residue one
modulo three, two on residue two, and zero on multiples of three.
Consequently

\[
P^kF\ge c_0 P^k1_{\rm unit}
      \ge\frac{c_0}{2}D_{k+1}.
\]

The uniform atom floor makes this at least `c0^2/2` on units once k is
large. Since `PF<=F`, the sequence `P^kF` decreases pointwise to a finite
function G with that positive floor. At each fixed target, the summands
are bounded by the summable series defining `PF(q)`. Dominated
convergence for this countable sum gives `PG=G`; Fatou alone would not
give the equality.

For an odd harmonic G, define its even values by `G(q)=PG(q)`.
For odd r the exact formula is

\[
\frac{G(2^E r)}{2^E r}
 =\frac1r\sum_{\substack{a>E\\2^a r\equiv1\ (3)}}
       \frac3{2^a}G\!\left(\frac{2^a r-1}{3}\right).
\]

The right side is a tail of a finite nonnegative series, so it tends to
zero for each fixed r. The definition is finite and harmonic on all
positive arguments because P only uses odd parents. A short unit parent
with exponent at most six gives a uniform positive floor on even units
too, after decreasing the constant if necessary.

The decay just proved keeps the odd core fixed. The explicit construction
in `HARMONIC_RAY_OBSTRUCTION.md` shows that harmonicity, a uniform floor,
and these ray limits are compatible with a positive lower bound for
`G(q)/q` along an unbounded sequence of odd units, including a marked
sequence when the pinned marked-ancestor theorem is used. A successful
closing argument must therefore use additional information about the
specific Abel-derived envelope, or a further uniform estimate.
