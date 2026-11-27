# A positive fraction of a long cycle must lie above twice its minimum

**PROPOSED written theorem.** There is an absolute $p_0$ such that in every primitive positive ordinary Syracuse cycle of odd period $p\ge p_0$, more than $p/21$ distinct odd phases exceed twice the minimum $m$. Moreover there is an absolute $\eta>0$ such that every nontrivial primitive positive ordinary cycle satisfies this conclusion with $\eta p$ in place of $p/21$. The proof concerns the phases of one literal cycle. It uses no random trajectory law and no inverse floor. It does not exclude cycles with the required spread.

Write $U(x)=(3x+1)/2^{v_2(3x+1)}$, and index the odd phases $x_i$ cyclically. Their distinctness follows from primitivity. If $A$ is the sum of the valuations on the entire lap, telescoping yields
$$
 0<A\log 2-p\log 3=\sum_{i=0}^{p-1}\log(1+1/(3x_i))\le p/(3m).
$$
Also $A\le2p$, since $3+1/x_i\le4$. Wu and Wang's Theorem 1 with constant coefficient zero gives, for every fixed $\zeta>0$ and all sufficiently large $p$, a lower bound $(2p)^{-4.1163051-\zeta}$ on this nonzero linear form. Consequently
$$
 \log m\le(5.1163051+\zeta)\log p+O_\zeta(1).
$$
No explicit numerical onset is asserted. [Wu and Wang, *On the irrationality measure of log 3*, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

Set $k=\max(1,\lceil\log_3 m\rceil)$ and $h_i=\lfloor\log_2(x_i/m)\rfloor$. These nonnegative integers satisfy $h_{i+1}\le h_i+1$ since $U(x)\le2x$. A positive level means $x_i>2m$, because $x_i$ is odd. Suppose that at most $p/21$ indices have positive level. Examine the $p$ windows from $i$ through $i+k$, counted by their distinct starting phases. At most $2p/21$ windows have either endpoint positive. Summing the number $r$ of positive interior levels over all windows gives at most $(k-1)p/21$. Thus with $\theta=4/75$, at least $(1-2/21-1/(21\theta))p=p/84$ windows have both endpoint levels zero and $r\le\theta k$.

For fixed $r$ between zero and $k-1$, these windows admit at most $\binom{k+r}{r}$ different level profiles. For each edge record the integer
$$
 a_j=h_j+\mathbf{1}_{h_{j+1}>0}-h_{j+1}\ge0.
$$
The inequality is immediate when the next level is zero, and otherwise follows from the one-level rise bound. Telescoping between the zero endpoints gives $\sum a_j=r$. Reading backwards from the terminal zero reconstructs every level by $h_j=a_j+\max(h_{j+1}-1,0)$. The code is therefore an injection into weak compositions of $r$ into $k$ parts, of which there are $\binom{k+r-1}{r}$. [Lean proof of code length, total mass and injectivity](OctaveOccupation.lean)

For each specified profile the moving-octave estimate M1 bounds the number of possible distinct ordinary sources by $(k+1)\lceil m/3^k\rceil=k+1$. Its terminal octave has lower endpoint $m$, irrespective of the intervening levels. In brief, on initial logarithmic phase $t\in[0,1)$ the cumulative valuations are floors of increasing degree-one lifts indexed by the successive octave intervals. Each coordinate increases at most once and their vector thus takes at most $k+1$ values. For a fixed word with total $s$, two sources agree modulo $2^{s+1}$ since the odd outputs differ by an even integer. Positivity of the affine carry gives $2^{s+1}>3^k$ when both end intervals are $[m,2m)$. This modulus exceeds the interval length. [M1, moving height intervals and dyadic–triadic order, §1](https://github.com/GettysburgResearch/collatz/blob/d35bdfd9d0c75effda50bbb8040c136482431e24/research/astra-global-synthesis-20261124/arithmetic/proof.md)

Summing the profile bounds and writing $f(t)=(1+t)\log(1+t)-t\log t$ gives
$$
 p/84\le(k+1)^2\exp(kf(\theta)).
$$
Here $\binom{k+r}{r}\le\exp(kf(r/k))$ follows from the binomial theorem and $f$ is increasing. But $f(4/75)<0.212$ and $5.12\cdot0.212<\log3$. Take $\zeta=0.003$ in the height bound. The right side is $O((1+\log p)^2p^\gamma)$ with $\gamma=5.12\cdot0.212/\log3<1$, a contradiction for sufficiently large $p$. This excludes the stated class of long cycles.

For every remaining nontrivial cycle there is at least one phase outside the minimum octave. The adjacent-gap denominator argument for a cycle wholly in $[m,2m)$ gives $2^A-3^p=1$, whose only positive solution is $A=2,p=1$, with $m=1$. Taking, for example, $\eta=\min(1/22,1/(p_0+1))$ handles bounded periods as well. [Complete denominator calculation, §2](https://github.com/GettysburgResearch/collatz/blob/d35bdfd9d0c75effda50bbb8040c136482431e24/research/astra-global-synthesis-20261124/arithmetic/proof.md)

The strict entropy comparison $5.12 f(4/75)<\log 3$ can also be checked without logarithms: the integers $79^{79\cdot128}$ and $3^{1875}(75^{75}4^4)^{128}$ have respective bit lengths 63744 and 63793.

The numerical fraction uses the published exponent of Wu and Wang; any effective polynomial two-logarithm bound gives a possibly smaller positive fraction. The proof imposes no bound on the heights or number of distinct excursions above $2m$. A cycle could satisfy the conclusion and still meet all known complete-lap divisibility conditions. The divergent case has no full-period logarithmic form or circular counting measure to which this argument applies.
