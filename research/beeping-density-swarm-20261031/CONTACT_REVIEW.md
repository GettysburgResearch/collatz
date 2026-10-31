# Independent review of the contact-family obstruction and occupation lift

**Disposition: the stated CT-001--005 claims and the cross-track cumulative
pairing are supported by the supplied arguments, within their PROPOSED
status. No surviving mathematical defect was found. Collatz remains open.**

This review was written by the inverse-transport track, independently of
the contact manuscript and its executable. The reviewed manuscript is
`pass2_contact/CONTACT_TRANSPORT.md`; the base definitions are those of
PR142, commit `d0f48c472d45a336e9083b37b45e1a8d39a2cf16`.
The frozen manuscript SHA256 is
`5f166612880ab6d84a2f12b5898af9850d52b5d8b7d28642931e3a83f2fb6e0f`.
The inherited spike used by CT-001 is credited there to PR106, commit
`7b7471ea0e7b359a2ac46fb1e6aff269331509c3`.

The main audit target was the all-k claim for

\[
n_k=243\,4^k+115,\qquad y_k=(3n_k+1)/2,\qquad k\ge12.
\]

It was not enough to check a finite sample of these sources. The review
reconstructs the treatment of every prefix up to the growing cutoff, the
infinite envelope tail, and the occupation lift's possible inverse tail.

## 1. The map and rank conventions are consistent

The prefix rank uses the unabsorbed shortcut map T; the envelope and
occupation process use S, absorbed at one. The rank omits zero
displacements. Neither a return to the starting source nor a zero
displacement is assigned rank zero. The contact return has positive
time, and the occupation arc includes its source and excludes its endpoint.
Those conventions are necessary for the residual and trace identities.

For a nonzero integer d,
`g(d)=d^2/3^v3(d)>=|d|>=1`. Hence a prefix at depth
`j>floor(log2 u)` has candidate `4^j g(d)>u^2` and cannot improve the
baseline. This cutoff requires no convergence hypothesis.

## 2. CT-002: the exact Gamma identities hold for every k>=12

### 2.1 Parity transfer also preserves displacement valuations

For n use b=115 and L=2k. For y use b=173 and L=2k-1. The differences
from the templates are respectively `3^5 2^L` and `3^6 2^L`, so every
prefix through L has the corresponding template parity word. Write

\[
T^j u=(3^{q_j}/2^j)u+\delta_j.
\]

The perturbation in the displacement `T^j u-u` is

\[
(3^{q_j}/2^j-1)(u-b).
\]

Its 3-adic valuation is at least 5 for the n family, and at least 6 for
the y family. In fact the coefficient `3^{q_j}-2^j` is a 3-adic unit
when q_j>=1; all of the templates here begin odd. The template
displacements have valuations at most 3 and 4 respectively. Thus no
cancellation can change any of these valuations. This check concerns the
**displacement**, not merely the transported state.

The first hits of one occur at depths 23 and 22, with 10 and 9 odd
steps. Continuing through the 1,2 cycle proves that no later template
displacement introduces a larger valuation. These are finite arithmetic
certificates, independently reproduced in `check_contact_review.py`.

### 2.2 The first 23 candidates

Apart from the winning depths 3 and 1, the leading coefficients

\[
a_j=\frac{(3^{q_j}-2^j)^2}{3^{v_3(T^j b-b)}}
\]

are at least 1 for b=115 and at least 25/27 for b=173. The absolute
values of `3^q/2^j-1` are at least 5/32 and 1/4, respectively; the
common lower bound 1/8 used in the manuscript is therefore safe. The
offsets are nonnegative and less than 3. For u>=240,

\[
|T^j u-u|\ge |3^{q_j}/2^j-1|u-3
\ge(1-24/u)|3^{q_j}/2^j-1|u.
\]

Consequently every nonwinning short candidate is at least
`(81/100)(25/27)u^2=3u^2/4`, strictly larger than
`(u+5)^2/3`. The winning displacements are `(n+5)/8` and `(y+1)/2`.
Their 3-adic valuations are exactly one, giving the two claimed candidates.
Both are smaller than the baseline u squared.

### 2.3 Prefixes from depth 24 through L

The template is already in the 1,2 cycle. Its coefficient is at most 1/2
and its affine offset lies in [0,2]. Thus the displacement magnitude is
at least u/4. Its 3-adic valuation is at most four by the previous
separation argument. Every such candidate is at least

