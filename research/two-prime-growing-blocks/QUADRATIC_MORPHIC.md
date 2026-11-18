# Quadratic morphic words reduce to finitely many linearly growing runs

**Proposed.** Consider any binary shortcut-parity word with a tail
$$
 \prod_{n\ge0} U_0 V_1^n U_1 V_2^n\cdots U_{d-1} V_d^n U_d,            \tag{1}
$$
where the $U_i$ are arbitrary fixed words (possibly empty) and the $V_i$ are nonempty. Let $s$ be the sum of the lengths of the $V_i$ and $l$ their total number of ones. Any positive rational 2-adic orbit realizing this word is eventually periodic if $l=0$, or if
$$
 \frac{s}{l\log_2 3}>\frac{4d^2-2d+1}{4d^2+2d+1}.
$$
In particular this holds for **all one- or two-run templates regardless of the fixed decorations**. More precisely the same bound uses the number of surviving Gaussian-series coefficients in the reduction below, even when there are more displayed runs.

Every letter-coded fixed word of a nonerasing substitution with quadratic seed-length growth has a tail of form (1). For linear seed-length growth such a word is eventually periodic. Combined with the [exponential-presentation result](../local-mahler-lifting/EXPONENTIAL_MORPHIC.md), this specifies both the first remaining polynomial-growth case and a direct exclusion inside it.

### From polynomial substitution growth to (1)

Pass to a common positive power so each recurrent letter in the reachable incidence graph has exactly one self-copy and no other letter in its strongly connected component. Indeed a nonnegative irreducible integer block of spectral radius one is a cyclic permutation matrix: two distinct paths of the same positive length returning to a vertex would give exponential growth, and any branching in a finite strongly connected graph gives such paths by concatenation. Further powers and finite initial shifts freeze the iterated images of bounded letters, since there are only finitely many words of bounded length.

For the prolongable seed $a$, write $\sigma(a)=aW$. Then its fixed word is $a\,W\,\sigma(W)\,\sigma^2(W)\cdots$. Along the chosen power, every growing length is eventually polynomial: the nonnilpotent diagonal blocks are singleton ones, so all nonzero eigenvalues are one. For linear seed growth, $|\sigma^j(W)|$ is bounded, giving an eventually periodic tail. For quadratic growth, that length is eventually linear and every letter reachable from $W$ has at most linear growth.

For any recurrent letter $b$ in this latter subalphabet with linear growth we have $\sigma(b)=P_b b Q_b$. All letters in $P_b,Q_b$ are bounded, since the sum of their iterated lengths enters $|\sigma^j(b)|$ and an unbounded term after the selected power grows at least linearly. Thus for all sufficiently large $j$, the words $\sigma^j(P_b),\sigma^j(Q_b)$ are constant. Iterating the displayed form yields $L_b^n C_b R_b^n$ for $\sigma^{J+n}(b)$ with fixed $J$ and fixed words $L_b,C_b,R_b$. Transient linear letters can be removed by a further finite initial expansion of $W$: a path from a linear transient to another linear transient cannot go through a recurrent linear or bounded letter, by the previous observation, so only finitely many such transitions in sequence are possible. Now concatenate the fixed bounded images and the displayed recurrent-letter forms and apply the letter coding. This gives (1) after a finite prefix, omitting empty powered blocks and absorbing fixed material in the $U_i$.

### From decorated runs to Gaussian series

The inverse affine map of any binary word $V$ of length $s_V>0$ with $l_V$ ones is $X\mapsto p_V+r_V(X-p_V)$, with $r_V=2^{s_V}/3^{l_V}\ne1$ and rational fixed point $p_V$. Each fixed decoration has its own rational affine map, with the identity allowed. Multiplying the maps in (1) for a single $n$ shows its inverse slope is $a q^n$, where $q=2^s/3^l$ and $a>0$ is the product of the decoration slopes. Its translation has the form
$$
 b(n)=c_0+\sum_{i=1}^{d-1}c_i w_i^n+c_d q^n,\qquad
 w_i=\prod_{j=1}^i r_{V_j}.
$$
Indeed each powered map has translation $p_{V_j}(1-r_{V_j}^n)$, and composing translations multiplies them by the preceding slopes. All coefficients are fixed rationals.

The 2-adic boundedness of the ordinary terminal states makes the starting value the convergent sum $\sum_{n\ge0}a^nq^{\binom n2}b(n)$. For $F_q(z)=\sum_{n\ge0}z^n q^{\binom n2}$ use $F_q(aq)=(F_q(a)-1)/a$. This leaves a rational constant plus at most $d$ Gaussian series with nodes $a,aw_1,\ldots,aw_{d-1}$ and coefficients $c_0+c_d/a,c_1,\ldots,c_{d-1}$. Distinct nodes have distinct 2-valuations in an interval of width below $s$; their denominators are powers of three. If necessary use $F_q(z)=1+zF_q(qz)$ once at all nodes so all valuations are positive. Nonzero coefficients remain nonzero. Apply the [two-prime Hankel criterion](PROOF.md) to the surviving terms. The threshold increases with their number. For two terms $13/21<1/\log_2 3\le s/(l\log_2 3)$, and one term has a smaller threshold.

If all coefficients disappear, all macro inverse maps are $X\mapsto c_0+a q^n(X-c_0)$. The unique bounded 2-adic starting tail at every macro boundary is $c_0$, by letting the product of future slopes tend to zero. The ordinary deterministic orbit therefore revisits its macro state and is eventually periodic. Finally $l=0$ gives zero asymptotic frequency of odd letters, impossible on a divergent positive rational trajectory by its telescoping logarithmic growth bound.

The same exclusion holds for rational 2-adic sources of either sign. For $l>0$ the nonzero Gaussian-series obstruction already concerns arbitrary rational values, and the common-pin case returns to the same state regardless of sign. For $l=0$, on any nonperiodic signed rational orbit the nonzero real limit of $2^N3^{-s_N}x_N$ proved in the [signed orbit argument](../local-mahler-lifting/SIGNED_PARITY.md) gives $\log|x_N|=s_N\log3-N\log2+O(1)$. This precludes the zero odd frequency of the template. Thus the transcendence dichotomy for exponential morphic words and the rational exclusion for decorated quadratic words have the same signed source domain, although the latter is an irrationality result.
