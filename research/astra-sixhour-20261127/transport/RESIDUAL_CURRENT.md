# An ordinary component current on the positive residual coordinate

Fix one hypothetical escaping odd component \(C\). Include every positive even integer whose odd part belongs to \(C\). Use the stationary ordinary-fibre measures \(\lambda_y\) and their retained-first-exponent even lifts from [the fixed-target susceptibility](SUSCEPTIBILITY.md). Define positive Borel measures on the residual coordinate \(u=y-r\) by
\[
       \nu_y(E)=\int {\bf1}_{\{y-r\in E\}}{\lambda_y(dr)\over y-r}.
\]
Write \(\nu=\sum_y\nu_y\), with \(\nu_o,\nu_e\) its odd and even parts. On the specified component all odd inverse paths are simple. The verified floor and simple-path bound give \(5y/6\le y-r\le y\), first on odd vertices and then under even lifts. Thus only finitely many ordinary vertices contribute to each compact interval, and the measures are Radon, supported away from zero. The singular real-fibre theorem makes each summand singular, hence also their countable sum. These claims concern this one component. [Ordinary floor and simple-path product](../descent/DISTORTION.md) · [Canonical ordinary fibre and bilateral coupling](https://github.com/GettysburgResearch/collatz/blob/795cfa38fbd6a2436285edfe82580680df4f9b0d/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md)

Write \(D_a(u)=au\), with its action on measures by pushforward. The retained-layer identity (8) of the susceptibility note gives exactly
\[
 D_2\nu_y=\nu_{2y}
              +{\bf1}_{\{3\mid 2y-1\}}D_3\nu_{(2y-1)/3}.           \tag{1}
\]
If the odd predecessor is a nonunit its measure is zero. The first branch has residual \(2(y-r)\), whereas the branch from \(x=(2y-1)/3\) has residual \(2y-(3r+1)=3(x-r)\); the prefactors 2 and 3 therefore disappear on dividing by the residuals. Every positive odd \(x\) occurs for \(y=(3x+1)/2\) in the same component. Summing positive measures gives
\[
 (D_2-I)\nu=(D_3-I)\nu_o,\qquad
                   \nu((X/2,X])=\nu_o((X/3,X])\quad (X>0).         \tag{2}
\]
For \(\sigma\ge1\) put \(M(\sigma)=\int u^{-\sigma}\nu(du)\) and define \(M_o\) similarly. These are finite: the even lifts and the floor give a constant times \(\sum_{a\ {\rm odd}}h(a)/a^{1+\sigma}\) after the summable even scaling factors \(2^{-j\sigma}\). Finiteness at \(\sigma=1\) follows from the discounted trace input. Therefore
\[
                   (1-2^{-\sigma})M(\sigma)
                    =(1-3^{-\sigma})M_o(\sigma).                    \tag{3}
\]
Equivalently under the probability on odd marked fibres obtained by normalizing \(u^{-\sigma}\nu_a(du)\), the actual first canonical reversed exponent \(E_1\) satisfies \(\mathbb E_\sigma[(3\,2^{-E_1})^\sigma]=1\). In fact \(M\) counts a source \(a\) at the even heights \(2^ja\) precisely for \(0\le j<E_1\), with moment multipliers \(2^{-j\sigma}\); sum this finite geometric series before substitution in (3).

There is an explicit disintegration at every fixed ordinary odd grade \(j\). Give the bilateral ordinary path on \(C\) its flux probability, with positions \(Z_j\), corrected height \(P(y)\), and bilateral product \(J_C\). Then \(y-r=P(y)J_C\) conditional on \(Z_j=y\), and \(h(y)/P(y)=H_C\,\mathbb P(Z_j=y)\). Consequently
\[
 \sum_{g(y)=j}\nu_y
     =H_C\,\mathbb E[J_C^{-1}\delta_{P(Z_j)J_C}], \qquad
 \nu_o=H_C\,\mathbb E\left[J_C^{-1}
                     \sum_{j\in\mathbb Z}\delta_{P(Z_j)J_C}\right]. \tag{4}
\]
Fix a grade-zero ordinary anchor \(q\), and let \(\pi(u)=\log_2u\bmod1\).
The corrected grade lattice gives \(P(Z_j)=P(q)3^j2^\ell\) with integer \(\ell\). Each grade's circle measure is therefore precisely the rotation through \(j\log_2 3\) of the finite measure \(H_C\,\pi_*(\operatorname{Law}(P(q)J_C)\ \text{weighted by }1/J_C)\). In particular these finite measures retain a nonvanishing first harmonic: \(J_C\in[5/6,1]\) confines the initial circle measure to an arc of length \(\log_2(6/5)<1/2\), so its first harmonic divided by its total mass has absolute value at least \(\cos(\pi\log_2(6/5))>0\). Their Cesàro means over consecutive grades converge weakly to their total mass times Haar probability, by the irrational rotation and trigonometric polynomials. The grade-zero measure is singular and lives on the supplied component. The Haar limit involves a growing number of different grades.

The component floor does not by itself upgrade (2) to separate dilation invariance. For a concrete balance control, take any compactly supported positive singular probability for \(t\) in \([1,5/4]\). For each such \(t\) put even atoms at \(2^nt\) for \(n\ge1\), odd atoms at \((3/2)^nt\) for \(n\ge0\), all with unit mass, and integrate over \(t\). These nonzero locally finite singular measures have a positive floor and satisfy \(D_2\nu=\nu_e+D_3\nu_o\) by reindexing the two geometric series. The control concerns the balance and the floor only. Equations (1) and (4) specify the additional genuine integer fibre, exponents and grade constraints. No derivation of separate dilation invariance for these actual fibres is available; nonzero separate \(D_2\)-invariance would itself contradict their positive floor.

## The lowest residual and its first reversed mark

There is a quantitative constraint at the bottom of this same component. Write \(\nu_o^{[e]}\) for the odd submeasure retaining \(E_1=e\), let \(u_*=\inf\operatorname{supp}\nu_o>0\), and use the probability from (3). Since the multiplier is \(3/2\) at \(e=1\) and at most \(3/4\) otherwise,
\[
 {1-(3/4)^\sigma\over(3/2)^\sigma-(3/4)^\sigma}
 \ \le\ \mathbb P_\sigma(E_1=1)\ \le\ (2/3)^\sigma .
\]
In particular the probability is \((2/3)^\sigma(1+o(1))\) as \(\sigma\to\infty\), with the coefficient one. The odd one-step stationary balance underlying this moment is the measure identity
\[
                          \nu_o=\sum_{e\ge1}D_{2^e/3}\nu_o^{[e]}.
\]
It follows directly by flowing each retained inverse branch back to its odd predecessor; before division by the residual the branch multiplier is \(3/2^e\), exactly the same factor as the transformation of the residual. Therefore on every Borel \(B\subset[u_*,4u_*/3)\) one has the exact copy
\[
                              \nu_o(B)=\nu_o^{[1]}((3/2)B).
\]
Also \(\nu_o^{[1]}((0,3u_*/2))=0\), by the same positive balance below the floor. Thus \(\inf\operatorname{supp}\nu_o^{[1]}=3u_*/2\) and the first mark has a completely specified measure in that next band. This is a local conclusion for the entire genuine component. It does not give the equality of the unmarked measure with its dilation on all bands.
