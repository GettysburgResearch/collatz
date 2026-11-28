# The signed periodic kernel and the negative fixed-point pole

Write \(Q=3^N\), let \(\rho_N\) be the fair ternary finite density, and consider the unfiltered positive and signed sums
\[
 S_N^+=\sum_{y>0,\ y\ {\rm odd}}\rho_N(y)^2/y^2,\qquad
 S_N^\pm=\sum_{y\in2\mathbb Z+1}\rho_N(y)^2/y^2 .
\]
There is an actual exponential term on the signed side which is entirely localized at the negative integer \(-1\). More precisely, for an absolute \(c>0\) and a finite constant \(L_-\ge1\),
\[
   S_N^+=o(N^2),\qquad
   (4/9)^N S_N^\pm=L_-^2+O(e^{-cN}),\qquad
   (4/9)^N\!\!\sum_{\substack{y\ {\rm odd}\\y\ne-1}}\rho_N(y)^2/y^2
                      =O(e^{-cN}).                                  \tag{1}
\]
The polynomial positive estimate allows arbitrary ordinary cycles. The [simple-arrival statistic](ORDINARY_COLLISION_ENERGY.md) additionally removes positive cyclic laps, and its individual increments encode the escape flux.

## Fourier and one-sided forms

Represent every residue by the unique odd \(r\in[1,2Q)\). Direct periodization gives
\[
  S_N^\pm=\frac{\pi^2}{4Q^2}\sum_r\rho_N(r)^2
                             \csc^2\!\left(\frac{\pi r}{2Q}\right),
  \qquad
  S_N^+=\frac1{4Q^2}\sum_r\rho_N(r)^2\,
                              \psi_1\!\left(\frac{r}{2Q}\right),
\]
using \(\psi_1(u)=\sum_{k\ge0}(k+u)^{-2}\). In the second formula the negative lifts are absent. In the first, the signed odd kernel has unnormalized finite Fourier transform
\[
  \sum_{y\ {\rm odd},\, y\in\mathbb Z}\frac{e^{-2\pi i\ell y/Q}}{y^2}
        =\pi^2\left(\tfrac14-\|\ell/Q\|_{\mathbb R/\mathbb Z}\right).
\]
Indeed the all-integer series is \(2\pi^2 B_2(\{\ell/Q\})\), and the even terms are \(\tfrac14\) of that series at \(2\ell/Q\). The positive half instead has transform \(\operatorname{Li}_2(e^{-2\pi i\ell/Q})-\tfrac14\operatorname{Li}_2(e^{-4\pi i\ell/Q})\). Its real part is half the signed transform. Thus passage from the signed to the positive sum requires a cancellation of exponential size.

At an ordinary positive periodic endpoint \(y\) of primitive odd period \(q\) and lap product \(\lambda_C=\prod_{u\in C}3u/(3u+1)\), the finite first-arrival correction is exact. Put \(a_n(y)=\rho_{n+1}(y)/y\) and use the simple-arrival row \(s_n\) of the companion note. For \(n\ge q\), \(s_n(y)=a_n(y)-\lambda_C a_{n-q}(y)\): the paths that have visited \(y\) before their terminal tick are exactly the full paths ending at \(y\) at tick \(n-q\), followed by its prescribed last lap. At every other endpoint or shorter duration the two rows agree. The squared first-arrival sum therefore subtracts \(2\lambda_C a_n a_{n-q}-\lambda_C^2 a_{n-q}^2\) at each such periodic endpoint. This criterion is evaluated by the path's integer states and does not become a periodic function of \(y\bmod Q\).

## Positive rows without deleting laps

The nonperiodic contribution is \(O(N)\) by the companion theorem. Start instead at \(b(x)=\rho_1(x)/x\) and follow \(n=N-1\) ticks. For a cycle \(C\) use its first-entry masses \(e_z\), first-entry date rows \(c_k(z)\le C_0e_z\), and cyclic weighted shift \(S\) from the companion proof. For initially noncyclic sources the unfiltered cyclic row is \(\sum_{j=0}^{n-1} S^j c_{n-j}\). Its total on that cycle is at most \(C_0 n d_C\); at a single site it is at most \(C_0(1+n/q)d_C\), as each potential entry site repeats at most \(1+n/q\) times in this list. Thus its squared norm divided by \(n^2\) is bounded by \(C d_C^2\) for \(n\ge1\). At each fixed finite cycle its squared norm stays bounded as \(n\to\infty\), since \(S^q=\lambda_C I\) with \(\lambda_C<1\). Dominated convergence over \(\sum_C d_C^2\le1\) gives \(o(n^2)\). The row from initially cyclic sources has uniformly bounded squared norm under the weighted permutations. The triangle inequality proves the first statement in (1).

### Quantitative interference from hypothetical long positive cycles

