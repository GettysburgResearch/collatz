# L-8201 — Sparse-resultant caps for every fixed negative-cycle pulse cone

**Claim ID:** `L-8201`
**Status:** `PROPOSED`
**Authoring agent:** `gpt56-outlier-01`
**Reviewing agents:** none yet
**Created:** 2026-07-23
**Last updated:** 2026-07-23
**Issue:** #52
**Dependencies:** branch-qualified PR #47 `L-9602` for the exact pulse-correction identity; PR #51 `L-8001` for the two-pulse comparison only
**Scope:** coordinatewise positive valuation perturbations of one fixed ordinary negative accelerated Collatz cycle word

## Statement

Let

\[
w=(a_0,\ldots,a_{K-1}),\qquad a_j\ge 1,
\]

be an accelerated valuation word with an ordinary negative odd cycle

\[
3z_j+1=2^{a_j}z_{j+1},\qquad z_K=z_0<0.
\]

Write

\[
A_0=0,\qquad A_j=\sum_{h<j}a_h,\qquad A=A_K,
\]

and put

\[
U=2^A,\qquad Q=3^K.
\]

Fix a nonempty pulse support. After cyclic rotation, write it as

\[
0=p_1<p_2<\cdots<p_e<K.
\]

At `p_i`, increase the valuation by `d_i>=1` and put

\[
X_i=2^{d_i},\qquad P_0=1,\qquad P_i=\prod_{h=1}^{i}X_h.
\]

Define the positive positional weights

\[
W_i=(-z_{p_i+1})3^{K-1-p_i}2^{A_{p_i+1}}
\]

and chain coefficients

\[
c_0=-W_1,\qquad
c_j=W_j-W_{j+1}\ (1\le j<e),\qquad
c_e=W_e.
\]

The pulse correction and cycle denominator are

\[
H=\sum_{j=0}^{e}c_jP_j,
\qquad
D=UP_e-Q.
\]

For each `1<=i<=e`, define

\[
H_i^- =\sum_{j=0}^{i-1}c_jP_j,
\]

\[
H_i^+ =\sum_{j=i}^{e}c_j\prod_{h=i+1}^{j}X_h,
\qquad
S_i=\prod_{h=i+1}^{e}X_h,
\]

with empty products equal to `1`, and define the reduced one-variable resultant

\[
\boxed{E_i=US_iH_i^-+QH_i^+.}
\]

Then:

1. **Exact elimination.** For every positive pulse-height tuple,
   \[
   D\mid H\quad\Longleftrightarrow\quad D\mid E_i.
   \]
2. **Nonvanishing with exact valuation.** For every such tuple,
   \[
   \boxed{\nu_2(E_i)=A_{p_i+1}.}
   \]
   In particular `E_i` never vanishes.
3. **Uniform coordinate cap.** Put
   \[
   \Lambda_i=
   U\sum_{j<i}|c_j|+Q\sum_{j\ge i}|c_j|.
   \]
   Every positive-divisor hit `D>0` and `D|H` satisfies
   \[
   \boxed{
   X_i\le
   \left\lfloor
   \frac{2^{e-1}\Lambda_i+Q}{2^{e-1}U}
   \right\rfloor.}
   \]
4. **Fixed-cone finiteness.** For the fixed word `w`, only finitely many pulse vectors
   \[
   b=(b_0,\ldots,b_{K-1})\in\mathbf Z_{\ge0}^{K}
   \]
   can satisfy the positive-cycle divisibility condition obtained by increasing `a_j` to `a_j+b_j`. Explicit bounds are computable support by support.

Subject to the exact pulse-correction identity in PR #47 `L-9602`, every positive accelerated cycle produced by upward pulsing this fixed negative cycle lies in that finite set and can be exhaustively replayed.

## Definitions and motivation

PR #51 proves that every fixed two-pulse packet has finite all-size caps by constructing two nonzero eliminants `K(M)` and `J(X)`. The question left open there is whether three or more pulses can support a hidden positive-dimensional resonance.

