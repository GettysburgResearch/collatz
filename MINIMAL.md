# The Minimal Statement

Every reduction in this program — radix rewrite, −17 phases, H-frame,
atlas, stack amplifiers, schedules, supply statistics — funnels into one
statement. This document fixes its exact form, its equivalents, its
trivial solutions, its nearest named relatives, and the one reduction
that looks genuinely attackable.

## Setup (all previously verified)

`H(64B+ε) = 81B+ε` for ε ∈ {0,1}; one H-step = 6 shortcut Collatz steps
on `n = (81A − 146)/17` when `A ≡ 6 (mod 17)` (charts 0/8/3 analogous);
`V∞ = {A ∈ ℤ₂ : every H-iterate has base-64 digit ∈ {0,1}}` is the
attractor of the contractions `J_ε(x) = (64x+17ε)/81` on ℤ₂ and is
homeomorphic to `{0,1}^ℕ` (Theorem 2). Valid orbits grow strictly
(`A_{t+1} − A_t = 17B > 0` off the trivial digits).

## M1 (existence form)

> **Does `V∞` contain a positive integer `A ≡ 6, 0, 8, or 3 (mod 17)`?**

*Yes* ⟹ the Collatz conjecture is false, with an explicit divergent
orbit. (One direction only — this subsystem is one road to divergence,
not all of Collatz.) The only integers known in `V∞` are the trivial
digits {0, 1}, which lie in classes 0 and 1 mod 17: **not** in any
chart class... (0 mod 17 = chart class 0 — but A = 0 gives n ≤ 0; A = 1
gives the fixed digit, n non-positive as well: no Collatz content).

## M2 (2-adic Mahler form)

`V∞`-membership says: the orbit of A under multiplication by 81/64
(with the ε-carry making it integral) keeps all base-64 digits in
{0,1}. This is precisely a **2-adic analogue of Mahler's Z-number
problem** (Mahler 1968: does ξ(3/2)^n mod 1 ∈ [0,½) for all n have a
solution?), with 3/2 replaced by 81/64 and the archimedean digit
constraint replaced by a 2-adic one. Mahler's problem is open;
Flatto–Lagarias–Pollington's interval obstruction (`limsup − liminf ≥
1/p` for (p/q)^n ξ mod 1) does not transfer: our constraint set has
2-adic measure 1/32 > 1/81, on the wrong side of the FLP threshold.
The real-side IFS `{J₀, J₁}` has attractor exactly [0,1] (overlapping,
similarity dimension log 2/log(81/64) ≈ 2.94 > 1): **no archimedean
obstruction exists at all** — the tension is purely 2-adic vs. size.

## M3 (counting form — the attackable reduction)

Let `R_K = {A mod 64^K : A valid for K steps}` — exactly the `2^K`
coded residues (Theorem 2). Integers in `[1, 64^K]` valid for K steps
are exactly the elements of `R_K` (as integers): **exactly `2^K =
(64^K)^{1/6}` survivors of the "fair" window.** A counterexample needs
survivors of *every* window length; the natural quantitative question:

> **How small can a nontrivial element of `R_K` be?**

Model: if `R_K` were archimedean-equidistributed in `[0, 64^K)`, its
smallest nontrivial element would be `≍ 64^K/2^K = 32^K`, and the count
of integers `< X` valid for `(1+δ)log₆₄X` steps would tend to 0 for
every `δ > 0` — *quantitative near-emptiness*, the strongest partial
result toward M1 short of solving it. So M1 reduces (in the negative
direction) to:

> **(EQ) The coded sets `R_K` are archimedean-equidistributed at scale
> `64^K/2^K`** — an explicit self-similar-set equidistribution
> statement, in range of modern Fourier-decay-of-self-similar-measures
> techniques (the recursion `R_K = 81^{-1}(64·R_{K−1} + 17ε)` is an
> affine IFS with a fixed multiplicative twist; Rajchman/decay results
> of the Li–Sahlsten / Solomyak school apply to exactly this shape of
> system, though over ℝ rather than mixed ℝ/ℤ₂).

EQ would prove: **almost no integer survives materially past its fair
window** — turning the free-fuel measurements (all Geometric-null) into
a theorem, and pinning any counterexample to an event of vanishing
density at every scale.

## Status of the pieces

| piece | status |
|---|---|
| designed fuel finite, steering constructible | proved (Lemma C, towers) |
| ensemble statistics exactly generic | proved (Theorem 5, isometry) |
| unsteered coincidences finite | proved (Theorem 6, SML) |
| periodic/automatic certificate formats | dead (Thms 1–4, Cobham, G–S) |
| EQ (equidistribution of `R_K`) | open — numerically testable now |
| M1 itself | the conjecture (2-adic Mahler for 81/64) |

`experiments/minimal_survivors.py` enumerates `R_K` completely for
K ≤ 20 (2^20 residues), finds the exact extremal survivors far beyond
any orbit-scan range, and measures the equidistribution EQ needs.

## Enumeration results (K ≤ 20, `results/minimal-survivors.log`)

* `|R_K| = 2^K` exactly at every level (coding theorem re-verified by
  full enumeration to K = 20 — over the implicit range `64^20 ≈ 1.3×10³⁶`).
* **Survivor law confirmed:** min nontrivial element of `R_K` tracks the
  equidistribution prediction `32^K` within a factor `[0.19, 1.9]` for
  all K = 2…20, no drift. At K = 20 the extremal survivor is a 101-bit
  integer with run/fair-window = 1.19, and the maximum excess among the
  200 smallest survivors is **1.188** — no integer materially outruns
  its designed window.
* **EQ verified at measured scales:** bucket χ² → ~df for K ≥ 16
  (converging to uniform; small-K spikes are the self-similar measure's
  low-scale structure washing out), and the tail counts match
  equidistribution exactly: 4 vs 4.0 predicted at `64^{0.85K}`,
  16,397 vs 16,384 at `64^{0.95K}`, and the only elements below
  `64^{0.7K}` are the trivial {0,1}.
* Chart classes are independent of validity: 0.2352 vs 4/17 = 0.2353.

The program's empirical picture is now complete and self-consistent
with all seven theorems: survivors exist in exactly the fair-window
numbers, sized exactly as equidistribution demands, with no anomalies.
Proving **EQ** (Fourier decay / equidistribution of the twisted
self-similar sets `R_K`) is the one concrete open problem this program
puts on the table: it would convert every null measurement here into a
theorem — quantitative near-emptiness of survivors — and is the
sharpest statement short of M1 itself.
