# Odd-time occupation measures and a sharp singular-mass obstruction

**PROPOSED**, reconstructed 2026-10-30. Proof text is not a formal proof build or independent review.

## Definitions

Let `X=1+2 Z_2`, with normalized Haar probability `m`. Put `a(x)=v_2(3x+1)` and `U(x)=(3x+1)/2^a(x)` except at `p=-1/3`. Set `a(p)=infinity` and extend `U(p)=1` for measurability. Positive ordinary orbits never meet p. For such an orbit `n_j=U^j(n_0)`, define `mu_N=N^(-1) sum_{j=0}^{N-1} delta_{n_j}`. Time here is the number of odd-to-odd steps, not shortcut time, logarithmic time, or a weighted occupation clock.

## O1. Occupation cost and invariance

If `n_j -> infinity`, every weak subsequential limit `mu` of `mu_N` satisfies

`U_*mu=mu`, `mu({p})=0`, and `integral a dmu <= c=log_2(3)`.

More generally, if all `n_j >= M > 1`, replace c by `d_M=log_2(3+1/M)<2`.

Proof. The exact real identity is

`sum_{j<N} a(n_j) = N log_2(3) + sum_{j<N} log_2(1+1/(3n_j)) + log_2(n_0/n_N)`.

For an escaping orbit the middle average tends to zero and the last term is bounded above by `log_2(n_0)/N`. Under the floor condition the middle summands are at most `log_2(1+1/(3M))`, and the endpoint term is at most `log_2(n_0/M)/N`. Thus the respective limsup average costs are at most c and d_M.

For every integer R, `a_R=min(a,R)` is continuous on compact X, including at p. Weak convergence followed by monotone convergence gives the cost bound. Since `a_R(p)=R`, it also gives `mu({p})=0`. For continuous bounded f, `f composed with U` is bounded and continuous except possibly at p. Its integrals therefore converge along this weak subsequence. The empirical invariance defect is exactly `(f(n_N)-f(n_0))/N`, which tends to zero. Hence mu is U-invariant. Compactness supplies weak subsequences. No uniform integrability of the unbounded a was assumed.

## O2. The absolutely continuous invariant part is Haar

The inverse branch `phi_b(y)=(2^b y-1)/3`, b>=1, maps X bijectively to `{a=b}` and scales m by `2^(-b)`. A valuation word `(b_0,...,b_{k-1})` is one odd residue class modulo `2^(1+sum b_i)` of m-mass `2^(-sum b_i)`. The diameters of nested cylinders tend to zero. Outside the countable backward orbit of p, this identifies `(X,m,U)` with the one-sided independent shift with probabilities `P(b)=2^(-b)`. In particular m is invariant and ergodic, and `integral a dm=2`.

Both images and inverse images of m-null sets under U are m-null: check each affine branch and the exceptional singleton. Therefore if an invariant finite measure has Lebesgue decomposition `mu=mu_ac+mu_s`, both summands are invariant (uniqueness of the decomposition). Every invariant finite measure absolutely continuous with respect to ergodic m is a constant multiple of m. One proof applies the m-ergodic theorem to indicators, transfers the almost-everywhere limit by absolute continuity, and integrates using invariance. Thus

`mu=(1-s)m+nu`, where `nu` is singular, invariant, and has mass s.

## O3. The mass bound and its exact boundary

Since a>=1 and its Haar mean is 2,

`integral a dmu >= 2(1-s)+s=2-s`.

O1 implies `s>=2-log_2(3)` for an escaping positive orbit, and `s>=2-log_2(3+1/M)` for an orbit remaining above M>1. This does not exclude either kind of orbit.

For every 1<d<2 the invariant measure

`mu_d=(d-1)m+(2-d)delta_{-1}`

has mean cost exactly d and singular mass exactly `2-d`, because `U(-1)=-1` and `a(-1)=1`. Consequently stationarity plus `integral a<=d` cannot imply a larger universal singular-mass bound. This is a 2-adic countermodel, not an ordinary positive counterexample or a claim that an escaping ordinary orbit has this limit.

## Fixed-source obligation

A contradiction would follow from a theorem forcing one occupation limit of every putative escaping positive orbit to have singular mass strictly below `2-log_2(3)`. No such arithmetic regularity theorem is proved here. For a full Collatz conclusion, nontrivial positive cycles must also be handled; the fixed-floor form covers them conditionally but does not exclude them.

## Provenance and external foundations

The inverse-branch argument is provided above rather than imported without proof. Its classical context is Bernstein and Lagarias, *The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics 48 (1996), 1154-1169, introduction and equations (1.1)-(1.6): https://websites.umich.edu/~lagarias/doc/bernstein.pdf . The first page was visually checked in this pass.

Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Section 1.2, Definition 1.7 and Proposition 1.9, uses the geometric valuation law for appropriately distributed sources, not as an unconditional law for a fixed orbit: https://arxiv.org/html/1909.03562 . This packet makes no such transfer.
