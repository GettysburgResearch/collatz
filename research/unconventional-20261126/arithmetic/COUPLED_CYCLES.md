# Many prescribed-prime-avoiding denominators with disjoint tripling fates

**J1.** Fix a finite set of primes \(S\) and a real \(0<\eta<2/5\). There are infinitely many pairwise coprime reduced denominators \(d>1\) avoiding \(S\cup\{2,3\}\) with the following property. For each such \(d\), at least \(d^{2/5-\eta}\) distinct positive odd rationals \(q\) of denominator \(d\) lie on pairwise distinct positive Collatz cycles. The positive odd rationals \(3q\) enter another family of pairwise distinct positive cycles after exactly one shortcut step. No cycle in one family occurs in the other. In particular the full forward orbits of every indicated pair \(q,3q\) are disjoint. This uses the actual eventual cycle of each source and has no inverse-depth cutoff.

For each \(q\), designating the cycle entered by \(3q\) gives an exactly invariant true basin whose indicators disagree at \(q,3q\). The construction proves this particular disagreement. It does not prove that this \(q\) is the first disagreement in its entire lattice, that all smaller sources have the opposite label, or that all smaller multiples of three avoid the designated basin. Those are extra hypotheses in the six finite PR200 models. Here all denominators are explicitly nonordinary. [PR200, all-depth least-multiple models](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/RATIONAL_MINIMA.md)

## Three paired words

Use shortcut branches \(T_0(X)=X/2\) and \(T_1(X)=(3X+1)/2\). For a binary word \(w\), read chronologically from left to right, let \(F_w=(3^pX+c_w)/2^N\), where \(N,p\) count length and ones. Appending a bit \(e\) replaces \(c\) by \(3^ec+e2^N\). The following three rows have identical clocks in the two columns.

| Name | Input word \(w\) | Output word \(v\) | \(N,p\) | \(c_w,c_v\) | \(2^N-3^p\) |
|---|---|---|---:|---:|---:|
| A | `10` | `01` | 2, 1 | 1, 2 | 1 |
| B | `010` | `100` | 3, 1 | 2, 1 | 5 |
| C | `110100000001` | `000001110100` | 12, 4 | 2117, 2336 | 4015 |

Each row satisfies \(c_v=3c_w-(2^N-3^p)\), or equivalently
\[
 F_v(3X-1)=3F_w(X)-1.                                      \tag{1}
\]
Composition preserves (1). Take an arbitrary ordering of \(a\ge1\) copies of A and \(b\ge1\) copies of B, followed by exactly one C, and denote its full input and output words by \(W,V\). Their common clocks are
\[
 N=2a+3b+12,\qquad p=a+b+4,\qquad D=2^N-3^p>0.
\]
Let \(X=c_W/D\) and \(Y=c_V/D\) be their respective rational periodic points. Both are positive and \(Y=3X-1\) by (1). The period words are physically exact: each rotated word gives a fraction with the same odd raw denominator, so every intermediate state is in the odd-denominator ring. At each step only its true parity branch maps that ring to itself. This rederives the relevant instance of Lagarias's rational-cycle theorem. [Lagarias, Theorem 2.1](https://doi.org/10.4064/aa-56-1-33-53)

The last bit of \(W\) is one, so \(q=(2X-1)/3\) is its actual preceding odd phase. It is positive: equivalently the map on the first eleven letters of C is \((27 Z+23)/2048\) at the positive state \(Z\) before C. The doubled numerator relation gives
\[
 T(3q)=(9q+1)/2=3X-1=Y.
\]
Every phase has the same reduced denominator \(d\mid D\) on its own cycle, since \(D\) is coprime to six. From \(Y=3X-1\), the two cycles and \(q,3q\) have this same reduced denominator. The odd rational \(3q\) cannot already be cyclic: its reduced numerator is divisible by three, whereas every odd cyclic phase has a preceding odd input and is a ternary unit by the accelerated recurrence.

## Distinct cycles and denominator concentration

The input circle has exactly one run of seven consecutive zeros, inside C, and has no occurrence of `111`. Every A or B ends in zero, the next block begins with at most one zero, and C begins with `11` and ends with one. On the output circle `111` occurs exactly once, inside C's output. Indeed A's output `01` and B's `100` can make at most two consecutive ones across a boundary; the output C starts and ends in zero. Thus the two cycles differ, each circle has least shortcut period \(N\), and its single marker locates the C block uniquely up to rotation. Once C is fixed in place the two A/B codes are prefix-free on either side. Distinct orderings therefore give different input cycles, different output cycles, and no identifications across the two families.

