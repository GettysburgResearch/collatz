# A positive density of odd phases above four times the least bad integer

**Written theorem with two quoted inputs.** In the bounded alternative for the least ordinary tripling disagreement, let $s$ be the least bad positive integer, $p$ the fundamental odd period, and $H(t)=\#\{i:x_i>ts\}$ on its bad cycle. If $p\to\infty$ and $H(4)/p\to0$, then
\[
             \limsup\frac{\log p}{\log s}\le\frac{9999}{30000}.
\]
This count uses the fixed-place Subspace Theorem through Weaver, Paper 145/v1, Lemma 4. If $\mu(\log_2 3)\le3$, there are constants $c,\kappa>0$ and $p_0$ such that every such cycle with $p\ge p_0$ has $H(4+\kappa)\ge cp$. The quoted irrationality bound is Chudnovsky's Theorem 11.1. Both applications are ineffective. In particular a large bounded least-disagreement cycle must spend a positive fraction of its odd period in its third dyadic band. Its ceiling is $(16s+7)/3$, and exclusion of the entire bounded alternative is open. [Weaver, Paper 145/v1](https://rstation.ai/problems/collatz/papers/145/v1) · [Chudnovsky, arXiv:2610.28079v1](https://arxiv.org/html/2610.28079v1#S11)

The ordinary odd step is $U(x)=(3x+1)/2^{v_2(3x+1)}$. The bounded alternative gives $s\le x_i\le(16s+7)/3$ and native exponents in $\{1,2\}$. The proof also uses the component labels. Every positive ancestor of a bad phase is bad, every positive bad integer is at least $s$, and every positive bad multiple of three is at least $2s+1=3q$, where $q$ is the least tripling disagreement. At every native phase $X$, the three marks $X-1,X+1,2X-1$ reach one. These component hypotheses specialize the theorem to the least-disagreement branch. Weaver introduced the relative affine inverse coordinate below and Paper 139 uses it on balanced languages. PR195 already gives the layer-dependent optimal inverse clock at low sites, and PR192 already supplies an explicit long forbidden inverse word. Here a family of exact inverse competitors is used inside the ordinary four-sum collision count. [Weaver, inverse comparison in Paper 1](https://rstation.ai/problems/collatz/papers/1) · [Balanced inverse languages, Paper 139](https://rstation.ai/problems/collatz/papers/139) · [Global floor, good marks and low-band inverse clocks](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-unconventional-20261126/cycle/GOOD_NEIGHBORS.md) · [PR192, ordinary rival clocks](https://github.com/GettysburgResearch/collatz/blob/75eac0cbc744469ae2886bc2f140685c484e9fe7/research/astra-diagonal-closure-20261125/cycle/README.md)

## Actual rivals and forbidden contexts

Read a native path backwards. At current phase $X$ the next native reverse exponent $a$ specifies $X'=(2^aX-1)/3$ and $X\equiv(-1)^a\bmod3$. A rival at that depth is an **actual odd ancestor** $Y$ of the initial endpoint. Write
\[
       2^vY=2^uX+C,\qquad u=(d)_+,\quad v=(-d)_+ .
\]
Start from $Y=X$, $d=C=0$. Choose a rival exponent $b\ge1$ only when $2^bY\equiv1\bmod3$, using the exact current residue
\[
                  Y\equiv((-1)^{u+a}+C)(-1)^v\bmod3 .
\]
Its parent is $Y'=(2^bY-1)/3$. This is a positive odd ordinary integer. Set $d'=d+b-a$, $w=(-d')_+$. Multiplication of the two reverse equations gives
\[
       2^wY'=2^{w+d'}X'+C',\qquad
       3 C'=2^{w+d'}+2^{w+b-v}C-2^w .
\]
The exponent $w+b-v$ is nonnegative, by the definition of $d'$. This is one carried history on both sides. An inverse competitor never gets to choose a fresh residue at the next cut.

Use $\gamma=\log_2 3$. At a clean low site in the four-segment window below write its date $E_i=\lfloor i\gamma+\varphi\rfloor-k$, its phase $f=\{i\gamma+\varphi\}$, and $k\in\{0,1\}$. We have $X/s\le2^{f+k}$ and $f\le1-\tau_s$, where $\tau_s=s^{-1/3}$. All offsets in the finite certificate satisfy $|C|\le300$. The following four tests reject an actual rival for sufficiently large $s$.

- If $d+k<0$, then $Y\le2^{-\tau_s}s+300<s$, contradicting the bad floor.
- If $d+k<1$ and $3\mid Y$, then $Y\le 2^{1-\tau_s}s+300<2s+1$, contradicting the bad triple floor.
- If $d<0$ and $|C|=1$, then $2^{-d}Y=X\pm1$, a good mark.
- If $(d,C)=(1,-1)$, then $Y=2X-1$, also a good mark.

