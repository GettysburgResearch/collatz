# Complete-witness charge and the limits of homogeneous power induction

23 November 2026. **PROVED:** an exact classification of affine merger
families at witnessed ordinary inputs; a constructive extraction of such
families; an all-clock exclusion on every member of the retained four-odd-step
source family; an obstruction to every finite-seed homogeneous power
induction; and an unbounded lower bound for the joint-edit metric.
**OPEN:** the original residue-512 implication and a universal successful
source-witness transformation.

The ordinary map is

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

The new [standalone Lean module](WitnessCharge.lean) uses only `Std`.
Its precise scope is recorded in section 7. The four-odd-step input family
and its forced target prefix were **already proved** in
[`WitnessLengthSeparation.lean`](../../lean/Collatz/WitnessLengthSeparation.lean).
They are reused, not presented as a new discovery. The new result is about
the complete class of homogeneous mergers and the edit metric, which allow
unlimited terminal padding.

## 1. The complete witness has an integer charge

For an actual ordinary prefix of length `L`, let `p(n,L)` count its odd
inputs and put

\[
\chi(n,L)=2p(n,L)-L.                                      \tag{WC1}
\]

This is an exact additive cocycle:

\[
\chi(n,a+b)=\chi(n,a)+\chi(T^a n,b).                       \tag{WC2}
\]

An odd step contributes `+1`, and an even step contributes `-1`.
Every complete standard cycle `1 -> 2 -> 1` contributes zero. Hence if
`T^L n=T^M n=1`, then

\[
\chi(n,L)=\chi(n,M).                                     \tag{WC3}
\]

For a known convergent input we can therefore write `chi(n)` without
choosing its first-hit certificate. This definition is only made on known
convergent inputs. There is no charge assigned to an unknown infinite
tail by taking a limit.

The formal proof also constructs complete tails after an arbitrary clock:
if `T^L n=1`, then

\[
T^{L+k}(T^k n)=1,
\quad
\chi(n,L)=\chi(n,k)+\chi(T^k n,L+k).                       \tag{WC4}
\]

Indeed the combined clock is `L+2k`, which appends exactly `k` terminal
cycles. This handles clocks before and after the supplied hit uniformly.

## 2. Exact classification and a positive family compiler

An *affine merger family at `(x,y)`* means fixed physical words, legal at
the base inputs and on an unbounded ordinary arithmetic progression
through them, whose endpoints agree identically as affine functions of
the progression parameter. This is more restrictive than a numerical
merger at one pair of integers.

Suppose the target input is `y=a*x+b`, with positive rational slope

\[
a=2^u3^v,\qquad u,v\in\mathbb Z.
\]

**WC5 (written general classification).** If complete witnesses for both
`x` and `y` are supplied, an affine merger family at these inputs exists
if and only if

\[
\boxed{\chi(x)-\chi(y)=u+2v.}                             \tag{WC5}
\]

**Necessity.** Let the two actual words have clocks `k,l`, odd counts
`p,q`, and full carries `C,D`. Their slopes are `3^p/2^k` and
`a*3^q/2^l`. Equality of the endpoint affine functions forces

\[
p-q=v,\qquad l-k=u.
\]

Appending the same actual complete tail from the common endpoint cancels
its charge. The difference is therefore `2(p-q)-(k-l)=2v+u`.

**Sufficiency.** Let the supplied complete profiles be `(L,r)` and `(M,s)`.
Append `i,j` standard cycles with
`i-j=v-(r-s)`; nonnegative `i,j` always exist. WC5 makes the padded
clock difference exactly `-u`, while the padded odd-count difference is
`v`. Both endpoint maps take the base input pair to 1 and have equal
parameter coefficients, so their constants also agree. A sufficiently
divisible ordinary increment makes both input changes integral and fixes
both complete parity words. This yields the required infinite family.

The preceding multiplier note proved the prime-factor restriction on
possible slopes. WC5 supplies the additional exact condition for admissible
slopes, using the complete ordinary certificates and their full carries.

### The actual half-map in the question

For `y=(x+1)/2`, define the finite-word condition

\[
\operatorname{HalfGerm}(x,y)iff
\exists l:\quad
T^{l+1}x=T^l y,
\quad p(x,l+1)=p(y,l).                                   \tag{WC6}
\]

Unique prime factorization shows that this is exactly the affine
coefficient condition for the half-map. In particular any fixed-word
identity on an arithmetic progression containing the base pair must
satisfy WC6. The Lean module proves, for arbitrary supplied complete
profiles,

\[
\boxed{\operatorname{HalfGerm}(x,y)iff\chi(y)=\chi(x)+1.}  \tag{WC7}
\]

