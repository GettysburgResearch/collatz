# A Gaussian cutoff for unequal-clock shortcut meetings

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Write
$d=\log(4/3)$, $\mu=2/d$ and $\sigma^2=2(\log3)^2/d^3$.
All unmarked logarithms are natural. Fix $\delta>0$. For a dyadic
octave $[X,2X)$ set $L=\log X$ and
$$
 H_X=\left\lfloor\mu L-\sigma\sqrt{L\{2\log L+
                    (1+\delta)\log\log L\}}\right\rfloor .
$$
Only sufficiently large $X$ matter. For any fixed integer $a$, outside
an exceptional set of $n$ with $\sum 1/n<\infty$, every meeting
$T^i(n)=T^j(n+a)$ with $0\le i,j\le H_X$ has $i=j$ and the same
number of odd inputs on both arms. The same holds with starting pair
$(2n,2n+1)$ and $H_X$ defined using the octave of $n$.
This deduction uses Leen's stated moderate-deviation theorem
and the lower bound for a nonzero linear form in $\log2,\log3$.

**Source and height estimate.** For an odd source $W_Y$ uniform on
$[Y,2Y)$ write $J_z$ for the number of accelerated odd steps to the
first odd value $P\le z$, and $J_z=\infty$ on failed passage.
Put $\sigma_J^2=2(\log2)^2/d^3$. Leen's theorem “Moderate deviations
with clock–landing independence” (source label thm:md-B) gives,
for every fixed $\epsilon_0\in(0,1)$, $K\ge1$, $A>0$ and
$0<c_\gamma<5/143$, uniformly for
$(\log Y)^{\epsilon_0}\le\log z\le(\log Y)/(1001/1000)$
and $0\le t\le K\sqrt{\log\log Y}$,
$$
 \Pr\left(J_z<\infty,\quad
 J_z\le\frac{\log(Y/z)}d-t\sigma_J\sqrt{\log(Y/z)}\right)
 \le (1+O((\log z)^{-c_\gamma}))H_z(1)\overline\Phi(t)
       +O((\log z)^{-A}).
