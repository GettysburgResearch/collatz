# Independent reconstruction of the terminal phase obstruction

**Internal review verdict: VERIFIED at the stated scope.** This is an
independent algebraic reconstruction by the arithmetic-route agent, not
external referee acceptance or formal verification.

Reviewed file:
`research/global-forcing-20261121/energy/TERMINAL_PHASE.md`

SHA-256:
`a6244f942da0f2b597fa3d204300dc300fec1200f13004e43b68438c5ebd0280`

The verdict covers TP1, TP2, the reconstructed prefix, and the certified
one-seed example. It does not approve neighboring energy claims or later
versions. The author made one suggested prose correction before this
pin: “unequal total path lengths” now distinguishes actual path length
from the signed slope exponent `k`, which proportional transport forces
to agree between arms. No mathematical repair was necessary.

## 1. The grade remains valid through visits to one

Write `H(n)=tau(n)-2r(n)` for a convergent ordinary input. Each whole
`1 -> 2 -> 1` turn has grade zero, so arbitrary terminal padding preserves
`H`. More explicitly `H(1)=0,H(2)=1`; the single edge `1 -> 2` has
grade minus one and `2 -> 1` has grade one. These are precisely the
same edge grades as before the first hit.

For a forward edge the slope and grade are

| Edge | Slope | `H(start)-H(end)` |
|---|---:|---:|
| even forward | `1/2` | `1` |
| odd forward | `3/2` | `-1` |
| even reverse | `2` | `-1` |
| odd reverse | `2/3` | `1` |

Consequently a finite path of actual ordinary edges in either direction,
with slope `3^j/2^k`, has grade `k-2j` for signed integers `j,k`. This
uses only legal positive integer edges. It does not extend `H` to
unknown nonconvergent inputs.

For two fixed native paths on an infinite arithmetic progression, let
their slopes on their own source coordinates be `alpha,beta`. If they
take `(x,5x)` to `(q(x),5q(x))`, the coefficients of `x` in the second
endpoint give `5 beta=5 alpha`. Unique factorization forces equality
of both signed exponents. Their grade contributions are equal; hence

`H(5x)-H(x)=H(5q)-H(q)`

whenever these grades are defined. The whole progression is used for
the affine slope identity; it need not consist entirely of convergent
pairs. At a particular input, a successful terminal construction makes
all states of the finite native paths convergent, and that is sufficient
to apply the grade identity there.

This also checks the adaptive quantifier. Each selected block preserves
the same integer at the actual supplied input, even if the dictionary
is infinite and block selection depends on the source or certificate.
A successful computation has finitely many stages, so induction over
that particular computation preserves the phase. No uniform bound on
its number of stages or clocks is needed.

## 2. Reconstructing the one-step source and long target prefix

For `a>=2`, let `x_a=(4^a-1)/3`. Then
`3x_a+1=4^a`, so its first-hit data are exactly `(tau,r)=(2a,1)`.
Also `x_a=a mod3`, proving the ternary-unit condition when `3` does
not divide `a`.

Put `m=a-1`. The first odd target edge has numerator
`3(5x_a)+1=4(5*4^m-1)` and exponent two. The resulting state is
`5*2^(2m)-1`. For `0<=j<=2m-1`, the run states are

`5*3^j*2^(2m-j)-1`.

For each nonfinal run edge the shifted value has at least two factors
of two, making the odd-step exponent exactly one. At the last displayed
state the next numerator is `2(5*9^m-1)`. Since `9^m=1 mod8`, its
valuation is exactly three. There are `1+(2m-1)+1=2a-1` odd edges,
and the endpoint is `(5*9^m-1)/4`.

Every displayed state, including that endpoint, exceeds one. Therefore
any eventual first-hit certificate for `5x_a` has at least `2a-1`
odd inputs. In fact one further odd input is needed, but the manuscript
only uses the weaker valid bound. The prefix is ordinary and legal for
every indicated `a`; eventual convergence of its endpoint is not used.

## 3. Exact product bound and the conditional-convergence quantifier

For any actual first-hit trajectory from `y`, multiplication of all
shortcut edges gives

