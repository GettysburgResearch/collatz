# Exact audit of the v3 Farkas proposal and v2 Dirichlet/exponent blueprints

**Status: mathematical audit and repaired local certificates. No Collatz proof
is claimed.** The original packages are preserved without editing. The main
positive extension is in `ORDINARY_DIRICHLET_COERCIVITY.md`: using PR146's
ordinary variation geometry, it proves a norm comparison throughout
`0 < s < 1`, beyond the range asserted by the finite-LP proposal and without
assuming divergence at the abscissa. The results below distinguish what the
uploaded verifiers actually establish from what their prose asserts.

## 1. What survives, what is repaired, and what remains open

| Item | Audit outcome |
|---|---|
| v3 residue-class Dirichlet relations | Correct, with the stated holomorphic remainder and the divergence hypothesis where normalization is used. |
| v3 exported dual at `r=4, s=0.84` | Repaired rigorously from its exact serialized decimal multipliers; every residual is positive. |
| v3 exported dual at `r=6, s=0.913` | Repaired rigorously in the same way. |
| Original claim of an exact verifier | The original uses floating point powers/matrix products, checks unrounded vectors, then exports rounded vectors without rereading them. |
| `r=8, 0.950131` and all exponents below it | No corresponding certificate or interval-coverage proof is supplied. The receipt's `r=8` field is a literal constant in the source. |
| v3 abscissa conclusion implies an all-scale `Omega` count | False as a general inference. A doubling-invariant counterexample is given below. |
| v2 exact scalar binomial-shift identity | Correct; its remainder is holomorphic near the abscissa. |
| v2 normalized residue bias from Landau alone | Unsupported without divergence or another argument controlling the normalized remainder. A singularity need not have infinite boundary value. |
| v2 transfer matrix | An averaged hidden-lift matrix, with an exact modulus-independent spectral radius computed below. It is not a source-persistent ordinary predecessor lower-bound system. |
| v2 global strict spectral monotonicity | False on `s>0`; the spectral radius at `s=3` exceeds its value at `s=1`. Monotonicity of the infinite-gap formula on `0<s<1` is true but does not repair the ordinary-model gap. |
| v2 claimed Krasikov–Lagarias certificate | The code computes roots of the same averaged scalar formula, not the minimax difference inequalities of that theorem. |
| v2 exponent crossing | A valid conditional counting contradiction, with the fixed-floor survivor upper bound still missing. A predecessor lower exponent cannot supply that upper bound. |

## 2. Exact meaning of the v3 finite system

Let `M=3^r`, `P=3^{r-1}`, and `i=2^{-1} mod M`. For an ordinary invariant
indicator `f`, write `D_a(s)` for its Dirichlet series in residue class `a mod M`
and `D(s)=sum_a D_a(s)`. Set

\[
p=2^{-s},\qquad q=3^{-s},\qquad t=(2/3)^s,
\quad\hbox{so that }tp=q.
\tag{1}
\]

The exact even/odd relation is

\[
O_a(s)=D_a(s)-pD_{ai}(s)\ge0
\tag{2}
\]

for real `s` in the convergence region. With `c=3k+2` and
`b=(2k+1) mod P`, the odd shortcut gives

\[
D_c(s)-t\sum_{m=0}^2O_{b+mP}(s)=H_c(s).
\tag{3}
\]

Expanding the shift factor `(1+1/(3n))^{-s}` at odd inputs yields a remainder
bounded on compact sets by a constant times `D(Re(s)+1)`. Its binomial series
converges normally there, so `H_c` is holomorphic on a neighborhood of the
abscissa. Finally the tripling difference is exactly

\[
\Delta_b(s)=D_{3b}(s)-q\sum_{m=0}^2D_{b+mP}(s)
=3^{-s}\sum_{n\equiv b\ (P)}(f(3n)-f(n))n^{-s}.
\tag{4}
\]

If `D(s)` tends to infinity as `s` decreases to the abscissa `sigma`, a
subsequential limit of `v_a(s)=D_a(s)/D(s)` satisfies the normalized system in
the proposal whenever `Delta_b(s)/D(s)` tends to zero. The divergence hypothesis
is used exactly to make `H_c(s)/D(s)` vanish; compactness alone does not do that.

In matrix notation the proposed zero-defect limiting system is

\[
v\ge0,\quad A(s)v\le0,\quad B(s)v=b,
\tag{5}
\]

where `b` is zero except for its final normalization entry, which equals one.
A certificate consists of `u>=0` and arbitrary `w` such that

\[
u^TA(s)+w^TB(s)\ge0,\qquad w^Tb<0.
\tag{6}
\]

Indeed, applying the first expression to a feasible nonnegative `v` gives a
nonnegative number, while feasibility implies it is **at most** `w^Tb<0`.
The original code's explanatory comment incorrectly writes this latter
inequality as an equality after discarding `u^TAv`; its subsequent intended
contradiction only requires the inequality and is valid.

