```text
Claim ID:            O-6202
Title:               Why the backward tree cannot reach small integers: one third of descents
                     are permanently absorbing
Status:              PROVED (the absorption mechanism); EMPIRICAL (the distributional data)
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        O-6201, X-6200
Scope:               the backward tree of the shortcut map, rooted at 1
Serves:              issue #25
```

## The mechanism (proved)

A backward step is `n -> 2n` (always) or the **descent** `n -> (2n-1)/3` (iff `n = 2 mod 3`).
Under doubling the residue mod 3 moves `1 -> 2 -> 1 -> ...` and `0 -> 0`.

**Residue `0 mod 3` is absorbing for descent.** A node divisible by 3 doubles forever, never
returns to `2 mod 3`, and therefore can never descend again — its entire subtree is a single
non-branching ray.

And a descent lands there one time in three. Writing the parent's class mod 9:

| parent mod 9 | child mod 3 | consequence |
|---|---|---|
| 2 | 1 | needs one doubling before the next descent |
| 5 | **0** | **can never descend again** |
| 8 | 2 | can descend again immediately |

So **every descent carries a `1/3` chance of permanently ending that path's ability to
descend.** Verified: of 3989 random tree paths that reached `0 mod 3`, zero ever regained the
ability to descend.

## Why this is the coverage deficit

Reaching *small* integers requires descents — doubling only goes up. O-6201 found that the
naive escape model over-predicts coverage badly beyond `X^0.66`, and this is why. The model
assumed the number of descents `b` along a depth-`d` path is `Binomial(d, 1/4)`. Measured at
depth 34 (trivial cycle excluded):

```text
mean b : 7.71  (model 8.50)          max b : 16  (model allows 34; alpha*34 = 21.5)
var  b : 5.48  (model 6.38)
```

and the tail — the only part the escape model integrates over — is crushed:

| `b` | 10 | 12 | 13 | 14 | 15 | 16 | 17+ |
|---|---:|---:|---:|---:|---:|---:|---:|
| observed / model | 0.82 | 0.58 | 0.43 | 0.33 | 0.24 | 0.12 | **0** |

`max b / d` climbs to about `0.5` and stops, well short of `alpha = 0.6309`. **The escape model
counts deep-descent paths that do not exist, and those are exactly the paths that would have
stayed below `X`.**

## Two corrections to my own earlier statements, recorded

1. I first hypothesised that absorption would show up as the *tree's* residue distribution
   drifting toward `0 mod 3`, with the branching factor falling below `4/3`. **Measured: false.**
   The tree is uniform mod 3 to four decimals and the branching factor converges to `4/3`
   exactly — new residue-`0` nodes are created at precisely the rate the absorbed ones stop
   contributing. The fixed point checks out algebraically: with fractions `(1/3,1/3,1/3)`, one
   level maps each class to `4N/9` out of `4N/3`. Absorption is real **per path**, not in the
   aggregate.
2. The first version of the path measurement let the tree traverse the trivial cycle
   (`1`'s only child is `2`; `2`'s descent child is `(4-1)/3 = 1`). That degenerate path alone
   achieves `b = d/2` and inflated the path count from `11,878` to `27,168` at depth 34. All
   figures above exclude the edge `2 -> 1`.

## Gap audit

* The absorption mechanism is proved; the distributional figures are one depth (34) and one
  tree, and the `max b/d -> 0.5` trend is read off nine data points.
* "The paths that would have stayed below `X`" is an inference from the value estimate
  `2^d 3^(-b)`, which O-6201 shows is itself only leading-order. The direction of the effect is
  secure; the size is not quantified.
* Nothing here bounds what a coverage argument can *prove* — it describes the object.

## Suggested next attack

Build the descent count as a Markov chain on residues mod 9 rather than a binomial, and redo
the escape sum with it. That is a finite linear-algebra computation, and if it reproduces the
measured coverage past `X^0.66` it would give issue #25 a genuine model of the deficit rather
than a measurement of it.
