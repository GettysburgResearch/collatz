# Synthesis with the newly published phase and descent packets

**Status: PROPOSED written deductions with separate reconstruction. Collatz
remains OPEN.** These deductions were added after the first publication of
PR194. They have no new Lean compilation claim. The previously compiled finite
kernels retain their source identities and evidence scope.

## Frozen sources and scope

- PR192, `be783656f0e889fe0d5318a2f7a9140099cb94b5`,
  [phase separation PS1--PS6](https://github.com/GettysburgResearch/collatz/blob/be783656f0e889fe0d5318a2f7a9140099cb94b5/research/astra-phase-and-cycle-20261124/PHASE_SEPARATION.md)
  and [cycle factors, sections 1--4](https://github.com/GettysburgResearch/collatz/blob/be783656f0e889fe0d5318a2f7a9140099cb94b5/research/astra-phase-and-cycle-20261124/CYCLE_FACTORS.md).
- PR193, `52beff703fd3ce798c430e5af8199eb58d41bf93`,
  [translated packing, sections 1--3](https://github.com/GettysburgResearch/collatz/blob/52beff703fd3ce798c430e5af8199eb58d41bf93/research/astra-universal-descent-20261124/escape.md),
  [full reduced denominator C5](https://github.com/GettysburgResearch/collatz/blob/52beff703fd3ce798c430e5af8199eb58d41bf93/research/astra-universal-descent-20261124/cycles.md),
  and [guarded ordinary partner](https://github.com/GettysburgResearch/collatz/blob/52beff703fd3ce798c430e5af8199eb58d41bf93/research/astra-universal-descent-20261124/ShadowCore.lean).
- This packet's original mathematical files at PR194,
  `764f3a9f539febf3d2661a9ca4acc1b10827878c`.

The root read the displayed source proofs and reconstructed the deductions
below. Separate agent reviews cover
[phase and synchronization](../../reports/astra-independent-review-20261124/LATEST_ESCAPE_REVIEW.md),
[cycle arithmetic](../../reports/astra-independent-review-20261124/LATEST_CYCLE_REVIEW.md),
and [formal statements and reported receipts](../../reports/astra-independent-review-20261124/LATEST_FORMAL_REVIEW.md).
The latter is a source/receipt review, not an independent replay of PR192--193.

## LS1. Stronger separation of colliding ordinary points

Let `q_0,q_1,...` be one injective positive odd orbit, put `n=M+1`, and let
`pi_M` be the uniform law on its first n points. For `1 <= m <= M` set
`Q=3^m`. Let B be the actual length-m canonical block at a uniformly selected
start in `0,...,M-m`. Write `H(B)` for its entropy in natural units and

```
d = 0.285859533495646...,
W = exp(-H(B)) Q^(-d).
```

The finite-window conclusion in [RUN_PARTITION](RUN_PARTITION.md) gives
`Col_Q(pi_M) >= c_q W`, with a positive constant depending only on the fixed
source. This is the empirical law of the displayed ordinary points.

Let X,Y be independent with law `pi_M`, and condition on the event E that
`X != Y` and `Q divides X-Y`. If `c_q W >= 2/n`, this event has positive
probability, since the diagonal mass is exactly `1/n`. Define

```
H_Q = 1 / E[1/|X-Y| | E].
```

PR193, `escape.md` (4)--(6), applies to this same empirical law and gives

```
Pr(E) / H_Q <= C log(2Q)/(nQ).
```

The actual orbit is an admissible set for that theorem: a merger at a common
odd clock would make two positions of the orbit equal. Since
`Pr(E) >= c_q W - 1/n >= c_q W/2`, it follows that

```
H_Q/n >= c'_q exp(-H(B)) Q^(1-d) / log(2Q).                 (LS1)
```

There is also a conditional separation quantile. At fixed Y, the number of
distinct positive sources at distance at most R, congruent to Y modulo Q,
is at most `2R/Q`. Every empirical atom has mass `1/n`, hence

```
Pr(0 < |X-Y| <= R | E) <= 2R/(nQ Pr(E)).
```

Taking `R=c_q n W Q/8` shows that at least half the distinct colliding pairs
have separation greater than R. Thus their conditional median scale is at
least a positive source-dependent multiple of
`n exp(-H(B)) Q^(1-d)`.

In a fixed rational actual phase, the canonical word is eventually periodic,
so `H(B)` is bounded uniformly in m and M. The power in these necessary
separation bounds is then

```
1-d = 0.714140466504354... .
```

This combines a stronger lower collision bound with the existing
inverse-distance estimate. It proves no opposing upper estimate for `H_Q/n`.
The statement requires the displayed diagonal threshold; it is not a bound
at every m for a fixed finite sample. The source-qualified extension to
PR185's harmonic inverse laws, and the separate nonuniform stationary gain,
are stated with their additional inputs in the escape review.

One cannot replace PR193's translated-interval exponent by 0.68 using
[OCCUPATION](OCCUPATION.md): that proof uses the absolute source height to
bound its endpoint carry. An interval's length does not replace its height.

## LS2. A full-denominator bound despite complete top-factor cancellation

Take the explicit mixed-prime family from [TOP_COMPONENT](TOP_COMPONENT.md).
Let r<s be distinct primes dividing g. The shortcut word has `A=5g`, `p=3g`.
In block j, `0 <= j < g`, its three odd positions are

```
5j + 1_{j == 1 mod (g/r)},
5j + 2 + 1_{j == 1 mod (g/s)},
5j + 4.
```

The original proof gives a primitive, positive rational cycle and complete
polynomial absorption of its top component. Let d now mean its **full reduced
numerical denominator**, not the entropy coefficient from LS1. Then

```
d >= 2^(5(g/s-1))/21.                                      (LS2)
```

Here is an elementary proof that keeps all numerical cancellation. There are
s equally spaced marked blocks in the s-grid, each separated from the next
by `g/s-1` interior blocks. The r-grid has r marks. Its intersection with the
s-grid consists only of block 1, because the lcm of `g/r` and `g/s` is g.
Therefore only r-1 of its marks lie in those interiors. Since r-1<s, at least
one entire interior interval has no mark from either grid. It supplies
`L=g/s-1 >= 1` consecutive copies of the baseline word `10101`.

Each five-step block maps x to `(27x+C)/32`, with
`C in {37,46,49,58}`. Every boundary of the positive cyclic realization
satisfies `37/5 < x <= 58/5`: the affine cyclic weighted average lies in the
closed interval, and at least one C is strictly greater than 37, so equality
at the lower endpoint would propagate around the cycle and is impossible.

The baseline word has literal positive rational cycle
`37/5 -> 58/5 -> 29/5 -> 46/5 -> 23/5 -> 37/5`.
All states of our mixed-grid cycle have the same reduced odd denominator d,
coprime to 3. This follows either from the exact cycle denominator
`2^(5g)-3^(3g)`, or by observing that both 2 and 3 are units at each prime
dividing d and that each shortcut step preserves a negative valuation.

At the beginning x of the baseline run and its endpoint x', the common
`5L`-bit word gives

```
2^(5L) (x' - 37/5) = 3^(3L) (x - 37/5).
```

After multiplication by 5d, both parenthesized quantities become integers.
Coprimality of 2 and 3 therefore implies
`2^(5L) divides 5d x - 37d`. This integer is strictly positive and at most
21d by the boundary interval. This proves (LS2).

The bound grows exponentially in g/s, in particular exponentially in g when
the two chosen primes are fixed. It does not give an exponential bound in g
uniformly over arbitrary choices of r and s. These remain nonintegral
rational cycles. The conclusion shows how complete top-component absorption
can coexist with a large actual denominator; it does not address every word.

## LS3. A concrete bounded-height target for a least nonconverger

Use the positive-input shortcut map
`T(x)=x/2` for even x and `T(x)=(3x+1)/2` for odd x. Suppose n is the least
positive integer that never reaches 1. Then n is odd. Every positive integer
below n reaches 1 by minimality.

PR193's `ShadowCore.guarded_certificate` supplies an explicit smaller ordinary
partner for `r=3^h u` when

```
u > 0, r odd, 3^(h+4) divides 1+2*4^h*u.
```

At `h=0`, the odd guard is exactly `r == 121 mod 162`, and the supplied partner
is

```
m = (64r-49)/81 > 0,       T^7(m) = T(r).
```

If r is any point on the forward orbit of n, this m must also fail to reach
1: otherwise its common endpoint with r would converge. To justify the last
step even when m hits 1 before time seven, use the actual cycle `1 <-> 2`;
every later iterate still reaches 1. Hence minimality gives m>=n. Every
guarded odd visit on this orbit must therefore obey

```
64r >= 81n+49.                                             (LS3)
```

Consequently, finding a guarded visit with `64r < 81n+49` would contradict
minimality. At r=n this already excludes the guarded residue class.
The inequality tracks the original n: merely proving m<r at a later,
much larger r does not suffice.

After an odd forward step the output is a ternary unit; dividing by powers
of two preserves that property. Thus the h>0 certificates cannot be assumed
to recur along an odd tail. No argument here forces a visit to the guarded
class in the required height range. The quantified missing step is explicit.

## What the newest results do and do not change

PR192 proves that **every finite canonical word has a convergent ordinary
witness**, with exactly two more odd steps after the prescribed prefix.
This is a changing-source assertion. It supplies neither an ordinary source
for an arbitrary infinite word nor a bound on the canonical complexity of
one hypothetical escaping orbit. The root reconstructed the terminal residue
permutation and the carry calculation in PS5.

PR192's prime-power survival theorem independently overlaps ABR-5; its broader
component irreducibility criterion is credited there. Its surviving
polynomial degree bound and norm-saturation examples preserve the distinction
between polynomial cancellation and the full integer evaluation. PR193 C5
does bound the full reduced denominator, conditional on a favorable factor
complexity scale. Both routes leave arbitrary high-complexity words open.

PR193's interval synchronization theorem provides many smaller partners in
every interval, with a common clock independent of its height. It leaves the
least member of each fiber. A hypothetical least nonconverger may remain one
of those minima. LS1 quantifies a necessary separation and LS3 specifies one
concrete successful visit, but neither forces the missing event.

These deductions sharpen the remaining arithmetic obligations. None proves
universal convergence or excludes all nontrivial positive cycles.
