# Five products with unrestricted odd divisions

Every positive odd \(L\)-step Collatz segment of minimum \(H>2^{8(L+1)^2}\) has distinct products on all five-element index multisets, including multisets with repetitions. No bound on the individual or total number of divisions is needed.

Use the [triple-product argument](UNRESTRICTED_TRIPLE_PRODUCTS.md) and its [four-product sign test](UNRESTRICTED_FOUR_PRODUCTS.md). Given a collision, cancel common indices, trim to its first and last surviving indices, and orient signs with \(c_m>0\) at the last index. Keeping the original \(L\) in all thresholds is valid. Equal index and clock sums hold at the stated height. Write \(h\le5\) for the common remaining cardinality. Index alignment forces \(c_m<h\), and every \(3\nmid c_m\) is already covered by the ternary prefix congruence. The case \(h\le4\) is also settled. Thus consider \(h=5,c_m=3\).

In reverse order the cumulative coefficients \(d_b=\sum_{i\le m-1-b}c_i\) start at \(-3\). As an index of the negative multiset is crossed, \(d_b\) increases by its multiplicity. Crossing a positive index decreases it. There are only two positive units outside the terminal index, against five negative units. If the nonzero signs consist of negatives followed by positives, the four-product sign test applies without a change.

In the remaining case the sequence reaches a positive value and later a negative one. The first traversal from \(-3\) to a positive value uses at least four negative units. The subsequent traversal from positive to negative uses at least two preterminal positive units, exhausting the entire positive budget. Consequently the first positive value is \(1\), and until the subsequent first negative value the sequence stays between \(-1\) and \(1\). Reaching \(2\) there would require at least three positive units to return below zero. At the subsequent first negative value both positive units have been spent and the value is exactly \(-1\). At most one negative unit remains, so every subsequent value lies in \(\{-1,0\}\). In particular **all nonzero coefficients starting at the first positive value are odd**.

The weighted partial sums \(G_j=\sum_{b\le j}d_b3^b2^{-E_b}\) are strictly negative before that first positive value, since all summands there are nonpositive and \(d_0<0\). For a later prefix, take its last nonzero index \(v\). The numerator \(2^{E_v}G_v\) is odd: the last summand contributes \(d_v3^v\), and every earlier one has the positive power of two \(2^{E_v-E_b}\). Any trailing zero entries preserve this nonzero value. Thus every weighted prefix is nonzero, even though \(3\mid d_0\).

The integral prefix bound \(|G_j|\ge2^{-E_j}\), the first-large-gap estimate and the polynomial root exclusion now give exactly the previous sufficient threshold
\[
 H>\max\{8kL3^{kL},\,2^{LM+2+k(L+2)}\},\qquad
 M=2L+\lceil\log_2(2kL)\rceil,\quad k=5 .
\]
Indeed \(10L\le2^{L+3}\) for \(L\ge1\), so \(M\le3L+3\). The exponent \(LM+2+5(L+2)\) is at most \(3L^2+8L+12\le8(L+1)^2\); the other threshold is smaller than \(2^{8(L+1)^2}\) as well.

Weaver's bounded-division all-order result allows the first correction to vanish, and its five-fold example does so. That example lies in the single-crossing case, where convexity rules out a positive root even if a prefix vanishes. The present parity argument concerns the other sign pattern. [Weaver, Paper 163, §§3, 6](https://rstation.ai/problems/collatz/papers/163)

At order six the numerical reverse coefficients can begin \((-3,-1,1,2)\). For reverse division gaps \((1,2,1)\) their weighted prefix is exactly \(-3-3/2+9/8+2\cdot27/16=0\). This sign-and-parity proof cannot automatically be extended across such prefixes.