\[
\frac{4^j}{16\cdot81}u^2>u^2.
\]

For the y family at k=12 this range is empty, which creates no gap:
L=23 and the next range starts at 24.

### 2.4 Every prefix after L through the growing cutoff

The two sources reach the same exact state

\[
T^L u=3^{k+4}+2.
\]

For n the template has q=k-1 at time 2k; for y it has q=k-2 at time
2k-1. The asserted state follows by substituting the respective template
perturbations. These formulas persist for all k>=12 because advancing
the terminal template by two steps returns to the same state and adds
one odd step.

The exact remaining cutoffs are

\[
\lfloor\log_2 n_k\rfloor=2k+7,\qquad
\lfloor\log_2 y_k\rfloor=2k+8.
\]

The remaining numbers of steps are therefore 7 and 9. The common height
bound in the manuscript is nevertheless correct: the extra factor 3/2
needed for the y family's ninth step is paid by
`y_k>=(3/2)243*4^k`. Applying `T(v)+1<=(3/2)(v+1)` gives

\[
T^j u/u\le (3/2)^8\left[\tfrac13(3/4)^k+
                                  \tfrac1{81}4^{-k}\right]<1/2.
\]

The inequality is certified exactly at k=12, and each term decreases
with k. Also `4^L>=2u` holds at k=12 and for every later k. Equivalently,
putting a=4^k, the two required inequalities reduce to
`a^2-486a-230>=0` and `a^2-2916a-1384>=0`; their coefficients after
translation by a=4^12 are all positive.

Hence every remaining candidate has nonzero displacement of magnitude at
least u/2, and is at least `4^(L+1)u/2>u^2`. The still later candidates
are excluded by the initial logarithmic cutoff. This covers every depth,
not just the parity-controlled part of the orbit.

### 2.5 The Phi identities

The six Gamma upper bounds B_0 through B_5 in the manuscript are valid
actual-prefix witnesses. I independently derived their quadratic
polynomials from the affine prefix words and checked the valuation
separation on this family. The 3-adic displacement valuations of these
witnesses are respectively `1,1,4,4,2,1`.

There are eight relevant polynomial comparisons:
`B_j/3^j<=B_0`, j=1,...,4, and
`B_(j+1)/3^j<=B_1`, j=1,...,4. Their differences have nonnegative
coefficients when expanded in n-115, with a positive coefficient in
each case. This certifies them on the entire needed half-line.

For positions j>=5 relative to either source u, the general envelope
bound is at most `(3/4)^5(u+1)^2<(u+1)^2/3`, which is below that
source's exact Gamma value. Those Gamma values are integers, so taking
ceilings preserves the bounds. The j=0 term attains the value. Therefore

\[
\Gamma(n_k)=\Phi(n_k)=(n_k+5)^2/3,
\qquad
\Gamma(y_k)=\Phi(y_k)=(y_k+1)^2/3
\]

hold for all k>=12. The adjacent sources are both odd contacts and
nonmultiples of three. The claimed limiting height and rank ratios follow.

## 3. CT-001 and CT-003: the finite-core obstructions have the stated scope

For CT-001, the only inherited substantive input is the earlier
power-of-three spike. The least doubling ancestor of `m=3^h` which is
contact exists: otherwise inverse Bellman identities force its Phi rank
toward one, contradicting its increasing ordinary height. Every state
between this ancestor and m is noncontact by minimality. The ensuing
positive-time return cannot be absorbed before reaching another contact,
since a noncontact cannot step directly to one.

Iterating the strict noncontact rank growth gives the displayed lower
ratio `(1/3)(3/2)^r`; the spike forces r to infinity. Every state on the
arc after its source has Phi at least m and hence ordinary height at
least `sqrt(m)-1`. Thus the **entire arc**, not just its endpoints,
eventually avoids each finite terminal set. The weighted atomic population
with coefficients `2^-j Phi(x_j)^-p` has finite input p moment and
infinite output p moment. Endpoint collisions do not weaken this lower
bound because all masses are nonnegative.

For CT-003 the odd family has a one-step contact edge and valuation pair
(0,0) at both ends. For a<2s, the inverse single-predecessor ratio tends
to `(3/2)^(2s-a)>1`. For a>=2s, the weights at n_k do not tend to zero,
which excludes summability even on this sparse subsequence. These two
cases exhaust every real a. A finite core or finite weight patch cannot
remove the eventual adjacent edge. Induction on the smaller odd-contact
section also retains this edge, so the same obstruction applies there.