Its constructive direction pads the source by `s` cycles and the target
by `r` cycles. The resulting odd counts both equal `r+s`, and the clocks
differ by exactly one. More generally a germ at clocks `l+1,l` lifts to

\[
T^{l+1}(x+2^{l+1}t)=T^l(y+2^l t),\qquad t\ge0,           \tag{WC8}
\]

where the right input is literally `(left input+1)/2`.
The underlying exact cylinder theorem retains the odd count:

\[
T^k(n+2^kt)=T^k(n)+3^{p(n,k)}t,
\quad p(n+2^kt,k)=p(n,k).                                \tag{WC9}
\]

For example, the numerical witnesses at 257 and 129 have charges 10 and
11. Their earlier merger at clocks 12 and 11 gives the infinite family

\[
T^{12}(4096t+257)=T^{11}(2048t+129)=729t+47.               \tag{WC10}
\]

This is an unconditional ordinary merger identity and therefore transports
any supplied complete source witness in that progression. In contrast,
385 and 193 have charges `-5` and `10`; their clock parities pass the
necessary phase test, but their charges exclude every affine half-germ.
Both numbers do converge, and ordinary numerical mergers still exist.

## 3. An entire retained four-step family has no homogeneous half-merger

Take `k>=1`, `m=27k`, and

\[
K=(4^m-1)/81,\qquad x=256K+1,\qquad y=128K+1.             \tag{WC11}
\]

The retained construction proves `K` is a positive odd integer and
`x mod512=257`. Its exact input tuple is

\[
[0,2,4,6,2m+8],\qquad 81x+175=2^{2m+8}.                 \tag{WC12}
\]

There are exactly four odd source steps, so `chi(x)=-2m`.
The actual target has the unconditional prefix

\[
T^{2m+7}y=3^m+1,
\qquad p(y,2m+7)=m+4,
\qquad\chi(y,2m+7)=1.                                  \tag{WC13}
\]

The source family, target prefix, and old output-length lower bound are
retained inputs. The following exclusion is new.

Every ordinary finite prefix satisfies

\[
2^L T^L n\le4^{p(n,L)}n.                                \tag{WC14}
\]

For an even step the local inequality is equality; for an odd positive
step it is `3n+1<=4n`. Induction proves WC14 with the actual odd count.
Thus if `T^L n=1` and `n<2^B`,

\[
L<B+2p(n,L),\qquad\chi(n)>-B.                           \tag{WC15}
\]

**WC16.** For every member of WC11,

\[
\boxed{\neg\operatorname{HalfGerm}(x,y).}                 \tag{WC16}
\]

**Proof.** A germ would transport the known source witness to the target.
WC7 would give `chi(y)=1-2m`. Removing the actual prefix WC13 would then
give a complete witness for `3^m+1` with charge `-2m`. But
`3^m+1<4^m=2^(2m)` for `m>=2`, contradicting WC15. The Lean proof performs
the witness construction and tail removal explicitly; target convergence
is not assumed. There is no bound on merger clocks or cycle padding.

Consequently no finite table of fixed physical word identities on
arithmetic progressions, together with finitely many numerical exceptions,
can cover the original implication. Each fixed word pair with unequal
affine coefficients can agree at at most one numerical input; balanced
pairs cover none of WC11. This statement concerns that table architecture,
not arbitrary source-dependent or recursive witness transformations.

## 4. All finite-seed homogeneous power induction is excluded

For a supplied complete witness of `n_a=3^a+1`, define

\[
J(a)=2a+\chi(n_a).                                       \tag{WC17}
\]

A homogeneous power comparison has a common physical clock and equal
full parameter coefficients:

\[
\operatorname{PowerGerm}(a,b)iff
\exists k:\quad T^k n_a=T^k n_b,
\quad p(n_a,k)+a=p(n_b,k)+b.                             \tag{WC18}
\]

Common clock is necessary because the parameter slopes are powers of
three; matching the powers of two in an arbitrary affine identity forces
the clocks to agree. The module proves the constructive classification

\[
\boxed{\operatorname{PowerGerm}(a,b)\iff J(a)=J(b)}        \tag{WC19}
\]

when complete profiles for both are supplied. A germ from one certified
power constructs a complete witness for the other and preserves `J`,
so this relation is also useful without pre-assuming both witnesses.

It is transitive with no uniform clock bound: if the first two powers
merge at clock `k` and the second and third at clock `l`, extend both
identities to clock `k+l`. Their exact odd counts compose. Therefore every
finite chain of these comparisons is already a single power germ.

Positive extraction is explicit: an accepted germ produces, for all
`t>=0`, an actual merger of

\[
3^a(1+2^kt)+1\quad\text{and}\quad3^b(1+2^kt)+1.           \tag{WC20}
\]

For example the literal eight-clock identity

\[
T^8(256t+146)=T^8(768t+436)=81t+47                        \tag{WC21}
\]

