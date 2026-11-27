# Charge and the multiplicity of fixed-target evidence

**PROPOSED.** For a positive ordinary \(x\) that reaches one, set
\[
      J(x)=F(x)-2P_{F(x)}(x)
\]
using its first shortcut hit \(F(x)\) at one. Each additional lap on the cycle through one uses two clocks and one odd input, so every later hit gives the same charge. If \(T^a x=T^b y\) on convergent sources, then
\[
 J(x)-J(y)=a-2P_a(x)-b+2P_b(y).                                      \tag{1}
\]
Indeed both sides decompose into the prefix charge and the identical charge from their common site. Conversely \(J(x)=J(y)\) is equivalent to a common equal-clock, equal-grade merger. First hits then differ by twice the odd-count difference; pad the earlier first hit by this many clock pairs divided by two. The resulting common deadline can be taken as the larger of their first-hit clocks. [Kernel verification of (1) and its balanced-pair consequence](Charge.lean)

## An all-clock counterexample to a source-independent word substitution

Suppose that two fixed lower words on \(z,y\) meet after clocks \(a,b\), and two fixed upper words on \(3z,3y\) meet after clocks \(c,d\). Suppose both identities hold *as functions* on a nonconstant affine family \(z=A t+B,\ y=A't+B'\) of positive ordinary parents, with \(A,A'>0\). Write \(p,q,r,s\) for the odd counts on the respective four words. Equality of the leading coefficients on the two arms gives
\[
       A'/A=2^{b-a}3^{p-q}=2^{d-c}3^{r-s}.
\]
Taking the valuations at two and three gives \(a-b=c-d\) and \(p-q=r-s\). The shift in clock minus twice the odd count is identical across the two arms. At any convergent specialization, equation (1) now forces
\[
       J(z)-J(3z)=J(y)-J(3y).                                       \tag{2}
\]
Contextual words can be arbitrarily long, selected after seeing the supplied source, have asynchronous clocks, or be composed from any number of contextual two-arm comparisons. Every selected comparison still satisfies (2). This applies to identities in a varying ordinary parameter. An isolated equality at one numerical source has no leading-coefficient obligation.

| parent | lower first hit and odd count | upper first hit and odd count | lower charge minus upper charge |
|---:|---:|---:|---:|
| 17 | \(9,3\) | \(17,7\) | 0 |
| 65 | \(19,8\) | \(76,43\) | 13 |

At the ordinary upper-rank-43 parent \(65\), the only smaller positive canonical parent is \(17\). The charge obstruction excludes **every** balanced physical merger between those two pairs, at all clocks; in particular it excludes the preceding contextual comparison at this source. Both pairs converge, so actual unbalanced comparisons are possible. The kernel theorem quantifies over every smaller canonical positive parent and all four clocks; its four finite certificates establish the charges of the actual ordinary starts. The finite checker separately verifies first hits. [Charge.lean](Charge.lean) · [Finite replay](check_pairs.py)

The prior joint entrance-grade observation derives two clock/grade invariants from leading coefficients on matched affine paths, and the prior graded-minimum work classifies some charged reference families. Here (2) gives an all-clock obstruction at a specified ordinary \(17\bmod48\) source against its *entire* smaller canonical pool. This failure on convergent data leaves the conditional least-disagreement problem open. [PR197, joint entrance grades, §6](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/joint-renewal/JOINT_ENTRANCE_GRADES.md) · [PR195, graded minima](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/GRADED_MINIMA.md)

## Why many protected predecessors need not give many protected representatives

Fix a positive \(q\) with a non-eventually-periodic trajectory. Consider any collection of canonical \(x\) whose lower arms visit this *same* \(q\) and whose triples reach one. Let \(h_x,p_x\) be the clock and odd count at \(q\), and \(j_x=J(3x)\). The clock at \(q\) is unique: a second visit would make \(q\) periodic. Two of these pairs admit eventual equal-clock, equal-grade mergers on each respective coordinate if and only if
\[
           (h_x,p_x,j_x)=(h_y,p_y,j_y).                              \tag{3}
\]
For necessity advance any lower merger to a common time after both arrivals at \(q\). Unequal \(h_x,h_y\) would give two equal iterates of \(q\) at distinct clocks, making its trajectory eventually periodic. With their clocks equal, the identical suffix forces \(p_x=p_y\). Equation (1) handles the upper coordinate. For sufficiency the lower arms meet at \(q\), and equality of the upper charges gives the equal-grade upper merger already described. Pad to one common clock if desired.

If both prescribed arrival clocks are at most \(H\), these mergers already occur by \(H\) within each class, and there are at most \((H+1)^2(2H+1)\) classes. This bound remains valid for any chosen subset and imposes no independence. It counts classes rather than original predecessors.

There is a sharper estimate on any one octave \(X\le x<2X\). The known uniform bound \(C_*\) on the reciprocal sum of all departed states in *any* simple positive Collatz prefix yields
\[
 1\le D_x=\prod_{\rm odd\ departure\ v}(1+1/(3v))\le e^{C_*/3}.
\]
The path through its visit to nonperiodic \(q\) is simple, and \(2^{h_x}q=3^{p_x}xD_x\). For each given \(p_x\), the quantity \(h_x-p_x\log_2 3\) belongs to an interval of length \(1+C_*/(3\log 2)\). Thus \(O(1)\) choices of \(h_x\) suffice per \(p_x\), uniformly in \(X,q\), and the number of classes in (3) is \(O((H+1)^2)\). The reciprocal bound is used only for this last improvement. [Uniform simple-path bound, round twelve](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-global-closure-20261124/round12/arithmetic/README.md)

In particular a pointwise lower bound for the **number of original paired predecessors** with polylogarithmic arrival clocks would still be compatible with only polylogarithmically many different counted classes on the octave. Obtaining \(X^\beta\) different classes in this fixed-target setting requires \(H\gg X^{\beta/2}\). When the original least disagreement is fixed, a smaller representative relative to a later predecessor can still exceed that original parent. The upper bound on exceptional representatives in [the interval theorem](PAIRED_INTERVALS.md) controls neither this multiplicity nor the least representative of one particular component.

## Arbitrarily many earlier canonical implications

For a convergent pair put \(d(x)=J(x)-J(3x)+2\). Consider any path from \(z\) to \(3z\) on a varying positive affine family, built from ordinary edges in either direction and directed jumps \(y_i\to3y_i\) at canonical \(y_i<z\). Let \(j\) be the number of jumps, \(\ell\) the number of ordinary forward clocks minus backward clocks, and \(p\) the analogous net odd grade. The endpoint's leading coefficient is three times the start's, so
\[
                    3^{p+j}/2^\ell=3,\qquad \ell=0,\quad p=1-j.
\]
On any specialization where both ends of every jumped pair converge and \(z\) converges, summing (1) over ordinary segments and adding the actual jump charge differences gives the necessary identity
\[
                              d(z)=\sum_{i=1}^j d(y_i).                   \tag{4}
\]
At \(z=65\) every eligible \(y_i\) equals 17. Here \(d(65)=15\), whereas \(d(17)=2\). This rules out the whole class of contextual paths, even with arbitrarily many earlier jumps. The Lean induction proves the stronger parity statement that *any* such ordinary cut walk at this numerical control has odd net clock, whereas a contextual tripling identity would require zero. [Charge.lean](Charge.lean)

Conversely, suppose the numerical start \(z\) and its triple converge, and a finite list of numerical smaller canonical \(y_i\) has both arms convergent and meets (4). There is a contextual path through that specialization with precisely the specified jumps, upon restriction to an infinite arithmetic progression of larger inputs. To prove this, regard every affine edge slope as \(2^a3^b\). Travel from \(z\) to one using its first hit. For each \(y_i\) travel backwards from one to \(y_i\) along its first-hit word, jump to \(3y_i\), then travel forward to one. Finally travel backwards from one to \(3z\) along its first-hit word. The ordinary two-clock lap at one has slope \(3/4\), with exponent vector \((-2,1)\). Each jump loop contributes \(a+2b=d(y_i)\). For the initial and terminal segments together the contribution is \(2-d(z)\). Thus (4) says that the aggregate vector differs from the desired tripling vector \((0,1)\) by an integral multiple of \((-2,1)\). Insert forward or reversed laps at one to remove that difference exactly.

At each jump loop, insert enough forward laps at its initial one to make the coefficient of its query strictly below one relative to the original input. Insert the same number of reverse laps immediately after this loop's return to one. The total slope is preserved. At the supplied specialization every intermediate integer is positive, each query is smaller than \(z\), and both endpoints equal their stated values. Every intermediate affine expression has a positive rational slope. On an arithmetic progression through the specialization divisible by all finitely many branch, inverse-divisibility and canonical-residue requirements, the same path is physically legal. Its query slopes and starting inequalities retain strict original-source ordering on all larger representatives. Its endpoint has slope three and the correct value at the specialization, hence is exactly the triple throughout that progression.

For every convergent canonical pair with \(z>161\), three smaller seed queries suffice for this construction, with repetitions allowed. Their \(d\)-values at \(17,65,161\) are \(2,15,-12\). The values \(2,-12\) generate every even integer as a nonnegative sum; adding \(15\) then yields every odd integer. This proves that the obstruction in (4) is complete on convergent specialization data, and explicitly distinguishes global linear-word synthesis from the physical value of a hypothetical nonbasin. The [explicit generator](check_cut_walk.py) replays the actual positive path at each seed and three larger specializations. [Finite receipt](../../../reports/astra-sixhour-20261127/descent/cut-walk-finite.json) The construction uses ordinary access to one from the supplied seed. It gives no such access at a hypothetical nonperiodic bad original lower.