The remote-field observation is that `D` and `H` are sparse Laurent polynomials in the dyadic variables `X_i`. Holding every variable except `X_i` fixed makes both polynomials linear in `X_i`. Their two-by-two Sylvester determinant eliminates `X_i`. The Collatz-specific coefficient valuations then rule out the zero-resultant locus on the dyadic torus.

The sparse-resultant and non-Archimedean/tropical literatures supply the right conceptual language. The proof below is elementary and does not import either literature as a black box.

## Proof

### 1. Chain form of the pulse correction

PR #47 `L-9602` gives, for a pulse vector supported at the ordered positions `p_i`,

\[
H=
\sum_{i=1}^{e}
W_i(X_i-1)P_{i-1}.
\]

Since `(X_i-1)P_{i-1}=P_i-P_{i-1}`, this telescopes into

\[
H=-W_1P_0+
\sum_{j=1}^{e-1}(W_j-W_{j+1})P_j+W_eP_e
=\sum_{j=0}^{e}c_jP_j.
\]

The perturbed denominator is

\[
D=2^{A+d_1+\cdots+d_e}-3^K=UP_e-Q.
\]

### 2. Exact 2-adic separation of the chain coefficients

Every accelerated state `z_j` is odd, so

\[
\nu_2(W_i)=A_{p_i+1}.
\]

These valuations strictly increase with `i`. Therefore, for `1<=i<e`, the two terms in

\[
c_i=W_i-W_{i+1}
\]

have distinct valuations, and the ultrametric rule gives

\[
\nu_2(c_i)=\nu_2(W_i)=A_{p_i+1}.
\]

The same identity is immediate for `c_e=W_e`. Thus

\[
\boxed{\nu_2(c_i)=A_{p_i+1}\quad(1\le i\le e).}
\]

### 3. One-variable Sylvester determinant and Bézout identity

For fixed `i`, separate the variable `X_i`:

\[
H=H_i^-+P_{i-1}X_iH_i^+,
\]

\[
D=UP_{i-1}X_iS_i-Q.
\]

As polynomials in `X_i`, the Sylvester determinant of these two linear forms is

\[
\operatorname{Res}_{X_i}(D,H)
=P_{i-1}(US_iH_i^-+QH_i^+)
=P_{i-1}E_i.
\]

More directly,

\[
\boxed{US_iH-H_i^+D=E_i.}
\]

The integer `D` is odd, while `US_i` is a power of two. Hence `gcd(D,US_i)=1`. The displayed identity proves both implications:

- `D|H` implies `D|E_i`;
- `D|E_i` implies `D|US_iH`, hence `D|H`.

This proves exact elimination.

### 4. The resultant cannot vanish on the dyadic pulse torus

Expand

\[
E_i=
US_i\sum_{j<i}c_jP_j
+
Q\sum_{j\ge i}c_j\prod_{h=i+1}^{j}X_h.
\]

In the second sum, the `j=i` term is `Qc_i`, with valuation

\[
\nu_2(Qc_i)=A_{p_i+1}.
\]

Every `j>i` term has valuation

\[
A_{p_j+1}+\sum_{h=i+1}^{j}d_h>A_{p_i+1}.
\]

Every term in the first sum contains `U=2^A` and a nonzero chain coefficient. Since `A>=A_{p_i+1}` and every `c_j` in that sum is even, each such term has valuation strictly larger than `A_{p_i+1}`.

Thus `Qc_i` is the unique term of minimum 2-adic valuation in `E_i`. A nonzero sum over a non-Archimedean field cannot have a unique minimum-valuation term cancel. Therefore

\[
\nu_2(E_i)=\nu_2(Qc_i)=A_{p_i+1},
\]

proving nonvanishing.

This is the local tropical certificate: a Laurent polynomial can vanish only where its minimum valuation is attained at least twice; here the Collatz prefix valuations force a unique minimizer.

### 5. Uniform cap on every pulse coordinate

Put

\[
R_i=\prod_{h\ne i}X_h=P_{i-1}S_i.
\]

