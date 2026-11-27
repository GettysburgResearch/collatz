# The two complete denominators have the same logarithmic fraction

**PROPOSED written theorem.** Use arbitrary positive Nielsen dictionaries from the [main note](README.md), and expand a fixed seed $w$ containing $a>0$ zeros and $b>0$ ones. Write $L,p$ for the output length and number of ones. Let $d$ be the reduced denominator of the physical periodic phase of this word and $d_*$ the reduced denominator of its companion periodic phase for $w'\!=3w/2$ at zero and $w'\!=(3w+1)/4$ at one. This companion equals $-D(x)/3$ for the corresponding periodic dyadic source $x$; its denominator is prime to six. Along **any sequence of such expansions** with $L\to\infty$ and $p/L\to\rho$ irrational, put $M=\max(2^L,3^p)$, $M_*=\max(2^{L+p},3^L)$. Then
$$
 \log d=c(w)\log M+o(L),\qquad \log d_*=c(w)\log M_*+o(L).       \tag{1}
$$
The same computable rational $c(w)\in[1/\gcd(a,b),1]$ occurs in both coordinates. The [primitive-clock bound](EXCEPTIONAL_TRANSLATES.md) also proves the lower fraction $1/g$ at arbitrary densities, including every exceptional translated subtorus. It equals one when $\gcd(a,b)=1$. The conclusion is individual along the indicated sequences and requires neither a random word nor a primitive output.

## Affine elimination of the two long blocks

Work over $R=\mathbb Z[1/6]$. Write $A(z)=Uz+c,\ B(z)=Vz+d_0$ for the two current coordinate maps. Initially the slopes and translations are $(1/2,0),(3/2,1/2)$ in the physical coordinate, and $(3/2,0),(3/4,1/4)$ in the companion coordinate. In both cases all slopes are units in $R$. The difference
$$
 K=(U-1)d_0-(V-1)c
$$
starts at $-1/4$ or $1/8$, respectively. A swap negates $K$. Replacing $B$ by $B\circ A$ leaves $K$ unchanged. Replacing $B$ by $A\circ B$ multiplies $K$ by $U$. These rules and swapping cover every allowed move, so $K$ is always a unit at **every prime outside two and three**.

Define $S_1(X,Y)$ by summing, over the ones in the seed, the product of the formal slopes in the suffix strictly after that one. Define $S_0$ analogously and $F=X^aY^b-1$. Telescoping gives $(X-1)S_0+(Y-1)S_1=F$. The translation of the expanded word is $C=cS_0(U,V)+d_0S_1(U,V)$, whence
$$
 (U-1)C=cF(U,V)+K S_1(U,V).                                     \tag{2}
$$
The closed phase is $-C/F(U,V)$. In either coordinate $F(U,V)$ has denominator a power of two and numerator, in absolute value, equal to the appropriate raw divisor $|2^L-3^p|$ or $|2^{L+p}-3^L|$, when $p>0$. Since the closed word has a positive number of ones eventually and its carry denominators divide the word's translation denominator $2^L$ or $2^{L+p}$, the phase denominator divides this raw divisor. Both raw divisors are prime to six.

At a prime $\ell\nmid6$, take $f=v_\ell(F(U,V))$. All evaluations in (2) are integral there. The truncated valuation $\min(f,v_\ell(S_1(U,V)))$ equals $\min(f,v_\ell(U-1)+v_\ell(C))$, because $K$ is a unit. Thus it exceeds $\min(f,v_\ell(C))$ by at most $\min(f,v_\ell(U-1))$. These inequalities address full prime powers, including common factors of the two numerical polynomials.

## A fixed symbolic computation and the Subspace Theorem

Set $g=\gcd(a,b)$, $Z=X^{a/g}Y^{b/g}$ and take $G=\gcd(F,S_1)$ over $\mathbb Q[X,Y]$, normalized as a product of monic cyclotomic factors in $Z$. Indeed $F=Z^g-1=\prod_{j\mid g}\Phi_j(Z)$; the polynomials $\Phi_j(Z)$ are irreducible in $\mathbb Q[X,Y]$. In the Laurent ring a unimodular monomial change sends the primitive exponent vector of $Z$ to a coordinate, where this is the usual irreducibility. No coordinate factor is lost because the constant terms are nonzero. Consequently $G=\prod_{j\in J}\Phi_j(Z)$ for a subset $J$ of the divisors of $g$, with $1\notin J$ since $S_1(1,1)=b>0$. Divide to obtain coprime integral $F'=F/G,\ S'=S_1/G$ by Gauss's lemma, with $F'(0,0)=\pm1$. Define
$$
 c(w)=1-\frac{\sum_{j\in J}\varphi(j)}{g}.                       \tag{3}
$$
For example, $00101101$ is primitive and has $g=4$, $G=XY+1$, and $c=3/4$. In this example $S_1=X^2Y^3+XY^2+XY+1=(XY+1)(XY^2+1)$, and $F=(XY)^4-1$.

For fixed coprime integral polynomials $P,Q$ not both vanishing at the origin, Corvaja–Zannier's gcd inequality at rational $S$-unit points bounds
$$
 \sum_{\ell\notin S}\min\{v_\ell(P(U,V)),v_\ell(Q(U,V))\}\log\ell
 \ \le\epsilon\max\{h(U),h(V)\}
