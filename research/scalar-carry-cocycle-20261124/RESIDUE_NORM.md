# Full numerical gcd through a residue-defect norm

Use the shortcut map $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. A cyclic parity word has $p\ge1$ odd steps and $A$ total steps. Let $d_i$ be the clock of its $i$-th odd step, $d_0=0$, and $d_p=A$. The corresponding positive gap word has positive gaps. Its full cycle numerator and denominator are
$$
C=\sum_{i=0}^{p-1}3^{p-1-i}2^{d_i},\qquad D=2^A-3^p>0.
$$
Any positive integral cycle must satisfy $Dq=C$. Below assume $\gcd(A,p)=1$.

## RN1: a full-gcd norm certificate

Rotate at an odd position minimizing the periodic discrepancy $p d_i-Ai$. Then $e_i=p d_i-Ai\ge0$, $e_0=0$, and the residues $r_i=e_i\bmod p$ permute $0,\ldots,p-1$. Write $e_i=r_i+p k_{r_i}$; all $k_r\ge0$, $k_0=0$. Let
$$
F(X)=\sum_{r=0}^{p-1}2^{k_r}X^r,\qquad H(X)=(X-1)F(X)\pmod {X^p-2},
$$
where $H$ is represented in degree less than $p$. If $f_r=2^{k_r}$, its coefficients are $2f_{p-1}-f_0$ at degree zero and $f_{r-1}-f_r$ at degree $r\ge1$. Thus the norm depends on differences in residue order, not simply on the maximum time-order discrepancy.

For every common divisor $m>1$ of $C,D$, both 2 and 3 are units modulo $m$. Choose integers $u,v$ with $up-vA=1$ and put $x=2^u3^{-v}\pmod m$. Since $2^A=3^p$, we have $x^p=2$, $x^A=3$, and $x^{e_i}=2^{d_i}3^{-i}$. Consequently $C=3^{p-1}F(x)\pmod m$ and $H(x)=0\pmod m$.

On the free rank-$p$ integer ring $R=\mathbb Z[X]/(X^p-2)$ let $M_H$ be the multiplication matrix of $H$, and set $J=\det M_H$. The evaluation row $(1,x,\ldots,x^{p-1})$ annihilates $M_H$ modulo $m$. Multiply by its integer adjugate; the first coordinate gives $m\mid J$. This applies to every common divisor, including full prime powers; hence
$$
\boxed{\gcd(C,D)\mid J,\qquad J=\prod_{j=0}^{p-1}H(2^{1/p}\zeta_p^j)\ne0.}
$$
Nonvanishing follows from Eisenstein irreducibility of $X^p-2$ and $F\ne0$ of degree less than $p$, as $X-1$ is nonzero in that field. The product formula is the usual diagonalization of multiplication over the complex roots. The result for $m=1$ is automatic. In particular $|J|<D$ excludes integrality. A bound solely on polynomial common factors does not yield this full numerical divisibility.

## RN2: mechanical itineraries are completely settled

For a balanced periodic mechanical parity word with coprime counts, rotate as above. The odd-clock positions have discrepancy spread less than $p$, so $k_r=0$ for every residue. For example, at the normalized rotation $d_i=\lceil iA/p\rceil$, the discrepancies are exactly a permutation of $0,\ldots,p-1$. Hence $F=1+X+\cdots+X^{p-1}$ and $H=1$. RN1 yields $\gcd(C,D)=1$. An integral cycle needs $D=1$. For $A\ge3$, $D\bmod8$ is 5 or 7, impossible. The only remaining positive denominator-one case is $(A,p)=(2,1)$, giving the standard cycle through one.

Here is the connection for all eventual mechanical shortcut itineraries. A lower mechanical binary word with slope $\alpha$ and intercept $\rho$ has digits $\lfloor(t+1)\alpha+\rho\rfloor-\lfloor t\alpha+\rho\rfloor$. For rational slope $0<p/A<1$ in lowest terms, it is periodic with period $A$. The successive odd positions have the form $\lceil(k-\rho)A/p\rceil-1$; the rounding errors lie in a single half-open interval of length one. Subtract the first position: the full discrepancy spread is strictly less than $p$. Upper mechanical words use the analogous floor expression and the same argument. Thus the above norm identity applies. To pass from a periodic parity tail to an actual cycle: equal first $L$ parity digits of two positive sources imply $2^L$ divides their difference, using the full affine identity and oddness of $3$. Equal entire parity tails force equality. In particular an actual orbit with a periodic tail is periodic from the start of that tail.

