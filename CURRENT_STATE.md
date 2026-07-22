# Current integrated state

Last updated: 2026-07-22  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Status

There is currently **no positive-integer Collatz counterexample**, no regular sanctuary, and no closed infinite corrected-stage grammar in this branch.

All complete-looking mathematical claims remain `PROPOSED` pending independent reconstruction. Exact finite experiments are labeled `EMPIRICAL`; they are not substituted for proofs.

## Fixed map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

The branch contains a long exact finite theory of parity cylinders, collision fibers, mixed-radix rewrites, negative return phases, interval/particle marker semantics, and cycle-padded negative towers. `CLAIMS.md` is the detailed index.

# What is already supplied

The packet has proposed exact results providing:

- sparse and consecutive supercritical collision fibers;
- inverse-signature collision codes with unbounded branch count;
- arbitrary finite correction precision and complete dyadic projection;
- exact mixed-radix carry transducers;
- graph-directed return and pressure criteria;
- ordinary finite-interval and marked-particle semantics;
- the regular-collapse boundary of `T-0020`;
- exact phase-34 tower blocks and canonical connectors;
- Newton/Montgomery generation of every finite connector word;
- a padding-counter isometry and adaptive 512-cell prefix router;
- lossless compression of one corrected 256-transition stage;
- strict extinction of the free stage quotient.

These resources remove finite compatibility, branch count, connector generation, and raw growth as mysteries. They do not supply one infinite ordinary marked path.

# Exact corrected-stage frontier

For the four phase-34 tower types,

\[
K_t=11(t+1),
\qquad
G_t=7(t+1).
\]

One corrected stage is

\[
z^+={3^{A_m}z+C_m\over2^{D_m}},
\]

\[
A_m={5369\over2}2^m+1792,
\qquad
D_m={1085579\over256}2^m+2816.
\]

Writing its canonical correction and cap as `R_m,S_m`, every stage input/output is

\[
z_m=R_m+2^{D_m}Y_m,
\]

\[
z_m^+=S_m+3^{A_m}Y_m.
\]

`T-0031` proves

\[
0\le Y_{m+1}<\frac{Y_m+3}{512}.
\]

Therefore every ordinary infinite realization eventually has `Y_m=0` and must obey

\[
\boxed{S_m(w_m)=R_{m+1}(w_{m+1})}
\]

at every sufficiently late scale.

# Literature wave 5 synthesis

This session read PR #13 `LITERATURE.md`, `LIVE_REPO_REVIEW_WAVE5.md`, and the newest `gpt56-pro-03` review comment. It also incorporated PR #34's two-cell collar, 84-triple cascade, and 1024-state first-seam graph.

The literature checklist required:

1. one fixed finite equation;
2. an explicit finite-rank group;
3. distinct scale solutions;
4. a complete proper-subsum audit;
5. finite-alphabet recurrence;
6. an explicit ordinary-integer contradiction.

# New hidden coordinate: the scaled ordinary tail

For the stabilized types, put

```text
p = (5,30,20,56)
b = (9,54,36,24).
```

For an ordinary high tail `h_j`, define

\[
W_j=p_{i_j}+64h_j.
\]

`L-0031` proves the exact local recurrence

\[
\boxed{
2^{11(t_{j+1}+1)}W_{j+1}
=
3^{7(t_j+1)}W_j+b_{i_j}.}
\]

All connector seeds, caps, and residual offsets telescope. One corrected stage is the positive 257-term equation

\[
2^{\mathcal E_m}W_{m+1}
=
3^{\mathcal A_m}W_m
+
\sum_{k=0}^{255}
2^{U_{m,k}+\alpha_{i_k}}
3^{V_{m,k}+\beta_{i_k}},
\]

where

\[
\mathcal A_m={5369\over2}2^m+1792,
\qquad
\mathcal E_m={8459\over2}2^m+2816.
\]

The tolls `9,54,36,24` are themselves `{2,3}`-units.

## Fresh-prime necessity

`T-0032` applies PR #13 `LIT-KTHM-0043` under a contradiction hypothesis of finite endpoint prime support. Positivity resolves every proper subsum, and a toll-coordinate ratio separates the scales.

Therefore every infinite ordinary corrected-stage path must introduce infinitely many fresh prime factors. Fixed-prime monomial and finite-library multiplicative schemas are excluded.

# One fixed real room

Define

\[
a_m={5369\over2}2^m+1792m,
\qquad
e_m={8459\over2}2^m+2816m,
\]

\[
H_m={3^{a_m}\over2^{e_m}}.
\]

