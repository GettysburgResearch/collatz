# Independent review of the endpoint telescoping estimate

Reviewer: `/root/five_transport`. Date: 2026-11-21 (Asia/Jerusalem).

**Scope:** ES3–ES4 of `FIXED_ENDPOINT_SUMMABILITY.md`, SHA256
`cbd8e00d73c0da06a063e7334a96ab27145a58ffcc3bd56604a3c8370d8663bd`.
The primitive-word definitions and the definition of PC were read in
`MOMENT_QUANTILES.md` as supporting notation. This is an independent
reconstruction by a reviewer who did not participate in deriving ES3–ES4.

**Verdict: VERIFIED for ES3–ES4 at the frozen file hash.** No mathematical
repair is required. The sharp per-source constant, infinite positive
summation, primitive sub-sum, moving-cutoff estimates and equivalence
with the restricted PC tail all hold with their stated scope. The open
PC estimate itself is not proved.

## Per-source identity and sharp constant

For the actual odd step from n_q to n_(q+1), with exponent a_q,

\[
 \frac{J_{q+1}}{n_{q+1}}
 =\frac{J_q}{n_q}\frac{3n_q}{3n_q+1}.
\]

This directly gives the claimed identity for
V_q=(J_q/n_q)^4. It also reconstructs
V_q=1/(n_0^4 I_q^4) without any boundedness assumption on I_q.

I independently expanded the cleared numerator of

\[
 1-(3t/(3t+1))^4-175/(256t).
\]

After multiplication by the positive denominator 256t(3t+1)^4, its
coefficients in increasing powers of t are

\[
 (-175,-1844,-6378,-5076,13473).
\]

They equal the expansion of
(t-1)(13473t^3+8397t^2+2019t+175). Hence the claimed lower bound holds
for every integer t>=1, with equality at t=1. For the fixed point 1,
J_q=(3/4)^q, and the geometric sum is exactly 256/175. This proves
sharpness in the stated per-source inequality, rather than merely
sharpness of an auxiliary estimate.

For every finite time cutoff the sum of V_q-V_(q+1) is at most
V_0=n_0^-4, because V_q is nonnegative. Monotone convergence of the
nonnegative summands therefore gives ES3(7). The proof requires no
termination, no exclusion of nontrivial cycles, and no assumption that
an infinite Jacobian product has a positive or zero limit.

## Infinite source sum and primitive injection

The primitive endpoint r_w and source b_w satisfy the exact full word
identity. I reconstructed the reverse divisibility argument: the full
3^q divisibility successively forces each inverse step to be integral;
positive exponents make every intermediate odd. A negative starting
integer would remain negative under all these actual odd steps and
could not end at positive r_w. Thus b_w is a positive ordinary source
with exactly word w.

At each fixed q, distinct words have distinct b_w, since an ordinary
source has a unique first q sequence of maximal valuations. This is
exactly the injection needed. No injection across different q is
required or claimed. The same original source may be counted at several
times, and ES3(7) already pays all of those contributions.

Consequently Tonelli permits summing the per-source estimate over all
positive odd sources and then retaining the primitive sub-sum. This
proves ES3(8). For r_w<=R, multiplying each fifth-power-weight term by
r_w^3<=R^3 proves ES3(9). All relevant series have nonnegative terms;
there is no cancellation or subtraction of infinite sums.

## Growing cutoffs and the PC equivalence

At one fixed q, the exact product identity gives

\[
 J_w^4/r_w^2=r_w^2/(b_w^4 I_w^4)\le R^2/b_w^4
 \quad(r_w\le R).
\]

Summing the fixed-q injection proves ES4(10). This bound uses only
I_w>=1, which holds equally on periodic and nonperiodic paths.

For r_w<=q^beta, the inequality r_w^3<=q^(3beta) gives ES4(11)
term by term from the unconditional fifth-power sum. The positive tail
splitting argument printed in the note correctly proves ES4(12) for
beta>0. At beta=0 it instead yields finite total mass, as explicitly
stated. For beta<=1/3, q^-1<=q^(-3beta), so the claimed harmonic-time
summability and vanishing Cesaro mean follow.

For beta<20/19, the exponent comparison
1+2beta<59/19 is correct. In particular the entire region r_w<=q
has a cumulative contribution o(N^3), and hence o(N^(59/19)).
Its fixed-time contribution is also at most C_4 q^2=o(q^(40/19)),
as claimed for the older pointwise premise.

At every finite cutoff N, the full PC numerator is exactly the sum of
the retained r_w>q part and the omitted r_w<=q part. The latter,
divided by N^(59/19), tends to zero and is nonnegative. Therefore the
two normalized sequences have the same liminf, including if that
liminf is infinite. This proves the equivalence in ES4(13), while
leaving its value unproved.

## Executed verification and limits

I checked the requested source SHA before reviewing. A separate Python
calculation, importing none of the submitted research checkers, verified
the polynomial factorization by multiplying integer coefficient lists,
verified the sharp constant by exact fractions, and checked 210 exact
instances of the ratio identity on seven ordinary sources (including 1).
The calculation completed successfully.

These finite instances are ancillary checks. The review's conclusions
about all times, all sources and all words rest on the reconstructed
identities and positive-series arguments above. This review does not
establish PC, exclude nontrivial cycles, prove full Collatz, or claim
proof-assistant verification.
