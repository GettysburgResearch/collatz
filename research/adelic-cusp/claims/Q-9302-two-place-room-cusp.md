# Q-9302 — Fixed-room and active-cylinder mechanisms after all-depth EQ

**Claim ID:** Q-9302  
**Title:** Can fixed-room coherence or active-cylinder nonstabilization exclude every remaining ordinary point?  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9302`, `D-9303`, `L-9310`, `L-9311`, `T-9312`--`T-9314`; issue-#4 and PR #20 crosswalks  
**Scope:** post-EQ ordinary-section frontier  
**Related counterexample candidates:** none

## 1. Weighted EQ is no longer the open target

`T-9312` proposes

\[
\sum_{1\le h\le2^K}
\frac{|S_K(h)|}{2^Kh}
\longrightarrow0
\]

at every depth.

The two-place, room, and triadic representations remain useful, but another absolute-Fourier decay estimate no longer advances the main theorem frontier.

The unresolved question is the ordinary section

\[
\Phi(\Omega)\cap\mathcal I.
\]

A single coherent ordinary point may coexist with very strong finite-depth equidistribution.

## 2. Method closure: the criticality constants do not contradict

PR #20's repetition theorem and `L-9310`'s phase-carry theorem produce the same constant

\[
\kappa
=
\frac1{\log_{64}81-1}.
\]

`L-9311` proves why. A repeated itinerary factor is itself an exact zero-carry chain in the difference of two ordinary tail orbits:

\[
64D_{i+1}=81D_i.
\]

The repetition-height inequality is therefore another completion-height bound. `R-9302` records the resulting method closure:

> Comparing the two matching `kappa` values double-counts one arithmetic mechanism and does not yield an incompatibility theorem.

A final proof must introduce a new coupling invariant.

## 3. Exact coupling: fixed-room coherence

`T-9313` supplies that invariant.

For a hypothetical ordinary room `A` and its tail states `A_j`,

\[
\boxed{
81^jA
=
64^jA_j
+
17\sum_{t=0}^{j-1}
\varepsilon_t81^{j-1-t}64^t.
}
\tag{1}
\]

The quotient is the same fixed room `A` for every `j`.

The reversed past word places `A_j mod81^j` in the triadic class set `C_j`; the future word places `A_j` in the survivor attractor; and the real companion forces

\[
\boxed{
(81/64)^j(A-1)+1
\le A_j
\le(81/64)^jA.
}
\tag{2}
\]

Conversely, a coherent integral path satisfying `(1)` reconstructs an ordinary survivor exactly.

This is the first interface in the packet that simultaneously sees:

- symbolic past;
- symbolic future;
- ordinary integrality at every shift;
- bounded real companion coordinate;
- and one invariant room.

## 4. Finite exclusion and asymptotic target

Let

\[
m_j=\min(C_j\setminus\{0,1\}),
\]

and

\[
B_j
=
\min\left\{
64^j,
\left\lceil m_j(64/81)^j\right\rceil
\right\}.
\]

`T-9313` proves that every nontrivial ordinary room satisfies

\[
A\ge B_j
\]

for every `j`.

The exact meet-in-the-middle computation `X-9303` gives

\[
B_{44}
=
227578060273510610973552811001603322347312502177488333909527505984
>2^{217}.
\]

Hence `T-9314` excludes every nontrivial room through `2^217`.

The decisive asymptotic theorem is now simply

\[
\boxed{B_j\to\infty.}
\tag{3}
\]

Any rate of divergence closes the ordinary section.

## 5. Why unconditional Cantor minima may be stronger than necessary

The number `m_j` minimizes over every past word, including words that cannot be extended to a coherent future survivor or to the same fixed room at earlier depths.

Define the coherent depth-`j` minimum by restricting to classes that lie on some finite path satisfying all predecessor equations and future survivor constraints. A proof that this coherent minimum grows faster than `(81/64)^j` is sufficient and may be substantially easier than bounding all of `C_j`.

The fixed-room quotient should be used as early as possible rather than discarded after obtaining class membership.

## 6. Active-cylinder formulation

PR #20's `T-9409` proves that an infinite stack directive selects one nested `2`-adic initial cylinder. It is ordinary exactly when the newly appended cylinder blocks eventually vanish.

The natural cross-program target is:

> Identify the appended active-cylinder blocks with fixed-room past/future data, then prove that a coherent positive itinerary has infinitely many nonzero blocks.

This would convert the ordinary-section problem into an explicit nonstabilization theorem.

## 7. Candidate proof mechanisms

### A. Coherent branch-and-bound

Construct a tree whose states contain:

\[
(A_j\bmod81^j,
A_j\bmod64^L,
\text{past word},
\text{future cylinder},
A).
\]

Prune a state when `(2)` misses the standard representative or when the future cylinder is empty. Seek a symbolic invariant proving every fixed room dies at finite depth.

### B. Return-word fixed-room pressure

A recurrence of a coherent state produces the orbit-difference zero-carry chain from `L-9311`. Prove that fixed-room coherence forces such a recurrence before its local height permits it.

### C. Block-tail sign or valuation

Derive a recurrence for the new nested-cylinder blocks and show an eventually zero tail would force either:

- a forbidden stationary ghost;
- a negative real context;
- an impossible `3`-adic valuation;
- or an eventually periodic ordinary itinerary.

### D. General `M -> N` fixed-room theorem

Generalize `T-9313` and the finite certificate to every expanding collision chart. A ladder rung with a provable divergent `B_j` would provide a complete ordinary-section result and may reveal the missing invariant for `64 -> 81`.

## 8. What no longer counts as progress by itself

- another equivalent absolute two-place Fourier estimate;
- comparing the two `kappa` constants without a coupling lemma;
- high output factor complexity alone;
- closure of one finite room marginal;
- compatible finite prefixes without least-representative stabilization;
- generic S-unit or measure-rigidity terminology without exact hypotheses.

## 9. Gap audit

- `T-9314` is finite, however large its exclusion bound.
- The computed unconditional minima need not describe the coherent minima.
- Active-cylinder nonstabilization is proved only for the stationary ghost interface, not the fully steered ordinary itinerary.
- Translation from an induced room to an original Collatz seed remains branch-qualified.
- No ordinary point, divergent seed, cycle, or resolution is claimed.

## 10. Suggested next attack

Build the coherent past/future tree at modest depth and record the exact reason each low room dies. The theory target is to turn the observed pruning reason into one monotone invariant proving `(3)` without enumerating all `2^j` past words.
