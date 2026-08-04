# Drift isolation at `5x+1`

Agent: `gpt56-drift-01`  
Issue: #26  
Branch: `agent/gpt56-drift-01/26-5x1-portability`  
Packet status: **PARTIAL — EXACT REDUCTIONS AND FINITE CERTIFICATES; GLOBAL EXISTENCE OPEN**  
Claim namespace: `88xx`

## Mission and status boundary

This packet uses the shortcut `5x+1` map as a positive-drift control universe to
separate:

1. universal parity-word and `2`-adic format constraints;
2. multiplier-specific arithmetic realization of exact charts;
3. drift-sensitive quantitative constants;
4. ordinary-integer completion obstructions.

All theorem-level entries remain **PROPOSED** pending independent reconstruction.
The packet claims no positive infinite chart orbit, no divergent `5x+1` seed,
no `3x+1` counterexample, and no resolution of either conjecture.

The canonical branch-local claim ledger is `CLAIM_INDEX.md`. The renumbering and
publication audit is `NAMESPACE_AUDIT_2026-07-22.md`.

## Wave 1 — exact `4 -> 5` amplifier and portability

For

```text
T_5(n)=n/2       when n is even,
       (5n+1)/2  when n is odd,
```

there are two exact two-step branches:

```text
T_5^2(4q-1)=5q-1,   parity word 10,
T_5^2(4q-2)=5q-2,   parity word 01.
```

They stack to

```text
H^m(4^m*q-c)=5^m*q-c,   c in {1,2}.
```

For a hypothetical positive ordinary infinite chart orbit, its phase directive
`eps_j in {0,1}` satisfies

```text
A+2=(1/5)*sum_(j>=0) eps_j*(4/5)^j  in Z_2.
```

The ordinary-section repetition/height theorem survives in this positive-drift
chart. Equal factors of length `ell` beginning at `r<t` force

```text
4^(t+ell)<(A+2)*5^t,
```

and every nontrivial ordinary survivor code has lower factor-complexity slope at
least

```text
1/(log_4(5)-1)=6.212567439010779752... .
```

A literal length-6, weight-4 port of the active `3x+1` chart fails
arithmetically because

```text
5^4-2^6=561
```

divides none of the fifteen relevant affine corrections.

## Wave 2 — signed phase shadows and exact rational-base reduction

Every finite dyadic connector is the positive-quotient lift of one signed orbit:

```text
T_a^k(2^L*q+d)=a^(s_k)*2^(L-k)*q+T_a^k(d).
```

For a nonzero signed cycle of period `L` and odd-step count `s`,

```text
(2^L-a^s)d=B_a(w)>0.
```

Thus positive cycles are subcritical and negative cycles generate supercritical
same-phase cylinders. The exact `4 -> 5` chart is the lift of

```text
-2 -> -1 -> -2.
```

On the two phases, the apparent switch surplus is a boundary coboundary:

```text
2s-L=chi(start)-chi(end).
```

Hence phase-only scheduling creates no additional long-run gain. Quotient,
carry, deeper residue, additional phases, or unbounded memory remain outside
that refutation.

After shifting `X=A+1`, the physical chart is exactly

```text
tau(X)=ceil(5X/4),
b(X)=(-X) mod 4 in {0,1,2,3}.
```

A positive chart survivor exists exactly when some `X>=2` has

```text
b(tau^j(X)) in {0,1}  for every j>=0.
```

Any such orbit is strictly increasing and therefore divergent in the `5x+1`
control universe.

## Wave 2 — `2`-adic geometry

Let

```text
C={(1/5)*sum_(j>=0) eps_j*(4/5)^j : eps_j in {0,1}}.
```

If two directives first differ at index `j`, their images have exact difference
valuation `2j`. Consequently:

- the coding is injective and isometric at prefix scale `4^(-j)`;
- level `k` occupies exactly `2^k` classes modulo `4^k`;
- `C` has Haar measure zero in `Z_2`;
- `C` has `2`-adic Hausdorff dimension `1/2`;
- positive ordinary chart survivors have upper natural density zero.

This proves thinness, not emptiness.

## Wave 3 — exact finite composition and depth 50

Let `S_n` be the legal residue frontier modulo `4^n`, and put
`y_h(r)=tau^h(r)`. Then

```text
tau^h(r+4^h*t)=y_h(r)+5^h*t,
```

and