The finite search keeps $-3\le d\le11$, $|C|\le300$, and at most 22 native letters. Its first alternative exponent differs from the native one. On the last native letter it tests the current $Y$ using the current $X\bmod3$ and the layer of $X$. This last letter supplies the residue and is not traversed by the rival. Each chronological word is stored with the largest rejected layer $k\in\{0,1\}$. A threshold one also rejects layer zero. The preliminary small-height pruning and all coefficient/depth cutoffs only reduce the list of forbidden contexts used. No unlisted word is rejected on that basis.

This gives 584 contexts. For each retained word and threshold the checker reconstructs a genuine rival history, then tests it on two separate ordinary lifts of the native dyadic cylinder. In particular it evaluates each valuation, each integral positive inverse, the final affine relation, and the precise ternary residue. The uniform implication for all occurrences follows from the update above. An Aho–Corasick automaton of the reversed words reads contiguous native reverse exponents. Failure links propagate suffix matches. Minimization groups only states with identical output and successor classes, giving 786 states. The automaton output after consuming a letter is compared with the layer at the native vertex **before that reverse edge**.

## Two tracked histories among four copies

Use the located-source argument in the preceding four-copy packet. We repeat the changes at width two because high sites and endpoints matter. Suppose $H(4)/p\to0$. Then $s\to\infty$ since a fixed integer minimum determines one forward orbit. Take $n\sim(\log_3 s)/3$, two guards of length $g=\lceil\eta n\rceil$, and four successive $n$-edge interiors, with fixed small $\eta>0$. Most cyclic origins have all seven mandatory cut vertices at most $4s$ and $o(n)$ high sites in their window, by cyclic averaging. There are at least $p/2$ such distinct origins eventually. The earlier proof gives the necessary modulus and separation margins even if an interior passes through a high site. [Full source congruence, reciprocity, grid bound and four-segment placement](FOUR_COPY_TAILS.md)

Write $b=4n+2g$, $\varphi=\log_2(x_0/s)+b/(3s\log2)$. Along a window,
\[
 E_i=i\gamma+\log_2(x_0/x_i)+c_i,\qquad 0\le c_i\le b/(3s\log2).
\]
At every low site with $\tau_s< f_i=\{i\gamma+\varphi\}<1-\tau_s$, this forces precisely the allowed two-row representation $E_i=\lfloor i\gamma+\varphi\rfloor-k_i$, $k_i\in\{0,1\}$. Indeed the strip width is $2+O(b/s)$ and $b/s=o(\tau_s)$. The upper bound on $x_i/s$ in the veto tests follows directly from $\log_2(x_i/s)=f_i+k_i+c_i-b/(3s\log2)$. Irrational rotation visits the shrinking seam neighborhoods at $o(n)$ sites uniformly in the starting phase. This follows by first bounding their frequency by that of fixed neighborhoods, then taking the neighborhoods to zero. Mark those seams as well as the actual high sites.

Read each interior backwards with $\alpha=\gamma-1$. A step from current fraction $f$ has mechanical increment $m=1+\mathbf1_{f<\alpha}$ and next fraction $\{f-\alpha\}$. Split at returns to $I=[0,1/400)$. There is a uniformly bounded initial delay from any phase because the irrational rotation translates of the interior of $I$ cover the compact circle. The positive first returns from $I$ have exactly three words, of lengths $306,359,665$, by the rational cut certificate below. Discard incomplete end pieces and every return touching a marked vertex. Altogether $o(n)$ interior edges are discarded. Record every ordinary date on these pieces and the guard exponents. The full outer ceiling $(16s+7)/3$ gives $E_i=i\gamma+O(1)$ even at an outlier, so this costs $\exp(O(\eta n)+o(n))$ including all masks. Integer, seam and anchor boundaries give $O(b)$ common phase cells counting their singleton endpoints. The retained returns in any fixed environment have the same mechanical schedules and two-row conventions for every allowed path.

