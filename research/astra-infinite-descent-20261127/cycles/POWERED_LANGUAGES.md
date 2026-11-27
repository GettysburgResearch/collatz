# Full rational denominators in words with arbitrarily many switches

**PROPOSED written results.** For a nonempty chronological shortcut word $U$, put $a_U=|U|$, $u_U=\#1(U)$, $\lambda_U=3^{u_U}/2^{a_U}$ and write $T_U(x)=\lambda_Ux+C_U/2^{a_U}$. Its center $s_U=C_U/(2^{a_U}-3^{u_U})$ is always defined, including the all-zero word with $s_U=0$. Both the magnitude of its raw numerator and that of its raw denominator are at most $3^{a_U}$, by comparison with the all-one carry. Thus its absolute logarithmic Weil height is $O(a_U)$. Iteration gives $T_{U^n}(x)-s_U=\lambda_U^n(x-s_U)$. All denominator results below concern actual positive rational closed words.

## Two moving motifs

Consider a sequence of **primitive** positive words $W=U^n V^m$ of length $h\to\infty$, where $U,V$ can change with the word, $n,m\ge1$, and $|U|+|V|=o(h)$. Let $(H_i,P_i)$ be the length and one-count of the two powered blocks, so $(H_1,P_1)=n(a_U,u_U)$ and $(H_2,P_2)=m(a_V,u_V)$. Put $p=P_1+P_2$ and $D=2^h-3^p>0$. If $q$ is the reduced denominator, then
$$
 \log_2 q=\log_2\!\left(\frac{D}{\gcd(D,\,2^{H_1}-3^{P_1})}\right)
              +O(|U|+|V|+1).                                       \tag{1}
$$
The estimate with its absolute error holds at finite length whenever the two centers are distinct. The positive fixed point of a primitive sufficiently long $W$ cannot have equal centers: in that case it equals the common center, and following $U$ alone returns it to itself in $|U|<h$ steps. The deterministic parity of the rational orbit follows because each inverse affine branch has the prescribed parity at an odd-denominator input.

If the two motifs have different one densities then $\log_2 q/h\to1$. If their densities agree, write $(H_i,P_i)=s_i(a,b)$ for primitive $(a,b)$ and positive integers $s_i$. Then
$$
 \frac{\log_2 q}{h}
       =1-\frac{\gcd(s_1,s_2)}{s_1+s_2}+o(1)\ \ge\frac12-o(1).     \tag{2}
$$
The motifs' internal bit complexity is unrestricted, as are the relative sizes of their exponents.

For (1), put $s=s_U,t=s_V$. Applying the two centered affine maps in order to their common closed-word starting value $x$ gives
$$
       D(x-t)=(s-t)\,3^{P_2}(2^{H_1}-3^{P_1}).
$$
The rational value $y=3^{P_2}(2^{H_1}-3^{P_1})/D$ has exactly the denominator inside (1), since $D$ is coprime to 3. Passing between $x=t+(s-t)y$ and $y=(x-t)/(s-t)$ changes the log of the reduced denominator by at most a constant times $\mathrm h(t)+\mathrm h(s-t)+1=O(|U|+|V|+1)$. This uses $\operatorname{den}(a+b)\le\operatorname{den}(a)\operatorname{den}(b)$, its product counterpart, and $\max(\operatorname{den}(v),\operatorname{den}(1/v))\le\exp(\mathrm h(v))$ for nonzero rational $v$.

