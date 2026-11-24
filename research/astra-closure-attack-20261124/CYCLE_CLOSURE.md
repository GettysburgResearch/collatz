# Complete cycle denominators from moving affine centers

**Status.** Source-qualified written theorems for the actual reduced denominator. Two finite algebraic identities are kernel-checked. The unrestricted positive integer cycle exclusion remains open.

## 1. A prime-power certificate at any pair of cyclic boundaries

Use the shortcut map with one division by two on either branch. Let a primitive chronological word of length $A$ have $p>0$ odd inputs at positions $d_i$, positive raw denominator $D=2^A-3^p$, and carry $C=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i}$. Its distinguished rational cycle starts at $C/D$. Each rotation has the same reduced denominator $d=D/\gcd(D,C)$. Indeed $D$ is coprime to six, and the rotated affine identities realize the prescribed parities and preserve every negative prime valuation. An ordinary cycle requires $d=1$.

Split at **any two distinct boundaries** into $W=UV$. Let $P=2^{L_1},Q=3^{p_1},R=2^{L_2},S=3^{p_2}$ be the two sets of clocks, so $D=PR-QS$. Each affine block has a unique rational fixed point, its *center*, since no positive-length clock multiplier equals one. Write these centers in lowest terms as $c/a,e/b$ with positive denominators. Let
\[
 K=ae-bc,\qquad G=\gcd(|P-Q|,|R-S|).
\]

**Complete valuation transport.** $K\ne0$, and
\[
 \boxed{\frac{D}{\gcd(D,|K|G)}\mid d.} \tag{1}
\]
For each $\ell^v\parallel D$, at least $\max(0,v-v_\ell(K)-\min(v_\ell(P-Q),v_\ell(R-S)))$ powers survive. No list of primes is chosen in advance.

**Proof.** Let $x,y$ be the two integer boundary numerators over $d$. Centered iteration gives
\[
 P(ay-dc)=Q(ax-dc),\qquad R(bx-de)=S(by-de).
\]
Eliminating yields
\[
 D b(ax-dc)=dKP(R-S),\qquad D a(by-de)=-dKR(P-Q).
\]
Both $P,R$ are units modulo $D$. Bézout on $P-Q,R-S$ gives $D\mid dKG$, proving (1). If $K=0$, both blocks fix the same center and so does their composition. The unique fixed point of the composition is the actual positive rational start. The orbit thus returns at the first proper block, contrary to primitive parity. For multiple cuts the least common multiple of the certificates (1) divides the same $d$.

**Exact on nonresonant primes.** Applying the first identity to the unreduced numerators (denominator $D$) gives $ab C\equiv KP(R-S)\pmod D$. The two equalities $\gcd(D,P-Q)=\gcd(D,R-S)=G$ follow from $\gcd(P,Q)=\gcd(R,S)=1$. Also $a\mid(P-Q)$ and $b\mid(R-S)$. Consequently at every $\ell\mid D$ with $\ell\nmid G$ the truncated valuations of $C$ and $K$ agree exactly. When $G=1$ the certificate in (1) is exactly $d$, including at a one-bit cut of either parity. For a resonant cut it can miss everything. $U=0010$, $V=1111$ gives $D=13$, $K=-17$, $G=13$, reduced denominator 13, and minimum $259/13$. Each large-center claim below is a separate height estimate, not an automatic consequence of this exact modular transfer.

## 2. Full exponential rate for independent clocks, sharp half-rate on the exceptional ray

