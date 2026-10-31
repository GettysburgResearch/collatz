# Independent review of the actual-prefix rank envelopes

**Disposition:** the integer envelope, Bellman/minimality identities, contact
clock, and critical rational envelope survive independent reconstruction.
They give proper ranks with bounded forward transport, not globally decreasing
ranks. The substantive increment over a height weight is the least-majorant
property, retained arithmetic savings, and the total contact interface.

Reviewed material: `RANK_ENVELOPE.md`, `rank_envelope.py`,
`check_rank_envelope.py`, and its saved finite receipt, together with PR106
`PROOF.md` and `SPIKES.md` at
`7b7471ea0e7b359a2ac46fb1e6aff269331509c3`.
The related source periodic-switching theorem was not needed or reviewed here.

## 1. Inherited rank assumptions and implementation

The rank uses ordinary shortcut prefixes, even if they pass through one:

\[
\Gamma(n)=\min\left(g(n),
\{4^k g(T^k n-n):k\ge1,\ T^k n\ne n\}\right),
\quad g(d)=\frac{d^2}{3^{v_3(|d|)}},
\]

for n≥2, with Γ(1)=0. Omitting zero displacements is essential. The envelope
uses the separately absorbed map S; the code respects this distinction.

For a physical length-k prefix, the identity
2ᵏTᵏn=3^q n+A has 0≤A≤3ᵏ−2ᵏ. Since 3^q≠2ᵏ and a nonzero integer
displacement d has |d|≥1,

\[
n\le2^k|d|+A\le3^k|d|\le4^k g(d).
\]

Together with n≤g(n)≤n² this proves n≤Γ(n)≤n². Every prefix candidate
is at least 4ᵏ, so no candidate with 4ᵏ above the current minimum can
improve it. The evaluator's early exit and logarithmic prefix cutoff are
therefore justified without any Collatz stopping assumption.

The inherited sublevel count is also consistent: for each physical word
and nonzero displacement there is at most one source; g(d)≤Y gives at
most [1/(1−1/√3)]√Y positive choices. Counting signs and all 2ᵏ words,
then summing k≤⌊log₄M⌋, yields the stated O(√M log M) upper bound.

## 2. Integer envelope: finite attainment and exact minimality

For n≥2, put

\[
\Phi(n)=\max_{j\ge0}\left\lceil\frac{\Gamma(S^j n)}{3^j}\right\rceil.
\]

The height inequality S(x)+1≤(3/2)(x+1) gives

\[
\Gamma(S^j n)/3^j\le(3/4)^j(n+1)^2.
\]

If an evaluated integer maximum is B and 3ʲ(n+1)²≤4ʲB, every current
and future **rounded** candidate is ≤B. The rounding is safe because B
is an integer. This proves exact finite attainment and the implemented
cutoff. A source-only cutoff below one suffices because Γ(n)≥n≥2.
The number of visited forward positions and their bit lengths are O(log n);
evaluating the inherited rank at each gives O((log n)²) prefix comparisons.
This does not assert unit-cost arithmetic or a total bit-operation count.

Splitting the finite maximum at time zero and using
ceil(ceil(x)/3)=ceil(x/3) proves

\[
\Phi(n)=\max\{\Gamma(n),\lceil\Phi(Sn)/3\rceil\},
\qquad\Phi(Sn)\le3\Phi(n).
\]

If an integer F majorizes Γ and satisfies F(Sn)≤3F(n), then
Γ(Sʲn)≤3ʲF(n). Rounding and maximizing proves Φ≤F. Thus the
least-integer-majorant statement is exact, not merely a numerical optimum.

The bounds Γ≤Φ≤(n+1)² imply properness and the inherited critical
summability exponent 1/2. The upper sublevel count follows from Γ, while
all sufficiently small ordinary n are in the sublevel by the height bound.
At exponent 1/2 the harmonic lower bound Φ(n)^(-1/2)≥1/(n+1)
proves divergence; dyadic sublevel shells prove convergence above 1/2.

## 3. The contact clock is total and noncircular

At a noncontact state, Φ(n)>Γ(n), so the Bellman equality forces

\[
\Phi(Sn)-1\ge3(\Phi(n)-1).
\]

After j consecutive noncontact states this yields a lower bound
3ʲ(Φ(n)−1). On the other hand,

\[
\Phi(S^j n)-1<(9/4)^j(n+1)^2.
\]

Therefore the proposed condition

\[
4^j(\Phi(n)-1)>3^j(n+1)^2
\]

excludes such a noncontact segment. Since Φ(n)−1≥n−1>0, its first
possible j is O(log(n+1)). A noncontact state cannot immediately hit one:
if Sn=1, Bellman gives Φ(n)=Γ(n). This takes care of the absorbed
boundary in the iteration of the inequality.

