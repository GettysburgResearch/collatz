# Integer constraints on a long first-ladder block

**Status — PROPOSED.** Use the [record conventions](README.md).
For a true positive odd-to-odd first-ladder block $q=x_0,\ldots,x_m=q'$
write $s=S_m$, $r=3^m/2^s>1$, and let $D$ be the largest proper-prefix
drawdown in binary logarithms. All constants below are independent of
the positive ordinary source unless marked otherwise.

## Signed periodic denominator at the two ends

Put $B=3^m-2^s$, and let $C$ be the integer carry given by
$2^sq'=3^m q+C$. The signed fixed point of the word is
$z=-C/B<0$. It is a genuine native periodic point since $B$ is odd,
each signed rotation has integral numerator over the same $B$,
and the exact parity bit is forced at each rotation by reducing the
native one-step identity modulo two. Its least period may divide
the supplied clock. With $a/d=z$ reduced and $d>0$, let
$\Delta=q'-q>0$ and $G=\gcd(B,\Delta)$. Then
$$
 d=B/G,\qquad d q-a=2^s\Delta/G,\qquad d q'-a=3^m\Delta/G.       \tag{L1}
$$
Indeed $C=2^s\Delta-Bq$ and $\gcd(2^s,B)=1$. These identities in
ordinary integers give both local congruences and their exact common
positive factor. In particular $d\ge B/\Delta$.

The block has no repeated odd vertex. A repetition before its end
would produce a positive cycle whose multiplicative coefficient on a
lap is strictly less than one, by multiplying its positive height
ratios. From the first repetition onward the prefix coefficients
are dominated by those in the already traversed lap and cannot cross
one for the first time. Repetition at the terminal point itself
would give $P_m<P_i\le1$ at the previously visited point $i$.
The uniform simple-path reciprocal estimate [from (H3)](HEIGHT.md)
bounds $\sum_{i<m}1/x_i$ by an absolute constant (sum its counting
estimate dyadically). Equivalently one may count just the distinct
odd vertices, cutting off the terminal native value if necessary.
There is no earlier repeated native vertex either: determinism would
force its next odd vertex to repeat, or make $q'$ an earlier odd
vertex. Hence, uniformly,
$$
 x_i=qP_i\prod_{j<i}(1+1/(3x_j))\le C_0q,\qquad 0\le i\le m.   \tag{L2}
$$
Here $P_i\le3/2$. In particular $\Delta\le C_0q$. The elementary
bound $q'\ge r(q+m/3)$ also gives $\Delta\ge m/3$.

The effective two-logarithm estimate for $m\log3-s\log2>0$
gives $B\ge c\,3^m(2m)^{-A}$ with absolute effective $A,c>0$
since $s=\lfloor m\log_2 3\rfloor$. Consequently every such block
satisfies
$$
        d\ge c'\frac{3^m}{q(2m)^A},\qquad d\le 3^m.               \tag{L3}
$$
If $m/\log(2q)\to\infty$, then $\log_3 d/m\to1$.
For each fixed $b<1/2$, the part of $d$ supported on primes
$\le m^b$ has logarithm $o(m)$, by [the checked specialization
of Yu](CYCLE_SIEVE_REVIEW.md) applied to the absolute determinant.
More generally this holds up to $\sqrt m/(\log(2m))^{1+\epsilon}$
for any fixed $\epsilon>0$: the estimate there is
$O(X^2\log(2X)\log(2m))$ for the full logarithm of the small-prime
part of $B$. Hence in the superlogarithmic case the quotient of
$d$ by this entire small-prime part still has
$\log_3(d_{\rm large})/m\to1$. This conclusion does not require
a smoothness hypothesis on $q,q'$ or on their difference.
The real two-logarithm input is classical;
[Lagarias, proof of Theorem 3.2](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf).

There is a related full-prefix statement on every fixed nonrepeating
ordinary ray. Let $k$ tend to infinity through its coefficient records,
with total clock $s_k$, and write $q_0$ for its single initial value.
Equation (L1) holds for each complete prefix as well, since its proof
uses only the two endpoints and positive total coefficient. The signed
fixed point has real value
$$
 z_k=-\frac{M_k}{M_k-1}\frac13\sum_{i<k}M_i^{-1}.
