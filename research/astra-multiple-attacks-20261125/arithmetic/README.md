# Prime factors of finite carries on ordinary trajectories

**PROPOSED written theorems.** Every sufficiently long ordinary shortcut word forces exponentially large prime-to-$S$ mass in its carry, up to an explicit price for its initial height. A two-window theorem gives a separate obstruction on every actual escaping orbit, even for arbitrary unequal-weight windows. Its application to balanced pairs excludes all escaping positive realizations of the physical encodings described in [the applications](APPLICATIONS.md). Positive cycles and general escape remain open.

Let $T(x)=x/2$ for even $x$ and $(3x+1)/2$ otherwise. For a positive ordinary start $a$, write $x_j(a)=T^j(a)$, $e_j(a)=x_j(a)\bmod2$, $P_j(a)=\sum_{i<j}e_i(a)$. Define
$$
 B_j(a)=\frac{2^j e_j(a)}{3^{P_{j+1}(a)}},\qquad
 U_N(a)=\sum_{j<N}B_j(a)=\frac{C_N(a)}{3^{P_N(a)}}.
$$
The nonnegative integer carry satisfies $2^N x_N(a)=3^{P_N(a)}a+C_N(a)$, and $0\le C_N(a)\le 3^N-2^N$. The latter follows by induction, with next carry unchanged at an even departure and $3C_N+2^N$ at an odd one. For a rational $Y$ with denominator supported in a fixed finite prime set $S\supseteq\{2,3\}$, put $H_S(Y)=\prod_{\ell\notin S}\ell^{v_\ell(Y)}$ if $Y\ne0$, and $H_S(0)=1$. This counts multiplicities in the numerator. It is unchanged by an $S$-unit factor.

## Uniform one-window theorem, including moving tower starts

For each $\epsilon>0$ there is $N_0(S,\epsilon)$ such that **every** positive integer $a$ and $N\ge N_0$ satisfy
$$
                 a\,H_S(C_N(a))\ \ge\ 2^{(1-\epsilon)N}.             \tag{1}
$$
Given $A>0$, uniformly on $1\le a\le\exp(AN)$ one has the stronger bound
$$
      2^{v_2(a)} H_S(a)\,H_S(C_N(a))\ \ge\ 2^{(1-\epsilon)N}        \tag{2}
$$
for all sufficiently large $N$, depending only on $S,A,\epsilon$. In particular the same exponential lower bound holds for the prime-to-$S$ carry itself on every tower $a=3^r$ uniformly over $0\le r\le AN$, renaming $A$. This includes the entire sequence of clocks of any fixed ordinary source, whether periodic, eventually periodic or escaping. Neither onset is effective in this proof.

