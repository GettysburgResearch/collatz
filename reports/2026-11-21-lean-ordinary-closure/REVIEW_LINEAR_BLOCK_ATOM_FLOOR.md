# Independent review: linear selected blocks and harmonic predecessor mass

## Verdict

I found no mathematical gap in the staged derivation
`agent-energy-global/LINEAR_BLOCK_ATOM_FLOOR.md`, including its updated
finite-cylinder argument. The proof establishes a uniform lower bound for
Syracuse residue densities and, consequently, divergent reciprocal mass
of the ordinary predecessors of every positive ternary-unit target,
**using Tao's published fine-scale mixing theorem**.

This is a review of the written analytic proof. It does not turn that
proof or its imported analytic theorem into a Lean-checked result. It
does not prove Collatz or the repository's still-missing finite-energy
estimate.

## Exact external input checked

I inspected Terence Tao's published Cambridge article directly:

https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F

Proposition 1.14, equations (1.26)–(1.27), quantifies over every
`1 ≤ m ≤ n`. With normalized counting measure and
`D_n = 3^n Pr(X_n = ·)`, its oscillation is precisely

\[
\|D_n-\operatorname{lift}D_m\|_1\le C_A m^{-A}.
\]

The reverse-word expression used in the staged note has the same law as
Tao's offset because its letters are independent and identically
distributed. Its consistency under ternary projection is immediate from
the displayed sum: terms past the projection level vanish. No
conditional estimate on an individual exponent total or joint affine-map
mixing assertion is being imported.

## Arithmetic counting and resolution checks

For a fixed total `A`, the offset numerator

\[
B(w)=\sum_{i=1}^d3^{i-1}2^{A-A_i}
\]

determines the word. Indeed,
`B(w) − 3^(d−1) = 2^(a_d) B(prefix)`, and the prefix numerator is odd.
The final letter is recovered by exact two-adic valuation, and induction
recovers the remaining letters, using the prescribed total for the first
letter.

For a fixed output representative `M`, every contributing word therefore
gives a distinct integer

\[
R_w=(2^A M-B(w))/3^d.
\]

At fixed `A` these integers occupy an interval of length at most
`B_*/ω`. A residue modulo `3^q` consequently receives at most
`B_*/(ω 3^q)+1` such integers. Multiplication by the transport coefficient
`ω`, followed by summation over input residues and the distinct totals,
gives the claimed weighted `L¹ → L∞` bound. Negative values of `R_w`
cause no issue for this counting argument.

This operator estimate is the essential additional ingredient. The
argument does **not** assert that a small `L¹` norm directly bounds every
residue density.

The changing resolutions satisfy all of the necessary identities:

\[
Q_N=d_N+k_N,\qquad
q_N=b_N+k_{N+1},\qquad
d_N+q_N=Q_{N+1},\qquad k_N\le q_N.
\]

Thus the comparison

\[
g_{N+1}-\operatorname{lift}g_N
=\sum_{w\in\Gamma_N}T_{w,q_N}
   (R_N-\operatorname{lift}D_{k_N})
\]

has the same domain and codomain on both sides. Transport commutes with
lifting because its affine map is injective from `G_q` onto the
corresponding cylinder in `G_(d+q)`.

## Uniform bounds and positive-cylinder construction

The elementary constants are valid:

- The geometric moment bound gives rejection probability at most
  `2 exp(−b_N/1200)`.
- Positive acceptance at every block and summable rejection imply a
  positive lower bound for all prefix acceptance products.
- The offset series is uniformly bounded because previous retained
  multipliers decay quadratically in the block index, while an individual
  block offset bound grows only exponentially in that index.
- The product `3^(q_N) Ω_N` is uniformly bounded for the same reason.
- `d_N = O(N²)` and `b_N = O(N)` make the resulting increment series
  `Σ O(N²)(exp(−cN)+N^(−4))` convergent.

The finite-cylinder replacement is particularly clean. Write
`ε_N` for the proved uniform increment bound. Choose `N₀` such that

\[
\sum_{N\ge N_0}\varepsilon_N<P_\infty/2.
\]

Since `g_(N₀)` has mean `P_(N₀) ≥ P_∞`, some residue `y` at level
`q = Q_(N₀)` has value at least `P_∞`. It is a unit because the selected
density vanishes on multiples of three. Uniform telescoping gives a
lower bound `P_∞/2` at every lift of that residue at every later selected
level. Averaging at a fixed intermediate resolution transfers the same
bound to `D_h` on the entire cylinder.

There is no almost-everywhere substitution at this step. The result
applies to each fixed residue in that cylinder. The proof can also avoid
an infinite-product notation: a sufficiently late tail has rejection
sum below one half, so a positive finite prefix product divided by two
is a uniform lower bound for all prefix products.

The one-step recurrence then spreads the cylinder lower bound to every
unit residue. Two generates the unit group modulo `3^(q+1)`, so one can
choose a positive exponent at most `2·3^q` sending any specified unit
output's inverse input into that fixed cylinder. This choice is uniform
in the finer resolution. The recurrence coefficient is bounded below by
`3·2^(−2·3^q)`, a strictly positive constant. Projection handles the
finitely many smaller resolutions.

## Ordinary inverse paths and periodic targets

