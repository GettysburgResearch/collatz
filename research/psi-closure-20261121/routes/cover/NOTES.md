# Route "cover": does a finite purely ordinary descent cover exist?

**Status of the Collatz conjecture: OPEN. Nothing here proves it.** This route decides a question
about one proof strategy, and the answer is negative.

## 1. Verdict

**OBSTRUCTION PROVED.** No finite purely ordinary descent cover exists. The point `(-1, 0)` of
`X = Z_2 x Z_3` has no descending ordinary path; the integer form of this statement is
machine-checked in core Lean (`CoverObstruction.lean`, axioms `propext`, `Quot.sound` only).

Integers near `(-1, 0)`: `n ≡ -1 (mod 2^K)` and `n ≡ 0 (mod 3^J)`. For such `n` every ordinary
walk of length `<= min(K, J)` ends at a value `>= n`. Explicit members: `n = 4^m - 1` has
`K = 2m`, `J = 1 + v_3(m)`; so `4^(3^(L-1)) - 1` is not descended by any ordinary walk of length
`<= L`. Least positive members for `K = J = 1..9`: 3, 27, 135, 1215, 1215, 16767, 203391,
1043199, 6082047.

## 2. Statements and status

| # | Statement | Status | Where |
|---|---|---|---|
| Z | If `2^K ∣ n+1`, `3^J ∣ n`, `T^q(w) = T^p(n)`, `p <= K`, and the first `q` steps of `w` contain at most `p + J` odd steps, then `w >= n`. | PROVED-LEAN | `no_descent` |
| Z' | If `2^L ∣ n+1` and `3^L ∣ n`, every ordinary walk of length `<= L` from `n` ends at `w >= n`. | PROVED-LEAN | `no_short_walk_descent`, `no_walk_descent_le` |
| Z'' | For all `L`, `N` there is `n > N` such that no ordinary walk of length `<= L` from `n` ends below `n`. Hence no finite family of ordinary descent certificates covers all large integers. | PROVED-LEAN | `unbounded_ordinary_descent_radius` |
| A | `(-1, 0)` is an obstruction point: every ordinary path has `α >= 1`, with `α = 1` only for the trivial path. | PROVED-WRITTEN (§4); follows from Z' | §4 |
| G | Exact description of the obstruction set `O` by a congruence between "driven orbits of 0". `O` is closed, of Haar measure 0, and projects into the non-stopping set of `Z_2`. | PROVED-WRITTEN (measure zero of the non-stopping set is SOURCE-QUALIFIED: Terras 1976, Everett 1977) | §3 |
| B | Fiber criterion: for integer `y0 >= 1`, `(-1, y0)` has a descending path iff some `y'' < y0` has a Collatz orbit hitting `2^j(y0+1) - B` early enough (§5). Exact decision for all `y0 <= 10^6`: 516 378 obstruction points, 483 622 not. | PROVED-WRITTEN + exact finite computation | §5, `fiber_scan.py` |
| C | `(-5, 0)` is an obstruction point. | PROVED-WRITTEN (§6), invariants replayed on 482 798 nodes | §6, `cycle_points.py` |
| D1 | `(-1, 30)` is not an obstruction point: path `oDDSDSSSSSDSS`, `α = 2048/2187`. | exact certificate | `shadow_bfs.py`, `fiber_scan.py` |
| D2 | Every `n ≡ 15 (mod 64)` has `(27n+11)/32` in its component by a walk of length 7; so a non-stopping 2-adic coordinate does not suffice (`(-43/27, 0)` is not an obstruction point). | exact certificate | §7 |
| N | "If the parity word of `x0` is non-stopping and never has two consecutive even steps, then `(x0, 0)` is an obstruction point." | **REFUTED** (my own conjecture): 29-step word, `w = (3n+7)/4` on a whole class mod `2^29` | §7, `verify_no00_counterexample.py` |
| F | "A finite purely ordinary cover exists." | **REFUTED** by Z'' | |
| H | Hand observation "a descent from `(-1,0)` needs a shadow on a negative cycle". | REFUTED as a mechanism at `(-1,0)`: the 3-adic shadow is never negative there (§4). The other two hand observations (B follows the `3x-1` map; side branches `J_b = (2^b+1)/3`) are VERIFIED. | §4 |
| E | Collatz ⟹ no positive integer is an obstruction point ⟹ no divergent orbit with `Σ 1/T^k(n) < ∞`. The equivalence "Collatz ⟺ no integer obstruction point" is not established: cycles are invisible to this notion. | PROVED-WRITTEN (§8) | §8 |
| X1 | `(-17, 0)`, `(-19/11, 0)`, and the greedy non-stopping word with `y0 = 0` have no descending path within the bounds of §9. | EMPIRICAL | §9 |
| X2 | Uncovered measure by walk length (§9 table). | EMPIRICAL | `uncovered_mc.py` |
| X3 | The fiber of `O` over `x0 = -1` has positive Haar measure in `Z_3` (integer density 0.516 up to `10^6`). | OPEN (EMPIRICAL support) | §5 |