Write $h(t)=\log\max(|m|,n)$ for reduced $t=m/n$, $n>0$, including $h(0)=0$. Then $|K|\le2\exp(h(c/a)+h(e/b))$. Uniformly on positive clocks,
\[
 \log D=A\log2-O(\log A).
\]
In fact $\Lambda=A\log2-p\log3>0$ has the fixed-base linear-form bound $\Lambda\gg A^{-B}$ for some absolute $B$. Use $D=2^A(1-e^{-\Lambda})$, separately for $\Lambda\le1$ and $\Lambda>1$. No verification floor for integer starting values is needed. [Matveev, Corollary 2.3](https://doi.org/10.1070/IM2000v064n06ABEH000314) and [the repository's two-clock specialization, §4](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/profound-closure-20261122/BOUNDED_POWER_LANGUAGES.md).

If $L_1p_2-L_2p_1\ne0$, $u=P/Q,v=R/S$ are multiplicatively independent rational S-units. Corvaja–Zannier, Corollary 1, equation (1.3), applies to the **fixed group** $\langle2,3\rangle^2$, even as both words and both clock slopes change. For every $\epsilon>0$, outside a finite exceptional set of independent pairs, the sum of nonnegative local gcd contributions is at most $\epsilon\max(h(u),h(v))$. Its contribution outside $2,3,\infty$ is exactly $\log G$: both differences are odd and at least one has positive odd count, so three cannot divide both. The maximum height is comparable to $A$ since $L_1+L_2=A$. Thus $\log G=o(A)$. [Primary theorem and local-height convention, pp. 1–2](https://arxiv.org/pdf/math/0311030).

Consequently, along any sequence with $A\to\infty$ and independent clocks,
\[
 \log d\ \ge\ A\log2-h(c/a)-h(e/b)-o(A). \tag{2}
\]
In particular total center height $o(A)$ gives **$d=2^{A-o(A)}$**. The cuts may contain internally arbitrary expanding and contracting runs.

If the clock vectors are dependent, write $(L_i,p_i)=t_i(a_0,b_0)$ on their common primitive ray. Positivity gives $N=2^{a_0}>M=3^{b_0}$. The Euclidean algorithm on exponents for the coprime bases $N,M$ gives
$G=N^{\gcd(t_1,t_2)}-M^{\gcd(t_1,t_2)}<2^{A/2}$.
Thus the same small-center condition gives **$d\ge2^{A/2-o(A)}$**. The half-rate is attained: $W_m=(01)^m(10)^m$ has precisely one cyclic 00 and one 11 and is primitive. Its centers are 2 and 1. Its fixed point is $(2\cdot3^m+4^m)/(3^m+4^m)$, already reduced. Hence $d=3^m+4^m$ while $A=4m$.

**Moving powers.** For $W=U^rV^s$ the centers are those of the two unpowered words. A length-$a$ word with $j$ odd symbols has carry at most $2^{a-j}(3^j-2^j)\le3^a$ and center denominator at most $3^a$. Thus (2) and its half-rate counterpart apply whenever $|U|+|V|=o(A)$, even if the two words, their patterns, and their independent repetition counts all vary. Equation (2) also permits a positive fraction of uncompressed input if its actual center-height cost leaves a linear margin below $A\log2$. The earlier fixed-language result classified integral cycles in a prescribed schema. Here the estimates apply to the complete denominators of varying languages.

## 3. Arbitrarily complicated cuts in fixed dimension

Fix $k\ge2$ and partition into $k$ nonempty windows. Put $X_i=3^{p_i}/2^{L_i}$, with center $c_i$, so window $i$ acts by $t\mapsto X_i t+c_i(1-X_i)$. In independent variables define
\[
 F=1-\prod_i T_i,\qquad H=\sum_i c_i(1-T_i)\prod_{j>i}T_j.
\]
Exactly $F(X)=D/2^A,\ H(X)=C/2^A$. Their outside-$\{2,3,\infty\}$ logarithmic gcd is **$\log(D/d)$**. This retains the distinguished evaluation at every prime power.

The primitive polynomial $F$ is irreducible, being linear in $T_1$ with relatively prime coefficients. Modulo $F$ in the Laurent ring, $H$ becomes
\[
 c_k-c_1+\sum_{i<k}(c_i-c_{i+1})\prod_{j>i}T_j.
\]
The monomials in $T_2,\dots,T_k$ are distinct. Vanishing would make every center equal, contrary to primitivity by the fixed-point argument in §1. Thus $F,H$ are coprime. At least one center is nonzero; rotate to such a first center so $H$ has degree exactly $k$, or pass to a fixed rotation on a subsequence. The constant term of $F$ is nonzero. Clearing denominators shows $h(H)=O_k(1+\sum_i h(c_i))$, and $\max_i h(X_i)\asymp_k A$.

**Moving-target dichotomy.** Assume $\sum h(c_i)=o(A)$. On any sequence with $\log(D/d)\ge\eta A$ for fixed $\eta>0$, some infinite subsequence admits a fixed nonzero $z\in\mathbb Z^k$ satisfying
\[
 \sum_i z_iL_i=o(A),\qquad \sum_i z_ip_i=o(A). \tag{3}
\]
Indeed, apply Grieve–Wang, Theorem 1.2, over the rationals with $S=\{2,3,\infty\}$. For small enough fixed epsilon the small-gcd alternative on an infinite subset contradicts the given lower bound, since each local contribution is nonnegative. The remaining alternative yields a fixed nontrivial character on a subsequence in a single proper subgroup, translated by an element of small height. Its value has height $o(A)$. The two valuations of $\prod_i X_i^{z_i}$ now give (3). In particular if the normalized clock arrays converge to a two-row matrix with no nonzero rational vector in its real kernel, then $d=2^{A-o(A)}$. This uses the infinite-subset quantifier of the moving theorem and does not promote it to an effective period cutoff. [Grieve and Wang, Theorem 1.2 and Example 1.3](https://arxiv.org/pdf/1902.09109).

**Exceptional clocks still require an exponential denominator.** A scaling of PR185's dyadic argument gives
\[
 \log_2 d\ \ge\ A/(2^k-1)-o(A) \tag{4}
\]
under the same small-center hypothesis and without (3). For completeness rotate at a minimum of the partial products of the clock multipliers, including the initial empty product and excluding the terminal product. Since the full product is below one, all suffix products in that rotation are at most one, also across the wrap. The full translation is a sum of centers times differences of consecutive suffix products. Thus the boundary height $x_0$ there satisfies $x_0\le 2\sum|c_i|/(1-3^p/2^A)$, giving $\log_2(x_0+1)=o(A)$. With $c_i=b_i/a_i$ reduced, $2^{L_i}$ divides the nonzero integer $a_i d x_i-d b_i$ by the exact centered equation at the next boundary. Nonvanishing follows from primitive period. Therefore
\[
 L_i\le\log_2 d+\log_2(x_i+1)+h(c_i)/\log2+1.
\]
At each actual shortcut step $T(x)+1\le2(x+1)$. If the previous windows consume $J$ steps, then $\log_2(x_i+1)\le\log_2(x_0+1)+J$. This yields $J_{\rm next}\le 2J+\log_2 d+o(A)$, uniformly through these fixed $k$ cuts; induction gives (4). [PR185, dyadic budget for fixed words, §§3–5](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/profound-closure-20261122/BOUNDED_POWER_LANGUAGES.md).

## 4. First unsupported step in a universal exclusion

If every member of a putative sequence of primitive ordinary cycles of increasing period admitted a bounded number of cuts with total center height $o(A)$, then (4) would contradict that sequence. At most finitely many cycles could remain under such a universal structural theorem. Turning finiteness into a replayable finite search would also require an effective threshold or another argument excluding the residual cases. The actual minimum is at most $p/(3\Lambda)$. This bounds a real endpoint, not the rational height of the fixed point of its return word. A rational close to a small integer may still have numerator and denominator with bit lengths proportional to $A$.

In fact if a proper window sends ordinary $s$ to ordinary $t$ with clocks $N=2^L,M=3^j$, its reduced center denominator is **exactly**
\[
 \frac{|N-M|}{\gcd(|N-M|,|t-s|)} .
\]
Its carry is $(N-M)s+N(t-s)$ and $N$ is a unit modulo $N-M$. In a primitive cycle $s\ne t$. Thus any macroscopic window $L\gg A$ joining two subexponential endpoints ($\log(s+t)=o(A)$) has center height at least $L\log2-o(A)$, by the same absolute linear-form bound including expanding windows. Selecting several small endpoints actually obstructs the desired cheap partition.

There is an exact obstruction to substituting low-height endpoints for low-height centers in the moving-target theorem. Even grant cheap integer boundaries $t_0,\ldots,t_k=t_0$. Encoding the translations as $t_i-T_it_{i-1}$ now gives the polynomial identity
\[
 \sum_i(t_i-T_it_{i-1})\prod_{j>i}T_j=t_0(1-\prod_i T_i)=t_0 F .
\]
Coprimality fails before one obtains an inequality. Cutting at every single bit gives centers $0,-1$ but dimension $A$. Cutting into a bounded number of arbitrary words preserves dimension but loses the center-height hypothesis. No mechanism forcing simultaneous bounded dimension and cheap centers on arbitrary hypothetical integer cycles was found.

The Lean file **cycle_two_centers.lean** checks the centered displacement and the Bézout cancellation with the complete modulus. It does not formalize the cited Diophantine results. **cycle_closure_controls.py** tests the integer equations and the sharp half-rate family. Compared source heads include PR192 at be783656f0e889fe0d5318a2f7a9140099cb94b5, PR193 at c6cb5e66516a86c33a757154983bbddc822510de, PR194 at b1bf1f151a2da8936f80d229f132d0b7539ba42c, and PR188 at f98262be4ea40068dc88c779a767a9400a8bcaa3.

The direct strict Lean run on version 4.34.1 printed only propext, Classical.choice, and Quot.sound for both finite declarations. The final optimized control run checked 6,315 positive primitive words through length 12 and 63,382 cuts, including 4,046 dependent cuts. The certificate exceeded one in 63,356 cuts and equaled the full reduced denominator in 57,920. The sharp-rate family was replayed through $m=32$. These finite counts are independent of the unbounded Diophantine estimates.