The word-to-source passage is valid in ordinary positive arithmetic.
The final congruence implies every prefix congruence, because all later
offset terms are divisible by the appropriate ternary power. Hence each
inverse intermediate is integral. Starting from a positive odd target,
the inverse formula has a positive numerator; integrality then gives a
positive integer. It is odd, so the prescribed division exponent is
exact. Fixed-depth source injectivity follows from deterministic forward
orbits and their exact valuations.

For a nonperiodic target, a source appearing at two depths would make the
target periodic. Depth sets are therefore disjoint, and a uniform
positive reciprocal mass at each depth gives divergence without double
counting.

For a periodic odd unit target, the three admissible exponents separated
by two produce three distinct odd parents. Their residues cycle through
the three ternary classes, so two parents are units. At most one is the
cycle predecessor. A nonperiodic unit parent therefore exists and its
predecessor set embeds into the original target's predecessor set.

For an even unit target `2^i a₀`, starting the admissible exponents at
`e ≥ i+1` ensures the ordinary shortcut orbit from the chosen odd parent
passes through the specified even target. Finally, the proposed
comparison of nonunit source mass with unit source mass is valid:
for each unit successor `m`, summing all possible nonunit parents gives
at most `6/m`. Thus divergence also holds after restricting sources to
ternary units.

## Scope and attribution

The selected-density strategy and weighted counting lemma are explicitly
attributed in the staged note to the external work identified by its
author. This review verifies the displayed mathematics; it does not
independently authenticate the inaccessible Zenodo archive or make a
priority claim. The new linear schedule is an adaptation of that
strategy.

## Additional review: positive lower logarithmic density

The later quantitative strengthening is also valid. It is necessary when
the desired endpoint contradiction concerns normalized means: divergent
reciprocal mass alone would not exclude a reciprocal sum growing more
slowly than `log X`.

For `A_s` the sum of `s` independent geometric letters,

\[
\mathbb E[(3/2)^{A_s}]=3^s,
\qquad
3^s\Pr(A_s>6s)\le(64/81)^s.
\]

Thus for every sufficiently large depth, words with `A_s ≤ 6s` retain
at least half the uniform normalized atom floor. Their ordinary sources
satisfy

\[
n<a(64/3)^s.
\]

For a nonperiodic odd unit target `a`, their contribution at each depth
is at least `c/(2a)`. Disjointness of depths gives

\[
H_a(X)\ge\frac{c}{2a}
\left(\left\lfloor\log_{64/3}(X/a)\right\rfloor-s_0+1\right)_+.
\]

In particular,

\[
\liminf_{X\to\infty}\frac{H_a(X)}{\log X}
\ge\frac{c}{2a\log(64/3)}>0.
\]

For an arbitrary positive unit target `a = 2^i a₀`, the first admissible
inverse exponent at least `i+1` belongs to `{i+1,i+2}`. Among it and the
next two admissible exponents, the chosen nonperiodic unit parent has

\[
b<\frac{64}{3}a<22a.
\]

Applying the preceding result to `b` therefore gives the stated uniform
lower logarithmic coefficient `c/(44a log(64/3))` for odd predecessors
of the original ordinary target.

The source-unit restriction remains valid with explicit cutoffs. Since
`U(n) ≤ 2n` for positive odd `n`, the earlier reciprocal parent bound
gives

\[
H_{\rm nonunit}(X)\le6H_{\rm unit}(2X),
\qquad
H_{\rm all}(X)\le7H_{\rm unit}(2X).
\]

Replacing `2X` by a new cutoff loses only the factor seven in the
asymptotic lower logarithmic coefficient. A valid uniform unit-only
constant is consequently `c/(308a log(64/3))` using the coarse parent
bound above.

The resulting theorem removes the fixed-target positive lower
logarithmic density hypothesis in the energy route. The all-source
energy or charge estimate required to force a constant ordinary invariant
remains a separate, unproved obligation.

## Exact application to the repository's rigidity statements

I also read the named statements at their frozen repository commits:

- PR163 `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  `research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, FE1.
- PR155 `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
  `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
  OD3, and the companion `ENDPOINT_BOUNDARY.md`, Section 1.

The application in `REPOSITORY_RIGIDITY_COROLLARY.md` matches those
hypotheses. A bounded 1-Lipschitz scalar separation of two distinct metric
labels is ordinary invariant and has no larger five or tripling defect.
FE1 has five energy on its right-hand side on exactly the positive odd
ternary-unit domain specified in the corollary.

At the endpoint, the pinned source's proof gives the centered shell
conclusion for all bounded real labels: it follows directly from its
`L¹` profile convergence and the lower measure of each integer cell.
Booleanity is used only to force the limiting constant to be zero or
one, a property the new argument does not need.

If `a_k` denotes the centered unweighted shell mean, then each shell's
centered reciprocal sum is at most `a_k`. Since `a_k → 0`, Cesàro
summation proves a centered reciprocal sum of `o(log X)`. On one of the
two separated ordinary label classes the centered distance is at least
half the separation. That class contains a positive unit target and its
predecessors, whose reciprocal mass is at least a positive multiple of
`log X`. This is the required contradiction. It does not assert finite
centered harmonic mass.

There is also a shorter route to the full stated exponent range. After
harmonic rigidity is proved, monotonicity gives

\[
E_5(1;f)\le E_5(s;f)\qquad(0<s\le1).
\]

Thus every subcritical finite-five-energy hypothesis implies harmonic
finite energy, and the endpoint argument alone proves rigidity on the
whole range. OD3 correctly gives the alternate subcritical argument in
the staged corollary, but is not a logically necessary additional
premise for its final rigidity conclusion.
