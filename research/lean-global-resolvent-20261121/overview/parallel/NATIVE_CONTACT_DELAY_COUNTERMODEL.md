# A bounded canonical envelope need not have a uniform contact clock

**Status:** an explicit generic-kernel countermodel, proved below. This is
not a Collatz counterexample and does not contradict a statement using the
specific inverse letters `(2^e q-1)/3`. It separates qualitative obstacle
and predecessor-population conclusions from a uniform moving-root clock.
The contact threshold is exactly `C={V<=2}`.

## 1. A convergent ordinary graph

On positive integers use the auxiliary forward map

\[
S(1)=1,\qquad S(n)=\lfloor n/2\rfloor\quad(n\ge2).
\]

Every forward orbit reaches 1. Define a stochastic inverse kernel `K`:
for `n>=2`, choose `2n` and `2n+1` with probability `1/2` each;
at 1, choose 1 with probability `1/2`, and 2 or 3 with probability `1/4`
each. Every transition is an actual inverse edge of `S`. The only reverse
cycle is the root loop, with multiplier `1/2`.

This graph has the same form of uniform predecessor population lower
bound used in the obstacle program:

\[
\#\{x\in(X/4,X]:x\text{ reaches }a\}\ge X/(4a)
\quad(X\ge4a).
\tag{1}
\]

For `a>=2`, choose `k` with `2^k a<=X<2^(k+1)a`. The entire descendant
interval `[2^(k-1)a, 2^(k-1)(a+1)-1]` lies in `(X/4,X]` and has
`2^(k-1)>X/(4a)` elements. The case `a=1` is immediate.

## 2. Arbitrarily long, finite delayed blocks

For `k>=3`, put

\[
q_k=4^k+1,\qquad T_k=k^3.
\]

The binary words for the `q_k` are prefix-free: the terminating 1 of a
shorter word occurs where each longer word still has a 0. Thus their full
binary descendant subtrees are disjoint.

Within the subtree rooted at `q_k`, define the profile by inverse depth:

\[
V(n)=
\begin{cases}
3,&0\le d(n,q_k)<T_k,\\
2,&d(n,q_k)=T_k,\\
1,&d(n,q_k)>T_k.
\end{cases}
\]

Set `V=1` outside these subtrees. In particular `1<=V<=3` everywhere.
Each inverse path encounters at most one delayed block, and that block
has finite length. The extra layer with value 2 ensures that the
one-step row sum in the next construction never exceeds 2.

Define the positive transfer operator

\[
(Pf)(n)=V(n)\sum_xK(n,x)\frac{f(x)}{V(x)}.
\tag{2}
\]

It follows immediately that `PV=V`. The row sums `P1` are among
`2/3, 1, 3/2, 2`. All parent sums are finite.

## 3. This is the canonical least excessive majorant

The obstacle is the constant function `g=1`. Let `W>=1` satisfy `PW<=W`.
Then `W/V` is `K`-excessive. At a point with `V=1`, already `W>=V`.
At a point in a delayed block, there is one finite depth `d` such that
every inverse path has reached the constant-1 region at depth `d`.
Iterating excessivity gives

\[
\frac{W(n)}{V(n)}\ge
\mathbb E_n^K\frac{W(X_d)}{V(X_d)}\ge1.
\]

Hence `W>=V` everywhere. Consequently `V` is precisely the least
excessive majorant of 1; it is not an arbitrary inserted harmonic
profile. The canonical finite obstacle iterations reach `V(n)` after a
finite, root-dependent number of iterations at every point.

Its harmonicization is exactly `G=V`. For `D_j=P^j1`, conjugacy gives

\[
D_j(n)=V(n)\mathbb E_n^K[1/V(X_j)],\qquad
\frac{V(n)}3\le D_j(n)\le V(n)\le3.
\tag{3}
\]

Every inverse path eventually lies in the constant-1 region, so bounded
convergence yields `D_j(n)->V(n)` at every fixed root. The entire critical
Abel family also converges to `V`. In particular the model has a uniform
positive finite-density floor, the critical-limit comparisons, and the
bound `D_j<=(4j+2)(3/2)^j` (`j=0` is checked separately).

All inverse-ray cylinder masses tend to zero: the product of `P` weights,
multiplied by the terminal `V`, is the initial `V` times a `K`-cylinder
probability, at most `V(n)2^(-j)`. Fixed-basin sublinearity holds uniformly
even over all roots, since `V(n)/n<=3/n`. Component normalization holds:
the unique ordinary component has infimum 1. Operator covariance with
component labels holds as usual because transitions stay in that
component. Thus none of these qualitative properties is being dropped.

## 4. The native contact probability is nevertheless zero

Take exactly `C={n:V(n)<=2}`. The `V`-Doob inverse kernel obtained from
`P` is exactly `K`. From `q_k`, its first entrance time is deterministic:

\[
\tau_C=T_k=k^3.
\]

For the proposed native depth

\[
L(q)=\left\lfloor
\frac{\log q-3\log\log(q+2)}{\log(3/2)}
\right\rfloor,
\]

one has `L(q_k)=O(k)<k^3` for large `k`. Therefore, with the same strict
endpoint convention as the entrance identity,

\[
\boxed{p_{L(q_k)}(q_k)=\Pr_{q_k}^V(\tau_C<L(q_k))=0.}
\tag{4}
\]

The selected heights `q_k=4^k+1` are positive odd ternary units, one above
a power of two. Thus restricting the selected roots to such a band does
not repair a deduction based only on the generic properties listed above.
The model's obstacle is 1 on its whole state space; its map and weights
are explicitly different from Collatz's ternary-unit operator.

## 5. Consequence for the next attack

This example does not challenge the exact Collatz contact-probability
claim. It shows that a proof of that claim must use additional arithmetic
structure of the actual inverse letters or a quantitative trace estimate.
Minimality, harmonicity, atom removal, component normalization, uniformly
bounded finite densities, and linear ordinary predecessor populations
are insufficient on their own, even on a graph where every forward orbit
converges and the canonical envelope is already globally bounded.

It also shows that the proposed probability condition is stronger than
the height conclusion it is meant to establish. A more selective sufficient
target is capture only on large-envelope marked states. For example,
if the native-depth front is `O(q/log^2(q+2))`, a uniform positive contact
probability would be needed only at marked `q` satisfying
`V(q)>=q/log(q+2)`: the entrance identity would contradict that inequality
for sufficiently large `q`, giving `V(q)<q/log(q+2)` everywhere on the
large marked section. The countermodel has `V<=3`, so it does not obstruct
that conditional target. No such arithmetic capture estimate is proved
here.
