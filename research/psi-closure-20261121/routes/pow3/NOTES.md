# Route pow3 — the powers-of-three family

**Target.** `theorem pow_three_basin : ∀ i : Nat, Basin (3^i)`.

**Status: OPEN. The target is not proved here.** Route verdict: **PARTIAL**. New machine-checked
identities were found (an exchange lemma for every cycle, an equivalent form of the target, links
between powers of three, Mersenne numbers and base-9 repunits, and families of unbounded depth).
The system of identities does not close. The stopping point is identified exactly in §4: it is the
ψ-closure lemma at an explicit family of points.

Written 2026-11-21 on branch `claude/collatz-prs-discussion-qq2bvk`, base head
`a5e384eaafffc6c40fdce7dca6891d32c2e05dda`. This route made no commit and edited no existing file.

## 0. Map, normalization, notation

- `T(n) = n/2` (n even), `(3n+1)/2` (n odd) on positive integers; Lean `shortcut`. `C` = Lean
  `Basin` = the `T`-orbit reaches 1. `a ~ b`: same component. `[a]`: the component of `a`.
- `P(i) := [3^i]`, `M(a) := [2^a − 1]`, `σ_j := (9^j − 1)/8`, `L_i := (3^i + 1)/2`, `φ(y) := 3y − 1`.
- Exchange: `T^n(x + 2^n u) = T^n(x) + 3^o u`, `o` = odd steps of `x` among the first `n`.
- Every statement is about ordinary positive integers and finite-time equality of ordinary orbits.
  "2-adically close exponents" always means a residue class of the exponent; no 2-adic limit is
  used as a conclusion.

## 1. Claim register

