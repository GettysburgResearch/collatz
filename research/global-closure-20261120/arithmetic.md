# Exact legal blocks and the failure of a simple recharge budget

**Status: PROPOSED, elementary written proofs with bounded exact replay.**
This note does not prove Collatz or construct an infinite escaping orbit.
It tests whether prime-height dispersion, growing binary complexity, and
translated-interval sparsity contradict each other once the exact `3n+1`
arithmetic is retained. They coexist on arbitrarily long **actual ordinary
Collatz segments**. A second result shows that a single fixed-valuation
step can replenish the entire clock of consecutive increasing steps.

The sources are frozen in section 8. The construction and its proof below
are self-contained; no prime number theorem, S-unit bound, probabilistic
assumption, or independence assertion is imported.

## 1. Domain and the precise quantifier boundary

Use the positive odd map

\[
 U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1).
\]

Let `b(n)` be binary bitlength, `r(n)` the number of maximal binary
one-runs, and `s_2(n)` binary popcount. Each segment below has one fixed
positive ordinary source and all of its edges are literal applications
of `U`. The source **depends on the requested finite length**. The result
does not interchange

\[
 \forall N\ \exists n_0\quad\hbox{and}\quad
 \exists n_0\ \forall N.                              \tag{1}
\]

For a finite prime set `S`, put

\[
 [n]_S=\prod_{p\in S}p^{v_p(n)},\quad
 x_i=\log_2 n_i,\quad y_i(S)=\log_2[n_i]_S,
 \quad W_m=\sum_{i<m}x_i,\quad Y_m(S)=\sum_{i<m}y_i(S).
\]

One set `S` is shared by the whole segment. It may be chosen after all
states have been observed. Every assertion for `|S|<=s` is uniform over
the primes chosen; choosing a different set separately at each state is
not permitted.

## 2. GA-001: the exact valuation-one clock

For an odd positive integer define

\[
 B(n)=v_2(n+1)-1\ge0.
\]

If `B(n)=b`, write `n=2^(b+1)u-1` with `u` positive odd. Then

\[
 U^j(n)=3^j2^{b+1-j}u-1\qquad(0\le j\le b),          \tag{2}
\]

the first `b` odd valuations are exactly one, and the valuation at the
last displayed state is at least two. In particular, `B(n)` is the
**exact** number of initial valuation-one edges, not just an upper bound.

Indeed, while `j<b`, dividing `3U^j(n)+1` by two leaves an odd integer.
At `j=b`, the displayed state is `1 mod 4`. Equivalently,

\[
 a(n)=1\iff B(n)>0,\qquad
 a(n)=1\Longrightarrow B(U(n))=B(n)-1.                \tag{3}
\]

For every actual finite odd orbit segment `n_0,...,n_t`, this gives the
exact accounting identity

\[
 \#\{j<t:a(n_j)=1\}
 =B(n_0)-B(n_t)+
   \sum_{\substack{j<t\\a(n_j)\ge2}}B(n_{j+1}).       \tag{4}
\]

An all-time valuation-one path would require a positive ordinary `n+1`
divisible by every power of two, which is impossible. This observation
does not bound the recharge sum in (4).

## 3. GA-002: simultaneous binary complexity with an odd multiplier

Fix `m>=2`, any positive odd `Q`, and a positive multiple `L` of 16
satisfying

\[
 4m(16/27)^{L/4}<1.                                  \tag{5}
\]

There exists an odd integer `v` of bitlength exactly `L` such that all
the even residues

\[
 t_i=(3^iQv-1)\bmod 2^L,\qquad 0\le i<m,
\]

have at least `L/8` one-runs. The fraction of excluded odd `L`-bit choices
is at most `4m(16/27)^(L/4)`. This is a deterministic counting statement;
the least acceptable `v` can be found by a finite exhaustive search.

**Proof.** Among length-`L` binary strings ending in zero, with leading
zeros allowed, the number with exactly `r` one-runs is

\[
 \binom L{2r}.                                       \tag{6}
\]

Choose the two boundaries of each one-run among the `L` available
boundaries, including the one before the first bit. Thus the number of
bad even residues is at most

