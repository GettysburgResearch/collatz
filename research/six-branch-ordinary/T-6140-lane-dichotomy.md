```text
Claim ID:            T-6140
Title:               Cycle lane and divergence lane are structurally different targets;
                     technique transfer is impossible in one direction
Status:              PROVED (the mathematical content); the cartography is a reading of it
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        T-6131, R-6112, L-6130 (in T-6131), T-6103 (the six-branch instance)
Scope:               the full shortcut Collatz map
Related counterexample candidates: constrains how both lanes may be attacked
Serves:              issue #36 / PR #38 (global dependency map and atomic blockers)
Duplication warning: the cycle-side facts below are classical and very likely overlap with
                     existing 42xx/50xx/83xx material. The *dichotomy* is the contribution;
                     an integrator should cross-reference rather than re-import the classics.
```

## Statement

Let `T` be the shortcut map and let `alpha = log2/log3`.

**(A) The cycle target is countable, explicitly parameterised, and rational.**
The set `C ⊂ Z_2` of points with eventually periodic `T`-orbit is countable; hence
`Haar(C) = 0` and `dim_H(C) = 0`. Every purely periodic point is the explicit rational

```text
x_w = c_w / (2^L - 3^k),      c_w = sum_{i=1..k} 3^(k-i) 2^(e_i),
```

for its period-`L` parity word `w` with `k` ones at positions `e_1 < ... < e_k`. For each
`(L,k)` the possible values are confined to the explicit window

```text
(3^k - 2^k)/(2^L - 3^k)   <=   x_w   <=   2^(L-k) (3^k - 2^k)/(2^L - 3^k)
```

when `2^L > 3^k` (and symmetrically negative when `2^L < 3^k`).

**(B) The divergence target is uncountable, unparameterised, and of near-full dimension.**
By T-6131 the set `D = {x : liminf k_L(x)/L >= alpha}` containing every divergent orbit has
`Haar(D) = 0` but `dim_H(D) = H_2(alpha) = 0.94996`. It has cardinality of the continuum, and
no element of `D` is forced to satisfy any vanishing identity.

**(C) Consequences for method.**

| | cycle lane | divergence lane |
|---|---|---|
| target cardinality | countable | continuum |
| Hausdorff dimension | `0` | `0.94996` |
| explicit parameterisation | yes, by `(L,k,w)` | none |
| a quantity forced to vanish | yes: `R = C - N(2^A - 3^K)` | **no** (R-6112) |
| Archimedean window per parameter | yes, finite check | vacuous (R-6112(b)) |
| height / denominator gates | available | **provably unavailable** |
| measure / dimension gates | vacuous (dimension already 0) | available, but cannot decide emptiness |
| finite prefixes decide? | yes per `(L,k)` | never (L-6105 gap audit) |

**(D) Transfer is asymmetric.** No cycle-lane height argument can be ported to the divergence
lane (R-6112: there is no small quantity). No divergence-lane dimension argument can be ported
to the cycle lane (the cycle target already has dimension `0`, so the bound is vacuous there
and excludes nothing). The two lanes therefore need genuinely different tools, and a result in
one is not evidence of progress in the other.

## Proof

**(A)** Eventually periodic parity words are countable: for each preperiod `m` and period `L`
there are at most `2^(m+L)` of them. By L-6130 the parity map is a bijection `Z_2 -> {0,1}^inf`
and the orbit is eventually periodic iff the parity word is, so `C` is countable; a countable
subset of `Z_2` has measure `0` and Hausdorff dimension `0`.

For the formula, let `w` be purely periodic of period `L` with `k` ones. Applying `T` around
one period gives the exact affine identity `2^L x = 3^k x + c_w`, i.e.
`x_w = c_w/(2^L - 3^k)`. (This is the standard cycle equation; T-6103(b) is the same
computation carried out inside the six-branch chart, where it produces the native ghost
window.)

For the bounds, `c_w = sum_{i=1..k} 3^(k-i) 2^(e_i)` with `0 <= e_1 < ... < e_k <= L-1`. The
sum is minimised by `e_i = i-1` and maximised by `e_i = L-k+i-1`:

```text
min c_w = sum_{i=1..k} 3^(k-i) 2^(i-1) = 3^k - 2^k,
max c_w = 2^(L-k) sum_{i=1..k} 3^(k-i) 2^(i-1) = 2^(L-k) (3^k - 2^k).
```