## 3. Rigorous repair of the two supplied exported certificates

The original certificate file has SHA-256
`ab41ca28f00904efa2732ffbdc06f19b592ae4e874b586554c550c2f975bde5c`.
The checker `check_farkas_and_ruelle.py` reads those bytes as exact decimal
rationals. It neither calls an LP solver nor regenerates any multipliers.
Every multiplier has denominator dividing `10^10`.

After collecting coefficients and using the exact identity `tp=q`, each dual
coordinate has the form

\[
C_a+A_a2^{-s}+B_a3^{-s}+F_a(2/3)^s,
\tag{7}
\]

with exact rational coefficients. This avoids treating two numerical
approximations to `t*p` and `q` as an exact identity. The checker constructs
these coefficients directly from (2)–(4) and the normalization row.

### Certified point results

All bounds in the table are outward-rounded exact enclosures of the minimum
over every dual residual coordinate.

| Level | Exact exponent | Coordinates checked | Minimum residual interval | Normalization multiplier |
|---|---:|---:|---|---:|
| `r=4` | `21/25` | 81 | `[0.999999999412877118, 0.999999999412877119]` | `-1` |
| `r=6` | `913/1000` | 729 | `[0.999999999270272552, 0.999999999270272553]` | `-1` |

In both cases every `u` is exactly nonnegative. These are therefore genuine
finite infeasibility certificates at the stated points. Their strict margins
also imply persistence on some neighborhood by continuity, but this packet
does not claim or scan a covering family of exponent intervals.

For a point `sigma` certified this way, let `m_sigma>0` be its minimum residual,
and let `W` be the largest absolute multiplier among the tripling rows. Applying
the same dual to the actual Dirichlet vector, including the remainders, gives

\[
(1+m_s)D(s)
\le \left|\sum_cw_cH_c(s)\right|
       +3^{-s}W D_{\partial_3K}(s).
\tag{8}
\]

Here `m_s` is the continuous minimum residual of these fixed multipliers at
nearby `s`; the inequality follows from (2), not from discarding a signed
ordinary forcing term. If `D(s)` diverges at this `sigma`, (8) proves the local
consequence

\[
\liminf_{s\downarrow\sigma}
\frac{D_{\partial_3K}(s)}{D(s)}
\ge\frac{3^\sigma(1+m_\sigma)}{W}>0.
\tag{9}
\]

The ordinary coercivity theorem in the companion note proves a positive
comparison throughout the subcritical strip without the divergence assumption.
That extension uses ordinary variation geometry, not an asserted all-level LP
result.

### Exact interval arithmetic

The numerical-looking table is decided only by integers. For `0<=z<=1/3`, use

\[
\log\frac{1+z}{1-z}
=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
\qquad
0\le R_N\le\frac{9}{4(2N+1)3^{2N+1}}.
\tag{10}
\]

Binary normalization reduces the needed logarithms to this range. With
`N=64`, every product and quotient is rounded outward on the integer scale
`10^50`. For `0<=x<=2`, the positive Taylor polynomial for `exp(x)` through
degree `L=80` has omitted tail at most

\[
\frac{2^{L+2}}{(L+1)!}.
\tag{11}
\]

This follows because the first omitted term is at most
`2^{L+1}/(L+1)!` and every later ratio is below one half. Inverting the positive
enclosure gives `exp(-x)`. Apply it to `s log2`, `s log3`, and `s log(3/2)`.
All coefficient signs are retained when selecting interval endpoints in (7).

As an exact negative control, at `s=1` the uniform vector `v_a=1/M` is feasible:
each inequality residual is `-1/(2M)`, every odd-image and tripling equality
residual is zero, and normalization is one. The checker also confirms that
both exported duals have a negative coordinate at `s=1`, as they must.

### Why the uploaded verifier alone was not this proof

The source builds `float64` matrices, computes real powers in floating point,
solves a floating point LP, and tests matrix products with a fixed tolerance.
It verifies the unrounded solver output, then serializes rounded decimal
multipliers without reading the serialized vectors back. A large floating
margin is useful evidence for repair; it is not by itself an outward error
bound for irrational coefficients or for the exported vector. The new checker
supplies precisely that missing bound.

The `r=8` receipt entry is inserted literally into the JSON object; the
original `main()` computes only `r=4` and `r=6`. No `r=8` vector is included,
and neither two point certificates nor a purported last feasible threshold
proves infeasibility at **all** exponents in the interval used by v3
Theorem 3.1. The mixed-sign equalities do not supply an automatic monotonicity
principle for that LP family.

## 4. Exact spectral formula for the v2 averaged matrices

