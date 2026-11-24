# When a primitive cycle word has a vanishing top determinant

**Status. Proposed written theorem and independent finite controls, 24 November 2026.** This classifies one algebraic obstruction in the cycle program. The Collatz conjecture remains open. The assertions below concern candidate words and their literal rational cycles. No new Lean kernel result is claimed.

## 1. Statement and source boundary

Use the shortcut map taking an even number to half its value and an odd number to half of three times its value plus one. Its rational extension uses the parity of the numerator over an odd denominator. For a binary word of length $A$ with $p>0$ ones, let $0\le d_0<\cdots<d_{p-1}<A$ be their positions, and set
$$
g=\gcd(A,p),\quad A=ga,\quad p=gb,\quad
Q(Z)=\sum_{i=0}^{p-1}2^{d_i} Z^{p-1-i},\quad
C=Q(3),\quad D=2^A-3^p.
$$
We consider contracting words $D>0$. For each $g$ use the monic integer polynomial
$$
H_g(Z)=(2^a)^{\varphi(g)}\Phi_g(Z^b/2^a).
$$
Here $H_g$ denotes the polynomial in the zero criterion, distinct from the multiplication element called $H$ in TCP-4. The **top determinant** is TCP-4's $J_g$, the component indexed by the full clock gcd. Its zero criterion is
$$
 J_g=0\quad\Longleftrightarrow\quad
 \gcd_{\mathbb Q[Z]}(Q,H_g)\ne1.
$$
This is equation (9) of the fixed source. In its complex product decomposition, writing $z^b=2^a\zeta^{-1}$ with primitive $g$-th root $\zeta$ identifies the evaluated sum with $z^{1-p}Q(z)$. The remaining factor $\tau-1$ cannot vanish since $|\tau|=2^{1/b}>1$. Each $z$ occurs, using coprimality of $a,b$. This also shows the vanishing property is independent of the choice of cyclic rotation. [PR191, 37b3916633cd32a0c173b20bb18ec3a7ec290a63, TCP-4](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md)

**Theorem.** Fix the clock gcd $g$, allowing all coprime clock ratios $a/b$ with $D>0$. Every primitive binary word at that clock gcd has $J_g\ne0$ precisely when $g=1$ or $g$ is a prime power different from 4. A word is primitive if it is no proper power under cyclic repetition.

1. For $g=\ell^t$, with $\ell$ prime, we have
   $$
      J_g=0\iff \text{the word is an }\ell\text{-fold repetition}
   $$
   whenever $g\ne4$ or $b$ is odd. For $g=1$ the determinant is always nonzero.
2. For $g=4$ a primitive word with $b=4$ and $J_4=0$ occurs at $A=28,p=16$. This existential witness settles the quantifier over all clock ratios for $g=4$.
3. For every $g$ with at least two different prime divisors, there is a primitive word with $A=5g,p=3g$ for which the entire top polynomial divides $Q$. In particular its entire numerical top cyclotomic factor divides $C$. These examples are literal positive nonintegral rational cycles.

The witnesses in parts 2 and 3 all satisfy $3^p<2^A<4^p$, the basic density window of a hypothetical nonstandard positive integer cycle. Their failure of integrality is checked independently.

## 2. Regrouping the polynomial

Choose any root $z$ of $H_g$, and put $w=2^a/z^b$, a primitive $g$-th root of unity. For $0\le i<b$ define
$$
 P_i(W)=\sum_{j=0}^{g-1}2^{d_{i+jb}-aj}W^j\quad\in\mathbb Q[W].
$$
Grouping the terms by the odd-position index modulo $b$ gives the identity
$$
 z^{1-p}Q(z)=\sum_{i=0}^{b-1}z^{-i}P_i(w).
$$
If $H_g$ is irreducible over the rationals, its degree is $b\varphi(g)$. Since $w\in\mathbb Q(z)$ has degree $\varphi(g)$, the extension degree $[\mathbb Q(z):\mathbb Q(w)]$ equals $b$, and $1,z^{-1},\ldots,z^{-(b-1)}$ are linearly independent over $\mathbb Q(w)$. Consequently $Q(z)=0$ precisely if every $P_i(w)=0$. Irrespective of irreducibility, divisibility of every $P_i$ by $\Phi_g$ gives $H_g\mid Q$, since every root has the indicated form and all roots of $H_g$ are simple.

For an odd $g$, $H_g$ is always irreducible. Indeed $K=\mathbb Q(w)$ is unramified at 2. To see this, $\Phi_g$ divides $X^g-1$, squarefree modulo 2 since $g$ is odd. Thus the discriminant of the monic $\Phi_g$ is odd. The field discriminant divides this order discriminant and 2 is unramified. At any prime of $K$ over 2 use the integral valuation normalized by $v(2)=1$. The roots of $X^b-2^a/w$ all have valuation $a/b$ in an algebraic closure with the extended valuation. The constant coefficient of a monic degree-$e$ factor over $K$ has valuation $ea/b$, an integer. Coprimality forces $b\mid e$. Thus the binomial is irreducible over $K$, so $[\mathbb Q(z):\mathbb Q]=b\varphi(g)$, as required. This includes $g=1$, for which the lone coefficient in each positive $P_i(1)$ prevents cancellation.