\[
 \begin{split}
 D_L&=\sum_{r=0}^{L/8-1}\binom L{2r}
       \le\sum_{k=0}^{L/4}\binom Lk\\
    &\le3^{L/4}(1+1/3)^L
       =4^L/3^{3L/4}.                                \tag{7}
 \end{split}
\]

Multiplication by `3^i Q` permutes the odd residues modulo `2^L`, and
subtracting one then bijects them with the even residues. At most `D_L`
odd residues are bad for each `i`. There are `2^(L-2)` odd integers of
bitlength exactly `L`, so (5) makes the union of all bad choices strictly
smaller than this source set. No independence between the conditions is
used. Both `L=16m` and `L=16m^2` satisfy (5):

\[
 (27/16)^4>(3/2)^4>4,\qquad 4^m\ge4m.                \tag{8}
\]

## 4. GA-003: a legal joint-constraint block with linear source height

For every `N>=1`, set `m=N+1`, `L=16m`, `Q=1`, and choose `v` by
GA-002. Define

\[
 n_i=3^i2^{m-i}v-1\qquad(0\le i<m).                 \tag{9}
\]

These are `m` distinct positive odd states with the following properties.

1. The `N=m-1` displayed edges are exact `U` edges with valuation one.
   They satisfy `n_(i+1)>(3/2)n_i`, so none descends below the source.
   The next odd valuation, at `n_(m-1)`, is at least two.
2. Every displayed state satisfies
   \[
    r(n_i)\ge2m+1> b(n_i)/10,\qquad b(n_i)\le18m-1.   \tag{10}
   \]
   Consequently every popcount is also greater than one tenth of its
   bitlength. The initial bitlength is exactly `17m`.
3. For every `|S|<=s`, both
   \[
    \frac{Y_m(S)}{W_m},\quad
    \frac1m\sum_{i<m}\frac{y_i(S)}{x_i}
    \ \le\ \min\left\{1,
       \frac{19s}{16}\bigl(m^{-1/2}+m^{-1}\bigr)\right\}.
                                                               \tag{11}
   \]
4. Every real interval of width `X>=0`, wherever placed, contains at most
   \[
    1+\log_{3/2}(X+1)                                \tag{12}
   \]
   displayed states. As an integer count it is at most the floor of
   this expression.

**Legality, height, and complexity.** Formula (9) is (2) with `b=N`.
Since `v` is odd,

\[
 n_i=(3^iv-1)2^{m-i}+(2^{m-i}-1).
\]

The first coefficient is even. The final nonempty run of ones therefore
has a zero separating it from the upper block, and

\[
 r(n_i)=r(3^iv-1)+1\ge r(t_i)+1\ge L/8+1.            \tag{13}
\]

The binary suffix cannot have more runs than the complete nonnegative
integer. Also `v<2^L` and `3^i<2^(2i)` for `i>0` give the height bound
in (10), with the `i=0` case immediate. The smallest odd `L`-bit `v` is
`2^(L-1)+1`, so `2^(L+m-1)<n_0<2^(L+m)` and `b(n_0)=17m`.
For the estimates below it suffices to use

\[
 h:=\min_i x_i\ge17m-2,\qquad
 M:=\max_i x_i<18m-1.                                \tag{14}
\]

**Prime-height bound.** If `i<j`, `d=j-i`, the exact affine relation is

\[
 2^d n_j=3^d n_i+(3^d-2^d),\qquad
 \gcd(n_i,n_j)\mid 3^d-2^d.                          \tag{15}
\]

This retains the full `+1` correction. In a consecutive block of `t`
states, select, for each `p in S`, a state of largest `p`-valuation. Its
`p`-height is at most `M`; the `p`-height of every other state is at most
`|j-i| log_2 3`. The largest possible sum of these distances is
`t(t-1)/2`, attained at an endpoint. Hence, for `t<=r`, the block's
total `S`-height is at most `s(M+rt)`.

Partition all `m` states into blocks of length at most
`r=ceil(sqrt(m))`. Summing gives

\[
 Y_m(S)\le s\bigl(\lceil m/r\rceil M+rm\bigr).        \tag{16}
\]

