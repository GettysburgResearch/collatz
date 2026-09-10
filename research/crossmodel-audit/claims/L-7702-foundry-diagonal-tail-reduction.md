# L-7702 — Correct diagonal tail reduction for foundry integer solutions

**Claim ID:** `L-7702`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-crossmodel-audit-01`  
**Created:** 2026-07-27  
**Dependencies:** the parity-vector bijection and canonical binary expansions, both re-proved in the frozen foundry packet  
**Scope:** arbitrary classes of strictly causal foundry operators  
**Related counterexample candidates:** none

## Statement

Let `C` be any class of strictly causal operators. For each finite canonical binary word `u`, let `[u]_2` be the nonnegative integer with binary expansion `u0^infinity`. Define the paired tail graph

\[
\Gamma_{\mathcal C}
=
\{(u,E(u0^\infty)):E\in\mathcal C,\,u\text{ finite canonical}\}.
\]

Then a nonnegative integer solution exists for some `E in C` exactly when

\[
\boxed{
\exists u,E:
(u,\Phi(u0^\infty))\in\Gamma_{\mathcal C}.}
\]

Equivalently,

\[
E(u0^\infty)=\Phi(u0^\infty).
\]

Any additional orbit property—supercritical parity density, avoidance of one, entry into a named cycle—must be tested on this same diagonal word.

If `C` is countable, then `Gamma_C` and its output projection are countable. No countability conclusion follows for an arbitrary uncountable operator class.

## Proof

A nonnegative integer `n` has a unique finite canonical binary prefix `u` with `digits(n)=u0^infinity`. The foundry closure equation is exactly

\[
E(\operatorname{digits}(n))=\Phi(n).
\]

Substituting the canonical expansion gives the displayed diagonal equality. Conversely, that equality makes `n=[u]_2` a closed-loop solution. Countability is a countable-union argument only when the operator class is itself countable.

## Strategic meaning

Feedback has not vanished. For ordinary integers it is compressed into the **paired relation** between a finite input prefix and its autonomous output tail. Projecting away the prefix destroys the certificate.

A useful search object is therefore not an output-language recognizer alone, but a proof-carrying transducer for intersections of

```text
(input prefix, autonomous output)
```

with the graph of the parity map. This is the smallest corrected version of the foundry program.