In the different-density case $2^h3^{-p}$ and $2^{H_1}3^{-P_1}$ are multiplicatively independent, as seen at 2 and 3. Corvaja and Zannier give the logarithmic gcd $o(h)$ at the outside primes, uniform over all such data. This includes $P_1=0$. In the equal-density case, the ordinary difference-of-powers gcd is exactly $2^{a e}-3^{b e}$ with $e=\gcd(s_1,s_2)$. All prime powers are retained since $2^a,3^b$ are coprime. Its logarithm is $ae\log2+o(h)$, by the same two-logarithm separation used for $D$ whenever $ae\to\infty$, or by boundedness when $ae$ stays bounded. [Two-unit gcd theorem, Proposition 2](https://arxiv.org/pdf/math/0311030) · [Finite same-slope gcd argument](DISPERSED_EDITS.md)

## Fixed collections of powered motifs with connectors

Fix nonempty words $U_1,\ldots,U_k$ and any fixed connectors (possibly empty). Any sequence of words in the resulting bounded expression, with growing **least** period and displayed length $h$, satisfies
$$
              \liminf \log_2 q/h\ \ge\ 1/k.                         \tag{3}
$$
Coprime displayed length and grade give limit one. The conclusion also holds if $\gcd(h,p)$ has no bounded prime divisor eventually. Unlike a bound on the number of runs of ones, (3) allows order-$h$ switches between odd and even bits. In fact it holds for any subset of a fixed bounded language in the formal-language sense. A mere bound on word counts without bounded-expression membership is insufficient for this deduction.

Pass to a subsequence on which each power exponent is fixed or tends to infinity. Absorb the fixed powers and end fragments into cyclic connectors and rotate to an entrance of a growing power. At least one growing power remains. Write the resulting cyclic presentation $U_1^{n_1}V_1\cdots U_r^{n_r}V_r$, with $r\le k$ and every $n_i\to\infty$. Now $s_i=s_{U_i}$ are fixed rational centers. Put $\kappa_i=T_{V_i}(s_i)-s_{i+1}$, indices taken cyclically. If $z_i$ is the actual entry value minus $s_i$, then
$$
             z_{i+1}= 3^{P_i}2^{-H_i}z_i+\kappa_i ,
$$
where $(H_i,P_i)$ includes the connector after the power. Let $d_1=b_1=0$ and $d_j,b_j$ be cumulative length and grade before block $j$. Iterating the affine relations at the entry $x$ of the first block gives
$$
       D(x-s_1-\kappa_r)
          =\kappa_r 3^p+
             \sum_{j=2}^r\kappa_{j-1}2^{d_j}3^{p-b_j}.              \tag{4}
$$
In particular the wrap term has been moved from date $h$ to date zero by subtracting $\kappa_r D$. If every $\kappa_i=0$, the contracting full lap has $z_1=0$. The same physical root then returns under $U_1$, bounding its least period by the fixed $|U_1|$. This is the only case not controlled by (3).

Otherwise clear a fixed common denominator of the nonzero $\kappa$'s. Extract each resulting integer coefficient's fixed power of two into its date. All dates lie in $[0,h)$ and are distinct eventually: consecutive power-block boundaries, including the final wrap, are separated by lengths tending to infinity. Removing zero terms preserves this property. Thus the sparse integer sum has at most $r$ terms with fixed odd coefficients. Its ratio to $D$ differs from $x$ by a fixed rational affine change with nonzero linear coefficient, costing $O(1)$ in the log denominator. Equations (3) and (8) of the sparse theorem prove (3) here and its coprime-clock conclusions. [Sparse numerator theorem](SPARSE_DENOMINATORS.md) · [Lean centered affine identities](PoweredBlocks.lean)

## Regular and context-free test families

Every infinite context-free language consisting entirely of primitive positive rational cycle words contains a subfamily of increasing lengths with lower denominator exponent **at least $1/2$**. The context-free pumping lemma gives fixed strings $u,v,x,y,z$ with $|v|+|y|>0$ and $uv^nxy^nz$ in the language for all $n\ge1$. Apply (3) to the one or two nonempty powered motifs and these fixed connectors. For an infinite regular language of such words, regular pumping uses one motif and gives exponent **one**.

The one-half conclusion is sharp. Put $U=1100$ and $V=1010$. Both have length four and grade two, and their centers are respectively $5/7$ and $1$. Every word $U^nV^n$, $n\ge1$, is primitive. Its cyclic sequence of odd-run lengths consists of $n$ entries equal to two followed by $2n$ entries equal to one. There are exactly two type changes; a nonconstant cyclic word repeated at least twice would have at least four. With $A=16^n,B=9^n$ the starting value is $(7A+5B)/(7(A+B))$. The numerator is a unit modulo seven, and its gcd with $A+B$ divides $2B$ while $A+B$ is odd and coprime to $B$. Hence the exact reduced denominator is $7(16^n+9^n)$, of exponent one-half. The language of these words is context-free via the grammar $S\to USV\mid UV$.

Thus no infinite context-free language of primitive positive rational cycle words can have a uniformly subexponential denominator. The source-dependent period question for arbitrary primitive ordinary words remains open. The separate [clock-language equivalence](CLOCK_LANGUAGES.md) gives a simpler argument for the all-integer finiteness statement without the analytic inputs used for the numerical denominator exponent. PR192 treats a different family consisting of boundedly many copies of one moving valuation word separated by moving markers. The fixed motifs here may be different, and the two-motif theorem above lets both of them change. [PR192 shared-background result](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-sixhour-20261127/arithmetic/SHARED_BACKGROUND.md)
