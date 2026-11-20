# Blocker in the attempted finite three-ray defect strengthening

**OPEN; unsuccessful exploratory route, not a theorem of closure.**

For ordinary shortcut orbits let f(n) be the eventual-merger component, and
consider the hypothesis that only finitely many **odd** x satisfy
`f(3x)!=f(x)`. The attempted strengthening was to derive full Collatz from
this hypothesis alone, without a separate bound on five-ray failures.

The frozen source is PR #146,
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`,
`research/upper-bit-mergers/THREE_RAY.md`. Its actual proof assumes a finite
lower limit for the five-ray failure count divided by log X; this first
implies finite odd three-ray defects, then supplies additional information.

Finite odd three-ray defects do let one define the stabilized component

`F(x)=lim_(j->infinity) f(3^j x)`.

The limit here means an eventually constant label. It obeys
`F(2x)=F(3x)=F(x)`. Also f and F differ on only finitely many odd parts:
a discrepancy at x requires a three-ray defect at some `3^j x`, so the
odd part of x is a power-of-three divisor of one of finitely many defective
odd inputs. The source's same synchronization argument then identifies
`f(x)=F(x)` for every x prime to three.

The unrepaired step is **`F(5x)=F(x)` for every x**. The published source
obtains this by producing quadratically many logarithmic five-ray failures
from a counterexample to that identity, contradicting its stronger
five-ray counting assumption. Finite odd three-ray defects alone do not
provide that counting contradiction.

The source's final elimination of a largest exceptional odd part uses
the multiplicative-five identity in the comparisons involving `10h+1`
and `16h+1`. Reusing that elimination without this input would leave a
gap. I did not derive the missing identity by another method and did not
construct a countermodel proving it impossible. This exploration therefore
does not establish the proposed finite-defect strengthening.