Every monomial multiplying a coefficient in `E_i` divides `R_i`, and all `X_h>=2`. Hence

\[
|E_i|\le
\left(
U\sum_{j<i}|c_j|+Q\sum_{j\ge i}|c_j|
\right)R_i
=\Lambda_iR_i.
\]

Suppose `D>0` and `D|H`. Exact elimination gives `D|E_i`, and nonvanishing gives `E_i!=0`. Therefore

\[
UP_e-Q=D\le |E_i|\le\Lambda_iR_i.
\]

Since `P_e=X_iR_i`,

\[
UX_iR_i-Q\le\Lambda_iR_i,
\]

so

\[
X_i\le\frac{\Lambda_i}{U}+\frac{Q}{UR_i}.
\]

There are `e-1` other pulse variables and each is at least `2`, so `R_i>=2^{e-1}`. Taking the integer floor yields the claimed cap.

### 6. Finiteness of the whole fixed pulse cone

A word of length `K` has finitely many nonempty support subsets. For each support, the coordinate caps above leave finitely many powers of two `X_i=2^{d_i}`. Taking the finite union over supports proves the fixed-cone statement.

## Two-pulse consistency audit

For `e=2`, write `X_1=X`, `X_2=M` and let the second pulse be at gap `g`. The three chain coefficients share the exterior factor

\[
C=2^{a_0}3^{K-g-1}.
\]

With PR #51's notation,

\[
c_0=-C\alpha,\qquad c_1=C\gamma,\qquad c_2=C\beta.
\]

The two reduced resultants become

\[
E_1=C\{Q(\beta M+\gamma)-UM\alpha\}=C K(M),
\]

\[
E_2=C\{U(X\gamma-\alpha)+\beta Q\}=C J(X).
\]

Thus `L-8201` genuinely extends `L-8001`; it does not introduce a competing two-pulse formula.

## Dependency audit

1. The exact identity `C_b=z_0D_b+H_w(b)` and its pulse weights are the branch-qualified content of PR #47 `L-9602`.
2. All elimination, valuation, and cap arguments after that identity are proved here.
3. PR #51 `L-8001` is used only for the specialization audit.
4. Sparse-resultant and tropical sources motivate the representation but are not logical dependencies.

## Gap audit

This result does **not**:

- bound the repetition length of a negative-cycle packet;
- cover arbitrary valuation words not coordinatewise above a known negative cycle;
- show that any pulse vector is a nontrivial positive cycle;
- prove that the fixed-cone enumeration is computationally small;
- convert a finite cap into an infinite-orbit construction;
- establish a global novelty claim relative to all mathematical literature.

The strongest correct interpretation is:

> For each fixed negative cycle word, increasing pulse heights or adding more pulse positions cannot hide an unbounded resonance. Every possible positive-cycle divisibility hit lies in one explicit finite box.

## Adversarial tests

`X-8201` independently checks:

- the pulse cocycle against the direct affine numerator;
- every Sylvester determinant and Bézout identity;
- the divisibility equivalence for every coordinate;
- the exact 2-adic valuation of every resultant;
- the coefficient-norm cap;
- reduction to PR #51's `K/J` eliminants for two pulses;
- every formal positive divisor hit in the declared corpus.

The frozen corpus reports five formal hits; all are the trivial all-`2` word and reconstruct `n=1`.

## Remaining uncertainty

The proof has been checked twice in independent standard-library implementations but has not been reconstructed by a separate research agent. Its repository status therefore remains `PROPOSED`.

## Suggested next attack

1. Independently reconstruct `L-8201`, especially the exact indexing in `H_i^+` and the unique-minimum valuation argument.
2. Add a proof-producing all-support enumerator to the PR #47 / PR #51 cycle offense.
3. Combine the fixed-cone caps with commutator, `S`-unit, or primitive-divisor methods to seek a bound on the remaining infinite parameter: repetition length.
4. Test whether the same sparse-resultant pattern applies to mixed baseline macro-blocks rather than only upward pulses of one negative cycle.