Starting from a contact, take one positive step and then apply this bound
to the resulting source, whose height is at most (3n+1)/2. This proves
totality of the first positive contact return, killed on arrival at one,
with the stated logarithmic clock.

The argument uses growth rates 3 versus 9/4, not the unknown convergence
of the orbit. It is therefore not a concealed “run until descent” argument.
It also does not imply that ranks decrease from one contact to the next.

## 4. Transport inequalities and what they actually improve

For the killed deterministic pushforward K and p≥0,

\[
\sum_y\Phi(y)^p(Kf)(y)\le3^p\sum_n\Phi(n)^p f(n)
\]

is obtained by summing the pointwise forward bound on surviving sources.
For signed mass apply positivity to |f|. At most two predecessors enter
each target, and Φ(y)≤3Φ(n) for each, so

\[
(K\Phi^{-s})(y)\le2\,3^s\Phi(y)^{-s}.
\]

These are bounded-operator estimates with constants greater than one.
They supply no strict inverse supersolution, no uniform all-time moment
bound, and no automatic estimate for an unbounded contact-return clock.
The domain changes: a finite Γ moment need not be a finite Φ moment.

**Height comparison.** H(n)=(n+1)² already majorizes Γ, has the same
critical exponent 1/2, and satisfies H(Sn)≤(9/4)H(n). Thus bounded
moments and that exponent, by themselves, are not new. The new construction
should be described through its least-majorant property, Γ-specific contact
set, and savings relative to H.

Those savings are provably substantial. For h≥1,

\[
\Phi(6^h)\le12^h,\qquad
\frac{\Phi(6^h)}{(6^h)^2}\le3^{-h}.
\]

For 0≤j≤h, the first j states are halving states
2^{h−j}3ʰ. Their discounted baseline ranks are at most
4^{h−j}3ʰ/3ʲ=12^{h−j}, which are integers. After h steps, the
source is 3ʰ and every further unrounded candidate is bounded by

\[
(3/4)^\ell\frac{(3^h+1)^2}{3^h}.
\]

Its ceiling is at most 3ʰ+3≤12ʰ. This proves the entire infinite-tail
bound, not merely the first h candidates.

For every **p>0**, the finite mass

\[
\mu(6^h)=\frac{36^{-hp}}h,
\qquad\mu(n)=0\text{ otherwise},
\]

has finite Φᵖ moment, since its terms are bounded by 3^{-hp}/h,
but infinite n^{2p} moment, whose terms are 1/h. Thus the new moment
space strictly includes the corresponding quadratic-height moment space.
The restriction p>0 is necessary for this example.

The opposite strictness, relative to the Γ moment domain, follows from
the inherited power-of-three spike theorem. Its proof in PR106 was also
checked: the two lower bounds 4ᵏ and n²/3ᵏ give exponent
κ=2log4/log12 by weighted geometric means. Hence Φ(3ʰ)/Γ(3ʰ)
is unbounded. This confirms that the regularization pays a real arithmetic
price; it does not claim to preserve every Γ-integrable source mass.

## 5. Critical real envelope: total exact evaluation is valid

Let

\[
\Psi(n)=\sup_{j\ge0}(4/9)^j\Gamma(S^j n).
\]

For an odd unabsorbed state x, Sx+1=(3/2)(x+1). For an even x≥2,

\[
\frac{Sx+1}{(3/2)(x+1)}
=\frac{x+2}{3(x+1)}\le\frac49.
\]

Thus if E_j counts the even steps before time j,

\[
(4/9)^j\Gamma(S^j n)
\le(16/81)^{E_j}(n+1)^2.
\]

If absorption occurs, every later candidate is zero. Otherwise there
are infinitely many even steps. Indeed an eventually all-odd positive
orbit would make the finite integer v₂(x+1) decrease by one forever,
because T(x)+1=3(x+1)/2 on odd states. This is impossible.

The last bound therefore eventually falls below the current positive
maximum. It gives a total exact stopping rule and proves that the
supremum is attained at a finite time and is rational. The argument does
not assume Collatz, and the implementation's even counter is updated
at the correct step.

Splitting at time zero proves the exact Bellman identity, and iteration
proves least-real-majorant minimality. Properness and sublevel estimates
follow as above. No logarithmic shortcut-time bound has been proved for
this critical evaluator: O(log n) even steps can be separated by long
odd runs. Integer rounding does not preserve the exact 9/4 factor, and
the note correctly restricts that statement to the rational envelope.

## 6. Evidence and remaining obligation

