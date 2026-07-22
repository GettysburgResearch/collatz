# Negative-three pulse chart: an invariant `9/(8,16)` ordinary subsystem

**Agent:** `gpt56-cartographer-01`  
**Source:** PR #51 `O-8001` at `0487d96e82eaa3d251820373ed690f3b0c9575f1`  
**Classification:** original cartography synthesis from an exact proposed source interface; independently checkable algebra, not an independently reviewed repository theorem  
**Full-objective role:** one positive all-time path is an unconditional Collatz counterexample

## 1. Source block chart

PR #51 centers the accelerated negative three-cycle at `z=-5`. With

```text
h=(n+5)/2,
```

the two exact two-odd-step blocks are

```text
A=(1,2):  h=8q    -> 9q,
B=(2,2):  h=3+16q -> 3+9q.
```

The physical boundary state is `n=-5+2h`.

## 2. Invariant multiple-of-21 section

Restrict to

```text
h=21x,
x in Z_(>0).
```

This section is forward invariant.

For block `A`, `21x=8q` forces `x=8s` and `q=21s`, so

```text
x=8s -> 9s.
```

For block `B`, `21x=3+16q` is equivalent to `x=7+16s`; then

```text
q=9+21s,
3+9q=21(4+9s),
```

so

```text
x=7+16s -> 4+9s.
```

Therefore the induced deterministic partial map is

```text
G(x)=9x/8        if x == 0 mod 8,
G(x)=(9x+1)/16  if x == 7 mod 16,
undefined       otherwise.
```

Equivalently, with `epsilon in {0,1}`,

```text
2^(3+epsilon) G(x)=9x+epsilon,
```

where `epsilon=0` is block `A` and `epsilon=1` is block `B`.

The exact physical embedding is

```text
n=42x-5.
```

The trivial physical state `n=1` would require `x=1/7`, so it is absent from the positive integral chart.

## 3. Full-counterexample implication

Every legal step of `G` replays one exact accelerated valuation block:

```text
x == 0 mod 8  -> valuations (1,2),
x == 7 mod16 -> valuations (2,2).
```

Thus an explicit `x_0>0` whose `G`-orbit is defined forever gives one ordinary positive shortcut-Collatz orbit from

```text
n_0=42x_0-5.
```

If a boundary state repeats, the physical orbit is a nontrivial positive cycle. If no boundary state repeats, the infinite sequence of positive integers is unbounded. Either outcome disproves Collatz.

## 4. Finite cylinders are a full binary tree

For a finite block word `epsilon_0,...,epsilon_(N-1)`, put

```text
E_0=0,
E_(j+1)=E_j+3+epsilon_j.
```

Composition gives

```text
2^E_N x_N
 =9^N x_0
  +sum_(j=0)^(N-1) epsilon_j 9^(N-1-j)2^E_j.
```

Because `9` is odd, induction gives exactly one initial residue class modulo `2^E_N` realizing every finite binary word. Hence finite compatibility cannot decide the problem. An infinite word selects one `2`-adic initial value; the positive target is precisely that this value be one ordinary positive integer, equivalently that the least compatible representatives eventually stabilize.

This puts the chart at the same ordinary-realization boundary as the centered and H programs, but with only two fixed local formulas and no external type control.

## 5. Renewal form and connection to H

A positive finite integer cannot take block `A` forever, because that would require divisibility by `8^m` for every `m`. Therefore every positive all-time path has infinitely many `B` blocks.

Start immediately after one `B`, let `r` be the number of consecutive `A` blocks before the next `B`, and set

```text
p=16x.
```

One renewal obeys

```text
p_next
 = [3^(2r+2)/2^(3r+4)] p + 1.
```

This is a toll-one affine renewal of exactly the same structural form as the H recurrence, with multiplier

```text
a_r^pulse=3^(2r+2)/2^(3r+4)
         =(3/4) a_r^H.
```

The critical mean run length is

```text
kappa_pulse
 =log(16/9)/log(9/8)
 =2 log(4/3)/log(9/8)
 =4.8849491923617...
```

Consequently the H cycle-minimum, entropy/capital, prefix-return, fresh-prime, renewal-height, and endpoint-product methods have a natural exact target here after their hypotheses are rederived for this chart.

## 6. Exact finite ordinary frontier through depth 31

`cartography/pulse_chart_frontier.cpp` exhausts every finite binary chart word through depth `31`. It maintains the exact cylinder invariant

```text
x_0=R+2^E q,
x_d=a+9^d q,
```

and lifts both possible next digits without expanding physical Collatz trajectories. The frozen run covers

```text
4,294,967,294 finite prefix words at depths 1..31.
```

The least positive initial state surviving `31` chart blocks is

```text
x_31^min=24,643,395,416,689,283,212,736,
n_31^min=42x_31^min-5
        =1,035,022,607,500,949,894,934,907.
```

Its chart word is

```text
0010000100100010100000110000010
```

with `0=A=(1,2)` and `1=B=(2,2)`. It survives exactly `31` blocks and then exits; every smaller positive `x` exits earlier.

The independent Python verifier repeats the complete minimum computation through depth `20`, checks every frozen minimizing word by direct chart replay, and checks the full depth-31 physical valuation replay. The depth-31 global minimum remains an exact source computation rather than an independently repeated `2^31` search.

Frozen artifact SHA-256:

```text
110d1322ad10d9748f3c888971681c5d90ec73c05e73507ea1034eab62386ced
```

This is a sharp finite ordinary-section result, not evidence of an infinite path.

## 7. Atomic decision

A positive resolution is:

```text
find one x_0>0 and a finite inductive top-boundary invariant
proving G^n(x_0) is defined for every n.
```

A decisive negative resolution is:

```text
prove every ordinary x_0>0 eventually leaves the domain,
using the renewal form or an exact completion-height theorem.
```

A modular lasso, arbitrary-depth compatible word, or isolated `2`-adic point is not a witness.

## 8. Finite checkers

`cartography/check_pulse_chart.py` independently checks the physical block replay and renewal identity on finite ranges. Its default frozen run checked:

```text
37,500 exact chart branches,
15,872 completed renewals,
maximum observed renewal run r=4,
semantic SHA-256:
35d17a9c0f0d6b6f1bb321e63606424aff3d617e1091b3baefcc75f7b367318b.
```

The one-step/renewal checker and the depth-frontier programs are finite regression artifacts only; neither is an all-time proof.
