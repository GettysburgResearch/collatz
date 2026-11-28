# The zero endpoint of the ordinary preminimum correction

**Source-qualified written theorem.** The main input is Weaver's retained-block proof of the uniform ordinary landing floor. It retains an absolute real offset bound in addition to its multiplier bound. The minimum and the real correction use the natural-history identification in the source packet. The results below concern original positive integer orbits. [Weaver, Paper 12, Lemma 13 and proof of Theorem 14](https://rstation.ai/problems/collatz/papers/12) · [Natural preminimum real law](REAL_FIBRE_LOG_GAUGE.md) · [Power bound for actual first landings](RAW_LANDING_MOMENTS.md).

Use the odd map $U(n)=(3n+1)/2^{v_2(3n+1)}$. Let $m(n)$ be the attained minimum on its infinite orbit, $\tau(n)$ its first occurrence, and put
\[
 R(n)=\sum_{0\le j<\tau(n)}\log_2(1+1/(3U^jn)).
\]
Write $\nu$ for the natural limiting law of $R$ and $D(Y)$ for the relative odd density of $m(n)>Y$. The natural law over all integers is the same, by decomposing an integer into its odd part and initial power of two. Let $\mathcal M$ denote the positive odd ternary units whose forward orbit never goes below its starting value, and $N(Y)=\#(\mathcal M\cap[1,Y])$. Two unbounded ordinary orbits are in the same escaping component when they eventually meet. An unbounded orbit has no repetitions and tends to infinity.

There are positive absolute $a,b$ such that, for all sufficiently large integers $Y$,
\[
 \nu([0,b/Y])\ \ge\ a N(Y)/Y.                                      \tag{1}
\]
If there are $q$ distinct escaping components, with any finite $q$ allowed when they are infinite in number, this implies
\[
 \liminf_{t\downarrow0}\frac{\nu([0,t])}{t\log(1/t)}\ge c q.           \tag{2}
\]
In particular a subsequence with $\nu([0,t])=o(t\log(1/t))$ excludes every escaping orbit. A subsequence with $\nu([0,t])=O(t)$ forces $\mathcal M$ finite and every positive integer eventually enters one of finitely many cycles. Neither endpoint upper estimate is presently proved.

## A counted ordinary minorant with a small correction

For any unit $m\le Y$, Paper 12 constructs a single direct odd predecessor $r$ of $m$ with $2KY-1/3\le r<C_bY$, for absolute $K,C_b$. It counts at least $cX/Y$ odd sources in $(X/4,X]$, for all $X\ge C'Y$, with first landing below $Y$ at $m$ through this $r$. All intermediate odd states exceed $Y$. Crucially the earlier path from a selected source $x$ to $r$ uses an affine multiplier $A_k$ and offset $0\le B_k\le B_0$, for an absolute $B_0$, with $r=A_k x+B_k$. Its physical survival is exactly $A_k x/r=1-B_k/r$, the product of $3z/(3z+1)$ over departed odd states. The last step from $r$ to $m$ multiplies survival by $3r/(3r+1)$. The full base-two log correction to first landing is at most
\[
 -\log_2(1-B_0/r)+\log_2(1+1/(3r))\le b/Y.                           \tag{3}
\]
If $m\in\mathcal M$ this landing is the first occurrence of the global minimum. These counted sets are disjoint over distinct $m$. Normalize by the number of odds in the source annulus, then let $X$ tend to infinity. Weak convergence gives the lower bound on the closed interval in (1). For each particular $m$, its natural minimum cell similarly has mass at least $a/Y$ in that interval for every $Y\ge m$ above the absolute onset. The primary count comes from Paper 12's written selected-block and joint oscillation inputs, without a new independent proof of those inputs.

Every escaping orbit, after discarding its first state if needed, consists of units. Take the minimum $y_0$ of its future tail, then the minimum $y_1$ of the tail after that occurrence, and continue. They are strictly increasing members of $\mathcal M$. Since $y_{i+1}\le U(y_i)\le(3y_i+1)/2$, one has $y_i+1\le(3/2)^i(y_0+1)$. Each chosen component supplies at least $\log Y/\log(3/2)-O_{y_0}(1)$ distinct labels through $Y$. Distinct components supply disjoint labels. Substitute in (1) at $Y=\lceil b/t\rceil$ to prove (2). If the ratio $\nu([0,t])/t$ is bounded along a subsequence, the same substitution bounds the nondecreasing $N(Y)$ there. Each positive cycle supplies its least odd label to $\mathcal M$ and distinct cycles are disjoint. An escaping orbit would supply infinitely many members. These facts prove the finite-attractor implication.

