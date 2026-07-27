```text
Claim ID:            Q-6174
Title:               The precise codimension target, and why the standard toolkit cannot reach it
Status:              OPEN QUESTION (with a scoped barrier argument, PROVED)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        T-6131, T-6170, R-6171, L-6130 (Terras bijection)
Scope:               elementary counting/dimension attacks on the full conjecture
TARGET NUMBER VOID:  T-6245.  The `0.415037` below is computed from R-6171's threshold
                     `log2(3/2)`, and that threshold is an artefact of a bound the above-line
                     condition forbids (T-6243a).  The requirement is not "codimension above
                     0.535" but "nu_L beats a polynomial", which the `0.050044` this file
                     computes ALREADY does.  The barrier argument in this file stands as a
                     statement about the toolkit's reach; its conclusion that the reach is
                     insufficient does not.  Read it as: the toolkit reaches exactly what is
                     needed, and what is missing is a LOWER bound on nu_L, which is a
                     different kind of object from anything (i)-(iii) produce.
```

## The question, stated as a number

R-6171 shows the self-referential loop closes iff the floor's growth exponent exceeds
`log2(3/2) = 0.584963`, and that the exponent supplied by the minimality constraint alone is
`1 - H_2(log2/log3) = 0.050044`. The exponent equals the **codimension** of the constraint
set. So:

```text
Q-6174.  Exhibit a constraint, satisfied by the minimal element of every Collatz
         counterexample, whose length-L prefix set has

                 dimension  <  1 - log2(3/2)  =  0.415037 ,

         equivalently at most  2^(0.415 L)  admissible prefixes of length L.
```

The minimality constraint alone gives `0.949956`. **The target is to remove `0.535` of
dimension**, i.e. to cut the admissible prefix count from `~2^(0.95 L)` to `~2^(0.415 L)`.

This is a well-posed, quantitative research target, and it is a far more useful thing to aim
at than "prove the conjecture".

## Why the standard toolkit cannot reach it (scoped barrier)

Consider arguments built from exactly three ingredients:

* **(i)** the Terras bijection: `Q_L : Z/2^L -> {0,1}^L` is a bijection (L-6130);
* **(ii)** the minimality inequality `T^j(m) >= m` for the orbit minimum;
* **(iii)** counting / measure / Hausdorff dimension.

Then:

1. **(i) forbids excluding any itinerary outright.** Every word of length `L` is realised, by
   exactly one residue class mod `2^L`. So no purely itinerary-local constraint — no forbidden
   factor, no subshift, no automaton — can be imposed a priori. Any constraint must come from
   the interaction of the word with the *value*.
2. **(ii) is the only such interaction available, and it yields the above-line condition.**
   R-6171(a) derives it exactly: `T^j(m) >= m` forces `k_j(m) > alpha j - 1` for
   `j < log_{3/2}(m) - 1`, and for large `m` the additive terms wash out, leaving precisely
   `k_j >= alpha j`.
3. **(iii) applied to that condition gives dimension exactly `H_2(alpha) = 0.949956`**
   (T-6131c) — not an estimate, the exact value, with the lower bound coming from
   Besicovitch-Eggleston. So the codimension is exactly `0.050044` and cannot be improved
   within (i)-(iii).

Therefore an argument of this shape is short by a factor of `11.69` and no sharpening of the
estimates can help: the shortfall is between two exact constants, `log2(3/2)` and
`1 - H_2(log2/log3)`.

**What this is not.** It is not a claim that Collatz is unprovable, nor a barrier in the
Baker/relativisation sense. It says: *these three ingredients, in this combination, cap out at
codimension `0.050`, and the loop needs `0.585`.* A successful attack must add a fourth
ingredient — something that constrains which above-line itineraries are realisable **by an
integer that is its own orbit minimum**, which is exactly the information (i) says the
itinerary alone does not carry.

## Where a fourth ingredient might come from

Recorded as leads, not results. Each is judged by the only criterion that matters here: does
it plausibly remove `0.535` of dimension?

* **Simultaneous minimality along the orbit.** Every `n_j` also satisfies `n_i >= m` for
  `i > j`. For a *cycle* this is strong — the orbit returns near its minimum every period, so
  the above-line condition is re-imposed from every near-minimal position — and it is
  essentially what produces the convergent condition of T-6141. For a *divergent* orbit it is
  weak: `n_j -> infinity`, so the constraint from time `j` is slack. **Verdict: promising for
  the cycle lane only** — which is consistent with T-6140, where the cycle lane is the one
  with real leverage.