For $g=2^t$, $t\ge1$, write $c=2^{t-1}$. Then $H_g(Z)=Z^{bc}+2^{ac}$. Apply the rational binomial irreducibility criterion to $Z^n-\gamma$, with $n=bc$ and $\gamma=-2^{ac}$. The degree-one case is immediate. For $n\ge2$, the criterion gives reducibility precisely if $\gamma$ is a rational prime-th power for some prime divisor of $n$, or $4\mid n$ and $\gamma=-4h^4$ with rational $h$. Negative $\gamma$ excludes the square case. An odd prime dividing $n$ divides $b$ and cannot divide $ac$, so the 2-adic valuation excludes that power. The last case requires $4\mid bc$ and $ac\equiv2\pmod4$. At $t=1$ these would force both $a,b$ even. At $t\ge3$ the latter congruence fails. At $t=2$ the two conditions hold exactly when $b$ is even, since then $a$ is odd. This proves precisely the stated irreducibility range. [Koley and Reddy, Theorem 1, arXiv:2006.03787v1, p. 1](https://arxiv.org/pdf/2006.03787v1)

For $g=\ell^t$, let $h=g/\ell$. The polynomial $\Phi_g(W)=1+W^h+\cdots+W^{(\ell-1)h}$ divides a polynomial of degree below $g$ exactly when its length-$g$ coefficient vector is invariant under shift by $h$ modulo $g$. For the forward implication the quotient has degree below $h$, so multiplying repeats its length-$h$ coefficient vector. The reverse implication follows by multiplication. For $P_i$ this gives
$$
 d_{i+(j+h)b}-d_{i+jb}=ah
$$
for nonwrapping indices, and the same equality on extending $d_{k+p}=d_k+A$. Hence the set of marked positions is invariant under translation by $ah=A/\ell$ and the word is an $\ell$-th power. Conversely that period contains exactly $p/\ell$ marks in each repeat, so the displayed identities and cancellation follow. Since a repetition multiplicity divides both $A,p$, any proper power at this clock gcd is an $\ell$-th power.

## 3. Physical examples and the full denominator

Every word with $D>0,p>0$ considered here has a positive literal rational cycle at $x=C/D$. Indeed $D$ is odd and coprime to 3, and $C\bmod2$ gives exactly the first bit $e$. For cyclic rotation past that bit, its new carry satisfies $2C_{\rm rot}=3^e C+eD$ by the sum for $C$. The shortcut step thus gives $C_{\rm rot}/D$, proving exact parity and closure on every rotation. Reduction retains the same odd denominator since it is coprime to 6. If the word is primitive, no smaller orbit period could generate it.

At $g=4$ take the marks
$$
(0,1,2,4,6,8,10,11,13,15,17,18,20,22,23,25).
$$
Here $H_4=Z^8+16384=(Z^4-16Z^2+128)(Z^4+16Z^2+128)$. Exact polynomial Euclidean division gives
$$
 \gcd(Q,H_4)=Z^4-16Z^2+128.
$$
The tests of powers require only repetition counts 2 and 4 since their counts must divide $g$. The set is not invariant under shift 14, as position 0 is marked while position 14 is unmarked. This excludes both repetitions. Numerically $C=318509945, D=225388735, \gcd(C,D)=65$, so the actual rational source is $4900153/3467519$. The top factor at 3 is $22945=65\cdot353$, and the shared quartic evaluates to 65. Its determinant vanishes while its numerical top factor cancels only in part.

For mixed $g$, choose different prime divisors $r,s$. For $0\le j<g$, mark the three clocks
$$
5j+\mathbf1_{j\equiv1\pmod{g/r}},\qquad
5j+2+\mathbf1_{j\equiv1\pmod{g/s}},\qquad 5j+4 .
$$
These positions are strictly increasing. The three coefficient rows $P_i$ are respectively the constant sequence 1 plus its indicator, constant 4 plus four times its indicator, and constant 16. All three evaluate to zero at primitive $g$-th roots. Each constant sequence sums a full geometric progression. Each marked coset sums a complete geometric progression of order $r$ or $s$. Hence $H_g\mid Q$. Because both polynomials have integer coefficients and $H_g$ is monic, this is integral polynomial divisibility. Reciprocal symmetry of $\Phi_g$, valid for $g>1$, gives $D_g=H_g(3)\mid C$.

If the word were a $k$-th power for $k>1$, then $k\mid g$. Translation by $5g/k$ shifts the block index by $g/k$ and must preserve both indicators. Their simultaneous period must be divisible by $\operatorname{lcm}(g/r,g/s)=g$, a contradiction. Every block contracts with multiplier $27/32$. Its fixed center is between $37/5$ and $58/5$, since its carry is $37+9\mathbf1_r+12\mathbf1_s$. The cyclic min/max principle puts each boundary in this same interval. Block 0 starts at an odd source and has its first two gaps equal to two. The only odd integers in the interval are 9 and 11. Source 9 has first two gaps 2 and 1, and 11 has first gap 1. Thus these cycles all have reduced denominator greater than one, even with complete top numerical cancellation.

## 4. What is open and what was checked

Top-component nonvanishing by itself gives no bound below $D_g$ on the determinant or exclusion of $D_g\mid J_g$. Complete cancellation in a top component similarly leaves other components available. Neither conclusion excludes arbitrary integer cycles or injective nonperiodic ordinary orbits.

Run `python -B check_top_component.py` to reproduce the supplied JSON. The standard-library controls directly compute the polynomial gcd over the rationals using primitive pseudoremainders and verify literal rational parity and closure for every test. They cover all 11,957 contracting words of lengths 2 through 14 starting at an odd position, including 11,495 positive-class equivalences, the explicit quartic exception, and twelve mixed-clock families with $6\le g\le60$. The bounded checks supplement the proofs. No full checkout validation or Lean compilation was executed for this note.
