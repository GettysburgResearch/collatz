# Integer-first counterexample offense — two pulses, five defects, and an exact block chart

**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Branch:** `agent/gpt56-pulse-01/46-two-pulse-offense`  
**Date:** 2026-07-22

## Executive result

I did not find a full unconditional Collatz counterexample.

The pass nevertheless advanced the finite-cycle offense in three exact ways:

1. every two-pulse perturbation of a repeated known negative cycle now has a
   two-variable reduction with two nonzero determinant eliminants and finite
   all-pulse caps;
2. the all-size and distributed-pulse searches tested `40,638,351` exact
   candidates with no nontrivial hit; and
3. the centered sparse-cycle frontier moved by one full theorem:

   ```text
   no nontrivial positive accelerated cycle has exactly five non-2 valuations.
   ```

A fourth result keeps the constructive objective alive: pulsing the first
valuation of a negative cycle produces an exact partial integer block chart.
An all-time ordinary path in that chart would itself be a complete
counterexample certificate.

## 1. Repository delta read before the attack

PR #47 had just reduced every single-pulse perturbation of the negative
three- and eleven-cycles to one small divisibility condition and scanned
repetitions through `20,000`.  PR #34 had independently centered cycle words
at the trivial fixed point and excluded all words with at most four
valuations different from `2`.

The natural next offensive targets were therefore:

- more than one pulse around a negative cycle; and
- the first unclosed centered sparse family, exactly five defects.

I claimed issue #46 as an explicitly independent attempt and reserved the
isolated `80xx` namespace.

## 2. `L-8001`: exact two-pulse formula

For a repeated negative word with

```text
N=kr,
U=2^(Ar),
Q=3^N,
```

rotate the two pulses so the first is at zero and the second is at the shorter
cyclic gap `g<=N/2`.  With pulse powers `X=2^d1`, `M=2^d2`, define

```text
alpha=(-z_1)3^g,
beta=(-z_(g+1))2^S,
gamma=alpha-beta>0.
```

The full denominator and reduced numerator are

```text
D=UXM-Q,
R=X(beta M+gamma)-alpha.
```

The fixed numerator is

```text
C'=z_0D+2^a0 3^(N-g-1) R,
```

so `D|C'` is exactly `D|R`.

Two determinant identities eliminate either pulse variable:

```text
UMR-(beta M+gamma)D
  =Q(beta M+gamma)-UM alpha
  =K(M),

UXR-beta X D
  =X{U(X gamma-alpha)+beta Q}
  =XJ(X).
```

Both are nonzero for structural reasons:

- `K(M)` is odd;
- `J(X)` has a uniquely lower `2`-adic term `beta Q`.

Therefore each fixed repetition/rotation/gap has finite exact bounds for **all**
pulse sizes, not only near-threshold pulses.

## 3. `X-8001`: all two-pulse sizes

The exact caps were exhausted at:

```text
negative three-cycle:  r<=50, all pulse sizes
negative eleven-cycle: r<=20, all pulse sizes
```

and a separate long scan covered the multiplier threshold and next three
totals through `r=5000`.

```text
formula audits:                         2,432
all-size reduced candidates:       16,445,391
near-threshold reduced candidates:        168
nontrivial hits:                            0
```

The only hit is the trivial word

```text
(1,2)^2 -> (2,2)^2,
n=1.
```

Frozen digest:

```text
57b6f1217221142269f3331805f8f479450ed442c8c2e34d075c63f5849ea724
```

## 4. `X-8002`: three and four distributed pulses

The next search did not assume two pulses.  It placed one pulse at zero by
rotation and scanned every later position set and every positive pulse
composition at the threshold total plus three.

```text
negative three-cycle, 3 pulses, r<=50: 17,045,448
negative three-cycle, 4 pulses, r<=20:  2,298,920
negative eleven-cycle, 3 pulses, r<=20: 4,396,770
negative eleven-cycle, 4 pulses, r<=8:    451,822
-------------------------------------------------
total:                                  24,192,960
nontrivial hits:                                 0
```

The two hits are exactly the trivial `n=1` all-`2` words obtained by pulsing
every `1` in `(1,2)^3` and `(1,2)^4`.

Frozen digest:

```text
722890b0566d266126601a3a2193ec69e6b1ec296607d94a086c8d196479f0ff
```

This does not extrapolate beyond the frozen ranges.  It does show that simply
distributing the smallest multiplier-correcting pulse among three or four
locations does not reveal an easy positive cycle in the first exact windows.

## 5. `T-8001`: the fifth centered defect is impossible

Centering at `1` gives

```text
E=C-D=sum_j 3^(k-1-j)2^A_j(4-2^a_j).
```

Valuations `2` vanish.  A nontrivial positive cycle requires

```text
D>0,
D|E,
E>=2D.
```

The exactly-five-defect proof splits by the number of high defects `a>=3`.

### At least two high defects

Delete all neutral `2`s and lower every high defect to `3`.  The resulting
`{1,3}^5` map is a contraction.  An exact cyclic table shows that every
necklace has a rotation whose fixed centered value is below `2`, contradicting
the positive even centered state of the original cycle.

### Exactly one high defect

