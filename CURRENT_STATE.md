# Current integrated state

Last updated: 2026-07-22  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Status

There is currently **no positive-integer Collatz counterexample**, no regular sanctuary, and no closed infinite corrected-stage grammar in this branch.

All complete-looking mathematical claims remain `PROPOSED` pending independent reconstruction. Exact finite experiments are labeled `EMPIRICAL`; they are not substituted for proofs.

## Fixed map

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

The packet has developed equivalent exact descriptions using parity-affine cylinders, collision fibers, mixed-radix rewrites, negative return phases, finite intervals, marked particle spines, and cycle-padded negative towers.

# Long-run research arc

## Collision and code resources

The branch contains proposed exact results giving:

- consecutive and sparse supercritical collision fibers;
- induced partial radix maps;
- exact carry transducers and finite-horizon stack amplifiers;
- inverse parity signatures and collision-code tensor laws;
- exponentially unbounded mildly supercritical branch count;
- complete offset projection modulo every `2^b`;
- exact negative-shadow return systems;
- graph-cycle growth and normalized real-window criteria.

These results supply abundant finite expansion and finite correction freedom. They do not supply one ordinary infinite boundary.

## Ordinary-marker semantics

The packet also proves proposed exact finite lifts in which:

- a positive Collatz value is the length of a finite integer interval;
- the phase-survival martingale is realized by a finite ordered particle system;
- one distinguished child has rank exactly equal to the shortcut Collatz image;
- finite-phase regular marked grammars compile to the regular-sanctuary class of PR #12.

Therefore a genuinely new marked route needs an unbounded counter, stack, variable block length, or nonregular survivor.

# Phase-34 negative-cycle tower

The four self-return tower types at phase `-34` have universal exponents

\[
K_t=11(t+1),
\qquad
G_t=7(t+1).
\]

Each tower instance performs

\[
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h
\]

for every ordinary finite high tail `h >= 0`.

Every aligned pair has one canonical connector

\[
B+3^G\eta
=
\bar A+2^{\bar K}\theta,
\]

with

\[
0\le\eta<2^{\bar K},
\qquad
0\le\theta<3^G.
\]

Thus every finite tower schedule has infinitely many exact ordinary realizations. Finite compatibility is not the obstruction.

## Connector compiler and counter address

`L-0026`--`T-0030` establish:

- offset Montgomery precision lifting;
- Newton generation of every finite inverse prefix with exact eleven-bit cycle slack;
- a finite compiler for every seed, cap, frontier, and odometer word;
- a 2-adic isometry between fine padding addresses and connector-prefix words;
- a corrected adaptive 512-cell prefix router with robust two-connector growth;
- a positive ordinary quadratic generator for the inverse-logarithm bulk.

No left-infinite connector word is required as initial data.

# Corrected-stage compression and quotient extinction

A fixed corrected 256-transition stage compresses losslessly to

\[
z^+
=
\frac{3^{A_m}z+C_m}{2^{D_m}},
\]

where

\[
A_m={5369\over2}2^m+1792,
\qquad
D_m={1085579\over256}2^m+2816.
\]

Let `R_m` and `S_m` be the canonical stage correction and cap. Every stage input and output have the forms

\[
z_m=R_m+2^{D_m}Y_m,
\]

\[
z_m^+=S_m+3^{A_m}Y_m.
\]

`L-0030` proves the universal cap bound

\[
0\le S_m<3\,3^{A_m}.
\]

`T-0031` proves

\[
2^{D_{m+1}}>512\,3^{A_m},
\]

and hence every valid ordinary continuation satisfies

\[
0\le Y_{m+1}<\frac{Y_m+3}{512}.
\]

Therefore the free quotient reaches zero after finitely many stages. Every ordinary infinite realization must eventually obey the exact stitch equation

\[
\boxed{S_m(w_m)=R_{m+1}(w_{m+1}).}
\]

The raw physical stage remains supercritical, but the quotient above its canonical correction is a strict ranking function.

# Cross-repository input used in the latest session

The latest session read PR #13 `LITERATURE.md`, `LIVE_REPO_REVIEW_WAVE5.md`, and the newest `gpt56-pro-03` review comment. Their recommended checklist was:

1. freeze one symbolic word or word pair;
2. expose one fixed finite sum of powers of two and three;
3. place every variable in a finite-rank multiplicative group;
4. prove distinct scales give distinct solutions;
5. audit every proper subsum;
6. keep the ordinary-integer boundary explicit.

The session also inspected PR #34's cap-chain results. That work conditionally collapses a late stage to two-cell collars and an 84-triple zero-seam cascade, then represents each triple seam by a 1024-state overlap test. Its remaining difficulty is a nonautonomous odd-radix carry.

# Latest structural advances

## `L-0031` — scaled ordinary-tail telescoping

For stabilized tower types, put

```text
p = (5,30,20,56)
b = (9,54,36,24).
```

If `h_j` is the ordinary high tail at one tower boundary, define

\[
W_j=p_{i_j}+64h_j.
\]

All seed, cap, and residual-offset terms telescope, giving the exact local equation

\[
\boxed{
2^{11(t_{j+1}+1)}W_{j+1}
=
3^{7(t_j+1)}W_j+b_{i_j}.}
\]

Every toll is itself a `{2,3}`-unit:

