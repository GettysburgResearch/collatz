# Coordinating mathematical reconstruction

23 November 2026. **Disposition: the four new written results are valid
within the scopes recorded below; none supplies global closure.** This is
internal agent review. It is not external peer review or Lean certification.

## Frozen proof boundary

| Proof | SHA256 |
|---|---|
| `FINITE_GAP_ONE_INSERTIONS.md` | `2501d3a849aca8582d8a1f623c85e668fedee90058dc1fe80df39c02855f39ab` |
| `ACTUAL_ALL_GAP_COLLISIONS.md` | `82b0bf20b7a315e0102692eddae3058f84d8ec74a983be057669c0b55f795caa` |
| `GENERIC_RAY_CONSTRUCTION.md` | `a6189cb6e635c234bab815fb26370763bc3c30f3a1e4acfc2a9369819a5c1e14` |
| `PAIRED_TENSOR_CLOSURE_ATTEMPT.md` | `b828c5c0155c3baa3377c1d56f7c284602762b2dec149cff772bba8b1a42016e` |

The coordinator wrote the generic-ray proof. Its independent reconstruction
is therefore the separate `GENERIC_RAY_REVIEW.md`, not this report. The
coordinator suggested the insertion question and the `n=3` boundary check,
then independently reconstructed the construction agent's complete bound.
The collision and tensor proofs were independently written by their lane
agents and read in full here. `REVIEW_ALL_GAP.md` supplies another independent
reconstruction of the collision theorem. These contribution boundaries are
disclosed rather than labeling every review independent of every author.

## 1. Finite insertion surgery

The inverse source formula is a telescoping identity. Inserting cuts from
left to right means the suffix at the next cut is still the original suffix.
The previous inverse prefix has slope
`2^(A_i+ell-1)/3^(i+ell-1)`. The additional inverse gap changes its input by
`-(q_i+1)/3`, giving exactly the displayed summand. Repeated cuts work the
same way. The formula neither requires nor implies that the partially edited
source is integral.

Each cut cost exceeds `n/3`, so the geometric sum gives
`m<(2/3)^t n`. Positive integrality yields `3^t<2^t n`, then
`2^t<n^2` by squaring and using `8^t<9^t`. These inequalities preserve their
strictness. A positive integral inverse source makes every intermediate
suffix integral: its denominator is simultaneously a power of two and an
odd power of three, and its inverse representation has odd numerator.
Thus the prescribed gaps are exact valuations, not just allowed divisions.

The aligned difference is the decisive invariant. All states in a successful
repair are positive odd integers. A common gap multiplies the difference
by `3/2^a`; an inserted one subtracts `(z+1)/2`. If the difference ever
became negative, it could not recover. If it became zero with an insertion
still ahead, that insertion would make it negative. Hence it is positive
until the last insertion and zero thereafter. This does not assert that
the two trajectories have no coincident states at some other alignment.

Across a common block, its positive even endpoint difference proves
`2^(B+1)|D_start`. On the other hand, common gaps increase the difference
by at most `3/2` and insertions decrease it. Thus
`D_start<2^(N+A_prev)`, giving the integral bound
`B<=N+A_prev-2`. Induction proves
`A_ell<=(N-2)(2^ell-1)`. Together with `t<2N` this gives the claimed
`N(n^2+2)` enlarged shortcut clock. The sharper real bound follows by
retaining `log_2(3/2)` and the actual initial difference.

The universal assertion includes zero-length common blocks and repeated
cuts. It is conditional on a successful positive integral same-endpoint
repair and does not bound deletions or replacements. At `n=3`, the first
gap of every proposed enlarged word is one, whereas the only smaller
positive odd source, one, has exact first gap two. This correctly rejects
a universal repair assertion for all positive sources. The existence
question at a least escaping source is still an unproved, stronger input.

## 2. Actual entropy and all-gap collisions

For the finite word laws, each offset `k`-block marginal of an `m`-block
sample is a sub-sample of the full `N-k` word positions of exactly
`N-m` positions. Entropy concavity gives the factor `(N-k)/(N-m)`.
Covering the `m` coordinates by `ceil(m/k)` such blocks, allowing overlap
of the last block, proves the stated sliding inequality. No independence
or asymptotic growing-block approximation is used.

Distinct ordinary endpoints below `3^m` have distinct `m`-gap words:
the complete carry fixes the endpoint modulo `3^m`. Conditional on those
`K` endpoints, the word law is uniform on `K` atoms. This yields
`K log K<=(N-m)H_(N,m)`. Choosing `m=floor(B log_3 N)+1` and passing
to a subsequence realizing the occupation limsup proves the new bound
using only the stated convergence at a fixed `k`. The first `m` clocks
have vanishing density. The argument also handles `H_k=0`.

