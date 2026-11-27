# The reflected mass constant and sharp ordinary octave tails

Use the definitions and frozen source law of Theorems A and B in the all-height census. Fix $0<\alpha<1/2$, set $\lambda=(\ln2)^2$ and $\kappa=1/\lambda$, and write $\Pr_k$ for the uniform probability on the odd integers of $[2^k,2^{k+1})$. The estimates below sharpen the polynomial losses in Theorem B.

**Reflected first-hit mass.** There is an absolute constant $C_*>1$ with
$$
 2^d p_d(-1)=C_*+O((3/4)^d).
$$
To see this, let $\mathcal V_s$ be the reflected integer gap words whose positive magnitudes first hit 1 after exactly $s$ edges. Put $b_s=\sum_{w\in\mathcal V_s}2^{s-E(w)}$. Once at 1 the reflected map has gap one and remains at 1. Splitting every length-$d$ inverse by its first hitting time gives the exact identity
$$
 2^d p_d(-1)=1+\sum_{s=1}^d b_s.
$$
For a first-hit word the $s$ departing magnitudes are distinct and exceed one. Its exact telescope from the start $u$ bounds $2^{s-E}\le(2/3)^s(s+1)/u$. Restrict first to $E\le6s$. Every starting magnitude satisfies $u\le2^{6s}$, by the positive inverse recurrence. Determinism permits each start just once. Hence the subtotal is at most $(2/3)^s(s+1)(1+6s\ln2)$. For $E>6s$, discard every terminal restriction. The geometric exponential moment gives $2^s\Pr(E>6s)\le [6(2/3)^6]^s$, whose base is less than $2/3$. These estimates imply $b_s\ll(3/4)^s$ and the asserted constant $C_*=1+\sum_{s\ge1}b_s$. At $s=1$ every odd exponent at least three is allowed, with total $b_1=1/3$, already giving $C_*\ge4/3$. The exact finite residue computation gives $1.454330<2^7p_7(-1)<1.454331$. This number is a lower approximation to the limiting constant.

**Sharp ordinary tails.** For each fixed $c\ge\kappa$,
$$
 \Pr_k(M_\alpha>c)\asymp_{\alpha,c} k^{1-c\lambda}.
$$
For $0<c<\kappa$, the same event has probability tending to one. In particular the exact order at $c=2\kappa$ is $1/k$.

For the upper bound use $p_d(-1)\le C_*2^{-d}$ in the stopped ordinary-source transfer (B3). With $d>j$, the reflected contribution is at most $C_*2^{-j}3^{-(d-j)}\le C_*2^{-d}$. Repeating the height and clock sum from (B4) now gives
$$
 \Pr_k(M_\alpha>c)\ll_{\alpha,c}
 k^{1-c\lambda}+k^{1-c\ln 4\ln(3/2)}+e^{-c'k}.
$$
The first power dominates for $c>0$.

For the lower bound inspect the independent native parity bits with positions from 1 up to $\lfloor\alpha k\rfloor-1$. Choose $d=1+\lfloor c\ln2(\ln k+C_\alpha)\rfloor$ with the uniform deterministic upper error for $g$. Count every occurrence of the bit pattern consisting of a zero followed by $d+1$ ones. At its last bit, the same physical source has traversed $d$ consecutive accelerated gap-one edges. The resulting valuation $v_3(y+1)\ge d$ proves the strict all-height exceedance through anchor 1. The count $N$ has mean $\mu=(\lfloor\alpha k\rfloor-O(d))2^{-(d+2)}\asymp_{\alpha,c}k^{1-c\lambda}$. Two distinct overlapping occurrences are mutually exclusive, since the later initial zero would have to be a one. Disjoint occurrences are independent. It follows that $\mathbb E N^2\le\mu+\mu^2$ and
$$
 \Pr_k(M_\alpha>c)\ge\Pr(N>0)\ge\frac{\mu}{1+\mu}.
$$
This gives the lower half, including the endpoint. The marker counts are entirely on the once-sampled ordinary source.

**Fluctuation scale.** The same estimates give
$$
 \limsup_{k\to\infty}\Pr_k\bigl(|M_\alpha-\kappa|\ln k>t\bigr)
      \le C_\alpha e^{-\lambda t}\qquad(t\ge0).
$$
Indeed the constants in both clock estimates can be taken uniform for $c\in[\kappa/2,2\kappa]$. The strict floor affects each bound by at most a constant factor. For the upper tail use $c=\kappa+t/\ln k$. For the lower tail use $c=\kappa-t/\ln k$ and $\Pr(N=0)\le(1+\mu)^{-1}$. For each fixed $t$ both choices lie in the indicated compact interval for all sufficiently large $k$.

These refinements give probabilities for the original uniform odd octaves. The macroscopic gate weighting may change their constants or their order on a fixed octave. The previously proved cumulative conclusions for that law require only domination by $1/x$ and the macroscopic lower mass.
