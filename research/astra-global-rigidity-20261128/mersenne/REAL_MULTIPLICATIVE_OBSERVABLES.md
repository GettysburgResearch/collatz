# Uniform decorrelation from real bounded multiplicative functions

Let $I=(X,2X]\cap\mathbb N$ with $X$ an integer, and write $E$ for its normalized counting average. Let $A_X(n)\in[0,1]$ be any mark that is equal on two physical starts in the expanded octave whenever they counted-fuse at time $t=\lfloor(\log_2 X)/4\rfloor$. Examples include membership in a union of components, a visit to a fixed target, and a mark of the state at a common later clock. For a visit to a fixed target the agreement follows because all states through $t$ exceed the target. Uniformly in such marks and **all** real multiplicative functions $g_X:\mathbb N\to[-1,1]$,
$$
                |E(A_Xg_X)-(EA_X)(Eg_X)|\ll (\log X)^{-1/150}.       \tag{1}
$$
In particular for a fixed basin mark $b_y$ with density $d_y$, $E(b_y g_X)-d_y Eg_X=o(1)$ even when $g_X$ varies with the octave. The displayed rate concerns centering at the actual octave mean.

Take $H=\lfloor\exp(\sqrt{\log X})\rfloor$. By the Leen binary-residue tail, replacing $A_X(n)$ by $A_X(n-j)$ in the weighted average costs at most $O(\sqrt{\log(2H)/\log X}+2^t/X)=O((\log X)^{-1/4})$, uniformly for $1\le j\le H$. This uses only $|g_X|\le1$. Average over the shifts and trim the two ends at cost $O(H/X)$. The expression $E(A_Xg_X)$ is now within these errors of
$$
              E_m\left[A_X(m)H^{-1}\sum_{1\le j\le H}g_X(m+j)\right].
$$
In Matomäki and Radziwiłł's published Theorem 1, take $\delta=(\log X)^{-1/150}$. Its error on typical intervals is $O(\delta+(\log\log H)/\log H)=O(\delta)$. The normalized exceptional count is
$$
  \ll \frac{(\log H)^{1/3}}{\delta^2H^{\delta/25}}
       +\frac1{\delta^2(\log X)^{1/50}}=O(\delta).
$$
The first term decreases faster than any fixed negative logarithmic power. On the exceptional intervals the difference is at most $2+O(1/H)$. This proves (1) in mean absolute value. [Matomäki–Radziwiłł, Annals 183 (2016), Theorem 1](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf) · [Leen's pair theorem, exact binary-residue form in Paper 209](https://rstation.ai/problems/collatz/papers/209).

Both $b_5$ and $b_{85}$ have positive density, and their supports are disjoint. Thus (1) holds for two demonstrably nonconstant marks. For example Liouville's function has octave mean tending to zero by the prime number theorem, so each of its signs occupies half of each of these two basins in relative natural density. This calculation uses the same real phase on both basins. The case of complex-valued multiplicative functions has a twist in the short-interval main term and does not follow by taking real and imaginary parts, which need not themselves be multiplicative. Paper 233's supplement already uses the Matomäki–Radziwiłł II complex short-interval theorem for finite-order characters in its ratio-of-predecessors argument. [Paper 233, §3 and reference 15](https://rstation.ai/problems/collatz/papers/233).

## An explicit smoothness cutoff with no RH input

Fix $0<c<1/150$ and set $u=c\log\log X/\log\log\log X$, $Y=X^{1/u}$ for sufficiently large $X$. Take the real multiplicative function $g_X(n)=1_{P^+(n)\le Y}$, with $P^+(1)=1$. Hildebrand's uniform smooth-number theorem gives $\Psi(X,Y)=(1+o(1))X\rho(u)$, and gives the analogous formula at $2X$ with parameter $u+(\log2)/(\log Y)$. The Dickman ratio estimate gives a ratio $1+o(1)$ at this increment since $u\to\infty$ and $\log(u+2)/\log Y\to0$. Here $Y$ greatly exceeds $\exp((\log\log(2X))^2)$, within the theorem's range. Subtracting yields
$$
 Eg_X=(1+o(1))\rho(u)=(\log X)^{-c+o(1)}
$$
by the Dickman asymptotic $\log\rho(u)=-u(\log u+\log\log(u+2)-1+o(1))$. Dividing (1) by this mean proves $E(A_X\mid P^+(n)\le Y)=EA_X+o(1)$. In each sufficiently large octave a positive proportion of the indicated smooth integers therefore physically visit any fixed unit target $y$. Applying the unit reduction to a supplied ordinary starting point gives an ancestor in its component. This bound controls prime sizes. Individual certificates for those primes require the separate sparse-support argument in [Squarefree ancestors](MULTIPLICATIVE_SOURCES.md). [Hildebrand–Tenenbaum, Theorem 1.1 and Corollaries 2.3–2.4](https://jtnb.centre-mersenne.org/article/JTNB_1993__5_2_411_0.pdf).
