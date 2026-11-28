# Almost a full binary word after an actual first landing

**Source-qualified written theorem.** Keep the ordinary odd first-landing law $p_{B,X}$, its distant limit $\mu_B$, and the limiting scaled-height and ternary density $G$ of [the local profile](LOCAL_LANDING_PROFILE.md). The only distant-octave comparison used below is the same uniform PR213 relative landing input used there. All moduli and intervals in this theorem may grow with the actual integer floor.

Let $\mathcal I$ be any partition of $[0,1]$ into at most $T$ intervals, with endpoint choices made consistently. For $m\ge0$, $k\ge1$, let $P$ denote the law under $\mu_B$ of
\[
   (\mathcal I(Y/B),\,Y\bmod 3^m,\,Y\bmod2^k)
\]
with a separate cemetery atom. Let $Q$ use the projection of $G$ onto the first two coordinates, an independent uniform odd residue modulo $2^k$, and zero cemetery mass. There are absolute constants such that, uniformly in the interval endpoints and both moduli, for $s=B/(T 3^m2^k)$ sufficiently large,
\[
                  \|P-Q\|_{\rm TV}\le C(1+\log s)^{-1/9}.             \tag{1}
\]
For actual uniform odd sources in $[X,2X)$, add $C(1+\log(X/B))^{-1/9}$ on the right when the separation is sufficiently large. Thus even an arbitrarily slowly diverging multiplicative slack suffices. The first $k$ shortcut parities after landing are a permutation coding of the binary residue, with the first parity fixed odd. These $k-1$ following bits are jointly close to unbiased independent bits, also jointly independent of the specified incoming height and ternary information, in exactly the range (1).

## Counting the finite word templates with growing clocks

In equation (3) of [the local profile](LOCAL_LANDING_PROFILE.md), choose $v\ge v_0$, $L=\lceil C_0v\rceil$, and a fresh octave $[Be^v,2Be^v)$. Retain words $w$ of odd grade $j\le L$ and total binary clock $D_w\le4L$. There are at most $2^{4L}$ such words by counting ordered compositions of each binary total, including the empty word. For every $v\le\gamma\log B$ with small fixed $\gamma$, the omitted actual probability is $O(e^{-cv}+B^{-c})$ by the uniform fresh-interval estimates in [the entropy theorem](FIRST_LANDING_ENTROPY.md).

At grade $j$, an exact compatible target lies in one particular odd class modulo $2\,3^j$. All actual height constraints are lower or upper bounds on $u=y/B$. The affine offsets of the full word and its suffixes are nonnegative and at most $(3/2)^j-1$, by iteration of the largest forward map $x\mapsto(3x+1)/2$. Consequently the original interval and $I_w$ have symmetric difference contained in two intervals of length at most $(3/2)^j/B$ each, with endpoints included as needed. This holds also when one of the intervals is empty. Each such interval contains $O(1)$ compatible integer targets because their spacing is $2\,3^j$ before division by $B$. The sum-norm discrepancy from dropping all offsets is $O(e^{-v}2^{4L}/B)$. Replacing the true probability per source by $2e^{-v}/B$ adds $O((Be^v)^{-1})$, since the number of retained sources is at most the fresh octave size. The relative passage input, uniformly on all events including the cemetery, then gives the sum-norm grid comparison with $g_v$ with error
\[
     C[v^{-1/9}+e^{-cv}+B^{-c}+e^{-v}2^{4L}/B].                     \tag{2}
\]
Independently, the fixed-$v$ argument in (4) of the local profile and its $L^1$ Cauchy limit give $\|g_v-G\|_1\le Cv^{-1/9}$.

For one word $w$, intersect $I_w$ with each cell of $\mathcal I$. Its ternary cylinder of depth $j$ intersects at most $3^{(m-j)_+}$ measured ternary classes, and each compatible pair determines one class modulo $3^{\max(j,m)}$. For each odd binary class modulo $2^k$, CRT then gives exactly one joint progression. Counting its representatives in each interval differs from the length prediction by at most two. Weighted by $2e^{-v}/B$, the sum of these errors for the word is $O(e^{-v} T 3^m2^k/B)$. The length prediction is precisely the projected product of its continuum template $e^{-v}1_{I_w}1_{\mathcal C_w}$ with independent uniform odd binary phase. Sum over the retained words, add (2), and finally replace $g_v$ by $G$ under projection. Take $v=c_1\log s$, choosing $c_1>0$ small enough for both the fresh estimate and $2^{4L}\ll s^{1/2}$. This proves (1). The actual-octave extension is a further application of the relative passage estimate to the joint grid event.

For the shortcut coding let $S(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. A prescribed length-$k$ parity word selects exactly one input class modulo $2^k$: fixing a compatible prefix of length $i$, shifting the source by $2^i$ leaves its earlier parities unchanged and changes the next state by the odd integer $3^{\#\mathrm{odd\ in\ the\ prefix}}$. Induction proves bijectivity, and odd initial sources are exactly the words with first letter one. Thus (1) applies to arbitrary events in the entire future parity word, with no assumption that individual tested words have a positive limiting probability.

At zero slack an unconditional statement of this strength fails. Set $B=2^k$, $T=1$, $m=0$. The binary residue identifies each odd numeric label $1\le y\le B$. Except for cemetery mass tending to zero, $\mu_B$ is supported on the ternary units, as every positive-time odd image is a unit. The uniform binary law assigns asymptotic mass $1/3$ to residues whose representative is a multiple of three. Hence the variation distance is at least $1/3-o(1)$. This test uses only the measured binary residue.

## Entropy of the future parity word

In the same regime $s\to\infty$, for $T=1,m=0$ and $k$ possibly increasing, the law of the binary residue, conditioning on a finite landing, satisfies
\[
       \mathsf H(Y\bmod2^k)=(k-1)\log2-o(1).                           \tag{3}
\]
This also holds on the distant actual source sequences in (1). To see uniform integrability, compare the finite landing probabilities $p$ with uniform measure on the odd source grid of size $N=\lceil B/2\rceil$. After conditioning, $Np(y)$ has uniformly bounded positive log-information moments of every fixed order under $p$, by [the entropy theorem](FIRST_LANDING_ENTROPY.md). If $p'$ and $q'$ are the images of $p$ and uniform grid measure under the binary projection, the likelihood ratio $p'/q'$ is a conditional expectation of $Np$ under uniform grid measure. Convexity of $t(\log_+t)^2$ gives a uniform second positive information moment for the image. Also $q'$ differs multiplicatively from uniform on odd residues by $1+O(2^k/B)=1+o(1)$. The negative entropy integrand near zero is uniformly negligible. Thus the relative entropy of the projected distribution against the flat binary law tends to zero: first clip $t\log t$ to a bounded Lipschitz function and use (1), then remove the clips by the uniform integrability. This proves (3) even if the word length is just an arbitrarily slowly diverging additive number of bits short of $\log_2 B$.
