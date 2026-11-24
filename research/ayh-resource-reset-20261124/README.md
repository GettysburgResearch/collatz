# Aaronson–Yolcu–Heule: nonlinear interpretations and a sparse ordinary section

**Collatz remains OPEN.** This packet attempts the global termination and ordinary-source closure steps. Its two main results are a checked obstruction to a broad nonlinear interpretation class for the full eleven-rule system, and a checked global reduction to a sparse set of marked inputs with a forced power-size descent. Neither result supplies a terminating interpretation or the final descent below the original source.

The principal Lean theorems and all their supporting modules were compiled with Lean 4.34.1 and warnings treated as errors. The combined audit lists 29 new public theorem declarations; their axiom dependencies are subsets of `propext`, `Classical.choice`, and `Quot.sound`. The proofs and evidence below distinguish the checked declarations from written extensions and external results. [Execution record and review](../../reports/ayh-resource-reset-20261124/README.md).

## 1. The nonlinear rank obstruction

Use the authors' ASCII alphabet: `a,b` are binary zero and one, `e,f,g` are ternary zero, one and two, and `c,d` are the left and right delimiters. The complete rules are

```text
ad -> d      bd -> gd
ae -> ea     af -> eb     ag -> fa
be -> fb     bf -> ga     bg -> gb
ce -> cb     cf -> caa    cg -> cab
```

Interpret symbols by functions on positive integer triples. Weak comparison is coordinatewise. Strict comparison additionally requires strict inequality in coordinate zero. Every symbol must preserve both comparisons. **Only the binary-zero symbol `a` needs to be polynomial:** its three outputs are nonzero polynomials with nonnegative integer coefficients. The other six symbol maps may be arbitrary functions preserving the two comparisons. Polynomial degree is unrestricted, and auxiliary coordinates can reset to positive constants.

**Checked theorem.** If this interpretation weakly orients all eleven rules, it cannot strictly orient even one of them. Dimensions one and two are included by padding with constant-one coordinates. The compiled theorem is `PositivePolynomialBarrier.no_strict_rule` in [PositivePolynomialBarrier.lean](PositivePolynomialBarrier.lean).

### Why it works

A nonzero polynomial on positive integers is at least every variable that occurs in it. Strictness in the first coordinate forces the first output of `a` to use its first input. Follow dependencies among the other two coordinates: a self-dependency is increasing, a two-coordinate cycle is increasing every two steps, and an acyclic dependency inherits the first coordinate's increase after at most two steps. Thus, for the map `A` interpreting `a`,

\[
A^2(x)\le A^4(x)
\]

coordinatewise, for every positive triple. [PolynomialPump.lean](PolynomialPump.lean) proves this for a syntax covering all the stated polynomials.

Now replay the actual shortcut trajectory

\[
41\to62\to31\to47\to71\to107\to161.
\]

Its 32 individual string rewrites use **all eleven rules** and have endpoints

\[
\texttt{c a b a² b d}\quad\longrightarrow^*\quad
\texttt{c a b a⁴ b d}.
\]

Weak rule orientation makes the final interpretation at most the initial one; a strict orientation of any rule makes it strictly smaller. The polynomial comparison inside the unchanged context gives the opposite weak comparison. This is a contradiction. [SelfEmbedding.lean](SelfEmbedding.lean) checks the literal trace and the generic ordered-algebra implication. It does not assume convergence of 41, or of any other integer, as a theorem.

An independent internal review reconstructed the polynomial argument, replayed the ASCII rules, and checked the exact source hashes. [Review](../../reports/ayh-resource-reset-20261124/POLYNOMIAL_TRACE_REVIEW.md).

### Exact limits

The positive cone is essential to the proof as formalized. Identically zero auxiliary outputs, orders other than the stated distinguished-coordinate order, transformed or restricted rule systems, and arbitrary dimension are not excluded by this theorem. A separate written proof handles the whole nonnegative orthant in dimension three, including zero auxiliary outputs, using a 308-step all-rule trace from 515 to 2051. It has an [independent mathematical review](../../reports/ayh-resource-reset-20261124/ZERO_FACE_REVIEW.md). The mathematical reverse-word argument and a positive-orthant extension through dimension five also have written proofs in [GLOBAL_METHODS.md](GLOBAL_METHODS.md); the headline machine-checked polynomial result is dimension three on positive coordinates. This is an obstruction to a proof method, not a divergent Collatz orbit.

## 2. A positive global theorem: sparse marked predecessors

Write `T(n)=n/2` on even integers and `T(n)=(3n+1)/2` on odd ones. For `d=floor(log₂ n)`, retain PR 173's mark

\[
n\text{ odd},\qquad(d+1)(n-2^d)\le70\,2^d.
\]

Let

\[
S=\{n\text{ marked}:5v_2(3n+1)\ge d+1\}.
\]

**Checked theorem.** For every positive target `q` not divisible by three and every bound `L`, there is an `n>L` in `S` with a physical prefix consisting of one odd step and subsequent halvings to an endpoint `u` such that

\[
u^5\le4^5n^4,
\qquad T^j(u)=q\text{ for some }j.
\]

The endpoint can be even. This is one ordinary predecessor of the original `q`; the construction does not change the target between finite witnesses. The theorem is cofinal in `L`, and the same file proves the closed equivalence

\[
\text{every positive integer reaches 1}
\quad\Longleftrightarrow\quad
\text{every }n\in S\text{ reaches 1}.
\]