## 3. Setting, normal form, exact description of the obstruction set

Map: `T(n) = n/2` (even), `(3n+1)/2` (odd). `X = Z_2 x Z_3`, integers embedded diagonally.
Moves at `(x, y)`: forward `T` with the branch chosen by the 2-adic parity of `x`; backward
doubling `D: z ↦ 2z`; backward odd branch `S: z ↦ (2z-1)/3`, legal iff `y ≡ 2 (mod 3)`.
A path acts on a neighbourhood as `n ↦ αn + β`. It is *descending* if `α < 1`, or `α = 1` and
`β < 0`. An *obstruction point* has no descending path; `O` is the set of obstruction points.

For a finite word `w` over `{0,1}` (0 = even step, 1 = odd step, first letter applied first) let
`f_w(t) = (3^{o(w)} t + c_w)/2^{|w|}` be the composed branch, `α_w = 3^{o(w)}/2^{|w|}` and
`y_w = f_w(0) = c_w/2^{|w|} >= 0` (the orbit of 0 driven by `w`).

**Normal form.** `T∘D = T∘S = id`, so a forward move after a backward move cancels, and every
path has the same affine map as a path "`p` forward moves, then `q` backward moves".

**Theorem G.** Let `u` be the parity word of `x0` and `u_p` its prefix of length `p`. The affine
maps realised by ordinary paths at `(x0, y0)` are exactly `f_v^{-1} ∘ f_{u_p}` with

    α_{u_p}·y0 + y_{u_p} ≡ y_v   (mod 3^{o(v)})   in Z_3,                       (V)

and then `α = α_{u_p}/α_v`, `β = (y_{u_p} - y_v)/α_v`. So `(x0, y0) ∈ O` iff every `(p, v)`
satisfying (V) has `α_v < α_{u_p}`, or `α_v = α_{u_p}` and `y_v <= y_{u_p}`.

*Proof.* Backward moves are always legal 2-adically. 3-adically, forward branches preserve
`Z_3`, so the backward word `v` is legal at `z ∈ Z_3` iff `f_v^{-1}(z) ∈ Z_3`, i.e. iff
`z ∈ f_v(Z_3) = y_v + 3^{o(v)} Z_3`. Apply this to `z = f_{u_p}(y0)`. ∎

Consequences.
- `v` empty gives: `(x0, y0) ∈ O` forces `3^{o_k} > 2^k` for every prefix of `u` (the
  *non-stopping set* `S_∞ ⊂ Z_2`, closed, measure 0). So `O` is closed and has measure 0.
- If `o(v) <= o(u_p)` then `3^{o(v)}` divides `α_{u_p}` and (V) does not involve `y0`: such a
  certificate is **purely 2-adic**, valid on a whole class mod `2^p`. Certificates with
  `o(v) > o(u_p)` are the ones that read the 3-adic coordinate.

## 4. Theorem A: `(-1, 0)` has no descending ordinary path

