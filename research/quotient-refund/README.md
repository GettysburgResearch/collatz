# Linear-height quotient-refund packet

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#43`  
**Namespace:** `85xx`  
**Status:** theorem-level claims are `PROPOSED`; `X-8501`--`X-8506` are exact finite-interface audits

## Headline

The frozen doubling-scale architecture in PR #33 loses its ordinary quotient to the next complete radix. This packet changes the phase-`-34` height schedule to

\[
t_n=t_0+16n.
\]

For one connector,

\[
N_t=3^{7(t+1)},
\qquad
M_t=2^{11(t+17)}.
\]

At every multiple of `16` with `t>=3744`,

\[
\boxed{N_t/M_t>2^{177}.}
\]

The architecture is therefore locally and strongly refunded. More importantly, every connector inverse and every marked stage variable can be removed from the runtime state.

## 1. Causal connector and complement-counter forms

`L-8502` generates the canonical connector inverse from one finite ordinary Bezout carry

\[
Nr=1+Mc.
\]

Increasing `t` by `16` appends one exact base-`3^112` carry digit while the binary modulus gains `176` bits. No completed logarithm or inverse tape is initialized.

Put

\[
d=M-r,
\qquad
e=N-c.
\]

`L-8503` defines

\[
W_{t,i}(k)=b_id+Mk,
\qquad
W^+_{t,i}(k)=b_ie+Nk,
\]

and proves

\[
M W^+_{t,i}(k)=N W_{t,i}(k)+b_i,
\qquad
W_{t,i}(k)\equiv p_i\pmod{64},
\]

where

```text
p=(5,30,20,56),
b=(9,54,36,24).
```

The output residue selects the next type. `T-8504` gives one deterministic partial map on `(t,i,k)` and proves every legal update with `t>=3744`, `k>=256` satisfies

\[
\boxed{k_{n+1}\ge2k_n.}
\]

One state whose map is defined forever already gives an explicit positive unbounded shortcut-Collatz orbit.

## 2. Unimodular physical marker

`L-8504` proves

\[
\boxed{
\begin{pmatrix}M&d\\N&e\end{pmatrix}
\in\operatorname{SL}_2(\mathbb Z).}
\]

For consecutive ordinary boundary words `(W,U)`,

\[
\boxed{k=eW-dU,}
\qquad
\boxed{b_i=MU-NW.}
\]

The cone edges `N/M` and `e/d` are neighboring Farey fractions. Thus the complement counter is an intrinsic lattice coordinate, not hidden connector metadata.

For the physical boundary integer

\[
n=2^{11(t+1)}W/64-34,
\]

one has

\[
\boxed{\nu_2(n+34)=11t+5+i.}
\]

Because `16|t`, this valuation modulo `176` recovers the type and then the full height. The remaining odd boundary word recovers the ordinary counter. A verifier may begin with one written integer and reconstruct every mark.

## 3. Prime-to-six core

Write

```text
b_i=2^i 3^(beta_i),
beta=(2,3,2,1).
```

After the first boundary, define

\[
\boxed{
C_n=
\frac{W_n}{2^{i_n}3^{\beta_{i_{n-1}}}}.}
\]

This is exactly the prime-to-six part of `n_n+34`. `L-8505` turns one connector into

\[
\boxed{
2^{L_n}C_{n+1}=3^{G_n}C_n+1,}
\]

where

\[
L_n=11(t_n+17)+i_{n+1}-i_n,
\]

\[
G_n=7(t_n+1)+\beta_{i_{n-1}}-\beta_{i_n}.
\]

Consequently

\[
\nu_2(3^{G_n}C_n+1)=L_n,
\qquad
\gcd(C_n,C_{n+1})=1.
\]

`T-8506` proves

\[
\boxed{C_{n+1}>2^{170}C_n.}
\]

Every legal connector replaces the entire prime-to-six core by a coprime core more than 170 bits larger.

## 4. Intrinsic primitive-core decoder

`T-8507` gives the smallest runtime state:

```text
(height t,
 previous ternary signature gamma in {1,2,3},
 current binary type i in {0,1,2,3},
 one positive core C coprime to 6).
```

Set

\[
G=7(t+1)+\gamma-\beta_i,
\qquad
D=11(t+17)-i,
\]

and compute

\[
X=3^GC+1.
\]

The step is defined exactly when

\[
\boxed{2^D\mid X}
\]

and, with `Y=X/2^D`,

\[
\boxed{[3^{\beta_i}Y]_{64}\in\{5,30,20,56\}.}
\]

The six-bit value uniquely selects the next type `j`, and

\[
C'=Y/2^j.
\]

The next state is

