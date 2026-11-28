# Complete denominators of rational cycles of odd width strictly below three

**Proposed written theorem using the cited inputs.** Let \(m,X,p,q\) be the real odd minimum, real odd maximum, primitive odd period and complete reduced denominator of a positive rational Syracuse cycle. Fix \(2<R<3\), suppose \(X/m\le R\), and write
\[
 \gamma=\log_2 3,\quad\alpha=\gamma-1,\quad\eta=\log_2(R/2),\quad
 \nu=5.116201,\quad
 \theta=\frac{\eta}{6\gamma}\log_2\frac{4096}{924},\quad
 b=\frac1{\nu\theta}-1,\quad \chi=\frac{\eta\log6}{3\log3}.
\]
Then
\[
 \liminf_{m\to\infty}\frac{\log q}{\log m}\ge b,\qquad
 \liminf_{p\to\infty}\frac{\log q}{\log p}\ge\frac{b}{b+\chi}.          \tag{1}
\]
Limits run over the cycles in this fixed band. The lower bounds increase as \(R\) decreases. As \(R\uparrow3\) the constants on the right tend to \(0.479141\ldots\) and \(0.601066\ldots\), respectively. The proof applies to arbitrary native valuations and to clocks with \(\gcd(\sum e_t,p)>1\). It requires a fixed width margin below three.

