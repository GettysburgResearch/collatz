# Independent review of the ordinary-extraction blocker

**Reviewer:** `gpt56-global-review-01` (`GPT-5.6 Pro`)  
**Issue:** #55, with overlap audit of #54  
**Review branch:** `agent/gpt56-global-review-01/55-extraction-firewall-review`  
**Frozen PR #57 head:** `6131c4768bf52e866829d1ad8ab69a295a90c801`  
**Frozen PR #56 head:** `e42d12e8a9859a917d91870c2490cc1eb87b040f`  
**Date:** 2026-07-25  
**Status:** independent mathematical reconstruction; no counterexample claim

## 1. Executive verdict

The central ordinary-extraction claims are sound.

The repository's repeated missing implication is exactly

```text
for every depth n, some positive integer realizes the first n gates
    + compatible inverse-limit data
    + conditional growth if an ordinary root exists

!=

one fixed positive integer realizes every gate.
```

For a fixed nested architecture the valid replacement is

```text
one ordinary all-time seed exists
iff the least positive depth-n seeds are uniformly bounded
iff those minima eventually stabilize.
```

For one compatible residue branch, positive ordinary extraction is equivalent to eventual stabilization of the canonical least residues, or equivalently eventual zero appended blocks.

The abstract compactness-plus-refund schema cannot prove this missing Archimedean statement. PR #56's `R-7801` constructs arbitrarily expanding exact odd-over-dyadic countermodels with every finite positive cylinder nonempty and no ordinary all-time root. PR #57's `(1110)^infinity` example is a Collatz-native instance. PR #57's new `R-7601` additionally proves that an unrestricted strictly causal Diagonal Foundry is surjective onto the computable `2`-adic points and therefore reparametrizes, rather than solves, ordinary extraction.

The project is therefore not wholly circular, but its positive divergent-orbit lanes have not crossed the ordinary-existence boundary. Their local machinery is useful only insofar as it now supports an attack on least-root stabilization or a full finite return.

## 2. Claim matrix

| Claim | Verdict | Review note |
|---|---|---|
| PR57 `L-7601` signed stabilization | **PASSED** | Canonical positive residues stabilize exactly for nonnegative integers; co-residues stabilize exactly for negative integers. |
| PR57 `T-7601` bounded-minimum extraction | **PASSED** | Elementary nested-set theorem; no compactness or hidden choice assumption. |
| PR57 `T-7602` supercritical ghost | **PASSED** | Finite parity bijection, block map, exact rational orbit, and countability argument reconstruct. |
| PR57 `T-7603` six-branch least-root decision | **PASSED, BRANCH-QUALIFIED** | Abstract decision theorem passes. The six digits and ceiling conjugacy reconstruct algebraically from the PR #45 branch table; source claim statuses are not promoted. |
| PR57 `R-7601` causal-foundry refutation | **SCOPE PASSED** | The unrestricted operator class contains the constant operators and is surjective onto all `2`-adic parity targets; restricted subclasses still require separate analysis. |
| PR56 `T-7801` extraction dichotomy | **PASSED MATHEMATICALLY / SOURCE REPAIR NEEDED** | Same correct theorem; the submitted source contains a malformed `\x0crac` token where `\frac` is intended. |
| PR56 `R-7801` expanding affine countermodel | **PASSED** | The inductive congruence construction and arbitrary expansion estimate are correct. It refutes a proof schema, not a Collatz subsystem. |
| PR57 architecture audit | **SCOPE PASSED** | Strategic classifications are consistent with inspected source boundaries; this is not an independent review of every cited theorem. |

No status is promoted automatically by this review branch.

## 3. Reconstruction of `L-7601`

Let

\[
0\le r_n<K_n,
\qquad
K_n\mid K_{n+1},
\qquad
K_n\to\infty,
\]

with compatible residues. If the inverse-limit value is an ordinary `m>=0`, then once `K_n>m` its canonical representative is exactly `m`, so `r_n` is eventually constant. Conversely, eventual constancy represents that ordinary integer at all late levels and compatibility gives all earlier levels.

For `-m<0`, the canonical residue is `K_n-m` once `K_n>m`; hence `K_n-r_n` is eventually constant. Writing

\[
r_{n+1}=r_n+a_nK_n,
\qquad
q_n=K_{n+1}/K_n,
\]

shows that the positive face is `a_n=0` eventually and the negative face is `a_n=q_n-1` eventually.

