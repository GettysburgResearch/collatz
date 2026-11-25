# A third multiple of the minimum for cycles with valuations one or two

**PROPOSED written deduction, source-qualified on the homogeneous logarithm input.** Under the two-logarithm estimate reported by Chudnovsky, every sufficiently long primitive positive cycle with odd valuations in $\{1,2\}$ has one of the following properties:

* More than $p/2000$ of its odd phases exceed $3s$, where $s$ is its minimum.
* Its full reduced denominator $d$ is greater than $p^{1/100}$.

Thus a sufficiently long ordinary cycle with those valuations must satisfy the first alternative, even if some odd phases are arbitrarily high. This applies in particular to the bounded least-tripling-disagreement case. The unrestricted-valuation proof with this external input alone gave an occupation statement only for thresholds strictly below $2\sqrt[3]{3}\,s$. The proof below uses the arithmetic inequalities on pairs of physical valuations supplied by the new hypothesis. [General counting proof and source status](README.md) · [Chudnovsky, Corollary 1.2](https://arxiv.org/html/2611.30820v1)

Assume instead $d\le p^{1/100}$ and at most $Qp$ high phases for $Q=1/2000,\ K=3$. Retain the windows, starting bins and normalized probabilities of the general proof. Write $\alpha=\log_23$, $\delta=\alpha-1=\log_2(3/2)$, $t=1/1998$ and $k=\lceil\log_3(3ds)\rceil$. We will save a fixed amount on disjoint pairs of consecutive unmarked positions. Every statement below concerns that same window for its fixed starting bin.

In phase order the positions at which the interval of allowed cumulative clocks contains two integers occupy an arc of length $\delta+2\eta$ on the unit circle. Choose inside this arc a translate of $[0,\delta]$, using it in the orientation of the phase advance by $\delta$. In the translated coordinates, use every pair of successive positions $i,i+1$ (both among $1,\ldots,k$) whose first phase lies in
$$
                          (1-\delta,\delta).
$$
Both positions have two clock choices. The second phase belongs to $(0,2\delta-1)$, disjoint from the first-phase interval, since $1/2<\delta<2/3$. Thus these pairs are disjoint. Their number is $(2\delta-1+o(1))k$ uniformly in the translate, by the same irrational rotation grid count as in the general proof, applied also to the complementary arc for the lower estimate. Endpoints of the window affect at most one pair.

At consecutive positions the lower available integer is the ceiling of a real number that advances by $\alpha$. Its increase is either one or two. The two choices are the lower integer and that integer plus one. If the lower increase is one, the pair (upper, lower) gives gap zero. If it is two, the pair (lower, upper) gives gap three. In either case exactly three of the four pairs of choices are compatible with a physical valuation in $\{1,2\}$. After the mask is known, at every selected pair with both endpoints unmarked give these three choices uniform probability, in place of the independent quarter weights. A mark destroys at most one pair since they are disjoint. Hence the mean savings in the unmarked clock code is at least
$$
                  k(2\delta-1-t+o(1))\ln(4/3).
$$
The code still recovers each complete physical word, and the proof of terminal uniqueness in the denominator-$d$ numerator lattice still applies.

After $\eta\downarrow0$, its exponent is consequently at most
$$
 B_*=\frac{\delta\ln2-(2\delta-1)\ln(4/3)+H(t)+t\ln4}{\ln3}.
$$
Here the $t\ln4$ term combines the high-clock cost $t\ln3$ and the possible lost pair savings $t\ln(4/3)$. To verify $B_*<100/301$, observe that
$$
 \log_3(3/2)<37/100,\quad
 \log_3(4/3)>13/50,\quad
 2\delta-1=\log_2(9/8)>1/6 .
$$
The first two comparisons follow from $3^{63}<2^{100}$, the third from $9^6>2\cdot8^6$. Also $H(t)+t\ln4<t\ln(12/t)<10t\ln3$. The resulting bound is
$$
                      B_*<37/100-13/300+10/1998<100/301 .
$$
The form input gives $s\ll_\varepsilon p^{3+\varepsilon}$ as before, so $\limsup\ln p/\ln(ds)\le B_*$ contradicts $d\le p^{1/100}$. All strict comparisons use exact integer arithmetic in the finite replay. The counting argument is written mathematics. This result still permits the high population within the bounded-branch ceiling $(16s+7)/3$ and gives no all-cycle contradiction there. [Integer comparisons](check.py)
