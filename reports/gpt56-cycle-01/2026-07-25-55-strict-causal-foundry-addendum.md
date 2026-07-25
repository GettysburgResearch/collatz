# Addendum — strictly causal foundries do not reduce ordinary extraction

**Agent:** `gpt56-cycle-01`  
**Source claim:** PR `#57/R-7601` at `6131c4768bf52e866829d1ad8ab69a295a90c801`  
**Date:** 2026-07-25  
**Verdict:** `PASSED`; no counterexample claimed

## Exact reconstruction

A strictly causal operator has outputs

\[
E(d)_k=E_k(d_0,\ldots,d_{k-1}).
\]

The foundry equation is

\[
\operatorname{par}(\alpha)=E(\operatorname{dig}(\alpha)).
\]

At binary depth `k`, one fixed residue has two lifts modulo `2^(k+1)`.  The
finite parity-flip lemma from `T-7602` says that the lifts have the same first
`k` shortcut parity bits and opposite parity at time `k`.  Strict causality has
already fixed the desired time-`k` output before digit `d_k` is selected.
Therefore exactly one lift survives.  Induction gives one unique

\[
\alpha_E\in\mathbf Z_2.
\]

This uniqueness theorem is correct.

It is also not a reduction.  Given any prescribed `alpha in Z_2`, define each
`E_k` on the distinguished prefix of `dig(alpha)` to equal the corresponding
bit of `par(alpha)`, and choose all off-path values arbitrarily.  Then `alpha`
satisfies the foundry equation, and uniqueness forces

\[
\alpha_E=\alpha.
\]

Thus unrestricted strictly causal foundries are surjective onto `Z_2`, with
continuum many operators per point.  The computable version is likewise
surjective onto the computable `2`-adic points.

## Tail-property equivalence

Let `P` be any parity-word property invariant under finite changes and
containing `1^infinity`.  The source theorem proves

```text
there exists a uniformly P-admissible causal foundry
with a positive ordinary closure point

iff

there exists a positive ordinary integer
whose actual Collatz parity word already lies in P.
```

The reverse construction sets the distinguished path equal to the witness's
actual parity word and all off-path outputs eventually to one.  Every off-path
output is then a finite modification of `1^infinity`.

For the supercritical frequency property, this becomes an exact equivalence
between a positive supercritical foundry point and a positive integer whose
actual parity word is supercritical.  The foundry syntax has parametrized the
original witness question rather than weakened it.

## Relationship to the new periodic theorem

`T-7501` eliminates autonomous bounded-state schedule generators because their
outputs are eventually periodic.  `R-7601` explains why allowing unrestricted
strictly causal, computable, aperiodic feedback does not automatically help:
such feedback can encode every computable `2`-adic point, including completion
ghosts.

The two results leave one legitimate positive direction:

```text
choose a sharply restricted causal syntax C
and prove from that syntax that its unique closure digits are eventually zero.
```

Without a finite-support or bounded-least-root theorem, searching causal
operators is only a search through a reparametrized `Z_2`.

## Global consequence

This closes another proposed reduction, not another Collatz orbit class.

- Strict causality gives unique inverse-limit extraction.
- Computability gives an effective digit sequence.
- Uniform supercritical output constraints give conditional divergence.
- None gives a positive ordinary boundary point.

The exact missing implication remains

\[
\boxed{
\text{causally generated compatible }\mathbf Z_2\text{ point}
\not\Longrightarrow
\text{eventually-zero binary expansion}.}
\]

A successful foundry theorem must prove eventual zero digits or bounded
canonical least roots for its own restricted operator family.  Otherwise there
is no real reduction from the original ordinary counterexample problem.