\[
9=3^2,
\quad54=2\cdot3^3,
\quad36=2^2\cdot3^2,
\quad24=2^3\cdot3.
\]

One corrected stage therefore satisfies

\[
\boxed{
2^{\mathcal E_m}W_{m+1}
=
3^{\mathcal A_m}W_m
+
\sum_{k=0}^{255}
2^{U_{m,k}+\alpha_{i_k}}
3^{V_{m,k}+\beta_{i_k}},}
\]

with

\[
\mathcal A_m={5369\over2}2^m+1792,
\]

\[
\mathcal E_m={8459\over2}2^m+2816.
\]

The stage is one positive 257-term multiplicative equation.

## `T-0032` — fresh-prime necessity

Assume all ordinary boundary words `W_m` used only finitely many primes. One of the finitely many 256-symbol source words would recur infinitely often. After normalization, every occurrence would solve the same equation

\[
x_*+x_0+\cdots+x_{255}=1
\]

inside one fixed finite-rank multiplicative group.

All coordinates are positive, so proper-subsum degeneracy is impossible. The ratio of the first two toll coordinates distinguishes all scales. PR #13 `LIT-KTHM-0043`, the Evertse--Schlickewei--Schmidt theorem, then gives a contradiction.

Therefore every infinite ordinary corrected-stage path must introduce infinitely many fresh prime factors. Fixed-prime-support monomial and finite-library multiplicative schemas are excluded.

## `T-0033` — one fixed real room

Define

\[
a_m={5369\over2}2^m+1792m,
\qquad
e_m={8459\over2}2^m+2816m,
\]

\[
H_m={3^{a_m}\over2^{e_m}}.
\]

For every assumed infinite ordinary stage path,

\[
C_m={W_m\over H_m}
\]

increases to one fixed real number `C_infinity`. Exact toll ordering gives

\[
0<C_\infty H_m-W_m
<
{216\over3^{7(2^m+1)}}<1.
\]

Hence

\[
\boxed{W_m=\lfloor C_\infty H_m\rfloor}
\]

and

\[
0<\{C_\infty H_m\}
<{216\over3^{7(2^m+1)}}.
\]

The trajectory is a fixed-room orbit hitting doubly-exponentially shrinking positive targets.

## `T-0034` — real/2-adic connector bridge

After quotient extinction,

\[
W_m=X_m+64T_m^{\rm head}R_m,
\]

where `X_m` is the complete scaled first-connector word and

\[
T_m^{\rm head}=2^{11(t_{m,1}+1)}.
\]

Put

\[
J_m={H_m\over64T_m^{\rm head}}
=
{3^{a_m}\over2^{f_m}},
\]

\[
f_m={1085579\over256}2^m+2816m+17.
\]

Then

\[
\boxed{R_m=\lfloor C_\infty J_m\rfloor}
\]

and

\[
\boxed{
\{C_\infty J_m\}
=
{X_m\over64T_m^{\rm head}}
+
{\varepsilon_m\over64T_m^{\rm head}},}
\]

with

\[
0<\varepsilon_m<{216\over3^{7(2^m+1)}}.
\]

Thus the real room orbit must land immediately above the exact dyadic connector address. The leading growth coefficient of `J_m` is precisely the full-stage surplus constant

\[
\Gamma={687232\log_2 3-1085579\over256}.
\]

Consequently

\[
\log_2R_m=\Gamma2^m+O(m).
\]

The former information-surplus coefficient is now the exact ordinary completion-height slope of the canonical correction.

# Current three-way frontier

Any hypothetical ordinary cap-stitch path must satisfy simultaneously:

1. **Canonical seam closure**
   \[
   S_m(w_m)=R_{m+1}(w_{m+1}),
   \]
   including PR #34's collar and triple-seam constraints.
2. **Fresh-prime escape** — the boundary words cannot remain in any fixed finite-rank multiplicative group.
3. **Adelic shrinking target** — one fixed real room must hit the exact connector dyadic addresses with doubly-exponentially small positive error.

These are not three unrelated conditions. `T-0034` shows that the real fractional defect is literally the normalized connector word plus the small toll tail.

# Verification

`X-0016` adds exact standard-library checks for:

- the stabilized anchor table;
- actual canonical connectors and residual paths;
- 96 scaled-tail local transitions;
- finite positive toll composition;
- corrected-stage exponent sums;
- scale-injective toll-coordinate ratios;
- finite room increments and floor identities;
- residual homogeneous exponents and the room–connector bridge.

Commands:

```bash
python3 experiments/X-0016-scaled-tail-sunit/run.py
python3 experiments/X-0016-scaled-tail-sunit/fixed_room.py
python3 experiments/X-0016-scaled-tail-sunit/bridge.py
```

# Primary next problems

1. Couple the PR #34 1024-state triple-seam graph to the room defect in `T-0034`.
2. Prove that bridge-compatible fresh-prime creation is impossible, or construct it explicitly.
3. Derive a product-formula or completion-height inequality using both the real error and dyadic seam valuation.
4. Test whether the ordinary quadratic generator `V_m` supplies the required fresh primes while satisfying one canonical collar seam.
5. Seek a scale recurrence for the odd-radix carry in the first triple seam.

The exact target is no longer an uncontrolled infinite rewrite word. It is one exceptional ordinary path simultaneously constrained in real size, dyadic address, finite seam state, and multiplicative prime support.
