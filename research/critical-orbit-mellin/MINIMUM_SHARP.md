# The sharp quadratic tail of the least-predecessor law

**PROPOSED.** In the notation of [the fixed-depth bound](MINIMUM_TAIL.md) and [the all-depth density transfer](../fixed-floor-shells/PREDECESSOR_MINIMA.md), there is an absolute constant $c>0$ such that
$$
 c\theta^2\le d(\theta)\le\theta^2\qquad(0<\theta\le1).
$$
The lower bound uses many depths in the central window of the critical tilted law. A restriction on the final letters makes overlaps between different depths summable.

Put $z=\log(1/\theta)$ and $q_*=z/\log(3/2^{4/3})$. For sufficiently large $z$ use the integers $q_*-\sqrt{q_*}\le q\le q_*$; smaller $z$ are covered by monotonicity and adjustment of the constant. At each such $q$ take $A=\lfloor(q\log3-z)/\log2\rfloor$, so $D=2^A/3^q\in(\theta/2,\theta]$ and $|A-4q/3|\ll\sqrt q$. Under iid letters of law $3\cdot4^{-a}$, the local probability of $S_q=A$ is $\asymp1/\sqrt q$ uniformly here. This follows from the negative-binomial formula in the fixed-depth proof by Stirling, with bounded standardized deviation. Condition on this total.

With constants $B,K$ independent of $q,A$, a positive fraction of words satisfy both
$$
 C\le B3^q,\qquad
 a_q+\cdots+a_{q-k+1}\le 8k/5\quad(K\le k\le q).
$$
Indeed the fractional moment argument of the fixed-depth proof only uses the local lower bound at $A$, so $B$ can make the first failure probability at most $1/4$. Unconditionally the suffix of length $k$ exceeds $8k/5$ with probability $\le e^{-ck}$ by a Chernoff bound, since the tilted mean is $4/3$. Conditionally this bound increases by at most $O(\sqrt{q/(q-k)})$ for $k<q$, by the local upper bound on the complementary prefix, or by $O(\sqrt q)$ for any $k$. Sum the first estimate through $k\le q/2$ and the second beyond $q/2$; choosing $K$ large makes this additional failure probability at most $1/4$ uniformly. Write $E_q$ for the union of the resulting ternary cylinders. Distinct words with this fixed total have distinct numerators $C$, and the first restriction bounds the number per residue by $B+1$. As in the fixed-depth proof,
$$
 \mu_3(E_q)\asymp 3^{-q}\binom{A-1}{q-1}\asymp \theta^2/\sqrt{q_*}.
$$

For two selected depths $r<q$ write $l=q-r$. On a given ternary cylinder $t\equiv t_0\pmod{3^r}$, the numerators of all possible longer marked words satisfy
$$
 0<C\le B3^q,\qquad C\equiv 2^At_0\pmod{3^r}.
$$
Thus they lie in a single progression of at most $B3^l+1$ terms. Set $k=\lfloor l/2\rfloor$, $J=1+\lfloor8k/5\rfloor$. For $k\ge K$ each possible longer numerator must decode at least $k$ letters with total valuation at most $J-1$. This property is determined modulo $2^J$. To decode from odd $C_j$ at depth $j$, take $a_j=v_2(C_j-3^{j-1})$ and $C_{j-1}=(C_j-3^{j-1})/2^{a_j}$. At these $k<q$ layers the previous numerator of any actual word is odd. If one starts with an odd uniform dyadic integer in place of $C_q$, each valuation has the law $\Pr(a=n)=2^{-n}$ for $n\ge1$, and conditional on that valuation the new odd quotient is uniform. This follows by subtracting the fixed odd constant from a uniform odd residue and stripping its exact power of 2. The valuations are therefore independent. For a fixed finite residue of precision $J$ the event of total at most $J-1$ depends only on those $J$ bits, since they certify the exact valuations and the parity of the final quotient. Even residues cannot be numerators. A Chernoff bound under this geometric law of mean 2 shows that at most $O(2^J e^{-c'k})$ residues modulo $2^J$ pass the test.

The progression has odd step and $2^J\ll3^l$, so each accepted residue occurs at most $O_B(3^l/2^J)$ times. The number of eligible longer numerators in the progression is consequently $O(3^l e^{-c''l})$. Each determines at most one longer ternary cylinder because $A$ is fixed at depth $q$. Dividing by $3^l$ proves
$$
 \mu_3(E_q\mid t\equiv t_0\bmod 3^r)\ll e^{-c''(q-r)}
$$
for every shorter residue, with a larger absolute constant for $k<K$. In particular $\mu_3(E_r\cap E_q)\ll\mu_3(E_r)e^{-c''(q-r)}$.

For $N=\sum_q {\bf1}_{E_q}$, summing the pair bound yields $\mathbb E N^2\ll\mathbb E N$, while the central window gives $\mathbb E N\asymp\theta^2$. Cauchy–Schwarz now implies $\mu_3(N>0)\gg\theta^2$. Every marked word witnesses the required strict ordinary inequality, proving the theorem.

The same bound holds as an ordinary lower frequency in each fixed odd dyadic class modulo $2^j$ in $[X,2X]$, uniformly for $C_jX^{-\gamma}\le\theta\le1$, with $\gamma=\log(3/2^{4/3})/\log3$. Indeed the entire finite union has period $3^{\lfloor q_*\rfloor}$ or a divisor, and this times $2^j$ is at most $X/2$ once $C_j$ is sufficiently large. CRT transfers at least a constant fraction of the uniform measure. Consequently the shell mean of $(t/m(t))^2$ is $\gg_j\log X$, and that of $(t/m(t))^s$ is $\gg_{j,s} X^{\gamma(s-2)}$ for $s>2$. Only the finite lower screen is asserted uniformly at this scale.
