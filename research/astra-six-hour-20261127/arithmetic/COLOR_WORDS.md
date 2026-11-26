# Uniform word complexity of every Collatz component coloring

Let $f$ map the positive integers into an alphabet of size $b<\infty$, with $f(Tn)=f(n)$ for the shortcut map $T$. It can label any specified collection of positive cycles and escaping components. Write $P_f(N)$ for the number of different words $f(m),\ldots,f(m+N-1)$ across **all** positive starting positions $m$. These are words across adjacent ordinary starts. The parity itinerary along one orbit is a different object.

For $\beta=\log_3 2$ and $\theta=H_2(\beta)<1$, there is an elementary uniform estimate
\[
\log P_f(N)\ll_b N^\theta/\sqrt{1+\log N}. \tag{1}
\]
Retaining the labelled interval-compression theorem in Weaver's paper 28 as an external written input gives absolute $\gamma>0$ and
\[
\log P_f(N)\ll_b (\log(2N))^2+N^{\theta-\gamma}. \tag{2}
\]
The constant and $\gamma$ in (2) have the ineffectivity of that source. An effective source version gives $(\log_2 N)^2\log2+2^{86} N^\theta\log b/(1+\log_2N)^{3/2}$ with the ceiling on the clock understood. In particular the entire shift closure of every such $f$ has zero topological entropy. These are uniform catalogue bounds, including rare words. A typical block being constant is insufficient to obtain them. [Weaver, paper 28, Theorems A and 1](https://rstation.ai/problems/collatz/papers/28)

## The elementary catalogue

For a length $k$ shortcut path let $p_k(x)$ count its odd departures. The exact lift is
\[
T^k(x+2^kq)=T^k(x)+3^{p_k(x)}q,\qquad
p_k(x+2^kq)=p_k(x).
\]
For any $N=2^k$ consecutive starts each binary itinerary of length $k$ occurs exactly once. In particular, grade $p$ has $\binom{k}{p}$ starts. When $m=2^kq+a$, $0\le a<2^k$, and $0\le i<N$, all grade-$p$ endpoints have the form
\[
3^p q+T^k(a+i).
\]
The second term is an integer between zero and $3\cdot3^p$. Indeed $a+i<2^{k+1}$, and the real affine offset of any word of grade $p$ is at most $(3/2)^p-1$. The bound follows by successively applying the shortcut branches to zero and omitting the halving steps for an upper bound. Every relevant endpoint index relative to the common centre is calculated from $a$. Extending $f$ arbitrarily at zero is harmless, since zero is fixed and positive starts remain positive.

Put $L(N)=\log P_f(N)$ with $f(0)$ included, a change of at most one word. Pick a fixed large integer $D$ and write $p_*=\lfloor\beta k\rfloor-D$. Specify $a$ in $k$ bits. For each $p\le p_*$, specify the word from the catalogue in the interval $[3^pq,3^pq+3\cdot3^p]$. For the other grades give the colors of their starts individually. Then
\[
L(2^k)\le k\log2+\sum_{p=0}^{p_*} L(3\cdot3^p+1)
+(\log b)\sum_{p>p_*}\binom{k}{p}. \tag{3}
\]
The final sum is $O_D(2^{\theta k}/\sqrt{k})$ by Stirling, since $\beta>1/2$ and the tail near $\beta k$ has a geometrically decreasing ratio.

To run the induction on dyadic $N$, round $3\cdot3^p+1$ upward to the nearest power of two $2^{j_p}\le8\cdot3^p$. For $p\ge\beta k/2$, the denominator $\sqrt{1+j_p}$ is comparable with $\sqrt{1+k}$. Summing the geometric sequence $2^{\theta j_p}$ through $p_*$ shows that this part costs at most $C_1 3^{-\theta D}2^{\theta k}/\sqrt{1+k}$ times the induction constant, with $C_1$ independent of $D$. The segment $p<\beta k/2$ costs $O(2^{\theta k/2})$ times that constant. Choose $D$ so the first coefficient is below $1/4$, then take $k$ sufficiently large for the second to be below $1/4$. All intervals in the sum are shorter than $2^k$. Enlarge the induction constant to cover the tail, the residue, and the finitely many smaller $k$. Monotonicity of the catalogue count and the next dyadic length give (1) for all $N$. This is a word-encoding application of recursive parity-cylinder interval compression; Leen and Weaver developed the related endpoint-count estimates.

## Exact reduction to synchronous interval compression

At time $t$ label each start $x$ by $(p_t(x),T^t(x))$. For fixed $m\bmod2^t$ the entire partition of $m,\ldots,m+N-1$ into equal labels is independent of the quotient. Indeed lifting a start by $2^tq$ adds $3^p q$ to its endpoint on grade $p$, preserving and reflecting equality on that grade. The class labels of the actual word are fixed by $f(T^tx)=f(x)$. Consequently, if $G_t(N)$ bounds the number of endpoint-and-grade classes in **every** length-$N$ interval, then
\[
P_f(N)\le2^t b^{G_t(N)}.
\]
With $t=\lceil\log_2N\rceil^2$ this gives (2) from Weaver's Theorem A, and the stated effective alternative from Theorem 1. The [Lean module](ColorWords.lean) verifies the exact shortcut lift, equality in both directions for labelled fibres, and factorization of every actual shifted color word through its residue's partition. The entropy estimates and the external compression theorem are written arguments.

The existence of two positive basins supplies two colors and long single-color blocks. It supplies no independent assignment of colors to the many classes in one critical interval. Proving a lower entropy dimension at least $\theta$ for a nonconstant saturated coloring would contradict (2). That lower bound remains open. Zero shift entropy alone allows nonconstant label sequences.