This is the exact finite-versus-adic inference repeatedly missing in the repo. Infinitely many zero digits, positive density of zero digits, or very long zero runs do not suffice; the tail must be identically zero.

## 4. Reconstruction of `T-7601`

For nested nonempty positive seed sets

\[
S_0\supseteq S_1\supseteq\cdots,
\qquad
m_n=\min S_n,
\]

the minima are nondecreasing.

- An all-time seed `x` gives `m_n<=x` for every `n`.
- A bounded nondecreasing integer sequence is eventually constant.
- If `m_n=m` eventually, then `m` belongs to every late `S_n`; nesting puts it in every earlier set.

Therefore

\[
\bigcap_nS_n\ne\varnothing
\iff
\sup_nm_n<\infty
\iff
m_n\text{ eventually stabilizes}.
\]

This is a genuine decision theorem for any strict subsystem. A bounded result extracts one concrete seed; divergence of `m_n` eliminates the complete subsystem. The positive existence statement is a sufficient condition for Collatz to be false, not a proposition logically weaker than that negation. The **two-sided restricted decision problem** is narrower than Collatz because its negative outcome concerns only the subsystem.

## 5. Reconstruction of `T-7602`

For a length-`n` parity word, the two lifts of its residue modulo `2^n` differ by `2^n`. After `j<n` shared shortcut steps their values differ by

\[
3^{s_j}2^{n-j},
\]

which is even, while after `n` steps the difference is the odd number `3^{s_n}`. Thus exactly one lift realizes each next bit. Every infinite parity word therefore selects one unique element of `Z_2`.

For `1110`, direct iteration gives

\[
T^4(x)=\frac{27x+19}{16}.
\]

Periodicity and uniqueness force a fixed point,

\[
x=-\frac{19}{11},
\]

with exact orbit

\[
-19/11\to-23/11\to-29/11\to-38/11\to-19/11.
\]

Every finite prefix has infinitely many positive representatives and the block multiplier is `27/16>1`; nevertheless no positive ordinary integer realizes the whole word. This decisively refutes compatibility-plus-growth reasoning.

New `T-7701` strengthens the example to the entire eventually periodic supercritical parity class.

## 6. Reconstruction of the six-branch crosswalk

The abstract part of `T-7603` is an immediate application of `T-7601`. I also reconstructed the submitted six-digit normalization from the exact PR #45 branch table.

The six physical macro equations have

\[
Qh'=Ph+C_i,
\qquad
P=3^{12},
\quad
Q=2^{19},
\]

with

\[
C_i=21\,2^{15-3i}3^{2i}.
\]

Every output boundary is divisible by `3`. Put `h=3x`. Division by three gives

\[
Qx'=Px+a_i,
\qquad
\boxed{a_i=7\,2^{15-3i}3^{2i}.}
\]

For `i=0,...,5`, these are exactly

```text
229376, 258048, 290304, 326592, 367416, 413343.
```

They satisfy `0<a_i<Q`. Hence an integral branch obeys

\[
x'=\left\lceil\frac{Px}{Q}\right\rceil,
\qquad
Qx'-Px=a_i.
\]

Conversely, the congruence determines the unique physical branch residue because

\[
C_i=Qe_i-Pd_i.
\]

Thus the six-branch ceiling crosswalk is algebraically coherent. This review does not promote the underlying PR #45 physical tables beyond their existing status.

## 7. Reconstruction of `R-7801`

PR #56 starts from any compatible nonordinary dyadic residue chain `R_n mod M_n` and any requested expansion factors `Lambda_n`. It inductively chooses an odd `A_n>Lambda_n q_n` and a residue `b_n mod q_n` so that the composed numerator vanishes precisely on the next selected cylinder.

The key invariant is

\[
C_n\equiv-P_nR_n\pmod {M_n}.
\]

Because `P_n` is odd, integrality of the depth-`n` composition is equivalent to

\[
x_0\equiv R_n\pmod {M_n}.
\]

Every finite cylinder therefore contains infinitely many positive integers, and every legal positive step expands by more than `Lambda_n`. The selected mixed-radix digits are neither eventually zero nor eventually maximal, so `L-7601` excludes every signed ordinary all-time root.

The construction is correct and proves a universal negative statement:

> no theorem using only nested dyadic compatibility, exact positive affine replay, and arbitrarily strong refund/expansion can extract an ordinary integer.

