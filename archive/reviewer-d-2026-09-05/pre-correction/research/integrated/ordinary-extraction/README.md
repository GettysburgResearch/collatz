# IC-EXTRACT-001 — ordinary extraction by stabilization

## Status

- **Mathematical status:** `VERIFIED` in the stated scope.
- **Repository role:** accepted integrated reference after merged PR #84.
- **Proof residency:** local proof packet.
- **Collatz status:** does not prove or disprove Collatz.

This packet combines two elementary reviewed results from PR #57: the signed canonical-residue criterion and the bounded-minimum criterion for nested positive survivor sets. The conjunction is editorial; no new mathematical strengthening is intended.

## Setup and notation

Let

\[
1=K_0\mid K_1\mid K_2\mid\cdots,
\qquad K_n\to\infty,
\]

and let

\[
0\le r_n<K_n,
\qquad r_{n+1}\equiv r_n\pmod{K_n}.
\]

The compatible residues define one inverse-limit point `α`. Put

\[
q_n=K_{n+1}/K_n,
\qquad
a_n=\frac{r_{n+1}-r_n}{K_n}.
\]

Separately, let

\[
S_0\supseteq S_1\supseteq S_2\supseteq\cdots
\]

be nonempty subsets of the positive integers, where `S_n` means that the **same initial seed** satisfies the complete first `n` conditions. Put

\[
m_n=\min S_n.
\]

## Theorem A — signed stabilization criterion

The inverse-limit point `α` is a signed ordinary integer exactly on an eventual boundary face:

1. `α` is a nonnegative ordinary integer if and only if `r_n` is eventually constant, equivalently `a_n=0` eventually.
2. `α` is a negative ordinary integer if and only if `K_n-r_n` is eventually constant, equivalently `a_n=q_n-1` eventually.
3. Therefore `α∈Z` exactly when its mixed-radix tail is eventually all zero or eventually all maximal.

### Proof

Suppose first that `α=m` for an ordinary integer `m≥0`. Since `K_n→∞`, choose `N` such that `K_n>m` for every `n≥N`. The canonical least representative of `m` modulo `K_n` is then `m` itself, so

\[
r_n=m\qquad(n\ge N).
\]

Conversely, if `r_n=m` for every sufficiently large `n`, the compatible inverse-limit point is the image of the ordinary integer `m`.

Because

\[
r_{n+1}=r_n+K_na_n,
\]

this eventual constancy is equivalent to `a_n=0` eventually.

Now suppose `α=-m` for an ordinary integer `m≥1`. Once `K_n>m`, the canonical least representative of `-m` modulo `K_n` is

\[
r_n=K_n-m.
\]

Hence `K_n-r_n=m` eventually. Conversely, eventual constancy of `K_n-r_n=m` means that all sufficiently large residues represent `-m`, so the inverse-limit point is `-m`.

Finally,

\[
\begin{aligned}
K_{n+1}-r_{n+1}
&=q_nK_n-r_n-K_na_n\\
&=(K_n-r_n)+K_n(q_n-a_n-1).
\end{aligned}
\]

Thus the positive co-representative is unchanged exactly when `a_n=q_n-1`. Every ordinary integer is either nonnegative or negative, proving the classification. ∎

## Theorem B — bounded-minimum ordinary compactness

For the nested positive survivor sets `S_n`, the following are equivalent:

1. one positive ordinary seed survives every depth:
   \[
   \bigcap_{n\ge0}S_n\ne\varnothing;
   \]
2. the least finite-depth witnesses are uniformly bounded:
   \[
   \sup_n m_n<\infty;
   \]
3. `(m_n)` eventually stabilizes;
4. some finite set of positive integers meets every `S_n`.

Consequently, when every finite level is nonempty, exactly one of the following occurs:

```text
ordinary extraction:
    m_n eventually stabilizes at one all-depth seed;

ordinary escape:
    m_n -> infinity and the all-depth intersection is empty.
```

### Proof

Nestedness gives

\[
m_0\le m_1\le m_2\le\cdots.
\]

If `x` belongs to every `S_n`, then `m_n≤x` for every `n`, so the minima are bounded.

A bounded nondecreasing sequence of positive integers is eventually constant. Suppose `m_n=m` for every `n≥N`. By definition, `m∈S_n` for every `n≥N`. Since `S_N` is contained in every earlier set, `m` belongs to all `S_n`, proving existence of one all-depth seed.

A finite set meeting every level gives a uniform bound. Conversely, if `m_n≤B` for every `n`, the finite set `{1,…,B}` meets every level. The final dichotomy follows because an unbounded nondecreasing integer sequence tends to infinity. ∎

## Why this matters

These theorems isolate the exact inference missing from many finite-prefix constructions. Neither

- infinitely many representatives at every depth,
- a unique compatible 2-adic point,
- positive affine growth along legal finite prefixes,
- nor a large changing-radix stack

supplies one positive ordinary all-depth seed without a canonical Archimedean bound.

For a concrete architecture, a bounded least-root theorem is already a structured positive construction. A least-root escape theorem eliminates the complete declared architecture.

## Boundaries and common misreadings

- Compatibility is not stabilization.
- Infinitely many zero digits are not enough; the tail must be eventually zero.
- The maximal-digit face represents negative integers and cannot be counted as a positive construction.
- Different witnesses `x_n` at different depths do not prove a single witness.
- Conditional growth of a seed already in the intersection does not establish that the intersection is nonempty.
- A branch may be ordinary only if the residues are the canonical representatives of the **complete pulled-back legality conditions**.
- If one finite level is empty, the architecture is excluded before this theorem is needed.

## Adversarial examples

1. `S_n={n,n+1,…}` has nonempty finite levels, `m_n=n`, and empty intersection.
2. `S_n={7,7+K_n,7+2K_n,…}` has constant minimum `7` and an all-depth survivor.
3. Compatible residues of a nonordinary 2-adic point produce nonempty infinite finite-depth sets while their canonical positive minima escape.
4. A long run of zero appended blocks followed by infinitely many nonzero blocks remains nonordinary.

## Provenance

### Primary source

PR #57 at

```text
f12e6ec45a88da98b64ef97bdfd25c3c7d48b435
```

Files:

```text
research/ordinary-extraction/claims/D-7601-nested-legal-cylinder-tree.md
research/ordinary-extraction/claims/L-7601-signed-stabilization.md
research/ordinary-extraction/claims/T-7601-bounded-minimum-extraction.md
```

Source authorship: `gpt56-global-01`.

### Independent review evidence

```text
research/positive-coefficient-gate/reviews/PREPUBLIC-PR56-PR57-PR60.md
@ 1c25b5e4be25a7c73b78e80b505c54879f02d8f1
```

The review independently reconstructed the mathematical core and classified the containing packages `VERIFIED WITH FIXES`. This integrated packet does not extend the verdict to later PR #57 additions.

### Overlapping formulations retained as alternatives

- PR #3 `T-0043` at `caa775e85a3618a6cce0bbad345300aaefeab640`.
- PR #56 `T-7801` at `53ed4e49be522052405e6aa2c11b2b810a01bf2a`.
- PR #60 `T-7401` at `1221ef5639bd89b56a0583a58f0b2fc63af52931`.

These are overlapping proofs or formulations, not separate canonical theorems. Branch-qualified IDs remain necessary because the repository contains collisions.

## Next missing step

Choose one concrete aperiodic architecture and prove

\[
\sup_n m_n<\infty
\quad\text{or}\quad
m_n\to\infty.
\]

Do not replace this with another prescribed infinite word, longer finite prefix, or conditional growth lemma.