For a four-sum collision of one segment's ordinary numerators the four signed contributions must be zero at every clean letter. Indeed the fixed dates on discarded parts contribute zero at each such letter. At a clean date the four powers of two are a common dyadic unit modulo three times four digits in $\{1,2\}$. Their signed digit lies between $-2$ and $2$. Reduction from the last ternary letter backwards forces that digit to vanish and induction continues. Thus the two positive-sign bits and the two negative-sign bits have the same sum 0, 1 or 2 at every retained departure. A terminal bit absent from the numerator is fixed at the segment cut, or may be counted freely at a discarded boundary with bounded cost. Completions with discarded dates fixed still overcount all actual sources. The external separation theorem is used to get ordinary numerator equality from a quantized source collision before this digit argument. [PR200's unrestricted two-row energy and its supercritical lower bound](https://github.com/GettysburgResearch/collatz/blob/2346db2d49030ef385b73e1ee3e27dcbff86d2d9/research/six-hour-20261127/cycles/UNRESTRICTED_BINARY_FOURTH_MOMENT.md) · [Located fourth-moment argument](FOUR_COPY_TAILS.md)

Track separate veto states for the two positive-sign histories, resetting them at the start of each reverse return. A fixed terminal bit $y$ going to earlier bit $x$ uses actual exponent $a=m+x-y$ and requires $a\in\{1,2\}$. Advance its veto state by $a$ and discard when the output threshold is at least $y$. The two negative-sign histories retain their multiplicity and only obey the native two-row and equal-pair constraints. For prescribed old and new pair sums their orientation has two choices on an allowed extreme-to-middle transition and one otherwise, conditional on a fixed previous orientation. This is because all four bits move weakly in the same direction for each $m$. Sorting the two tracked (state,bit) pairs identifies symmetric future counts while retaining ordered transition multiplicities. In particular the estimate allows arbitrary correlations among the four trajectories.

For a return word $w$ of length $r$, let $R_w(i,j)$ count all these ordered continuations with fixed initial four-bit configuration of grade $i$ and final grade $j$. The count is the same for the different configurations of grade one by the two pair symmetries. Using the weight vector $v=(2,5,20)$, the exact certificate gives
\[
                         R_w v < (9/10)3^r v
\]
entrywise for all three returns. It starts at $2^{48}$ for each of the three initial conditions separately. After every exact integer transition sum it divides by three and rounds **up** at every state. By positivity, the resulting integer matrix divided by $2^{48}$ is an entrywise upper bound for $R_w/3^r$. The C++ code checks the unsigned range before every accumulation. An independent literal enumeration of all ordered four-bit paths with small toy vetoes checks the unrounded multiplicities and endpoint convention. The schedule enumeration brackets $\alpha$ using two rational atanh series. On the return anchor all itinerary cuts are $\{j\alpha\}$ and $\{1/400+j\alpha\}$ through step 665. The labeled clipped order and the unwrapped floors agree at both slope endpoints. Each cut moves less than the anchor width across that bracket, excluding an unrecorded transit across the whole anchor. Testing all breakpoints and open-cell midpoints covers the circle endpoint conventions.

The integer inequality $9^{10000}3^{665}<10^{10000}$ gives $(9/10)3^r\le3^{(9999/10000)r}$ for $r\le665$. Weighted row bounds multiply across retained returns after each veto reset. Discarded pieces and their new grade endpoints cost at most $\exp(o(n))$, including bounded weight ratios when a component starts. The ordinary numerator collision count on one interior is therefore at most $\exp(o(n))3^{(9999/10000)n}$. The located four-factor convolution bounds the accepted source paths by six times the geometric mean of these four counts per environment. Letting $\eta\downarrow0$ proves the stated exponent.

## Consequences at and above four

The product identity gives $0<(\sum e_i)/p-\gamma\le1/(3s\log2)$. If $\mu(\gamma)\le3$, it gives $s\ll_\epsilon p^{3+\epsilon}$, contradicting the preceding strict source exponent along any sequence with $H(4)/p\to0$. Consequently there is $c_0>0$ with $H(4)\ge c_0p$ on all sufficiently large periods in the bounded alternative.

For the extension in the ratio, put $\xi_i=\log_2(x_i/s)\bmod1$. The native edge gives $\xi_{i+1}=\xi_i+\gamma+O(1/s)\bmod1$. For every fixed nonzero integer $m$, cyclic telescoping therefore bounds
\[
  |1-e^{2\pi i m\gamma}|\left|p^{-1}\sum_i e^{2\pi i m\xi_i}\right|
       \ll |m|/s .
\]
The limiting angular measure is uniform by the Weyl criterion. For fixed sufficiently small $\kappa>0$, any odd site with $4s<x_i\le(4+\kappa)s$ has its fraction in $[0,\log_2(1+\kappa/4)]$. Its limiting proportion is at most that length. Choose the length below $c_0/2$ to get $H(4+\kappa)\ge c_0p/3$ eventually. This final inference uses only the distribution of the actual odd phases after the width-two theorem. All third-row dates in its collision argument were recorded on discarded pieces.

[Exact checker](check_rival_pressure.py) · [Integer transfer](rival_pressure.cpp) · [Exact output](RIVAL_PRESSURE_CONTROLS.json) · [Lean kernels](RivalPressure.lean)