Use the rational-number-field subspace theorem of Schmidt and Schlickewei for the fixed places $V=S\cup\{\infty\}$. In the version for primitive integral $d$-vectors, the product of $d$ independent linear forms per place, in the usual normalized absolute values over $V$, bounded above by $\|\mathbf z\|_\infty^{-\delta}$ puts the vectors in finitely many proper rational subspaces. We use only rational forms. If a rational vector has denominators supported in $S$, clearing these denominators by an $S$-unit leaves the product unchanged. Dividing out the integral common gcd leaves it unchanged at its $S$-part and decreases it for its prime-to-$S$ part. [Schlickewei, original linear-forms theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Kebis et al., Theorem 2.1 in their integral formulation](https://people.mpi-sws.org/~joel/publications/transcendence_pisot_morphic_words26.pdf)

Apply it to the two coordinates $(a,U_N(a))$, taking coordinate forms everywhere except that at 2 the first is replaced by $a+U_N(a)$. This has dyadic size at most $2^{-N}$ by the exact ordinary endpoint. At every place the resulting two forms are independent. For $U_N\ne0$, the entire product is at most
$$
 2^{-N}\left(\prod_{v\in V\setminus\{2\}}|a|_v\right)
       \prod_{v\in V}|U_N|_v
   =2^{-N}2^{v_2(a)}H_S(a)H_S(C_N).
$$
For $U_N=0$ every bit is even, so $2^N\mid a$ and (2) holds directly. Under $a\le\exp(AN)$ the primitive height is at most $\exp(O_A(N))$, by clearing $3^{P_N}$ and the carry bound. Failure of (2) infinitely often thus gives one repeated rational line. Since $a>0$, it has $U_N=t a$ for one fixed rational $t\ge0$. Then $v_2((1+t)a)\ge N$, and $2^{v_2(a)}\ge2^{N-v_2(1+t)}$, contradicting failure for large $N$. This proves (2). A failure of (1) would already give $a<2^N$, to which (2) applies, while $2^{v_2(a)}H_S(a)\le a$.

The exponent one is sharp. On the cycle from 1, at positive even $N$ the endpoint is 1 and $C_N=2^N-3^{N/2}<2^N$. Thus no uniform $1+\epsilon$ exponent is possible.

## All-word two-window theorem on a single escape

Fix one positive source $x$ with injective ordinary orbit $x_j=x_j(x)$. Every non-eventually-periodic positive trajectory is injective and tends to infinity. Fix $K\ge1$. For **any** $q,N\to\infty$, partition $\{0,\ldots,N-1\}$ into at most $K$ arbitrary sets $I$, allowed to change every time. Put
$$
   Y_I=\sum_{j\in I}\bigl(B_j(x_q)-B_j(x)\bigr).
$$
Then
$$
 \liminf\frac{\log_2(x_q+1)+\sum_I\log_2H_S(Y_I)}{N}\ \ge\ 1.      \tag{3}
$$
No periodic approximation, equal grade, or regularity of the observed words is needed. With a single set the discrepancy is $R=U_N(x_q)-U_N(x)$. Choosing $q=\lfloor\sqrt N\rfloor$ gives $H_S(R)\ge2^{N-o(N)}$ for all large $N$, since $x_q+1\le(x+1)(3/2)^q$. Choosing $q=N$ gives $H_S(R)\ge(4/3)^{N-o(N)}$.

**Real sizes at the same source.** The reciprocal sum $\sum_{j\ge0}1/x_j$ is finite. One elementary quantitative proof on arbitrary finite simple segments is in [PR195, pinned round twelve, §1, (2)](https://github.com/GettysburgResearch/collatz/blob/99a4ab3f808c01acd115ef08eee42a8b886d5d4c/research/astra-global-closure-20261124/round12/arithmetic/README.md). It counts starts below $X$ by splitting short parity words into heavy ones (few cylinders) and light ones (distinct endpoints below a reduced cap), obtaining $O(X^{79/80})$ uniformly and summing by shells. The exact one-step identity gives
$$
 0\le U_N(a)=a\left(\prod_{j<N}(1+e_j(a)/(3x_j(a)))-1\right).
$$
Thus $U_N(x)=O_x(1)$ uniformly in $N$, and $U_N(x_q)\le x_q(\exp(\tfrac13\sum_{j\ge q}1/x_j)-1)=o(x_q)$, also uniformly in $N$. All terms $B_j$ are nonnegative. In particular every $|Y_I|=o(x_q)$ in the ordinary absolute value, independently of the choices of time sets. This is where following one physical escaping orbit matters.

**Finite-place size and rank reduction.** Write $D=x_q-x>0$ eventually. The two endpoint identities give
$$
 D+\sum_I Y_I=2^N\left(\frac{x_{q+N}}{3^{P_N(x_q)}}-
                        \frac{x_N}{3^{P_N(x)}}\right).               \tag{4}
$$
Hence the displayed linear form has dyadic size at most $2^{-N}$. Suppose (3) fails by a fixed positive margin along a subsequence. Pass to a further subsequence fixing the number of nonzero discrepancy coordinates, omitting zeros. Keep $D$ as first coordinate. Use the coordinate forms over $V$, replacing the first at 2 by (4). The product over all forms and places is at most $2^{-N}|D|\prod_I H_S(Y_I)$, exponentially small by hypothesis. All coordinates have denominator dividing $3^N$. The integer coordinate $D$ is at most $2^N$ under failure, and clearing denominators in each partial sum gives height at most $\exp(O(N))$, since there are at most $N$ terms bounded by $2^N3^N$ after clearing on each side. The primitive height therefore admits the same bound. The subspace theorem gives a fixed nonzero rational linear relation on an infinite subsequence.

Its coefficient at $D$ must be zero, since $D\sim x_q$ and every other coordinate is $o(x_q)$ in the reals. Eliminate one $Y_I$ by this relation and restrict to the subsequence. On the remaining coordinates the original dyadic form still has coefficient one at $D$, with fixed rational coefficients at the other coordinates. Its size is still at most $2^{-N}$. The product estimate remains valid because we have dropped a factor $H_S(Y_I)\ge1$. Local independence still follows from the leading coefficient one. Height and ordinary bounds persist. Iteration either gives a relation with nonzero coefficient at $D$, already impossible, or leaves only $D$, when (4) forces $2^N\mid D$, contradicting the size bound. This proves (3).

For a single discrepancy set, one may also keep **any fixed shift $q>0$** on an escape. Then $D\ne0$ is fixed and (4) applies. Any repeated line forces $U_N(x_q)-U_N(x)$ to have a constant value, which (4) makes $-D$ by letting $N\to\infty$ dyadically. The endpoints must then satisfy $x_{q+N}/x_N=3^{P_N(x_q)-P_N(x)}$. Both endpoints are ternary units at all sufficiently late times: once an odd departure occurs it produces a unit, and both branches preserve being a unit thereafter. Thus the ratio must be one, contradicting injectivity. This proves $H_S(U_N(x_q)-U_N(x))\ge2^{N-o(N)}$ at every fixed positive shift. If the discrepancy vanishes on a subsequence then (4) already contradicts fixed nonzero $D$.

## Consequence for physical near-repetitions

Suppose the length-$N$ windows at $0,q$ differ only on at most $K$ disjoint intervals, and within each interval the two words have equal odd counts. Let $L$ be the sum of the interval lengths, however large the individual lengths. Then on an escape (3) implies
$$
 \liminf\frac{\log_2(x_q+1)+(\log_2 3)L}{N}\ge1
 \qquad(q,N\to\infty).                                              \tag{5}
$$
Indeed the outside intervals contribute zero, since past odd counts synchronize at every boundary. A changed interval starting at $j$, of length $\ell$ and grade $u$, contributes the difference of its two integer carries times $2^j/3^{P_j(x)+u}$. Thus its $H_S$ is at most $3^\ell$, including the zero convention. Apply (3) with at most $K+1$ sets. With bounded total length this promotes the exact-prefix return threshold to a bounded number of balanced replacements. For unbounded intervals even a fixed small **positive** fraction of changed clocks is permitted in an exclusion argument.

**First unsupported inference.** Neither the true minimality of a bad basin nor the integer prefix equation gives a subexponential upper bound on the prime-to-$S$ mass of its arbitrary two-window discrepancies. Even in (1) an ordinary orbit can have exponentially large prime-to-$S$ carries without violating any integrality condition, as the known cycle of 1 illustrates. The symbolic inputs in the applications prove (5) would fail on their scripts. No step forces such scripts, or any bounded partition violating (3), on a putative arbitrary escape. These measures of forward carry arithmetic do not test the complete denominator of a hypothetical nontrivial positive cycle.

[Lean finite identities](BalancedWindows.lean) · [Lean replay and transitive axiom output](../../../reports/astra-multiple-attacks-20261125/arithmetic/LEAN.json). The kernel checks the physical trace, single-word exact carry, unrestricted unequal-grade two-word divisibility, and chunked equal-grade identities. The subspace theorem, the asymptotic arithmetic deductions, and the symbolic applications are written mathematics.