$$
The simple-path reciprocal estimate gives $x_i/M_i\to L>0$ and
$\sum_i M_i^{-1}<\infty$ by the exact affine formula. Since $M_k\to
\infty$, the $z_k$ converge in $\mathbb R$ to the finite negative
value $-(L-q_0)$ and in $\mathbb Z_2$ to $q_0$, by (L1).
Moreover $d_k(q_0-z_k)\ge2^{s_k}$ and $q_0-z_k\to L$, hence
$$
                   d_k\ge (L^{-1}+o(1))\,2^{s_k}.                 \tag{L4}
$$
The entire small-prime part up to
$\sqrt k/(\log(2k))^{1+\epsilon}$ has log $o(k)$ by Yu as above
with $s_k\le\alpha k$. Since $s_k\ge k$, the large-prime part
of the signed prefix denominator is exponentially large on every
actual escaping ray. These periodic approximants are negative and
have unbounded reduced denominators.

## A shallow block has few possible factors

Put $\alpha=\log_2 3$. If $D\le1$ then
$$
                          m\le 2\log_3 q+O(1).                    \tag{L5}
$$
If $D\le1+\delta$ for fixed $0<\delta<1$, then for every
$\epsilon>0$,
$$
                         m\ll_{\delta,\epsilon}
                              (q+1)^{\delta\log_3 2+\epsilon}.    \tag{L6}
$$
If $D\le D_0<1$ there is instead a uniform finite bound
$m\le C(D_0)$ independent even of $q$.

For the proof, at every proper interior time
$\alpha i<S_i\le\alpha i+D$. For $D\le1$ this forces
$S_i=\lceil\alpha i\rceil$. The consecutive differences of these
ceilings on a window of $v$ steps have at most $v+1$ possibilities:
as the initial rotation phase varies, the relative floor differences
change only at the $v+1$ cuts $\{-j\alpha\}$ for $0\le j\le v$.
The actual interior phases never hit a floor cut. Each root state of
one such factor lies in $[1,C_0q]$ by (L2). The same $v$ gaps specify
one residue modulo $2^{S_{i+v}-S_i}$, since their total affine
numerator must be divisible by this power and the leading coefficient
$3^v$ is odd. This modulus is at least $3^v 2^{-D}$. Take
$v=\lceil\log_3(C_0q\,2^D)\rceil+1$. Such a factor can occur at
most once among the distinct integer vertices. The $m-1-v$ interior
starts, if this is positive, therefore number at most $v+1$,
proving (L5).

For $D\le1+\delta$, write
$S_i=\lceil\alpha i\rceil+u_i$ with $u_i\in\{0,1\}$. The choice
$u_i=1$ is available only when $\{\alpha i\}\in[1-\delta,1)$.
Both the underlying floor differences and the eligible indices in
a window are constant on the cells of at most $2(v+1)$ phase cuts.
Allowing single cut points separately gives at most $4(v+1)+1$
patterns, including a possible endpoint hit at $1-\delta$. Let
$M_v(\delta)$ be the maximum, over starting phases, of the number
of visits to an interval of length $\delta$ among $v+1$ successive
rotation points. The number of words is at most
$(4v+5)2^{M_v(\delta)}$. Irrational rotation gives
$M_v(\delta)=(\delta+o(1))v$ uniformly in the initial phase.
For example, bound the moving interval by a finite grid of outer
intervals with lengths $\delta+O(1/k)$, use ordinary
equidistribution on each, and then let the grid size $k$ tend to
infinity. Using the same $v$ and the same integer collision bound
proves (L6). A completely finite upper bound uses the minimum
circular spacing $\Delta_v=\min_{1\le j\le v}\|j\alpha\|>0$:
$M_v(\delta)\le1+\lfloor\delta/\Delta_v\rfloor$. Finally if
$D_0<1$, choose a positive $j$ with $\{\alpha j\}<1-D_0$ by
density. The required integer interval at this fixed $j$ is empty,
so $m\le j$.

The factor-count argument is in the established tradition of
Dubickas's parity complexity bound and Houzé's critical Sturmian
corridor. Here the constraint is imposed at odd times between two
specified coefficient records; (L5) corresponds to a native
corridor of multiplicative width three, and is consistent with the
earlier factor-complexity exit estimate. Results for actual *height*
bands and wider native corridors, including sharper claims in
those settings, cannot be inferred from (L5)–(L6).
[Houzé, critical Sturmian parity exits](https://aixiv.online/abs/2611.00363)
· [Weaver, first exits and positive high occupation](https://rstation.ai/problems/collatz/papers/181/v1)

The tests quantify two alternatives a long ordinary block must
meet. A long block may have a deep internal drawdown and an
arithmetically large signed shadow at the same time. Neither
condition alone prevents a subsequent genuine record.
