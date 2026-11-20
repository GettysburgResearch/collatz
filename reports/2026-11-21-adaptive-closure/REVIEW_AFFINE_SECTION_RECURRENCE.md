# Independent review of exact affine-section finite-core recurrence

**Verdict: VERIFIED WITH FIXES, at the pinned manuscript below.**
The required fixes were the distinction between absolute and conditional
natural density in Section 7 and the distinction between a cylinderwise
affine identity and one numerical ratio-five coincidence. Both are
incorporated in the reviewed version.
The verdict covers Theorem S, formulas S1--S11, and their stated finite-core
and finite-delay consequences. It does not by itself cover the separate
new PR146 controller or an almost-sure return-to-root companion theorem.
Neither ordinary forward-five closure nor Collatz follows here.

## Frozen subject and review method

Subject: `AFFINE_SECTION_RECURRENCE.md`, SHA-256
`f033ed30e8468a1235dd5aaee0f9445074d32192b6c4f14357cb28c1ed06379a`.
The earlier version inspected initially had SHA-256
`de5d5def9d644720ba4c6c9af01439fa909d7fc19176d4d4d7b43064df529595`.
The density-only correction had SHA-256
`55cf105f0d351a9535f63b86cdb012f7618bc686c368db2835abd39732eb6833`.

The reviewer independently derived the affine recurrence, checked the
state lattice in all four parity cases, reconstructed the three-step
variance lower bound and carry moment estimate, checked the constants
in the Foster drift, and proved the hitting-time argument without an
irreducibility premise. This is a mathematical review of the manuscript;
no execution of its still-separate checker is claimed in this review.

## 1. Ordinary identity and exact state space

For `y=5*3^k*x+c`, applying the two actual shortcut branches gives

\[
k'=k+\eta-\epsilon,\qquad
c'=(3^\eta c+\eta-5\,3^{k'}\epsilon)/2.
\]

Since `5*3^k` is an odd binary unit, `eta=epsilon+c mod2` holds even
when k is negative and c has an odd denominator. The proposed lattice

\[
c\in3^{-\max(0,-k)}\mathbb Z
\]

is invariant. Equal parity bits preserve the denominator allowance.
The `(epsilon,eta)=(0,1)` transition multiplies c by three before
adding one and increases k, cancelling one denominator factor if k<0.
The `(1,0)` transition decreases k and adds at most one factor of three
to the denominator. Binary parity cancels the division by two in every
case. Thus bounded k and bounded real c imply finitely many states;
there is no hidden dense rational state space in the properness claim.

The parity-cylinder argument is also correct. An h-bit prefix fixes one
residue modulo `2^h`; its next parity splits its two lifts equally because
the affine numerator coefficient `3^p` is odd. This gives independent
fair source bits for Haar input and after any fixed finite prefix. It
does not apply to a prescribed infinite ordinary source itinerary.

## 2. Renewed variance and carry contraction

At an odd carry, k changes by plus or minus one with equal probabilities;
at an even carry it does not change. Hence k is a martingale. The identity

\[
v_2(5\,3^k-1)=2\quad(k\text{ even}),\qquad
v_2(5\,3^k-1)=1\quad(k\text{ odd})
\]

holds for all integer k, since `3^k` is one or three modulo eight.
The cases in Section 3 give an active increment within three steps with
probability at least one quarter. Orthogonality of distinct martingale
increments then yields `E Delta^2>=1/4`, not merely a positive variance
on one selected branch.

For `R=sqrt(|c|/(1+lambda))`, the bound `r'<=A*r+1/2` follows directly
from the affine recurrence. On odd carry, the two reciprocal A-values
lie in `[2/3,2]` and sum to `8/3`. Convexity of `u^(-1/2)` bounds their
sum at the endpoints, giving

\[
\mathbb E\sqrt A\le(\sqrt2+\sqrt6)/4<97/100.
\]

The even-carry values attain the same endpoint bound. Also
`1/sqrt2<71/100`. Iteration therefore gives exactly S7. No independence
between the random carry and the random k increment is assumed: the
subsequent estimate uses a pointwise bound on the g-ratio instead.

## 3. Foster constants and properness

