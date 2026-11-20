# A uniform product budget before the first repetition

**PROPOSED integration of source-qualified orbit bounds. Full Collatz
closure remains OPEN.** This note removes the linear observation horizon
from a sufficient coefficient test on a simple ordinary orbit prefix,
at the cost of an explicit large threshold. It does not prove that every
ordinary source passes the test, nor exclude a nontrivial positive cycle.

The two dependencies are read at PR146 head
`fd991063721e9c157d318e40bb20131762f7d750`:

- `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, Sections 1 and 3,
  for the explicit counting argument and constants;
- `research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`, for the directed
  reduction at height `X/176106` and the finite list of smaller
  adjacent implications.

The coefficient product bound for an infinite distinct orbit already
appears in the first source. The extra argument below extends its same
explicit constant to every finite simple prefix; the subsequent
least-failure application is the integration made here.

## SPS1. Finite simple odd segments have the same explicit bound

Let `U(x)=(3x+1)/2^v2(3x+1)` on positive odd integers. Suppose

\[
u_0,u_1,\ldots,u_{L-1},\qquad u_{j+1}=U(u_j),
\]

is a finite segment with pairwise distinct entries. Put
`S={u_0,...,u_(L-1)}`. For every real `Z>=1`,

\[
\boxed{\#(S\cap[1,Z])\le4Z^{39/40}.}                 \tag{S1}
\]

Here no assumption is made about the continuation after the segment.
In particular, that continuation is allowed to enter a cycle.

For completeness, the small change to the source proof is given
explicitly. Put

\[
q=\left\lfloor\frac35\log_2 Z\right\rfloor,
\qquad m=\lfloor5q/3\rfloor,
\qquad \eta^3=3125/3456.
\]

When `q=0`, the integer count is at most `Z<4Z^(39/40)`.
For `q>=1`, remove the last `min(q,L)` positions. On the remaining
positions `U^q` is injective, since the shifted positions still lie
inside the given simple segment. The two-lane calculation in the
source therefore applies to those positions and gives

\[
\#(S\cap[1,Z])
\le 2Z\eta^q+\frac12(3/2)^q+q.                        \tag{S2}
\]

It uses the exact valuation cylinders, not independent sampling of
successive valuations. The elementary integer inequality
`8*3125^24 < 3456^24` implies `eta<2^(-1/24)`, while
`eta>2/3`. Since `q=floor((3/5)log_2 Z)`,

\[
2Z\eta^q<3Z^{39/40},\qquad
\tfrac12(3/2)^q\le\tfrac12Z^{3/5}
\le\tfrac12Z^{39/40}.
\]

For an integer `q>=1`, `q<=2^(q-1)`. Also
`Z^(39/40)>=2^(13q/8)>=2^q`. Thus the extra removed positions satisfy

\[
q\le\tfrac12Z^{39/40}.
\]

These three estimates prove S1 with the source's unchanged constant 4.

If every entry of the segment is at least a real `F>=1`, nonnegative
integration of the counting function yields

\[
\sum_{u\in S}\frac1u
=\int_F^\infty \#(S\cap[1,t])t^{-2}\,dt
\le160F^{-1/40}.                                      \tag{S3}
\]

For a finite set the integral identity is immediate term by term;
there is no limit interchange involving signed quantities.

## SPS2. Product control at every clock of a simple prefix

Use the shortcut map `T(x)=x/2` on even inputs and `(3x+1)/2` on odd
inputs. Let `n_j=T^j(n)`, and let `b_i` count odd inputs at times `j<i`.
Then exactly

\[
n_i=n\frac{3^{b_i}}{2^i}
       \prod_{\substack{0\le j<i\\n_j\text{ odd}}}
       \left(1+\frac1{3n_j}\right).                    \tag{S4}
\]

Suppose `n_0,...,n_(i-1)` are pairwise distinct and all at least `F`.
The odd inputs form a finite simple `U`-segment. Applying S3 and
`log(1+t)<=t` to S4 gives

\[
1\le P_i:=
\prod_{\substack{0\le j<i\\n_j\text{ odd}}}
       \left(1+\frac1{3n_j}\right)
\le\exp\left(\frac{160}{3}F^{-1/40}\right).           \tag{S5}
\]

This is uniform in the length `i` of the simple prefix. If

\[
F\ge80^{40},
\]

then `P_i<=exp(2/3)<2`. The final strict inequality follows, for
example, from strict Jensen convexity of `1/t` on `[1,2]`, which gives
`log 2=integral_1^2 dt/t > 2/3`.

The bound concerns times up to the first repetition. It must not be
applied repeatedly around a cycle: the product then includes repeated
values, whereas S3 counts each value once.

## SPS3. An unbounded-horizon sufficient least-failure test

Retain the source notation

\[
X=128k+1,\qquad Y=64k+1,\qquad n=27k+1=T^6(Y),
\qquad k>0,\quad4\nmid k.
\]

Set the real floor

\[
F=\frac{5X}{8\cdot176106}.                             \tag{S6}
\]

Suppose `F>=80^40`. Follow the actual ordinary orbit from `n`, stopping
when a value repeats. If at any clock `i` before the input prefix has
repeated,

\[
\frac{3^{b_i}}{2^i}<2^{-17},                           \tag{S7}
\]

then some state `n_j`, `0<=j<=i`, is strictly below `F`.

Indeed, otherwise every state through `i` is at least `F` and S5 applies.
Equations S4 and S7 give

\[
n_i<\frac{n}{65536}<\frac{5X}{8\cdot176106}=F,          \tag{S8}
\]

a contradiction. The middle inequality is exact for every `k>0`:

\[
8\cdot176106(27k+1)<5\cdot65536(128k+1).
\]

The right side minus the left side is `3904144k-1081168`, which is
at least `2822976>0` for every integer `k>=1`.

Take the first actual state `m=n_j<F`. The source-qualified directed
reduction supplies a finite list of smaller eligible implications with
upper antecedents below

\[
176106m<\tfrac58X.
\]

Their joint validity proves `Y` convergent. Consequently a globally least
failed adjacent comparison cannot have such a crossing before its first
repetition, once S6 meets the stated threshold.

The criterion has no prescribed time horizon. It is a sufficient
semidecision procedure, not a total successful selector. Observing S7
does not require it to be the first coefficient crossing; simplicity of
the preceding input prefix and the uniform product budget are what pay
for the affine correction. The finite-source certificate obtained after
finding `m` still has `O(log(2k))` smaller antecedents, but the time spent
finding it has no proved universal bound.

## The remaining closure step

For an infinite distinct orbit, the same existing source proves that
`3^(b_i)/2^i` tends to infinity. This condition is fully compatible with
never satisfying S7. A nontrivial periodic orbit is also not excluded:
after its first repetition, the product bound S5 is unavailable over
multiple periods. Thus neither infinite divergent orbits nor nontrivial
cycles have been eliminated by this test.

The useful gain is that the additive `O(i)` remainder and its resulting
linear horizon were artifacts of a local bound. Uniform orbit sparsity
pays the entire correction product on every simple prefix. What remains
is an ordinary-source theorem forcing a sufficiently low coefficient
excursion, or an independent argument excluding the sources whose
coefficients never make that excursion and the possible cycles.
Independent binary ballot counts beyond their natural modulus range do
not establish that assertion. GRH alone supplies no such implication.

## Exact finite evidence

`check_simple_prefix_product_sieve.py` validates 129 finite simple odd
segments at their 2,459 attained size thresholds, checks S1 and S3 by
exact integer or rational inequalities, and rejects five malformed
controls. It also replays four large ordinary sources satisfying S6,
checks the exact product identity at every observed clock, and finds
the actual earlier state below the floor. All four correction products
are also directly below two.

Three examples are fixed members of the source's rank-five family
`e=119+162j`, with `k=(8*2^e-22)/243`:

| Exponent e | First floor hit | First crossing of `2^(-17)` | Odd inputs at crossing |
| --- | ---: | ---: | ---: |
| 281 | 1360 | 1362 | 848 |
| 443 | 1715 | 1731 | 1081 |
| 605 | 2411 | 2425 | 1519 |

The other example has `n=2^270`. Both normal and Python `-OO` executions
produce the same report. These executions support the local arithmetic
and normalization; the unbounded claims rest on the proof above. The
71-path reduction is an imported dependency, and neither convergence of
the entire Mersenne progression nor its eventual crossing is inferred
from the three rows.
