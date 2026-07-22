# Residue-cylinder dichotomy packet

**Agent:** `gpt56-cylinder-01`  
**Issue:** `#31`  
**Namespace:** `97xx`  
**Status:** all mathematical claims are `PROPOSED`; experiments are exact finite checks only  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22, cap-chain height-collapse session

## Headline

This packet now contains three completion-height results for classes cut from PR
#3's four phase-`-34` cycle-padded tower types.

### 1. Direct dyadic boundary class

`T-9702` proves side **A** of the residue-cylinder dichotomy for the class using
one direct connector from height `t` to `2t`. For every infinite four-type
directive, the least initial representatives have infinitely many nonzero new
blocks and the unique `Z_2` completion is not an ordinary integer.

### 2. Corrected composed 256-transition class

`T-9703` reaches PR #3's genuinely supercritical corrected stage. Any
hypothetical ordinary nonnegative infinite stage trajectory eventually has

```text
Y_m = 0,
z_m = R_m,
S_m = R_(m+1).
```

Thus the free ordinary quotient cannot carry information forever. The full-stage
question becomes the exact cap-correction equality.

### 3. Global height collapse on the cap chain

`L-9703` proves the type-word-uniform normalized offset bound

```text
|beta_m| < 256 Lambda_m.
```

`T-9704` then proves that every surviving cap-correction chain satisfies

```text
limsup log_2(R_m+257)/D_m
 <= 161341/44508739
 < 1/275.
```

The ordinary correction therefore uses asymptotically less than `0.363%` of its
complete cylinder precision. The remaining negative target is no longer a
generic routing problem: it is an exceptionally strong structured p-adic
approximation or product-formula problem.

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
transition exists. `L-9701` converts this into infinitely many nonzero
initial-cylinder blocks for every directive.

## Composed-stage interface and quotient exhaustion

At scale `m>=8`, PR #3 `T-0027` gives

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

`L-9702` proves

\[
0\le S_m<3^{A_m}.
\]

Paying the next complete stage cylinder gives

\[
\frac{3^{A_m}}{2^{D_{m+1}}}<\frac14,
\]

more exactly

\[
\log_2\frac{3^{A_m}}{2^{D_{m+1}}}
<
-\frac{22173699}{5248}2^m+rac{1024}{41}.
\]

With `r_m=z_m/2^(D_m)`,

\[
r_{m+1}<rac{3^{A_m}}{2^{D_{m+1}}}(1+r_m).
\]

While `r_m>=1` it more than halves; below one it stays below one. Exact
membership forces eventual

\[
\boxed{S_m(w_m)=R_{m+1}(w_{m+1}),
\qquad Y_m=0.}
\]

The current stage is supercritical relative to its own denominator; the next
stage's nearly squared modulus creates the completion-height drain.

## Cap-chain offset and global height

Write one complete stage as

\[
z_{m+1}=\Lambda_mz_m+\beta_m,
\qquad
\Lambda_m=3^{A_m}/2^{D_m}.
\]

`L-9703` proves every local corrected-stage slope exceeds one and

\[
|\beta_m|<256\Lambda_m.
\]

On a cap-correction chain,

\[
R_{m+1}=\Lambda_mR_m+\beta_m.
\]

Since `Lambda_m>257`,

\[
R_{m+1}+257<\Lambda_m(R_m+257).
\]

The exact upper bound `log_2 3<65/41` gives

\[
\log_2\Lambda_m
<
\frac{161341}{10496}2^m+rac{1024}{41}.
\]

Consequently, for a chain beginning at `M`,

\[
\log_2(R_m+257)
<
\log_2(R_M+257)
+rac{161341}{10496}(2^m-2^M)
+rac{1024}{41}(m-M).
\]

Against `D_m`, this yields

\[
\boxed{
\limsup
\frac{\log_2(R_m+257)}{D_m}
\le
\frac{161341}{44508739}<\frac1{275}.}
\]

This is a height budget, not nonexistence. A closing theorem must identify the
structured nonzero p-adic numerator, logarithmic form, or algebraic approximant
whose valuation is forced by the cap chain.

## Claims

- `D-9701` — exact direct dyadic-boundary class.
- `L-9701` — unique finite cylinders and exact residue-block recurrence.
- `T-9701` — general finite-trap contraction theorem.
- `T-9702` — direct-boundary directives have infinitely many nonzero blocks.
- `Q-9701` — historical broad transfer target, now narrowed.
- `X-9701` — exact direct-class derivation and independent physical replay.
- `L-9702` — canonical finite composite caps remain below the odd multiplier.
- `T-9703` — every ordinary corrected-stage trajectory exhausts its free quotient.
- `Q-9702` — exclude or construct an infinite cap-correction chain.
- `X-9702` — exact exponent, composite-cap, and quotient-exhaustion checks.
- `L-9703` — type-uniform normalized stage-offset bound.
- `T-9704` — factor-greater-than-275 cap-chain height collapse.
- `X-9703` — exact expanding-offset and cap-chain height checks.

See `CLAIM_INVENTORY.md` for status and dependencies.

## Exact remaining theorem

A negative full-stage result must prove that every admissible directive has
infinitely many scales with

\[
S_m(w_m)\ne R_{m+1}(w_{m+1}).
\]

The strongest current route is to express each fixed normalized stage word's
correction equation as a finite p-adic exponential/logarithmic form and combine
a uniform lower bound with the factor-275 height gap.

A positive result must generate equality forever by a finite rule and still
supply one explicit finite positive initialization, every physical transition,
positivity, and growth. No `K-####` identifier is appropriate before all of
those obligations are met.

## Verification

Run `X-9701`, `X-9702`, and `X-9703` from the repository root using the commands
in their experiment READMEs. Each experiment has a separately written checker
that does not import its derivation module.

`X-9703` freezes:

```text
stage coefficient rows: 25
expanding composite chains: 82082
independent expanding chains: 11403
artificial cap steps: 224
independent cap steps: 162
asymptotic height ratio: 161341/44508739
payload digest: 7131a6e74497002b4edd008deb4c3ff3adf5072b33995b21e88d13bd8f5d30b5
all independent cap-chain height checks passed
```

Finite checks validate exact algebraic interfaces only; the infinite statements
come from the theorem proofs.

## Repository hygiene

This packet does not edit `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`,
`CANDIDATES.md`, `NEGATIVE_RESULTS.md`, `NOTATION.md`, or any competing branch
ledger. Cross-branch claims are cited with their native IDs and retain their
native status.

No `K-####` candidate is proposed.
