# Excluding every mixed calendar whose two blocks contract

**PROPOSED written theorem, with a finite exact arithmetic certificate and one named external logarithmic-form estimate.** Use the primitive positive rational shortcut cycle, its full reduced denominator $d$, and the centered integer numerator $U_i=2a_i+d$ from [the modular-quotient theorem](MODULAR_QUOTIENTS.md). Suppose the entire parity calendar consists of $m\ge2$ consecutive blocks of length $s$, each a free bit followed by the **same** fixed tail of $s-1$ bits. Both free symbols occur. Let $v$ count the odd bits of the fixed tail and set $A=3^v$, $B=2^s$. The free-bit word can have arbitrary length, arrangement and Hamming complexity.

**All-contracting case.** If $3A<B$, every such cycle satisfies $d>1$. This excludes the whole family of positive ordinary cycles, at every period. More precisely, if $K$ is the positive centered carry of one block, then
$$
              d K>(m-1)(B-A)(B-3A).                              \tag{1}
$$
The result concerns blocks of different weights, including their arbitrary mixtures.

**Straddling case.** The only remaining positive mixed calendar has $A<B<3A$. Put $p=\log_3 2$ and $\delta=sp-v\in(0,1)$. For blocks ending at their smallest boundary state, the terminal run of small-slope blocks has length at least $\lfloor 1/\delta\rfloor$. If $v>0$, the resulting exact ternary divisibility gives
$$
 \log_2 d\ \ge\ v\log_2 3\,\lfloor1/\delta\rfloor-O(s+\log n),\qquad n=ms.
                                                                    \tag{2}
$$
The integer implicit in the divisibility is a nonzero return displacement from the small-block fixed point. There is no contracting-prefix assumption on the full physical word.

## Two contracting branches

Write $W_j$ for the positive centered integer at the start of block $j$. Since the free bit occurs first, the carry is independent of it:
$$
 B W_{j+1}=3^{b_j}A W_j+dK,\qquad
 K=\sum_{t=0}^{s-1}2^t3^{\,\sum_{t<i<s}b_i^{\rm block}}.
$$
Here the superscript on the last bits refers to a single block; positions $1,\dots,s-1$ belong to its fixed tail. The two maps are increasing strict contractions with distinct fixed points $L=dK/(B-A)$ and $H=dK/(B-3A)$. Every boundary lies strictly between $L$ and $H$. For example the minimum cannot lie below $L$ since either image of every state above that minimum is larger than it. If it equals $L$, its predecessor must also be $L$ and have used the small map. Iterating back around the entire cycle would force all bits to be small. The maximum has the analogous strict upper bound.

Immediately after the free bit the centered numerator is $(3^{b_j}W_j+d)/2$. Hence the span of these $m$ post-bit centered numerators is strictly less than
$$
 \frac{3H-L}{2}=\frac{d K B}{(B-A)(B-3A)} .
$$
They are $m$ distinct physical phases, with a common future of $s-1$ fixed bits. Their uncentered numerator differences are multiples of $2^{s-1}$ by literal dyadic coding, so their centered span is at least $(m-1)B$. This proves (1).

For given $s,v$, each term of $K$ increases when a fixed one moves to the right across a fixed zero: the affected suffix count increases, and all other suffix counts stay the same. Thus the largest carry occurs with the $v$ ones at the far right. Direct summation gives
$$
       K\le K_{\max}=2^{s-v+1}3^v-3^v-2^s<2B(3/2)^v.             \tag{3}
$$
For all positive integers $s$ and $0\le v<s$ such that $3^{v+1}<2^s$, we claim
$$
                  (B-A)(B-3A)\ \ge\ K_{\max}.                   \tag{4}
$$

For $1\le s<256$ this is a finite exact integer comparison. The [certificate](check_block_carries.py) checks every admissible pair with literal powers. Its only equality is $(s,v)=(2,0)$, where both sides equal three. For $s\ge256$ put $\lambda=s\log 2-(v+1)\log3>0$. Lagarias's Lemma 2.2(1) gives $\lambda\ge(\log3)/(1200s^{13.3})>1/(1200s^{14})$. Using $1-e^{-\lambda}\ge\lambda/2$ for $0\le\lambda\le1$, and $1-e^{-\lambda}>1/2$ otherwise, we get $B-3A\ge B/(2400s^{14})$. Also $B-A>2B/3$. Since $p>3/5$ (equivalently $2^5>3^3$) and $v<sp$, we have
$$
       (3/2)^v<2^{(1-p)s}<2^{2s/5}.
$$
Therefore (4) is strict as soon as $2^{3s/5}>7200s^{14}$. On $2^{8+j}\le s<2^{9+j}$ the base-two logarithm on the right is less than $139+14j$, while $(3/5)2^{8+j}>139+14j$ for $j\ge0$. The case $j=0$ and monotonicity under the dyadic step prove the last assertion. This proves (4) at every $s$. Together (1)–(4) imply $d>m-1$, in particular $d>1$. For $s\ge256$ the sharper lower bound is
$$
            d>(m-1)\,2^{3s/5}/(7200s^{14}).
