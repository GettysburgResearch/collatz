# Trying to construct the triadic dual from the unchanged ordinary source

**Status: OPEN construction attempt.** The finite triadic closing criterion
in the pinned PR178 is retained. This note derives the exact complementary
coefficient and fixed-denominator lattice available from our pressure
maximum, then tests whether the other repository routes determine its
translation. They do not currently do so. No universal candidate, new
conditional closing theorem, or numerical census is asserted.

## 1. What the wider repository supplies

The resident research map and scoped errata distinguish ordinary
realization, coefficient stopping, complete-cycle divisibility, transported
mass, and lower-rank merging. These are separate open obligations. In
particular, neither a compatible completion nor a sequence of changing
finite witnesses supplies one positive ordinary source for all clocks.

The more recent interfaces relevant to this attempt are as follows.

| Source read at a fixed head | What it supplies here | What is still needed |
|---|---|---|
| PR146, `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/PREFIX_REPRESENTATIVES.md`, blob `76f124b14a3f01c26060e44bb83b0ebbe3e3a2ed` | Exact high-bit transport and smaller equal-clock partners; sufficiently high tails over a certified lower source reduce to shifted powers of three. | The retained comparisons, including the shifted-power families, are not all decided. |
| PR173, `fa0c9e2a2851e6324391e39c17afcb5913185aec`, `research/lean-shell-cover/README.md`, Section 6, blob `93450d0c12443a33d1eacbae295c8e4ad56ccfd7` | Every positive orbit makes a bounded visit to the marked band above a power of two. | Eventual descent across returns remains open; a marked visit is not a complementary-carry congruence. |
| PR177, `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`, `research/lean-exact-witness-global-20261121/HIGH_VARIANCE_WITNESS.md`, FB1--FB9, blob `f3143fc4c63c3eff749ceb2d18ce7326a184a5c1` | Complete capturing certificates trim to a finite boundary on which their supplied grade can be optimized exactly. | A certificate for the actual target, or a forward meeting with the known basin, is not supplied by that optimization. |
| Our parent `b78819e95ee7d39f02022de991b42217821e7590`, `research/closure-round2-20261123/SOURCE_CLOSURE.md` and `TwoSidedPressure.lean` | In an escaping unit component, one fixed attained pressure maximum has both all-forward and all-inverse coefficient inequalities. | Their simultaneous incompatibility has not been proved. The product construction remains a source-pinned written input to the generic Lean result. |
| PR180, `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, `research/source-clock-20261123/TARGET_DESCENT.md`, TD1--TD3, blob `7db001e85a372a5f62429621ee322d84a4548f38` | An exact nonnegative discrepancy for an integral semigroup word that passes the original target's parity guards. | The first failed target parity must still be repaired without losing the descent endpoint or earlier guards. |

These results motivated trying to construct a different witness: a signed
triadic complementary start for the original target itself. Throughout
the main construction attempt, `n` stays fixed and the parity word is the
actual prefix of its ordinary orbit. We do not replace it by an optimized
source, a nearby band offset, or a newly chosen parity cylinder.

## 2. The precise triadic construction target

The new input is PR178 at
`4e204f54136c79cf8c9393b34e3330594f99ae0a`:

- `research/global-closure-20261123/duality/TRIADIC_RANK.md`, blob
  `ab60fd248086bd8a2b753ea12a7b41387ea5c2de`;
- `research/global-closure-20261123/duality/lean/TriadicDualClosure.lean`,
  blob `8eed815f2dc89b16da80d759c965244513082ac4`.

Its Lean result closes an all-time compatible trajectory from one finite
candidate `(n,a,r)`. Its explicit finite height criterion is a written
proof, not a theorem supplied by that Lean module. I read both arguments;
no source construction is hidden in either conclusion.

Use the shortcut map `T`, and fix `n>0`. Let

\[
x_i=T^i(n),\quad e_i=x_i\bmod2,\quad
s_K=\sum_{i<K}e_i,\quad b_K=K-s_K.
\]

The complete original and complementary carries obey

\[
C_0=D_0=0,\qquad
C_{i+1}=3^{e_i}C_i+e_i2^i,\qquad
D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i.
\tag{1}
\]

Thus `3^s_K n+C_K=2^K x_K`. The closing target is to find one
`a in Z`, `r>=0`, and `K` satisfying

\[
2^K\mid 3^{b_K}a+3^rD_K,
\qquad
K\ge8\operatorname{bl}(n)+(9r+8)
\operatorname{bl}(\max(1,|a|,3^r))+2.
\tag{2}
\]

Here `bl(u)` is the least positive `L` with `u<2^L`. Every carry in
(2) comes from that same fixed `n` through that same actual clock `K`.

The finite criterion closes because a passed prefix cancels the
denominator exponent at original-even steps, while the integral paired
energy eventually decreases. It does not require a conjecture about
cycles in addition to the candidate. Conversely a known path to one
already constructs a triadic dual by pulling the complementary terminal
value two backward. Therefore constructing (2) universally is a full
Collatz-strength task.

The parity-complement involution and its rationality boundary come from
Monks and Yazinski, *The autoconjugacy of the 3x+1 function*, Theorem 2.1
([primary paper](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf)).
That theorem does not construct the numerator in (2).

## 3. What the common pressure maximum adds

Suppose, for this subsection, that the fixed ordinary source is the
single pressure maximum `m` selected in an escaping unit component in
our previous packet. This is an additional property of that source;
we do not assert that an arbitrary original target is already this
maximizer. If an escaping target shares the component with `m`, their
ordinary orbits eventually meet, but a certificate at `m` has not thereby
been constructed at the target.

Let the accelerated odd clocks be `A_j`. The previous result gives

\[
2^{A_j}<3^j\qquad(j\ge1).
\]

This extends to every positive shortcut clock:

\[
c_K:=3^{s_K}/2^K>1\qquad(K\ge1).
\tag{3}
\]

Indeed, between consecutive odd clocks `A_j<K<=A_(j+1)`, the original
odd count is `j+1`, and
`3^(j+1)/2^K >= 3^(j+1)/2^A_(j+1)>1`. At an odd clock use the
displayed inequality directly. This retains the original ordinary
clock rather than substituting an odd-step count for it.

The real affine map obtained by following the *complementary word*,
without yet claiming that its input passes any rational parity test, is

\[
F_K(y)=\bar c_K y+\frac{D_K}{2^K},\qquad
\bar c_K=\frac{3^{b_K}}{2^K}.
\]

Its slope satisfies the exact relation

\[
c_K\bar c_K=(3/4)^K.
\tag{4}
\]

Consequently (3) gives the uniform prefix contraction

\[
|F_K(y)-F_K(z)|<(3/4)^K|y-z|.
\tag{5}
\]

This was the strongest new input to the attempted construction: every
real initial candidate is drawn together under the same complementary
affine word. However, (5) bounds differences. It does not bound the
translation `D_K/2^K`, nor establish parity compatibility for any chosen
real or rational input.

## 4. Exact pullback arithmetic: the translation still has to be paid for

For fixed `n,K,r`, the number `3^b_K` is invertible modulo `2^K`.
There is therefore exactly one residue class of possible numerators:

\[
a\equiv a_{K,r}:=-3^{r-b_K}D_K\pmod{2^K},
\tag{6}
\]

where a negative exponent in this congruence means the inverse of the
corresponding power of three. In particular the full fixed-denominator
set of compatible initial values is exactly

\[
\boxed{\left\{\frac{a_{K,r}+2^Kj}{3^r}:j\in\mathbb Z\right\}.}
\tag{7}
\]

Changing the representative only moves by `2^K/3^r` in the real
initial coordinate. Formula (7) is a set of legal full-prefix candidates,
not an assumption that every point in the smaller height window occurs.

It is useful to distinguish this set from the easier pullback of
integer *terminal* values. That latter set is

\[
F_K^{-1}(\mathbb Z)
=-\frac{D_K}{3^{b_K}}+
\frac{2^K}{3^{b_K}}\mathbb Z.
\tag{8}
\]

At the pressure maximum its spacing is greater than `(4/3)^K` by
(4)--(5). Allowing a terminal denominator `3^r` makes a larger pullback
lattice, but its intersection with the prescribed initial grid
`3^(-r) Z` must still be taken. That intersection is precisely (7).
Ignoring this intersection would incorrectly manufacture extra choices
of the initial numerator.

For a certificate at its own horizon put `N=bl(n)` and
`L=bl(max(1,|a|,3^r))`. Equation (2) demands

\[
L\le\frac{K-8N-2}{9r+8}.
\tag{9}
\]

So the desired member of (7) must have an exceptionally small numerator
relative to the period `2^K`. Centering (6) guarantees only
`|a|<=2^(K-1)`. It gives no bound of the strength (9).

I tried using (5) to choose the terminal integer closest to
`D_K/2^K`, then pulling it back. Equations (7)--(8) show the exact
failure: contraction enlarges the distance between its inverse images,
and the prescribed numerator grid imposes an additional congruence on
that terminal choice. The unknown translation has not disappeared.

The original small source gives a second exact congruence,
`C_K=-3^s_K n mod 2^K`. I also tried to couple this to (6) through
the ordered carries. The determinant-like combination is exactly

\[
W_K=3^{b_K}C_K-3^{s_K}D_K,
\]

with the signed recurrence already recorded in the pinned triadic
packet. That recurrence retains the actual order of every parity.
I obtained no estimate putting (6) in the small window (9). Replacing
its signs by average cancellation would be an unsupported step.

## 5. Why the other routes do not presently provide that translation

**Band visits.** A marked state `2^d+h` has a small *real* offset
relative to `2^d`. This supplies no divisibility of `h` by a long power
of two. Consequently it does not identify the complementary carry with
the one at the nearby power of two. At a later marked state, `h` is
smaller than that state but can exceed the unchanged least-bad target
`t`. Inferring convergence of the offset first requires `h<t`.
Even when that comparison holds, its eventual hitting time need not
fit inside the common binary-prefix clock. PR146's exact high-bit
identities preserve this clock issue and leave the shifted-power
comparisons open; they do not justify discarding it.

**Complete source optimization.** Choosing the least-grade complete
boundary source optimizes certificates ending at one. It supplies no
relation between its word and the complementary word of the original
target. Transporting its numerator into (6) would need an actual
meeting, or another proved exact word relation.

**Semigroup descent.** A freely chosen multiplicative word may have a
useful endpoint. The source-pinned discrepancy theorem explains why
its first target-parity mismatch is substantive. Such a mismatch also
prevents substituting its carry for `D_K` in (2). Repairing it by editing
the actual parity word is not a free parameter: the fixed ordinary
source determines its entire length-`K` word uniquely.

**Real complementary contraction.** The ordinary hypothesis cannot be
dropped when attempting to turn (5) into a rationality or triadicity
claim. The resident `1110` completion has the rational cycle

\[
-19/11\longmapsto-23/11\longmapsto-29/11
\longmapsto-38/11\longmapsto-19/11.
\]

Every coefficient prefix is supercritical. Its complementary cycle is

\[
8/13\longmapsto4/13\longmapsto2/13
\longmapsto1/13\longmapsto8/13.
\]

The complementary prefix slopes contract, but the exact dual `8/13`
is not in `Z[1/3]`. This is an algebraic scope check using the already
resident completion ghost, not a positive ordinary counterexample or a
refutation of the original construction target.

## 6. Joint denominator optimization at its own horizon

I next allowed `r` to vary with `K`, rather than choosing a denominator
beforehand. The horizon itself gives a restrictive exact budget.
Since `3^r>=2^r` and `3^r<2^L`, one has `L>=r+1`. Consequently
every admissible pair satisfies

\[
K\ge8N+(9r+8)(r+1)+2
=8N+9r^2+17r+10,
\qquad r\le\sqrt K/3.
\tag{10}
\]

Thus at a fixed clock only `O(sqrt K)` consecutive powers of three
can be used within the candidate's own height. Taking exponentially
many denominator exponents and then increasing the horizon does not
preserve the original approximation modulus.

### What pigeonholing those powers actually returns

Put `M=2^K` and `omega=-3^(-b_K)D_K mod M`. For `R>=1`, partitioning
the residues `3^j omega mod M`, `0<=j<=R`, into `R` intervals gives
some `0<=s<s+d<=R` and an integer `z` such that

\[
\left|3^s(3^d-1)\omega-zM\right|\le\lceil M/R\rceil.
\tag{11}
\]

It gives a close **pair**, not an orbit point near zero. Let
`v=v2(3^d-1)` and `u=(3^d-1)/2^v`. Dividing (11) by `2^v` gives
an integer `A` with

\[
3^s u\omega\equiv A\pmod{2^{K-v}},\qquad
|A|\le\frac{\lceil M/R\rceil}{2^v}.
\tag{12}
\]

The extra odd factor `u` is coprime to three. It equals one only for
`d=1,2`: for odd `d`, reduction modulo eight forces `3^d-1=2`;
for even `d`, the two even factors `3^(d/2)-1` and `3^(d/2)+1`
would both have to be powers of two differing by two, hence be two
and four. In general (12) approximates by a rational with denominator
`3^s u`, outside the required localization. There is no guarantee that
the close pair has one of those two exceptional gaps.

Even in those exceptional cases the pigeonhole estimate is too weak to
establish the height budget. Explicitly, `v=1` for odd `d`, while
`v=2+v2(d)` for even `d`, so `2^v<=4R`. The right-hand side of the
guaranteed bound in (12) is therefore at least

\[
\frac{M}{4R^2}\ge\frac{9\,2^K}{4K}
\qquad\text{when }R\le\sqrt K/3.
\tag{13}
\]

For `K>=18`, this exceeds `2^(K/8)`, whereas every admissible numerator
in (2) has absolute value less than `2^(K/8)`. Equation (13) compares
the **guaranteed bound** with the requested bound; it is not a lower
bound on the error of a lucky actual pair. Thus the joint pigeonhole
argument neither produces the right denominator nor guarantees the
required exponential saving.

There is also an explicit generic residue for which every allowed
denominator fails. Take `omega=2^(K-1)-1`. For
`0<=r<=R<=sqrt K/3` and `K>=18`, one has `3^r<=2^(K-2)`; its centered
numerator is exactly `2^(K-1)-3^r`, at least `2^(K-2)`. However, this
is **not** an admissible fixed-small-source counterexample: the
complementary original word is `0^(K-1)1`, whose least positive
ordinary source is `2^(K-1)`. Its bit length is `N=K`, inconsistent
with `K>=8N+10`. The ordinary-height restriction excludes this example.

### A count that does retain the actual ordinary height

The following finite-budget bound does use positive ordinary sources.
Fix their exact bit length `N>=1` and a deadline `K`. Assume
`K>=8N+10`; below that value no candidate has its own required horizon.
Define

\[
L_r=\left\lfloor\frac{K-8N-2}{9r+8}\right\rfloor,
\qquad
J_{N,K}=\{r\ge0:L_r\ge1,\ 3^r<2^{L_r}\}.
\]

Then the number of ordinary integers `2^(N-1)<=n<2^N` possessing
a certificate (2) at **some** clock no later than `K` is at most

\[
\boxed{\sum_{r\in J_{N,K}}\left(2^{L_r+1}-1\right).}
\tag{14}
\]

**Proof.** A candidate `(a,r)` with a successful clock `k<=K` already
passes the full prefix through its own horizon `H(N,a,r)<=k`.
It obeys `|a|<2^L_r` and `3^r<2^L_r`, so there are at most
`2^(L_r+1)-1` numerators at a given `r`. The rational `a/3^r`
determines its own parity word at that horizon. Its complement fixes
one ordinary source residue modulo `2^H`, by the finite parity-word
bijection. Since `H>=8N+10>N`, at most one source in the specified
`N`-bit interval has that residue. Sum over the candidates; duplicates
can only reduce the number of distinct sources covered. This also
explains why no extra factor counting possible clocks is necessary.

Using (10), a simpler upper bound in (14) is

\[
\left(\lfloor\sqrt K/3\rfloor+1\right)
\left(2^{\lfloor(K-8N-2)/8\rfloor+1}-1\right).
\tag{15}
\]

For every fixed `0<epsilon<8`, if `K<=(16-epsilon)N`, the fraction
of all `N`-bit sources that (14) can certify by this deadline is at most

\[
4\left(\frac43\sqrt N+1\right)2^{-\epsilon N/8},
\tag{16}
\]

and hence tends to zero. This is a restriction on a uniform construction
using this particular conservative certificate horizon. It is neither
a lower bound on the ordinary time to one nor evidence that any source
fails at a later source-dependent horizon.

The actual small-source information is therefore substantive: it removes
the simple generic obstruction above and sharply limits any uniform
early certificate. What remains missing is a positive estimate for the
specific translated residue (6) at a sufficiently late horizon chosen
for the fixed source. The joint search over denominator exponents does
not supply that estimate.

## 7. First unsupported inference and outcome

The desired inference is still:

> For the actual word of one fixed positive ordinary `n`, some pair
> `(K,r)` makes the centered residue in (6) small enough to satisfy
> (9), with `3^r` included in that same height.

The attained pressure maximum gives (3)--(5), and the complete ordered
carry gives (6)--(8). No argument here crosses from these identities to
the quoted source-specific small-residue assertion. In particular, a
real contraction and a legal candidate at every changing finite depth
have not been turned into one candidate meeting its own height budget.

The contribution of this lane is the explicit attempted connection
between the previous same-root pressure theorem and the new full
triadic closing mechanism, with the initial/terminal lattices and
ordinary-source guard kept distinct. The missing construction remains
open. No new Lean module or numerical search was added to disguise
that gap as a further closing theorem.
