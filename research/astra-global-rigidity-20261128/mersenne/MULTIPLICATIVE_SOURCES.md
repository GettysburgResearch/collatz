# Squarefree ancestors whose prime factors carry termination certificates

Use the shortcut map $T(2a)=a,\ T(2a+1)=3a+2$. Write $b_y(n)$ for the indicator that the forward orbit from $n$ visits $y$, allowing time zero. A prime passes the test $F_v$ if its shortcut orbit visits $v$ and subsequently reaches 1 within five times the binary bit length of the prime. Each coordinate in this test can be checked by a finite integer computation. We use $v=5$ or 85, separately. Their two tails enter 8 on different edges.

## The fixed-source theorem

Fix a supplied positive integer $s$. Choose $y=s$ if $3\nmid s$. Otherwise strip powers of two from $s$ and take one odd shortcut to obtain $y\equiv2\pmod3$. Fix an integer $B\ge2$, $0<\theta\le1$, and $v\in\{5,85\}$. On each octave $(X,2X]$, form the set $\mathcal N_X$ of squarefree integers whose prime factors $p$ all satisfy
$$
                   B<p\le X^\theta,\qquad F_v(p)=1.
$$
Assume ordinary RH and the Collatz input theorems cited below. Then
$$
 \frac{\sum_{X<n\le2X,\;n\in\mathcal N_X} b_y(n)}
 {\#\{X<n\le2X:n\in\mathcal N_X\}}
 =\frac1X\sum_{X<n\le2X}b_y(n)+o(1)\ \longrightarrow\ d_y>0.       \tag{1}
$$
The integer $n$ in this statement physically visits the chosen point on the orbit of $s$. If $s$ misses 1, so does $n$, although **every prime factor of $n$ individually has a bounded certificate through the same prescribed target $v$**. Choose $B=j$, $\theta=1/j$ in succession and increase the octaves. This gives actual antecedents $n_j$ of $y$ whose smallest prime factor tends to infinity and for which $\log P^+(n_j)/\log n_j\to0$. The number of distinct prime factors tends to infinity. No uniformity in $j$ is used.

The sampling theorem below uses no RH. The use of ordinary RH in (1) is solely the input that enough *primes* pass the specified Collatz certificate. With the fixed set of primes in any reduced class modulo a fixed integer, the same squarefree and smooth sampling statement requires no RH. It then supplies examples with prescribed prime-factor congruences.

## Relative smoothing on sparse multiplicative sets

For each large integer $X$, let $\mathcal N=\mathcal N_X$ be any multiplicative subset supported on odd positive integers. Multiplicativity here means $mn\in\mathcal N$ exactly when both $m,n\in\mathcal N$, for coprime $m,n$. Assume there is a fixed $\alpha\in(0,1)$ such that, uniformly in $X$ and $2\le w\le z\le X^\alpha$,
$$
  \sum_{w<p\le z,\ p\in\mathcal N}\frac1p
  \ge \alpha\sum_{w<p\le z}\frac1p-O(1/\log w).                    \tag{2}
$$
Put $g=1_{\mathcal N}$, $G=X^{-1}\sum_{X<n\le2X}g(n)$, and $D=\prod_{p\le X,\,p\notin\mathcal N}(1-1/p)$. Matomäki and Radziwiłł's Lemma 10.5(i),(iii), using $r=g$ in (iii), yields $G\asymp_\alpha D$, with constants also depending on the fixed constant in (2). In particular $G\gg1/\log X$ by Mertens. Use their Theorem 1.9 with $f=g$, $\vartheta=\min(\alpha,1/16)$ and any $0<\rho<\rho_\alpha$. Its hypothesis is precisely $(\alpha,X^\vartheta)$-nonvanishing on the finite range in (2), uniformly for the moving prime support. The real-valued conclusion sets the twist to zero. In fact zero minimizes its nonnegative distance term prime by prime here. Write $J(g;X)=\prod_{p\le X,\,g(p)=0}(1+1/p)\asymp D^{-1}$, using the convergent product of $1-p^{-2}$. Take $h_0=\lceil(\log X)^2\rceil$, physical length $h=h_0J(g;X)$ and $H=\lfloor h\rfloor$. At each fixed tolerance $0<\delta<1/1000$, the exceptional proportion tends to zero and the local average differs from the octave mean $G$ by at most $(\delta+o(1))D$. The theorem's constants depend on the fixed parameters. First fix the tolerance and then let it decrease. Since $G\asymp D$, this proves
$$
   S(m)/G\to1\quad\text{in probability for }X<m\le2X,\qquad
   S(m)=H^{-1}\sum_{1\le j\le H}g(m+j).                            \tag{3}
$$
Floors contribute $O(1/(HG))=o(1)$ after normalization, and $H\ll(\log X)^3$. Averaging $S/G$ over the entire octave gives $1+O(H/(XG))=1+o(1)$. It is nonnegative, so the normalized mean absolute deviation tends to zero. Indeed the mean of $(1-S/G)_+$ tends to zero by boundedness and (3), and the mean of $S/G-1$ tends to zero.

Take $t=\lfloor(\log_2X)/4\rfloor$, $Q=2^t$. For each shift $j\le H$ the Leen pair estimate gives a set of at most
$$
                   O\!\left(Q\sqrt{(1+\log(1+j))/(1+t)}\right)
$$
residues modulo $Q$ on which $m,m+j$ fail counted fusion by time $t$. Off this set the two ordinary trajectories have a common state at time $t$. Equal odd-step counts make this test a property of the residue class for all representatives. All states through time $t$ exceed $X^{1/2}$ on the interval in question for large $X$. Hence a visit indicator for any fixed $y$ is equal at $m,m+j$ on a successful residue. The same is true of any bounded label $A_X\in[0,1]$ that agrees as soon as these truncated paths fuse, including a union of whole components or a prescribed mark of the state at a common later clock.

The error must be bounded *under the sparse weight*. For one odd residue $a\pmod Q$, Shiu's Theorem 1 applied to $0\le g\le1$ on the containing octave gives
$$
  \sum_{n\asymp X,\ n\equiv a\;(Q)} g(n)
   \ll \frac{X}{\phi(Q)\log X}\exp\!\left(\sum_{p\le3X,\,p\nmid Q}\frac{g(p)}p\right)
   \ll \frac{XD}{Q}.                                                   \tag{4}
$$
A fixed number of overlapping octaves covers all endpoints. Here $Q\le X^{1/4}$, $\phi(Q)=Q/2$, and $g(2)=0$. Mertens and a convergent $\sum p^{-2}$ compare the exponential to $D\log X$. On even residues the sum vanishes. Shifting the exceptional classes by $j$ leaves their number unchanged. Thus replacing $A_X(n)$ by $A_X(n-j)$ inside the $g(n)$-weighted sum has normalized cost $O(G\sqrt{\log\log X/\log X})$, uniformly for $j\le H$. Average over $j$, trim the two ends at cost $O(H/X)=o(G)$, then use the mean absolute deviation in (3). This proves
$$
 \frac{1}{XG}\sum_{X<n\le2X}g(n)A_X(n)
       =\frac1X\sum_{X<n\le2X}A_X(n)+o(1).                         \tag{5}
$$
No rate of convergence of the unweighted mark is needed. Matomäki and Radziwiłł's relative theorem is substantive here because $G$ may tend to zero. Applying an unweighted exceptional-density estimate directly to the sparse sample would not prove (5). [Matomäki–Radziwiłł, Theorem 1.9 and Lemma 10.5](https://arxiv.org/pdf/2007.04290) · [Shiu, Theorem 1](https://doi.org/10.1515/crll.1980.313.161) · [Leen's finite binary-residue estimate as used in Paper 209, Theorem 4.2](https://rstation.ai/problems/collatz/papers/209).

## Verifying the prime input and the fixed-source conclusion

For $v=5,85$, the ordinary-clock positive-density theorem applied at $2v$ gives $\gg_v U$ odd $a\le U$ whose trajectory reaches $2v$ in at most $10.46\log(a/(2v))+O_v(1)$ ordinary steps. Lift each to its unique $2^j a\in(U,2U]$. Its ordinary clock increases by $j$, within the $10.46\log(2^j)$ allowance, and its shortcut orbit visits $v$ since an ordinary visit to $2v$ is followed by the halving. The fixed tail reaches 1. Paper 233 §3 converts the ordinary clock to at most $4.833\log_2 U+O_v(\log\log U)$ shortcut steps. Its equation (1) at multiplier 1 and the joint mark at common deadline $5\lfloor\log_2 U\rfloor$ gives $\gg_v U/\log U$ primes in *each* sufficiently large octave passing $F_v$, under ordinary RH. All successful lifts count actual positive tracks. [Paper 233, §3](https://rstation.ai/problems/collatz/papers/233).

To obtain (2), partition $(w,z]$ into complete intervals $(2^jw,2^{j+1}w]$ and one final partial octave. On each sufficiently large full octave the marked reciprocal prime sum is $\gg_v1/\log(2^jw)$, while the full reciprocal sum there is $\ll1/\log(2^jw)$. The missed partial octave costs $O(1/\log w)$. Fixed excluded primes $p\le B$ enlarge only the constant in (2). Choose $\alpha$ below both this comparison factor and $\theta$. The cutoff $p\le X^\theta$ leaves (2) intact, and being squarefree puts no further restriction on $g(p)$. This supplies (5). Positive ordinary predecessor density for fixed $3\nmid y$ gives (1). The same positivity alone gives a positive lower relative fraction if one takes only the corresponding lower-density input. [Fixed-target input and attribution](https://rstation.ai/problems/collatz/papers/233).

Paper 233 §3 and its supplement already use Matomäki–Radziwiłł II, Theorem 1.7, for finite-order characters in a ratio-of-predecessors argument. Its §4 addresses prescribed marks on *partial products* of squarefree integers with a fixed number of prime factors. Formula (1) instead imposes the *individual* certificate on every prime factor and leaves their number free. No bound by a fixed number of factors follows. A termination proof for all these products, or a proof that their nonterminating fraction has zero liminf even for one choice of $v,B,\theta$, would imply ordinary Collatz. The needed inheritance from prime factors to their product is open.

The difference between the factors' certificates and a certificate for the product is visible at small integers. Both factors of $85=5\cdot17$ pass $F_5$, while the product goes directly down the 85 branch. Both factors of $36{,}489=3\cdot12{,}163$ pass $F_5$ in 5 and 44 shortcuts respectively. The product reaches 85 after 88 shortcuts and reaches 1 after 96, beyond its own deadline 80. The opposite branch change occurs at $45{,}313=113\cdot401$, where both primes pass $F_{85}$ and the product visits 5. [Exact finite controls](factor_certificate_controls.json) · [Checker](check_factor_certificates.py).