$$
Here $H_z(1)=1+o(1)$ and $\overline\Phi$ is a standard Gaussian tail.
This is the negative-tail inequality with the constant landing test.
[Leen, original TeX, moderate deviations](https://zenodo.org/api/records/23252395/files/collatz-brownian-motion-md.tex/content)
· [clock definitions and input hypotheses](https://doi.org/10.5281/zenodo.23252395).

Take $n$ uniform on $[X,2X)$. Dropping $v_2(n)>3\log_2 L$ costs
$O(L^{-3})$ in probability. At each retained valuation $e$, the odd
core $w$ is exactly uniform among the odd integers in $[Y,2Y)$ with
$Y=X/2^e$ and $\log Y=L+O(\log L)$. Choose $z=\exp(L^{1/4})$.
If the shortcut path reaches $[1,z]$, its initial $e$ halvings stay
above $z$ for large $X$. Starting at $w$, the first odd landing occurs
after $D$ shortcut steps. The first shortcut visit to $[1,z]$ is
at most $\log_2 z$ steps earlier, since each intervening step halves
an even value already at most $z$. Multiplying the shortcut updates
gives
$$
 D=\log_2(w/P)+J_z\log_2 3+
       \sum_{u\text{ odd before }P}\log_2(1+1/(3u)).
$$
Thus the first shortcut visit from $n$ occurs at time at least
$\log_2(Y/z)+J_z\log_2 3-\log_2 z$. Failed odd passage entails
failed shortcut passage.

Put $t_L=\sqrt{2\log L+(1+\delta/2)\log\log L}$. Use
$\sigma_J\log_2 3=\sigma$ and $1/\log2+(\log_2 3)/d=\mu$.
If that visit occurs by $H_X$, then
$$ J_z\le\log(Y/z)/d-t_L\sigma_J\sqrt{\log(Y/z)}. $$
Indeed using $\log(Y/z)$ in place of $L$ in the center costs
$O(L^{1/4}+\log L)$ and in the square-root term costs $o(1)$.
Replacing $1+\delta$ by $1+\delta/2$ provides a positive margin
of order $\sqrt L\log\log L/\sqrt{\log L}$, larger than both errors
and the $\log_2 z$ shift. The source theorem applies with
$\epsilon_0=1/4$, $K=3$ and $A=12$. By the Gaussian tail bound
$\overline\Phi(t)\ll e^{-t^2/2}/t$, the probability that any
shortcut iterate by $H_X$ falls to $z$ or below is at most
$$
 O_\delta\left(\frac{1}{L(\log L)^{1+\delta/4}}+L^{-3}\right).
$$
This bound is uniform over the retained valuations and hence holds
for all ordinary sources in the octave. Summing over $X=2^h$ gives
finite reciprocal mass to exceptional starts. Bounded shifts of the
starting integer satisfy the same assertion by covering their interval
with adjacent octaves. The $O(1)$ changes in the clock center and
constant-factor changes of $z$ when passing to either adjacent octave
are absorbed by the same Gaussian margin. For $2n,2n+1$ use the
octave at $2X$ and bound either parity restriction by twice its full
octave probability.

**Collision.** If both paths stay above $z$ through this horizon and
the numbers of odd inputs are $p,q$, the same product identity at
a common endpoint gives
$$
 |(p-q)\log3-(i-j)\log2|
 \le |\log(1+a/n)|+2H_X/(3z).
$$
For the pair $(2n,2n+1)$ the initial log ratio is $\log(1+1/(2n))$.
A nonzero left side is at least $c(2H_X+2)^{-C}$ with absolute
$c,C>0$ by the two-logarithm case of Baker–Wüstholz. The upper bound
is smaller for large $X$. Unique factorization gives $p=q$ and $i=j$.
[Baker and Wüstholz, logarithmic forms](https://doi.org/10.1515/crll.1993.442.19).

In particular, if the even-start pairs that never meet at equal
shortcut times have divergent reciprocal sum, the even-start pairs
admitting **no meeting of any two clocks** through $H_X$ also have
divergent reciprocal sum. This last inference removes a set of
finite reciprocal mass from the assumed divergent set. It imposes
no restriction on later unequal-clock meetings.

**Sharpness for the height test.** Keep $z=\exp(L^{1/4})$, replace
$1+\delta$ in $H_X$ by any fixed real $b$, and write
$t=\sqrt{2\log L+b\log\log L}$. The fraction of ordinary octave
starts visiting $[1,z]$ by this cutoff is
$(1+o(1))\overline\Phi(t)$. To see the reverse comparison, on a
finite odd passage with $J_z=O(L)$ the positive residual in the
formula for $D$ is $O(L/z)$ since each earlier odd state exceeds
$z$. Also $P\ge1$, so the shortcut visit from $n$ is no later than
$e+\log_2(2Y)+J_z\log_2 3+O(L/z)$. Together with the lower estimate
above this sandwiches the event between the two finite odd-clock
lower tails of the source theorem with standardized levels
$t\pm C L^{-1/4}$. Indeed the centers differ by $O(L^{1/4})$,
and the normalization changes by a relative $O(L^{-3/4})$.
The lower-tail event used for sufficiency has $J_z=O(L)$.
Use both sides of Leen's relative estimate with $g=1$ and $A=12$.
The Gaussian tail ratios tend to one, since $tL^{-1/4}=o(1)$.
The omitted large valuations cost $O(L^{-3})=o(\overline\Phi(t))$.
Thus the reciprocal mass of these height exceptions is finite
exactly when $b>1$, by
$\overline\Phi(t)\asymp L^{-1}(\log L)^{-(1+b)/2}$.
This boundary concerns fast passage to the specified growing floor;
even a fast passage need not produce an unequal-clock collision.

## Sharp reciprocal order of pairs with no meeting

At each positive integer $n$ use $X=2^{\lfloor\log_2n\rfloor}$
to assign the cutoff $H_X$ above to the pair $(2n,2n+1)$. Let $B$
contain the $n$ for which these two trajectories have no meeting at
**any** pair of times $0\le i,j\le H_X$. For each fixed $\delta>0$,
$$
 \sum_{\substack{n\le N\\n\in B}}\frac1n
       \asymp_\delta \sqrt{\log N}\qquad(N\to\infty).
$$
This conclusion also uses Leen's terminal clock central limit theorem,
minimum-tail estimate and finite balanced synchronization bound.
[Brownian motion in Collatz orbits](https://doi.org/10.5281/zenodo.23252395)
· [Exact rates in Collatz synchronization](https://doi.org/10.5281/zenodo.23268751).

For a start $x$, write $m(x)$ for its global orbit minimum and
$\tau_*(x)$ for the first shortcut time attaining it. The minimum
for shortcut and ordinary dynamics agrees: an omitted intermediate
$3x+1$ exceeds the retained neighboring values. The Brownian paper's
minimum-tail corollary gives
$\Pr(m(W_Y)>R)\ll_A(\log R)^{-A}$ uniformly on odd octaves $Y\ge R$.
With $R=\exp(\tfrac12 L^{1/4})$ and the same dyadic stripping as
above, this costs $O(L^{-3})$ taking $A=12$.
Thus, except for a set $E$ of parent indices $n$ of finite reciprocal
mass, both sibling paths stay strictly above their own minima through
$H_X$ and every meeting through $H_X$ is synchronous. The bounds
use the entire octave for each arm, so the separate parity restrictions
cost at most a factor two.

On every $n\notin B\cup E$ there is therefore a common endpoint at a
common time before either first minimum. The common future must attain
both global minima and its remaining clock to that value is identical.
This gives $\tau_*(2n+1)=\tau_*(2n)=1+\tau_*(n)$. The last equality
holds for every $n$ because $T(2n)=n<2n$.

Take $u$ uniform in $[1,2)$ and put $n_j=\lfloor 2^ju\rfloor$.
The digit selecting $n_{j+1}=2n_j$ or $2n_j+1$ is fair and
independent of $n_j$. Define $Z_j=\tau_*(n_j)-j$.
It stays fixed at every even child and at every odd child whose
parent lies outside $B\cup E$. By the terminal Brownian theorem
$\tau_*(n_j)=\mu j\log2+O_{\Pr}(\sqrt j)$ on these octaves.
Tightness on the full interval $[2,2^{j+1}]$ transfers to its
upper octave by a factor at most three in probability; replacing
$\log n_j$ by $j\log2$ costs $O(1)$.

Put $b=\mu\log2-1>0$. Choose a fixed $M$ so large that
$|Z_j-bj|\le M\sqrt j$ has probability at least $9/10$ at
every sufficiently large depth. Then choose fixed $C>4M/b$ and
$k=j+\lceil C\sqrt j\rceil$. With probability at least $4/5$
both endpoint bounds hold, and their intervals are disjoint for
large $j$. Hence $Z_j\ne Z_k$, requiring at least one observed
odd child with parent in $B\cup E$. For a particular parent $n$
at depth $i$ that observation has probability $2^{-i-1}\le1/n$.
The probability of any such observation with parent in $E$ at
any depth $i\ge j$ tends to zero by reciprocal summability.
Consequently for all sufficiently large $j$,
$$ \sum_{\substack{2^j\le n<2^k\\n\in B}}1/n\ge1/2. $$
Take consecutive blocks of these depths. Each increment in $\sqrt j$
is bounded above by a constant, giving $\gg\sqrt{\log N}$ completed
blocks through $N$.

For the upper estimate, a pair in $B$ has failed balanced shortcut
coalescence by native time $j$ for $2^j\le n<2^{j+1}$, since
$H_{2^j}\ge j$ eventually. In the full octave of adjacent starting
positions $x\in[2^{j+1},2^{j+2})$, native balanced noncoalescence
at time $j$ has fraction $O(j^{-1/2})$ by the complete-period
absorption count. Keeping only $x=2n$ costs at most two.
The reciprocal contribution is thus $O(j^{-1/2})$ per octave.
Summing proves the matching order.

There is an explicit form of the shorter-block lower estimate. For
each fixed $s>0$ take $k=j+\lceil s\sqrt j\rceil$. The marginals of
$(Z_j-bj)/\sqrt j$ and $(Z_k-bj)/\sqrt j$ converge respectively
to a centered normal of variance $\sigma^2\log2$ and its translate
by $bs$. This follows from the terminal clock theorem by differencing
initial intervals for the octave limit. Test both marginals at $bs/2$.
The difference of their probabilities forces unequal endpoint labels
with limiting lower probability $2\Phi(bs/(2\sigma\sqrt{\log2}))-1$.
After removal of $E$ this is a lower bound for the liminf of the same
block reciprocal sum. The number of completed blocks through binary
depth $J$ is asymptotic to $2\sqrt J/s$, since
$\sqrt k-\sqrt j\to s/2$. Letting $s\downarrow0$ gives
$$
 \liminf_{N\to\infty}
 \frac1{\sqrt{\log N}}\sum_{\substack{n\le N\\n\in B}}\frac1n
 \ \ge\ \frac{2(\mu\log2-1)}{\sigma\sqrt{2\pi}\log2}.
$$
This computation uses only the separate Gaussian marginals at the two
depths; the two nested sources need no joint limit theorem.
