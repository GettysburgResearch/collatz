# Session report — tower connectors and corrected 256-step Hensel stack

Date: 2026-07-21  
Agent: `gpt56-pro-01`  
Issue: `#2`  
Branch: `agent/gpt56-pro-01/2-collision-rewrite-bootstrap`  
Status: mathematical claims `PROPOSED`; experiment `EMPIRICAL`; no candidate counterexample

## Objective

Continue the first contributor packet beyond the finite-state regular-collapse
boundary. The immediate target was to determine whether the negative
-eleven-cycle padding counter can support an exact unbounded marked stack, and
to separate genuine all-height structure from another family of arbitrarily
deep finite cylinders.

## Inputs used

- `T-0015`: cycle-padded mismatch towers;
- `T-0020`: finite-phase regular marked grammars collapse to regular sanctuaries;
- PR #13 imported infrastructure, especially exact multiplicative-order/LTE,
  nondegenerate power-sum finiteness, and the finite-versus-completion warning;
- PR #11's valuation-fuel cautions, especially the deep-burn obstruction;
- the phase-`-34` self-return types of the negative eleven-cycle.

## Claims added

### `L-0016` — tower tail replacement

For each padded tower instance there are canonical finite blocks

\[
A_t<2^{K_t},
\qquad
B_t<3^{G_t}
\]

such that, for every ordinary finite high tail \(h\ge0\),

\[
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h.
\]

The finite core is periodic in the padding counter. The four phase-`-34`
self-return types have periods `16,8,4,2`.

### `L-0017` — universal connector tiles

Every ordered pair of phase-aligned tower instances has a unique canonical
binary seed \(\eta\) and nonnegative ternary cap \(\theta\) satisfying

\[
B+3^G\eta=\bar A+2^{\bar K}\theta.
\]

Hence

\[
\eta+2^{\bar K}z
\longmapsto
\theta+3^Gz
\]

for every \(z\ge0\). Every finite tower schedule therefore has infinitely many
ordinary finite realizations.

### `L-0018` — growing inverse-prefix obstruction

For odd \(a\),

\[
\operatorname{ord}_{2^K}(3^a)=2^{K-2}.
\]

The required inverse-power prefixes cannot be controlled by a fixed periodic
residue table as precision grows.

### `T-0021` — bounded-tail affine-counter obstruction

