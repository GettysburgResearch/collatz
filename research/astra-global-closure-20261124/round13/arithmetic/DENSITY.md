# A density-one consequence for growing blocks of original parents

**SOURCE-QUALIFIED written consequence.** Use the parent family and ordinary map in the [arithmetic proof](README.md). Let $I$ be any interval of $N\ge2$ consecutive integer parameters all at least $J$. Take an arbitrary $F\subseteq\{0,\ldots,J\}$ containing zero. Except for at most
$$
 C N\min\left(1,\frac{1+J}{\sqrt{\log(2N)}}\right)
$$
parameters $m\in I$, all the parents $Z_{m-i}$ for $i\in F$ merge at one ordinary endpoint by a common *post-peak* clock $h=\lfloor\log_2 N\rfloor$. Each parent's total clock at that horizon is $7+11+162(m-i)+h$. In particular a fraction tending to one has a merger to all $J$ earlier consecutive parents when $1\le J=o(\sqrt{\log N})$, uniformly in the interval location. Each earlier triple has its original ordinary upper hit at one. The analytic pair estimate below is an input from a frozen proposed result, not an independently established tail estimate of this round.

For a uniform binary input $X$ consider $Y=3^sX+d$. Define absorption by equality of the two physical affine forms and their augmented grades on a whole binary prefix. With $s\ge0$, $d\in\mathbb Z$ and $h\ge1$, PR146 states
$$
 \Pr_{s,d}(\tau>h)\le C_0(1+s+\sqrt{|d|/3^s})/\sqrt h .
$$
This is the oriented-process estimate in the section “Reaching a small normalized offset” of the source. Its final section already transfers pair counts to consecutive exponential exponents. Here we use the stronger symbolic event in the proof to ensure simultaneous equality of the actual ordinary paths. We read the frozen statements and their transition argument. Their complete probabilistic proof has not been independently replayed in this packet. [PR146 at f4310782, growing additive gaps](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md) · [Underlying oriented pair calculation](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

For $h\ge3$, the variable $n_m=3^{11+162(m-J)}$ runs once through every residue $3\bmod8$ modulo $2^h$ per period $2^{h-3}$. This follows from $v_2(3^{162t}-1)=3+v_2(t)$ for $t>0$. The post-peak starts are $3^a n_m-1$ with $a=162(J-i)$. Sort these $a$ increasingly. Consecutive entries $a,a+s$ give
$$
 X=3^a n_m-1,\qquad Y=3^sX+(3^s-1).
$$
Within a period, $X$ uniformly fills one residue modulo eight at depth $h$, so conditioning the source estimate on this residue costs at most a factor eight. The normalized absolute offset is strictly below one. Failure of a pair's absorption by $h$ consequently has proportion $O((1+s)/\sqrt h)$. Once absorbed, a pair stays equal at every later common clock. The union bound over consecutive pairs costs $O((|F|-1+162J)/\sqrt h)$, since the sum of their nonnegative grade gaps is at most $162J$. This proof needs no independence between pairs.

An interval of $N$ indices is covered by at most $\lceil N/2^{h-3}\rceil+1$ periods, whose total length is at most $N+2\cdot 2^{h-3}=O(N)$. For the finitely many $h<3$ the trivial estimate suffices. This proves the claimed uniform count under the pinned source estimate. It does not imply coverage for one specified index. In fact the [independent shifted-height finite-class proof](../trace/FINITE_FAMILY.md#every-actual-augmented-class-is-finite) gives infinitely many actual indices without an earlier augmented synchronous post-peak comparison.
