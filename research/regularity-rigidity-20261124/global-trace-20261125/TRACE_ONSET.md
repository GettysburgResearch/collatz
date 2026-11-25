# Quantitative obstruction to early ordinary trace convergence

Status: new written deductions, conditional on the explicitly identified published/preprint inputs; not a proof of Collatz. No new compiler check.

Use the accelerated odd map U(a)=(3a+1)/2^v2(3a+1). Let rho_k be the mean-one cylinder density modulo 3^k for the original Syracuse law, rho_0=1. At a positive odd integer a the exact inverse-word formula is
rho_k(a)=sum_{U^k(x)=a} 3^k/2^{D_k(x)}.
Set A_K(a)=(1/K)sum_{k=1}^K rho_k(a). These are arithmetic values, not samples along a typical 3-adic trajectory.

## Inputs
I: Weaver, rStation paper 12, v1, §§7–9, Corollary 5 and Known Theorem 6 (credit there to Valbuena, Theorems 8,14,16). The reciprocal predecessor floor d_a >= c/a holds for positive odd ternary units. Here d_a is relative odd natural predecessor density. The canonical integer Cesaro trace is
h(a)=lim_K A_K(a)=c_* a beta_a/(1-lambda_a), c_*=log(4/3)/2,
with c_0 d_a <= beta_a <= d_a, absolute c_0>0, lambda_a=0 for a nonperiodic root, and otherwise lambda_a the product of 3z/(3z+1) over its odd cycle. The cited result also bounds the total inverse weight at each FIRST-hit odd depth by C a d_a, uniformly in the root and depth (including periodic roots). All constants are absolute. We retain the source's analytic dependencies; no Lean artifact of the source has been rebuilt.

II: Weaver, rStation paper 146, v1, theorem (1) and corollary (2a), 14 November 2026: for the Haar density rho, m_3{rho>t} <= C/t^2 for large t and integral rho_k^2 <= C(k+1). The finite densities are conditional expectations. Only the upper bounds are needed.

## 1. Escaping ray forces a second-moment spike in every octave
Suppose the odd orbit a_i=U^i(a_0) is nonrepeating; discard a possible nonunit initial state. Its values tend to infinity because they are distinct positive integers. Its predecessor sets are nested along the ray; hence d_{a_i} >= d_{a_0}>0. Each a_i is nonperiodic, so input I gives h(a_i) >= c(a_0) a_i.

For EVERY sufficiently large integer X there is an a_i in [X,2X): take the first crossing of X. Since U(v) <= (3v+1)/2 <2v for odd v>1, and the preceding state was below X, the crossing lies in that octave. Thus
(1/X) sum_{X<=a<2X, a odd, 3∤a} h(a)^2 >= c(a_0)^2 X.             (1)

In contrast, for 1<=K<=floor(log_3 X),
(1/X) sum_{X<=a<2X, a odd, 3∤a} A_K(a)^2 <= C(K+1).             (2)
Indeed, each residue class modulo 3^k occurs in the interval at most X/3^k+1 times. For k<=K this is at most 2X/3^k. Dropping the odd and unit restriction increases the sum of nonnegative terms. Apply input II to the complete period of rho_k, then Jensen to the finite average. The same bound holds for any convex mixture of depths 0..K with K+1 on the right.

By the triangle inequality in the finite weighted Euclidean norm, (1) and (2) imply
||(h-A_K)|_[X,2X)∩odd units||_(2,X) >= c(a_0) sqrt(X) - C sqrt(K+1),
where ||v||_(2,X)^2 = X^(-1) sum v(a)^2. In particular this gap is of order at least sqrt(X), uniformly at all logarithmically bounded depths above. The source's Haar L^p convergence cannot simply be interchanged with the ordinary Cesaro limit on moving integers.

An explicit sufficient ESCAPE-EXCLUSION criterion is
liminf_{X→∞} X^(-2) sum_{X<=a<2X, a odd unit} h(a)^2=0.           (3)
It would exclude every nonrepeating positive odd orbit, not just almost every one. Equivalently one may prove o(X) for the normalized second moment along one unbounded sequence of octaves. A sufficient stronger estimate is ||h-A_K||_(2,X)=o(sqrt(X)) along such a sequence with K<=floor(log_3 X). None of these estimates is proved here.