Let \(M\) be a positive product of all prescribed primes exceeding three, with empty product one, and set \(L=\varphi(M)\). The two column vectors \((2,1),(3,1)\) have determinant \(-1\). Choose \(a,b\) in prescribed residue classes modulo \(L\) so that \((N,p)=(0,1)\pmod L\). For any large integer \(n\) these classes have representatives \(a,b\in[n,n+L)\). Then \(D\equiv-2\pmod M\), so all reduced denominators avoid the prescribed primes. For fixed \(M\) and \(n\to\infty\),
\[
 \log_2D=5n+O_M(1),\qquad
 \log_2\binom{a+b}{a}=2n+O_M(\log n).
\]
The raw denominator has only \(D^{o(1)}\) positive divisors. For example, for any \(\delta>0\), \(e+1\le p^{\delta e}\) at every sufficiently large prime \(p\), and the finitely many smaller primes cost a fixed constant each after taking the maximum of \((e+1)p^{-\delta e}\). Pigeonholing the reduced denominator thus finds a \(d\mid D\) with at least \(D^{2/5-o(1)}\) paired cycles. The three input-block affine maps preserve \([0,1]\) and are strict contractions, so the fixed point \(X\) is in \((0,1]\). There are at most \(d\) such rational numbers of denominator \(d\). Thus the selected \(d\) grows, and since \(d\le D\), the number of pairs at that \(d\) is at least \(d^{2/5-\eta}\) at all sufficiently late choices. Adding all previously selected prime divisors to the next \(M\) gives a sequence of pairwise coprime reduced denominators. The loss \(o(1)\) was taken separately for each fixed \(M\) before this induction.

Lagarias's Theorem 3.3 already constructs denominators with more primitive cycles than the exponent used here. The additional requirement in J1 is that many pairs of different cycles actually realize the precise tripling comparison at a cyclic positive input after one shortcut step, even with prescribed finite-place exclusions. The exact affine pair chain, including counted coalescence, is established elsewhere. The present construction concerns explicit periodic words staying in distinct cycles. We make no general historical-priority claim. [Lagarias, Theorem 3.3](https://doi.org/10.4064/aa-56-1-33-53) · [Weaver, Paper 124, references and scalar inputs](https://rstation.ai/problems/collatz/papers/124)

## Reciprocal comparison at the two cycle minima

The construction has a second exact tripling edge in the reverse direction. Just before the C block let the input be \(Z\) and the output \(3Z-1\). Set
\[
 q_A=(27Z+23)/2048,\qquad q_B=(3Z-1)/32.
\]
These are the actual odd phases immediately before the final input one and immediately before the first output one in C, respectively. We already have \(q_A=q\). The additional identity
\[
 9q_B+1=64q_A
\]
shows that \(U(3q_B)=q_A\) with division exponent exactly six. Thus tripling at a cyclic odd phase enters the opposite cycle in both directions.

In fact \(q_A,q_B\) are the respective unique odd minima of the two cycles. Each input-block map preserves \([2/5,1]\), so every input-block endpoint is in this interval and every output-block endpoint is in \([1/5,2]\). In input A and B the sole odd input is at least \(1/5\). In C the odd inputs at positions zero, one and three are at least \(2/5\), while \(q_A\le50/2048\) occurs at position eleven. In output A and B the sole odd input is at least \(1/10\). In output C the phase \(q_B\le1/16\) at position five is followed by odd inputs at positions six, seven and nine, each greater than \(1/4\) by the indicated actual branches. These strict comparisons prove the minimum claims. Orbit-minimum comparisons by themselves do not exclude smaller positive points elsewhere in the full basin.

## Four full least-disagreement certificates

For the following four fixed words only, a complete fate check certifies the stronger least-disagreement condition. Choose the smaller of the two marked odd phases for the source and designate the cycle of the larger phase. The last three columns use integer numerators in that row's denominator.

| Word | Reduced denominator | Smaller phase | Larger phase | First multiple entering designated basin |
|---|---:|---:|---:|---:|
| ABC | 130343 | 1937 | 2309 | 5811 |
| AABC | 522101 | 9395 | 9479 | 28185 |
| ABBC | 1046389 | 9907 | 17743 | 29721 |
| AABBC | 598249 | 6367 | 10243 | 19101 |

`check_coupled.py` first checks the rational periods, their physical branch values and both tripling edges using exact arithmetic. For a smaller numerator \(q_0\) it then tests every positive odd numerator \(u\le q_0\) and every odd numerator divisible by three with \(u\le3q_0\). Common divisors with \(d\) give exact exclusions by invariance. All other inputs are followed on the actual integer-numerator map until they enter a previously proved fate or repeat and close a different cycle. A safety-cap exceedance aborts the entire run. The only hit in the tested set is \(3q_0\) itself in each row. Stripping powers of two includes the even cases, and every reduced denominator other than \(d\) in the prime-to-six domain stays distinct. Thus the complete designated basin has no smaller positive multiple of three, and every positive start through \(q_0/d\) is outside it. The marked source is the actual least positive odd tripling disagreement in this sense.

The four runs test 23,009 odd numerical starts across the stated sets and certify 653,953 new odd transitions. All 45 pairwise gcds amongst these four denominators and PR200's six denominators are one. In consequence, any collection of at most nine primes misses at least one denominator admitting the full least-disagreement certificate. J1 permits an arbitrary fixed finite set of primes for reciprocal disjoint fates, with the stronger full least-disagreement condition verified only on the ten individual denominators. `COUPLED_CONTROLS.json` records all replayed counts. `CoupledCycles.lean` checks equation (1) for arbitrary concatenations and both marked affine identities. Positivity, marker uniqueness, denominator counting and the full-basin fate checks are outside that Lean kernel.
