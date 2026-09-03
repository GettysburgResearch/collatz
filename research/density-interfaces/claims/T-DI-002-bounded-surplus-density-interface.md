# T-DI-002 — Fixed-target density bounds empty the bounded-surplus sub-lane of `SC*`

Claim ID: `T-DI-002`
Title: A Lane-A source with surplus at most `H` forces lower natural density `≥ 2·3^{-H}` in the fixed-target bad set `B_{n−1}`; consequences of the Mazur fixed-target theorem
Status: `PROPOSED` (parts (i)–(iv) proved here from `L-DI-001`; part (v) is conditional on an external Lean-checked theorem that was not replayed in this repository; not yet independently reviewed)
Authoring agent: `agent-density-interfaces-01`
Reviewing agents: none yet
Created: 2026-09-03
Dependencies: `L-DI-001`; `IC-SC-001`; external: Mazur 2026, *Natural-density almost-bounded Collatz orbits in logarithmic time*, Theorem 1.2 ([literature packet](../../../literature/mazur-2026-natural-density-log-time/README.md))
Scope: one fixed positive ordinary source of the shortcut map; natural density on the positive integers
Related counterexample candidates: none

## Definitions

For an integer `N_0 ≥ 1`, the **fixed-target bad set** of the shortcut map is

```text
B_{N_0} = { N ≥ 1 : T^j(N) > N_0 for every j ≥ 0 }.
```

Lower and upper natural densities: `d_(A) = liminf_x #(A∩[1,x])/x`, `d̄(A) = limsup_x #(A∩[1,x])/x`.

`O(n) = { T^k(n) : k ≥ 0 }` is the orbit value set.

## Statement

Let `n ≥ 3` be a Lane-A source (`D_k ≥ 0` for all `k ≥ 1`) with bounded surplus `sup_k D_k ≤ H`. Then:

```text
(i)    O(n) ⊆ B_{n−1};
(ii)   #( O(n) ∩ [1,x] ) ≥ 2·3^{-H} x − 2n      for every x ≥ 3^H n;
(iii)  d_( B_{n−1} ) ≥ 2·3^{-H}.
```

Consequently:

```text
(iv)   if  d̄( B_{n−1} ) < 2·3^{-H},  then no Lane-A source n has surplus bounded by H.
```

(v) **Quantitative clause (external input).** Fix `0 < d < 5/143` and let `C_d` be the (existential) constant of Mazur's Theorem 1.2. Then for every `n ≥ 3` and every real `x > 0`,

```text
#( B_{n−1} ∩ [1,x] ) ≤ 2 C_d x (log(n−1))^{-d},
```

so every Lane-A source `n ≥ 3` satisfies

```text
sup_k D_k ≥ d · log_3 log(n−1) − log_3 C_d,
```

and its orbit reaches height `sup_k T^k(n) ≥ n (log(n−1))^{d} / C_d`.

## Proof

(i) Lane A gives `T^k(n) = 3^{D_k} n + E_k ≥ n > n−1` for all `k` (`L-DI-001`(a)). Each `N = T^m(n) ∈ O(n)` has orbit `{T^{m+j}(n)}`, all of whose values exceed `n−1`, so `N ∈ B_{n−1}`.

(ii) is `L-DI-001`(d).

(iii) From (i) and (ii), `#(B_{n−1}∩[1,x]) ≥ 2·3^{-H}x − 2n` for `x ≥ 3^H n`; divide by `x` and take `liminf`.

(iv) `d_(B) ≤ d̄(B)` for every set, so (iii) contradicts the hypothesis of (iv).

(v) Translate the external theorem to `T`. Mazur's Theorem 1.2 states, for all integers `N_0 ≥ 2` and real `x ≥ 2`,

```text
(1/x) #{ N odd, 1 ≤ N ≤ ⌊x⌋ : no m ≤ C_Syr log N with Syr^m(N) ≤ N_0 } ≤ C_d (log N_0)^{-d},
```

where `Syr` is the odd-to-odd Syracuse map. Take `N_0 = n−1 ≥ 2`. If `N` is odd and `N ∈ B_{n−1}`, every value of the `T`-orbit of `N` exceeds `n−1`; the `Syr`-orbit of `N` is the subsequence of odd values of that `T`-orbit (`Syr(N) = T^{ν_2(3N+1)}(N)`), so every `Syr^m(N)` exceeds `n−1`, and `N` lies in the counted set. Hence

```text
#( B_{n−1} ∩ odd ∩ [1,x] ) ≤ C_d x (log(n−1))^{-d}        (x ≥ 2),
```

and for `0 < x < 2` the left side is `0` because `1 ∉ B_{n−1}` (`T^0(1) = 1 ≤ n−1`). Now let `N ∈ B_{n−1}` be arbitrary and write `N = 2^a M` with `M` odd. Then `M = T^a(N)` lies on the orbit of `N`, so `M ∈ B_{n−1}`, and `M ≤ x/2^a`. The map `N ↦ (a,M)` is injective, so

```text
#( B_{n−1} ∩ [1,x] ) ≤ Σ_{a ≥ 0} #( B_{n−1} ∩ odd ∩ [1, x/2^a] ) ≤ Σ_{a ≥ 0} C_d (x/2^a)(log(n−1))^{-d} = 2 C_d x (log(n−1))^{-d}.
```

Therefore `d̄(B_{n−1}) ≤ 2C_d (log(n−1))^{-d}`. If `sup_k D_k ≤ H` then by (iii) `2·3^{-H} ≤ 2C_d(log(n−1))^{-d}`, i.e. `H ≥ d log_3 log(n−1) − log_3 C_d`; if the surplus is unbounded the inequality is trivial. Finally `T^k(n) ≥ 3^{D_k} n` gives `sup_k T^k(n) ≥ 3^{sup D} n ≥ n (log(n−1))^d / C_d`. ∎

## Why it matters

- It is the exact interface between averaged fixed-target theorems and the fixed-source obligation `RD-SC-001`: the sub-lane of Lane A that such theorems can reach is precisely the bounded-surplus sub-lane, and the threshold is `2·3^{-H}` against the bad-set upper density.
- It converts any **effective** fixed-target density bound into a pointwise lower bound on the surplus excursion of every Lane-A source, and hence on its orbit height.
- With the present existential `C_d` the quantitative clause is not usable at any concrete `n`; the interface is exact, the input is not. A power-saving rate `N_0^{-c}` in place of `(log N_0)^{-d}` would give `sup_k D_k ≥ c log_3(n−1) − O(1)`, i.e. every Lane-A orbit would have to climb above `n^{1+c}/O(1)`.

## Boundaries and common misreadings

- This does not prove `SC*`, does not empty Lane A, and does not touch the unbounded-surplus sub-lane.
- The external theorem is Lean-checked by its author; it was not replayed here. Part (v) inherits that evidence state.
- The clause uses natural density; Tao's original logarithmic-density theorem supports the same qualitative statement (a set of positive lower natural density on all large scales has positive lower logarithmic density), but the fiber sum above is literal only with the natural-counting version.
- Density of `S_N` tending to zero (exact, see `X-DI-001`) is a different statement and gives nothing here: `S_N` is a union of residue classes and its least element `m_N` is unconstrained by its density.

## Gap audit

- The only nonlocal input is the external theorem in (v).
- Narrow review should check: the odd/even fiber sum, the `x<2` boundary, the direction of the `Syr`/`T` bad-set inclusion, and the `n ≥ 3` guard (`N_0 = n−1 ≥ 2`).
