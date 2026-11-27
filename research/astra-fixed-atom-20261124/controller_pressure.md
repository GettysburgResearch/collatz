# Testing cumulative contraction in the critical steering controller

The three-switch theorem finds a locally contracting edge at every positive critical input. I tested whether repeating those switches and restarting forces a net decrease. For the controller specified below, even an arbitrarily long search need not find a contracting product on a set of positive ternary Haar measure. The same estimate accommodates accumulated real affine offsets. It does not produce a positive integer whose controller search fails.

Write the shifted ordinary state as \(a=6k+2\) and use \(L=4k+1=(2a-1)/3\). The change from \(k\) to \(L\) preserves probability Haar measure on \(\mathbb Z_3\). In the two nonterminal classes the available switches are

| Guard | New \(k\) | New \(L\) |
|---|---|---|
| \(k=3m\) | \(4m\) or \(32m+2\) | \((4L-1)/3\) or \((32L-5)/3\) |
| \(k=3m+1\) | \(8m+3\) or \(16m+6\) | \((8L-1)/3\) or \((16L-5)/3\) |

If \(k\equiv2\pmod3\), write \(L=3^r u\) with \(r\ge1\) and \(3\nmid u\). Apply the sibling correction to \(2a-1=3L\). Its fully normalized shifted value is \(p_0=2^{r+1}u\) and the other available sibling is \(p_1=2p_0\). The two are component-equivalent to \(a\). Indeed the ordinary shifted identities \(2v\sim3v\) and \(2v-1\sim v\) give \(a\sim 3L\sim p_0\); writing \(a=2v\), the sibling identity \(2v\sim8v-2=2(2a-1)\) likewise gives \(a\sim p_1\). Exactly one of these two even units is \(2\bmod6\). Let \(\epsilon\in\{0,1\}\) select it, so \(2^{r+\epsilon}u\equiv1\pmod3\). One can stop at \(p_0\) without a restart or continue at the critical state \(2^\epsilon p_0\). Testing \(p_1\) as an additional terminal cannot detect a smaller state than \(p_0\).

For the continuing state the coordinate is
\[
 L'=\frac{2^{r+2+\epsilon}u-1}{3}
     =\lambda_\epsilon L-\tfrac13,\qquad
 \lambda_\epsilon=\frac{2^{r+2+\epsilon}}{3^{r+1}}.
\]
The trial exit \(p_0\) in the same coordinate is \(\lambda_0L-1/3\), whether or not it is critical. The exceptional ternary point \(L=0\) and its finite preimages under the controller form a null set. Each \((r,\epsilon)\) has one guard residue modulo \(3^{r+1}\); each nonterminal class has Haar mass \(1/3\). On its guard each continuing affine map sends the conditional Haar distribution to Haar distribution: after removing the fixed ternary digits its remaining slope is a power of two, a ternary unit. Consequently a specified finite history has cylinder mass equal to the product of its guard masses. Different alternatives at a nonterminal guard can overlap in initial inputs. The bound below sums over them, allowing that overcount.

**All-horizon estimate.** At a node let the resource assigned to its history be its cylinder mass divided by its cumulative homogeneous multiplier. For a nonterminal switch with numerator coefficient \(f\), its child-to-parent resource ratio is \((1/3)/(f/3)=1/f\). Their sum over the four switches is \(15/32\). At a terminal guard, if stopping at \(p_0\) achieves the first desired product, stop there; otherwise take the unique critical restart. This choice is determined by the previous multipliers and the guard. The ratio spent on that guard is at most \(3^{-(r+1)}/\lambda_0=2^{-r-2}\) because the restart multiplier is at least \(\lambda_0\). Thus the combined resource of continuations and new stops, relative to their parent, is at most
\[
     \frac{15}{32}+2\sum_{r\ge1}2^{-r-2}=\frac{31}{32}.
\]
For restarts alone it is \(27/32\). Stop a path at the first nonempty history with product at most one, counting the smaller trial exit as an opportunity. Its cylinder mass is at most its resource. After the first round, the sum of accumulated stopped resources and still-live resources is at most \(31/32\); replacing a live node by its children cannot increase that sum. This holds at every finite truncation, also for countably many terminal guards, by summing nonnegative terms. The union of successful paths over **all finite depths** consequently has Haar mass at most \(31/32\). This test allows adaptive choices of either available preparatory switch.

**Real offsets.** Fix \(M>62\) and divide each homogeneous multiplier in the product test by \(1+2/M\). The same argument bounds the union of histories reaching adjusted product at most one by \((1+2/M)31/32<1\). Every listed map or trial exit has the form \(L'=\lambda L-\gamma\) with \(0\le\gamma\le5/3\). For ordinary real \(L\ge M\),
\[
      \frac{L'+2}{L+2}\ \ge\ \frac{\lambda L}{L+2}
                            \ \ge\ \frac{\lambda}{1+2/M}.
\]
If an ordinary input \(L_0\ge M\) first drops below its initial value at a tested boundary or exit, multiply these inequalities up to that first drop. Its adjusted product is strictly less than one. This argument permits unbounded waiting and accounts for the additive term at each step. It gives a necessary symbolic test for the physical drop.

In particular the steering and restart formulas do not force even this necessary test for all ternary inputs. For every fixed number of rounds one can also choose arbitrarily large positive critical integers failing the test up to that horizon: remove the null exceptional preimages, choose a surviving ternary input, and fix the finitely many ternary digits read by its finite branching search. The witness can depend on the horizon. Positive integers themselves have Haar measure zero, so the all-horizon measure estimate leaves the fixed ordinary input question open. The argument concerns precisely the listed switches, full normalizations, critical restarts and trial exits. Other quotient edges or a first meeting at some unrelated component vertex are outside its scope.

The finite steering identities are in [termination.lean](termination.lean). This pressure and offset argument is a written proof.