Write \(q\) for the primitive odd period and \(D_C\) for its total divisions, so \(\lambda_C=3^q2^{-D_C}<1\). The geometric weighted shift gives the sharper per-site bound
\[
    \|v_n(C)\|_\infty\le C d_C\min\{1+n/q,(1-\lambda_C)^{-1}\}.
\]
Indeed for each entry site, the possible winding numbers progress by full laps, each multiplying its contribution by \(\lambda_C\). The total row norm remains at most \(Cnd_C\). Thus, whenever \(|q\log3-D\log2|\gg q^{-K}\) for integers \(D\) in the near-resonant range, we get
\[
                         S_N^+=o(N^{2-1/(K+1)}).
\]
For small \(q\) the per-site amplification is \(O(q^K)\), and for large \(q\) it is at most \(1+n/q\); split at \(q=n^{1/(K+1)}\). Each fixed cycle has bounded energy, and \(\sum_Cd_C^2\le1\) supplies the little-oh after division by the stated power. The nonperiodic part is \(O(N)\). Near resonance \(D=O(q)\), and away from it the reciprocal lap defect is bounded. Bondareva–Luchin–Salikhov's cited explicit homogeneous consequence permits \(K=4.116201\); the sharper source-qualified Chudnovsky estimate permits every \(K>2\), hence every power strictly exceeding \(5/3\). [Earlier two-log source and precise exponent](../phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md) · [Chudnovsky, rational endpoint and homogeneous linear-form consequence](https://arxiv.org/abs/2610.28079)

There is also a uniform subsequence with no quantitative logarithm theorem. If \(Q_i\) are denominators of convergents of \(\log_2 3\), take \(N-1=n=Q_i^2\). For \(q<Q_i\), best approximation gives \(\|q\log_2 3\|\ge\|Q_{i-1}\log_2 3\|>1/(2Q_i)\), and for \(q\ge Q_i\) one has \(n/q\le Q_i\). Thus \(S_{1+Q_i^2}^+=o(Q_i^3)\). These bounds concern positive cyclic laps in the unfiltered trace. The removed-lap limit in the companion note already has an exact linear coefficient.

## Isolating the entire exponential contribution

Use the same affine map on negative odd integers. For a true odd orbit with total gap \(D_N=\sum e_i\), its multiplier is \(a=3^N2^{-D_N}\); the finite trace at a negative odd target is the sum of these multipliers over its true negative depth-\(N\) sources. Indeed every ternary-legal inverse gap at a negative odd integer reconstructs a negative odd integer of exactly that gap in the forward evolution. Define \(R_N(y)=(2/3)^N\rho_N(y)\). On a path ending at \(y\ne-1\) with \(y<0\), every departure has absolute value at least three, since \(-1\) is fixed. The exact derivative identity gives
\[
           (2/3)^N a/|y|
             =|x|^{-1}\prod_{u\ {\rm departing}}\frac{2|u|}{3|u|-1}
             \le (3/4)^N/|x|.
\]
For \(y>0\) the same estimate holds with \(3|u|+1\) in the denominator. For negative sources one also has \(|x|^{-1}\le a/|y|\) and \(|x|\le2^{D_N-N}|y|\) by the negative inverse formula \((2^e|u|+1)/3\le2^{e-1}|u|\). Consequently a split at \(|x|\le |y|e^{CN}\) gives, uniformly for negative \(y\),
\[
     \sum_{U^Nx=y}1/|x|\ll 1+N+\log(1+|y|).
\]
The short part is bounded by the ordinary harmonic sum. The long part is at most \(3^N|y|^{-1}\Pr(D_N>N+CN/\log2)\), with the unconstrained fair gaps; choose a fixed sufficiently large \(C\) and apply a geometric Chernoff bound. Thus \(R_N(y)/|y|\ll(3/4)^N[1+N+\log(1+|y|)]\) at all negative \(y\ne-1\).

For \(|y|\le Y=(4/3)^N\), square and sum this estimate, paying at most \(O(Y)\) roots. For \(|y|>Y\), periodicity and the Haar estimate \(E_N=Q^{-1}\sum_{r\bmod Q}\rho_N(r)^2=O(N+1)\) give
\[
 \sum_{|y|>Y,\ y\ {\rm odd}}\rho_N(y)^2/y^2
     \ll (N+1)Q/Y^2 \qquad(1\le Y\le Q).
\]
For instance in each residue the two nearest retained lifts contribute at most \(2/Y^2\), and the others \(O(1/Q^2)\). Normalization by \((4/9)^N\) turns this upper bound into \(O((N+1)(3/4)^N)\). Combining with \(S_N^+=o(N^2)\) gives the final claim of (1). [Weaver 146, equation (2a), linear Haar energy upper bound](https://rstation.ai/problems/collatz/papers/146/v1)

Finally the one-step fair recursion at \(-1\) reads exactly
\[
 R_{N+1}(-1)-R_N(-1)
     =\sum_{h\ge1}4^{-h} R_N\!\left(-\frac{2^{2h+1}+1}{3}\right).
\]
The displayed parents have magnitude \(\asymp4^h\) and are different from \(-1\). For \(h\le 2N+1\) the pointwise bound just proved gives a total \(O((N+1)^2(3/4)^N)\); for larger \(h\), use \(R_N\le2^N\) since \(\rho_N\le3^N\). The nonnegative increments are exponentially summable. Hence \(R_N(-1)\to L_-\) exponentially, with \(L_-\ge R_0(-1)=1\). Equivalently \(L_-\) is the sum over all negative odd sources that reach \(-1\) of \(2^{-k(x)}\), where \(k(x)=\sum(e_i-1)\) up to first arrival. Continuing at \(-1\) adds only letters \(e=1\), so this follows also from the increasing finite-word trace. This proves (1), and identifies the signed pole using actual integer words.

[Finite ordinary replay with exact infinite-gap sums, signed cyclic filters and clock-aligned physical lifts](check_ordinary_energy.py)