* **3-adic or mod-`3^k` structure.** I flagged this as the one lead not obviously capped, then
  tested it. **Verdict: dead, and its death strengthens the barrier.**

  *Addendum (PROVED).* For every odd modulus `M` and every `L`, each length-`L` itinerary
  occurs together with **every** residue class mod `M`. Proof: the itinerary is a function of
  `n mod 2^L` (L-6130) and `gcd(2^L, M) = 1`, so by CRT the two are independent. Verified for
  `M = 5, 7, 27, 35, 81` in `crt_independence.py`.

  Consequently **no congruence condition at an odd modulus can reduce the dimension of the
  itinerary constraint set at all** — conditioning on a residue class mod `M` leaves the
  itinerary set unchanged. This extends the barrier from "itinerary-local constraints" to
  "itinerary-local constraints together with arbitrary odd-modulus congruence data", which is
  the entire modular toolkit.

  Genuine 3-adic facts exist — e.g. after any odd step the value is `= 2 (mod 3)`, so the orbit
  never meets a multiple of 3 again — but they constrain the **value**, not the itinerary, and
  are therefore invisible to any dimension argument.

  (Recorded process note: the first version of this check reported `False` and looked like a
  crack. It was an off-by-one — the scan covered `[1, M*2^L)` instead of a full period, so
  classes containing `0` were one short. Verified over the full period, it is `True`.)
* **Congruence conditions on `m`** (odd, not divisible by 3, exceeding the verification
  bound). **Verdict: dead.** Finitely many congruences change the floor by a bounded factor,
  not by an exponential rate; and the verification bound fixes the loop's starting depth, not
  its slope, so the verdict is scale-invariant (R-6171 gap audit).
* **Sharper additive control** (tracking `c_j` exactly instead of bounding it). **Verdict:
  dead.** The additive terms only affect the `O(1)` in `k_j > alpha j - 1`; the exponent is
  unchanged.

## Where the remaining hope actually is: the backward direction

With the forward direction capped, the only standard approach left is not about itineraries at
all — the **backward tree / coverage-deficit** route (this repository's issue #25): bound below
the count of `n <= X` that reach 1, and push the exponent to 1.

That route is not touched by anything in this file, because it never speaks of a
counterexample's itinerary. And the quantitative comparison is striking:

| route | quantity | have | need | gap |
|---|---|---|---|---|
| forward / self-referential | dimension of the constraint set | `0.949956` | `< 0.415037` | `0.534918` |
| backward / coverage | exponent of `#{n <= X reaching 1}` | `~0.84` (literature) | `1` | `~0.16` |

**The backward gap is numerically narrower — but it is not the same kind of object, and this
comparison must not be quoted as if it were.** Closing the forward gap would *prove the
conjecture*; closing the backward one would not, since `X^{1-o(1)}` coverage permits
`X^{o(1)}` exceptions. The backward target is both nearer and weaker (O-6182).

What survives, and is the sharpest direction this namespace can offer: **the backward lane is
the one not capped by T-6131**, because it never speaks of a counterexample's itinerary.

Measured (X-6180, `X = 10^8`): the exponent `0.84` is reached at backward-tree depth `65`
(only `2.45 log2 X`), while full coverage needs depth `592`. So the difficulty in that lane is
not depth — it is the tail: `0.84 -> 1` costs a factor `9` in depth, and the last `0.05%` of
integers need more depth than the first `99.95%`.

*Caveat:* the `0.84` is the Krasikov-Lagarias-type exponent taken from memory of the
literature; it cannot be verified from inside this repository and should be checked and cited
properly before anyone relies on the comparison. The forward number is proved here.

## Adversarial tests

* The target number is self-consistent: `1 - log2(3/2) = 0.415037` and
  `H_2(log2/log3) = 0.949956`, so the required reduction `0.949956 - 0.415037 = 0.534918`.
* CRT independence verified for `M = 5, 7, 27, 35, 81` over full periods, after an off-by-one
  in the first attempt produced a false positive.
* The claim that (ii) yields nothing beyond the above-line condition is checked numerically in
  X-6170: the value-based floor `s_L` and the itinerary-based floor `nu_L` coincide for every
  `L <= 375` (O-6172). If the value information carried extra constraint, the two would
  separate.

## Suggested next attack

Anyone proposing a new elementary attack on the full conjecture should first answer: **what is
your constraint's dimension?** If it is above `0.415037`, the self-referential loop cannot
close, whatever else is true about the argument. That single question disposes of a large
class of proposals in one line, which is the practical value of this file.