*Shadows.* For a path `n ↦ αn + β` put `x = -α + β` (image of `-1`) and `y = β` (image of 0).
Both follow the moves, the legality of `S` is read from `y`, and `α = y - x`.

*Proof.* Normal form: `p` forward steps give `(x, y) = (-1, (3/2)^p - 1)`, `α = (3/2)^p`. Then
apply `i` moves `S` and `j` moves `D`. Put `X = -x`. `X` starts at 1 and follows `X ↦ 2X`,
`X ↦ (2X+1)/3`, so `X >= 1` always, and `α = 2^j (3/2)^{p-i}`, `y = α - X`.

1. *While `i <= p`:* `X` is an integer with `1 <= X <= 2^j`, and an `S`-move made with `i < p`
   is legal iff `X ≡ 1 (mod 3)`. Induction: `y = 2^{j+i-p} 3^{p-i} - X ≡ -X (mod 3)`; `S` gives
   the integer `(2X+1)/3 <= (2·2^j+1)/3 <= 2^j`; `D` gives `2X <= 2^{j+1}`. Hence
   `α >= 2^j >= X`, so `y >= 0` and `α >= 1`, with equality only for `j = 0`, `i = p`: the path
   that returns to the start.
2. *Level nodes (`i = p`):* `α = 2^j` and `y = 2^j - X` is an integer `>= 0`.
3. *`i > p`:* just before the `(p+1)`-th `S`-move the node is a level node with `y ≡ 2 (mod 3)`,
   so `y` is a positive integer. From then on `y` stays a positive integer (`D` doubles it; `S`
   is applied only when `y ≡ 2 (mod 3)` and gives `(2y-1)/3 >= 1`). So `α = y + X >= 2`. ∎

The 3-adic shadow is therefore `>= 0` at every node: it never reaches a negative cycle (H).
The values `X` are the backward tree of 1 under `S(c) = c/2 | (3c-1)/2`; the one-`S` nodes are
`X = (2^b+1)/3`, `b >= 3` odd.

*Integer form (Lean).* `Inv n p w q o`, for `T^q(w) = T^p(n)` with `o` odd steps: either
`2^a (w+B) = 2^j 3^a (n+1)` with `o+a = p`, `o+j = q`, `1 <= B <= 2^j`; or
`3^e w = 2^d n + 3^e y` with `o = p+e`, `q = p+d`, `3^e (y+1) <= 2^d`. The base case is
`2^p (T^p(n)+1) = 3^p (n+1)`; `step_even`, `step_odd` propagate it backwards (`3^J ∣ n` is used
only in the second regime, `e+1 <= J`); `inv_le` gives `n <= w`.

*No finite cover.* A finite family of ordinary certificates has a maximal path length `L`.
By Z'' there are arbitrarily large `n` from which no walk of length `<= L` ends below `n`. This
also excludes finite families that are not affine or not tied to residue classes.

## 5. Theorem B: the fiber over `x0 = -1`

Let `Tree` be the set of `B >= 1` whose `S`-orbit reaches 1, and `j(B)` the number of even
`S`-steps on the way. Let `y0 >= 1` be an integer.

**Theorem B.** `(-1, y0)` has a descending ordinary path iff there are `y'' >= 1`, `t >= 1`,
`B ∈ Tree` with

    T^t(y'') = 2^{j(B)} (y0 + 1) - B      and      3^o > 2^{j(B)+t},

`o` = number of odd steps among the first `t` steps of `y''`. Any such `y''` is `< y0`.

*Proof.* As in §4 with `n+1` in place of the shadow of `-1`: while `i <= p` the node is
`(-B, α(y0+1) - B)` with `B ∈ Tree`, `B <= 2^{j(B)}`, `α = 2^{j(B)} (3/2)^{p-i} >= 1`, and the
legality of `S` depends on `B` only. Level nodes are `(-B, y')`, `y' = 2^{j(B)}(y0+1) - B`, a
positive integer, with `α = 2^{j(B)}`. Beyond a level node the shadow is a positive integer and
a backward word is exactly a backward Collatz path (`(2y-1)/3` is odd), so the node has shadow
`y''` with `T^t(y'') = y'` and `α = 2^{j(B)+t}/3^o`. Finally `α = (y'' + |x|)/(y0+1)` with
`|x| >= 1`, so `α < 1` forces `y'' < y0`. ∎

