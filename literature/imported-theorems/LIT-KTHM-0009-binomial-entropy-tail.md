# LIT-KTHM-0009 — entropy bound for a supermajority binomial tail

**Source:** standard entropy estimate for binomial coefficients
**Proof status:** complete proof
**External status:** FOLKLORE / STANDARD

## Statement

Let `1/2<delta≤1`, and let `L≥1`. Write

```text
H(x) = -x log_2 x - (1-x) log_2(1-x).
```

Then

```text
sum_{a=ceil(delta L)}^L binom(L,a)
  ≤ (L+1) 2^(L H(delta)).                         (1)
```

Consequently, if a finite digit family `D_L` injects into binary words of length `L` whose weight is at least `delta L`, then

```text
L - log_2 |D_L|
  ≥ (1-H(delta))L - log_2(L+1).                   (2)
```

## Proof

For `x=a/L`, the binomial theorem applied with probabilities `x` and `1-x` gives

```text
1 ≥ binom(L,a) x^a (1-x)^(L-a).
```

Hence

```text
binom(L,a)
 ≤ x^(-a)(1-x)^(-(L-a))
 = 2^(L H(x)).                                    (3)
```

On `[1/2,1]`, `H` is decreasing. Therefore every `a≥delta L` satisfies `H(a/L)≤H(delta)`. There are at most `L+1` summands, so (3) yields (1). Taking base-two logarithms of `|D_L|≤` the left side of (1) gives (2). ∎

## Native mappings

For a supercritical parity word, `3^a>2^L` implies

```text
a/L > log_3 2.
```

If the native collision argument injects one branch per such word, (2) gives the asymptotic cost floor in `CLAUDE/T-0014` with `delta=log_3 2`.

## Non-applications

This theorem bounds the total number of supercritical words. It does not estimate how those words partition into equal-endpoint collision fibers and gives no lower bound on the largest fiber.