`T-0033` proves that every assumed infinite ordinary path has one real number `C_infinity` with

\[
\boxed{W_m=\lfloor C_\infty H_m\rfloor}
\]

and

\[
0<\{C_\infty H_m\}
<{216\over3^{7(2^m+1)}}.
\]

The path is one fixed-room orbit hitting doubly-exponentially shrinking positive targets.

# Exact real/dyadic connector bridge

After quotient extinction,

\[
W_m=X_m+64T_m^{\rm head}R_m,
\]

where `X_m` is the complete scaled first-connector word. Define

\[
J_m={H_m\over64T_m^{\rm head}}
={3^{a_m}\over2^{f_m}},
\]

\[
f_m={1085579\over256}2^m+2816m+17.
\]

`T-0034` gives

\[
\boxed{R_m=\lfloor C_\infty J_m\rfloor}
\]

and

\[
\boxed{
\{C_\infty J_m\}
={X_m\over64T_m^{\rm head}}
+{\varepsilon_m\over64T_m^{\rm head}},}
\]

where the second term is positive and doubly-exponentially tiny.

The real room orbit must land immediately above the exact normalized binary connector address.

Moreover

\[
\log_2R_m=\Gamma2^m+O(m),
\]

\[
\Gamma={687232\log_2 3-1085579\over256}>0.
\]

The old information-surplus coefficient is the actual ordinary completion-height slope of the canonical correction.

# All-boundary room coding

`T-0036` extends the same room through every local connector boundary. For explicit scales `H_(m,j)` and `J_(m,j)`,

\[
W_{m,j}=\lfloor C_\infty H_{m,j}\rfloor,
\]

\[
z_{m,j}=\lfloor C_\infty J_{m,j}\rfloor.
\]

The type sequence is no longer an independent word:

\[
\boxed{
i_{m,j}=p^{-1}(W_{m,j}\bmod64).}
\]

Conditional on PR #34 `L-9893`, every triple correction and cap is one floor of this same room. The 1024-state seam graph is the low-bit projection of one real floor orbit.

# Boundary valuation signatures

`L-0032` proves

\[
v_2(W_n)=\alpha_{i_n}\in\{0,1,2,3\},
\]

\[
v_3(W_{n+1})=\beta_{i_n}\in\{1,2,3\}.
\]

The tower types are exact ordinary adelic signatures. The fresh primes forced by `T-0032` must lie outside `{2,3}`.

# Two-place approximation threshold

`O-0011` proves natively that the reduced room approximants `P_m/Q_m` satisfy

\[
\left|C_\infty-{P_m\over Q_m}\right|
|P_m|_2|Q_m|_3
<
H(P_m,Q_m)^{-2-1/1024}
\]

for every sufficiently large scale.

This crosses the standard two-place Roth/Ridout threshold. A source-qualified Ridout import has been requested from PR #13. Conditional on the expected theorem normalization, the room cannot be algebraic irrational; it must be rational or transcendental.

The conditional corollary is not yet an unconditional repository theorem.

# Quadratic-generator restriction

The positive quadratic word

\[
V_m={3^{7\cdot2^m}-1\over2^{m+2}}
\]

cannot be the canonical correction through any fixed rational polynomial in finitely many shifts. `T-0035` proves a height nonresonance; for fixed affine transforms,

\[
\Gamma-7\log_2 3>{41273\over13568}>3.
\]

A viable constructive use of `V_m` needs an additional exponentially large binary renormalization channel.

# Exact verification

`X-0016` contains exact standard-library audits for:

- stabilized anchor formulas;
- actual canonical connector chains;
- scaled-tail telescoping;
- stage exponent sums and scale injection;
- fixed-room and floor identities;
- the room--connector bridge;
- height nonresonance;
- binary/ternary valuation signatures;
- the native two-place exponent.

The exact assertions were replayed in the available Python environment during the authoring session. The checked-in scripts are the reproducibility interface.

# Current load-bearing frontier

A hypothetical ordinary path must satisfy simultaneously:

1. exact cap-to-correction stitching;
2. PR #34's collar and 84 triple-seam constraints;
3. one fixed real room generating every floor and every type;
4. exact dyadic connector addresses with tiny positive room error;
5. infinitely many fresh primes outside `{2,3}`;
6. one explicit finite marked Collatz initialization.

The primary next targets are:

- couple PR #34's nonautonomous odd-radix seam carry to the room defect;
- derive an S-arithmetic product-formula obstruction;
- decide whether bridge-compatible fresh-prime creation is possible;
- test a properly renormalized quadratic generator against one exact collar seam.
