# O-7401 — Preimage gates canonicalize the covered first-crossing source but do not beat the quadratic mechanical threshold

**Claim ID:** `O-7401`  
**Status:** `PROPOSED` pending independent review  
**Authoring agent:** `gpt56-complexity-01`  
**Date:** 2026-08-01  
**Context:** pre-public review of frozen PRs #76, #77, and #79  
**Dependencies:** branch-qualified proposed `T-6701`, `T-6710`, `T-6602`, and `R-6601`

## Statement

Assume the branch-qualified least-counterexample setup from PRs #76--#79. Let `n` be the least positive Collatz counterexample, let `j<infinity` be its first coefficient-crossing time, and suppose the endpoint class is one of

```text
2, 4, 5, 8 modulo 9.
```

Then the preimage bounds proposed in `T-6602` imply

```text
j > log_2(n).
```

Consequently

```text
n < 2^j,
```

so `n` is not merely a member of the length-`j` parity cylinder: it is that cylinder's canonical positive source in `{1,...,2^j}`. The fixed-source valuation formulation in `T-6710` therefore applies with no change of representative.

However, combining this canonicalization with the method boundary `R-6601` does not yet produce a contradiction. The weakest covered preimage inequality gives only

```text
n = O(j),
```

whereas the unconstrained upper-mechanical no-descent threshold grows at least as

```text
Omega(j^2).
```

Thus the two inequalities are directionally compatible for large `j`. Closing the delayed-crossing lane still requires either cofinal merge exclusion, a substantially smaller ordinary-cylinder threshold, or a source-specific restriction showing that the actual word cannot remain near the mechanical extremizer.

## Proof

Among the four covered endpoint classes, the weakest lower bound in `T-6602` is

\[
 j>{n+5\over4\alpha},
 \qquad
 \alpha={\log2\over\log3}<1.
\]

Hence

\[
 j>{n+5\over4}.
\]

The imported floor `T-6701` gives `n>N_*>16`. The real function

\[
 f(x)={x+5\over4}-\log_2x
\]

is positive for `x>16` (for example, its derivative is positive there and `f(16)=5/4`). Therefore

\[
 j>{n+5\over4}>\log_2n,
\]

which proves `n<2^j`.

Every length-`j` parity word occupies exactly one residue class modulo `2^j`. Since `n` realizes the first-crossing word and lies in `{1,...,2^j}`, it is the canonical positive representative of that class.

For the non-closure statement, rearranging the weakest `T-6602` inequality gives `n<4\alpha j-5`, hence `n=O(j)`. By `R-6601`, the real no-descent threshold of the unconstrained upper-mechanical word is bounded below by a positive constant times `j^2` along the relevant lower convergents. An `O(j)` source is not excluded by an `Omega(j^2)` upper threshold. No contradiction follows from these two estimates alone. ∎

## Status boundary

- This observation is conditional on the cited proposed source claims.
- It does not verify or repair those claims retroactively.
- It does not close any residue class or prove Collatz.
- Its role is to connect the canonical-source formulation of PR #77 with the preimage barriers of PR #79 and to prevent an invalid claim that the existing linear and quadratic estimates already collide.
