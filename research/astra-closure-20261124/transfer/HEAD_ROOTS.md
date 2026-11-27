# The actual head-root discrepancy and its clock labels

Let $T$ be the positive shortcut map. Let $R=81^j$, $d=\log_2R$, $x\in[7R,8R)$ and $m=\lfloor x/81\rfloor$. Write $P_M(n)$ for the first ordinary iterate at most $M$, and leave it undefined when no such iterate exists. Defining it via strict inequality changes only the endpoint conventions. The two arms may use independently chosen clocks.

**Theorem 1 (written).** For every fixed $\log_2\sqrt3<\alpha<1$, the number of $x$ with defined, unequal first-passage roots $P_{R^\alpha}(x)\ne P_{R^\alpha}(m)$ is
$$
                     \Theta_\alpha(R/\sqrt j).                                     \tag{1}
$$
A single subset of size $\gg_\alpha R/\sqrt j$ has **defined and unequal** roots for *every real* $M\ge R^\alpha$ simultaneously. The lower bound uses elementary arithmetic and the reflection principle. The upper bound imports the finite-grid affine fusion bound from [PR146](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md), in the normalization spelled out in [PR197](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/MACROSCOPIC_PAIR_CLOSURE.md). The sharpness is for actual landing integers in this specified power range, independent of their later components.

**Proof of the lower bound.** Fix any one remainder $0\le r<81$ and write $x=81m+r$. Choose $0<\lambda<1$ close enough to one and a fixed $\eta>0$ small enough that
$$
          1+\lambda[(1/2+\eta)\log_2 3-1]<\alpha .
$$
Take $b=\lfloor\lambda d\rfloor$. In a complete grid of $m\bmod2^b$ consider the first $b$ steps on both arms. Write $p_n(i)$ for the number of odd inputs before clock $i$ and put $D_i=4+p_x(i)-p_m(i)$. Given the low $i$ bits of $m$, the parity of each arm at clock $i$ is a fair bit as the next binary digit varies. Both affine coefficients of that bit are odd. Hence the earlier digits determine whether the two parities agree. If they agree then $D_{i+1}=D_i$, and if they differ its increment is an equiprobable sign.

One can expose separate independent fair coins for a mixed step and an agreeing step, choosing the stream before looking at the next bit. At mixed steps use the next fair sign to choose the unique bit producing that sign. At agreeing steps use a coin from the other stream. This samples exactly the uniform word. A simple symmetric walk started at four and driven by the mixed-sign stream remains strictly positive through its first $b$ moves with probability $\gg1/\sqrt b$. For example, starting at one only decreases this survival probability, and reflection gives $2^{-b}\binom{b}{\lfloor b/2\rfloor}$ at one. Since at most $b$ mixed steps take place by physical clock $b$, at least this proportion has $D_i>0$ at every $0\le i\le b$. No assumption on the physical waiting times, or on parities after the native precision, enters this estimate.

On a fixed low residue write $m=2^b q+s$. The affine lifting identity for the $i$th child and $k$th parent iterates shows that their slopes as functions of $q$ are
$$
          81\,2^{b-i}3^{p_x(i)},\qquad 2^{b-k}3^{p_m(k)} .
$$
The counts are constant over these lifts. Equal slopes require $i=k$ by their powers of two, followed by $D_i=0$ by their powers of three. Neither is possible jointly on our chosen residues. Thus for each $(i,k)$, ordinary equality holds for at most one $q$. Removing at most $(b+1)^2 2^b$ ordinary parents removes **every** possible collision through the two independent clocks $0\le i,k\le b$. The interval of parents has length $R/81+O(1)$. Incomplete-grid error is $O(2^b)$, and both discarded errors are $o(R/\sqrt b)$ because $\lambda<1$. The local Lean theorems `affine_lift` and `unique_affine_collision` check the lifting and uniqueness formulas used here.

It remains to ensure both passages occur by $b$. For either arm, if its first $b$ inputs exceed $R^\alpha$, its endpoint is at most
$$
 8R\,3^{p_n(b)}2^{-b}\exp(b/(3R^\alpha)).
$$
For $p_n(b)\le(1/2+\eta)b$ the endpoint is below $R^\alpha$ by the strict choice of parameters. The proportion violating the count bound is exponentially small in $b$ on complete grids. For the child this uses that $m\mapsto81m+r$ permutes the binary residues. The incomplete grid contributes $O(2^b)$. Removing both arm exceptions has total cost $o(R/\sqrt b)$. The remaining pairs have both first clocks for every $M\ge R^\alpha$ at or before $b$, yet their two complete orbit segments through $b$ are disjoint. This proves the simultaneous lower bound with only one remainder $r$.

