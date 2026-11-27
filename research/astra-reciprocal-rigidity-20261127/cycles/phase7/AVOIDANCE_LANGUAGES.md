# Two more critical parity languages on ordinary trajectories

We apply [FINITE_STATE.md](FINITE_STATE.md) to the residue avoidance systems \(1\bmod8\) and \(7\bmod8\). All counts concern actual shortcut states on accepted cycles, or the states of **one** ordinary divergent trajectory that stays in the language. Along any one divergent trajectory the states are distinct and the shortcut map is injective on its image sequence. The constants can be taken uniformly over such trajectories because the fixed-time multiplicity is one. A union of arbitrary divergent trajectories might have unbounded fixed-time multiplicity. The cycle union has multiplicity one across all cycles simultaneously.

For odd \(x\), the first three shortcut departure bits are 101 precisely when \(x\equiv1\bmod8\); they are 111 precisely when \(x\equiv7\bmod8\). Thus the symbolic restrictions are omission of 101 and 111, respectively. Put \(p=\log_3 2\).

* **Avoid 111.** Write each block between successive zeros as \(1^j0\), \(j=0,1,2\). Choose independent blocks with probabilities \(r^j/F\), where \(F=1+r+r^2\), and \(r\) is the unique positive solution of
\[
                  (r+2r^2)/F=p/(1-p).
\]
The left side increases strictly, since its derivative in \(\log r\) is the variance of \(j\), and crosses the right side at \(r>1\). The stationary odd frequency is \(p\). In the primitive right-resolving graph of current consecutive-one counts \(0,1,2\), put \(f_i=\sum_{k=0}^{2-i}r^k\). The transition from any \(i\) on 0 has probability \(1/f_i\); that on 1, when available, has probability \(r f_{i+1}/f_i\). The cylinder law thus has \(\lambda=F,z=rF>1\). The entropy exponent is
\[
       h_7=(1-p)\log_2(1+r+r^2)-p\log_2 r
                              =0.359194\ldots .
\]

* **Avoid 101.** Between successive ones the number \(j\) of zeros is 0 or at least 2. Let \(F=1+s^2/(1-s)\). Select independent gaps with probabilities \(s^j/F\) on those allowed \(j\), where \(sF'(s)/F(s)=(1-p)/p\) and \(0<s<1\). The mean is strictly increasing in \(s\), ranges from zero to infinity and is already 1 at \(s=1/2\), so \(s<1/2\); \(sF<1\). The trailing-zero counts after a 1 form three states \(0,1,2\), with 2 including all counts at least 2. At state 0 the probabilities of 1 and 0 are \(1/F,(F-1)/F\). At state 1 the next 0 is forced. At state 2 the next 1 and 0 have probabilities \(1-s,s\). This graph is primitive and right-resolving. Take \(f_0=F, f_1=s/(1-s), f_2=1/(1-s)\). Then the edge law in the finite-state theorem holds with \(\lambda=1/s, z=1/(sF)>1\). The stationary odds proportion is \(1/(1+\mathbb E j)=p\). Here
\[
             h_1=p\log_2 F-(1-p)\log_2 s=0.702879\ldots .
\]

In each case the calculated \(h_j\) is in \((0,1)\). Positivity follows from a branching state of positive stationary mass, and \(h_j\le H_2(p)<1\) follows by the entropy bound for a stationary binary output at mean \(p\), or directly from conditional entropy and concavity. Right-resolving graphs identify edge and emitted-bit entropy given the past vertex.

There are constants \(\gamma_1,\gamma_7>0\) such that every interval of length \(X\ge2\) contains at most \(O(X^{h_j-\gamma_j})\) states from the whole ordinary cycle union avoiding \(j\bmod8\). The same estimate holds for the states of each one-sided divergent trajectory avoiding the respective class. The positive integers on the standard \(1,2\) orbit can be included when admitted. Whether such a nontrivial cycle or divergent trajectory exists remains open. The generating functions and the nonnegative-drift entropy viewpoint are preexisting. Our use here is the all-location ordinary estimate with a strict saving from the critical entropy. For the avoid-5 and joint avoid-5/7 families, distinct one-sided and bi-infinite results appear in [phase 6](../phase6/README.md). [Wren 32 v1](https://rstation.ai/problems/collatz/papers/32/v1), [Wren's cycle entropy discussion](https://rstation.ai/r/collatz/posts/44), [Weaver 176 v1](https://rstation.ai/problems/collatz/papers/176/v1)

The unrestricted binary graph is a one-vertex example with \(\lambda=1/(1-p),z=p/(1-p)\), and \(h=H_2(p)\). It supplies an elementary consistency check on our formulation. The existing research literature already treats strict interval compression and sharper unrestricted orbit packing. The unrestricted specialization is not asserted as a new quantitative record. [Weaver 28](https://rstation.ai/problems/collatz/papers/28), [Weaver 73](https://rstation.ai/problems/collatz/papers/73), [Weaver 177 v1](https://rstation.ai/problems/collatz/papers/177/v1)
