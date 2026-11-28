# The logarithmic square threshold for a typical early integer visit

**Proposed written theorem.** Let \(j\) denote the binary octave index of \(y\in[2^j,2^{j+1})\). For every nondecreasing, computable \(w:\mathbb N\to\mathbb N\) tending to infinity, there is a single computable odd set \(F\) with
\[
               |F\cap[2^j,2^{j+1})|/2^j\ll w(j)^2/j^2                 \tag{1}
\]
which a density-one set of ordinary positive starts reaches in \(o(\log n)\) native steps, strictly before the true global minimum date. There is no minimum rate of growth required of \(w\). Its diverging minorant used in the construction never exceeds \(O(\log j)\). Conversely, if the octave densities of a deterministic mask are \(O(1/j^2)\), then the probability that an ordinary source reaches it before its minimum and by \(o(\log n)\) dates tends to **zero**. At the exact order \(O(1/j^2)\) the construction can attain any fixed lower hit frequency less than one by \(O(\log n)\) native steps, with a constant in the density bound depending on the desired frequency.

For every such \(w\), the computable \(+1\)-only map of [Density-one unit perturbation](DENSITY_ONE_UNIT_PERTURBATION.md) may accordingly be taken with
\[
            |\{n\le X:U(n)\ne T(n)\}|
             \ll X\,w(\lceil\log_2 X\rceil)^2/(\log X)^2,               \tag{2}
\]
while its escaping starts have density one, all edges below any prescribed threshold remain genuine, and its and the true map's stopped-path laws have total variation distance tending to one. In particular an arbitrarily slowly diverging computable multiplier on \(1/j^2\), in place of its square, is obtained by using an integer square-root minorant. The upper construction is elementary. The reverse implication quoted above uses the source-qualified [all-height upper bound](ALL_HIGH_TARGETS.md).

## First-passage words and their exact density cost

Use iid positive gaps \(a_i\) with probabilities \(2^{-a_i}\), and \(s_k=\sum_{i=1}^k a_i,\ W_k=3^k2^{-s_k}\), \(W_0=1\). This is a positive mean-one martingale. For a rational \(L>1\), take the set of finite words which first cross \(L\) before first falling below \(1\), stopping when \(W_k\ge L\), and having \(k\le C\lceil\log_2 L\rceil\). A fixed integer \(C\), for example \(100\), suffices below. Comparisons with \(1,L\) are rational; at any positive depth \(W_k\ne1\). The family is finite since \(W_k\ge L\) implies \(s_k\le k\log_2 3\). For each such stopped word use the actual terminal ternary cylinder modulo \(3^k\) from the reversed word formula in [Sharp multiscale targets](SHARP_MULTISCALE_TARGETS.md). Denote their union by \(A(L)\), with the varying moduli understood.

Let \(p_L\) be the probability that the original iid excursion realizes one of the stopped words. Then for absolute \(c>0\), all sufficiently large \(L\),
\[
            c/L\le p_L\le 1/L,\qquad
            \sum_{\text{stopped words of length }k}3^{-k}
                   \ \le\ 1/L^2 ,                                      \tag{3}
\]
where the sum ranges over **all** retained lengths and words. Indeed the probability of a word of total \(s_k\) is \(2^{-s_k}\), and \(3^{-k}=2^{-s_k}/W_k\) on that word. These stopped word events are disjoint on the iid chronological gap tape. Doob's maximal inequality for \(W_k\), or first-crossing expectation at the bounded stop, gives \(p_L\le1/L\), hence the last estimate. Distinct cylinders may overlap after reversal; summing their measures only enlarges the bound.

For the lower estimate tilt one gap to probability \(3\cdot4^{-a}\). These probabilities sum to one, have mean \(4/3\), and their joint likelihood relative to the original tape on a word is exactly \(W_k\). The tilted log-product has positive mean increment \(d=\ln3-(4/3)\ln2\). It has a fixed positive probability of never falling below its initial level: choose small \(\delta>0\) with \(\mathbb E_*(e^{-\delta\log W_1})<1\), first take a fixed number of \(a_i=1\) to accumulate a positive height \(b\), and then use the nonnegative supermartingale maximal inequality to bound the chance of descending by \(b\) by \(e^{-\delta b}<1\). By the law of large numbers it reaches \(\ln L\) by \(100\lceil\log_2 L\rceil\) with probability tending to one, since \(100d/\ln2>1\). Thus simultaneous successful crossing before failure and within the cutoff has tilted probability bounded below independently of large \(L\). The overshoot satisfies \(L\le W_k<3L/2\), since each factor is at most \(3/2\). Summing the reverse likelihood over the disjoint stopped words gives \(p_L\gg1/L\).

For a whole octave of size \(2^j\) and \(L=O(j)\), the proportion of integers satisfying these terminal cylinders is at most \(2/L^2\) for large \(j\), including rounding. Indeed all moduli \(3^k\le3^{100\lceil\log_2 L\rceil}=j^{O(1)}\) are then below \(2^j\); for each word the number is at most \(2(2^j)3^{-k}\). No stationary density or word-separation bound enters (3).

## Many fresh trials within the native bit budget