The code inspection matches the formulas and boundary conventions. The
existing finite receipt checks the advertised 10,000-input range, separate
envelope recursions, and selected exact critical cases. The reference Φ
routine independently implements envelope aggregation but still calls the
shared Γ routine; Γ itself has a separate bounded reference check. These
are different layers of regression, not a proof-assistant certification.

No additional broad replay was necessary to settle the reviewed algebraic
questions. The universal validity claims above are supported by their
ordinary proofs, not by extrapolation from finite frequencies.

The remaining decisive claim would be contraction or a lower-rank physical
merging cover for the actual contact-return process. The new total contact
clock makes this a well-defined question, but does not answer it. The
document explicitly retains examples where Φ increases, including after a
numerical halving, and should continue to do so.

## 7. Addendum: ORD-005 inverse contact fans and the sharpened row bound

This addendum independently verifies the later ORD-005 statement, its two
exact rows, and the rank-only-weight obstruction. The complete reviewed
scope is ORD-001--005, including the 6^h savings and moment-domain example.

Suppose a contact source x first returns to a contact y at positive time r,
without absorption. Put P=Φ(y). Its r−1 interior states are noncontact,
so repeated Bellman equalities give

\[
\Phi(Sx)=\left\lceil\frac{P}{3^{r-1}}\right\rceil\ge2.
\]

For r≥2 this implies 3^{r−1}<P and hence
r≤D=ceil(log₃P). The same bound holds at r=1 because P≥2. The strict
inequality handles exact powers of three correctly; there is no extra
depth in that boundary case.

Backward exploration uses 2z and, when valid, (2z−1)/3. Exclude one,
which is an absorbing killed state, stop at a contact predecessor, and
expand only noncontacts. Every stopped leaf has a positive-time first
contact return to y. Every actual such return is found, since none of its
interior vertices would stop the exploration. At depth D every predecessor
must be contact; otherwise its noncontact rank would be at most one,
contradicting properness. The finite fan therefore has no missing tail.

The stronger source-height bound suggested during this review is valid.
At inverse depth d≥1, the parent has rank ceil(P/3^{d−1}), including
the d=1 root case. Since an inverse predecessor is at most twice its
parent and every state is at most its proper rank,

\[
x\le2\left\lceil P/3^{d-1}\right\rceil.
\]

At a fixed depth distinct inverse paths cannot represent the same source:
the deterministic forward orbit would then give the same path. This
source cap consequently bounds the number of tested nodes at that depth.

The Fibonacci bound is also valid. Let F_0=0,F_1=1. At depth d the
unrestricted shortcut inverse counts for targets of residues 0,1,2 modulo
three are bounded, respectively, by 1,F_{d+1},F_{d+2}. A type-zero
target has only a type-zero even predecessor; a type-one target has only
a type-two even predecessor; a type-two target has a type-one even
predecessor and at most one additional predecessor of arbitrary type.
These rules establish the three bounds inductively. Killing and contact
stops only reduce the counts.

Thus the full row has at most

\[
\sum_{d=1}^{D}\min\left(F_{d+2},
2\left\lceil P/3^{d-1}\right\rceil\right)
=O(P^\alpha),
\quad\alpha=\frac{\log\varphi}{\log(3\varphi)}\approx0.3046.
\]

For a direct check of the exponent, use F_{d+2}≤varphi^{d+1} and
P/3^{d−1}>1 on d≤D. The second width bound is at most 12P/3^d.
Split at floor(log_{3varphi}P); both geometric sums are O(P^alpha).
This counts tested nodes, not bit operations; evaluating the ranks at
those nodes has an additional arithmetic cost. It does not count bad
Collatz sources or assert any density estimate.

The two stated rows can also be reconstructed directly. For y=26, its
predecessors are contact 52 and noncontact 17; the latter has exactly
contact predecessors 34 and 11. For y=44 they are contact 88 and
noncontact 29; the latter has contact predecessors 58 and 19. The ranks
in the packet give, respectively,

\[
\{11:(2,48),\ 34:(2,1024),\ 52:(1,2704)\},\quad P=192,
\]

and

\[
\{19:(2,192),\ 58:(2,3136),\ 88:(1,7744)\},\quad P=1728.
\]

At target 26, the source 11 alone contributes
Phi(11)^{-s}=4^s Phi(26)^{-s}, exceeding the proposed target weight
for every s>0. More generally a positive nonincreasing function of Φ
cannot be an inverse supersolution on the entire contact operator: that
source contributes at least the target weight and two other positive
contributions remain. The exact full-row ratios at s=1 are
11515/2704 and 57951/5929, as stated.

These finite counterexamples exclude the specified global rank-only
weights. They do not exclude killing a larger verified core, modifying
weights on finite sets, or constructing an arithmetic weight with other
features. The finite fan theorem remains valid independently of that
unsuccessful weight choice.
