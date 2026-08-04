# T-0105 — All chronological Minkowski tensors freeze sub-scale filled radius

Claim ID: `T-0105`  
Title: \(D\mapsto D+2^{L}E\) never increases filled radius below scale \(2^{L}\)  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `T-0104`  
Scope: arbitrary finite integer offset alphabets \(E\) (any weight suffix)  
Related counterexample candidates: none (strengthened obstruction)

## Statement

Let \(D_0\subset\mathbb Z\) be finite and \(L\ge0\). Let \(E\subset\mathbb Z\) be any
nonempty finite integer set (the normalized suffix offsets in the tensor law
\(D_{UV}=D_U+2^{L_1}E_V\)). Put

\[
D_1=D_0+2^{L}E.
\]

Then every nonzero element of \(2^{L}(E-E)\) has absolute value at least
\(2^{L}\). Consequently

\[
\bigl((D_1-D_1)\setminus(D_0-D_0)\bigr)\cap(-2^{L},2^{L})=\emptyset.
\]

Therefore, if \(R(D_0)<2^{L}\),

\[
\boxed{R(D_1)=R(D_0).}
\]

In particular, **no** chronological tensor suffix — atomic, weight-two,
weight-three, or otherwise — can grow the filled difference radius of a seed
chart whose radius lies below the current length scale \(2^{L}\).

This strictly generalizes `T-0104` (which treated atomic two-point \(E\)).

## Motivation

`X-0120` found weight-three suffixes with \(R(E)\ge1\) at moderate precision,
suggesting a growing-geometry escape. The escape fails: scaling by \(2^{L}\)
produces a comb with gaps of size \(2^{L}\), not a filled interval of radius
\(R(E)2^{L}\). Empirically `X-0124` shows post-tensor \(R\) stuck at the seed
radius despite \(R(E)=2\).

## Proof

\(D_1-D_1=(D_0-D_0)+2^{L}(E-E)\). If \(x\in 2^{L}(E-E)\) is nonzero, then
\(x=2^{L}(e_1-e_2)\) with \(e_1\neq e_2\), so \(|x|\ge2^{L}\). Hence no new
differences appear in the open interval \((-2^{L},2^{L})\). If the seed filled
radius is already \(<2^{L}\), it cannot increase.

## Dependency audit

- Tensor shape from the collision-code concatenation law (integer \(E\)).
- Special case atomic: `T-0104`.

## Gap audit

- Does not forbid growth of **sparse** large-scale geometry (e.g. surjectivity
  modulo primes, or difference sets with large holes).
- Does not forbid non-Minkowski / non-concatenative chart changes.
- Growing \(R\) above scale \(2^{L}\) in the comb sense is possible but is not
  the filled-interval resource used for local carry repair.

## Adversarial tests

`X-0124`: seed \(R=3\), \(L=6\), weight-3 \(R(E)=2\); post-tensor \(R=3\)
still (not \(128\)).

## Suggested next attack

Abandon filled-radius growth via chronological tensoring. Seek either
non-concatenative geometry growth or a different closure resource (cycle /
heteroclinic paths already opened).
