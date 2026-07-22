# LIT-KTHM-0043 — Nondegenerate finite-rank multiplicative equations have finitely many solutions

**Type:** external black-box theorem with a native applicability checklist.  
**Source:** J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt, *Linear Equations in Variables Which Lie in a Multiplicative Group*, Annals of Mathematics 155 (2002), 807–836.  
**Maps to:** fixed-word cap-stitch equations in PR #3/PR #33 and successive H-core compatibility equations in PR #19/PR #34.

## External theorem

Let `K` be a field of characteristic zero, let

```text
a_1,...,a_n in K^*,
```

and let `Gamma` be a finite-rank subgroup of

```text
(K^*)^n.
```

Consider

```text
a_1 x_1 + ... + a_n x_n = 1,                       (1)
```

with

```text
(x_1,...,x_n) in Gamma.
```

A solution is **nondegenerate** when no nonempty proper subsum of the left side of `(1)` vanishes.

Then `(1)` has only finitely many nondegenerate solutions. The source proves an explicit bound depending only on `n` and the rank of `Gamma`.

The proof is imported as a black box.

## Why this theorem is relevant

Several current branch equations are finite sums of quantities assembled from powers of `2`, powers of `3`, and finitely many rational coefficients. If a frozen symbolic word turns such an equation into

```text
c_1 2^(u_1)3^(v_1)
 + ...
 +c_n 2^(u_n)3^(v_n)
 =1,                                                 (2)
```

with fixed nonzero rational `c_i`, then the variable tuple lies in a finite-rank multiplicative group. The theorem can make the set of nondegenerate exponent tuples finite.

This is potentially decisive when an infinite Collatz construction would force infinitely many distinct solutions of the **same** frozen equation.

## Native application checklist

The theorem may be invoked only after all of the following are supplied.

1. **One fixed equation.** The number of terms and rational coefficients must not change with scale.
2. **Finite-rank group.** Every variable term must be placed in one explicitly defined finite-rank multiplicative group.
3. **Injective parameter map.** Distinct scales or stages must yield distinct group solutions, or the native argument must explain why infinitely many stages force infinitely many solutions.
4. **Proper-subsum audit.** Every possible vanishing proper subsum must be classified. Degenerate families are not covered by the finiteness conclusion.
5. **Finite symbolic alphabet argument.** If the equation depends on a finite word pair, an infinite directive must first be reduced to one pair occurring infinitely often with the same equation.
6. **Ordinary realization boundary.** Finiteness of exponent tuples does not by itself prove that a `2`-adic completion is nonordinary; the exact native contradiction must be written.

## Candidate PR #3 / PR #33 use

The late corrected-stage problem is

```text
S_m(w_m)=R_(m+1)(w_(m+1)).                          (3)
```

For one fixed pair `(w,w')`, derive an exact closed expression for both sides in powers of `2` and `3`. If `(3)` becomes a fixed nondegenerate equation of the form `(2)`, then the source theorem allows only finitely many scales for that pair.

Because the stage-word alphabet is finite, an infinite stitch sequence repeats some word pair infinitely often. A uniform native reduction of every pair to the theorem would therefore exclude every infinite stitch tail.

This is a strategy, not a completed application: the current repository has not yet exposed the fixed finite-term expression or classified its degeneracies.

## Candidate H use

The successive-core equation in `SYN/L-9894`,

```text
8^R 4^b Y - 9^R 3^a X = 9^R - 8^R,                (4)
```

becomes an S-unit equation only after the prime supports of `X` and `Y` are controlled. Splitting those variables into persistent and fresh prime mass may isolate a finite-rank part to which the theorem applies.

Again, the proper-subsums and the contribution of fresh primes must be audited explicitly.

## Nonconsequences

This theorem does not say that:

- every equation involving powers of `2` and `3` has finitely many solutions;
- degenerate proper-subsum families are finite;
- coefficients may vary freely with scale;
- a finite set of `2`-adic residues contains no ordinary integer;
- or the Collatz conjecture follows from the phrase “S-unit equation.”
