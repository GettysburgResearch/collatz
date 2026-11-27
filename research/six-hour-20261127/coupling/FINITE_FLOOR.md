# A certified reciprocal floor for unequal postpeak clocks

**Lean theorem.** Let $y_t=T^t x$, $0\le t\le L$, be an ordinary
shortcut Collatz segment with distinct sites. If $y_t\ge2^{71}$
at every site, including the endpoint, then
\[
  \sum_{t=0}^L \frac1{y_t}<\frac{249}{250},\qquad
  \sum_{\substack{t<L\\ y_t\;{\rm even}}}\frac1{y_t+1}<\frac14.
\]
The hypotheses place no restriction modulo three.
[FloorCounting.lean](FloorCounting.lean) proves the actual-visit
recurrence below. [FloorCertificate.lean](FloorCertificate.lean) uses
it to prove both inequalities with exact kernel arithmetic.

**Written application.** For a literal merger
$T^i(3^m-1)=T^l(3^t-1)$ at the first visit of each arm to the chosen
common endpoint, write $a=i-l$ and
$b=m+Q_i(3^m-1)-t-Q_l(3^t-1)$. If
$|a\log2-b\log3|\ge1/4$, some actual integer on those
two prefixes lies below $2^{71}$. Both peaks and their Mersenne
predecessors then reach one by the published verification through
that range. No bound on either clock is needed. The
[shifted product identity](CROSS_CLASS_FLOOR.md) gives a difference
of two nonnegative logarithms, each less than the even-departure
sum when its segment has an even departure, and equal to zero for
an empty product.
[Barina, *The Journal of Supercomputing* 81 (2025), article 810](https://doi.org/10.1007/s11227-025-07337-0)

For example, every such merger with $|a|=1,2,4,7$ suffices for
every integer $b$. The powers $2^{|a|}=2,4,16,128$ differ by a
factor of at least $4/3$ from every power of three, in the direction
that makes the factor at least one. Here
$\log(4/3)>2/7>1/4$, by
$\log u>2(u-1)/(u+1)$ for $u>1$.
The conclusion also holds when precisely one of $a,b$ vanishes.

## The kernel arithmetic and the even-departure balance

Let $N_j$ count sites below $2^j$ and put $q_j=\lfloor41j/65\rfloor$.
Since $3^{41}<2^{65}$, the recurrence below with $h=j+1,d=0$
and the unpruned binomial counts gives
\[
 N_{j+1}-N_j\le j+1+\sum_{p>q_j}\binom{j+1}p.
\]
Each site in this shell has reciprocal at most $2^{-j}$. Write $w_j$
for the right side times $2^{-j}$ if $j\ge71$, or zero otherwise.
The kernel sums $w_j$ through $j=324$ using exact integer binomial
coefficients and verifies $\sum_{j<325}w_j\le993/1000$.
Tilting the upper binomial tail by $(5/3)^p$ and comparing 65th powers
bounds its normalized mass by $(8/3)(31/32)^j$.
The reserve $R_j=2(j+2)2^{-j}+(256/3)(31/32)^j$ therefore
satisfies $w_j+R_{j+1}\le R_j$. Exact rational arithmetic gives
$R_{325}<3/1000$. This bounds every finite collection of shells
by $249/250$ and proves the all-site estimate.

Let $E(y)$ be $1/(y+1)$ for $y$ even and zero for $y$ odd.
For $y\ge10000$, the two shortcut formulas give the rational inequality
\[
  \frac{3999}{1000} E(y) \le \frac1y+
       3\left(\frac1{Ty+1}-\frac1{y+1}\right).
\]
On an odd step the right side is $1/y-1/(y+1)$. On an even step
the inequality follows by clearing the positive denominators.
Summing leaves only the initial and terminal reciprocal terms.
Thus $(3999/1000)\sum E(y_t)<249/250+3/10000$, giving the stated bound.

## Recurrence for a single arbitrary segment

Let $N_k$ count its sites in $[1,2^k)$, including the final site.
We have $N_k=0$ for $k\le71$. For a site $x<2^k$,
at any clock $j\le k$ consisting of $p_j$ odd inputs, one has
$T^j x<2^{k-j}3^{p_j}$. Induct on $j$ using the displayed integer
upper limit $G$ at the current clock. An odd input $y\le G-1$ gives
$(3y+1)/2<3G/2$, while an even input $y<G$ gives $y/2<G/2$.
Thus to remain above the floor a word must obey
$2^{k-j}3^{p_j}>2^{71}$ at every prefix.

Fix $h=k-d$ with $0\le d<k$. Let $B_{k,h,p}$ count length-$h$
binary words of grade $p$ that satisfy those strict prefix
inequalities. Pascal extension with the failing cells zeroed computes
these integers. The usual parity-vector bijection gives one residue
modulo $2^h$ per word. Among the $2^d$ possible sites in that residue
below $2^k$, at least $\lfloor 2^d/3\rfloor$ are multiples of three,
since successive representatives are a fixed unit apart.

Split the starting sites at their grade after $h$ steps. At most $h$
sites are too near the segment endpoint to have that many steps. For
the sites of grade $p\le q$, the actual endpoints lie below
$2^d3^q\le2^v$, with $v=d+\lceil\log_2(3^q)\rceil$. These
endpoints are distinct since the segment is simple and the shift $h$
is fixed. For grades above $q$, count the admissible starting residues.
This yields

$$
    N_k\le h+N_v+
       (2^d-\lfloor 2^d/3\rfloor)\sum_{p>q}B_{k,h,p}.
$$

The following independent, floor-pruned variant uses the ternary-unit
hypothesis and has a separate exact Python replay. Through $k=350$ the replay minimizes this bound over $0\le d\le8$,
$0\le q\le h$ with $v<k$, together with the trivial $N_k\le2^k$.
For $351\le k\le1500$ take $d=0$, $q=\lfloor3k/5\rfloor$ and
replace $B_{k,k,p}$ by $\binom{k}{p}$. All resulting $U_k\ge N_k$
are integers. Beyond $K=1500$ one can use the same split and count
low endpoints directly as fewer than $3^{3k/5}$ up to rounding
(there are at most $3^q$ positive sites below the integer $3^q$).
The normalized high count is bounded by
$[(5/4)(2/3)^{3/5}]^k$, by tilting with weight $(3/2)^p$.
Both this geometric ratio and $3^{3/5}/2$ are less than $r=99/100$,
as verified by fifth powers. Therefore

$$
  \sum_{k>K}2^{-k}N_k
  \le (K+2)2^{-K}+2r^{K+1}/(1-r).
$$

Every positive integer $2^{j-1}\le y<2^j$ contributes exactly
$\sum_{k\ge j}2^{-k}=2^{1-j}\ge1/y$ to the cumulative bound.
The even departed sites have pairwise different successors $y/2$ on
the segment. Their reciprocal sum is at most half the sum of $1/y$
over all sites. The [exact rational replay](floor_bound.py) checks
that half the finite sum and its infinite tail is below $7/25$.
The [integer-rounded controls](FLOOR_CONTROLS.json) multiply values
by $10^8$ and round upward. No trajectory sampling enters this bound.

**Dependency and limit.** The decomposition by endpoint or parity word
is the effective counting method of PR195,
51d97cbe17054415acaf95e422801a3532545033,
research/astra-global-closure-20261124/round13/trace/FINITE_FAMILY.md,
section “Every actual augmented class is finite.” The explicit range,
floor-dependent prefix counts, ternary-unit restriction and transfer
to the two supplied ordinary clocks above are the present calculation.
There is a stronger external estimate for a different reciprocal sum.
Lemma 2.20 of Nikzad, Frinkle and Bagherzadeh’s 2026 preprint gives
$\sum_{y\text{ departed, odd}}1/y<9/50$ when the simple prefix has
departures above $28019077177231758495$. Hence its unshifted distortion
$\rho=\prod_{y\text{ odd}}(1+1/(3y))$ satisfies
$0\le\log\rho<3/50$. The shifted product equals
$\rho(1+1/\mathrm{endpoint})/(1+1/\mathrm{start})$.
At a common endpoint the endpoint factors cancel. Thus the preprint's
lemma implies the same convergence test already at
$|a\log2-b\log3|\ge3/50+2^{-71}$, including all $1\le |a|\le7$.
The two elementary certificates here give weaker cutoffs for
this application. The preprint's Lemma 2.7 also includes the sharp
finite-prefix endpoint inequality used above.
[On Bounds for Reciprocal Sums and Residues in Collatz Orbits, and Their Consequences, Lemma 2.20 and Appendix 1](https://hexagonmath.org/pdf/2611.00033)

Producing an actual merger of a surviving exponent at a qualifying
clock and grade gap is the first unsupported step.