$$
off finitely many proper translated subtori and finitely many points, for every $\epsilon>0$, with $S=\{2,3,\infty\}$. This is the outside-$S$ part of the nonnegative negative-log sum in their proof of Theorem 1, equation (2.30). A fixed nonzero constant polynomial instead bounds the relevant sum by a constant. [Corvaja and Zannier, Theorem 1, proof around (2.30)](https://arxiv.org/pdf/math/0311030)

Here the hypotheses excluding translated subtori must be established for the *whole sequence*. Write $v_A=(L_A,p_A),v_B=(L_B,p_B)$ for the block clocks. They form a unimodular basis since this holds for the two one-letter blocks and every move preserves the absolute determinant. For each coordinate, the exponent vectors of its slopes at $2,3$ are the images of these clocks under a fixed unimodular linear map: $(l,k)\mapsto(-l,k)$ or $(l,k)\mapsto(-(l+k),l)$. Thus on a translated subtorus $U^rV^s=\lambda$ with fixed $(r,s)\ne(0,0)$, the vector $t=r v_A+s v_B$ is fixed (or there are no points). It is nonzero. But the total clock $v=a v_A+b v_B=(L,p)$ satisfies
$$
 |\det(t,v)|=|rb-sa|.
$$
If infinitely many points lay on that translate, dividing by $L$ gives $t_1\rho=t_2$, impossible for a nonzero integer vector and irrational $\rho$. A single fixed point can be covered by such a translate. Also $h(U),h(V)=O(L)$ since both seed letters occur. The gcd losses for the two polynomial pairs $(F',S')$ and $(F,X-1)$ are consequently $o(L)$. The second pair is coprime because $b>0$. At each good prime the gcd valuations for $(F,S_1)$ are those of $G$ plus those for $(F',S')$. Equation (2) now proves that the logarithm removed from the complete raw divisor is
$$
 \sum_{\ell\nmid6} v_\ell(G(U,V))\log\ell+o(L).                 \tag{4}
$$

To evaluate (4), put $Z(U,V)=R_0/Q_0$ in lowest terms. The numerator is $3^{p/g}$ and denominator $2^{L/g}$ for the physical map. They are $3^{L/g}$ and $2^{(L+p)/g}$ for the companion. For all sufficiently late indices both exponents are positive. For $j>1$ every homogeneous value $Q_0^{\varphi(j)}\Phi_j(R_0/Q_0)$ is prime to six, by its leading and constant coefficients. Its log is $\varphi(j)\log\max(R_0,Q_0)+O_j(1)$ because $\Phi_j$ has no nonnegative real root, including at the ratio one. For the complete raw divisor, $\log|2^u-3^v|=\log\max(2^u,3^v)+O(\log(2L))$ at both clocks: the two-log lower bound gives $|u\log2-v\log3|\gg L^{-13.3}$. Together these identities prove (1). [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

## Applying the relation to the existential question

Along a sequence of distinct primitive positive integer cycles their minima tend to infinity by determinism. The cycle product therefore gives $p/L\to\log 2/\log 3$, an irrational density. Equation (1) excludes any fixed seed for infinitely many such physical cycles, since their physical denominator would have to be one. On the same words the companion is then automatically covered by the second estimate. The uniform ordinary length obstruction in the [main note](README.md) gives the stronger changing-seed estimate for ordinary cycles.

For the seed $10$, $S_1=X$ is a unit upon evaluation. Equation (2) at every prime of the clock proves exactly $d=|2^L-3^p|,\ d_*=|2^{L+p}-3^L|$ for every dictionary, without a limiting hypothesis. This special case of the physical full-divisor identity meets the balanced-cycle result. It also shows precisely what can fail if one tries to iterate the single substitution $\sigma(0)=1,\sigma(1)=01$ from PR182. The parity word $10$ is the actual cycle of 1. Its first two images are $011$ and $10101$, with initial physical phases $-10$ and $37/5$. More generally $\sigma^k(10)$ has Fibonacci clocks, $p/L\to(\sqrt5-1)/2$, and both reduced denominators attain their raw sizes. Their logs grow proportionally to $L$. Thus even the known orbit of 1 does not give integrality or bounded denominators throughout this substitution procedure. These new words describe different periodic trajectories. [Knight, balanced high-cycle gcd](https://doi.org/10.1016/j.disc.2025.114812)

The [pinned PR195 round-five theorem](https://github.com/GettysburgResearch/collatz/blob/1c6e750e2f6970e6d5456cba5a93c2f3de8c2a97/research/astra-global-closure-20261124/round5/arithmetic/UNIT_RELATIONS.md) controls particular factors in discrepancy masks via fixed-field unit relations. Here the fixed objects are the two seed polynomials, and the evaluated affine commutator remains a unit through arbitrary Nielsen directives. This eliminates both block carries before applying the gcd inequality, and yields the exact leading loss including common symbolic factors. For unrestricted physical words there is no uniform fixed seed; the ordinary finite paths in the main note witness complete failure of shortening. The gcd theorem has polynomials and exceptional translates depending on the seed. Its use here does not extend (1) to linear-length changing seeds or imply that $D(n)$ is triadic at a prescribed positive integer.

**Formal scope.** [SeedDenominator.lean](SeedDenominator.lean) imports Std and proves the swap and concatenation rules, (2) for arbitrary seed lists over rational affine maps, the clock determinant identity, and both initial commutators. Lean 4.34.1 printed only propext, Classical.choice and Quot.sound for the six declarations, including the finite length-versus-height pigeonhole bound from the main note. The factorization, translated-subtorus exclusion at an irrational slope, Diophantine inequalities, and ordinary mechanical-segment bounds are written arguments.
