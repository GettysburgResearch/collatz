# LIT-KTHM-0028 — Causal conjugacy fixed points in `Z_2`

**Type:** known corollary with complete proof.  
**Sources:** Bernstein--Lagarias conjugacy; Banach fixed-point theorem.  
**Maps to:** `FOUNDRY/L-9601`, `FOUNDRY/T-9601`.

## Statement

Let `T:Z_2->Z_2` be the shortcut Collatz map and let

```text
Q(x) = sum_(k>=0) (T^k(x) mod 2) 2^k
```

be the parity-vector map. Let `Phi=Q^(-1)`. Bernstein--Lagarias prove that `Phi` is an isometry and conjugates the `2`-adic shift to `T`.

Let

```text
E: Z_2 -> Z_2
```

be **strictly causal** in binary digits: output digit `k` depends only on input digits `0,...,k-1`.

Then:

1. `E` is `1/2`-Lipschitz in the `2`-adic metric;
2. `F=Phi o E` is a strict contraction;
3. there is a unique `alpha_E in Z_2` satisfying
   ```text
   Q(alpha_E)=E(alpha_E);
   ```
4. for every starting point `x_0`, the iteration
   ```text
   x_(n+1)=Phi(E(x_n))
   ```
   converges to `alpha_E`, gaining at least one correct binary digit per iteration.

## Proof

If

```text
x = y mod 2^k,
```

then their input digits below position `k` agree. For every output position `j<=k`, strict causality says that output digit `j` depends only on input positions below `j`, hence only on positions below `k`. Therefore

```text
E(x)=E(y) mod 2^(k+1).
```

Equivalently,

```text
|E(x)-E(y)|_2 <= (1/2)|x-y|_2.
```

Since `Phi` is an isometry,

```text
|Phi(E(x))-Phi(E(y))|_2
 = |E(x)-E(y)|_2
 <= (1/2)|x-y|_2.
```

Thus `F=Phi o E` is a contraction on the complete metric space `Z_2`. Banach's theorem gives a unique fixed point `alpha_E` and convergence of every iteration to it. Finally,

```text
alpha_E=Phi(E(alpha_E))
```

is equivalent, after applying `Q`, to

```text
Q(alpha_E)=E(alpha_E).
```

The contraction estimate shows that each iterate gains at least one binary digit. ∎

## Applicability

This supplies a short external proof of the Foundry existence/uniqueness theorem and explains the native flip construction as digitwise contraction iteration.

It does **not** prove that `alpha_E` is rational, an ordinary integer, positive, or dynamically supercritical. Those are the Foundry program's native questions.

## Literature boundary

Anashin's automata theory identifies digit-transducer functions with `1`-Lipschitz maps and characterizes finite-state cases using van der Put coefficients. Strict causality is the stronger `1/2`-Lipschitz condition used here. Finite-state realizability does not imply that the fixed point is ordinary.