For the upper bound take $b'=\lfloor(1-\alpha)d/2\rfloor$. Both starting values exceed $cR$ for an absolute $c>0$, and neither arm can decrease by more than a factor two per step. Thus both stay above $R^\alpha$ through clock $b'$ for all sufficiently large $R$. The cited finite-grid fusion result bounds failure to meet by this clock for $m,3^4m+r$ by $O(1/\sqrt{b'})$ of the grid. Count all 81 remainders, with $O(81\cdot 2^{b'})$ endpoint error. After meeting above the barrier the arms have the same future, so any defined first roots are equal. This proves (1).

The normalized lower bound in (1) is not summable over $j$. It persists if every positive integer reaches one. PR199 asks for failures of **component** equivalence and permits a polylogarithmic barrier. Replacing that test by literal equality at these higher barriers would impose a false summability condition.

## Decoding the two stopped clocks at a polylogarithmic barrier

**Theorem 2 (written).** Let both actual first passages below the common threshold $M$ occur by clock $H\ll d$, with $M\le R^{.98}$ and $M/d^{14.3}\to\infty$. Write $v=P_M(x), w=P_M(m)$ and let $t,s$ be their respective first clocks. The pair $(v,w)$ uniquely determines the two integer differences
$$
                     4+p_x(t)-p_m(s),\qquad s-t                                  \tag{2}
