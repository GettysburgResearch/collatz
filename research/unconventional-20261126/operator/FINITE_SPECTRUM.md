# Uniformly computable norms and selfadjoint spectra on the ordinary graph

**PROPOSED constructive theorem.** For a finite *-polynomial $P$ with rational-complex coefficients, in the two shortcut branch operators and finitely specified rational-complex periodic diagonal tables, its full counting-space operator norm is uniformly computable. If $P$ is selfadjoint, its spectrum is uniformly computable in Hausdorff distance. By [O1](COMPONENT_OPERATORS.md), the same output applies to every individual weak component, including the basin of 1. The resource bounds below are intended to terminate; their growth makes them unsuitable for large precision requests.

## A finite localization error from forward paths

Use the undirected graph metric. Let $r$ be the largest number of branch or adjoint factors in a monomial. Pick a computable $M\ge\|P\|$, for example the sum of the absolute scalar coefficient bounds of its monomials multiplied by the sup norms of all corresponding diagonal factors. A rational upper bound for each such summand suffices. A radius-$r$ ball contains at most $B_r=3\cdot2^r-2$ vertices, for the maximum undirected degree is three. For $S\ge1$, define
$$
    \mu_x(z)=\frac1S\sum_{j=0}^{S-1}1_{T^j x=z},
       \qquad \xi_x(z)=\sqrt{\mu_x(z)},\qquad
       (\chi_z u)(x)=\xi_x(z)u(x).
$$
Each $\chi_z$ is supported on $B(z,S)$, and $\sum_z\|\chi_z u\|^2=\|u\|^2$. The total $\ell^1$ difference of $\mu_x,\mu_{Tx}$ is at most $2/S$ by telescoping the two orbit segments, also when points repeat. Along a path of length at most $r$ it is at most $2r/S$. Since $(\sqrt a-\sqrt b)^2\le|a-b|$, we have $\sum_z|\xi_x(z)-\xi_y(z)|^2\le2r/S$ at that distance.

Row Cauchy–Schwarz uses at most $B_r$ entries per row. Summing entrywise and using the squared norms of the columns $P\delta_y$ gives
$$
 \sum_z\|[P,\chi_z]u\|^2
 \le B_r\sum_{x,y}|P_{xy}|^2 |u(y)|^2
                  \sum_z|\xi_x(z)-\xi_y(z)|^2
 \le \delta_S^2\,\|u\|^2,\qquad
 \delta_S=M\sqrt{2r B_r/S}.
$$
This follows first for finite vectors and then by continuity. It also holds with zero error when $r=0$.

For center $z$ form the rectangular matrix $P_{z,S}$ of $P$ on *inputs* supported in $B(z,S)$, with all outputs in $B(z,S+r)$ retained. Let $L_S=\sup_z\|P_{z,S}\|$ and $l_S=\inf_z\nu(P_{z,S})$, where $\nu(A)=\inf_{\|v\|=1}\|Av\|$ is the lower norm. The extra output rows are essential. The direct-sum triangle inequality for $(P\chi_z u)_z$ and $(\chi_z Pu)_z$ yields
$$
 L_S\le\|P\|\le L_S+\delta_S,\qquad
 l_S-\delta_S\le\nu(P)\le l_S.
$$
For the upper norm, bound $\sum_z\|P\chi_z u\|^2\le L_S^2\|u\|^2$. For the lower norm use $\sum_z\|P\chi_z u\|^2\ge l_S^2\|u\|^2$. The inequalities in the other directions follow by restricting the inputs.

## All relevant matrices have a finite, effective list

Put $R=S+r+1$ and let $d$ be a common diagonal period. Enumerate every formal word of length at most $R$ in the rational affine maps $X/2,(3X+1)/2,2X,(2X-1)/3$, including its prefixes, without requiring legality. This gives finitely many distinct rational affine maps of positive slope. Compute a threshold $H$ above every positive equality root of two distinct maps and above every zero of any map. For centers $z>H$, the list of coincidences between legal path endpoints depends only on *identity of affine maps*. Which paths are legal and which diagonal coefficients occur depend only on $z\bmod d6^{R+1}$: every slope denominator divides $6^R$, and the difference under a root increment of $d6^{R+1}$ is divisible by $6d$ for each partial map. All involved values on legal paths are positive. Forward-domain and inverse-domain restrictions use only parity and residues modulo 3.

Hence it suffices to check every ordinary center from 1 to $H$ and one ordinary center greater than $H$ in each residue class modulo $d6^{R+1}$. Compute each matrix by multiplying the actual branch and diagonal entries along the words; when two words have the same matrix entry their contributions are added. This directly lists every localized matrix up to relabeling, including those at low centers on a short cycle. The maximum and minimum in the preceding inequalities can be evaluated from the largest and smallest eigenvalues of the finite rational Hermitian Gram matrices to any desired certified accuracy, for example by real algebraic root isolation. Thus $S$ and the internal numerical precision can be chosen effectively for any target additive error.

For selfadjoint $P$, $\nu(P-tI)$ is exactly $\operatorname{dist}(t,\operatorname{spec}P)$ for real $t$. Compute it on a finite mesh of $[-M,M]$ of spacing at most $\epsilon/4$, including both endpoints, to error $\epsilon/4$. Retain those mesh points whose computed distance is at most $\epsilon/2$. Every spectral point has such a nearby mesh point, and every retained point is within $3\epsilon/4$ of the spectrum. This gives a finite Hausdorff approximation. No claim about computing exact point spectrum, kernel dimensions or convergence for a fixed ordinary start follows.

General operator-norm localization and finite-patch spectral computation have an established literature. The forward-segment cutoff, explicit error, and effective enumeration above apply directly in the intrinsic metric of this specific ordinary graph. [Sako, property A and norm localization](https://doi.org/10.1515/crelle-2012-0065) · [Hege–Moscolari–Teufel, finite-patch computation](https://doi.org/10.1090/mcom/4075)