For `g(k)=1/(10^6+k^2)` and `phi(k)=log(10^6+k^2)`, both relevant
logarithmic derivatives have absolute value at most `1/1000`. Over three
steps the g-ratio is at most `M=1000/997`. The exact values

\[
Ma=912673/997000<23/25,\qquad
Mb=2066739/997000<211/100
\]

produce S9. For `|k|>=2003`, the entire Taylor interval has `|u|>=2000`,
so `phi''(u)<=-(6/5)g(u)<=-6g(k)/(5M)`. The variance lower bound gives
the negative logarithmic term `-3g(k)/(20M)`. Combining with one hundredth
of the carry drift leaves the exact coefficient
`3/(20M)-211/10000=2569/20000>1/8` in S10.

For `|k|<=2003`, the stated threshold on R makes S11 strictly negative;
the denominator `5012009` is exactly `10^6+2003^2`. The function V is
nonnegative and proper on the proved discrete state lattice. These facts
are sufficient for the argument in Section 6, even though the negative
drift tends to zero along parts of the unbounded state space.

## 4. Finite-set hitting does not require irreducibility

Stop the three-step skeleton at its first visit to the finite core. Its
V-values form a nonnegative supermartingale. Finite branching makes each
conditional expectation finite, and the drift inequality bounds the
expectations uniformly by the starting V-value. The stopped values
therefore converge almost surely to a finite limit.

Let delta be the actual strictly positive expected decrease outside the
core. Telescoping the stopped conditional expectations gives

\[
\mathbb E\sum_{j<\tau}\delta(X_j)\le V(X_0).
\]

Thus the accumulated decrease is finite almost surely. On avoidance of
the core forever, supermartingale convergence makes the sample path's
V-values bounded. Properness confines that path to a finite state set;
delta has a strictly positive minimum there. The accumulated decrease
would be infinite, a contradiction. Hitting is therefore almost sure
from every state, without irreducibility, an invariant probability
distribution, or a uniform negative drift constant.

Applying that conclusion conditionally at each deterministic skeleton
time and intersecting the countably many probability-one events proves
infinitely many visits. An eventually trapped path inside the core is
included. This part of the proof is complete.

## 5. Density fix and deterministic boundary

For a prescribed parity prefix of length h, success has relative natural
density one inside its cylinder, hence absolute density `2^(-h)` when
membership in that cylinder is part of the condition. Without prescribing
a prefix, fixed-delay finite-core success has absolute natural density
one. The updated Section 7 now makes this distinction explicit.

The stronger zero-upper-Banach-density conclusion is also valid: each
finite successful cylinder union is periodic, so its density is uniform
over all interval positions up to a bounded error. Letting its measure
tend to one gives zero upper Banach density for the full failure set.

An exact numerical control checks the second correction. At source x=5
and clock L=12, the ordinary pair is `(1,5)`, but the two odd counts are
five and six. Hence the relative section is `(k,c)=(1,-10)`, not the
root. This was verified by a separate literal twelve-step calculation
with exact rational recurrence. Root implies ratio five; the converse
requires an affine identity across a cylinder, not one input value.

The statement still cannot be intersected over all delays to infer a
natural-density claim or success for each positive integer. Nor does a
fair-bit theorem apply after conditioning on a source's complete infinite
terminating tail. Those are mathematical quantifier boundaries, not
unverified implementation details.

There is a useful stronger control for any proposed infinite-root-return
corollary. Let an ordinary positive source x have a supplied first-hit
shortcut clock tau. A root section implies the ordinary pair is in ratio
five. After clock tau the source is in `{1,2}`, so any such return puts
the pair at `(1,5)` or `(2,10)`. From `(1,5)` there are no later ratio-five
returns; from `(2,10)` the next pair is `(1,5)` and there are none later.
Consequently the total number of root returns is at most `tau+2`,
regardless of whether five-closure was initially known at x.

Thus every certified ordinary source is necessarily an exception to an
almost-sure infinitely-many-root-returns theorem. This is consistent with
Haar measure and with every fixed-delay density-one statement. It makes
the still-missing deterministic certified-source argument particularly
explicit.