## Upper control on the same labels and endpoint

Apply the first-landing lower count separately at the own floor of each $m\in\mathcal M$. For arbitrary finite sets of such $m>Y$ the resulting minimum events are disjoint and included in $\{m(n)>Y\}$. Thus
\[
 \sum_{m\in\mathcal M,\ m>Y}1/m\ll D(Y)\ll_\eta Y^{-g\eta},\qquad
 g=1-H_2(\log_3 2)+1/351,\quad 0<\eta<1.                              \tag{4}
\]
The same disjoint minimum cells give $\mathbb E_{\rm nat}m\ge a N(Y)-O(1)$ for every $Y$, by multiplying their own-floor mass floors by their labels. Thus the limiting minimum has finite first moment exactly when $\mathcal M$ is finite, equivalently when all orbits enter finitely many cycles. For the converse, each finite cycle family bounds all global minima by the maximum of its cycle minima. When $\mathcal M$ is finite the only other possible minimum labels are nonunit starting sources, each of natural mass zero. Tightness of the limiting minimum law excludes mass escaping through those labels. This statement is about a moment of the limiting distribution. Convergence of untruncated finite-source arithmetic means does not follow from weak convergence alone.

Summation over dyadic shells gives $N(Y)\ll_\eta Y^{1-g\eta}$. Moreover a preminimum state $z\le Y$ incurs at least $\log_2(1+1/(3Y))$. Consequently, if $R$ is smaller, either the minimum exceeds $Y$ or first landing at $Y$ equals the minimum. The latter is a unit apart from a source already equal to its own nonunit minimum at most $Y$, a set of zero natural density. This implication is literal at finite sources. To pass to the limiting law, bound the smaller closed interval $[0,b'/Y]$ by the open interval $(-1,\log_2(1+1/(3Y)))$ for a sufficiently small absolute $b'>0$ and use the open-set weak-convergence inequality. We obtain
\[
 \nu([0,b'/Y])\le D(Y)+\mu_Y(\mathcal M\cap[1,Y])\ll_\epsilon Y^{-g+\epsilon} \tag{5}
\]
from (4) and the arbitrary-set estimate in the linked raw landing moments, taking its independent exponents sufficiently close to one. This controls a distinguished endpoint of the law but leaves a substantial gap to (2).

## A disjoint family controlled by the true cemetery

Choose one forward unit ray $(r_{C,j})_{j\ge0}$ in each escaping component $C$. At floor $Y$ use indices strictly after its last visit to $[1,Y]$, or every index if there is no such visit. For every retained $r=r_{C,j}$, let $z=4r+1$ if that is a unit and $z=16r+5$ otherwise. Then $r<z\le21r$ and $U(z)=U(r)$. Both candidates cannot be nonunits, since the second is four times the first plus one. The sibling $z$ is off its entire ray: equality to any $r_{C,i}$ would force $r_{C,i+1}=r_{C,j+1}$, hence $i=j$ and $z=r$. The siblings are distinct, and no sibling lies in the future of a different one, since each moves immediately onto its own ray. Thus their first-landing-at-own-floor events are pairwise disjoint even though the floors differ. Every point in such an event stays above $Y$ for its whole future. Using the first-landing floor at $z$, taking arbitrary finite subsets first, gives
\[
 \sum_C\sum_{j\text{ retained at }Y}\frac1{r_{C,j}}\ll D(Y).           \tag{6}
\]
For each selected ray starting at most $Y$, the first state after its last visit below the floor is at most $(3Y+1)/2$. Hence $Y D(Y)\gg\#\{C:r_{C,0}\le Y\}$. A single escaping component implies a logarithmically growing truncated first moment of the global minimum, by integrating $D(Y)\gg1/Y$. The double sum covers only states after last exit. It places no such restriction on earlier high excursions.
