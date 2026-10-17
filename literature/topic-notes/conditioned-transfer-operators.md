# Conditioned transfer operators and rare Collatz events

## Repo object

Issue #8 proposes conditioning finite parity/valuation dynamics on a rare long-growth event and looking for persistent `3`-adic or Fourier structure. The exact state includes the valuation sum and affine correction, not parity alone.

## Standard finite-state theorem

For a frozen finite Markov/additive model, exponential tilting produces a matrix `P_s` with

```text
E exp(s G_n) = mu P_s^n 1.
```

Chernoff and Perron–Frobenius bounds then give a rigorous finite-state rate estimate; see `LIT-KTHM-0026`.

## Relation to Tao

Tao's almost-all theorem uses `3`-adic mixing and Fourier decay in a carefully chosen stochastic/first-passage framework. It demonstrates that these tools are relevant to Collatz. It does not prove that the conditioned exceptional ensemble in issue #8 has a persistent mode, nor that a mode yields one ordinary exceptional orbit.

## Required normalization audit

A theorem-quality computation must state:

- state space and truncation;
- base transition multiplicities;
- additive observable;
- tilt parameter and normalization/Doob transform;
- boundary treatment;
- exact relationship between conditioned samples and the matrix model;
- certified spectral data;
- dependence of constants on modulus and depth.

## Ordinary-integer boundary

A nested compatible residue family defines a `2`-adic integer. To obtain one ordinary positive integer, least nonnegative representatives must eventually stabilize. Merely converging in `Z_2`, or obtaining arbitrarily long finite prefixes, is insufficient.