From the first one of a fair native bit tape, cut the iid gap sequence into successive completed excursions, each ending at the first \(k\ge1\) with \(W_k<1\) relative to the preceding cut. These pieces are iid. The number \(D_-\) of gaps in one piece has an exponential tail: \(D_->n\) implies \(\log W_n\ge0\), exponentially unlikely under the original iid law of negative log drift. For instance use \(\mathbb E W_1^\delta<1\) at any \(0<\delta<1\). Its native duration \(s_{D_-}\) has an exponential tail as well: split at \(\lfloor t/4\rfloor\) gaps, and bound the probability of a total above \(t\) among that many original geometric gaps by exponential Markov. The initial delay to the first one is also geometric. Consequently some absolute \(b_0,c_0>0\) give probability \(1-O(e^{-c_0K})\) of completing at least \(\lfloor b_0K\rfloor\) excursions by native date \(K\); apply the exponential moment bound to the sum of that many durations, choosing \(b_0\) small. Each excursion has independent success probability \(p_L\) to contain a retained crossing. Without conditioning on fitting all excursions inside the date budget, union bounding the two failure events gives
\[
       \Pr(\text{no completed marked word by native date }K)
               \le \exp(-c_2 K/L)+O(e^{-c_0K})                         \tag{4}
\]
when \(K/L\) stays bounded away from zero and \(L,K\) are large, with a fixed \(c_2>0\). A final one terminating a successful word is an actual odd state. Marking it uses only parity through date \(K\).

## Placing the tests at the physical heights

For large \(j\) put \(e=\lfloor\log_2 j\rfloor\). Start at the first \(e_0\ge1\) with \(w(2^{e_0-1})\ge1\), set \(b'_{e_0}=1\), and for \(e>e_0\) form the positive integers
\[
              b_e'=\min(b_{e-1}'+1,\,w(2^{e-1})),\qquad L_e=2^e/b_e'.
\]
Leave the finitely many initial octaves without three defined neighboring parameters \(L>1\) empty. The \(b_e'\) increase to infinity, grow by at most one per stage, and are \(O(e)\). On octave \(j\) retain the odd integers in any of \(A(L_{e-1}),A(L_e),A(L_{e+1})\). The neighboring parameters have reciprocals \(O(w(j)/j)\), because \(b_{e+1}'\le w(2^e)\le w(j)\) and \(j<2^{e+1}\). Hence (3) and its integer rounding bound give (1). All parameters and finite words can be computed with integer arithmetic.

Take \(K=\lfloor j/\sqrt{b_e'}\rfloor\) from the starting octave, using integer comparison to take the floor. Then \(K=o(j)\), \(K/L_e\to\infty\), and every state through date \(K\) has octave index \(j'\in[j-K-1,j+K+1]\), inside \([j/2,2j]\) for large \(j\). Thus the test \(A(L_e)\) is accepted at every possible terminal height of a successful trial. The exact native \(16K\)-bit dictionary on any subinterval of at least \(2^{20K}\) consecutive sources carries error \(O(2^{-4K})\). Equation (4) now implies a true integer hit by \(K\) with probability tending to one. As in the [fixed-total construction](SHARP_MULTISCALE_TARGETS.md), the number of odd departures by \(16K\) is at most \(9K\) with failure \(O(e^{-cK})\). The correction to the homogeneous log multiplier is \(O(K2^{16K}/n)\), so \(T^{16K}n<n2^{-K}\), below every state through date \(K\). This establishes the minimum and all-cutoff density assertions. The same argument at the exact \(j^{-2}\) scale takes \(b_e'=b\) a large fixed constant, \(K=\lfloor j/64\rfloor\); the complete grid still fits, the additive correction tends to zero, and (4) leaves failure \(O(\exp(-c b))\). A constant depending on any prescribed failure tolerance suffices. This fixed-constant variant claims a lower limiting frequency, with no assertion here that it equals one.

For the converse, at most \(O(K+1)\) nearby octaves can be visited within \(K=o(j)\) native steps from a start in the whole \(j\)-th octave. The square-root costs \(O(1/j)\) give total \(o(1)\). Apply [All high targets](ALL_HIGH_TARGETS.md), restricting the source from the uniform interval through \(2^{j+1}\) to the octave at a bounded factor. This gives the uniform whole-octave conclusion, and hence the natural-density version for any prescribed deadline \(o(\log n)\) by domination on full dyadic octaves.

Finally, forward closure of the seeds under the computable least-odd rounding rule preserves (2) by the geometric seed count in [Density-one unit perturbation](DENSITY_ONE_UNIT_PERTURBATION.md). For seed heights \(W\in[\sqrt X,2X]\) one may bound the nondecreasing envelope uniformly by \(w(\lceil\log_2(2X)\rceil)\) for a shell estimate. For the cumulative bound through \(X\), every contributing seed is itself at most \(X\), so its actual octave index is at most \(\lceil\log_2 X\rceil\) even when a bounding shell extends above \(X\); use this capped index in the same geometric sum. The contribution from heights \(W<\sqrt X\) is \(O(\sqrt X+\log X)\) on each top shell, and the lower part of the final cumulative sum is negligible. This proves the stated form even for an envelope with arbitrarily large jumps.