Both quantities on the left of (11) are at most `Y_m(S)/(mh)`. For
`m>=2`, (14) gives `M/h<=9/8` and `h>=16m`. Therefore that ratio is at
most

\[
 s\left[\frac98\left(\frac1r+\frac1m\right)
              +\frac r{16m}\right]
 \le\frac{19s}{16}\bigl(m^{-1/2}+m^{-1}\bigr),         \tag{17}
\]

as asserted. In particular the moving set of `s` most useful primes
cannot retain a positive fraction of height along this family of finite
blocks, for fixed `s` as `m` increases.

**Intervals.** If `k` displayed states lie in an interval of width `X`,
their first and last differ by at least `(3/2)^(k-1)-1`. This follows
from the strict geometric growth and the fact that the first state is
at least one. It proves (12), including `k=1` and `X=0`.

## 5. GA-004: pairwise coprime legal blocks avoiding all small primes

One can strengthen the prime interface without abandoning exact legality.
Set

\[
 Q_m=\prod_{d=1}^{m-1}(3^d-2^d)
             \prod_{k=1}^{m}(2k-1),\qquad L=16m^2.    \tag{18}
\]

Choose an odd `L`-bit `v` using GA-002 with this `Q_m`, and put

\[
 n_i=3^i2^{m-i}Q_mv-1\qquad(0\le i<m).               \tag{19}
\]

All `m-1` edges remain literal valuation-one edges. Every displayed
state has all of the following properties:

\[
 \begin{gathered}
  \gcd(n_i,n_j)=1\quad(i\ne j),\qquad
  p\mid n_i\Longrightarrow p>2m-1,\\
  r(n_i)\ge2m^2+1>b(n_i)/10,\qquad
  b(n_i)\le18m^2+m-1.                               \tag{20}
 \end{gathered}
\]

The translated-interval bound (12) still holds. Moreover, for every
`|S|<=s`,

\[
 \begin{split}
  \frac{Y_m(S)}{W_m}
     &\le \min\left\{1,\frac{s}{m}
                    \left(1+\frac1{16m}\right)\right\},\\
  \frac1m\sum_{i<m}\frac{y_i(S)}{x_i}
     &\le\min\{1,s/m\},\\
  \#\{i<m:[n_i]_S\ge n_i^\epsilon\}
     &\le\min\{m,s\}\qquad(\epsilon>0).              \tag{21}
 \end{split}
\]

**Proof.** Relation (15) still holds. Any prime dividing a gcd there
would divide `Q_m`, whereas every `n_i` is `-1 mod Q_m`. This is a
contradiction. The second product in (18) excludes every odd prime at
most `2m-1`; the states are odd, so two is excluded as well.

For `m>=2`, `2m<=2^m` and

\[
 Q_m<2^{m(m-1)}(2m)^m\le2^{2m^2-m}.                  \tag{22}
\]

The same separated binary expansion as in (13) proves the run bound.
The inequalities `v<2^L` and `3^i<=2^(2i)` give
`n_i<2^(L+2m^2+i)`, proving the bitlength bound in (20).

Each prime can divide at most one displayed state. Thus `Y_m(S)<=sM`,
and at most `s` states have positive `S`-height. Every edge increases
logarithmic height by less than one, so

\[
 M<x_0+(m-1),\qquad W_m\ge mx_0,\qquad
 x_0\ge16m^2+m-2.
\]

Consequently `M/x_0<1+1/(16m)`. These observations prove all of (21).
No factorization of the constructed states is assumed or required.

## 6. GA-005: a fixed-valuation step can recharge arbitrarily much

For every `m>=1` and positive odd `u`, define

\[
 z=2^{m+3}u-3,\qquad x=3\cdot2^m u-1.
\]

Then

\[
 3z+1=8x,\quad a(z)=3,\quad U(z)=x,\quad
 B(z)=0,\quad B(x)=m-1,\quad 1<z/x<4.                \tag{23}
\]

Thus a single valuation-three step replenishes `m-1` consecutive
valuation-one edges, while its decrease in logarithmic height is less
than two. Neither the valuation cost nor that height decrease bounds
the recharge by any universal constant multiple.

There is a sharper obstruction to a simple additive resource. With
`u=1`, both states have exactly two binary one-runs, and

