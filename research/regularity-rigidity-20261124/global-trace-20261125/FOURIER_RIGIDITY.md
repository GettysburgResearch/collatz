# Improved Fourier cancellation and a quantitative Fourier-Stieltjes obstruction

Status: written deductions conditional on the prior source-qualified PR146/200 estimates, and on the stated predecessor-density input where indicated. No new formal verification.

## 1. Inputs and notation
Use the actual invariant binary label f on positive integers, e(t)=exp(2 pi i t), c_X its average on [1,X]. Set theta=log_2 3 modulo 1, epsilon_R=(log R)^(-1/2), g_R(t)=f(floor(R 2^t)) on the logarithmic circle, a_R=integral g_R, G_R=g_R-a_R. From PR200 MACROSCOPIC_RIGIDITY.md, conditional on PR146's written variation/absorption estimates P, use:
- adjacent variation O(R epsilon_R) on a shell [R,2R];
- ||G_R(t+theta)-G_R(t)||_1 <= C epsilon_R;
- for R=X/2^j>=sqrt X, |a_R-c_X|<=C(j epsilon_(sqrt X)+epsilon_X^(1/(kappa+1))).
Assume ||h theta||>=c h^(-kappa) for all integers h>=1, kappa>=1. Wu–Wang (2014), theorem 1, gives kappa=4.117: set the constant term to zero and use a nearest integer to h log_2 3. Their theorem bounds a linear form, not the rational approximation error itself, so the exponent here is 4.117, not 3.117.

## 2. Improved uniform cancellation
We obtain
sup_alpha |X^(-1) sum_{1<=n<=X}(f(n)-c_X)e(alpha n)|
 <= C (log X)^(-1/(2(2kappa+1))) sqrt(log log X)                  (F).

Large physical frequencies |alpha|>=sqrt(epsilon_R), represented in [-1/2,1/2], follow by Abel summation from adjacent variation, as in the previous Fourier argument. For smaller frequencies the normalized discrete shell sum centered by a_R differs from
integral_0^1 G_R(t) phi_lambda(t) dt, phi_lambda(t)=(log 2) 2^t e(lambda 2^t), lambda=R alpha,
by O(|alpha|+1/R). Real shell endpoints are immaterial.

Write epsilon=epsilon_R and choose M asymptotic to epsilon^(-2/(2kappa+1)). For nonzero m the rotation bound gives
|Ghat_R(m)| <= C epsilon / ||m theta||.
For 1<=|m|<=M the points m theta are mutually separated and separated from zero by >=c'(2M)^(-kappa). Ordering their circular distances from zero and summing j^(-2) gives
sum_{1<=|m|<=M} ||m theta||^(-2) <= C M^(2kappa).
Thus the L2 norm of the low nonzero Fourier part of G_R is <=C epsilon M^kappa. Also ||G_R||_2<=1.

If |lambda|<=M/C0 for a sufficiently large absolute C0, the Fourier coefficients of phi_lambda at |m|>M are O(1/|m|). Indeed integrate its smooth amplitude against phase lambda 2^t-mt on [0,1]; the first derivative is bounded below in magnitude by |m|/2, the second derivative is O(|m|), and the boundary contribution is O(1/|m|). Therefore its high Fourier part has L2 norm O(M^(-1/2)). Parseval and Cauchy–Schwarz bound the integral by C(epsilon M^kappa+M^(-1/2)) = O(epsilon^(1/(2kappa+1))).

For |lambda|>M/C0, let L be asymptotic to epsilon^(-2kappa/(2kappa+1)) and choose q the largest continued-fraction convergent denominator of theta at most L. Its successor exceeds L, so the approximation bound and the Diophantine lower bound give q>=c L^(1/kappa). The first q rotation points have pairwise circular separation >=1/(2q), by the best-approximation inequality for the preceding convergent. Average phi_lambda over these q rotations; replacement in the integral costs O(q epsilon).

For two translates with indices i != j, split at their wrap points (at most three intervals) and substitute y=2^t. The resulting phase is linear with frequency lambda(u_i-u_j), u_l=2^({l theta}-b_l) and b_l in {0,1}. The amplitude and its variation are uniformly bounded, u_l in [1/2,2], and |u_i-u_j| >= c ||(i-j)theta||. Integration by parts bounds the cross inner product by C/(|lambda| ||(i-j)theta||). By the q-point separation, for every i the sum over j != i of the reciprocal circular distances is O(q log(2q)). The square norm of the translate average is at most
C(1/q + log(2q)/|lambda|).
By Cauchy–Schwarz the integral is O(q epsilon + q^(-1/2) + sqrt(log(2q)/|lambda|)), which is O(epsilon^(1/(2kappa+1)) sqrt(log(2/epsilon))) by the choices of q,L,M.