\[
2^{H(y)}=y(3/4)^{r(y)}
\prod_{\text{odd inputs }n}\left(1+\frac1{3n}\right).
\]

All its odd inputs occur before the first hit and are at least three.
Hence each factor is at most `10/9`, and

`2^H(y) <= y(5/6)^r(y)`.

For `y=5x_a`, divide by `2^H(x_a)=2^(2a-2)`. The remaining initial
factor is exactly `(20/3)(1-4^(-a))<20/3`. The prefix lower bound
therefore proves the manuscript's strict inequality

\[
2^{\Delta(x_a)}<\frac{20}{3}(5/6)^{2a-1}
\]

**conditional only on convergence of that particular `5x_a`.** The
proof of incompleteness uses the conditional correctly: if a compiler
successfully reaches one of its certified terminal pairs, the actual
native paths establish target convergence, and the displayed inequality
can then be invoked. No all-parameter target-convergence assumption is
hidden in the argument.

The integer threshold is also correct. From `20/3<8` and
`6^4>2*5^4` one gets
`Delta(x_a)<(13-2a)/4`. For
`a>=max(2,7-2D)` this is strictly below `D`; infinitely many allowed
values remain after excluding multiples of three. Phase preservation
would instead give `Delta(x_a)>=D` from the terminal library. Thus
every proposed compiler of the stated architecture misses an input
with a complete one-odd-step source certificate.

This proof excludes an arbitrary terminal collection whose phases have
a common lower bound, and therefore every finite certified library.
It is stronger than a bounded-dictionary or bounded-clock search
failure, but it remains an architecture-specific obstruction.

## 4. The completely certified one-seed family

For `L=17+18k`, the integer `x=(5*2^L-7)/9` has `x=1 mod3` because
`2^L=14 mod27`, and `x=49 mod64`. Its two actual exponent words are
`(2,L-2)` to 5 and `(5,L-5)` from `5x` to 25. The latter follows from

`3(5x)+1=32*(25*2^(L-5)-1)/3`.

All parenthetical inverse quantities are positive odd integers. Both
arms use two odd inputs and `L` shortcut clocks. The independently
replayed first-hit data are

`(tau,r,H)(1)=(0,0,0)`,
`(tau,r,H)(5)=(4,1,2)`, and
`(tau,r,H)(25)=(16,7,2)`.

It follows that both large starts have grade `L-2`, so their phase is
zero. Terminal parameter one has phase two. A block-to-one compiler
cannot cover this known convergent family. As the manuscript says,
admitting terminal five bypasses this **particular** example; TP2 is
the separate argument showing that no finite enlargement is complete.

## 5. Scope, provenance, and actual finite checks

The general grade/affine invariant and a previous finite-seed
application were independently read in PR146 at
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/BASIN_PHASE.md`. The one-step family and
the 5/25 inverse-lift obstruction were read in PR157 at
`64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/closing-attempts.md`, GCL-001--002.
The author credits these sources accurately. The reviewed addition is
their specific composition into the proportional-five, finite-terminal
architecture, including reverse native edges.

An independent short integer/Fraction program authenticated the pinned
file, reproduced the three base grades above, and checked the exact
first-hit product and phase inequality for the 15 eligible values
`2<=a<=24`. Every one of those particular targets reached one during
the actual replay; their phases ranged from `-85` to `0`. This is
finite supplemental evidence. The all-parameter prefix, conditional
product inequality, and adaptive no-go theorem were reconstructed
algebraically above; no universal convergence is inferred from the
15 checks.

The following stronger conclusions are **not** supported:

* Exclusion of pointwise numerical certificates. Their endpoint
  coincidence may hold at a single source without the slope equality.
* Exclusion of nonproportional intermediate comparisons, arbitrary
  recursive programs, or a certified terminal class with phases
  unbounded below.
* Failure of an energy estimate restricted to hypothetical nonzero
  component defects. The completely certified examples already have
  zero component defect, and the stopping grade is not defined for an
  unproved nonconvergent target.
* Disproof of multiplication-by-five closure or of Collatz. The phase
  obstruction is compatible with both being true.