Both `build_ruelle_syracuse_matrix` and `build_kl_matrix` construct the same
kind of matrix on units modulo `M=3^r`. For a source class `u`, a gap `g`, and
each hidden lift `c in {0,1,2}`, they insert weight `(3/2^g)^s/3` at

\[
v\equiv\frac{2^g(u+cM)-1}{3}\pmod M
\tag{12}
\]

when division is integral and `v` is a unit. Let gaps range from 1 to `G`.

**Exact matrix theorem.** For every `r>=1`, `G>=1`, and real `s>0`,

\[
\rho(L_{r,G}(s))
=3^{s-1}\sum_{g=1}^G2^{-gs}.
\tag{13}
\]

**Proof.** Fix a unit target `v` and a gap `g`. There is exactly one solution

\[
u+cM\equiv2^{-g}(3v+1)\pmod{3M},
\tag{14}
\]

with `0<=u<M` and `c in {0,1,2}`. The recovered `u` is a unit and satisfies
the legal gap congruence. Thus every target column receives exactly one weight
`(3/2^g)^s/3` per gap. Every column sum equals the right side of (13). It is
an eigenvalue of the transpose with the all-ones eigenvector, while the induced
column-sum norm bounds the spectral radius above by the same number. QED.

The companion checker verifies (14) against direct source/lift enumeration at
36 fixed `(r,g)` pairs; the proof above, rather than those finite cases, gives
all `r,g`. In the unlimited-gap model the exact formula becomes

\[
\rho(L_{r,\infty}(s))=\frac{3^{s-1}}{2^s-1}.
\tag{15}
\]

The following consequences identify the original code's scope:

* It is independent of `r`. Increasing the ternary modulus cannot improve the
  roots computed by these particular matrices.
* At finite `G`, the value at `s=1` is `1-2^{-G}`, not exactly one. The original
  large `G` makes the difference smaller than its floating tolerance.
* In the unlimited-gap model the values at `s=1` and `s=3` are `1` and `9/7`.
  Therefore global strict decrease on `s>0` is false. Already with `G=4`, the
  corresponding values are `15/16` and `5265/4096`.
* The infinite-gap expression does decrease on `0<s<1` and is greater than one
  there. Indeed its logarithmic derivative is
  `log3-(log2)*2^s/(2^s-1)`, which is negative on that interval. This scalar
  fact does not identify the matrix with ordinary predecessor dynamics.
* The v2 roots approaching one as `G` increases are roots of (13), an averaged
  normalization equation. They are not Krasikov–Lagarias minimax certificates.

### The concrete missing ordinary term

A coarse residue mass is the sum of its three hidden-lift masses. It does not
make each lift one third of that sum. If the actual lift masses are `F_{u,c}`,
the exact projection involves the three separate terms; the averaged operator
replaces them by `F_u/3`. Its omitted signed contribution contains

\[
\sum_c w_{u,c}\bigl(F_{u,c}-F_u/3\bigr),
\tag{16}
\]

with branch-dependent target and survival weights. Nothing in the uploaded
verifiers proves that this term vanishes, has a favorable sign, or stays small
under repeated transport from one fixed ordinary source.

For a concrete one-step example, take the positive odd source `7`, whose class
modulo three is `1`, and gap `g=2`. Its actual inverse endpoint is
`(4*7-1)/3=9`, excluded by the unit restriction. The averaged row for source
class `1 mod3` uses hidden lifts `1,4,7 mod9`, whose targets modulo three are
`1,2,0`: it assigns positive mass to two surviving unit targets. This is the
specific hidden-lift replacement, not a rounding error.

## 5. Two analytic inferences that require separate hypotheses

### 5.1 A singularity need not have infinite boundary value

Let

\[
\ell(k)=\lceil\log_2(k+1)\rceil,\qquad
n_k=k^2\ell(k)^4,\qquad A=\{n_k:k\ge1\}.
\]

The `n_k` are strictly increasing. The zero-one Dirichlet series of `A` has
abscissa one half, because `log n_k/log k` tends to two. But its critical value
is finite:

\[
D_A(1/2)=\sum_{k\ge1}\frac1{k\ell(k)^2}<\infty.
\tag{17}
\]

On `2^{j-1}<=k<2^j`, the inner contribution is at most `1/j^2`. The boundary
point is still a singularity: the differentiated absolute series at one half
has block contributions at least `(j-1)log(2)/j^2`, so its sum diverges and
`D_A'(s)` tends to minus infinity as `s` decreases to one half. A holomorphic
extension through that point would have a finite derivative.
Consequently the holomorphic remainder in the correct v2 scalar identity does
not automatically disappear after division by `D(s)`. The identity itself is
valid; the normalized mass conclusion needs an additional hypothesis.

This example is not asserted to be invariant under Collatz. It disproves the
generic implication from a nonnegative Dirichlet singularity to divergence,
which is the inference used in the blueprint.