It does not prove that any specific Collatz architecture is empty. A successful source-specific theorem may still bound its canonical representatives.

## 8. Diagonal Foundry disposition

PR #57 `R-7601` correctly identifies the unrestricted strictly causal foundry as a parametrization of `Z_2`, not a weaker existence theorem. A constant operator can prescribe any target output parity stream; the parity conjugacy then gives the corresponding unique `2`-adic point. Restricting to computable operators gives every computable `2`-adic point.

For a tail property stable under finite changes, the existence of a positive ordinary fixed point in a uniformly property-valued foundry is equivalent to the pre-existing existence of a positive ordinary Collatz parity word with that property. Thus strict causality and feedback uniqueness do not add the eventual-zero binary tail required by `L-7601`.

This does not eliminate a genuinely restricted operator family with an independently proved bounded-root theorem. It eliminates the unrestricted foundry as a reduction.

## 9. New closure results on this review branch

### `T-7701`

Every eventually periodic shortcut parity schedule whose period has multiplier greater than one has a negative rational realization. Therefore every autonomous finite-state high-drift schedule generator is excluded as a positive counterexample certificate.

### `T-7702`

For finitely many fixed nested architectures,

\[
\bigcap_n\bigcup_iS_n^{(i)}
=
\bigcup_i\bigcap_nS_n^{(i)}.
\]

A finite portfolio has an ordinary survivor only if one constituent already does. Merely retaining several unresolved machines cannot repair extraction; actual cross-machine transitions define a new architecture and need their own least-root theorem.

## 10. Blunt progress assessment

### Genuine progress

The repository has genuinely:

- excluded complete frozen infinite classes, especially the corrected phase-34 architecture;
- independently reconstructed significant theorem chains;
- found and repaired false completion, stack, scaling, and foundry bridges;
- eliminated fixed-modulus, periodic, low-complexity, bounded-support, and fixed-pulse certificate classes;
- built exact finite full-denominator closure criteria for the cycle side;
- reduced several positive lanes to deterministic ordinary machines with explicit finite states.

These are not circular achievements. A negative theorem deciding every member of a strict infinite class is legitimate progress.

### Treading water relative to the full objective

After ordinary extraction has been isolated, the following no longer count as full-objective progress by themselves:

- a longer finite survivor;
- another prescribed infinite schedule;
- another inverse-limit encoding or unrestricted causal foundry;
- increased conditional drift or quotient refund;
- a finite SCC or modular lasso;
- Haar measure, entropy, dimension, or branch-count estimates;
- fresh-prime turnover conditional on an already infinite path;
- another proper denominator factor for a near-cycle.

They matter only when used to prove one of:

```text
bounded canonical least roots,
eventual zero transported blocks,
one explicit forever-defined seed,
a global forced-exit theorem,
or the exact full-denominator cycle equality.
```

At the reviewed cutoff, none of the leading positive divergent-orbit lanes has supplied the first three.

## 11. Consolidation recommendation

PRs #56 and #57 substantially overlap and use the same agent ID in parallel namespaces.

Recommended integration:

1. use PR #57 as the canonical Collatz-native extraction packet because it separates positive and negative boundary faces and contains the explicit raw-parity and foundry refutations;
2. retain PR #56 `R-7801` as the stronger abstract proof-schema countermodel, either by cross-link or by importing it under one noncolliding canonical ID;
3. fix the malformed `\x0crac` token in PR #56 `T-7801`;
4. integrate `T-7701` and `T-7702` after independent review;
5. avoid maintaining two competing least-root ledgers for the same theorem.

## 12. Exact next global target

The cleanest current target is still the six-branch least-root sequence because the machine is fixed, deterministic, and physically expanding whenever defined:

\[
\boxed{
\sup_nm_n<\infty
\quad\text{or}\quad
m_n\to\infty.}
\]

The first outcome yields one explicit restricted root and, after physical replay, a `K-####` candidate. The second eliminates the complete six-branch architecture. Neither outcome is currently proved.

A cross-architecture alternative is acceptable only if it supplies exact physical switching blocks and then decides the least-root sequence of the resulting single machine.

## 13. Review boundary

- No ordinary all-time seed was found.
- No full-denominator positive cycle was found.
- No source theorem is silently promoted.
- The architecture audit remains strategic where its dependencies were not independently reconstructed.
- The new results close certificate classes; they do not resolve the six-branch least-root decision or Collatz.