Dividing by `2^L - 3^k` gives the window. `QED`

**(B)** T-6131(b),(c). `D` is uncountable because it contains a set of positive Hausdorff
dimension. `QED`

**(C),(D)** Read off from (A),(B) together with R-6112. The one line that needs stating: a
dimension bound `dim_H(S) <= t` is informative only when `t < dim_H` of the ambient search
space *and* the argument being replaced is a covering argument. For the cycle lane the target
already has dimension `0` and is still not known to be empty, which is precisely the
demonstration that dimension bounds cannot decide emptiness — the same warning that C-6111 and
T-6131's gap audit attach to the divergence lane. `QED`

## Motivation

The project's global audit treats "cycle route" and "divergence route" as two roads to one
destination, and repeatedly proposes carrying machinery between them. (A)-(D) show they are
different kinds of object, and make precise which carrying is possible:

* The cycle lane is a **Diophantine** problem. Its target is a countable, explicitly listed
  family of rationals; the whole difficulty is integrality of `c_w/(2^L - 3^k)`, and height,
  denominator, valuation-replay and near-integrality arguments all have purchase because a
  specific quantity must vanish. PR #50's `L-8310` is the right shape of tool for this lane.
* The divergence lane is a **dimension** problem. Its target is a Cantor set of dimension
  `0.94996` with no parameterisation and no vanishing quantity. Every tool that works in the
  cycle lane is provably inapplicable (R-6112), and the tools that *are* available — measure,
  dimension, density, least-root growth — are exactly the ones that cannot decide emptiness.

That asymmetry, not any individual construction, is why the positive lane keeps arriving at
the same wall while the cycle lane keeps producing real (if insufficient) exclusions.

## Gap audit

* *Is (A) new?* **No.** The cycle equation and its window are classical (Crandall 1978,
  Steiner 1977, Simons-de Weger 2005 and the surrounding literature) and are almost certainly
  present in this repository already. The claim is recorded here only so that (C)/(D) have a
  stated dependency; an integrator should replace the (A) block with a pointer to whichever
  existing claim states it first.
* *Does (C)'s "height gates unavailable" overstate R-6112?* R-6112 proves the direct analogue
  of the cycle-side quantity is a large positive integer, so *that* gate cannot exist. It does
  not prove no conceivable height argument exists for any derived quantity; the table entry
  should be read with R-6112's own gap audit attached.
* *Does dimension `0` for the cycle lane mean the cycle lane is "easier"?* No, and the file
  says the opposite: dimension `0` and still undecided is the demonstration that dimension is
  the wrong instrument there.
* *Is `C` really the right cycle target?* `C` is all eventually periodic points in `Z_2`; the
  Collatz cycle question is about the positive integers inside it. The countability and
  parameterisation, which is all (C)/(D) use, are unaffected.

## Adversarial tests

* The six-branch chart is an instance of (A) restricted to one subsystem, and the two windows
  live in **different coordinates** — T-6103's `[-57.786, -32.067]` is in the chart coordinate
  `x`, while (A) is in the physical coordinate `n`. Pushing the chart window forward by
  `n = 6x-5` gives `[-351.72, -197.40]`, and the general `(L,k) = (19,12)` window is
  `[-9436.62, -73.72]`; the former is contained in the latter, as it must be, since the chart
  uses 6 of the 31824 available words. Verified in `audit_premises.py`. (Checking this
  containment naively in the chart coordinate would appear to *fail* — `-32.07 > -73.72` — so
  the coordinate change is load-bearing, not cosmetic.)
* The six-branch constants are the general ones specialised: `c_w` for the word `W_0` is
  `kappa_0 = 35765 + 6 a_0 = 1412021`, and `x_w = 1412021/(2^19 - 3^12) = -1412021/7153 =
  -197.40`, matching the crosswalk certificate of T-6101.
* Numerically, for `(L,k) = (4,3)` — the parity word `1110` — (A) gives
  `x_w = c_w/(2^4 - 3^3) = 19/(16-27) = -19/11`, matching the native ghost verified in
  `audit_premises.py`. The negative sign is the `2^L < 3^k` branch of the window.

## Suggested next attack

For the integrator: fold (C)'s table into the global dependency map (issue #36 / PR #38) as the
top-level split, and route new proposals by which column they live in. For researchers: a
proposal should state its lane and, if it claims a technique from the other lane, cite the
line of (D) it intends to defeat.
