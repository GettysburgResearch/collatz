# An explicit bounded prefix maximum and its sharp defect size

With ordinary shortcut slopes $a(n)=1/2$ or $3/2$, denote the first $j$-step slope product by $A_j(n)=3^{p_j(n)}/2^j$. Give the input its own finite horizon
\[
 k(n)=\max(0,\lfloor\log_2 n\rfloor-3),\quad B(n)=\max_{0\le j\le k(n)}A_j(n),\qquad u(n)=B(n)^{-2}.
\]
This gives an explicit positive rational function $u\le1$. Write $r(n)=a(n)B(Tn)/B(n)$; the positive logarithmic defect for squared slopes is $2\log^+ r(n)$. Let $p=\log_3 2$, $h_*=H_2(p)$.

**Counts and amplitudes.** In each sufficiently large dyadic shell $[2^m,2^{m+1})$ the number of violations $r(n)>1$ is
\[
                \Theta\bigl(2^{h_*m}m^{-3/2}\bigr).                   \tag{1}
\]
The same two-sided order holds for the sites attaining the maximum possible $r(n)=9/4$, hence a squared-slope log loss of $4\log(3/2)$. No pointwise estimate comparable to $1/n$ can account for these losses. The statistics of coefficient-surviving parity words are established prior work. Here they count failures of a concrete input-dependent Bellman horizon. [Terras, *A stopping time problem on the positive integers*](https://doi.org/10.4064/aa-30-3-241-252) · [Weaver and Wren, Paper 87, §1](https://rstation.ai/problems/collatz/papers/87/v1) · [Weaver, Paper 176, §5.3](https://rstation.ai/problems/collatz/papers/176)

To prove (1), write $k=m-3$. At an even input $k(Tn)=k-1$, so the finite prefix recurrence excludes a violation. At an odd input $k(Tn)\in\{k,k+1\}$. The maximum in $a(n)B(Tn)$ ranges over the nonempty prefix slopes through length $1+k(Tn)$. Thus a violation requires a new strict coefficient record at length $k+1$ or $k+2$; if both exceed the old maximum, the earlier already gives such a record. All nonempty slope products differ from one. A record at $N$ means every reverse prefix of the first $N$ parity bits has positive logarithmic gain. The last one or two newly allowed factors are each at most $3/2$, giving $r(n)\le(3/2)^2$ globally, with the clipped small horizons included (at an even site whose horizon is clipped to zero use $a=1/2$).

For completeness, the number $M_N$ of positive-meander words of length $N$ is comparable to $2^{h_*N}(N+1)^{-3/2}$. For independent fair parity bits set $S_j=p_j\log3-j\log2$. No nonempty partial sum vanishes. The Sparre Andersen–Spitzer fluctuation identity gives the formal series
\[
 \sum_{N\ge0} 2^{-N}M_N z^N
       =\exp\left(\sum_{j\ge1}z^j\Pr(S_j>0)/j\right).
\]
Equivalently, apply Spitzer's exponential identity to the running minimum with parameter tending to positive infinity. The bounded exponential of the minimum converges to the survival indicator, and the corresponding endpoint term to $\mathbf 1_{S_j>0}$. Coefficients use finitely many endpoint terms. Writing $\rho=2^{h_*-1}$, the largest binomial term at the threshold $\lceil pj\rceil$ has order $\rho^j/\sqrt{j+1}$ by Stirling, uniformly over the rounding of the count. Higher terms decrease geometrically since $p>1/2$. Thus $b_j=\rho^{-j}\Pr(S_j>0)/j\asymp j^{-3/2}$. The $N$th coefficient of $\exp(\sum b_j z^j)$ is at least $b_N$ and is $O(N^{-3/2})$. Indeed some part of each $s$-fold convolution is at least $N/s$, giving the bound $C s^{5/2}\|b\|_1^{s-1}N^{-3/2}$ before division by $s!$. This proves the estimate for $M_N$. The same fluctuation-identity method is used for the weighted minimum in Paper 176. [Spitzer, *A combinatorial lemma and its application to probability theory* (1956)](https://doi.org/10.1090/S0002-9947-1956-0079851-X)

Each $N$-bit word occupies one residue modulo $2^N$. For $N=k+1,k+2$ a full dyadic shell therefore realizes each word boundedly many times. This proves the upper bound in (1). For the lower bound take any positive meander of length $k-1$, append one odd bit, and reverse. The resulting physical word begins odd and sets a strict record at $k$. Append two further odd bits to its physical end. The interval $[3\cdot2^{m-1},2^{m+1})$ has length $2^{k+2}$ and hence contains exactly one ordinary lift of each such full word. Its odd first step crosses $2^{m+1}$, increasing the horizon by one. At every lift the ratio is exactly $9/4$ because its length-$k$ slope already equals the old maximum and its next two steps attain the largest possible factors. This proves both lower bounds.

**No uniform accumulated-defect repair on simple paths.** The construction of two successive long climbs using a power-of-three congruence has antecedents in Rozier and in [freelan_lab, Paper 200 v2, Remark 8.3](https://rstation.ai/problems/collatz/papers/200). That source uses a different congruence for a predecessor-density lower bound. Here the conclusion concerns the accumulated defect of the specific input-dependent prefix maximum. For arbitrarily large $L$, choose $h\ge L+4$ for which $3^h\equiv-5\pmod{2^L}$. For $L\ge3$, powers of 3 modulo $2^L$ give exactly the units congruent to 1 or 3 modulo 8. Indeed $v_2(3^{2^j}-1)=j+2$ for $j\ge1$, by factoring the successive differences of squares. The order is $2^{L-2}$, and the indicated residue set has that cardinality. Hence one may take $h\le L+4+2^{L-2}$.

The first $h$ steps from $x_0=2^h-1$ are all odd and strictly increasing, with $x_j=3^j2^{h-j}-1$. They form a simple path to $Y=3^h-1$. Here $k(x_0)=h-4$, $B(x_0)=(3/2)^{h-4}$ and $A_h(x_0)=(3/2)^h$. Since $Y\equiv-6\pmod{2^L}$, its next $L$ true parities begin like the signed trajectory $-6,-3,-4,-2,-1,-1,\ldots$. These are the four bits $0100$ followed by $L-4$ odd bits. Its own horizon is at least $L$ for sufficiently large $L$. Thus
\[
 B(Y)\ge(3/16)(3/2)^{L-4},\qquad
 \sum_{j<h}\log r(x_j)=\log(A_h(x_0)B(Y)/B(x_0))
                     \ge L\log(3/2)+\log(3/16).
\]
At the same time the odd reciprocal sum of the initial segment is at most $h/(2^h-1)\to0$. Thus even the **signed** accumulated deficit is unbounded over these simple ordinary segments with varying sources. On a fixed escaping source, the telescoping product and the uniform simple-path reciprocal estimate instead give at least $(\log x_t-O_{x_0}(1))/(2\log(3/2))$ actual violating departures before time $t$. Neither estimate proves that any fixed source escapes.

[ESCAPE_FLUX.md](ESCAPE_FLUX.md) gives a different construction with much sparser conditional defect support and shows the precise cumulative logarithmic lower bound each escaping component would require.