\[
 s_2(z)=m+2,\qquad s_2(x)=m+1.                        \tag{24}
\]

For any fixed real coefficients `lambda>0`, `mu`, `nu`, and `kappa`, the
potential

\[
 V(n)=\lambda B(n)+\mu r(n)+\nu s_2(n)+\kappa\log_2 n
\]

increases on some such legal edge. Indeed,

\[
 V(x)-V(z)=\lambda(m-1)-\nu+\kappa\log_2(x/z)
 \ge\lambda(m-1)-|\nu|-2|\kappa|\longrightarrow+\infty.
                                                               \tag{25}
\]

This refutes only this specified class of additive potentials. It does
not rule out a potential with different variables, nonlinear terms,
multiple-step amortization, or a different treatment of the recharge.
The total prime-factor height `sum_p v_p(n) log_2 p` equals `log_2 n`
and therefore adds no separate resource to this particular class.

## 7. What the global attempt leaves open

The prime-height source proves necessary dispersion; the binary sources
prove necessary growing complexity; the interval source proves necessary
spatial sparsity. GA-003 and GA-004 show that all three phenomena coexist
on arbitrarily long exact Collatz segments. GA-003 already does so with
initial bitlength `17(N+1)`. GA-004 even makes the entire segment pairwise
coprime. These results strengthen a generic comparison-sequence example
by retaining every local Collatz cocycle and valuation condition.

They do **not** show that these constraints are useless in a global proof.
A theorem using the fixed initial source, restrictions on subsequent
recharges, or complete cycle closure can still distinguish a hypothetical
infinite orbit from this family. In particular, every constructed block
has exactly its stated finite valuation-one lifetime, after which the
next valuation is at least two. No outcome after that point is claimed.

The attempted accounting proof stops at the recharge sum in (4). To get
global descent from that account, one would need a bound on accumulated
recharges for one fixed ordinary source, strong enough to offset the
coefficient growth of the intervening blocks. Equation (23) rules out
charging each recharge by a fixed multiple of that individual reset
step's valuation or logarithmic decrease. Neither the prime-height nor
the binary occupancy estimates supplied such an accumulated bound.
Complete cycle denominators are also untouched. **Both global
convergence and exclusion of arbitrary nontrivial cycles remain OPEN.**

## 8. Frozen source comparisons and replay scope

| Source | Frozen head and exact claim boundary |
| --- | --- |
| PR #154 | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0`, `research/structural-reset-20261120/adelic/PRIME_HEIGHT_ESCAPE.md`, ADEL-001--ADEL-006; `CLOSING_ATTEMPT.md`, sections 1--6. These motivated the prime-height comparison; (15)--(17) are proved here for the constructed segments. |
| PR #150 | `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`, `research/pointwise-closure-20261120/GROWING_COMPLEXITY.md`, displayed finite inequality (1) and growing-threshold theorem; `SPARSE_RETURN_SPECTRUM.md`, SR-1 and the distinct-segment occupancy consequence. Their theorems are not needed to prove GA-001--GA-005. |
| PR #153 | `eb04a5d79020cefa0ba46794095b5766c5ff66a4`, `research/fixed-integer-descent/arithmetic.md`, RC-1--RC-5; `drift.md`, FID-DRIFT-001--FID-DRIFT-005. This note changes neither the six-run guard nor its replay. |

The standalone checker is
[`global_closure_arithmetic.py`](../../experiments/global_closure_arithmetic.py).
It checks the exact residue-count formula on a bounded complete domain,
constructs deterministic ordinary sources in both regimes, replays all
displayed edges, checks run counts and bitlength bounds, checks every
pairwise gcd, and checks the fixed-valuation recharge family. It does
not factor the large states or enumerate every prime set; the uniform
prime-set quantifier is justified by the written proofs. The saved
[`arithmetic-report.json`](../../reports/2026-11-20-global-closure/arithmetic-report.json)
records the actual coverage and reproducible source hashes.

```sh
python -X utf8 -B experiments/global_closure_arithmetic.py --compare reports/2026-11-20-global-closure/arithmetic-report.json
```

The replay is finite implementation evidence, not a formal proof checker,
an external mathematical review, or evidence of an infinite counterexample.