### 5.2 An abscissa lower bound is not an every-scale counting bound

Here is a counterexample retaining exact doubling closure and divergence at
the critical exponent. Set `gamma=21/25` and

\[
N_k=2^{25\cdot2^k},\quad L_k=2^{21\cdot2^k},\quad
U_k=\{N_k+2j+1:0\le j<L_k\},
\]

and let `A` contain every dyadic multiple of every odd integer in every `U_k`.
The odd roots are distinct, and

\[
D_A(s)=\frac1{1-2^{-s}}\sum_{k\ge1}\sum_{u\in U_k}u^{-s}
\tag{18}
\]

for `s>0`. Since each block has `L_k=N_k^gamma` roots comparable to `N_k`, its
contribution is comparable to `N_k^{gamma-s}`. Therefore the abscissa is exactly
`gamma`, and the critical series diverges, with each block contributing a
positive amount bounded away from zero.

Yet at `X_k=N_{k+1}/2=N_k^2/2`, no later block has appeared. Each old odd root
has at most `1+log_2 X_k` dyadic multiples below `X_k`, so

\[
|A\cap[1,X_k]|\le(1+\log_2X_k)\sum_{i\le k}L_i
=O((\log N_k)N_k^\gamma).
\tag{19}
\]

For every `0<epsilon<gamma/2`, division by `X_k^{gamma-epsilon}` tends to zero.
Thus even exact doubling invariance and divergence at the critical abscissa
do not imply the every-scale `Omega(X^{gamma-epsilon})` conclusion asserted
by v3. The support is not claimed to be Collatz invariant; it tests the stated
generic Dirichlet-to-counting inference. For sets of integers the general
identity is that the abscissa equals the **limsup** counting exponent.

The companion ordinary theorem establishes equal abscissae for actual invariant
populations, and clearly leaves this all-scale upgrade separate. PR146 already
contains a distinct ordinary argument giving a smaller positive exponent at
every large scale, and the power-0.84 conclusion along an unbounded sequence.

## 6. Exponent crossing and the chain/core proposal

The conditional counting principle in v2 is correct: if every hypothetical
component `K` contains a predecessor family with count at least `c_K X^alpha`,
and the eternal survivors above its fixed minimum have count at most
`C_K X^beta` with `beta<alpha`, the two inequalities contradict one another.
The missing assertion is the fixed-floor survivor upper bound. A native
finite-horizon estimate does not transfer to all-time fixed-floor survival
without a proof, and an external predecessor exponent such as `0.901` is a
lower-bound input, not an upper survivor exponent. Subtracting `0.84` from it
does not measure a proved remaining upper/lower gap.

The proposed ternary-chain/core split does not supply that proof or a new
polynomial boundary bound:

* Counting all points in an invariant set and stripping their odd parts gives,
  without additional information, a lower bound with a possible `log X` loss.
  The claimed same-exponent constant for odd points is not immediate.
* A finite chain beginning below `X` may first leave the set at a scale
  arbitrarily larger than `X`. Finiteness of its exit time is not a uniform
  bound on its exit scale. The Case A assertion leaves this exact term
  uncontrolled.
* The core closed under multiplication by two and three need not be invariant
  under the ordinary map, under multiplication by five, or under addition by
  one. The cited qualitative obstruction does not by itself yield a polynomial
  number of five-ray defects with bounded multiplicity and scale. That is the
  missing Case B inference.

The associated verifier checks one value of `floor(log_3 X)+1` and a finite
range of the bridge identity; it does not construct the chain partition or
verify either of those two purported global cases. The bridge identity itself
is valid on all positive inputs and is now checked as an exact affine identity
in the ordinary coercivity packet.

## 7. Reproduction and claim boundary

Run the exact checker against the preserved supplied JSON:

```sh
python check_farkas_and_ruelle.py --certificates PATH/TO/farkas_certificates_r4_r6.json --output farkas_ruelle_receipt.json
python -O check_farkas_and_ruelle.py --certificates PATH/TO/farkas_certificates_r4_r6.json --output farkas_ruelle_receipt_optimized.json
```

All verification conditions use explicit runtime checks, so Python optimization
does not remove them. The receipts must be byte-identical. They record source
and checker hashes, exact interval semantics, every finite point scope, the
uniform feasible negative controls, and the averaged-matrix reconstruction.

The global positive proof and its separate finite replay are in
`ORDINARY_DIRICHLET_COERCIVITY.md`, `check_ordinary_dirichlet.py`, and
`ordinary_dirichlet_receipt.json`. They use the pinned PR146 ordinary construction
at commit `7d04c4dd756cfe495eb3eee78eba35a99085cd2a`. Neither checker purports to
decide the infinite arguments by finite tests. No new threshold scan, formal
all-level infeasibility claim, or full Collatz resolution is attached to this
packet.
