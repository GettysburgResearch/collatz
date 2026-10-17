# L-8811 — Finite low-digit cylinders have infinitely many positive roots

Claim ID: L-8811  
Title: Every finite legal `4 -> 5` chart word is realized by infinitely many positive roots  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8806, T-8807, L-8804  
Scope: every finite binary bottom-word prefix in the exact base-`5/4` chart  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let

```text
tau(x)=ceil(5x/4),
b(x)=(-x) mod 4 in {0,1,2,3}.
```

For every word

```text
w=w_0...w_(n-1) in {0,1}^n
```

there is a unique residue class `r_w modulo 4^n` such that every nonnegative
integer

```text
X congruent r_w (mod 4^n)
```

has

```text
b(tau^j(X))=w_j,  0<=j<n.
```

Consequently, every finite low-digit word is realized by infinitely many
positive roots `X`, and therefore by infinitely many positive physical starts
`A=X-1` once `X>=2`.

Equivalently, if `eps_j=1-w_j` is the phase normalization used in `T-8802`,
every finite phase directive has infinitely many positive physical
representatives.

## Motivation

This proves a strict limitation on finite obstruction searches. A finite word
may fail to extend from one particular root, but no finite word over the legal
alphabet is intrinsically impossible. Global extinction must preserve the
coherence of one ordinary root through unbounded depth.

## Proof

`T-8807` proves that length-`n` directive prefixes occupy exactly `2^n`
distinct residue classes modulo `4^n`, one for each binary prefix. Translating
between its phase digit `eps` and the bottom digit `w=1-eps` is a coordinatewise
bijection, so there is exactly one residue class `r_w modulo 4^n` for the chosen
bottom word.

Alternatively, solve the inverse branches successively. At each step the edge
identity

```text
4*x_(j+1)=5*x_j+w_j
```

has a unique solution for `x_j modulo 4^(n-j)` because `5` is invertible modulo
every power of four. This yields the same unique initial class.

Now take one representative `r_w` in `[0,4^n)`. By the cylinder-affine identity
of `L-8804`, for every integer `t>=0`,

```text
tau^j(r_w+4^n*t)
 =tau^j(r_w)+5^j*4^(n-j)*t,
```

for `0<=j<=n`. Before step `n`, the added term is divisible by `4`, so the
bottom digit at each of the first `n` steps is unchanged. Hence all integers

```text
r_w+4^n*t
```

follow the same word. Taking arbitrarily large `t` supplies infinitely many
positive roots, and taking `X>=2` makes `A=X-1` positive. **QED**

## Dependency audit

- `T-8806` supplies the physical/root shift and bottom-digit interpretation.
- `T-8807` supplies one distinct residue class per binary prefix.
- `L-8804` supplies exact preservation under addition of `4^n*t`.

Only one of the last two existence proofs is logically necessary; both are
recorded as cross-checks.

## Gap audit

- The theorem is finite-depth only.
- The positive representative may depend on the depth and the word.
- Compatible representatives for all prefixes of one infinite word determine a
  `2`-adic point, but need not stabilize to one ordinary positive integer.
- The result does not construct an infinite survivor.

## Adversarial tests

`X-8802` replays the physical/tree correspondence for more than one million
bounded edges. `X-8803` independently materializes the complete finite
frontiers used by `L-8804`.

## Remaining uncertainty

None known in the finite cylinder statement. The infinite one-root coherence is
exactly `Q-8801`.

## Suggested next attack

Any negative search should track least ordinary representatives or a monotone
height invariant, rather than trying to forbid a finite binary word.
