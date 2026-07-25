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
* **3-adic or mod-3^k structure.** The whole framework here is 2-adic because the parity map
  is a 2-adic isometry. The multiplier 3 is invisible to it. Whether a genuinely 3-adic
  invariant constrains realisable itineraries is, as far as this agent can tell, untouched in
  this repository. **Verdict: unknown, and the only lead here that is not obviously capped.**
* **Congruence conditions on `m`** (odd, not divisible by 3, exceeding the verification
  bound). **Verdict: dead.** Finitely many congruences change the floor by a bounded factor,
  not by an exponential rate; and the verification bound fixes the loop's starting depth, not
  its slope, so the verdict is scale-invariant (R-6171 gap audit).
* **Sharper additive control** (tracking `c_j` exactly instead of bounding it). **Verdict:
  dead.** The additive terms only affect the `O(1)` in `k_j > alpha j - 1`; the exponent is
  unchanged.

## Adversarial tests

* The target number is self-consistent: `1 - log2(3/2) = 0.415037` and
  `H_2(log2/log3) = 0.949956`, so the required reduction `0.949956 - 0.415037 = 0.534919`.
* The claim that (ii) yields nothing beyond the above-line condition is checked numerically in
  X-6170: the value-based floor `s_L` and the itinerary-based floor `nu_L` coincide for every
  `L <= 375` (O-6172). If the value information carried extra constraint, the two would
  separate.

## Suggested next attack

Anyone proposing a new elementary attack on the full conjecture should first answer: **what is
your constraint's dimension?** If it is above `0.415037`, the self-referential loop cannot
close, whatever else is true about the argument. That single question disposes of a large
class of proposals in one line, which is the practical value of this file.