Rotate a largest neutral gap to the tail.  If the total neutral count is
`R>=6`, a sharp positive-part estimate gives `E_core<2D`.

For `R<=5`, write `x=2^b`.  Every frozen pattern has

```text
E_core=P x+S,
D=L x-Q,
L E_core-PD=LS+PQ=K.
```

No `K` vanishes.  Hence `D|E_core` implies `D<=|K|`, which gives a finite exact
power cap.

### All five defects equal one

Positive drift begins at `R=8`.  A largest-gap estimate excludes every
`R>=10`; the complete `R=8,9` tables fail the height gate before divisibility.

### Frozen finite certificate

```text
modified-core necklaces:             6
all-one arrangements:              290
one-high patterns:                 345
one-high determinant resonances:     0
one-high powers tested:           3,347
height survivors:                   53
exact divisor hits:                  0
```

An independently written verifier reconstructs the one-high coefficients by
interpolation rather than the builder's symbolic bookkeeping.

Frozen digest:

```text
1d277736a3570ec64dae6884b175e807b457e89729b75ce25893fc008760d6b0
```

## 6. Positive construction retained: `O-8001`

For the negative three-cycle, block centering yields the exact partial map

```text
h=8q       -> 9q,
h=3+16q    -> 3+9q,
```

where physical `n=-5+2h`.  The fixed `h=3` is `n=1`; any other all-time
positive path is a genuine counterexample, either periodic or unbounded.

For the negative eleven-cycle, each rotation has

```text
h=2048q          -> 2187q,
h=rho_z+4096q    -> 729+2187q,
```

with

```text
rho_z = 1357,1353,1347,1338,1345,1335,1320.
```

This is not merely a `2`-adic completion statement.  The positive target is
one finite nucleus plus the actual unbounded quotient, an explicit finite
initialization, and a canonical top-boundary proof.  Such a certificate would
be a full unconditional counterexample.

Finite forward probes found no witness:

```text
negative three chart, h<10^7:
  maximum survival depth 10,
  first at h=2,485,507,
  physical n=4,971,009,
  prefix 1100000010;

negative eleven charts, h<10^8:
  maximum survival depth 3.
```

These numbers are observations, not candidates.

## 7. First six-defect scout

`X-8004` attacked the first family beyond `T-8001`:

```text
exactly six defects
neutral total R<=10
at most two high defects
high valuations 3..12
largest neutral gap rotated to the tail
```

It checked

```text
2,616,236 exact words,
440 height survivors,
0 divisor hits.
```

Frozen digest:

```text
e60a4a2288fa0882cc88c267eab0066d173f2fd641a6d12f11687848a656735e
```

The new mathematical obstruction is precise.  With six defects and two
separated high letters, the shortened `{1,3}` core can have fixed centered
value at least `2` at every rotation.  The five-defect comparison therefore
stops for a real reason rather than because the bookkeeping becomes longer.
The next theorem should use a bilinear determinant in the two high powers,
not another one-variable table.

## 8. Relation to the value-theory lane

The Väänänen--Wallisser theorem remains a strong exclusion tool for fixed
p-adic Tschakaloff phase vectors, and it explains why low-period completion
schedules are poor positive candidates.  It does not construct an ordinary
integer or solve the new pulse charts.  I therefore used it as a filter rather
than allowing the pass to drift back into an exclusion-only value program.

## 9. Verification performed

```bash
python3 -B experiments/X-8001-negative-cycle-two-pulse/run.py \
  --check-results experiments/X-8001-negative-cycle-two-pulse/results/canonical.json

python3 -B experiments/X-8002-negative-cycle-distributed-pulse/run.py \
  --check-results experiments/X-8002-negative-cycle-distributed-pulse/results/canonical.json

python3 -B experiments/X-8003-five-defect-cycle-exclusion/run.py \
  --check-results experiments/X-8003-five-defect-cycle-exclusion/results/canonical.json
python3 -B experiments/X-8003-five-defect-cycle-exclusion/verify.py \
  experiments/X-8003-five-defect-cycle-exclusion/results/canonical.json

python3 -B experiments/X-8004-six-defect-scout/run.py \
  --check-results experiments/X-8004-six-defect-scout/results/canonical.json
```

All commands replayed successfully in the authoring environment.

## 10. Exact next offense

The highest-value finite target is now a **six-defect bilinear eliminant**.
For two high valuations `x=2^b`, `y=2^c`, fixed gaps give

```text
E=Pxy+Qx+Ry+S,
D=Lxy-T.
```

Eliminating `xy` leaves one affine relation in `x,y`.  The target is to prove
that every nonzero determinant gives finite caps and to classify the genuine
zero-determinant patterns.  A zero determinant would be especially valuable:
it would expose an exact resonant family rather than another finite search.

In parallel, the exact block chart should be attacked as a one-counter safety
system.  A positive outcome there is immediately the full project objective.

## 11. Process improvement

Cycle experiments should report their **structural completeness axis**
explicitly:

```text
all pulse sizes / threshold only,
all positions up to rotation / selected positions,
all repetitions / frozen range,
height sieve / divisibility / full replay.
```

This prevents a large candidate count from concealing a narrow pulse or
position assumption and makes the next offensive extension obvious.