See `cofinal_marked_power_predecessors` and `universal_iff_marked_power` in [InversePowerRows.lean](positive-section/InversePowerRows.lean). The formal statement uses an existential halving exponent instead of a valuation convention.

The construction combines a four-clock inverse lift with a one-sided rational rotation grid. It simultaneously places the high bits in the narrow mark and forces an initial prefix of at least one fifth of the input bit length in shortcut clocks, ending at `u <= 4 n^(4/5)`. The odd numerator contributes up to two extra bits, so the guaranteed net bit-length drop is at least the prefix length minus two. Its exact phase-error estimate, arithmetic attachment, physical orbit, and global equivalence are all formalized. [Full proof and source pins](positive-section/README.md).

The written counting argument bounds the number of candidates per octave by

\[
1+\frac{70\,2^{d-\lceil(d+1)/5\rceil}}{d+1}.
\]

A separate written extension permits any fixed odd binary suffix in a marked predecessor of the same target. Its arithmetic gluing is checked in Lean; the full fixed-suffix extension and the octave count are written proofs. The fixed suffix and the growing valuation constraint are separate conclusions.

### The attempted closing step and the precise obstruction

In the actual construction, `u >= 2^Q q`, where `Q` is the rotation denominator. A large drop from `n` therefore need not produce a number below the original `q`. The Lean arithmetic also proves

\[
u\ge q,\quad u\le4n^{4/5}
\quad\Longrightarrow\quad q^5\le4^5n^4.
\]

Thus an inverse construction with these properties cannot give a representative of size `O(q^(5/4−ε))` on unbounded targets. Such a bound, if supplied by a different same-component selector, would combine with the power descent to give induction on sufficiently large elements of `S`, after resolving the finite base. This packet supplies no such selector. The theorem reduces the all-input problem and identifies a failed closing mechanism; it does not discharge that problem.

## 3. Other proved structure and nonlinear transfer

The same exploration produced complementary results, with their evidence levels kept explicit.

| Result | Scope and evidence |
|---|---|
| Scalar rigidity | Arbitrary strictly increasing maps `N -> N` weakly orienting the full system force all five digit maps to be identity, in both composition orders. Standard-library Lean proof; [proof](SCALAR_RIGIDITY.md). |
| Extensive-algebra obstruction | A 29-step all-rule derivation from `cbabbd` to `ceababbd` ends in a supersequence of its start. No context-compatible extensive interpretation weakly orienting all eleven rules can make any rule strict. Checked generic theorem and literal witness. |
| Returning matrix paths | Six nonnegative carry defects sum to a commutator; its trace against every power of the digit sum is zero. Every defect vanishes on a returning digit path. Checked in [CarryTrace.lean](CarryTrace.lean). |
| Boundary reset control | An explicit full-system weak matrix interpretation has digit defect `J` with `J²=0` but `JCJ=J`. This prevents applying digit-only nilpotence across a boundary reset. Exact arithmetic control and written explanation. |
| Monomial-to-affine equivalence | For every finite SRS, positive multivariate monomial interpretations and natural affine interpretations realize the same weak and marked-strict orientations in each dimension. Written constructive proof and exact [compiler](monomial_transfer.py), with equality-preserving prime weights. |
| Two-base semantic ranks | Bell's theorem plus an explicit expanding ordinary segment excludes semantic ranks simultaneously regular in bases two and three that weakly decrease at every step and strictly decrease on all even inputs or on all odd inputs. Source-qualified written proof; it requires representation invariance. |

The proofs, countermodels, larger-dimensional limits, and exact next interfaces are in [GLOBAL_METHODS.md](GLOBAL_METHODS.md).

## 4. Relation to earlier work and current literature

PR 6 recorded the original natural/arctic frontier and missing legacy proofs. PR 153 obtained a run-guarded termination result. PR 183 normalizes the one-rule deletion system and isolates a blocked ordinary merger; restoring the missing rule need not decrease its rank. We retain those distinctions. This packet does not import an old conditional claim as a solution.

The refreshed literature also contains Nashida's later [natural/arctic barrier repository](https://github.com/harappa/collatz-arctic-interpretation-barriers/tree/de961be6671b2084ae0189a3572b674c60788456), whose `paper_thm_9_2_T` states the all-dimensional natural-matrix no-removal theorem. We inspected the pinned primary source and its verification scope but did not rebuild that external development. Our checked three-coordinate **nonlinear polynomial** theorem and the ordinary predecessor theorem do not depend on it. The monomial transfer is independent; its Collatz corollary inherits the exact external barrier hypotheses and verification status.

The latest PRs through 191 were used to locate the active frontier. In particular, finite rational-phase, repeated-word, substitution, and denominator results do not establish arbitrary-source termination. We did not re-audit all of those branches. [Inspection ledger](SOURCES.json).

## Replay

From a built Mathlib checkout pinned to `d13f23b723b8a846827a245b89c10fc7d3f11612` and Lean `v4.34.1`:

```sh
lake env bash /path/to/research/ayh-resource-reset-20261124/check_lean.sh
python -B /path/to/research/ayh-resource-reset-20261124/check_rewrite_certificates.py
python -B /path/to/research/ayh-resource-reset-20261124/check_zero_faces.py
python -B /path/to/research/ayh-resource-reset-20261124/monomial_transfer.py
python -B /path/to/research/ayh-resource-reset-20261124/positive-section/replay_marked.py
```

The Lean script builds all ten modules into fresh temporary storage and prints every new public theorem's axioms. Three upstream files are included byte-for-byte with their original identities. Finite controls and repository integrity checks supplement the proofs; they are not substitutes for the missing global argument.
