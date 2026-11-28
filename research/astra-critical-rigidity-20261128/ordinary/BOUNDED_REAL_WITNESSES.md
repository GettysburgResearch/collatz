# Rational merger sources in one bounded real interval

**Proposed theorem.** Let $z=u/q$ be reduced with $q>0$ odd and $3\nmid uq$. The [universal rational merger construction](UNIVERSAL_RATIONAL_MERGERS.md) can realize $z$ as a synchronous unequal-slope merger of $s_*$ and $3s_*$, with
$$
             |s_*|<2^{40},\qquad \operatorname{den}(s_*)=q3^d
                 \quad\text{for some integer }d\ge0.                   \tag{1}
$$
The real bound is absolute for both signs of $z$, all denominators and any chosen positive exponent $j$ with $q\mid 3^j-1$. The source is an odd rational. Its sign is unrestricted. The same construction retains entry time $O(j+\log(2+|(3^j-1)z|))$.

## Reversing the two parts of the physical construction

Start at level $j$ with $a_j=(3^j-1)z$. In the inverse U/E stages choose $4\le e_k\le9$ with $2^{e_k}a_k\equiv2\pmod9$ and set $a_{k-1}=(2^{e_k}a_k+1)/3$. These six consecutive exponents still cover the ternary units modulo nine. Each $a_{k-1}$ is a nonzero integer of the same sign as $a_k$, with $|a_{k-1}|\ge5|a_k|$. The original lower arm runs only even steps throughout these forward stages, so at level zero its value is $X=2^Ez$, $E=\sum e_k$. From the exact product
$$
 |a_0|=\frac{2^E}{3^j}|a_j|
       \prod_{k=1}^j\left(1+\frac1{2^{e_k}a_k}\right)
       \ge \frac{59}{64}\frac{2^E}{3^j}|a_j|
$$
we obtain $|X|\le(64/59)(3^j/(3^j-1))|a_0|<2|a_0|$. The product estimate follows from $\prod(1-d_i)\ge1-\sum d_i$ for $0\le d_i\le1$ and $\sum_{r\ge0}(16\cdot5^r)^{-1}=5/64$.

Now reverse the $n$ contracting translation blocks until the base translation has absolute magnitude at most 11. With $M=19683$, $N=16384$, $\lambda=N/M$, each inverse step on the absolute translation is $b'=\lambda b+\delta$ with $|\delta|\le38740/M$. Therefore
$$
                   \lambda^n|a_0|\le 11+\frac{38740}{M-N}<23.           \tag{2}
$$
The actual lower coordinate, in the original arm ordering, changes by $X'=\lambda X-C_W/M$ on each of these blocks. This remains true for the negative-translation construction, where the original lower arm receives the other of the two calendars. Their offsets are nonnegative and at most $C_{\max}=2^5(3^9-2^9)=613472$, attained at the nine final odd dates. Hence the original lower coordinate at the end of the reversed block sequence obeys
$$
           |X_n|\le \lambda^n |X|+C_{\max}/(M-N)<233.
$$
The finite seed and base calendar comprise at most 30 steps: 11 for the negative seed, one U after swapping, and at most 18 in the table. Each inverse native step obeys $|X_{\rm prev}|+1\le2(|X_{\rm next}|+1)$. Thus $|s_*|+1<2^{30}\cdot234<2^{40}$. The changed inverse level choices increase $|a_0|+1$ by at most a factor 512 per level, preserving the entry-time estimate. The lower preimage formula is $s_*=(2^tu-qC_W)/(q3^g)$. Its numerator is prime to $q$ since $q$ is odd and prime to $u$. This proves the exact denominator form in (1).

## The integrality limitation on ordinary targets

For every real bound $B$, infinitely many positive ternary-unit integer targets admit no integer source $|s_*|\le B$ for even a single-arm visit. For $m\ge2$ with $3\nmid m$, set $z_m=(4^m-1)/3$. These are distinct odd ternary units greater than one. Their first shortcut step is $2^{2m-1}$, after which they visit only powers of two and the cycle through one. Any one positive integer trajectory can visit at most one of the $z_m$. A nonpositive integer trajectory stays nonpositive. The finitely many bounded integer sources therefore cover only finitely many targets of this family.

In particular for infinitely many **ordinary** targets the compact rational witnesses in (1) necessarily have $d>0$. The argument uses targets already in the basin of one. Real boundedness of a rational merger witness does not supply a smaller ordinary integer reaching a prescribed target.