has words `01011100` and `00100101`, odd counts four and three, and carries
206 and 260. Since `3^20 mod256=145` and `3^64 mod256=1`, it gives the
actual exponent-decreasing comparison

\[
\operatorname{Basin}(3^m+1)iff\operatorname{Basin}(3^{m-1}+1)
\quad(m\equiv21\pmod{64},\ m\ge21).                      \tag{WC22}
\]

The attempted full exponent induction nevertheless fails throughout this
architecture. For every `h>=1`,

\[
3^{3h}+1<2^{5h}
\]

because `27^h+1<32^h`. WC15 therefore proves

\[
\boxed{J(3h)>h}                                         \tag{WC23}
\]

for **every** complete witness of that input.

Let a finite set of power seeds have verified complete witnesses. Their
signatures have a finite maximum `H`. Choose positive `h>=H`. A power
germ from `3h` to any seed would construct its complete witness and force
`J(3h)<=H<=h`, contradicting WC23. Transitivity excludes every chain
through arbitrarily many intermediate powers as well.

This is an all-policy conclusion for homogeneous power comparisons. It
does not restrict the word lengths, clocks, padding, or the choices made
at intermediate powers. An induction that uses changing offsets,
inhomogeneous numerical coincidences, or additional separately paid
queries is outside the excluded class.

For the first critical exponent 27, the exact signature is 57. It is
different from every signature at exponents 1 through 26. That finite
control illustrates the obstruction; WC23 proves the unrestricted
finite-seed conclusion independently of those computations.

## 5. The same charge gives an unbounded joint-edit lower bound

Use the ordinary alignment rules of the retained
[`JointEditCompiler`](../../repo-synthesis-20261123/candidate/JOINT_EDIT_COMPILER.md):
a same-parity step on both coordinates costs zero, while a step on only
one coordinate costs one. All states and clocks are actual ordinary ones.

**WC24.** A complete source witness together with a successful `t`-edit
alignment constructs a complete target witness and proves

\[
\boxed{|\chi(x)-\chi(y)|\le t.}                          \tag{WC24}
\]

At a matched step the two charges change by the same amount. At a
unilateral step the charge difference changes by `+1` or `-1`. At the
meeting it is zero. The formal induction carries the supplied complete
witness through each step; it does not assume the target's convergence.

Apply this to WC11 with `m=3h`, so `h=9k`. The source has charge `-6h`.
WC13 and WC23 force the charge of any successfully witnessed target to
satisfy `chi(y)+6h=1+J(3h)>h+1`. Hence every successful alignment obeys

\[
\boxed{t\ge9k+2.}                                      \tag{WC25}
\]

The source still has exactly four odd steps. Therefore **no edit-budget
bound depending only on source odd-step count can succeed universally**.
This differs from the retained output-length separation: standard-cycle
padding supplies arbitrarily many source odd steps that can be matched
at zero edit cost, but it cannot change the charge. WC25 covers all such
padding and every possible merger clock.

## 6. The remaining constructive step

I attempted to continue the retained four-step construction by induction
on the exponent of `3^m+1`. The positive cell WC22 and the exact compiler
WC19 make that a concrete ordinary proposal. WC23 proves that enlarging
the clocks or the menu of homogeneous power comparisons cannot complete
any finite-seed version of it. The required change is structural: a
successful next step must change the signature through a separately
justified transformation, rather than preserve it along another merger
inside the same power family.

For the original implication, a pointwise inhomogeneous merger may still
exist at every required input. WC16 does not exclude one. The edit bound
WC25 is a necessary budget, not a successful selector. No output
certificate is asserted for an unknown target solely from its source
tuple, and no universal witness implication is claimed.

## 7. Formalization and evidence boundaries

The standalone `Std` module proves 21 public declarations, including
the complete-charge uniqueness, exact ordinary cylinder lift, both
constructive germ classifications, the four-step all-clock exclusion,
power-germ transitivity and finite-seed barrier, and the actual alignment
charge theorem with WC25.

The general rational-slope formulation WC5, the equivalence between
fixed-word affine families and the derivative conditions via unique
prime factorization, the original infinite parameter construction, and
the explicitly displayed cell WC21/WC22 have written-proof scope. The
parameter construction and original tuple interpretation are credited
to the retained module; the new file reproves the needed actual prefix
profiles under `4^m=81K+1`.

The [exact checker](check_witness_charge.py) compares the classifications
with independent finite closed-orbit controls, verifies full polynomial
carries, replays lifted positive families and the retained source tuples,
and computes one complete ordinary edit optimum. Its finite-seed barrier
control does not assume or simulate convergence of the excluded larger
power. Execution records and exact source hashes are in the associated
[report](../../../../reports/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/README.md).