Both frequency ranges, including the discrete approximation errors, give the same bound. Summing full dyadic shells R=X/2^j>=sqrt X, replacing their means by c_X with the pinned mean comparison, and dropping the initial O(sqrt X) points proves (F). Numerically the log exponent is >0.054 for kappa=4.117, in place of the earlier 1/[16 kappa(kappa+1)]. The argument uses ordinary labels, not an independence assumption about deterministic T-edges.

## 3. Fejer norm and approximate representation lower bounds
Apply (F) to the actual nonconvergence indicator b, extended evenly to negative integers and by b(0)=0. Conditional additionally on input I of TRACE_ONSET.md (positive fixed-root predecessor density suffices), if Collatz fails then c_X stays in [eta,1-eta] for some eta>0 and all large X. This follows by taking predecessors of 1 and of one fixed bad odd unit.

Let
K_N(t)=sum_{|n|<N}(1-|n|/N)b(|n|)e(nt),
the same Fejer polynomial used by PR193. Put P_X(t)=X^(-1) sum_{n=1}^X(b(n)-c_X)e(-nt).
Writing delta_X=(log X)^(-1/(2(2kappa+1))) sqrt(log log X), we have ||P_X||_infty<=C delta_X. For N>=2X,
integral K_N P_X = X^(-1) sum_{n=1}^X (1-n/N)b(n)(1-c_X) >= c_X(1-c_X)/2.
Therefore for every sufficiently large N, choosing X=floor(N/2), a counterexample forces
||K_N||_1 >= c_eta (log N)^(1/(2(2kappa+1))) / sqrt(log log N).   (G)

A stronger representation formulation: if a finite complex measure mu satisfies |muhat(n)-b(n)|<=eta(1-eta)/2 for 1<=n<=X, then pairing with P_X gives ||mu||_TV >= c_eta/delta_X. Indeed the error in the pairing is at most the uniform coefficient error, and the exact main term is c_X(1-c_X). Use consistent Fourier-transform signs for mu and the test. Thus the obstruction does not depend on a particular approximation kernel. In particular a subcritical upper bound on ||K_N||_1 along ANY unbounded sequence of cutoffs would prove full convergence, conditional on P and the density input. No such upper bound is supplied. This extends PR193's qualitative bounded-norm criterion, not its idempotent theorem proof.

## 4. Independent obstruction from whole-interval synchronization
Conditional on PR146 WHOLE_INTERVAL_SYNCHRONIZATION.md, both colors of a nonconstant actual convergence label occupy arbitrarily long consecutive intervals arbitrarily far out. For the bad color choose a fixed bad odd unit q and synchronize to q; for the good color use 1. The paired construction is more than is needed here.

If both colors are thick in this sense, construct positive a_i,b_j recursively with b(a_i+b_j)=1 iff i<=j: after choosing a_1,...,a_j, use a sufficiently long distant 1-interval to fit their translates by a new b_j; then use a sufficiently long distant 0-interval to fit b_1,...,b_j translated by a new a_(j+1). Thus no weakly almost periodic extension to Z can have these positive coefficients, by the double-limit criterion.

There is also a direct quantitative finite proof avoiding the idempotent theorem and predecessor-density input. For any m take the corresponding m by m array, and let H_ij=1/(j-i) for i!=j, H_ii=0. This matrix has l2 operator norm <=pi: extend vectors by zero to Z and use the Fourier multiplier of the discrete Hilbert transform, the bounded sawtooth with coefficients 1/k (sign is immaterial). For all t, the two character vectors (e(t a_i)) and (e(t b_j)) have Euclidean norm sqrt(m). Hence the test Q(t)=sum_ij H_ij e(-t(a_i+b_j)) has sup norm <=pi m. Take N>=2 max_ij(a_i+b_j). Its pairing with K_N is at least
(1/2) sum_{i<j} 1/(j-i) = (m H_(m-1)-(m-1))/2.
The lower triangle is zero. Thus ||K_N||_1>= (H_(m-1)-1)/(2pi) for every such N. Sending m to infinity proves divergence of the norm for a nontrivial basin using only thickness. It is quantitative in the order of the witnessed triangular array; there is no useful bound on the array size at a specified cutoff here. (G) is the distinct quantitative-in-N result.