*Exact scan* (`fiber_scan.py 1000000`; every certificate replayed as a legal walk on actual
integers; verdicts for `y0 <= 45` cross-checked against exhaustive search to depth 22):

| class of `y0 <= 10^6` | obstruction points |
|---|---|
| `y0 ≡ 0 (mod 3)` | 324 696 / 333 333 = 0.9741 |
| `y0 ≡ 1 (mod 3)` | 191 682 / 333 334 = 0.5750 |
| `y0 ≡ 2 (mod 3)` | 0 (one `S`-move descends) |
| `3^M ∣ y0`, `M = 2..6` | 0.9814, 0.9894, 0.9938, 0.9954, 0.9978 |

First obstruction values: 0, 1, 3, 6, 7, 9, 12, 15, 16, 18, 19, 21, 24, 25, 27, 28, 33, 36, 37,
39, 42, 43, 45, ... First multiples of 3 that are not: 30, 81, 108, 111, 144, 192, 273, 333, 444.
The longest certificate kept by the scan has 162 moves.

## 6. Theorem C: `(-5, 0)` has no descending ordinary path

`-5 → -7 → -10 → -5` has parity word `(110)^∞`; `α_p = 3^{o_p}/2^p > 1` for `p >= 1`. Shadows:
`x` = image of `-5`, `y` = image of 0, `α = (y - x)/5`.

1. While the number `i` of `S`-moves is `<= o_p`: `x = -B` with `B` a positive integer in the
   `S`-basin of `{5, 7, 10}`, and `S` is legal iff `B ≡ 1 (mod 3)` (same argument as §4).
2. Every `B` in that basin is `>= 5` (1, 2, 3, 4 go to 1); every `B ≡ 1 (mod 3)` in it other
   than 7, 10 is `>= 13`.
3. A reduced path with `p >= 1` leaves the cycle by a doubling (from `-7` or `-10`; from `-5`
   no side branch exists) and stays off the cycle. With `B_t` the values where `S` is applied,
   `B = |x_p| 2^j (2/3)^i Π(1 + 1/(2B_t))`, and `5 α_p = |x_p| R_p`, `R_p` the product of
   `1 + 1/14` or `1 + 1/20` over the `o_p` odd forward steps. Since
   `Π <= (27/26)^i < (21/20)^{o_p} <= R_p`, we get `5α > B`, so `y > 0` and `α > B/5 >= 1`.
   For `p = 0` only doublings are legal and `α = 2^j`.
4. Level nodes (`i = o_p`): `α = 2^m`, `m >= 1`, `y' = 5·2^m - B` a positive integer.
5. Beyond: `y''` is a positive integer with `T^t(y'') = y'`, `α = (y'' + |x|)/5` with `|x| > 1`,
   and `α >= 2^m y''/y'` (strict if an odd step occurs). If `y'' >= 4` then `α > 1`. If
   `y'' ∈ {1, 2}` then `y' ∈ {1, 2}` and `α > 1`. If `y'' = 3` then `y' ∈ {3, 5, 8, 4, 2, 1}`;
   `y' <= 5` gives `α >= 6/5`, and `y' = 8` needs `m >= 2` because `B = 10 - 8 = 2 < 5` is
   impossible, giving `α >= 3/2`. ∎

The same scheme needs, for a negative cycle with least element `x0`: (H1) its `S`-basin has
minimum `|x0|`; (H2) backward products `Π` are dominated by the forward product; (H3) a finite
check of shadows `y'' <= |x0| - 2`. For the `-17` cycle the factor-by-factor comparison used
for (H2) fails (off-cycle basin values 49, 67 are below the cycle value 136).