| ID | Claim | Status |
|---|---|---|
| T | `∀ i, 3^i ∈ C` | **OPEN** |
| A1 | Linearity `T^n(x + 2^n u) = T^n(x) + 3^o u`; master exchange over ℤ for every odd denominator `d`; periodic form `(2^(pk) w + c)/d ~ (3^(ok) w + c)/d` | PROVED-LEAN |
| A2 | `8^k u − 5 ~ 9^k u − 5`; `(8^k w + 1)/5 ~ (3^k w + 1)/5` | PROVED-LEAN |
| A3 | T ⟺ `C` closed under `x ↦ x + 2^n` whenever `T^n(x) = 1` | PROVED-LEAN |
| A4 | `T^n(x) = 1` with `o` odd steps ⟹ `x + 2^n u ~ 4^o u + 1` | PROVED-LEAN |
| B1 | `3^(2j+1) ~ 4σ_(j+1) + 1`; `3^(2j) = 8σ_j + 1`; `σ_j ≡ j (mod 8)` | PROVED-LEAN (middle one is arithmetic) |
| B2 | `2^(2j+1) − 1 ~ 2^(2j+2) − 1 ~ σ_(j+1)` | PROVED-LEAN (the fold is also in PR #176) |
| B3 | `3^(4k+1) ~ 2^(4k+2) − 1 ~ 2^(4k+1) − 1` | PROVED-LEAN |
| C1 | If `3^N = 1 + 4^s q`, `w = 3^(s−1) q`: `3^N ~ 3w+1`, `3^(N−1) ~ 2w+1` | PROVED-LEAN |
| C2 | If `3^N = 1 + 2·4^s q`: `3^N ~ 2·3^s q + 1`, `3^(N−1) ~ 3^s q + 1` | PROVED-LEAN (same mechanism as PR #181 `paired_descent`) |
| C3 | `3^(4^t u) ~ 3^(4^t u − 1)` for every `t ≥ 1` and `u ≡ 7 (t odd) / 5 (t even) (mod 8)` | PROVED-LEAN |
| C4 | `2^(a+1) c − 2 ~ 2^(a+1) c − 1` when `3^a c ≡ 3 (mod 4)`; hence C1 closes whenever `w + 1 = 2^(a+1) c`, `3^a c ≡ 1 (mod 4)` | PROVED-LEAN |
| C5 | If `3^N = 1 + 32q`, `q` odd: `2^N − 1 ~ y`, `3^(N−1) ~ 3y − 1`, `y = (3q+1)/2` | PROVED-LEAN |
| C6 | If in C1 `3w + 1 = 8x`, `x` odd: `3^N ~ m`, `3^(N−1) ~ 3m − 1`, `m = 3x + 1` | PROVED-LEAN |
| D1 | `R_(2j) = 4σ_j`; `R_(2j+1) ~ σ_(j+1)`; `σ_(j+1) ~ 3σ_j` for odd `j` (the three hand-derived items of the brief) | first is arithmetic; second is B2 with the packet's `basin_pow_two_pred`; third is the packet's `basin_odd` at `y = 3σ_j` — PROPOSED as stated (not separate Lean theorems) |
| D2 | Cross links `M(m) = P(m−1)` on `m ≡ 7 (16)`, `19 (32)`, `41, 59 (64)`, …; `P(i) = P(i+1)` on `i ≡ 19, 40 (64)`, … | EMPIRICAL (exact symbolic class certificates by script E2; not in Lean) |
| D3 | Covered tail classes in C4 have density 1/2 among odd `w` | PROPOSED (disjoint classes, geometric sum) |
| D4 | Exchange invariant: `P(m+N) = [1 + 2^(e_m)(3^N − 1)]` for `N ≡ 0 (mod 2^K)`, `e_m = 2(o_m + m) − n_m` | PROPOSED from A4 + packet; four exact checks (E3c) |
| N1 | No bounded-depth system of certificates `3^i ~ 3^(i±δ)` closes the family; for each depth there are exponent classes without such a certificate | PROPOSED (derivation §5) + EMPIRICAL (E3d, E3e) |
| N2 | In the searched space no identity lowers the level of `3^e` on any class of modulus ≤ 16, and none reaches a family known to lie in `C` | EMPIRICAL (E1) |

## 2. Lean

File: `Pow3Families.lean` (this directory), Lean 4.34.1 core only, `import Collatz` (the packet).
50 definitions/theorems, no `sorry`. Compiled standalone, exit code 0, with

```
LEAN_PATH=<repo>/research/psi-closure-20261121/lean/.lake/build/lib/lean \
  <lean-4.34.1>/bin/lean -DwarningAsError=true Pow3Families.lean
```

`lean_check_output.txt` is the output of that run: 25 `#print axioms` lines, each
`[propext, Classical.choice, Quot.sound]` or a subset. `lake` was not run and the packet's `lean/`
directory was not touched.

Main statements (namespace `CollatzPow3`; `iter n x` = `T^n(x)`, `odds n x` = odd steps):

```
iter_add_pow (n) : ∀ x u, iter n (x + 2^n*u) = iter n x + 3^(odds n x) * u
basin_shift (n x u) : Basin (x + 2^n*u) ↔ Basin (iter n x + 3^(odds n x) * u)
master (d) (hd : d % 2 = 1) (n) : ∀ (y : Nat) (w c : Int),
    ((d*y : Nat) : Int) = 2^n*w + c → ((d * iter n y : Nat) : Int) = 3^(oddsZ d n c)*w + iterZ d n c
periodic_exchange (d) (hd : d % 2 = 1) (p) (c : Int) (hper : iterZ d p c = c) (k y y' : Nat) (w : Int)
    (h : ((d*y : Nat) : Int) = 2^(p*k)*w + c) (h' : ((d*y' : Nat) : Int) = 3^(oddsZ d p c * k)*w + c) :
    Basin y ↔ Basin y'
basin_steps (n y y') (w c : Int) (o) (c' : Int) (ho : oddsZ 1 n c = o) (hc' : iterZ 1 n c = c')
    (h : (y : Int) = 2^n*w + c) (h' : (y' : Int) = 3^o*w + c') : Basin y ↔ Basin y'
basin_pow_eight_sub_five (k u) (hu : 5 ≤ 8^k*u) : Basin (8^k*u - 5) ↔ Basin (9^k*u - 5)
basin_cycle_one_fifth (k y y' w) (h : 5*y = 8^k*w + 1) (h' : 5*y' = 3^k*w + 1) : Basin y ↔ Basin y'
pow_three_iff_shift_closure : (∀ i, Basin (3^i)) ↔ (∀ x n, iter n x = 1 → Basin (x + 2^n))
basin_shift_to_one (n x u) (hx : iter n x = 1) : Basin (x + 2^n*u) ↔ Basin (4^(odds n x) * u + 1)
repunit_mod_eight (j) : ((9^j - 1)/8) % 8 = j % 8
basin_pow_three_odd (j) : Basin (3^(2*j+1)) ↔ Basin (4 * ((9^(j+1) - 1)/8) + 1)
basin_mersenne_even (j) : Basin (2^(2*j+2) - 1) ↔ Basin ((9^(j+1) - 1)/8)
basin_mersenne_odd (j) : Basin (2^(2*j+1) - 1) ↔ Basin ((9^(j+1) - 1)/8)
basin_mersenne_pair (j) : Basin (2^(2*j+2) - 1) ↔ Basin (2^(2*j+1) - 1)
basin_pow_three_mersenne (k) : Basin (3^(4*k+1)) ↔ Basin (2^(4*k+2) - 1)
pow_three_pair_normal_form (N s q) (hN : 1 ≤ N) (hs : 1 ≤ s) (h : 3^N = 1 + 4^s*q) :
    (Basin (3^N) ↔ Basin (3*(3^(s-1)*q) + 1)) ∧ (Basin (3^(N-1)) ↔ Basin (2*(3^(s-1)*q) + 1))
pow_three_pair_normal_form_odd (N s q) (hN : 1 ≤ N) (h : 3^N = 1 + 2*(4^s*q)) :
    (Basin (3^N) ↔ Basin (2*(3^s*q) + 1)) ∧ (Basin (3^(N-1)) ↔ Basin (3^s*q + 1))
basin_pow_three_consecutive (N s q) (hN) (hs) (h : 3^N = 1 + 4^s*q) (hw : (3^(s-1)*q) % 8 = 1) :
    Basin (3^N) ↔ Basin (3^(N-1))
three_pow_dyadic (t u) : ∃ q, 3^(4^(t+1)*u) = 1 + 4^(t+2)*q ∧ q % 8 = (5*u) % 8
basin_pow_three_dyadic_odd (a u) (hu : u % 8 = 7) : Basin (3^(4^(2*a+1)*u)) ↔ Basin (3^(4^(2*a+1)*u - 1))
basin_pow_three_dyadic_even (a u) (hu : u % 8 = 5) : Basin (3^(4^(2*a+2)*u)) ↔ Basin (3^(4^(2*a+2)*u - 1))
basin_adjacent_family (a c) (hc : (3^a*c) % 4 = 3) : Basin (2^(a+1)*c - 2) ↔ Basin (2^(a+1)*c - 1)
basin_pow_three_consecutive_gen (N s q a c) (hN) (hs) (h : 3^N = 1 + 4^s*q)
    (hw : 3^(s-1)*q + 1 = 2^(a+1)*c) (hc : (3^a*c) % 4 = 1) : Basin (3^N) ↔ Basin (3^(N-1))
pow_three_mersenne_closure_pair (N q) (h : 3^N = 1 + 32*q) (hq : q % 2 = 1) :
    (Basin (2^N - 1) ↔ Basin ((3*q+1)/2)) ∧ (Basin (3^(N-1)) ↔ Basin (3*((3*q+1)/2) - 1))
pow_three_pair_closure_form (N s q x) (hN) (hs) (h : 3^N = 1 + 4^s*q)
    (hx : 3*(3^(s-1)*q) + 1 = 8*x) (hodd : x % 2 = 1) :
    (Basin (3^N) ↔ Basin (3*x+1)) ∧ (Basin (3^(N-1)) ↔ Basin (3*(3*x+1) - 1))
```

## 3. Structures found

### 3.1 One lemma behind every exponent-parametrized identity (PROVED-LEAN)

`master`: if `d` is odd and `d·y = 2^n·w + c` with `w, c ∈ ℤ`, then `d·T^n(y) = 3^o·w + c'`, where
`c'` is the `n`-th iterate of `c` under the `3x+d` map on ℤ and `o` its odd count. With a periodic
`c` this is `periodic_exchange`. The packet's two families are the cycles `{1,2}` (`d = 1`) and
`{−1}`; the cycle `−5 → −7 → −10` gives `8^k u − 5 ~ 9^k u − 5`; the rational cycle
`1/5 → 4/5 → 2/5` gives `(8^k w + 1)/5 ~ (3^k w + 1)/5`. With a numeral `c`, `basin_steps` turns any
finite-step certificate on a residue class into one line. Every identity with a step count growing
in the exponent that the search found is an instance.

Applied to the target: `∀ i, 3^i ∈ C` holds iff `C` is closed under `x ↦ x + 2^n` at every time `n`
at which the orbit of `x` sits at 1 (`pow_three_iff_shift_closure`). More generally
`x + 2^n u ~ 4^o u + 1` (`basin_shift_to_one`).

### 3.2 The search (EMPIRICAL)

**E1** (`e1_family_merge_search.py`, exact big integers). 964 family labels `(c·3^e + d)/g`
(`c ≤ 16` prime to 3, `|d| ≤ 16`, `c, d` not both even, `g ∈ {1,5,7}`) and `(c·2^a + d)/g` (`c, d` odd,
`≤ 15` in absolute value, `g ∈ {1,3,5,7,9}`; four labels duplicate others), 51 072 members,
`e ∈ [30,125]`, `a ∈ [48,143]`. A 3-type member is followed
16 steps, a 2-type member `a + 16` steps. 1 288 889 linked pairs; 91 052 relations hold for every
tested exponent of a class mod `M ≤ 32` with a constant step signature. For `3^e` (375 relations):

- all `e`: 35 relations to 2-type families with `a = 2e + const` (`2^a+1`, `3·2^a+1`, `(2^a+1)/3`, …)
  and 4 to 3-type families (`3^(e+1)+1`, `4·3^e+1`, …). All are level-preserving instances of
  `basin_shift` at a base point `x ∈ C`; none lowers `e`;
- `e ≡ 1 (4)`: `3^e ~ 2^e − 1 ~ 2^(e+1) − 1` (now B3); `e ≡ 6 (16)`, `e ≡ 18 (32)`:
  `3^e ~ 2^(e+1) − 1`; `e` even or `e ≡ 3 (4)`: `3^e ~ 2^(2e+1) + 1`;
- same family, other exponent: only `e ≡ 27 (32)` ↔ `e + 1` (now the `t = 1` member of C3).

For `2^a − 1`: `a ↔ a+1` for odd `a` (B2), plus exchange relations such as
`2^a − 1 ~ (2^(a+2) − 13)/9` (this appears to be the identity of PR #177). The digest counts 0
uniform relations between a core family (`3^e`, `3^e ± 1`, `2^a ± 1`, `(2^a+1)/3`) and `(4^j − 1)/3`,
the one listed family that lies in `C` trivially.

**E2** (`e2_exponent_class_sieve.py`). `T^t(c·3^i + d) = (α·3^i + β)/2^t` with `(α, β)` a function
of `i mod 2^(t−2)`; equal `(α, β)` for two families certify `T^t(F(i)) = T^t(G(i))` on the whole
class. 4096 classes mod `2^12`, depth ≤ 60. "exact" = classes of modulus ≤ `2^12`; the second figure
samples deeper classes.

| pair | first classes (depth) | density exact (t ≤ 14) | within 60 steps |
|---|---|---|---|
| `3^i`, `3^(i+1)` | `27 (32)` (7); `19, 40 (64)` (8); `35, 79, 120 (128)` (9) | 0.1655 | 0.3203 |
| `3^i`, `3^(i+2)` | `135 (256)` (10) | 0.0273 | 0.1775 |
| `3^i`, `3^(i+3)` … `3^(i+8)` | depth ≥ 14 | ≤ 0.0005 | 0.1089 … 0.0093 |
| `3^m − 1`, `3^m + 1` (`M(m)` vs `P(m−1)`) | `2 (4)` (4); `7 (16)` (6); `19 (32)` (7); `41, 59 (64)` (8) | 0.4421 | 0.5369 |
| `3^m − 1`, `3^(m+1) + 1` (`M(m)` vs `P(m)`) | `1 (4)` (4); `108 (128)` (9) | 0.3025 | 0.4094 |
| `3^m − 1`, `3^(m+1) − 1` (`M(m)` vs `M(m+1)`) | `1 (2)` (2); `30 (64)` (8) | 0.5476 | 0.6084 |

### 3.3 The reduction graph

Nodes: the components `P(i)` and `M(a)`. Every edge is an equality of components.

- All exponents (Lean): `P(i) = [L_(i+1)] = [3^(i+1)+1] = [4^(i+1)+1] = [(2·4^(i+1)+1)/3]` (packet);
  `P(2j) = [8σ_j + 1]`, `P(2j+1) = [4σ_(j+1) + 1]`; `M(a) = [3^a − 1]` (packet);
  `M(2j+1) = M(2j+2) = [σ_(j+1)]`.
- Exponent classes, bounded depth: `P(m) = M(m) = M(m+1)` for `m ≡ 1 (4)` (Lean). Further classes
  of E2 (D2, not in Lean).
- Unbounded depth (Lean): `P(4^t u − 1) = P(4^t u)` for all `t ≥ 1`, `u ≡ 7 / 5 (mod 8)`; more
  generally C4.

In repunit coordinates `x = σ_j` the whole graph is the question which of `[x]`, `[4x+1]`, `[8x+1]`,
`[9x+1]` coincide: `M(2j) = [x]`, `P(2j−1) = [4x+1]`, `P(2j) = [8x+1]`, `M(2j+2) = [9x+1]`.
`4x+1 ~ x` for odd `x` gives B3.

**No edge leaves the graph downward.** Every edge joins exponents at distance ≤ a few; no node is
joined to a family known to lie in `C`. An induction on the exponent would need, for every `N ≥ 1`, a
chain of edges from `P(N)` to some `P(N')`, `N' < N`. The families without such an edge are the
exponent classes outside the certified ones; the first is described in §4.

### 3.4 After the structured phase (PROVED-LEAN unless marked)

For `N = 2^k u` (`u` odd, `k ≥ 1`) write `3^N − 1 = 2^(k+2) q`, `q` odd. The first `k+2` steps of
`3^N`, `3^(N−1)` and `2^N − 1` are forced by exchange, and then:

- `k` even, `s = (k+2)/2`, `w = 3^(s−1) q`: `P(N) = [3w+1]`, `P(N−1) = [2w+1] = [3w+2]`. The two
  consecutive powers of three become the **adjacent pair** `(3w+1, 3w+2)`.
- `k` odd, `s = (k+1)/2`: `P(N) = [2·3^s q + 1]`, `P(N−1) = [3^s q + 1]`, and
  `3^s q + 1 = 2 φ^(s−1)(T(q))` (arithmetic; E3b). `M(N) = [q]` (E3b; Lean for `k = 3` in C5, where
  `(M(N), P(N−1))` is the closure pair `(y, 3y − 1)`).

Adjacent pairs `(z, z+1)` with `z + 2 = 2^(a+1) c`, `3^a c ≡ 3 (mod 4)` meet after `a + 3` steps
(`basin_adjacent_family`, one statement for all `a`). This gives C4, and with the 2-adic expansion
of `3^(4^t)` (`three_pow_four_pow`, `three_pow_dyadic`) the explicit family C3: the orbits of
`3^(4^t u)` and `3^(4^t u − 1)` meet after exactly `2t + 5` steps. E3a confirms the step count for
`t = 1..12` (40/40 each) and that no other odd residue of `u` has met by then (0/30 each).
This is an infinite family of exponent classes (one class mod `2^(2t+3)` for each `t`) whose
certificates have unbounded depth and one uniform proof.

### 3.5 Exchange invariant (PROPOSED + EMPIRICAL)

If `3^m` reaches 1 after `n_m` steps with `o_m` odd steps, put `e_m = 2(o_m + m) − n_m`. By A4 and
the packet's `4^i v + 1 ~ 3^i v + 1`: `P(m + N) = [1 + 2^(e_m) (3^N − 1)]` for `N ≡ 0 (mod 2^K)`,
`K ≥ n_m − 2`. For `3^m − 1` the same holds with `f_m = 2o' − n' + 2m`. So near a fixed small
exponent the component depends on `m` only through one integer. E3c: `e = 0,1,3,18,4,16,6,13,13,8,…`,
`f = 1,1,2,2,16,16,6,6,8,8,…`; for `m ≤ 600`, `e_m = e_m'` for some `m' < m` in 555 cases,
`e_m = f_m` in 448 cases (all 150 with `m ≡ 1 (4)`), `f_(2j−1) = f_(2j)` in 299/299. These are facts
about the total stopping data of individual small exponents; each yields only a class of modulus
about `2^(n_m)`.

## 4. First statement needed and not proved

Induction on the exponent needs, for every `N ≥ 1`,

> (S) `Basin (3^(N−1)) → Basin (3^N)`.

By C1 this is, when `3^N = 1 + 4^s q`, the adjacent-pair statement `Basin (3w+2) → Basin (3w+1)`,
`w = 3^(s−1) q`. It is proved for `w + 1 = 2^(a+1) c`, `3^a c ≡ 1 (mod 4)`:
`w ≡ 1 (8), 11 (16), 7 (32), 47 (64), …`. The shallowest class where C4 does not apply is
`w ≡ 5 (mod 8)`: there `3w + 1 = 8x` and the pair becomes `(x, 9x + 2)`. **On its half
`w ≡ 13 (mod 16)` (`x` odd)**, by C6, (S) is exactly

> `Basin (3m − 1) → Basin m`,  `m = 3x + 1`,  `x = (3w + 1)/8` odd,

the reverse ψ-closure at the point `m` (the direction of the packet's `OpenLemma`, at `m = 3x + 1`
instead of `27k + 1`). Smallest exponent family: `N = 4u`, `u ≡ 3 (mod 16)`, i.e. the pairs
`(3^(64j+11), 3^(64j+12))` (derivation `q ≡ 5u (mod 16)`; exact check for `N = 12, 76, 140, 204` in
E3g). I could not prove this statement, and no identity found reduces it. For the ladder the pair
is `(L_N, 3L_N − 1) ∈ P(N−1) × P(N)`; here it is `(m, 3m − 1) ∈ P(N) × P(N−1)`.

## 5. Negative findings

1. **Coalescence above a fixed height is not an identity.** 273 of the 370 pairs `(3^e, 3^(e+1))`,
   `e = 30..399`, share an orbit value ≥ `2^44` (E3f). A first version of E1 linked members merged
   anywhere above `2^44` and produced one class of 1694 members; that criterion was dropped. Only
   relations with a constant step signature on a whole exponent class are reported.
2. **No level-lowering identity in the searched space** (N2): for `3^e` the relations valid for all
   `e` are level-preserving exchange relations; the only same-family relations are on thin classes.
3. **Fixed step counts force bounded depth.** If `T^a(3^i) = T^b(3^(i+δ))` for infinitely many `i`
   of a class with the same parity vectors, comparing the `3^i`-coefficients gives `a = b`; the
   certificate then depends on `i mod 2^(a−2)`. Near `i ≡ −1 (mod 2^K)` the two orbits shadow the
   orbits of `1/3` and `3^(−1−δ)` for `K+2` steps and cannot meet earlier (PROPOSED). E3e, `K = 40`,
   300 exponents: the earliest certificate for `(3^i, 3^(i+1))` is at depth `K+5` (87 cases, the C3
   class), and for `(3^(i−δ), 3^i)`, `δ ≤ 8`, at depth `K+9`.
4. **Reach of bounded depth is small and grows slowly.** On 2000 random 64-bit exponents (E3d) a
   certificate `3^i ~ 3^(i−δ)`, `δ ≤ 8`, exists within depth 8 / 16 / 32 / 64 for
   8.1% / 21.9% / 34.4% / 51.1%; with either sign of `δ`: 14.6% / 40.6% / 60.1% / 76.9%.
5. **Unbounded-depth families do not close either.** C3/C4 cover half of the tail classes (D3);
   the first remaining class is the closure pair of §4, which is the open lemma itself.

## 6. Overlap with concurrent PRs

Statements read at heads `ad9a0611` (#176), `27a2c741` (#179), `5f03d809` (#181), `23bbf738` (#177);
none rebuilt here.

- `basin_mersenne_pair` is PR #176 `mersenne_even_exponent_fold`. Credit to #176.
- `basin_iter` is PR #181 `basin_orbit`. The cases of A1 at the fixed point `−1` and the cycle
  `{1,2}` with odd counts are PR #179 `ones_block`, `twos_block` and PR #181 `power_four_profile`;
  PR #179 `ladder_path` composes them. `master` adds arbitrary base points, cycles and denominators.
- PR #181 `paired_descent` transports a closure pair `(m, 3m−1)` through the `{1,2}` exchange;
  C2 is that mechanism for `(3^(N−1), 3^N)`. C1, C3, C4, C6 treat the even-order case.
- E1's relation `2^a − 1 ~ (2^(a+2) − 13)/9` matches the PR #177 identity as described to me.

## 7. Files and checks

| file | content |
|---|---|
| `Pow3Families.lean`, `lean_check_output.txt` | Lean source; compiler output (exit 0, axiom lines) |
| `e1_family_merge_search.py`, `e1_output.txt` | E1 and its digest (about 60 s) |
| `e2_exponent_class_sieve.py`, `e2_output.txt` | E2 |
| `e3_dyadic_invariant_reach.py`, `e3_output.txt` | E3 a–g (seeded; about 2 s) |
| `NOTES.md` | this file |

Run: `python3 e1_family_merge_search.py`, `python3 e2_exponent_class_sieve.py`,
`python3 e3_dyadic_invariant_reach.py` (no arguments, no dependencies). Each was run to completion
and the saved outputs are those runs. `python3 -X utf8 -B tools/validate.py` was attempted once and
refused to run (exit 1, "tracked files or index are dirty"), so there is no validator result for
this tree. Not run: `lake build`, any Mathlib build.

## 8. Handoff

- Strongest uncertainty: D2 and N1/N2 are script results on finite ranges; D3, D4 and item 3 of §5
  are written derivations, not Lean.
- The route's induction step is the closure lemma at explicit points. The family
  `m = 3x + 1`, `x = (9q + 1)/8`, `q = (81^u − 1)/16`, `u ≡ 3 (mod 16)` is a concrete test set for
  any proposed proof of the reverse closure `Basin (3m − 1) → Basin m`: such a proof must give
  `3^(4u) ∈ C` from `3^(4u−1) ∈ C`.
- `basin_steps` and `periodic_exchange` are reusable: a finite-step class certificate or a new cycle
  costs one line each.
- Next lemma within reach: `three_pow_dyadic` to precision `2^(a+3)`, which would make C4 explicit
  in `(t, u)` for every `a`. It would raise coverage of the tails towards 1/2 and no further.
