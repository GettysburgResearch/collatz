# A located-source count for the bounded least-disagreement branch

**PROPOSED pending independent proof review and replay.** Let a least-disagreement cycle satisfy the bounded alternative of the pinned PR195 results. Write $s$ for its ordinary odd minimum, $p$ for its least odd period, $h$ for its total halving count, and $\lambda=h/p$. For every fixed $\theta>23/60$ there is a constant $C_\theta$ such that
$$p\le C_\theta s^\theta.$$
In particular these cycles satisfy $0<\lambda-\log_2 3\ll_\theta p^{-1/\theta}$. The bound $23/60=0.38333\ldots$ is above the $1/3$ threshold for an asymptotic finiteness argument using irrationality exponent three. Only the finite transfer has a local exact replay. The written argument uses the ineffective Subspace-Theorem separation in Paper 145.

## The masks and the finite transfer

Use the exact rational-clock rank mask from PR195. At an arbitrary cut let $B_i=\lfloor\phi+i\lambda\rfloor$, $0\le\phi<1$, and $\beta_i=B_{i+1}-B_i$. The physical exponent is $a_i=\beta_i+k_i-k_{i+1}\in\{1,2\}$, with $0\le k_i\le3-\beta_i$. Indeed the highest band is forbidden exactly at the ranks with $\beta_i=2$. This is the entire mask needed in this count. Its real height assumptions hold for every sufficiently large cycle in the stated branch. The actual chronological odd positions are $B_i+k_0-k_i$. [PR195, exact rank mask](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-global-closure-20261124/round13/cycle/README.md)

For a consecutive block of $L$ odd steps put $S=B_L-B_0$, $c_i=2^{2-k_i}$, and take its common normalized carry
$$C=\sum_{i<L}3^{L-1-i}2^{B_i-B_0}c_i.$$
Starting layers are allowed to differ between copies. If the four starts equal a fixed $k$, write $E_k$ for the number of ordered quadruples of legal histories, with their last layers free, satisfying $C_1+C_2-C_3-C_4=0\bmod 2^S$. Different histories are counted with their multiplicities, including a last-layer choice which does not change $C$. With four possibly different prescribed starts $k_j$ and any requested residue, Fourier inversion on the cyclic group and Hölder bound the count by $\prod_{j=1}^4 E_{k_j}^{1/4}$.

At $L=64$, all schedules at $\lambda=\log_2 3$, including the extra last symbol defining the last-layer mask, give the following maxima over all starts. Denote each maximum by $E$.

| Native $S$ | $E$ |
|---:|---:|
| 101 | 68931768644982317296080290705653987 |
| 102 | 102176439881582869100955782739787728 |

Both satisfy $E^{20}<2^{23S}$. The phase cells begin at $\{-j\lambda\}$, $0\le j\le65$. Their circular order and all the schedules are constant on a neighborhood of this irrational slope, since the finitely many floors and pair-order comparisons are locally constant away from rationals of denominator at most 65. The checker computes $\lfloor k\log_2 3\rfloor$ by integer bit lengths, also for negative $k$. Its signed carry starts at zero and at each step requires
$$2^{\beta_i}d_{i+1}=3d_i+c_{i,1}+c_{i,2}-c_{i,3}-c_{i,4}$$
to have an integer successor. It counts both ordered path pairs through their layer histograms with multiplicities. Free integer terminal carry is exactly the displayed modular test. At eight steps a separate direct enumeration checks every phase and start. [Exact finite transfer](check_strip_energy.py) · [Replay output](../../../reports/astra-sixhour-20261127/arithmetic/strip_energy.json)