$$
among the admissible clock range. Thus literal equality forces $t=s$ and $p_m(s)=p_x(t)+4$. For fixed $v$, all possible $w$ lie in the union of $O(H+1)$ intervals of length $O(H+1)$, regardless of how many original head inputs give the same $v$. The row-support bound uses elementary arithmetic alone. Decoding uses [Rhin's phase-gap theorem as pinned by PR199](https://www.proofatlas.ai/formalizations/rhin-phase-gap-log2-three/), with the exponent $13.3$ also given in [Simons and de Weger, Lemma 12](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf). This external Diophantine input is source-qualified.

As a direct application, for every fixed $A>1$ choose $D$ sufficiently large for [PR197's first-passage theorem](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md) and $D>14.3$. Then the description applies away from $O_A(Rd^{-A})$ original head inputs at $M=d^D$. A larger $D$ in that proof preserves the timely conclusion. For its strict threshold convention use that convention for both arms. Every retained row contains $O(d^2)$ possible integer columns in a band containing $\asymp M$ possible integers.

**Proof.** Before the respective first crossings, every shortcut input exceeds $M$ (at least $M$ in the strict convention). The exact product corrections on the two arms lie in $[1,\exp(H/(3M))]$. The initial ratio differs from 81 by $r/m=O(1/R)$. Set $a=4+p_x(t)-p_m(s)$ and $k=s-t$. Then
$$
     |\log_2(v/w)-a\log_2 3-k|\le C[(H+1)/M+1/R].                              \tag{3}
$$
Both roots lie between $M/2$ and $M$, inclusive up to the endpoint convention. Thus for each of the $O(H+1)$ candidate $a$, only $O(1)$ values of $k$ can satisfy (3). At fixed $(v,a,k)$ the allowed $w$ form one interval of length $O(H+1+M/R)=O(H+1)$. This is a deterministic restriction on the support of the actual stopped pair. No factorization of its law was used.

Two distinct candidates with different $a$ give linear forms separated by $\gg (H+1)^{-13.3}$, by the phase-gap input; those with the same $a$ differ by at least one. Since $H\ll d$, the tolerance in (3) is $o((H+1)^{-13.3})$. This proves unique decoding, including when $H$ stays bounded. For $v=w$ the zero candidate fits (3) identically, so uniqueness forces both differences to vanish (one may include zero in the bounding rectangle even if that candidate is unobserved).

The restriction does not make the remaining $O(d^2)$ columns of a row equivalent to its root. Nor does it bound the true multiplicity of off-component pairs within those columns. The sparse support and the all-components return comparison are compatible with an unbounded trajectory reappearing after its first entrance to a fixed small floor.

## The same-source pair law is asymptotically singular relative to its own product marginals

Use the preceding PR197 choice of $H,M$, for which the children with **both** passages timely number $(1-O_A(d^{-A}))R$. Condition on this set. Write $J$ for its empirical joint probability law over the original head sources and $J_1,J_2$ for its two marginals. Then
$$
 d_{\rm TV}(J,J_1\otimes J_2)\ge1-O((H+1)^5/M),\qquad
 I_J(v;w)\ge\log M-5\log(H+1)-O(1).                                  \tag{4}
$$
These bounds use the elementary row-support estimate and the physical first-passage fiber estimate in PR197. Rhin's separation is unnecessary for (4).

For an arbitrary cap $H$ under Theorem 2, use the following mass-dependent form instead. Choose **any selection** of the timely original children of size at least $pR$, with $0<p\le1$, and give it the uniform law. The conclusions persist with $(H+1)^5/M$ replaced by $(H+1)^5/(pM)$ in the probability deficit, and with $\log p$ added to the entropy lower bound. The selection may remove every equal-root pair. The estimate is informative when the displayed ratio is small. It imposes no lower bound on the size of a set selected by eventual basin behavior.

For a fixed parent-arm endpoint $w$ and fixed clock and odd count, any two corresponding actual parents $n_1\le n_2$ satisfy $n_2/n_1\le\exp(H/(3M))$, by cancellation in their two exact product formulas. Each such fiber has $O(1+HR/M)$ parents. At most $(H+1)^2$ clock/count pairs occur, and there are at most 81 children per parent. As $M\le R$ and $H\ll M$, a single second-coordinate atom therefore has probability $O((H+1)^3/(pM))$ on the selected children. The same argument holds on the first coordinate. Let $S$ be the deterministic relation of admissible slope windows in (3). Every selected ordered pair belongs to $S$. Each of its rows has at most $C(H+1)^2$ columns. The product of the two **selected** marginals assigns at most $C'(H+1)^5/(pM)$ to $S$. Taking the difference on this event proves the variation bound. The second marginal's entropy is at least minus the logarithm of its largest atom. Conditional on any first root its entropy is at most $\log(C(H+1)^2)$. Subtraction proves the information bound with natural logarithms.

The conditioning factor is necessary at an arbitrary cap. For example, take $H=\lfloor d/2\rfloor$, let $X$ be the least multiple of $81\cdot2^H$ at least $7R$, and take $M=X/2^H$. The pair $(X,X/81)$ is timely because both starting values are multiples of $2^H$. For large $R$, $X<8R$. A timely child must use exactly $H$ even steps: an odd step would put the endpoint at least $3\cdot7R/2^H>M$, and an earlier all-even arrival would put it at least $14R/2^H>M$. The child must therefore be a multiple of $2^H$ in $[7R,X]$, leaving at most 82 possibilities. Its conditional mutual information is bounded by $\log 82$ even as $M\asymp\sqrt R$ grows. This example credits the packet's independent arithmetic review.

For the full empirical distribution use a cemetery value if a passage fails, retaining any late but defined first roots. Couple it to the timely conditional law by redrawing only exceptional samples. The joint laws differ in variation by $O_A(d^{-A})$, as do each pair of marginals; the corresponding products differ by at most twice this error. Thus the unconditional joint and product have total variation at least $1-O_A(d^{-A}+d^5/M)$. With the specified choice of $D$ the deficit is summable over $j$. This quantifies the error in a product replacement even though it leaves the actual mass of edges between different components open.

## Narrower rows from sliding windows and centered prefix counts

For any fixed $A>1$, enlarge $D$ in the PR197 application if needed. Except on $O_A(Rd^{-A})$ original sources, the actual ordered root has
$$
 |a|+|k|\ll_A\sqrt{d\log d},\qquad
 |\log_2(v/w)-a\log_2 3-k|\ll_A (\log d)/M.                           \tag{5}
$$
Thus at each $v$ the regular relation now has $O_A(\sqrt d(\log d)^{3/2})$ possible columns. On this population formula (4)'s bound on the product mass of the relation improves to $O_A(d^{7/2}(\log d)^{3/2}/(pM))$ after an original-source selection of mass at least $p$. The coarse relation (3) holds for every timely pair, including sources outside this refinement.

To prove the first bound, augment the binary tests in PR197's [first-passage proof](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md). Its successive thresholds $Y_i$ have geometrically decreasing logarithms and its block sizes are $l_i=\lfloor\log_2(Y_i)/2\rfloor$. For each such block include the failure of
$$
             |p_u-u/2|\le C_A\sqrt{l_i\log d}\qquad(0\le u\le l_i).
$$
On a complete binary grid its probability is at most $2(l_i+1)d^{-2C_A^2}$ by Hoeffding with natural log in the bound. It depends only on the first $l_i$ bits. At a noninitial $Y_i$ the PR197 first-entrance fiber estimate (3) costs $O(d^3)$ times that grid probability as a fraction of **original sources**, including actual first passages up to its clock cap; the initial block has bounded grid-cover cost. There are $O(\log d)$ stages, so choosing $C_A$ large gives the claimed exception. Every actual partial stage through the first $M$ passage has length at most $l_i$ on PR197's good population. Their centered counts add, giving
$$
                  p_n(t)=t/2+O_A(\sqrt{d\log d})
$$
since $\sum_i\sqrt{l_i}\ll\sqrt d$. Apply this on both arms. Their starting heights and their respective landing heights are each pairwise within fixed factors. The exact logarithmic product formulas, with drift $1-(\log_2 3)/2>0$ per shortcut clock, now give $|s-t|\ll_A\sqrt{d\log d}$ and then $|4+p_x(t)-p_m(s)|\ll_A\sqrt{d\log d}$.

For the improved tolerance use PR197's actual sliding window conclusion, with window length $b\asymp_A\log d$. Any full $b$ steps before the first $M$ crossing multiply the current height by at most
$$
       2^{-b}3^{.525b}\exp(b/(3M))\le 2^{-c b}
$$
for an absolute $c>0$ and all sufficiently large $d$. Looking backwards from the crossing, partition the pre-crossing input times by their distance modulo $b$ from the final pre-crossing block. Each backward jump by $b$ raises the input by at least $2^{c b}$, and each final pre-crossing input is at least $M$. Therefore $\sum_{i<t}1/T^i(n)\le b/[M(1-2^{-cb})]$. The two logarithmic additive corrections in (3) are consequently $O_A((\log d)/M)$ as asserted. Counting admissible exponents and integer columns gives (5)'s row bound. This controls the allowed differences on actual sources, without describing their conditional distribution.

In particular an unconditioned irrational-rotation model for $a$ cannot supply such a distribution: the finite-grid affine-fusion argument for Theorem 1, run for $\lfloor d/2\rfloor$ steps, merges the two paths above this polylogarithmic barrier off $O(R/\sqrt d)$ inputs. On those fused paths which reach $M$ in the stated clock cap the decoded pair is exactly $(a,k)=(0,0)$. The arithmetic weights on the remaining, unresolved population are unknown. [Conditional source coupling, paper 13, Theorem 8](https://rstation.ai/problems/collatz/papers/13) treats prescribed affine offsets in a specified survival law and binary source window. Its clocks and conditioning do not give a relative mixing theorem for the actual two stopped head roots.

The same estimates improve the **marginal** atom bound on this regular population. In fact for a fixed parent root $w$, comparison with the known parent interval and $M/2\le w\le M$ gives
$$
 s=\frac{\log_2(R/M)}{1-(\log_2 3)/2}+O_A(\sqrt{d\log d}+1)
$$
by the first-prefix deviation just proved. There are $O_A(\sqrt{d\log d})$ choices of the clock. At any fixed $s$, $p_m(s)$ has only $O(1)$ choices, since $m$ ranges over a fixed-ratio interval and the product correction is $\exp(O_A((\log d)/M))$. For a single $(s,p_m(s),w)$, that last correction restricts the largest parent divided by the smallest to $1+O_A((\log d)/M)$. The fiber consequently contains $O_A(1+R(\log d)/M)$ parents. Each parent accounts for at most 81 children. The same reasoning applies to child roots. The maximum atom of either selected marginal is therefore $O_A(\sqrt{d}(\log d)^{3/2}/(pM))$.

Multiplication by (5)'s row bound gives the stronger conclusion
$$
 (J_1\otimes J_2)(S_{\rm regular})\ll_A \frac{d(\log d)^3}{pM},
 \qquad I_J(v;w)\ge\log(pM)-\log d-3\log\log d-O_A(1).                \tag{6}
$$
Here $J$ is any uniform selection of $\ge pR$ regular original children. Ordinary variation transfers back to the full empirical law with $O_A(d^{-A})$ error as before. The root-relation estimate applies uniformly to all rows, without a lower bound for each row weight.

## Verification boundary

`PhysicalReturn.lean` imports only `Std`. With official Lean 4.34.1 and warnings as errors, its five printed public declarations used only `propext`, `Classical.choice` and `Quot.sound` in aggregate. The product-relation theorem counts actual marginal multisets sampled with replacement, so repeated roots preserve their multiplicities. The analytic estimates, first-passage comparison and irrationality measure were not formalized in this module.

`python -B controls.py` and `python -B -O controls.py` gave the same results. The bounded checks tested the ballot lower bound over 165,726 low-binary head profiles through depth ten. At 81 distinct ordinary parents at scale $R=81^{40}$, one for each remainder, integer-only candidate separation recovered every pair of clock and odd-count differences at floor $2^{60}$; 43 of the first roots were equal. The test checks finite identities and does not estimate an asymptotic frequency.
