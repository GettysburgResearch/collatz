# LIT-KTHM-0035 — Approximation exponent greater than one excludes a rational 2-adic target

**Type:** elementary product-formula lemma.  
**Maps to:** `PADIC/T-9412`, `PADIC/T-9414`, and future Hermite--Padé systems.

## Statement

Let `alpha in Z_2` and let

```text
r_n=p_n/q_n in Q,
gcd(p_n,q_n)=1,
q_n odd,
r_n != alpha.
```

Let

```text
H(r_n)=max(|p_n|,|q_n|).
```

Suppose

```text
limsup_(n->infinity)
 v_2(alpha-r_n)/log_2 H(r_n) > 1.                     (1)
```

Then

```text
alpha notin Q.                                        (2)
```

The same conclusion follows if `(1)` is replaced by an eventual inequality

```text
v_2(alpha-r_n) >= (1+epsilon)log_2 H(r_n)-O(1)        (3)
```

for some `epsilon>0`.

## Proof

Assume `alpha=a/b` in lowest terms. Because `alpha in Z_2`, the denominator `b` is odd. The nonzero integer

```text
N_n=a*q_n-b*p_n
```

has

```text
v_2(N_n)=v_2(alpha-r_n),                              (4)
```

since `bq_n` is odd. Its ordinary size obeys

```text
|N_n|
 <= |a||q_n|+|b||p_n|
 <= (|a|+|b|)H(r_n).                                  (5)
```

Every nonzero integer `N` satisfies

```text
2^v_2(N) <= |N|.                                      (6)
```

Combining `(4)`--`(6)` gives

```text
v_2(alpha-r_n)
 <= log_2 H(r_n)+log_2(|a|+|b|),                      (7)
```

contradicting `(1)` or `(3)`. ∎

## Interpretation

The critical exponent for excluding a **fixed rational target** is one, not the Roth/Ridout exponent two needed to exclude all algebraic irrational targets. This is why PR #20's scalar and short-period Padé constructions can prove irrationality with exponents between one and two.

## Audit requirements for native use

A proposed approximant family must report:

1. the exact nonzero error;
2. the reduced rational denominator and its parity;
3. the height after reduction;
4. a uniform exponent strictly greater than one;
5. the possibility of exceptional orders where the approximant equals the target.

Formal denominator size before cancellation is not enough.