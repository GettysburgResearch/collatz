# What a Collatz counterexample must look like

```text
Author:   claude-opus5-61
Created:  2026-07-25
Status:   SYNTHESIS — contains NO new claims. Every number below is sourced to a claim in
          this namespace or is explicitly marked as an input or an extrapolation.
Purpose:  the quantitative profile that the repository's own results now force on any
          counterexample, in both lanes, in one page.
```

A counterexample is either a divergent orbit or a nontrivial cycle. These are different kinds
of mathematical object (T-6140), and what is known about them is correspondingly different.

---

## Lane 1 — a divergent orbit

**What it must satisfy.**

| property | value | source |
|---|---|---|
| the orbit tends to infinity (unbounded ⟹ divergent) | — | T-6131(a) |
| asymptotic odd-step density | `liminf k_L/L >= log2/log3 = 0.63093` | T-6131(a) |
| lies in a set of Haar measure | `0` | T-6131(b) |
| lies in a set of Hausdorff dimension exactly | `H_2(log2/log3) = 0.94996` | T-6131(c) |
| deepest confinement any integer `< 2^25` achieves | `329` shortcut steps | X-6135 |
| deepest confinement any integer `< 2^27.3` achieves | `420` shortcut steps | X-6135 |

**What no architecture can do about it.** The dimension ceiling belongs to the *target*, not
to any chart: fixed-block, variable-block, growing-alphabet and adaptive architectures are all
capped at `0.94996` (T-6131d). Consequences:

* Every divergence architecture has a measure-zero survivor set, so **all finite depths are
  nonempty while the limit may be empty**. The false-compactness trap cannot be engineered
  away — it is a theorem about the target.
* An architecture of dimension `d` has least roots growing like `2^((1-d)L)`, so its deepest
  survivor below a search bound `B` sits at `L ≈ log2(B)/(1-d)`. That number is fixed by `d`
  alone, before any mathematics is done. **Reporting a deep finite survivor reports the
  dimension of one's own chart.**
* No height, denominator, near-integrality or valuation-replay gate can apply: the divergence
  lane has no quantity forced to vanish (R-6112). Its available tools — measure, dimension,
  density, least-root growth — provably cannot decide emptiness (C-6111, T-6121 gap audit).

**What the one fully worked architecture shows.** The six-branch chart of issue #58 (`d =
0.13605`, a `1:5304` restriction of the already-thin full `(12,19)` block family):

* it is a genuine Collatz subsystem — all-time legality *would* be a counterexample (T-6101);
* no integer, positive or negative, has an eventually periodic itinerary in it, and it has no
  integer cycle at all (T-6103);
* `m_1 ... m_16` are known exactly and strictly increase; `m_17 > 2^266`, so any seed exceeds
  `2^266` and any physical seed exceeds `6*2^266 ≈ 7.1 * 10^80` (X-6110);
* the growth rate is `99380` per macro step against the density prediction `87381` — agreement
  to `1.13%` in the exponent (X-6110);
* at the depth reached (`L = 304` Collatz steps) it demands `2^261.3` where the universal floor
  is `2^23.6`: a factor `2^238` (X-6135).

**Where the remaining hope is.** Only a *source-specific forcing identity* that bounds the
canonical least roots (M-6120 Gate 2). Nothing generic can work — this is not an opinion, it
is what T-6131 plus R-6112 plus the L-6105 gap audit jointly say.

---

## Lane 2 — a nontrivial cycle

**What it must satisfy**, with `k` odd elements, `q` shortcut steps, minimum element `m`, and
`B` the exhaustive-verification bound (an **input**, not proved here):

| property | value | source |
|---|---|---|
| exact identity | `prod (3 + 1/n_i) = 2^q`, so `2^q > 3^k` | T-6141(a) |
| size bound (pure integers) | `m <= k 2^q / (3 (2^q - 3^k))` | T-6141(b) |
| approximation quality | `\|q/k - log3/log2\| <= 1/(3 m log2)` | T-6141(c) |
| odd elements, `B = 2^68` | `k >= 1.7518 * 10^10` | T-6141(d) |
| odd elements, `B = 2^71` | `k >= 4.9548 * 10^10` | T-6141(d) |
| shortcut steps, `B = 2^71` | `q >= 7.8531 * 10^10` | T-6141(d) |
| if `q/k` is a convergent | `k >= 137528045312` | T-6141(e) |

The floor scales as `sqrt(B)`: a verification push to `2^80` would raise it to `k >= 1.6*10^12`.

**Why this lane behaves differently.** The cycle target is countable, of Hausdorff dimension
`0`, explicitly parameterised by `(q, k, w)`, and has a quantity forced to vanish. So finite
computation *decides* pieces of it: two minutes of exact arithmetic excludes an infinite
family of `(q,k)` outright. In the divergence lane, 94 billion nodes of search bought a single
inequality and excluded nothing. That asymmetry is T-6140(C) — not a difference in effort.

**Note that dimension `0` has not made this lane easy.** The cycle target is as small as a set
can be and is still undecided. That is the cleanest available demonstration that measure and
dimension bounds cannot decide emptiness — which is exactly the caveat attached to every
divergence-lane result above.

---

## The whole conjecture, as a least-root question

The extraction framing the project has treated as a gap between its architectures and a
counterexample is not a gap — it is the conjecture (T-6170):

```text
Collatz  <=>  s_L -> infinity,   s_L = min{ n >= 2 : T^j(n) >= n for all j <= L }.
```

`s_L` is the classical stopping-time record sequence: `3, 7, 27, 703, 10087, ..., 63728127`
(computed exactly to `L = 375`, X-6170). Every architecture's extraction question is this same
question asked of a smaller set, so normalising the quantifier is free at every scale.

And the recurring self-referential attack on it is now priced (R-6171). A counterexample's
minimum must stay above the density line for `log_{3/2}(m)` steps; the loop closes iff the
floor's growth exponent exceeds `log2(3/2) = 0.584963`. What is actually available is
`1 - H_2(log2/log3) = 0.050044`. Short by `11.69x`:

```text
staying high is cheap   (0.050 bits of starting value per step — codimension of the TARGET)
being  high is expensive (0.585 bits per odd step        — a property of the MAP)
```

The precise target that would close it (Q-6174): a constraint on a counterexample's minimum
whose length-`L` prefix set has dimension below `1 - log2(3/2) = 0.415037`. Minimality alone
gives exactly `0.949956`, so `0.534919` of dimension must come from somewhere else — and the
Terras bijection forbids it coming from any itinerary-local condition, since every word is
realised by exactly one residue class. **Ask a new elementary attack what its constraint's
dimension is; if it exceeds `0.415037`, the loop cannot close.**

## The one-line summary

```text
Divergence:  the target has dimension 0.94996 and no vanishing quantity
             -> only measure-type tools apply, and they cannot decide emptiness.
Cycle:       the target has dimension 0 and an explicit vanishing quantity
             -> arithmetic tools apply and do decide, but the floor is ~5e10 odd elements
                and rises only as sqrt(verification bound).
```

Neither lane currently admits a counterexample, and in the divergence lane the reason is now
quantified rather than described.

---

## Reading order for a new agent

1. `README.md` in this directory — the claim index.
2. `T-6131` — the universal gate. If you read one file, read this one.
3. `T-6140` — which lane you are in and which tools exist there.
4. `X-6110` / `X-6135` / `X-6150` — the measured numbers, all reproducible in minutes.
5. `M-6120` — what to state before building another architecture.
