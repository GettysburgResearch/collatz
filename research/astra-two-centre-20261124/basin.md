# The marked joint law is singular

**Result conditional on the cited inputs.** The exact PR200 ratio-five return law lifted to \(\mathbb R\times\mathbb Q_3\) is purely singular for product Haar measure. Its branch probabilities equal their product Haar Jacobians, yet it admits no finite positive-volume invariant tile. The proof uses the unmarked seed-image volume bound of [Weaver, paper 19 v2, Section 1](https://rstation.ai/problems/collatz/papers/19), which itself imports a counted-coalescence estimate. The proof below transfers the geometric bound to individual codes, without assuming absolute continuity between the marked and unmarked bit laws.

Let \(f_0(x)=x/2,\ f_1(x)=(3x+1)/2\), acting in both places. Use \(D_L=[0,L)\times\mathbb Z_3\) and \(S_n^L=\bigcup_{|w|=n} f_w(D_L)\), allowing **all** binary words in this union. Normalize product Haar measure \(m\) by \(m(D_1)=1\). The imported bound is \(m(S_n^L)\le CL/\sqrt{n+1}\) for \(L\ge1\).

**Individual codes.** Read the bits \(i_1,i_2,\ldots\) from the outermost map inward. Suppose their one-frequency tends to \(\rho\in(0,\log_3 2)\). Write \(P_j=\sum_{\ell=1}^j i_\ell\), \(\lambda=\log 2-\rho\log 3>0\) and \(a_i=3^i/2\). Each suffix defines a joint affine-series limit \((R_n,Z_n)\) starting after \(n\) bits, with \(R_n\ge0\) and \(Z_n\in\mathbb Z_3\). The ternary series converges because infinitely many ones occur in each suffix. For the real series, given sufficiently small \(\epsilon>0\) we have \(|P_j-\rho j|\le\epsilon j\) for all sufficiently large \(j\). Hence the first \(t\) real multipliers after \(n\) have product at most

$$
\exp\{2\epsilon n\log3-(\lambda-\epsilon\log3)t\}
$$

for all sufficiently large \(n\) and all \(t\ge0\). The additive terms are at most \(1/2\), so a geometric sum gives \(\limsup_n n^{-1}\log(1+R_n)\le2\epsilon\log3\). Sending \(\epsilon\) to zero proves sublinear growth of this logarithm. Any fixed earlier suffix follows by finite composition.

The identities \(1+f_1(r)=\tfrac32(1+r)\) and \(1+f_0(r)=\tfrac12(1+r)(1+1/(1+r))\) now telescope exactly:

$$
\log(1+R_0)-\log(1+R_N)
=P_N\log3-N\log2+
\sum_{\substack{1\le j\le N\\i_j=0}}\log(1+1/(1+R_j)).
$$

The correction sum divided by \(N\) tends to \(\lambda\). Choose an integer \(L\) large enough that \(\log(1+1/(1+L))<\lambda/2\). Each summand is at most \(\log 2\), and those with \(R_j>L\) are at most \(\lambda/2\). Consequently the lower asymptotic frequency of \(j\) with \(R_j\le L\) is at least \(\lambda/(2\log2)>0\). At each such clock the joint endpoint belongs to \(S_j^{L+1}\), since the suffix seed belongs to \(D_{L+1}\).

For every fixed \(L\), the integrated visit frequency through \(N\) is at most \(C'(L+1)/\sqrt N\), by the imported volume bound. These integrals are summable along \(N=2^k\), so the dyadic visit frequencies tend to zero \(m\)-almost everywhere. Thus endpoints with positive lower visit frequency lie in a Haar-null Borel set. Taking the countable union over integer \(L\) gives **one Haar-null set containing the endpoints of every code with limiting one-frequency in \((0,\log_3 2)\)**.

**Application to return marks.** PR200's bound (S2) at commit 39918be7 bounds every length-\(n\) reversed prefix probability by \(C(n+1)^2 2^{-n}\). A fair binomial deviation estimate and Borel–Cantelli imply one-frequency \(1/2\) almost surely. The resulting real and ternary series give the joint stationary law at return marks. Uniqueness follows by coupling two initial points with the same independent outermost-first blocks: the products tend to zero in both places along the block endpoints. Equivalently, for two stationary initial distributions independent of the common blocks, the coupled difference tends to zero in probability. The individual-code result therefore proves pure singularity of this joint law.

For a marked word \(w\) with length \(e\), odd count \(p\), and carry \(C_w\), the map \(F_w=(3^p x+C_w)/2^e\) has product Haar Jacobian \(2^{-e}\), equal to its probability. If a measurable set \(D\) of finite positive Haar volume were tiled almost everywhere by its marked images \(F_w(D)\), normalized Haar measure on \(D\) would be stationary. Uniqueness and pure singularity exclude it. This conclusion concerns product measure. Singularity of the joint law does not decide absolute continuity of its ternary marginal or yield a lower bound at any ordinary integer. Diagonal \(\mathbb Z[1/6]\) is itself nondiscrete in these two places, since \(3^j/2^{2j}\) tends to zero in both.

## Transporting the real fibre on a fixed ordinary cohort

Consider an injective positive odd orbit \(q_t=U^t(m)\). Write its forward prefix as \(F_t(x)=A_t x+C_t\) for its affine branch and \(F_t(m)=q_t\). For any infinite inverse code at \(m\) with real evaluation \(R_m\), prefixing the actual segment gives an inverse code at \(q_t\) with real evaluation \(R_{q_t}=F_t(R_m)\). Thus

$$
\frac{q_t-R_{q_t}}{q_t}
=\frac{m-R_m}{m}\prod_{j=0}^{t-1}\frac{3q_j}{3q_j+1}.
$$

Weaver's nonperiodic integer-fibre separation (B4) bounds the first factor below by an absolute positive constant. The product also has a positive lower bound independent of \(t\), by the distinct-state reciprocal occupation bound (B2) and \(\log(1+u)\le u\). Thus transporting the actual retained cohort along its known orbit keeps a positive **relative** distance from the diagonal. The same calculation applies through any genuine return marks within its path. It supplies no code with real evaluation equal to its ternary integer value.

## An explicit residue bias

The stationary distribution of PR200's marked dictionary differs from the unmarked Syracuse offset law already modulo three. The calculation uses the mark convention in REVERSE_RENEWAL.md at commit 39918be7. Absolute continuity remains open here.

Let \(d\) count the trailing zero bits of the chronological first-return word, before padding. The word starts with a one. After the return, the number \(b\) of additional zero bits before the next odd mark is independent of the word, with probability \(2^{-j-1}\) at \(j\ge0\). Reading backward, the last consumed one is at position \(A_1=1+d+b\). For the sign character of the units modulo three, the offset expansion gives

$$
\mathbb E_\nu\chi=\mathbb E(-1)^{A_1}=-\tfrac13\mathbb E(-1)^d.
$$

In the unmarked Syracuse law \(S\), the first backward gap is geometric on the positive integers, so \(\mathbb E_S\chi=-1/3\).

The class \(x=49\bmod 64\) has first-return source word 101000. At its canonical representative the paired trajectories are

| Clock | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Source | 49 | 74 | 37 | 56 | 28 | 14 | 7 |
| Companion | 245 | 368 | 184 | 92 | 46 | 23 | 35 |

The first positive ratio-five endpoint is at clock six, with two odd bits on each arm. In a lift by \(64t\), the two endpoints at clock \(j\) change by \(2^{6-j}3^{p_X(j)}t\) and \(5\cdot2^{6-j}3^{p_Y(j)}t\), respectively. Unequal odd counts exclude a root by definition. At equal counts the ratio-five error is unchanged. Thus the whole class has this first return. Its conditional probability given an odd source is \(1/32\), and \(d=3\). Consequently

$$
\nu(1\bmod3)-S(1\bmod3)=\tfrac13\Pr(d\text{ odd})\ge 1/96.
$$

The mark spacing also precludes a direct positive-intensity Palm identification. PR146's FIVE_RETURN_CLOCK_AND_TERMINALS.md at f431078 gives \(\Pr(h>n)\asymp n^{-1/2}\) even after fixing the first bit odd. Thus \(L=h+b\) has infinite mean. With \(u_j\) the renewal probability at clock \(j\), including \(u_0=1\), the probability of observing a mark at an independent geometric clock of mass \((1-s)s^j\) is

$$
(1-s)\sum_{j\ge0}u_js^j=\frac{1-s}{1-\mathbb E s^L}\asymp\sqrt{1-s}.
$$

The estimate follows by summing the tail in \(1-\mathbb E s^L=(1-s)\sum_{j\ge0}s^j\Pr(L>j)\). A nonconstant density relative to the unmarked law remains possible. Neither the residue discrepancy nor the geometric-clock estimate supplies such a density or a lower estimate at an individual ordinary target.

The companion finite control [basin.py](basin.py) checks 3,069 multiplicative forms of the real telescoping identity at rational seeds and 1,024 lifts of the first-return cylinder. It does not verify the imported asymptotic volume estimate.

## Electrical conductance and the side cut

Write \(d(x)\) for the relative odd predecessor density, and restrict the inverse tree to odd units in an escaping component. [Weaver, paper 12 v1, Sections 8–10](https://rstation.ai/problems/collatz/papers/12) gives \(d(x)=\sum_{Uy=x}d(y)\), the canonical profile equation \(h(x)=\sum_{Uy=x}3\,2^{-e_y}h(y)\), and \(h(x)\asymp x d(x)\) at nonperiodic units. Here \(e_y=v_2(3y+1)\). Give the edge from \(x\) to its forward parent conductance \(d(x)\). Each inverse generation below a root \(a\) is then an edge cut of total conductance \(d(a)\). A unit current across \(N\) such disjoint cuts has energy at least \(N/d(a)\) by Cauchy–Schwarz on each cut. This is a recurrence estimate for the symmetric network on that inverse tree. The directed process which only chooses children with probabilities \(d(y)/d(x)\) has different transitions.

There is an actual second conserved flow. On the escaping component put

$$
l(x)=\frac{3x}{3x+1},\qquad W(x)=\prod_{j\ge0}l(U^jx),\qquad
g(x)=W(x)h(x)/x.
$$

The uniform reciprocal packing bound makes \(W\) bounded away from zero. The identities \(W(y)=l(y)W(x)\) and \(3\,2^{-e_y}/x=l(y)/y\) when \(Uy=x\) prove \(g(x)=\sum_{Uy=x}g(y)\). Paper 12, equations (23)–(24), also identifies this flow up to a fixed factor with the ordinary basin mean of \(W\). The ratio \(g/d\) is harmonic for the directed inverse chain. On the symmetric network of the **whole escaping component**, it is the *increments* \(V(Ux)-V(x)=g(x)/d(x)\) which define a harmonic potential. (On a rooted inverse subtree the root has a boundary current instead.) This potential increases by at least \(g(m)\) at each forward step from \(m\), since \(g(q_t)\ge g(m)\) and \(d(q_t)\le1\). It is unbounded, so a recurrence-based bounded-harmonic argument does not yield a constant potential.

The bounded arithmetic function \(W\) itself has unnormalized symmetric Laplacian

$$
\Delta_d W(x)=\frac{W(x)d(x)}{3x}
\left(1-3\sum_{Uy=x}\frac{d(y)}{d(x)}2^{-e_y}\right).
$$

This follows by taking its difference from the parent and from every child. A child of exponent one prevents a uniform sign deduction from the exponent bounds alone. Weighting the edge instead by \(x d(x)/W(x)\) makes \(W\) exactly harmonic, with current \(d(x)/3\). But that network has a finite-resistance forward ray, since \(\sum_t W(q_t)/(q_t d(q_t))\le d(m)^{-1}\sum_t1/q_t<\infty\). It cannot supply the recurrence needed for the proposed contradiction.

To quantify the multi-descendant attempt, let \(C(a)\) be the supremum of \(\sum_{x\in A}1/x\) over finite unit antichains in the inverse tree. The reciprocal floor and disjointness give \(C(a)\le d(a)/c\). Conversely, paper 12's finite profile equation and Cesàro trace give

$$
\rho_{j+1}(a)=\sum_{U^jx=a}\Omega_j(x)\rho_1(x)\le 2a\,C(a),
\qquad
\lim_{N\to\infty}N^{-1}\sum_{j<N}\rho_{j+1}(a)=h(a).
$$

Indeed \(\rho_1\le2\) vanishes on nonunits, \(\Omega_j(x)\le a/x\), and a fixed generation is an antichain. Thus single-generation cuts already give \(C(a)\ge h(a)/(2a)\gg d(a)\). For PR202's modular router alone, common depth \(b(k)\) supplies at least \(2\cdot 3^{k-1}\) unit descendants of \(a\), one per unit class, all at most \((4/3)^{b(k)}a\). The cardinality over upper height certificate is \(2\cdot3^{k-1}(3/4)^{b(k)}/a\). Its numerator is at most one because the same router at \(a=1\) must fit the same number of distinct positive integers below \((4/3)^{b(k)}\). Counting its guaranteed representatives by height cannot increase the reciprocal scale. An improved estimate would have to exploit the sizes or extra multiplicities of actual side descendants. No divergent sum over the side cuts was obtained.