## 7. Points that are not obstruction points

- `(-1, 30)`: `n ≡ 1 (mod 2)`, `n ≡ 30 (mod 3^8)` ⟹ `(2048n - 2391)/2187` is in the component.
- `n ≡ 15 (mod 64)`: forward `111100`, then one `S`: `w = (27n+11)/32`. The 3-adic coordinate is
  irrelevant (`o(v) = 1 <= 4`). The 2-adic point with word `111100 1^∞` is `-43/27 ∈ S_∞`.
- Conjecture N refuted: `u = 11101101101101010101101101101` (non-stopping, no `00`), backward
  word `DDSSDDSDDDSSDSDSSSSSSSSSSSS`, result `w = (3n+7)/4` for every `n` in one class mod
  `2^29`, total length 56, purely 2-adic (18 odd backward steps `<=` 19 forward). Found by
  exhaustive search over all 1 619 191 admissible `00`-free words of length `<= 30` with
  backward depth `<= 34`; for exactly 3 of them the side tree at the end of the word contains
  a descent (longer words inherit it from their prefix).

So the 2-adic projection of `O` is a proper subset of `S_∞`, and mixed forward/backward
certificates cover whole 2-adic cylinders that forward stopping does not.

## 8. Integer points

If `n ∈ C`, or the component of `n` contains a cycle, then `n` is not an obstruction point
(reach the cycle and go round it forwards: positive cycles have `3^o < 2^L`).
If the component of `n0` has no cycle and `Σ_k 1/T^k(n0) < ∞`, it contains an obstruction point:
the multiplier `μ(n0 → w)` is well defined on the component, `ρ(w) = μ(n0 → w)/w` does not
increase along forward steps, and `ρ(T^k n0) >= (1/n0)·exp(-(1/3) Σ 1/T^s(n0)) =: c > 0`; so
`μ(n0 → w) >= c·w`, the multiplier attains its minimum, and the least minimiser is an
obstruction point.

## 9. Empirical results (bounded searches; nothing here is a proof)

- `shadow_bfs.py 38 28`: `(-1,0)`: 503 842 nodes to depth 38, 0 invariant violations, 0
  descents. `(-1, y0)`, `y0 = -12, -9, ..., 63` step 3: only `y0 = 30` descends within depth 28.
- `integer_check.py 36`: balls of radius `L <= 36` around `n ≡ -1 (2^L)`, `0 (3^L)`:
  minimum is `n` (1 241 972 nodes); meet form with `K != J`: 2 031 915 nodes. `n = 27`: no
  smaller integer within walk radius 40.
- `cycle_points.py 38`, `capped_search.py`: `(-17, 0)`, `(-19/11, 0)`, greedy word with
  `y0 = 0`: no descent with `p <= 400` forward steps and backward part of multiplier `<= 2^16`
  (3.2 M, 0.3 M, 11.6 M nodes). Balls of radius `L <= 34` around `n ≡ x0 (2^L)`, `0 (3^L)` have
  minimum `n` for `x0 = -5, -17, -19/11`.
- `slice_experiments.py`: greedy word, `y0 = 0..45`, `p <= 300`, `q <= 30`: no descent for
  `y0 ∈ {0, 1, 3, 6, 7, 9, 12, 15, 16, 18, 19, 21, 24, 25, 27, 28, 33, 37, 39, 42, 43}`. Random
  admissible words with `y0 = 0`: `00`-free 0/100 descend within these bounds; unrestricted
  100/100 descend (30/30 purely 2-adic in `capped_search.py`).
- Uncovered measure (`uncovered_mc.py 100000 34`, seed 20261121, random 180-bit `n`):

