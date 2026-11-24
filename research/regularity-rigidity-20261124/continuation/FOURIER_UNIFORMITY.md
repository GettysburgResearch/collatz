# Uniform additive Fourier cancellation for invariant labels

**PROPOSED written proof using the same source-qualified P as MACROSCOPIC_RIGIDITY.md.** This is a separate global spectral obstruction; it applies to the actual basin label on ordinary integers, not to a sampled orbit.

Use f, g_R, a_R, c_X, theta, kappa, epsilon_R, delta_R from MACROSCOPIC_RIGIDITY.md. Put e(u)=exp(2 pi i u). Then for an effective absolute c>0,

    sup_(alpha in R/Z) |(1/X) sum_(n<=X) (f(n)-c_X)e(alpha n)|
        = O((log X)^(-c)).                       (FOU)

One may take c=1/[16 kappa(kappa+1)] with the fixed Diophantine input of that document (no optimization).

## 1. Large physical frequencies

On a shell [R,2R), adjacent variation is O(R epsilon_R) by P. The partial sums of e(alpha n) are bounded by C/|alpha| when alpha is represented in [-1/2,1/2] and alpha!=0. Abel summation gives normalized bound O(epsilon_R/|alpha|+1/(R|alpha|)) for the centered shell label f-a_R. Thus |alpha|>=epsilon_R^(1/2) is harmless, with bound O(epsilon_R^(1/2)).

For the remaining alpha, replace the discrete sum by its real integral over the unit cells. The normalized error is O(|alpha|+1/R), since the phase changes by O(|alpha|) across a unit cell. With lambda=alpha R, the normalized integral is

    integral_0^1 (g_R(t)-a_R) phi_lambda(t) dt,
    phi_lambda(t)=(log 2) 2^t e(lambda 2^t).

## 2. Small scaled frequencies

The uniform primitive discrepancy on the circle is O(delta_R), and the sup norm plus total variation of phi_lambda is O(1+|lambda|). Integration by parts therefore gives O(delta_R(1+|lambda|)).

Put A=1/[2(kappa+1)]. For |lambda|<=epsilon_R^(-A) this gives O(epsilon_R^A), because delta_R=O(epsilon_R^(1/(kappa+1))).

## 3. Large scaled frequencies: oscillation under the rotation

Let q>=1. By approximate rotation invariance (1), replacing the test by the average of its first q translates phi_lambda(t+i theta mod1) costs O(q epsilon_R). Apply Cauchy-Schwarz to the integral against g_R-a_R (L2 norm <=1).

For distinct i,j<q, split t in [0,1] at the at most two wrapping points of their fractional rotations. On each resulting interval, the translated test has form

    (log 2) u_i 2^t e(lambda u_i 2^t),

where u_i=2^({i theta}-b_i), b_i either 0 or 1 on that interval, and likewise for j. Both u values lie in [1/2,2]. By the mean value theorem and the irrationality measure,

    |u_i-u_j| >= c' ||(i-j)theta|| >= c'' q^(-kappa).

In the inner product of these translates change variables y=2^t. The amplitude and its total variation are O(1), and the phase is linear with frequency lambda(u_i-u_j). Integration by parts on each of the at most three pieces gives absolute inner product O(q^kappa/|lambda|). The diagonal inner products are bounded by a constant. The L2 norm squared of the translate average is therefore O(1/q + q^kappa/|lambda|). The original integral is bounded by

    C(q epsilon_R + q^(-1/2) + q^(kappa/2)/sqrt(|lambda|)).

For |lambda|>=epsilon_R^(-A), take q comparable to epsilon_R^(-A/(2 kappa)). The three terms tend to zero at power rates; the slowest is O(epsilon_R^(A/(4 kappa))). Together with Sections 1 and 2, this gives the claimed shell bound with c=A/(8 kappa).

## 4. Full cutoff and the Gowers consequence

Sum complete dyadic shells with R=X/2^j down to sqrt X and use the bound on |a_R-c_X| established in MACROSCOPIC_RIGIDITY: it is <= C(j epsilon_(sqrt X)+delta_X). Shell weights form a geometric series, and the omitted prefix contributes O(sqrt X/X). All bounds are uniform in the same alpha. This proves (FOU).

In particular view n=1,...,X as the cyclic group Z/XZ and set F=f-c_X. With normalized discrete Fourier transform, Parseval and the standard finite U2 identity yield

    ||F||_(U^2)^4 = sum_xi |Fhat(xi)|^4
                  <= max_xi |Fhat(xi)|^2 sum_xi |Fhat(xi)|^2
                  = O((log X)^(-2c)).

This is a genuine two-variable additive-uniformity statement about invariant ordinary labels. It does not imply that the deterministic pair (n,Tn) has independently colored endpoints. That pair is supported on a one-dimensional affine graph and is not controlled by U2 uniformity. It also does not contradict arbitrarily long, but relatively short, monochromatic intervals from PR146/200.

Under the separately source-qualified input M (positive lower natural predecessor densities), a nontrivial basin f has variance c_X(1-c_X) bounded below. Equation (FOU) then rules out approximating its centered label in normalized mean square with o((log X)^(2c)) Fourier modes on Z/XZ: any such approximation lies in their span, whose orthogonal projection of F has squared norm <= number_of_modes * max |Fhat|^2=o(1). More generally a bounded coefficient-l1 trigonometric predictor cannot correlate nontrivially with F if its coefficient l1 norm is o((log X)^c).

This supplies a second quantitative complexity obstruction complementary to the digit automata theorem, but no sparse Fourier approximation to the actual label has been constructed. The universal closing step remains open.