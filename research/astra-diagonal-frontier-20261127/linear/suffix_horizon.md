# The remaining binary digits and the limiting basin label

This note refines the local hypotheses of the [short-interval first-landing theorem](local_first_landing.md), compares its information budget to current ordinary-time descent estimates, and records exactly what an infinite-residue limit says about a fixed basin.

## Two moduli and the effective residual scale

Keep its notation $X,M,\rho,k,r,R,q,t,\theta=\log_2 3$ and $\lambda=2-\theta$. One may also prescribe $x\equiv v\bmod3^h$ for any integer $h\ge0$. In the large-threshold proof, put $u=(v-r)2^{-k}\bmod3^h$. Specify the favorable offset at
\[
   w-3^b2^{-s}(t+3^qu)\pmod {3^{b+q+h}}.
\]
The extra precision is $q+h$. This gives $z=t+3^qm$ with $m\equiv u\bmod3^h$, hence the prescribed CRT class of the original $x$. The offset residue still lifts the favorable fixed cylinder since $b$ is large. Lemma 7 of Paper 48 concerns all these **offset** residues, even if the terminal inverse state $z$ itself happens to be divisible by three. The terminal state needs no further inverse edge when the native prefix has no odd input. The count at fixed $b,s$ gains exactly the factor $3^{-h}$. Thus (1), and separately its reserve restriction, holds with denominator $M2^k3^h$ whenever $k+h\le\kappa R$, decreasing the absolute $\kappa$ if needed. [Weaver and Wren, Paper 48 v2, equation (76)](https://rstation.ai/problems/collatz/papers/48)

There is a stronger range for a native prefix with few odds. Put $S=R-k$. With $S\to\infty$, $q+h\le\kappa S$, and $S^{-1/9}\le\rho\le1/2$, the first-landing and strict-reserve counts continue to hold. Here $k$ itself can approach $R$. Indeed the logarithm that sets the length of the selected inverse block is now
\[
       L=S+q\theta+O(1)
\]
at the large-threshold stage, since $w\asymp M$. Thus $b\asymp S$, and the assumed $q+h$ fits the extra precision $\delta b$. Native intermediates are at least $X2^{-k}=M2^S$, while the height correction $d/X<2^k/X=2^{-S}/M$ is negligible. In the reserve proof at most $q$ additional odd gaps are appended at the higher source, regardless of the number of its initial even halvings. In the auxiliary-threshold step $S$ decreases by at most $O(\log S+1)$ since $P=C_2\max(M,\rho^{-1})$, leaving the strict exponent slack used in the rotation count. For $r=0$, $q=0$ and the shortcut reduces each such $x$ by $k$ exact halvings. Increasing $k$ in this example simply acts on the same lower-scale population $x/2^k$.

For general dense native prefixes the constraint is real. If $q\asymp R$ and $R-k=o(R)$, the central length for locating a source near $X$ is $b=(R-k+\theta q)/\lambda+o(R)$, so
\[
                      \frac qb\ \longrightarrow
                   \frac{\lambda}{\theta}=\log_3(4/3).
\]
At exact total $s=2b$, only $\binom{2b-1}{b-1}\asymp 4^b/\sqrt b$ words are available. To populate every residue above even one fixed favorable cylinder at depth $b+q$ takes at least $c3^{b+q}$ distinct words. Consequently a uniform single-slice floor at that total requires
\[
       q\ \le\ b\log_3(4/3)-\tfrac12\log_3 b+O(1).                 \tag{1}
\]
This is a necessary bound for a full offset-cover on a fixed slice. It does not rule out combining clocks or using the actual smaller set of prescribed source-offset pairs. It explains why extending the existing $\delta b$ input to all positive native prefixes near their full binary horizon would require a very different quantitative result. Cutting a selected inverse block in two does not erase the $q$ low constraints at the fixed old source.

## What present descent estimates reach

On an interval of $N$ consecutive starts, with $L=\log_2 N$, Weaver's Theorem 1 bounds the number of exceptions by $CNL^3 2^{-cB}$ and reaches relative thresholds down to a constant multiple of $2^B/N$, for $B_0\le B\le L/2$. For the octave starting at $N$ this gives a visit below a constant multiple of $2^B$, at the stated physical clock. A fixed least bad integer $m$ would make every visit below $m$ a proof of convergence. In applying this comparison one should use an eligible unit $a$: if the least bad $m$ is even it already descends, and if it is odd and divisible by three then $a=U(m)<2m$ is a bad unit. The local first-landing theorem at $M=a$ supplies a bad fraction at least $c'/a\gg 1/m$ in each admitted rectangle, in particular in each ordinary octave after splitting into a fixed number of short windows.

Taking $B$ just below $\log_2 m$ to guarantee descent below $m$ leaves an upper bound of order $L^3 m^{-c}$ on the exceptional fraction. The published proof has $c\le1/2$. Neither this estimate nor its $O_A(L^{-A})$ restatement, whose reached height is instead $O(L^{K_A})$ with $cK_A>A+3$, gives an upper bound smaller than the competing reciprocal scale. Taking $A$ large while fixing $m$ also cannot preserve that last height condition as $X\to\infty$. Theorem 1 concerns every translated interval. Its Proposition 3 supplies examples of translated intervals with $\lfloor N/F\rfloor$ finite-deadline misses at threshold $Fx/N$; those intervals may lie arbitrarily far out and are not counterexamples to a statement restricted to a chosen octave. [Weaver, Paper 191 v2, Theorem 1, Proposition 3, and proof after equation (9)](https://rstation.ai/problems/collatz/papers/191)

## The limiting residue conditional is constant

Let $f$ be a fixed $0$-$1$ component label preserved by the shortcut. Let its natural mean be $p$. Density-one adjacent coalescence gives
\[
                 X^{-1}\sum_{X\le n<2X}|f(n+1)-f(n)|\to0.
\]
For any fixed integer modulus $Q$, the counts in adjacent residue classes differ by $o(X)$: translate the interval by one, then bound discrepancies by the absolute-difference sum and the two endpoints. All $Q$ class counts therefore equal $pX/Q+o(X)$. In particular the joint laws of $(n,f(n))$ for uniform $n\in[X,2X)$, embedded in $\mathbb Z_2\times\{0,1\}$, converge weakly to
\[
                  \text{Haar}_{\mathbb Z_2}\ \otimes\ \mathrm{Bernoulli}(p).
\]
Finite binary cylinders determine this weak limit. The same argument works with the joint $2$-adic and $3$-adic coordinates, using fixed CRT classes. Weaver's Paper 13, Corollary 2, gives a quantitative predecessor of this observation: for every modulus sequence $Q=X^{o(1)}$ the octave averages of an invariant label in each individual residue converge uniformly to its natural mean. The qualitative fixed-modulus consequence requires only adjacent coalescence. [Weaver, Paper 13, Proposition 1 and Corollary 2](https://rstation.ai/problems/collatz/papers/13)

If $0<p<1$, this limit puts both mark values above almost every residue point. It is not the graph of a Boolean function of that point. An arbitrary function on positive integers can always be extended to a Borel function on $\mathbb Z_2$ because the original domain is countable; such an extension imposes no graph-law identity in the weak limit. Conversely, if an invariant Boolean label can be approximated to arbitrarily small upper density of error by fixed dyadic-cylinder rules, it has $p=0$ or $p=1$: for every such rule of Haar mean $u$ its limiting error is $p(1-u)+(1-p)u\ge\min(p,1-p)$. Applied to convergence, positive predecessor density for every fixed bad unit and for 1 then rules out any counterexample. No dyadic approximability of the complete positive-integer convergence label is proved here.