| `L` | no forward descent in `L` steps | no ordinary walk of length `<= L` descends | ratio |
|---|---|---|---|
| 1 | 0.49820 | 0.33468 | 0.672 |
| 4 | 0.18717 | 0.10473 | 0.560 |
| 8 | 0.07381 | 0.03852 | 0.522 |
| 12 | 0.05555 | 0.02475 | 0.446 |
| 16 | 0.03232 | 0.01275 | 0.394 |
| 20 | 0.02610 | 0.00877 | 0.336 |
| 24 | 0.01725 | 0.00581 | 0.337 |
| 28 | 0.01334 | 0.00428 | 0.321 |
| 34 | 0.00891 | 0.00252 | 0.283 |

  Per-step decay over `L = 24..34`: 0.936 (forward), 0.920 (ordinary); the asymptotic forward
  rate is `2^-(1-H(log 2/log 3)) = 0.9659`. Rigorous: the uncovered set at depth `L` has measure
  `>= 6^-L` (Z') and tends to 0. Whether ordinary walks improve the exponential rate is OPEN.

## 10. First statement needed and not proved

A usable description of the 2-adic projection of `O`. Concretely the first instance that
stopped: **`(-17, 0)` is an obstruction point** (step (H2) of §6 needs a path-wise product
bound). Behind it: which non-stopping `x0` have no purely 2-adic descending path; and X3.

## 11. Relation to other work in the repo

- PR #146 (`lean/Collatz/ReverseBasin146.lean`): its finite cover uses the conditional rule
  `P(3n) → P(n)` on `n ≡ 3 (mod 6)`. Z'' shows some non-ordinary rule is unavoidable for any
  finite cover; every neighbourhood of `(-1, 0)` and `(-5, 0)` lies in `n ≡ 3 (mod 6)`.
- PRs #171, #179, #180 (reported by the coordinator; not read, not re-claimed): none decides
  this question. **Not compared** with the 437 unresolved cells of #180 or the exceptional set
  of #171. Only structural remarks: the proved points `(-1,0)`, `(-5,0)` are limits of integers
  divisible by high powers of 3, outside the ternary units of #171; the fiber points
  `(-1, y0)` with `y0 = 1, 7, 16, 19, ...` are limits of odd ternary units. Every neighbourhood
  used here has density tending to 0, so there is no conflict with a density-zero exceptional set.

## 12. Files and replay

All in `research/psi-closure-20261121/routes/cover/`. This agent edited no existing file and
made no commit. While it worked, the coordinating session swept the then-existing files of this
directory into wip commits (`a5e384e`, `e681fbf`, `ad37dcb`, each labelled unverified). At the
last check the branch was `claude/collatz-prs-discussion-qq2bvk` at
`ad37dcbd99d1701a7afc5c9be1329257d0ee785f`, the tracked copies were identical to the working
files, and `NOTES.md` was untracked.

`python3 -X utf8 -B tools/validate.py` was started once and refused to run ("tracked files or
index are dirty": a tracked file of the `layers` route, not of this route, was modified in the
working tree). So there is no repository validation result for this state.

| File | Tier | Command |
|---|---|---|
| `CoverObstruction.lean` | machine-checked, Lean 4.34.1 core, no imports | `lean -DwarningAsError=true CoverObstruction.lean` (exit 0; axioms `[propext, Quot.sound]`) |
| `shadow_bfs.py` | exhaustive bounded, exact rationals | `python3 -X utf8 -B shadow_bfs.py 38 28` |
| `integer_check.py` | exhaustive bounded, integers | `python3 -X utf8 -B integer_check.py 36` |
| `fiber_scan.py` | exact decision given Theorem B | `python3 -X utf8 -B fiber_scan.py 1000000` |
| `cycle_points.py` | replay of §6 invariants; EMPIRICAL for other points | `python3 -X utf8 -B cycle_points.py 38` |
| `no00_exhaustive.py`, `verify_no00_counterexample.py` | exact counterexample to N | `python3 -X utf8 -B no00_exhaustive.py 30 34 200` |
| `deep_slice_search.py`, `slice_experiments.py`, `capped_search.py`, `uncovered_mc.py` | EMPIRICAL | no arguments needed |

Strongest uncertainty: §5–§6 are written proofs checked only by bounded replay, not by Lean.
The Lean statements Z, Z', Z'' do not depend on them.
