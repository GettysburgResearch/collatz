# Session report — coefficient tangents and first-crossing envelope

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-31  
**Repository:** `GettysburgResearch/collatz`  
**Primary issue:** #75  
**Stacked base:** draft PR #77  
**Namespace:** corrected isolated `69xx`

## Publication correction

An initial draft used identifiers in the already occupied `66xx` range. PR #79 had prior ownership of exact `66xx` claim IDs. The colliding draft is preserved only as an audit trail and superseded by this corrected packet; no duplicate claim ID is promoted.

## Result

No proof of Collatz was obtained.

The packet makes three global advances.

### 1. Divergent-orbit tangent

Every divergent positive orbit has successive tail minima `h_i` satisfying

```text
t(h_i)=infinity;
h_i->infinity;
tau(h_i)->infinity.
```

A subsequence converges 2-adically to an all-prefix coefficient-supercritical tangent while the same ordinary integers escape to infinity in the real place. This proves exactly why compactness does not extract one bounded ordinary seed.

### 2. Exact canonical first-crossing defect

For every first-crossing word,

```text
D*r-A = 2^j*(r-y),
D=2^j-3^q,
y=T^j(r).
```

Thus Box 2 is canonical descent. Positivity descends every lift; zero is a positive cycle; negativity is a CST failure.

### 3. One-envelope coupling and zero-entropy exclusion

Every canonical failure at length `j` satisfies

```text
m_(j-1)^sup <= r^+(w) <= A_w/D <= F_j.
```

Hence `m_(j-1)^sup>F_j` closes every crossing at length `j`. Since `F_j` is unbounded along lower convergents, the same cofinal inequality also forces `m_N^sup->infinity`.

In parallel, an effective Baker bound plus exact dyadic factor separation proves that no unbounded acyclic failure family can have both logarithmic coefficient bank and uniformly zero factor entropy. This strictly broadens the linear-complexity family closure in PR #80 `T-6505`.

## Claims

```text
T-6901  finite coefficient threshold;
T-6902  wave-minimum supercritical tangent;
T-6903  divergence/CST dichotomy;
R-6901  compactness firewall;
L-6904  canonical first-crossing integer gap;
L-6905  Box-1/Box-2 envelope coupling;
T-6904  logarithmic-bank zero-entropy exclusion.
```

All remain proposed pending independent reconstruction. `T-6904` is source-dependent at the Baker lower bound.

## Exact remaining blocker

The sharp unified target is

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

for every sufficiently late valid first-crossing length `j`, followed by the finite small-length audit.

The current packet proves the necessary canonical-failure class is empty when it has both logarithmic proper-prefix bank and uniformly zero factor entropy. The surviving region is:

```text
superlogarithmic proper-prefix bank;
positive factor entropy at logarithmic scales;
or a positive cycle/repeated state.
```

No bounded numerical experiment is load-bearing.