For irrational mechanical slope, the number of distinct length-$L$ factors is at most $L+1$, because the rotations of the intercept circle are partitioned by the $L+1$ boundary points of the digit coding. The word is not eventually periodic (its limiting odd density is irrational). On an actual nonperiodic shortcut orbit, all states are distinct and $T(n)+1\le(3/2)(n+1)$. For sufficiently large $L$, the first $L+2$ states are all below $2^L$, since $(3/2)^L=o(2^L)$. Pigeonhole among their length-$L$ parity words gives two identical words; the congruence just proved forces the two states to be equal, a contradiction. The same proof excludes a nonperiodic parity tail whose factor count has linear slope strictly below $1/\log_2(3/2)$ (choose enough starting states just above the factor count). Slopes 0 and 1 give eventually constant words. An all-even positive tail is impossible by binary divisibility; an all-odd tail gives $T^j(n)+1=(3/2)^j(n+1)$, impossible for all $j$ by the same divisibility.

Thus every actual eventually mechanical shortcut orbit reaches one. Mechanical/Christoffel cycle exclusions and complexity-based arguments have prior art; this is a separate direct reconstruction using the full-gcd norm, not a claim that the whole class was previously unstudied. In particular see Kevin Knight, "Collatz high cycles do not exist", Discrete Mathematics 349 (2026), 114812, and the repository's prior cycle and complexity work. The norm framework extends beyond balanced words.

## RN3: a nontrivial full-denominator family

Consider profiles $k_r=1$ on one interior residue interval $u\le r<v$ with $0<u<v<p$ and zero elsewhere. Then $H=1+X^v-X^u$. We prove a uniform exponential norm saving:
$$
|J|<(2999/1000)^p.
$$
Write $\rho=2^{1/p}$, $a=\rho^u$, $b=\rho^v$, and $y_j=|1+b\zeta_p^{jv}-a\zeta_p^{ju}|^2>0$. Its mean $M=1+a^2+b^2$ is below 9. If $u\le3p/4$, then $a^2\le2^{3/2}<3$, so $M<8$; AM-GM proves the claimed bound.

If $u>3p/4$, set $t=p-u$ and $s=p-v$, so $0<s<t<p/4$. In the squared modulus the two frequencies $\pm t$ come only from the term with coefficient $-a$; these are distinct from $\pm s,\pm(t-s)$. Orthogonality implies the variance of $y_j$ is at least $2a^2\ge2$. Every $y_j\le25$. On $(0,25]$, $\log y\le \log M+(y-M)/M-(y-M)^2/(2\cdot25^2)$ by Taylor's theorem and the bound on the second derivative. Average this inequality, then divide by two for the logarithm of the norm per root. It follows that $|J|^{1/p}\le 3e^{-1/1250}<2999/1000$, where the last strict inequality follows from $e^x\ge1+x$ and rational comparison. Nonzero $y_j$ follows from RN1.

For a nonstandard positive integer cycle, all its odd states exceed one. Multiplying their exact equations gives $p\log_2 3<A<2p$. The standard effective two-logarithm lower bound (Matveev, as used in PR185 scientific commit e04daab0a0ddd59c80f5d16a51b9943fd5149e6c, PRIMITIVE_DENOMINATOR_GROWTH.md) gives $A\log2-p\log3\ge c p^{-K}$ for effective positive absolute constants $c,K$. Thus $D\ge c3^p p^{-K}$, eventually strictly greater than $(2999/1000)^p$. RN1 excludes every sufficiently large period in this class. This is an effective finite-period reduction, not an enumeration or complete exclusion of the finitely many remaining periods. It is conditional only on the cited established logarithmic-forms theorem, which is not formalized here. The endpoint interval $v=p$, higher elevations, arbitrary defect profiles, and noncoprime $A,p$ are outside this result.

## Next proof obligation

For arbitrary primitive actual cycle words, obtain a full-denominator obstruction even with noncoprime clock counts and multiple residue-order defect intervals. The exact norm reduces the coprime case to a concrete integer invariant but need not be small for every profile. A successful extension would need arithmetic constraints on profiles arising from actual cycles, rather than merely counting or bounding individual coefficients. No universal norm bound is claimed.

Finite BigInt controls check complete gcd divisibility on small coprime words, the balanced gcd, and the numerical norm bound on bounded interior interval examples. The corresponding finite ring identities have draft Lean source; the norm determinant, mechanical theorem and analytic bound are written proofs, not claimed to be Lean-compiled.