The ingredients are the [ordinary six-mass excursion classification](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md), the [sparse integer recurrence theorem](SPARSE_RANK_RECURRENCES.md), and a spatial array constructed from genuine, possibly backward, chronological shifts. Its sampling step comes from \(\gamma\), independently of the cycle clock. A zero of a rational comparison supplies integer comparisons on the entire circuit. The period conclusion additionally uses a [uniform rational four-copy source count](https://github.com/GettysburgResearch/collatz/blob/5136b7fe70176172405a0de168a2de2ed26429b8/research/astra-global-rigidity-20261128/cycles/FOUR_COPY_WIDTH.md), which built on Weaver's [located count](https://rstation.ai/problems/collatz/papers/145/v1) and [confined ordinary source theorem](https://rstation.ai/problems/collatz/papers/181/v1). That rational count and the two-logarithm estimate alone give only \(1-\nu\chi\) as the period exponent, negative near width three. Classical [Halbeisen–Hungerbühler minimum estimates](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf) relate the rational minimum and the odd/halving clock.

## A chronological grid at a controlled physical scale

Extend the true odd trajectory \(x_t\) and its native exponents \(e_t\ge1\) periodically to \(t\in\mathbb Z\). Write \(A=\sum_{t=0}^{p-1}e_t\), \(E_0=0\), \(E_{t+1}=E_t+e_t\) and \(\widetilde X_t=2^{E_t}x_t\). Then
\[
 \log_2(\widetilde X_{t+1}/\widetilde X_t)=\gamma+\epsilon_t,\quad
 0<\epsilon_t=\log_2(1+1/(3x_t))\le C/m,\quad
 \widetilde X_{t+p}=2^A\widetilde X_t.                                  \tag{2}
\]
The reduced numerator of each \(x_t\) is odd and its reduced denominator is the same odd \(q\). Indeed a full lap gives a denominator dividing \(2^A-3^p\), prime to six, and every forward update preserves reduction at all primes of \(q\).

Let \(Q_i\) be the consecutive denominators of the continued-fraction convergents of \(\gamma\). From [Bondareva–Luchin–Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) we have \(\|d\gamma\|\ge c d^{1-\nu}\) for integers \(d\ge1\), and hence \(Q_{i+1}\ll Q_i^{\nu-1}\). With \(m\to\infty\), take the last \(i\) such that \(Q_iQ_{i+1}\le m/\log m\). Set \(\tau=\pm Q_i\) with sign chosen so that \(\tau\gamma=k+\vartheta\), \(k\in\mathbb Z,\ \vartheta=\|Q_i\gamma\|>0\), and \(N=\lfloor 1/\vartheta\rfloor\). The convergent inequalities give \(Q_{i+1}<1/\vartheta<Q_{i+1}+Q_i\). Consequently
\[
   N|\tau|\ll m/\log m,\qquad N\gg(m/\log m)^{1/\nu},\qquad
   \max_{0\le r\le N}|r\vartheta-r/N|\le 1/N.                            \tag{3}
\]
For the middle bound use \(m/\log m<Q_{i+1}Q_{i+2}\ll Q_{i+1}^{\nu}\). Neither \(\tau\bmod p\) nor any actual clock fraction is assumed to generate a cyclic group.

Choose \(v>0\) with \(v+\eta<\alpha\), put \(L=2^{1-v}m\), and define the *true base* at every integer time by
\[
 F_t=\lfloor\log_2(\widetilde X_t/L)\rfloor,\qquad
 f_t=\log_2(\widetilde X_t/L)-F_t,\qquad h_t=F_{t+1}-F_t.
\]
In particular \(F_{t+p}=F_t+A\). Take \(W=\lfloor N/(\log N)^5\rfloor\). The synchronized columns and their actual tags, for \(0\le j\le W\), are
\[
 Z_{t,j}=2^{-F_t-kj}\widetilde X_{t+j\tau},\qquad
 c_{t,j}=2^{E_{t+j\tau}-F_t-kj},\qquad
        2^{h_t} Z_{t+1,j}=3Z_{t,j}+c_{t,j}.                              \tag{4}
\]
They are \(p\)-periodic in \(t\), including for negative \(\tau\). By (2)–(3)
\[
 \log_2(Z_{t,j}/L)=f_t+j\vartheta+O(j|\tau|/m)=f_t+o(1)                  \tag{5}
\]
uniformly in \(t,j\). Since \(Z_{t,j}=c_{t,j}x_{t+j\tau}\), the strictly positive margins \(L>X/2\) and \(2L<4m\) force \(c_{t,j}\in\{1,2\}\). In particular \(q Z_{t,j}\) is an integer. At \(f_t<v-o(1)\) all tags equal one since \(Z_{t,j}<2m\); at \(f_t>v+\eta+o(1)\) all tags equal two since \(Z_{t,j}>X\).

We also need a single long integer array. Choose an anchor \(t_*\) with \(f_{t_*}=o(1)\) from above. Such anchors exist: as \(m\to\infty\), the empirical measures on the period of \(f_t\) are asymptotically invariant under rotation by \(\gamma\), by (2), so all weak limits are Haar and every fixed open interval \((0,\epsilon)\) is eventually visited. Write
\[
 Y_r=2^{-F_{t_*}-kr}\widetilde X_{t_*+r\tau},\qquad 0\le r<N .
\]
The same sum in (2), this time up to \(N|\tau|\) edges, gives
\[
 \log_2(Y_r/L)=f_{t_*}+r/N+O(1/N+N|\tau|/m)=r/N+o(1)                   \tag{6}
\]
uniformly. The margin argument following (5) again shows \(Y_r/x_{t_*+r\tau}\in\{1,2\}\), so \(qY_r\) is an integer bounded by \(O(qm)\). For \(r/N\) in any compact subinterval of \((0,1)\) and \(j\le W,\ r+j<N\), (6) gives **exactly**
\[
  F_{t_*+r\tau}=F_{t_*}+kr,\quad f_{t_*+r\tau}=r/N+o(1),\quad
                    Z_{t_*+r\tau,j}=Y_{r+j}.                             \tag{7}
\]
The construction does not sort rational phases or identify phases with the same ideal rank.

## Six equal summands would force a sparse zero interval

For two different multisets of six offsets in \([0,W]\), let \(P(T)\) be the signed difference of their monomials, \(H_t=\sum_j P_j Z_{t,j}\), \(d_t=\sum_j P_j c_{t,j}\). Then \(P\ne0,\ \sum P_j=0,\ |d_t|\le6\), and \(2^{h_t}H_{t+1}=3H_t+d_t\). Suppose \(H_{t_0}=0\) at one date. Now **all** \(H_t\) are integers: \(qH_t\in\mathbb Z\), and \(q\mid qH_t\) propagates to \(q\mid qH_{t+1}\) in (4) since \(q\) is odd. Periodicity covers every date. When all tags equal two, \(d_t=0\) and \(4\mid H_t\), since every \(qZ_{t,j}\) is twice an odd numerator and \(\sum P_j=0\).

Put \(a_t=\gamma-1+\epsilon_t\). The true angles satisfy \(f_{t+1}=\{f_t+a_t\}\) and \(h_t=1+\lfloor f_t+a_t\rfloor\). Uniformly \(1/2<a_t<2/3\) for large \(m\), hence the calendar has no consecutive ones and no three consecutive twos. A date after a one has \(f_t\ge\alpha>v+\eta\), hence it is forced two in its tags. Choose a fixed closed interval \(J\) of positive length inside
\[
             (\max\{v+\eta,1-\alpha\},\ \alpha).
\]
Whenever \(f_t\in J\), the current winding is two, its predecessor winding was two (a preceding one implies \(f_t\ge\alpha\)), and the current tags are all two.

Here is the integer run argument with this variable-increment calendar. In a positive run entered from a nonpositive value, a one cannot give the first positive value, since the successor is divisible by four and \(2H'\le6\). Nor can a forced two give it. Hence it is born at an active second two and the next value is one, at a winding of type one. At a type-one date carrying a value in \(\{1,2,3\}\) in this run, the next value, if positive, is four because \(2H'\le15\) and \(4\mid H'\). The forced first two then sends four to three. This reaches either the next one, or the second two in a two-symbol run, from which a continuing positive successor lies in \(\{1,2,3\}\) by \(4H'=9+d\). Thus every second two reached within a positive run has value three. Negation gives minus three in negative runs. Since a zero exists somewhere on the full circuit, all nonzero values belong to such entered runs. On \(J\) the divisibility by four excludes both possibilities. Hence \(H_t=0\) at every date with \(f_t\in J\).

By (7), on a fixed interval interior to \(J\) the true integer sequence \(qY_r\) satisfies \(P(E)(qY)_r=0\). If \(qm\le N^K\) for fixed \(K\), this contradicts the [sparse recurrence theorem](SPARSE_RANK_RECURRENCES.md) by (6), with scale \(qL\), at most twelve terms of \(P\), degree at most \(W\), and coefficients bounded by six. We have proved that along every such polynomial-height sequence all six-sums of the columns at every temporal base are distinct for sufficiently large \(m\).

## Coding and the complete denominator

At any one base record the tags in these \(W+1\) columns over \(n=\lceil\log_3(16qL)\rceil+2\) successive dates. Two coordinatewise equal six-sums over the integers give \(d_t=0\) on all \(n\) dates. Then \(2^{F_{t+n}-F_t}\mid qH_t\) by (4), since three is odd. From (2), this divisor is at least \(2^{n\gamma-1}>12qL\); equation (5) gives \(|qH_t|<12qL\) for large \(m\) (each of the two sums lies between \(6qL(1-o(1))\) and \(12qL(1+o(1))\)). Thus \(H_t=0\), and the six-sum conclusion identifies the original multiset.

The variable tag rows have angles in \([v-o(1),v+\eta+o(1)]\). On a polynomial-height sequence \(qm\le N^K\) we have \(n=O_K(\log m)\), since \(N\ll m\); thus over these \(n\to\infty\) dates accumulated perturbation is \(O(n/m)=o(1)\). The underlying irrational rotation has interval discrepancy tending to zero, uniformly in its starting angle. It follows that deleting all constant rows yields a binary \(B_6\) code of length at most \((\eta+o(1))n\) and size \(W+1=N^{1-o(1)}\). This only requires that equality of six binary sums implies equality of source multisets.

For a binary \(B_6\) code of size \(M\) and length \(d\), the collision probability of six iid codewords summed over the integers is at most \(6!/M^6\). Its minimum over *all* distributions on the cube is \((\binom{12}6/2^{12})^d\). Indeed it is the twelfth power of the torus \(L^{12}\)-norm of the characteristic polynomial, convex in the distribution and invariant under coordinate flips. Averaging over the flips attains the uniform cube, where the one-coordinate probability is \(924/4096\). This is the [Polyanskiy argument in Gu, Proposition 3.8](https://arxiv.org/abs/1809.07364). We conclude
\[
                       \log N\le (\theta+o(1))\log(qm).                   \tag{8}
\]
If \(\log(qm)/\log N\) is unbounded, pass to subsequences where it tends to infinity or stays bounded. In the former case (8) in its limsup-ratio sense is automatic. In the latter the established polynomial-height argument applies. Combining (3) and (8) gives the minimum bound in (1).

The uniform rational four-copy theorem cited above gives \(p\ll_{R,\epsilon}q(1+m)^{\chi+\epsilon}\). For bounded \(m\), distinct odd numerators in the width band already give \(p=O_R(q(1+m))\). For growing \(m\), the first conclusion gives \(m\le q^{1/(b-o(1))}\) since \(b>0\) throughout \(R<3\). Substitute this in the four-copy bound and send \(\epsilon\) to zero to obtain the second conclusion. This argument estimates the full reduced odd denominator of each cycle; no selection of denominator primes enters it.