$$


The small and intermediate range also has a compact proof certificate. Direct comparison is needed only for $1\le s<18$. The exact powers $3^{306}<2^{485}$ and $2^{84}<3^{53}$ give $306/485<p<53/84$. For $18\le s\le255$ put $k=v+1$. From $k<sp$ we get $84k<53s$, whence
$$
 sp-k>\frac{306s}{485}-k
 \ge\frac1{84}-\frac{s}{84\cdot485}>\frac1{200}.
$$
Thus $B-3A\ge B/400$ by the exponential inequality used above, and the ratio of the left side of (4) to $K_{\max}$ exceeds $2^{3s/5}/1200>1$ already at $s=18$. The last inequality follows from $2^{54}>1200^5$. [ContractingCalendar.lean](ContractingCalendar.lean) contains candidate kernels for the short range, both power comparisons and the intermediate rational gap. The independent exact Python comparison covers all 20,465 pairs below 256.

## The backward run at the boundary minimum

If $A\ge B$, both maps increase every positive input, contradicting a return; equality of the powers cannot occur. Thus the remaining case has $A<B<3A$ and $v=\lfloor sp\rfloor$. Let $W_0$ be the least boundary and take the last occurrence of a large branch before it. It is followed by $L$ small branches. The homogeneous multiplier across this entire terminal arc, including the large branch, is $3(A/B)^{L+1}$. The affine forcing is positive and the initial boundary is at least $W_0$. Hence $3(A/B)^{L+1}<1$, or $L+1>1/\delta$. This proves $L\ge\lfloor1/\delta\rfloor\ge1$.

Define $Y_j=(B-A)W_j-dK$. It is nonzero at $j=0$: if $W_0$ were the small-map fixed point, its preceding small branch would have the same input, contradicting least physical period. In fact $Y_0>0$ by the same lower-endpoint argument as above (the large map exceeds its input in this case). Along a small branch $B Y_{j+1}=A Y_j$. Coprimality of $A$ and $B$ now gives
$$
       A^L\mid Y_0,\qquad A^L\le Y_0 < B W_0 .                  \tag{5}
$$
This uses *the ending boundary*, which is small; taking the difference at an arbitrary high start of the run would lose that control. Some boundary lies fewer than $s$ physical steps after the global minimum. The elementary growth $x_{i+1}+1\le(3/2)(x_i+1)$ gives
$$
              W_0\le 2d(3/2)^s(x_*+1).
$$
Insert this in (5) and use $x_*<600n^{14.3}$ as in the modular-quotient theorem to obtain (2). The finite divisibility (5) and the run length do not need a linear-forms estimate. When $s$ is a lower record with particularly small $\delta$, (2) strengthens the local dictionary estimate. A nontrivial ordinary cycle in a one-variable-column calendar would have to lie in this straddling case and pay both bounds. The case $s=1$ already includes the unrestricted binary calendar.

## Source and comparison

PR191, `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, `research/two-sided-cycle-packing-20261124/README.md`, TCP-1, bounds an equal-weight block dictionary by its fixed-point interval and common-tail spacing. PR212, `505d3fe782922904e86477990cc5d41e9110edda`, `research/astra-infinite-descent-20261127/cycles/ARC_HEIGHT.md`, proves dyadic and ternary divisibility for arbitrary reference arcs. We use their respective mechanisms with two *unequal* slopes sharing a centered carry, and at the terminal small-slope run forced by a true minimum. PR211, `4b44cded44af5bb7c3ce67fb16a70c898ad505d5`, `research/astra-reciprocal-rigidity-20261127/cycles/phase10/RECORD_TYPES.md`, concerns criticality of the *full period*. The record gap in (2) belongs to the shorter block length $s$.


**Earlier qualitative implication.** PR191 at the same pin, TCP-3, already proves that no atom of an equal-length all-contracting dictionary can repeat around an ordinary primitive cycle. It uses PR177, `25bf9b95a9404998e8e55aa401773488cd3dd4b8`, `research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md`, TS5/TS6. A two-atom mixed dictionary would thus have exactly two blocks and exactly two mismatches at the block shift. PR212 at the pin above, `cycles/ALL_SHIFT_HEIGHTS.md`, excludes fewer than 42 mismatches at every proper shift of a nontrivial ordinary cycle using the published Hercher–Bařina computational and period inputs. Those two earlier claims already imply the qualitative nontrivial-cycle exclusion. Equation (1), its explicit rational-denominator consequence and the direct proof independent of a computational Collatz verification floor are the present additions. The straddling-case endpoint bound (5) has separate scope.

The uniform tail of (4) and the period-only form (2) use the external logarithmic-form estimate in [Lagarias, Lemma 2.2(1)](https://arxiv.org/abs/math/0512006); the finite comparison is recorded separately. None of these inputs supplies an exclusion when the two block slopes straddle one at general $s$.
