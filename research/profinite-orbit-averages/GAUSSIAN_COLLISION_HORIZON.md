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
