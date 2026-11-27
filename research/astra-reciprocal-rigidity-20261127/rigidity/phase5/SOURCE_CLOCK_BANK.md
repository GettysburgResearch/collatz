# A finite inverse tree for fast first landings at any moving target

For the shortcut map \(T(n)=n/2\) on even inputs and \(T(n)=(3n+1)/2\) on odd inputs, let \(d_y(n)\) be the first shortcut time to \(y\). All logarithms in clock formulas are to base two. Write \(\theta=\log_2 3\).

**Moving-target theorem.** There are absolute \(s>1/2,C,c>0\) with the following property. For every odd integer \(y\ge1\) prime to three, every real \(M\ge y\), and every \(X\ge CM\), there is an explicitly selected finite set \(E\subset[X,2X)\) of distinct ordinary positive integers such that

\[
 |E|\asymp (X/M)^s,\qquad
 \max_{k\in\mathbb Z}\#\{n\in E:d_y(n)=k\}
 \le \frac{C|E|}{\sqrt{\log_2(X/M)}}.                         \tag{1}
\]

For each \(n\in E\), every odd state strictly before \(y\) exceeds \(M\). Thus \(y\) is the actual first odd landing below the original threshold, including when \(y\) lies on a cycle. Earlier even states on the final dyadic descent into \(y\) can be at most \(M\). All constants are independent of \(y,M,X\). The denominator in (1) can be replaced by \(\sqrt{1+\log_2(X/M)}\) by changing \(C\).

The same finite construction gives a lower bound on the number of starts at prescribed asymptotic first-hit speeds. Choose any probability vector \(p=(p_H)_{27\le H\le40}\) and put

\[
 \bar H=\sum_H p_H H,\qquad
 v(p)=\frac{\bar H}{\bar H-6\theta},\qquad
 \gamma(p)=\frac{H_2(p)+\sum_H p_H\log_2 M_H}{\bar H-6\theta}.    \tag{2}
\]

Here \(H_2(p)=-\sum_{p_H>0}p_H\log_2p_H\), and the positive integers \(M_H\) are tabulated below. For each \(X\ge CM\), there is an individual true clock

\[
 k=\log_2(M/y)+v(p)\log_2(X/M)+O_p(1)                             \tag{3}
\]

at which at least \(c_p(X/M)^{\gamma(p)}(1+\log_2(X/M))^{-14}\) distinct integers in \([X,2X)\) first visit \(y\), with \(y\) their first odd state at or below \(M\). Taking the extreme pure types gives speeds \(40/(40-6\theta)\) and \(27/(27-6\theta)\). All intermediate speeds occur; they range from about 1.312 to 1.544 steps per binary digit of scale. The conventional negatively drifting geometric-valuation model has central speed \(2/(2-\theta)\approx4.82\). Formula (3) treats much faster, relatively rare paths.

## Actual inverse steps