This does not exclude arbitrary residue-dependent, nonmonotone, or
computable arithmetic corrections. It excludes precisely the stated
eventual polynomial height/rank weight with a valuation-only factor.

## 4. CT-004: no hidden infinite boundary enters the occupation lift

Fix a noncontact target n with M=Phi(n). Along any backwards segment
which has not yet met a contact, Bellman gives the exact rank
`ceil(M/3^d)` at depth d. A noncontact positive state cannot have rank
one, so every branch meets a contact within `ceil(log3 M)` levels.
Shortcut inverse fibers have at most two predecessors, and the proved
finite fan bounds give a complete finite enumeration. A contact target
has only the arc which starts there, since all return endpoints are
excluded from the occupation sum.

Each contact leaf contributes once. A noncontact arc cannot repeat a
state, because its Phi ranks strictly increase forward. Determinism
prevents two different paths from the same contact source to the target
before the next contact. This proves pointwise finiteness and excludes
an unobserved inverse tail. Positivity follows independently by taking
the first contact among the target's doubling ancestors.

Summing the telescoping residual of each finite arc gives
`(I-K)Lw=iota_C(w-K_Cw)`. Every pointwise expression is a finite sum;
the global mass equality `sum Lw=sum r(x)w(x)` follows by nonnegative
Tonelli summation even when both sides are infinite.

For a prescribed finite contact trace w, the noncontact values are a
finite recursion in contact boundary values. A superbalanced extension
therefore dominates the lift, and an exactly balanced extension equals
it. This proves the claimed minimality and uniqueness without assuming
summability or an effective convergence oracle. If w is pointwise
computable, this finite recursion computes each lift value.

## 5. CT-005 and the inverse-density pairing

The stated clock bound follows by applying the earlier noncontact exit
criterion at u=Sx and choosing the next integer strictly beyond its
logarithmic threshold. It includes the extra initial step from x. Its
height exponent is

\[
1+\frac{\log(3/2)}{\log(4/3)}
=\frac{\log2}{\log(4/3)}=\theta.
\]

The constants and moment exponents in (15)--(17) follow with this theta.
The occupation sum is finite for s>1/2 after paying the logarithmic
clock. Its p-height and p-Phi moments require the explicitly stated
additional source integrability. Repeated use of the endpoint bound
increases the required exponent; it is not a uniform bound on iterated
contact transport in one fixed moment space.

The stronger pairing (20)--(22) is also valid. It uses the actual odd
endpoint population of the occupation lift and its finite second height
moment. From the independently reviewed inverse theorem,
`sum_(q<=Q)rho_q(t)<=kappa_t[t(1+Q log96)+(9/8)(64/81)^Q]`, and the
unconditional cycle factor bound `kappa_t<=3t+1`, nonnegative summation
gives exactly (21). Summation by parts gives the Abel upper order (22).
The explicit choice s=6 is safe; `3^11<2^18` proves
`theta<11/4`, so `2theta+1/2<6`.

This argument does not equate shortcut return time with odd inverse
depth. It yields an average in inverse depth, with a stated moment cost;
it neither bounds every individual depth nor proves unweighted Collatz
termination.

## 6. Independent deterministic receipt

`check_contact_review.py` is independent of the contact executable and
does not import its functions. It checks both template certificates,
all six affine/valuation witness polynomials, all eight envelope
comparisons, the exact cutoff inequalities, and the complete Gamma/Phi
formulas at 24 sample indices:
`k=12,...,32,40,60,100`. Its rank evaluator uses the full logarithmic
prefix cutoff, and its envelope evaluator uses the universal source-height
tail bound. The universal conclusion above rests on the proof, not on
these samples.

Normal and Python `-O` runs produced byte-identical JSON. Receipt:
`contact_review_checks.json`, SHA256
`f7378ecb4e5c736a467b37621105609fed0af3f9eb40abc4d91c21c858b2d41f`.
No proof-assistant certification is inferred. The reviewer found and
reported a display-control-character typo and requested that the two
different long-prefix cutoffs and the relative envelope time be made
explicit; all three editorial fixes are present in the finalized draft.
