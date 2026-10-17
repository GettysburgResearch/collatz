# T-9409 — Finite-tower cylinder and active fuel conservation

Claim ID: T-9409  
Title: Every prescribed finite stack schedule selects exactly one initial residue cylinder  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9406  
Scope: every finite or infinite sequence of nonnegative stack heights  
Related counterexample candidates: issue #4 active stack frontier; no `K-####` candidate

## Statement

Fix stack heights

```text
m_0,m_1,...,m_K,
```

and require exact regeneration from height `m_i` to `m_(i+1)` for
`0<=i<K`.  Put

```text
M_i=64^(9m_i+1),
Q_K=product_(i=1)^K M_i
   =2^B_K,
B_K=6*sum_(i=1)^K (9m_i+1).                    (1)
```

Then there is exactly one residue

```text
R_K mod Q_K                                    (2)
```

such that an ordinary initial context `x_0` realizes all `K` stages iff

```text
x_0=R_K mod Q_K.                               (3)
```

Equivalently, any two initial contexts realizing the same finite height
schedule satisfy

```text
v_2(x_0-x'_0)>=B_K,                            (4)
```

and every context in that cylinder realizes the schedule.

This is the **active fuel-conservation law**: stage `i` appends exactly

```text
6*(9m_i+1)
```

new binary constraints to the initial context, and no later affine quotient
map refunds or compresses them.

## Recursive construction

The cylinder can be computed backwards without search.

Start with the unconstrained terminal context

```text
R=0,
Q=1.
```

For `i=K-1,K-2,...,0`, let `r_i=r_(m_i,m_(i+1))` and
`k_i=k_(m_i,m_(i+1))` from L-9406.  Solve the unique congruence

```text
y_i = A_(m_i)^(-1)*(R-k_i) mod Q.              (5)
```

Then replace

```text
R <- r_i+M_(i+1)*y_i,
Q <- M_(i+1)*Q.                                (6)
```

After the final step, `(R,Q)=(R_K,Q_K)`.

## Proof

Induct on `K`.  For `K=0`, every initial context is allowed, represented by
`R_0=0 mod 1`.

Assume the suffix schedule

```text
m_1,...,m_K
```

selects exactly one next-context cylinder

```text
x_1=R mod Q.
```

By L-9406, the first stage requires

```text
x_0=r_0+M_1*y,
x_1=A_(m_0)*y+k_0.                             (7)
```

Because `A_(m_0)` is odd, the suffix condition fixes exactly one class `y mod
Q`, namely (5).  Substituting it into the first equation gives exactly one
class `x_0 mod M_1Q`, which is (6).  This proves the induction, (2), and (3).
The modulus recursion gives (1), and (4) is equivalent to congruence modulo
`Q_K`. **QED**

## Infinite schedules

For an infinite directive

```text
m_0,m_1,m_2,...,
```

its finite cylinders are nested:

```text
R_(K+1)=R_K mod Q_K,
Q_K | Q_(K+1),
Q_K -> infinity.                               (8)
```

Therefore they determine exactly one

```text
x_0^* in Z_2.                                  (9)
```

This `2`-adic context realizes every finite prefix formally.  It is an ordinary
nonnegative integer iff the least representatives

```text
0<=R_K<Q_K
```

eventually stabilize.  If they stabilize at `R`, then `R` belongs to every
cylinder and gives one ordinary infinite stack chain.  Conversely, if an
ordinary `R>=0` belongs to every cylinder, then once `Q_K>R`, the least
representative is exactly `R` forever.

Thus active stack closure is reduced exactly to a least-representative
stabilization problem, with no compactness ambiguity.

## Quantitative schedule cost

If the heights are strictly increasing, then `m_i>=m_0+i`, and

```text
B_K
 >= 54*K*m_0 + 27*K*(K+1) + 6K.               (10)
```

For the reported stack increment range

```text
17<=m_i-m_(i-1)<=18,
```

we have

```text
54*K*m_0 +459*K*(K+1)+6K
 <= B_K
 <=54*K*m_0 +486*K*(K+1)+6K.                  (11)
```

Hence the initial precision selected by a `K`-stage tower is quadratic in the
number of stages, even after ignoring all raw zero-run factor complexity.

## Interpretation

- Finite CRT steering is now an exact one-cylinder theorem rather than a vague
  existence statement.
- An infinite schedule does not leave a Cantor family of possible initial
  contexts: it selects one `2`-adic point.
- Odd affine quotient evolution transports unused digits isometrically.  It
  never creates extra compatible initial cylinders.
- The remaining ordinary-integer question is whether the unique nested residue
  sequence stabilizes, not whether finite prefixes are mutually compatible.

## Dependency audit

Only L-9406 and finite induction are used.  No equidistribution, automaticity,
SML, or finite experiment is a proof dependency.

## Gap audit

- A unique `2`-adic initial context may still be an ordinary positive integer;
  the theorem does not rule this out.
- Quadratic precision does not imply quadratic computational complexity: a
  compact algorithm may compute the selected digits.
- Formal finite-prefix realization must still be translated through the chart
  congruence to an ordinary Collatz seed before any `K-####` claim.
- Positivity of all intermediate contexts is an additional requirement for a
  candidate; the cylinder theorem classifies integrality, not positivity.

## Adversarial tests

`X-9404` computes cylinders independently by backward congruence and forward
stage replay, checks random members of each cylinder, perturbs every selected
binary block to force failure, and verifies the exact exponent `B_K`.

## Remaining uncertainty

Independent reconstruction is pending.  The main frontier is to prove
nonstabilization for the balanced `17/18` directive, or find a schedule and one
ordinary stable representative.

## Suggested next attack

Study the block digits

```text
(R_(K+1)-R_K)/Q_K mod M_(K+1).
```

A proof that infinitely many are nonzero for every admissible balanced
directive would rule out an ordinary initial context.  A construction making
them eventually zero would produce an ordinary infinite stack candidate.
