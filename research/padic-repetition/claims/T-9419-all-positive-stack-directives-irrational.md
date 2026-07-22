# T-9419 — Every infinite positive stack directive is irrational

Claim ID: `T-9419`  
Title: No infinite positive height-increment directive selects a rational or ordinary stack context  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9407`, `L-9408`, `T-9418`  
Scope: the complete sparse-stack class with arbitrary positive height increments  
Related counterexample candidates: issue #4 stack frontier; no `K-####` candidate

## Setup

Fix any starting height

```text
m_0>=0
```

and any infinite increment directive

```text
d_1,d_2,d_3,...,
d_i>=1.                                                (1)
```

Put

```text
m_t=m_0+sum_(1<=i<=t)d_i,
ell_t=9m_t+1.                                          (2)
```

The sparse stack series of `L-9407` and `L-9408` is

```text
Theta(m_0;d)
 =sum_(j>=0)T^E_j,
T=64/81,
E_0=0,
E_j=sum_(1<=i<=j)ell_i.                                (3)
```

Its ones occur at positions

```text
0,E_1,E_2,...
```

with successive gaps

```text
E_(j+1)-E_j=ell_(j+1)=9m_(j+1)+1.                     (4)
```

## Theorem

For every directive satisfying (1),

```text
boxed:
Theta(m_0;d) notin Q.                                 (5)
```

Consequently:

1. the initial context in the sparse stack partial-theta normal form is irrational;
2. the formal stack state `A_*(m)` is irrational;
3. no such directive has an ordinary integer initial context;
4. no finite steering prefix can repair any infinite positive suffix;
5. in particular, the balanced mechanical `17/18` directive and every periodic, eventually periodic, Sturmian, Ostrowski, or adaptive positive increment directive in this exact stack model are excluded.

## Proof

Since every increment is positive,

```text
m_t>=m_0+t,
```

and therefore the gaps in (4) satisfy

```text
ell_t>=9(m_0+t)+1 -> infinity.                         (6)
```

The series (3) is a binary `T`-power series with infinite support and unbounded gaps. `T-9418` therefore gives (5).

`L-9407` expresses the exact initial context as

```text
x_0
 =-1/81
  +17/81^[ell_0+1]
    *sum_(j>=0)T^H_j,                                 (7)
```

where the normalized support gaps are the same increasing stack lengths after removal of the first stage. The coefficient multiplying the tail in (7) is a nonzero rational number. Hence rationality of `x_0` is equivalent to rationality of that sparse tail, which has already been excluded.

Likewise, the formal state is a nonzero rational multiple of the sparse support series from (3), so it is irrational.

A finite steering prefix acts by the rational affine transfer identity of `L-9408`. If the full prefixed value were rational, solving that identity for its positive infinite suffix would make the suffix rational, contradicting (5). **QED**

## Direct denominator proof inside the stack notation

For review, the argument may also be reconstructed without citing `T-9418`.
Define the stage tails

```text
Theta_t=Theta(m_t;d_(t+1)d_(t+2)...).
```

Then

```text
Theta_t=1+T^[ell_(t+1)]Theta_(t+1).                    (8)
```

If `Theta_0` were rational, `L-9416` would force every reduced tail denominator to divide one fixed odd integer `B`. But

```text
0<Theta_t-1
 <=T^[ell_(t+1)]/(1-T)
 ->0,                                                  (9)
```

while every rational `Theta_t!=1` with denominator dividing `B` satisfies

```text
|Theta_t-1|>=1/B.                                     (10)
```

Contradiction.

## What this closes

This theorem closes the exact sparse counter-stack ordinary-initialization problem studied in this packet:

```text
arbitrary positive height directive
 -> unique Z_2 stack context
 -> never a rational number
 -> never an ordinary integer.                        (11)
```

The conclusion is uniform over the directive. No periodicity, balance, finite-state rule, bounded increment, or complexity assumption remains.

The native and source-dependent Padé theorems `T-9412`--`T-9417` remain valid and useful as stronger value-theoretic models, but they are no longer load-bearing for rationality exclusion of the sparse stack class.

## What remains open

The theorem does **not** settle:

- the full M1 survivor attractor, whose arbitrary binary codes need not have unbounded zero gaps;
- dense ordinary survivor codes with bounded zero runs;
- PR #3's negative-cycle cap-stitch system, which is not this sparse positive-increment series;
- the H subsystem;
- the Collatz conjecture.

Its broad M1 consequence is only the necessary condition from `T-9418`: every nontrivial ordinary survivor with infinite support must have bounded zero runs.

## Dependency audit

- `L-9407` supplies the exact sparse context and rational affine equivalence.
- `L-9408` supplies the finite-prefix transfer and stage recurrence.
- `T-9418` supplies unbounded-gap irrationality.
- No external theorem, experiment, Padé approximation, or asymptotic coefficient estimate is used.

## Gap audit

- Positivity of every increment is essential for gap divergence. A directive allowing resets or nonpositive height changes lies outside the definition.
- Infinite continuation is essential. Every finite schedule has rational finite truncations and exact ordinary cylinders.
- Irrationality excludes an ordinary context but does not construct a Collatz trajectory or prove convergence of all ordinary integers.
- Branch-qualified stack definitions must not be conflated with every binary `64 -> 81` code.

## Adversarial tests

`X-9413` verifies recurrence (8), gap growth, exact finite-prefix identities, and denominator descent on independent synthetic data. The infinite contradiction is the proof above, not the finite audit.

## Suggested next attack

Remove the sparse stack from the live M1 construction portfolio and refocus on the dense bounded-gap survivor frontier. Combine the new bounded-gap necessity with:

```text
- T-9401/T-9402 repetition and complexity rigidity;
- PR #16 centered nearest-integer block recurrence;
- the independently reviewed all-depth EQ theorem;
- and exact finite survivor minima.
```

The next decisive target is to show that a bounded-gap ordinary survivor cannot maintain the required appended base-64 block stabilization.
