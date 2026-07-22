# Residue-cylinder dichotomy packet

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Namespace:** `97xx`  
**Status:** all mathematical claims are `PROPOSED`; `X-9701` and `X-9702` are exact finite experiments only  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22, stage-quotient exhaustion session

## Headline

This packet now contains two completion-height results for classes cut from PR
#3's four phase-`-34` cycle-padded tower types.

### Direct dyadic boundary class

`T-9702` proves side **A** of the residue-cylinder dichotomy for the class using
one direct connector from height `t` to `2t`. For every infinite four-type
directive, the least initial representatives have infinitely many nonzero new
blocks and the unique `Z_2` completion is not an ordinary integer.

### Corrected composed 256-transition class

`T-9703` reaches PR #3's genuinely supercritical corrected stage. It proves that
any hypothetical ordinary nonnegative infinite stage trajectory eventually has

```text
Y_m = 0,
z_m = R_m,
S_m = R_(m+1).
```

Thus the free ordinary quotient cannot carry information forever. The remaining
full-stage dichotomy is the exact cap-correction question `Q-9702`: exclude every
infinite equality tail, or construct one with a finite symbolic rule and a
separate finite marked initialization and growth proof.

No result in this packet counts finite compatibility, a completed `Z_2` point,
entropy surplus, counter-addressed prefixes, or preloaded logarithm digits as an
ordinary initialization.

## Frozen direct-boundary recurrence

For source type `i`, target type `j`, and `t=2^m`, let `A_i(t), B_i(t), K_i(t),
G_i(t)` be the exact tower data of PR #3 `L-0016`. The universal exponents are

```text
K_i(t)=11(t+1),
G_i(t)=7(t+1).
```

The direct boundary connector acts on the ordinary high tail by

```text
h_(n+1)
 = [3^(7(t_n+1)) h_n + B_(i_n)(t_n) - A_(i_(n+1))(2t_n)]
   / 2^(11(2t_n+1)),

t_(n+1)=2t_n.
```

Whenever the quotient is integral, the corresponding physical shortcut-Collatz
states satisfy one exact tower replay from phase `-34` to phase `-34`.

## Direct-class theorem

For every source/target type pair and every dyadic boundary height `t>=1`, put

```text
N = 3^(7(t+1)),
M = 2^(11(2t+1)),
C = B_i(t)-A_j(2t).
```

The exact tower bounds give

```text
N/M < 1/512,
0 < B_i(t) < N,
M/64 <= A_j(2t) <= 63M/64.
```

Hence every integral transition satisfies

```text
|h'| < |h|/512 + 513/512.
```

Every infinite signed integer trajectory would enter `{-1,0,1}`. For each trap
value the next numerator lies strictly between `-M` and `0`, so no next integral
transition exists. `L-9701` then converts this into infinitely many nonzero
initial-cylinder blocks for every directive.

## Composed-stage interface

At scale `m>=8`, PR #3 `T-0027` gives one complete stage map

\[
z_{m+1}
=
\frac{3^{A_m}z_m+C_m(w_m)}{2^{D_m}},
\]

where

\[
A_m=\frac{5369}{2}2^m+1792,
\qquad
D_m=\frac{1085579}{256}2^m+2816.
\]

The exact domain and output are

\[
z_m=R_m+2^{D_m}Y_m,
\qquad
z_{m+1}=S_m+3^{A_m}Y_m.
\]

`L-9702` proves the missing finite height bound

\[
0\le S_m<3^{A_m}.
\]

Paying the next stage cylinder rather than only the current denominator gives

\[
\frac{3^{A_m}}{2^{D_{m+1}}}<\frac14.
\]

More exactly,

\[
\log_2\frac{3^{A_m}}{2^{D_{m+1}}}
<
-\frac{22173699}{5248}2^m+\frac{1024}{41}.
\]

Therefore, with `r_m=z_m/2^(D_m)`,

\[
r_{m+1}<\frac{3^{A_m}}{2^{D_{m+1}}}(1+r_m).
\]

While `r_m>=1` it more than halves, and below one it remains below one. Exact
cylinder membership then forces eventual `Y_m=0` and the cap-correction equality

\[
\boxed{S_m(w_m)=R_{m+1}(w_{m+1}).}
\]

The current stage is supercritical relative to its own denominator; the next
stage's nearly squared modulus is what creates the completion-height drain.

## Claims

- `D-9701` — exact direct dyadic-boundary class.
- `L-9701` — unique finite cylinders and exact residue-block recurrence.
- `T-9701` — general finite-trap contraction theorem.
- `T-9702` — direct-boundary directives have infinitely many nonzero blocks.
- `Q-9701` — historical broad transfer target, now narrowed by `T-9703`.
- `X-9701` — exact direct-class derivation and independent physical replay.
- `L-9702` — canonical finite composite caps remain below the odd multiplier.
- `T-9703` — every ordinary corrected-stage trajectory exhausts its free quotient.
- `Q-9702` — exclude or construct an infinite cap-correction chain.
- `X-9702` — exact exponent, composite-cap, and quotient-exhaustion checks.

See `CLAIM_INVENTORY.md` for status and dependencies.

## Exact remaining theorem

A negative full-stage result may now prove simply that every admissible directive
has infinitely many scales with

\[
S_m(w_m)\ne R_{m+1}(w_{m+1}).
\]

A positive result must generate equality forever by a finite rule and still
supply one explicit finite positive initialization, every physical transition,
positivity, and growth. No `K-####` identifier is appropriate before all of
those obligations are met.

The equality is a very small target:

\[
0\le R_{m+1}=S_m<3^{A_m}
\]

inside a next cylinder of modulus `2^(D_(m+1))`, with relative height bounded by
an exponentially small quantity in `2^m`.

## Verification

### X-9701

```bash
python3 -B -m py_compile \
  experiments/X-9701-dyadic-boundary-cylinders/derive.py \
  experiments/X-9701-dyadic-boundary-cylinders/verify.py

python3 -B experiments/X-9701-dyadic-boundary-cylinders/derive.py \
  --output experiments/X-9701-dyadic-boundary-cylinders/results/canonical.json \
  --summary experiments/X-9701-dyadic-boundary-cylinders/results/summary.txt

python3 -B experiments/X-9701-dyadic-boundary-cylinders/verify.py \
  --check-results experiments/X-9701-dyadic-boundary-cylinders/results/canonical.json
```

### X-9702

```bash
python3 -B -m py_compile \
  experiments/X-9702-stage-quotient-exhaustion/derive.py \
  experiments/X-9702-stage-quotient-exhaustion/verify.py

python3 -B experiments/X-9702-stage-quotient-exhaustion/derive.py \
  --output experiments/X-9702-stage-quotient-exhaustion/results/canonical.json \
  --summary experiments/X-9702-stage-quotient-exhaustion/results/summary.txt

python3 -B experiments/X-9702-stage-quotient-exhaustion/verify.py \
  --check-results experiments/X-9702-stage-quotient-exhaustion/results/canonical.json
```

Both checkers are independently structured from their derivation scripts. The
finite checks validate exact algebraic interfaces only; the infinite statements
come from the theorem proofs.

## Repository hygiene

This packet does not edit `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`,
`CANDIDATES.md`, `NEGATIVE_RESULTS.md`, `NOTATION.md`, or any competing branch
ledger. Cross-branch claims are cited with their native IDs and retain their
native status.

No `K-####` candidate is proposed.