\[
(t+16,\beta_i,j,C').
\]

The high divisibility automatically forces the current source cell. This runtime map contains no connector inverse, carry tape, target type, future directive, or completed `2`-adic address.

The associated physical integer is

\[
\boxed{
n=2^{11t+5+i}3^\gamma C-34.}
\]

Every defined core step is exactly `11(t+1)` shortcut-Collatz steps with `7(t+1)` odd steps.

## 5. Eight exact ordinary blocks

`L-8506` compiles each finite state `(t,gamma,i)` completely.

Let

\[
a=[-3^{-G}]_{2^D},
\qquad
h=(3^Ga+1)/2^D.
\]

For each target type `j`, the six-bit output condition gives one binary block modulo `2^(D+6)`. Enforcing `3`-primitivity splits that block into exactly two ternary lifts. Thus every finite state has exactly eight canonical ordinary source cylinders modulo

\[
3\cdot2^{D+6}.
\]

For each block there are explicit integers `Rhat_(j,nu)` and `Shat_(j,nu)` such that, for every `m>=0`,

\[
\boxed{
\widehat R_{j,\nu}+3\cdot2^{D+6}m
\longmapsto
\widehat S_{j,\nu}+3\cdot2^{6-j}3^Gm.}
\]

The same finite ordinary high tail is preserved, and every branch multiplier is greater than `2^170`.

Local branch existence and growth are therefore complete. The sole missing theorem is exact compatibility of one output block with a legal block at every later scale.

## 6. Complete counterexample criterion

One written positive integer whose intrinsic core decoder is defined forever is an unconditional Collatz counterexample. The packet already proves:

- exact reconstruction of height, type, ternary signature, and core from the integer;
- every physical transition and intermediate positivity;
- deterministic future type selection;
- complement-counter doubling;
- primitive-core growth by more than 170 bits per connector;
- unboundedness.

The sole positive gap is all-time recurrence of the high binary divisibility and six-bit output gate.

## 7. Necessary prime renewal

`T-8505` proves

\[
\gcd(W_n,W_{n+1})\mid b_{i_n}.
\]

After the exact powers of `2` and `3` are removed, consecutive cores are coprime integers greater than one. A fixed finite eventual prime support would yield infinitely many distinct primitive nondegenerate `S`-unit triples, contradicting Evertse's 1984 Corollary 1.

Therefore every fixed finite prime set is escaped infinitely often, and infinitely many globally new odd primes divide `n_n+34`.

A successful invariant cannot be a fixed-prime multiplicative library. It must manufacture a rapidly growing coprime core at every step and globally new prime content infinitely often.

## 8. Other structural filters

`T-8502` proves that compatible initial completions have Haar measure zero and `2`-adic Hausdorff dimension zero. At depth `N`, the directive exposes at most `2N` symbolic bits while exact continuation demands

\[
88N^2+(11t_0+275)N
\]

residue bits.

`T-8503` applies the fully inspected Väänänen–Wallisser theorem to the linear-grid completion series. Every eventually periodic local type tail of minimal period at most `58` is irrational and nonordinary; the source condition first fails at `59`.

A witness must therefore be an exceptional ordinary point generated by genuinely unbounded arithmetic state. Entropy, a short autonomous controller, a fixed-modulus lasso, and a fixed prime library do not supply it.

## Verification

Every `X-85xx` derivation has a separately written checker importing no derivation module.

```bash
python3 -B experiments/X-8501-linear-refund/derive.py \
  --output experiments/X-8501-linear-refund/results/canonical.json \
  --summary experiments/X-8501-linear-refund/results/summary.txt
python3 -B experiments/X-8501-linear-refund/verify.py \
  --check-results experiments/X-8501-linear-refund/results/canonical.json

python3 -B experiments/X-8502-complement-quotient/derive.py \
  --output experiments/X-8502-complement-quotient/results/canonical.json \
  --summary experiments/X-8502-complement-quotient/results/summary.txt
python3 -B experiments/X-8502-complement-quotient/verify.py \
  --check-results experiments/X-8502-complement-quotient/results/canonical.json

python3 -B experiments/X-8503-unimodular-physical-marker/derive.py \
  --output experiments/X-8503-unimodular-physical-marker/results/canonical.json \
  --summary experiments/X-8503-unimodular-physical-marker/results/summary.txt
python3 -B experiments/X-8503-unimodular-physical-marker/verify.py \
  experiments/X-8503-unimodular-physical-marker/results/canonical.json

python3 -B experiments/X-8504-primitive-core-turnover/derive.py \
  --output experiments/X-8504-primitive-core-turnover/results/canonical.json \
  --summary experiments/X-8504-primitive-core-turnover/results/summary.txt
python3 -B experiments/X-8504-primitive-core-turnover/verify.py \
  experiments/X-8504-primitive-core-turnover/results/canonical.json

python3 -B experiments/X-8505-intrinsic-core-decoder/derive.py \
  --output experiments/X-8505-intrinsic-core-decoder/results/canonical.json \
  --summary experiments/X-8505-intrinsic-core-decoder/results/summary.txt
python3 -B experiments/X-8505-intrinsic-core-decoder/verify.py \
  experiments/X-8505-intrinsic-core-decoder/results/canonical.json

python3 -B experiments/X-8506-core-block-compiler/derive.py \
  --output experiments/X-8506-core-block-compiler/results/canonical.json \
  --summary experiments/X-8506-core-block-compiler/results/summary.txt
python3 -B experiments/X-8506-core-block-compiler/verify.py \
  experiments/X-8506-core-block-compiler/results/canonical.json
```

## Review order

1. `D-8501-linear-connector-refund-class.md`
2. `L-8504-unimodular-physical-marker.md`
3. `L-8505-primitive-core-syracuse.md`
4. `T-8507-intrinsic-core-decoder.md`
5. `L-8506-core-block-replacement.md`
6. `T-8506-primitive-core-growth.md`
7. `T-8505-fresh-prime-turnover.md`
8. `L-8503-complement-quotient-normal-form.md`
9. `T-8504-single-counter-refund-map.md`
10. `L-8502-inverse-carry-connector-normal-form.md`
11. `L-8501-fixed-width-linear-refund.md`
12. `T-8502-quadratic-cylinder-pressure.md`
13. `T-8503-period-58-irrationality.md`
14. `Q-8501-infinite-defined-residual.md`
15. `experiments/X-8501-*` through `X-8506-*`

## Scope boundary

This packet is not a Collatz counterexample. It is an integer-first reduction that leaves one exact safety property open. A long valid prefix, zero-dimensional completion set, modular lasso, causal inverse carry, qualitative fresh-prime condition, rapidly growing core, or locally complete block compiler does not prove that one finite ordinary core survives forever.
