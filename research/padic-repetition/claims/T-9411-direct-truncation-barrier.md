# T-9411 — Direct truncation approximation barrier

Claim ID: T-9411  
Title: Sparse stack truncations have exact subcritical `2`-adic approximation exponent  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9407, T-9410  
Scope: every increasing bounded-increment stack directive  
Related counterexample candidates: issue #4 stack frontier; no `K-####` candidate

## Setup

Use the notation of L-9407 and put

```text
z=64/81,
Theta=sum_(j>=0) z^H_j in Q_2,
Theta_K=sum_(j=0)^K z^H_j.                          (1)
```

Write

```text
Theta_K=P_K/81^H_K,
P_K=sum_(j=0)^K 64^H_j * 81^(H_K-H_j).              (2)
```

Let `height(a/b)=max(|a|,|b|)` for a reduced rational `a/b`.

## Statement 1 — exact reduced denominator

For every `K`, equation (2) is in lowest terms and

```text
den(Theta_K)=81^H_K.                                (3)
```

Moreover,

```text
81^H_K
 <=height(Theta_K)
 <=(81/17)*81^H_K.                                  (4)
```

### Proof

Every term in `P_K` except the last is divisible by `81`, while the last term
is `64^H_K`, which is nonzero modulo `3`. Thus `gcd(P_K,81)=1`, proving (3).
Since all terms are nonnegative in the real embedding and

```text
sum_(j>=0)(64/81)^j=81/17,
```

we have `0<Theta_K<=81/17`; multiplying by the denominator gives (4). **QED**

## Statement 2 — exact `2`-adic error

For every `K`,

```text
v_2(Theta-Theta_K)=6*H_(K+1).                       (5)
```

### Proof

The first omitted term has valuation `6H_(K+1)`. Every later omitted term has
strictly larger valuation, so the ultrametric equality gives (5). **QED**

## Statement 3 — limiting approximation exponent

Define

```text
tau_K
 =[-log_2 |Theta-Theta_K|_2]
   /log_2 height(Theta_K).                          (6)
```

Then

```text
lim_(K->infinity) tau_K
 =6/log_2(81)
 =1/log_64(81)
 =0.946394630357... .                               (7)
```

### Proof

Statements (4) and (5) give

```text
tau_K
 =[6H_(K+1)]/[H_K log_2(81)+O(1)].                 (8)
```

T-9410 gives `H_(K+1)/H_K ->1`, proving (7). **QED**

## Statement 4 — context truncations have the same barrier

Let

```text
x_0^*
 =-1/81
  +17/81^(ell_0+1)*Theta                           (9)
```

and let `x_(0,K)` be obtained by replacing `Theta` with `Theta_K`. Then the
reduced denominator of `x_(0,K)` is

```text
81^(ell_0+1+H_K),                                   (10)
```

its `2`-adic error has valuation `6H_(K+1)`, and its limiting rational
approximation exponent is again the constant in (7).

### Proof

After multiplication by the denominator in (10), all numerator terms except
the term arising from `z^H_K` are divisible by `3`; that last term is
`17*64^H_K`, nonzero modulo `3`. Hence no factor `3` cancels. The affine
prefactor is a `2`-adic unit, so the error valuation remains (5). The fixed
`ell_0+1` does not change the limit. **QED**

## Consequence — direct Ridout/truncation methods cannot fire

A rational-approximation transcendence criterion requiring exponent `>2` cannot
be triggered by any subsequence of the direct sparse partial sums, whose
exponent converges to `<1`. The problem is not an omitted constant: the exact
reduced denominator and exact `2`-adic error are both frozen above.

Equivalently, any successful Diophantine approximation argument must introduce
new approximants with a genuine gain over ordinary truncation, for example by:

```text
- cancelling a macroscopic part of the 3-power denominator;
- creating simultaneous shifted linear forms from repeated standard words;
- exploiting another absolute value in an adelic determinant;
- or constructing Padé-type rather than partial-sum approximants.
```

## Sharp lacunary-theorem boundary

The support points themselves satisfy

```text
H_(K+1)/H_K ->1.                                    (11)
```

Thus any lacunary theorem requiring multiplicative gaps bounded below by a
constant greater than one misses this series at its first gap hypothesis. This
is exactly consistent with (7).

## Dependency audit

- L-9407 supplies the exact series and context affine transform.
- T-9410 supplies `H_(K+1)/H_K ->1`.
- No external transcendence theorem is a proof dependency; the comparison with
  Ridout-type criteria is methodological.

## Gap audit

- The theorem rules out only **direct truncation** as a sufficiently strong
  approximant family. It does not prove the value rational or irrational.
- A different approximant family may have much smaller reduced height.
- The real geometric bound in (4) is used only to estimate rational height; the
  real and `2`-adic limits are not identified.
- The exponent convention is stated explicitly; integer-approximation criteria
  use a different threshold but face the analogous cylinder ratio limit one.

## Adversarial tests

`X-9406` verifies the reduced-denominator congruence, exact error valuation, and
finite approximation exponents for balanced prefixes.

## Remaining uncertainty

Whether standard-word or Padé approximants can cross the critical exponent is
open.

## Suggested next attack

Derive exact S-adic transfer polynomials for standard directive words and search
for determinants whose reduced height is below the direct denominator scale
`81^H_K`.