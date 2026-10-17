# Q-9409 — Quadratic-lacunary `2`-adic value problem

Claim ID: Q-9409  
Title: Can the sparse stack partial-theta value be an ordinary integer?  
Status: IDEA / primary value-theory frontier  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-21  
Dependencies: L-9407, T-9410, T-9409  
Scope: admissible increasing stack directives, especially the balanced `17/18` directive

## Exact question

For a height directive `m=(m_t)`, put

```text
ell_t=9*m_t+1,
H_0=0,
H_j=sum_(1<=i<=j) ell_i,
```

and define

```text
Theta_m
 =sum_(j>=0)(64/81)^H_j
 in Q_2.                                             (1)
```

L-9407 gives the unique initial stack context as

```text
x_0^*
 =-1/81+17*Theta_m/81^(ell_0+1).                    (2)
```

T-9409 says the same point is the inverse limit of the unique finite active
cylinders. Therefore ordinary stack closure is equivalent to asking whether
(2) is an ordinary integer, followed by positivity and chart-class checks.

## Balanced mechanical form

For a mechanical `17/18` directive, write

```text
m_(t+1)-m_t=17+s_t,
s_t=floor((t+1)*theta+rho)-floor(t*theta+rho),       (3)
```

where `s_t in {0,1}`. Then

```text
m_t=m_0+17*t+floor(t*theta+rho)-floor(rho),          (4)
```

and

```text
H_j
 =j*(9*m_0+1)
  +153*j*(j+1)/2
  +9*sum_(i=1)^j [floor(i*theta+rho)-floor(rho)].    (5)
```

Thus (1) is a `2`-adic partial-theta/Hecke-Mahler-type value with quadratic
exponents and an irrational-rotation perturbation.

## Why existing shortcuts do not immediately apply

T-9410 proves that the coefficient word of

```text
F_m(T)=sum_(j>=0)T^H_j                              (6)
```

has factor complexity `Theta(n^2)`. Therefore:

1. the raw coefficient word is not Sturmian or quasi-Sturmian;
2. linear-complexity `p`-adic digit criteria do not apply directly;
3. `H_(j+1)/H_j -> 1`, so fixed-ratio Hadamard-gap hypotheses are absent;
4. nonrationality of `F_m(T)` as a formal function does not by itself decide
   the special value `F_m(64/81)`.

Any imported theorem must be checked against these exact hypotheses rather than
cited by analogy.

## Target outcomes

### Obstruction outcome

Prove

```text
Theta_m notin Q                                    (7)
```

inside `Q_2`, or at least prove that (2) is not an ordinary integer, for every
admissible balanced directive. Combined with L-9407 this closes the exact stack
architecture.

### Construction outcome

Find an admissible directive for which (2) is an ordinary nonnegative integer.
Then:

1. reconstruct every context by L-9406;
2. prove all contexts positive;
3. check the chart class modulo `17`;
4. lift the formal `H` chain to the shortcut Collatz map;
5. create a `K-####` candidate only after the exact replay succeeds.

## Proposed proof interfaces

1. **S-adic matrix products.** Build convergent matrices for standard words of
   the mechanical directive while tracking exponent sums and partial values.
2. **`p`-adic Subspace Theorem.** Use repeated standard words to create several
   simultaneous rational approximants, not merely one truncation.
3. **Exceptional-value theorem.** Prove that the nonrational series (6) has no
   rational value at `64/81` under bounded positive second differences.
4. **Block-tail formulation.** Translate a value theorem into infinitely many
   nonzero active-cylinder blocks `a_K` from T-9409.
5. **Adelic formulation.** Combine the `2`-adic convergence with real bounds on
   the same standard-word approximants; do not identify the two limits.

## Falsification and safety criteria

- A theorem about Sturmian **digits** is insufficient unless the actual digits
  of (1), after odd-denominator carries, satisfy its hypothesis.
- Formal function transcendence is insufficient unless an exceptional-value
  theorem is supplied.
- Finite nonzero cylinder blocks are bounded evidence only.
- Compatible finite cylinders determine one `2`-adic point, not automatically
  an ordinary integer.

## Immediate deliverable

Ask issue #7 to audit primary `p`-adic transcendence results for this precise
quadratic-support, ratio-limit-one setting and record exact hypothesis matches
or failures.