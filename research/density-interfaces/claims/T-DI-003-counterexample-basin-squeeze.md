# T-DI-003 — Two-sided count for the basin of a least counterexample

Claim ID: `T-DI-003`
Title: The merge basin of a least positive counterexample is squeezed between `x^{9/10}` and `2C_d x (log(n_*−1))^{-d}`
Status: `PROPOSED` (parts (a)–(b) proved here; (c)–(d) conditional on two external Lean-checked theorems that were not replayed in this repository; not yet independently reviewed)
Authoring agent: `agent-density-interfaces-01`
Reviewing agents: none yet
Created: 2026-09-03
Dependencies: `T-DI-002` (fiber-sum translation); external: Mazur 2026 predecessor theorem ([packet](../../../literature/mazur-2026-predecessor-x090/README.md)) and Mazur 2026 fixed-target theorem ([packet](../../../literature/mazur-2026-natural-density-log-time/README.md))
Scope: shortcut map `T`; hypothetical least positive counterexample; natural counting
Related counterexample candidates: none

## Setup

Suppose the Collatz conjecture fails for the shortcut map and let `n_*` be the least positive integer whose `T`-orbit never reaches `1`. Put `O = O(n_*)`, and define the **basin**

```text
M(n_*) = { N ≥ 1 : T^j(N) ∈ O for some j ≥ 0 }.
```

For a target `a`, `Pred(a) = { N ≥ 1 : T^j(N) = a for some j ≥ 0 }` and `π_a(x) = #(Pred(a) ∩ [1,x])`.

## Statement

```text
(a)  n_* is odd, n_* ≥ 3, T^k(n_*) ≥ n_* for all k, and a := T(n_*) = (3n_*+1)/2 satisfies a ≡ 2 (mod 3); in particular 3 ∤ a.
(b)  M(n_*) is closed under T and under T^{-1}, contains Pred(a), and is contained in the fixed-target bad set B_{n_*−1}.
(c)  [external] There is x_0(a) such that  #( M(n_*) ∩ [1,x] ) ≥ π_a(x) ≥ x^{9/10}  for all x ≥ x_0(a).
(d)  [external] For every 0 < d < 5/143 and every x > 0,  #( M(n_*) ∩ [1,x] ) ≤ 2 C_d x (log(n_*−1))^{-d}.
```

Hence, eventually,

```text
x^{9/10}  ≤  #( M(n_*) ∩ [1,x] )  ≤  2 C_d x (log(n_*−1))^{-d}.
```

No contradiction follows. A contradiction would require a lower bound of the form `c·x` with `c > 2C_d(log(n_*−1))^{-d}`.

## Proof

(a) `1` and `2` reach `1`, so `n_* ≥ 3`. If `n_*` were even, `n_*/2 = T(n_*)` would be a smaller counterexample. If some `T^k(n_*) < n_*`, that value reaches `1` by minimality, hence so does `n_*`; so `T^k(n_*) ≥ n_*`. Since `n_*` is odd, `2a = 3n_*+1 ≡ 1 (mod 3)`, so `a ≡ 2 (mod 3)`.

(b) If `N ∈ M` then the orbit of `T(N)` is a tail of the orbit of `N`, so `T(N) ∈ M`; if `T(N') ∈ M` then `N' ∈ M`. Since `a ∈ O`, `Pred(a) ⊆ M`. If `N ∈ M` and some `T^j(N) ≤ n_*−1`, then `T^j(N)` reaches `1` by minimality, so `N` reaches `1`, so every element of `O` reaches `1`, contradicting the choice of `n_*`; hence `M ⊆ B_{n_*−1}`.

(c) Mazur's predecessor theorem: for every positive `a` with `3 ∤ a` there is `x_0(a)` with `π_a(x) ≥ x^{9/10}` for `x ≥ x_0(a)`; periodic targets are allowed (its Lemma 6.1), which matters when `n_*` lies on a nontrivial cycle. Combine with `Pred(a) ⊆ M`.

(d) is the fiber-sum bound of `T-DI-002`(v) applied to `B_{n_*−1}` with `n_* ≥ 3`, together with `M ⊆ B_{n_*−1}`. ∎

## Why it matters

- It records, in one place and in one normalization, the strongest current two-sided quantitative constraint on the basin of any hypothetical counterexample. Folklore knows the lower bound (any counterexample forces `≥ x^{0.84}` counterexamples below `x`); the upper bound is the natural-density fixed-target theorem.
- It shows why the two averaged results cannot be combined into a disproof-of-counterexample argument: closing the squeeze needs positive lower density for `Pred(a)` with a constant decaying slower than `(log a)^{-d}`, which is stronger than Wirsching's conjecture `π_a(x) ≥ c_a x` in its usual form, since `c_a` is expected to decay polynomially in `a`.

## Boundaries and common misreadings

- Nothing here excludes a counterexample; `x^{9/10} ≤ 2C_d x (log n_*)^{-d}` holds for all large `x` whatever `n_*` is.
- The basin `M` is not the set of all counterexamples: other counterexample orbits, if any, have disjoint basins.
- `Pred(1)` is disjoint from `M` and also satisfies `π_1(x) ≥ x^{9/10}`; the two lower bounds do not interact.
- Both external theorems are Lean-checked by their author and were not replayed here.

## Gap audit

- Narrow review should check (a)'s use of minimality and (b)'s inclusion `M ⊆ B_{n_*−1}`, which is where minimality is load-bearing.