For any longer bridge, ordinary equality of its four normalized carries forces the signed carry at every intermediate cut to be integral. This follows by reducing the remaining suffix terms modulo its power of two and using that three is odd. Given the four entrance layers and signed carry at each 64-step block, the condition at the exit specifies one residue of the block carry. Successive counting therefore bounds the number of ordinary four-copy equalities, even with prescribed terminal layers, by $O(2^{23T/20})$ when the native duration is $T$. A remainder shorter than 64 costs an absolute factor. Differences between $T$ and the mechanical clock telescope across blocks and are bounded at the endpoints. Within a bridge with a prescribed entrance layer the ordinary and normalized raw carries differ by one common power of two. Their exact equalities coincide.

## From a bridge to the located interval

Select $b$ odd gaps and include the last odd bit. For a fixed phase, start and terminal layer let $K=B_b+k_0-k_b+1$ be the native duration. Distinct exponent words give distinct source residues modulo $2^K$, by chronological parity coding. Fix a small constant $\epsilon>0$, let $P=\lfloor K/(4+10\epsilon)\rfloor$, and start four consecutive disjoint bridges at odd cuts, the first at native offset $3\epsilon P+O(1)$. Give each native length $(1-\epsilon)P+O(1)$, choosing the odd indices by the mechanical clock before specifying the interior. Condition on the finitely many boundary layers and the exterior word. Each bridge then has fixed count, fixed endpoints and independent uniform histories under the uniform full family. All those walks concatenate. The exterior uses $O(\epsilon K)+O(1)$ native steps, contributing at most $2^{O(\epsilon K)+O(1)}$ choices. Leave the final odd bit outside.

For each bridge the two raw moduli in Paper 145 are $2^m,3^n$, where $m$ is the remaining native time at the start and $n$ counts the cumulative odd inputs through its end. Both exceed $2^P$ uniformly for $\lambda$ sufficiently close to $\log_2 3$. The first end lies past $(1+2\epsilon)P+O(1)$, and the last start leaves more than $(1+\epsilon)P+O(1)$ native steps. The local ordinary numerator is $O(T2^T)$ by the bounded prefix deviations and $\lambda\ge\log_2 3$. Thus the paper's raw dual identity and Lemma 4 imply that each balanced grid collision of four copies of **one fixed bridge** at binary precision $P$ gives exact equality of their balanced ordinary numerator sums, for all sufficiently large $K$. The input requires the clock margins and $T<(1-\epsilon/2)P$. The same separation lemma is used for height two in that paper. [Weaver, Paper 145, §§4–6 and 10](https://rstation.ai/problems/collatz/papers/145/v1)

If the bridge has $N_j$ histories and quantized probability law $f_j$, its fourth Fourier moment is consequently at most $O(2^{23T_j/20})/N_j^4$. Hölder in the convolution of the four actual bridge laws bounds its largest atom. The four grid remainders cost at most six possible grid sums for a prescribed interval of length $2^{-P}$. Multiplying by the actual number $\prod_j N_j$ of full interior histories cancels every $N_j$. The located count is therefore
$$2^{O(\epsilon K)}O(2^{(23/80)\sum_jT_j})\le O_\epsilon(2^{(23/20)P+O(\epsilon K)}).$$

For an interval of $Y$ integers choose $b=\lceil ((4+10\epsilon)/(3+10\epsilon))(\log_2 Y+5)/\lambda\rceil$. Then $K=\lambda b+O(1)$, $K-P\ge\log_2Y$, and $P\le(\log_2Y)/(3+10\epsilon)+O(1)$. All source residues in that interval lie in a circular interval of length at most $2^{-P}$. There are $O(b)$ phase cells for the fixed slope and boundedly many endpoint layers. Thus for every $\theta>23/60$ the located source count is $O_\theta(Y^\theta)$ on a sufficiently small right neighborhood of $\log_2 3$, after choosing $\epsilon$ small enough. In the prescribed bounded branch every distinct odd phase lies in $[s,(16s+7)/3]$ and admits all these windows. The product identity gives $0<\lambda-\log_2 3\le1/(3s\log 2)$. This proves the claims, absorbing bounded minima.

The transfer includes high-mismatch words throughout the stated mask. The full denominator-one exclusion and first-crossing trajectories remain open.