The analogous argument for fixed 1<r<2 uses the Haar L^r bound from II and gives an early norm O_r(1), whereas the limiting ordinary norm is at least c(a_0) X^(1-1/r). This supplies other possible trace-transfer targets.

## 2. Single integer onset and a stronger elementary depth barrier
Input II and layer cake give rho_k(a) <= C 3^(k/2) uniformly in the residue: on a cylinder of Haar mass m, integrate min(m,C/t^2) to get integral <= C' sqrt(m), and divide by m. Thus A_K(a) <= C 3^(K/2)/K for K>=1. On the same escaping ray, any K at which A_K(a_i)>=eta h(a_i), for fixed eta>0, must satisfy
K >= 2 log_3 a_i + 2 log_3 log a_i - O_(a_0,eta)(1).
The log-log term follows by first deducing K>=2 log_3 a_i-O(1), then substituting into the original inequality.

There is also a simple, stronger exponential-scale bound (not claimed as a new result on the maximal cylinder density). For fixed total division exponent D of a word of length k, set M=3^k/2^D and B=sum_{j<=k}3^(j-1)/2^{D_j}. Then 0<=B<=(3/2)^k-1, M<=(3/2)^k. The integer carry 2^D B uniquely identifies the word given D and k: for k>=2 subtract 3^(k-1) and recover the last exponent as the 2-adic valuation, then recurse; k=1 is determined by D. Within any residue modulo 3^k these carries differ by multiples of 3^k. Consequently the total weight of the fibre for one D is bounded by M+((3/2)^k-1) <=2(3/2)^k. There are O(k) choices D<=8k. The remaining weight is bounded by 3^k P(D_k>8k) <= [6(3/4)^8]^k via the geometric law moment E[(4/3)^e]=2. Thus rho_k(a)<=C(k+1)(3/2)^k and A_K(a)<=C'(3/2)^K. On an escaping ray a constant fraction of the trace cannot appear before log_(3/2)(a_i)-O_(a_0,eta)(1). This sharper estimate does not use II. The missing issue is controlling the later depths, not bounding early depths more tightly.

## 3. Periodic targets have an even slower onset
Suppose a is periodic of primitive odd period p. Write L_j(a) for the sum of weights of odd starts whose FIRST hit of a is at depth j. By I, L_j(a)<=C a d_a for every j>=0. Each subsequent visit to a adds p to the depth and multiplies the weight by lambda_a. Therefore, exactly,
rho_k(a)=sum_{0<=l<=floor(k/p)} lambda_a^l L_{k-lp}(a).
In particular rho_k(a)<=C a d_a(1+k/p). The canonical formula in I gives h(a)>=c' a d_a/(1-lambda_a), so
rho_k(a)/h(a) <= C'(1-lambda_a)(1+k/p).
The same bound with K holds for A_K(a)/h(a).

At the minimum s of this cycle, 1-lambda_a <= sum_{z on cycle}1/(3z+1) <= p/(3s). Hence
A_K(a)/h(a) <= C''(p+K)/s.                                     (4)
This holds at ALL phases of the cycle. For the bounded least-bad-cycle branch in PR192/205 one has p=O(s^.49), so any fixed-fraction onset needs K=Omega(s), not merely logarithmic depth. A uniform sublinear-onset theorem for large positive ordinary roots would exclude sufficiently large cycles in that branch, and a logarithmic upper onset strictly below the barrier of §2 would exclude escape. No such uniform estimate follows from fixed-root convergence.

Also by I, every odd phase has h(a)>=c/(1-lambda_a)>=c's/p. The p phases of the bounded branch lie in [s,6s] by PR192. For each r>1 they contribute
(1/s) sum_{s<=a<=6s, a odd unit} h(a)^r >= c_r (s/p)^(r-1).
Uniform bounded ordinary r-moments on these larger shells would thus exclude arbitrarily large cycles of that branch (not a single finite remaining cycle without an effective estimate).

## 4. Why the latest regularity theorem is insufficient
II concerns Haar averages and a fixed truncation depth. The arithmetic limits of I are taken with the target held fixed, before the root is allowed to move. (1)–(4) quantify the possible noncommutation. Neither replacing h by rho almost everywhere, nor selecting a favorable residue and declaring it an ordinary root, gives the missing transfer. The route requires a uniform estimate on actual integer traces or their onset, plus a complete ordinary cycle exclusion. The rational models in the companion note warn against obtaining that exclusion from local descent alone.