From an odd positive \(z\), an admissible exponent \(e\ge1\) with \(2^ez\equiv1\pmod3\) gives the positive odd predecessor \(z'=(2^ez-1)/3\). Since \(3z'+1=2^ez\) and \(z\) is odd, the exact valuation is \(e\), and \(T^e(z')=z\). Between its odd endpoints the path consists of \(2^{e-1}z,\dots,2z\).

Set \(m=\lceil\log_2(M/y)\rceil+10\). Among \(m,\ldots,m+5\) there is a unique \(e_0\) with \(2^{e_0}y\equiv4\pmod9\), since (2) has order six modulo nine. Then \(Y=(2^{e_0}y-1)/3\equiv1\pmod3\), \(Y\asymp M\), \(Y>100M\), and \(e_0=\log_2(M/y)+O(1)\). The bridge from \(Y\) to \(y\) has no interior odd state.

Our first two constructions use banks of length \(r\) supplies, at every odd \(z\equiv1\pmod3\), exactly \(M_H\) selected inverse words with \(r\) exponents, all at least two, total \(H\), and endpoint again one modulo three. A deterministic choice, when more exist, takes the first \(M_H\) in lexicographic order. Every inverse odd step from every reached vertex increases it by at least \(5/4\), because \((4z-1)/3\ge5z/4\) at \(z\ge4\).

There is a two-branch bank requiring no tabulation. Put \(r=2,H=24,26,M_H=1\). For a given \(H,z\), choose the unique even \(e_2\in\{4,6,\ldots,20\}\) satisfying \(2^{e_2}\equiv2^H z-12\pmod{27}\). Powers of four have order nine modulo 27 and the right side is one modulo three. Put \(e_1=H-e_2\ge4\). The terminal candidate is

\[
       z'=(2^Hz-2^{e_2}-3)/9\equiv1\pmod3 .
\]

The congruence also implies \(2^{e_1}z\equiv1\pmod3\); the intermediate and terminal odd states are integral, positive and strictly increasing in inverse order. Each branch uses its stated true time.

For the first quantitative bank put \(r=6\). Read the following table as simultaneous minima over all 729 admissible root residues modulo \(3^7=2187\).

| Total \(H\) |27|28|29|30|31|32|33|34|35|36|37|38|39|40|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(M_H\) |2|4|8|10|14|19|25|34|43|55|63|82|95|121|

The exact finite recursion starts with one empty suffix, residue \(1\bmod3\), time zero. For each child suffix of known root class \(b\bmod3^i\), prepend \(e\ge2\). Its unique parent class modulo \(3^{i+1}\) is \((3b+1)2^{-e}\), its time increases by \(e\), and its multiplicity is added to the corresponding bin. Keep totals at most 40, allowing at least two for each remaining step. After six traversals take the minimum for each \(H\) over classes \(z\equiv1\pmod3\). Integrality and exact valuation along the word follow inductively from the inverse formula. The recurrence and its independent short physical-path comparison are in [source_clock_controls.py](source_clock_controls.py).

A second finite bank allows an exponent one when cumulative inverse growth stays positive. Use \(r=8\), require every proper or full chronological prefix to satisfy \(2^{e_1+\cdots+e_i}>3^i\), and now allow every \(e_i\ge1\). The minimum over the 6,561 root classes equal to one modulo three, among classes modulo \(3^9=19683\), is as follows.

| Total \(H\) |24|25|26|27|28|29|30|31|32|33|34|35|36|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(M_H\) |2|4|7|11|18|31|47|67|96|128|172|224|285|

For each total \(H\), the reversed suffix recursion records the remaining prefix total \(h\), initially \(H\). At prefix length \(i\), discard \(h<\lfloor\log_2(3^i)\rfloor+1\). For each possible last prefix letter \(e\), prepend it to the suffix by the previous residue update and replace \(h\) by \(h-e\). The empty prefix must have total zero. This enforces the test at every chronological prefix. The checker computes each threshold as the integer bit length of \(3^i\). All counts use unbounded Python integers. A separate physical enumeration compares both residue recursions against actual integers at three odd steps.

## Stopping measure and unweighted clocks

Write \(Q_H=2^H/3^r\). For a selected word \(e_1,\ldots,e_r\), define \(Q_i=2^{e_1+\dots+e_i}/3^i\). Its exact endpoint is

\[
            z_r=Q_H\left(z-\frac13\sum_{i=1}^r Q_i^{-1}\right).     \tag{4}
\]

For the banks with letters at least two, since \(Q_i\ge(4/3)^i\), the positive quantity subtracted inside the parentheses is at most one. Thus at each macro boundary \(\log_2(z_r/z)=\log_2Q_H+O(1/z)\). The successive boundary heights grow by a factor at least \((5/4)^r\). For any path of \(j\) macro steps from \(Y\), with total time \(S_j=\sum_{a=1}^j H_a\), the entire error remains uniformly bounded:

\[
           \log_2(z_j/Y)=S_j-jr\theta+O(1/Y).                       \tag{5}
\]

For the eight-step bank, \(\min_{1\le i\le8}2^{\lceil i\theta\rceil}/3^i=256/243\). In (4) the correction for every prefix is at most \(8/3\). Since every macro parent \(z\ge Y>100M\ge100\), each intermediate odd state is greater than \(z\), by \(Q_i(z-8/3)>z\). At full macro boundaries \(Q_H\ge 2^{24}/3^8>2000\), giving geometric growth there as well. Equations (4) and (5), with their uniform summable logarithmic errors, therefore hold also for this bank.

The unique \(s>0\) satisfying \(\sum_H M_H Q_H^{-s}=1\) exists since each \(Q_H>1\) and at least two branches exist. For the six-step bank its pressure at \(1/3\) exceeds one by the exact rational certificate

\[
 \sum_{H=27}^{40}M_H (3^6/2^H)^{1/3}
 \ge\sum_{H=27}^{40}\frac{9M_H}{2^{\lceil H/3\rceil}}
 =\frac{18081}{16384}>1.                                            \tag{6}
\]

For the eight-step bank, the same calculation gives
\[
 \sum_{H=24}^{36} M_H(3^8/2^H)^{1/2}
 \ \ge\sum_{H=24}^{36}81M_H\,2^{-\lceil H/2\rceil}
 =269649/262144>1.                                                     \tag{8}
\]
Use its unique pressure root for (1). The six-step bank gives the more elementary special case \(s>1/3\). Formula (2) holds for the second bank too on replacing six by eight and using its own \(M_H\).

Give each individual outgoing word of time \(H\) probability \(Q_H^{-s}\). The times \(H_1,H_2,\ldots\) are independent with probabilities \(M_H Q_H^{-s}\), because those probabilities are identical at all possible parent states.

For \(R\ge2\), stop each branch at its first macro boundary \(z_j\ge RY\). The endpoint lies in \([RY,Q_{\max}RY)\), where \(Q_{\max}=\max Q_H\), and \(j\asymp\log R\) for sufficiently large \(R\). Every leaf has path probability \(2^{-s(S_j-jr\theta)}\asymp R^{-s}\) by (5). The finite stopping leaves have total probability one. Their count is consequently comparable to \(R^s\), and the unweighted fraction of any subfamily is bounded by a constant times its probability.

Distinct leaves are distinct physical odd integers. From a leaf the forward odd orbit uniquely recovers every exponent until its first visit to \(Y\); there is no earlier visit because every intermediate odd state is greater than its macro parent and the successive macro parents strictly increase. The number of odd transitions is \(rj\); partitioning them into groups of \(r\) recovers the branch choices. The same reasoning shows that two different stopping leaves cannot lie on each other's forward path before \(Y\). If they did, their depths might at first appear misaligned, but their distances to \(Y\) in odd steps are both multiples of \(r\); one would be a macro boundary of the other. That contradicts the first-crossing rule.

Fix a true time \(d=e_0+S_j\). By (5) and the bounded logarithmic width of the stopping interval,
\(jr\theta=d-e_0-\log_2 R+O(1)\). Only a bounded number of \(j\) can contribute. The independent, finitely supported, nonconstant time law satisfies \(\sup_a\Pr(S_j=a)\le C/\sqrt j\). To see this, choose two distinct atoms and condition on the indices falling in their union and on all other values. The number of chosen indices has a binomial law with positive mean proportion, and conditional on \(m\) such indices the maximal mass is \(O((1+m)^{-1/2})\) by the binomial bound. A binomial tail estimate handles \(m\) below half its expectation. Dropping the stopping condition at each of the boundedly many depths now proves the point-atom estimate on the leaves.

Use \(R=X/(Q_{\max}Y)\), increasing the absolute lower bound for \(X/M\) as needed. The leaves lie in \([X/Q_{\max},X)\). For each odd leaf \(z\), multiply by the least \(2^a\) with \(2^az\ge X\). The resulting integers lie in \([X,2X)\); their odd parts recover their distinct leaves. The clock changes by one of at most \(1+\lceil\log_2Q_{\max}\rceil\) possible shifts. This bounded union preserves the point-atom estimate and proves (1). In fact any \(w\) prescribed clock values capture at most \(Cw/\sqrt{\log_2(X/M)}\) of this selected set.

## Entropy of a prescribed fast clock

For a given \(p\) let \(A=\bar H-r\theta>0\). At each depth \(j\), choose nonnegative integer multiplicities \(b_H\) with \(\sum b_H=j\), zero off the support of \(p\), and \(|b_H-jp_H|\le1\). These words all have one total \(D=\sum H b_H=j\bar H+O(1)\) and one ideal logarithmic growth \(D-jr\theta=jA+O(1)\). By (5) their true endpoints have the same logarithmic height within \(O(1/Y)\). Take \(j=\lfloor\log_2(X/Y)/A\rfloor-K\) with a fixed integer \(K\) large enough that all endpoints are below \(X\). Every endpoint is at least \(c_pX\). For large enough \(X/M\) this depth is positive. Bounded smaller scales can be covered by enlarging fixed constants, or by using the bridge and a dyadic lift directly.

There are exactly
\[
             \frac{j!}{\prod_H b_H!}\prod_H M_H^{b_H}               \tag{7}
\]
physical endpoints. Histories at this common depth are recovered from the deterministic odd orbit. The standard multinomial type bound gives (7) at least \(c_p (1+j)^{-14}2^{j[H_2(p)+\sum p_H\log_2 M_H]}\). For example, the exact type is a mode under its own empirical probabilities and there are at most \((1+j)^{14}\) possible types. Replacing empirical by fixed positive \(p_H\) on its support costs a bounded factor by differentiability of entropy there. The dyadic shell lift adds only boundedly many possible clock values, so a fixed fraction of the endpoints give one clock with (3). This proves the fast-speed count.

## Fixed components and bounds from other sources

Take \(M=y\). On any ordinary component with signed shortcut clock \(\tau(Tn)=\tau(n)+1\) away from a cyclic cut at its minimum cycle vertex, these sources satisfy \(\tau(n)=\tau(y)-d_y(n)\). A trajectory ending at a noncyclic \(y\) cannot pass through a cycle first. If \(y\) lies on the cycle, a cut at or below \(y\) cannot occur among the earlier odd states, and earlier even states are greater than \(y\). The minimum cycle vertex is odd. The identical finite first-hit construction therefore transfers a clock anomaly at a supplied target to many actual sources. Their number and dispersion are relative to this particular selected cohort. The support or density of a separately specified exceptional cohort is an additional question.

For a *fixed* ordinary component, Mazur's positive lower predecessor density for each fixed ternary-unit target gives a different deduction. Every component contains an odd ternary unit: start at any integer, remove powers of two, and if the odd part is divisible by three then the next odd iterate is a unit. Its predecessor set has positive lower density under Mazur's theorem. Dividing the phase-three ambient-clock bound by that density gives \(O_C(1/\sqrt{\log X})\) relative mass for each clock in the *whole* fixed component below \(X\). The constant may depend on the component. Mazur's source reports a Lean formalization; its entire development has not been rebuilt here. [Mazur, Positive lower density of Collatz predecessors](https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [ordinary ambient-clock proof](../phase3/CLOCK_DISPERSION.md)

Krasikov and Lagarias prove a much larger predecessor counting exponent \(0.84\) for fixed targets with target-dependent onset. Wren 10, Corollary 3.5, obtains a uniform lower count at each central odd depth from an external averaged joint Syracuse mixing estimate. Weaver 12, Lemma 13 and Theorem 14, retains real offsets and proves a linear-size set hitting an arbitrary odd unit first below \(M\) in a factor-four shell. In its proof there are \(\gg\sqrt L\) distinct shortcut times \(e+d_k\), \(d_k=\lfloor L+k\theta\rfloor\), with \(\gg X/(M\sqrt L)\) sources per time, \(L=\log_2(X/r)\) and \(r\asymp M\). Equal thinning at those times gives a linear-size selected cohort with \(O(1/\sqrt L)\) largest relative atom on Weaver's inputs. Those works already supply stronger population counts in the central-speed range. Our finite bank gives an elementary first-landing construction at different, explicitly fast speeds (2)–(3). It does not import those mixing or density estimates. [Krasikov–Lagarias](https://arxiv.org/abs/math/0205002) · [Wren 10, v3](https://rstation.ai/problems/collatz/papers/10/v3) · [Weaver 12](https://rstation.ai/problems/collatz/papers/12)

These results constrain actual ancestors of every target. They leave the future orbit of that target unrestricted and do not establish universal descent.