For a gap anchor, `D=2^A-3^d` is odd and prime to three. Its reduction
factor is therefore a unit at two and three. The exact affine identity
forces that factor to divide the endpoint difference, and gives the
two displayed valuation identities. The extra factor two in
`2^(A+1)3^m` comes from the difference of two odd endpoints. All signs
are retained when the anchor is negative; the height bound uses the
absolute value of its numerator. The exact CRT cylinder needs the final
oddness bit, hence modulus `2^(A+1)`, not merely `2^A`.

Grouping word atoms by endpoint residue increases collision mass. Combining
this with the entropy bound at `m=floor(log N/Phi)` gives at least
`cN^(1+beta)` ordered pairs under a strict finite Shannon deficit.
There are at most `N(2L+1)` pairs at lag at most `L`, including the
diagonal. Subtracting them proves the long-gap conclusion. The statement
does not infer word equality from endpoint collision.

The source-qualified stationary extraction is not newly re-proved here.
The finite statements are unconditional for the supplied injective
segment, and the asymptotic occupation and location statements clearly
name their fixed-block entropy input. Their conclusions allow escape.
The diagonal and fixed-resolution-then-limit upper-bound targets are
different, and the note does not interchange those limits.

## 3. Infinite generic rays

The independent review records the full argument. The key distinction is
between a law that is stationary and a selected sequence having its finite
empirical statistics. Zero-density insertions preserve every finite word
frequency; the mean requires the separate exact gap-sum identity because
the alphabet is unbounded. The running regulator is `o(n)` by uniform
sublinearity of a zero-mean input sum, but it changes the pressure's
one-sided behavior at every clock.

The positive branch's real finite series is `sum chi_j^-1`. The stationary
reversed-gap series is `sum chi_j`, which diverges on this positive branch.
The negative branch makes the latter finite and has a strict maximum,
not a minimum, at the origin. These are separate conclusions.

The image law is proved nonatomic by a subsequence-count union bound.
Injectivity of the 2-adic gap code then excludes every rational source
almost surely by countability. No rational-periodicity conjecture and no
false identity between the real and 2-adic values is used. Every finite
prefix has positive ordinary realizers, but they cannot stabilize to one
ordinary integer for an irrational full code.

## 4. Paired complete-denominator cycles

Multiplying the two complementary affine recurrences gives
`4P_next=3P+(1-e)x+e y`. The full-word product closure is exactly
`2^A Y f+2^A X g-fg`, where `f,g` are the scalar residuals. Replacing
`X',Y'` by `X-f/2^A,Y-g/2^A` also proves the polynomial-moment ideal
statement directly. This concerns equality constraints, not all possible
inequalities on integral points.

The centered product sum `sum (2x_i-1)(2y_i-1)=3A` follows by summing
the product recurrence and the two scalar recurrences. The gcd identity
uses `T=2^A D+3^p E` and its symmetric version, with powers of three
coprime to the scalar denominators. These are identities for all full
words, so they cannot be counted as additional independent divisibilities.

For the one-rise word, exact reduction gives
`q=(2^(p+b)-3^b)/gcd(3^b-2^b,2^p-1)`. Positivity of the original
denominator and `p>b` yield `q>3^(p-b)-1`. In the retained arbitrary-floor
family, the elementary period-to-excess bound implies both refreshed
linear lower bounds on `q`. Nonintegrality of the original source follows
from its exact `v_2(x+1)=p` and the simultaneous bound `x<4H<2^p-1`.
Thus the controls genuinely satisfy the complete complementary bounds
while failing the original integer condition. They do not refute an
argument that actually uses that missing condition.

The arbitrary-floor family is credited to checkpoint 17; the new result is
its complete complementary denominator and the combined tensor test.
The finite examples check every literal parity step; their sizes do not
constitute a proof of the arbitrary-floor assertion.

## 5. Execution scope and remaining uncertainty

All new finite checkers use explicit exceptions, including under `python -O`,
and emit stdout without changing adjacent input files. Two authors initially
used Python assertions; coordinating review required explicit checks before
the final normal/optimized runs. The final records bind the corrected
checkers, not the earlier development versions.

The integrated replay compares normal and optimized outputs with the frozen
results and checks the source-content pins available in the checkout. One
PR183 entry was metadata-only and unavailable as a local object; it is
explicitly excluded from content verification and is not a proof ingredient.
No historical Lean or large census suite is replayed. No new Lean
formalization is claimed.

The two substantial positive statements are the finite source-dependent
edit bound and the actual occupation/long-gap consequences. They do not
construct an accepted all-source certificate, establish the necessary
actual collision upper estimate, or exclude all positive cycles. The
generic-ray and tensor results prevent specific invalid closing inferences;
they are not impossibility results for every use of stationary laws or
complete-denominator arithmetic.
