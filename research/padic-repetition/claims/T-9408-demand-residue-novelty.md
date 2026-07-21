# T-9408 — Demand-residue novelty along bounded-increment schedules

Claim ID: T-9408  
Title: Exponential no-reuse windows for exact stack demands  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9405  
Scope: every strictly increasing stage schedule with bounded positive increments  
Related counterexample candidates: issue #4 Sturmian/Ostrowski stack frontier; no `K-####` candidate

## Statement

Let

```text
m_0<m_1<m_2<...
```

be an integer stage schedule satisfying

```text
1 <= m_(t+1)-m_t <= C                         (1)
```

for one fixed integer `C>=1`.  At base-`64` demand depth `j>=1`, put

```text
P_j = 2^(6j-4),
W_j(C) = floor((P_j-1)/C)+1.                  (2)
```

Then every `W_j(C)` consecutive demand residues

```text
D_j(m_t), D_j(m_(t+1)), ..., D_j(m_(t+W_j(C)-1))
```

are pairwise distinct.  Consequently, among the first `T` stages,

```text
|{D_j(m_t):0<=t<T}| >= min(T,W_j(C)).         (3)
```

For the active `17/18` schedule interface, `C=18`, so

```text
W_j(18)=floor((2^(6j-4)-1)/18)+1.             (4)
```

Examples:

```text
depth j=2: W=15,
depth j=3: W=911,
depth j=4: W=58,255.
```

Thus exact depth-`j` demand templates cannot be reused inside an exponentially
long stage window.

## Finite-state corollary

Suppose an online implementation has a state `s_t` and its exact depth-`j`
demand output is a function only of `s_t`.  On any window covered by the
theorem, all states must be distinct.  Therefore the implementation needs at
least

```text
W_j(C)
```

reachable states, or at least

```text
log_2 W_j(C) = 6j-O(log C)                    (5)
```

bits of distinguishable control state, if it represents the demand by a
bounded finite-state table.

## Proof

Take two indices `a<b` in a window of length `W_j(C)`.  By (1),

```text
0 < m_b-m_a
  <= C(b-a)
  <= C(W_j(C)-1)
  <= P_j-1.                                   (6)
```

Hence `m_b-m_a` is a positive integer strictly smaller than `P_j`, and cannot
be divisible by `P_j`.  L-9405 gives

```text
D_j(m_b)=D_j(m_a)
  iff m_b=m_a mod P_j,
```

so the two demands are distinct.  This proves the window statement and (3).
The finite-state corollary follows because a repeated state would force a
repeated output inside a window where none exists. **QED**

## Interpretation

This is a padding-free arithmetic novelty bound:

- the count is taken per stack stage, not per emitted zero;
- each extra base-`64` precision digit expands the no-reuse window by `64`;
- the result measures exact residue distinguishability rather than raw word
  complexity.

## Dependency audit

Only L-9405 is used.  The schedule need not be Sturmian, automatic, random, or
balanced; positivity and the upper increment bound are sufficient.

## Gap audit

- The state lower bound applies only when the exact residue is determined by a
  bounded state table.  An unbounded counter plus modular exponentiation can
  recompute the residue without materializing all states.
- Distinct demands do not imply independent demands.
- The theorem does not show that the evolving high quotient fails to carry the
  required stage information.
- The actual stack asks for a depth that grows with the next stage.  The fixed
  depth theorem is an atomic lower bound to be inserted into that moving-depth
  recurrence.

## Adversarial tests

`X-9403` exhausts all `2^12` words over the increment alphabet `{17,18}` at
three demand depths and checks every pair whose stage difference is below the
isometry modulus.

## Remaining uncertainty

Independent reconstruction is pending.  The central question is whether the
active high quotient acts as a genuine information source or merely transports
the preloaded inverse-limit residue blocks identified here.

## Suggested next attack

At stage `t`, record the first depth at which the supplied high quotient differs
from the unique demanded lift.  Prove a conservation or monotonicity law for
that mismatch depth under the exact stack update.