A finite library of fixed high tails together with finitely many affine counter
updates \(t'=ct+d\) can satisfy the exact connector equations at only finitely
many heights. The proof reduces an alleged infinite family to a nondegenerate
power-sum zero set and uses the imported Skolem–Mahler–Lech corollary.

### `L-0019` — nonlinear Hensel escalator

For the normalized connector prefix

\[
\omega_t=
\frac{\mu_t+3^{-g_t}}{2^{r+1}},
\]

the exact order-sized jump

\[
\Delta_H=2^{H+r-1}
\]

satisfies

\[
\omega_{t+\Delta_H}\equiv\omega_t\pmod{2^H}.
\]

This is the first genuine nonlinear all-height counter mechanism in the packet.

### `T-0022`, `L-0020`, `L-0021` — one-connector precursor

A 128-transition stage preserves a logarithmically growing immediate connector
prefix and has a seven-bit odometer. These claims remain correct, but are now
explicitly marked `PROPOSED / PRECURSOR`.

### Correctness correction — residual cost

The immediate connector high tail is not the residual stack after the next
connector has been parsed. The exact residual recurrence is

\[
z_{n+1}=
\frac{3^{G_n}z_n+\theta_n-\eta_{n+1}}{2^{K_{n+2}}}.
\]

Therefore the relevant slope is

\[
3^{G_n}/2^{K_{n+2}},
\]

not \(3^{G_n}/2^{K_{n+1}}\). The 128-step lane eventually falls below unit
residual slope after this second cylinder cost.

### `T-0023`, `L-0024` — corrected 256-step stage

The valid schedule is

\[
t_{m,j}=2^m+j2^{m-8},
\qquad0\le j\le256.
\]

At \(j=256\), the stage reaches scale \(m+1\). The connector-prefix valuation
has the exact eight-bit odometer law

\[
\nu_2(\omega_{m,j}-\omega_{m,0})
=m-r-7+\nu_2(j).
\]

### `O-0009` — explicit rational frontiers

The four stage-boundary frontiers are

\[
19/243,
\quad38/81,
\quad76/243,
\quad638/729,
\]

with exact binary periods `162,54,162,486`.

### `L-0023` — quadratic moving bulk

Put

\[
y_m=3^{-7\cdot2^m},
\qquad
u_m=\frac{y_m-1}{2^{m+2}}.
\]

Then

\[
u_{m+1}=u_m+2^{m+1}u_m^2.
\]

The complete stage-boundary prefix is a periodic rational frontier plus a
shifted copy of this one odd moving bulk word.

### `L-0025` — exact cycle-margin sandwich

The negative eleven-cycle bit margin satisfies

\[
\frac5{53}<7\log_2 3-11<\frac4{41},
\]

proved from exact integer-power comparisons rather than floating point.

### `T-0024` — full-stage information surplus

After paying the complete next-stage connector-precision increase, the corrected
256-transition stage retains more than

\[
\frac{20985}{6784}2^m>3\cdot2^m
\]

bits of rigorous residual capacity, apart from a fixed type constant.

This proves that information supply and real growth are not the remaining
bottleneck.

## Exact experiment

Experiment: `X-0012-tower-connector-stack`

Commands:

```bash
python3 -m py_compile experiments/X-0012-tower-connector-stack/run.py
python3 experiments/X-0012-tower-connector-stack/run.py
python3 -m py_compile experiments/X-0012-tower-connector-stack/stage.py
python3 experiments/X-0012-tower-connector-stack/stage.py
```

The scripts verify:

- all four finite core periods;
- exact binary-to-ternary replacement;
- 1,024 canonical connector families;
- direct two-block Collatz replay;
- growing multiplicative orders;
- Hensel prefix preservation;
- periodic rational frontiers;
- quadratic bulk recurrence;
- failure of the 128-step residual budget;
- success of the corrected 256-step residual budget;
- exact eight-bit odometer valuations;
- full-stage precision surplus.

Final output:

```text
all tower-connector-stack checks passed
all stage-boundary checks passed
```

## What was ruled out

1. Pairwise or finite connector failure is not the obstruction; connectors always
   exist.
2. Fixed periodic counter control cannot supply growing precision.
3. A finite high-tail library with affine counter updates cannot close at all
   heights.
4. The padding counter is a scale parameter, not the complete memory channel.
5. The 128-step one-connector lane does not regenerate the residual stack.
6. Positive bit-length surplus alone does not force the required next low bits.

## Current exact state

The preferred state is

\[
(i,m,j,W,z,n),
\]

where \(i\) is finite tower control, \(m\) the unbounded scale, \(j\) the
8-bit odometer, \(W\) the finite frontier/quadratic-bulk stack, \(z\) the
ordinary residual tail, and \(n\) the explicitly marked ordinary Collatz
integer.

## Remaining load-bearing theorem

Construct one finite 256-transition stage substitution that:

1. selects every connector cylinder exactly;
2. updates the periodic frontier and odometer by finite control;
3. implements
   \[
   u_{m+1}=u_m+2^{m+1}u_m^2;
   \]
4. uses the proved surplus to generate the newly required high bits forward;
5. keeps every residual division exact and nonnegative;
6. transports the marked ordinary integer through all deterministic Collatz
   blocks;
7. returns the same track types at scale \(m+1\);
8. starts from one finite configuration.

The principal open question is now `Q-0020`: route the full-stage surplus into
the exact next connector prefix, quadratic bulk, and residual congruence.

## Status

No positive integer is proposed. The new theorems and lemmas remain `PROPOSED`
pending independent reconstruction. The experiment is finite exact evidence and
not an infinite closure proof.