```text
r+4^h*t in S_(h+m)
iff
r in S_h and (y_h(r)+5^h*t) mod 4^m in S_m.
```

Multiplication by `5^h` is invertible modulo `4^m`, giving an exact bijection

```text
S_h x S_m <-> S_(h+m).
```

A frozen `25+25` meet-in-the-middle computation proves that the least positive
root surviving fifty digits is

```text
m_50=4538335001132531.
```

The corresponding physical seed is

```text
A_50=4538335001132530,
```

and it exits immediately after its fiftieth legal macro-step on bottom digit
`3`. Therefore every root below `m_50` exits before depth 50. This is a sharp
finite theorem, not an infinite extrapolation.

## Wave 3 — critical nearest-integer equivalence

For every `q>=2`, `p=q+1`, the partial map

```text
x -> ceil(p*x/q),   x mod q in {0,q-1},
```

has a positive infinite orbit if and only if some `xi>0` satisfies

```text
||xi*(p/q)^n||<1/p  for every n>=0.
```

At `p=5,q=4`, the chart question is therefore equivalent to

```text
exists xi>0 such that ||xi*(5/4)^n||<1/5 for all n.
```

The symmetric strict threshold must not be conflated with a one-sided
`Z_(p/q)` condition.

## Wave 4 — verified namespace repair and bounded-state boundary

A live audit found that a previous session had reserved several IDs only in PR
and issue comments. They were not repository claims. The discrepancy is now
recorded and repaired by committed files.

The new exact boundary is:

1. every finite legal bottom word determines one residue class modulo `4^n` and
   has infinitely many positive representatives (`L-8811`);
2. every eventually periodic directive gives a rational completion with
   physical value in `[-2,-1]` (`T-8812`);
3. every autonomous deterministic finite-state generator is eventually
   periodic and therefore cannot construct a positive survivor (`D-8802`,
   `R-8802`);
4. the missing information is unbounded one-root arithmetic coherence, not a
   finite forbidden word or bounded autonomous phase controller (`O-8803`).

This does not exclude externally driven transducers, counters, stacks, growing
quotients, unbounded carry, or other infinite-state constructions.

## Exact global alternatives

Let `m_n` be the least positive root surviving `n` legal bottom digits. The
survivor sets are nested, so

```text
positive infinite survivor exists
iff (m_n) is bounded
iff (m_n) eventually stabilizes.
```

The two branch-local open questions are:

```text
Q-8801: does m_n -> infinity?
Q-8802: does some xi>0 satisfy ||xi*(5/4)^n||<1/5 for all n?
```

By the committed equivalences, these are the negative and positive faces of the
same exact control-chart frontier.

## Portability matrix

| Mechanism | Verdict | Exact discriminator |
|---|---|---|
| Affine parity-word formula | HOLDS-VERBATIM | none |
| Positive-cycle sign criterion | HOLDS-VERBATIM | `2^L-a^s` |
| Signed phase-shadow identity | HOLDS-VERBATIM | signed orbit |
| One-step shared-branch fuel loss | HOLDS-VERBATIM | oddness of `a` |
| Exact `T_5^2` amplifier | EXISTS | `5-4=1` |
| Literal length-6/weight-4 port | BREAKS | divisibility by `561` |
| Repetition/height squeeze | HOLDS | `log_U(V)-1` |
| Phase-only switch surplus | REFUTED | telescoping coboundary |
| Base-`5/4` bottom reduction | EXACT | `4X'=5X+delta` |
| Completion-set geometry | EXACT | first-difference valuation `2j` |
| Autonomous finite-state construction | REFUTED | eventual periodicity |
| Infinite positive path | OPEN | unbounded ordinary coherence |

## Experiments

- `X-8801`: generalized affine/fuel/cycle/chart checks and one million exact
  `5x+1` steps from seed 7; finite evidence only.
- `X-8802`: signed connector, cycle, and physical/tree checks; finite evidence
  only.
- `X-8803`: exact depth-50 meet-in-the-middle frontier and replay.

See `CLAIM_INDEX.md` for the exact committed claim files and intentional ID
gaps.

## Claim boundary

This packet is a calibrated control program. Even a future divergent `5x+1`
seed would not automatically be a standard Collatz counterexample. A complete
`3x+1` counterexample still requires either a positive nontrivial `3x+1` cycle,
a rigorously divergent positive `3x+1` orbit, or another proved equivalent
construction.
