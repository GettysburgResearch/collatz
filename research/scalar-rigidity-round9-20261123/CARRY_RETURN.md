# A uniform ordinary return bound for arbitrary denominator-eight carries

23 November 2026. Parent:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Status: PROPOSED written theorems, with finite Lean arithmetic and
exact ordinary controls. The denominator-eight exclusion and full
Collatz remain OPEN.**

This continues the actual scalar construction in the parent packet.
The new result covers **every first carry excursion**, with no bound
on the carries or excursion length: its physical endpoint is bounded
by the same two-step map `P(x)=(9x+5)/32`. It therefore extends the
short-block descent result to arbitrary paid excursions. A hypothetical
least positive source with scalar `7/8` must lie in a precise rare
binary class. The return procedure is total for one excursion; its
iteration is not proved to terminate on every ordinary source.

## 1. Actual scalar and complete carry equations

For positive odd q use

\[
U(q)=(3q+1)/2^{g(q)},\qquad g(q)=v_2(3q+1),\qquad
h(q)=\sum_{i\ge0}g(U^iq)/3^{i+1}.
\]

The pinned parent results R8-G1--R8-G2 supply

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q),\qquad
h(q)\in\mathbb Z[1/3]\Longleftrightarrow q\longrightarrow1.
\tag{1}
\]

Their source is `research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`
at the full parent head above. The parent `ORDINARY_SELECTOR.md`,
R8-O1--R8-O4, constructs actual finite expanding returns with scalars
approaching `7/8`; it does not construct equality at that value.

After ternary clearing, the unresolved denominator-eight phases are
`5/8,7/8`. Write an actual tail as

\[
h(q_i)=p_i+k_i,\qquad k_i\in\mathbb Z_{\ge0},
\]

with p alternating between the two phases. At a start with `p_0=7/8`,
the canonical gaps b alternate `2,1`. The full coupled equations are

\[
g_i=b_i+3k_i-k_{i+1}\ge1,\qquad
2^{g_i}q_{i+1}=3q_i+1.
\tag{2}
\]

A low state means `k_i=0`. Every high state has `h>=13/8`. At `h=5/8`
the next actual gap must be one, and its successor has scalar `7/8`.
At `h=7/8`, gap two starts an unpaid low pair `(2,1)`, whereas gap one
enters the high state `13/8`. These exhaust the options by strictness
of the lower bound in (1).

Any actual denominator-eight tail avoids one, since `h(1)=1` and its
fractional phases remain nonzero. All its ordinary states are therefore
at least three. None of the following minima is identified with a
pressure maximum.

## 2. The complete two-block family and its sharp threshold

Let L have gaps `(2,1)` and P have gaps `(1,4)`. Their literal domains
and complete affine maps are

\[
q\equiv9\pmod{16}:\quad L(q)=\frac{9q+7}{8},\qquad
q\equiv3\pmod{64}:\quad P(q)=\frac{9q+5}{32}.
\tag{3}
\]

Both preserve the candidate scalar `7/8` over their two transitions.
For m consecutive L blocks followed by P, put

\[
A_m=\frac9{32}\left(\frac98\right)^m.
\]

The complete endpoint is

\[
r=A_m(q+7)-\frac{29}{16}.
\tag{4}
\]

**R9-C1 (complete source class and 10/11 threshold).** Let u_m be the
least positive residue of `13*9^(-m-1)` modulo 32. The complete positive
ordinary source class for `L^mP` is

\[
\boxed{q=2^{3m+1}(u_m+32z)-7,\quad z\ge0,\qquad
r=\frac{9^{m+1}(u_m+32z)-29}{16}.}
\tag{5}
\]

For `m mod 4` equal to `0,1,2,3`, the respective values of u_m are
`5,29,21,13`. Every such source descends when `0<=m<=10`, and every
such source expands when `m>=11`.

To verify the class, write `q+7=2^(3m+1)u`. The L blocks successively
remove three powers of two from this shifted coordinate. Their last
endpoint x has `x+7=2*9^m*u`. The P condition is exactly

\[
9^{m+1}u\equiv13\pmod{32},
\]

which is the condition in (5), including an odd final endpoint.
Conversely, (5) makes every intermediate L domain and the last P domain
literal. It also proves positivity, oddness, and necessity of the class.

For the threshold, `m=0` is immediate. When `1<=m<=10`, (5) gives
`q>=73`, and `A_m<=A_10<1`. Consequently

\[
r-q\le80A_{10}-\frac{1197}{16}<0,
\qquad A_{10}=\frac{31381059609}{34359738368}.
\tag{6}
\]

When `m>=11`,

\[
A_m\ge A_{11}=\frac{282429536481}{274877906944}>1,
\]

so `(A_m-1)q+7A_m-29/16>0`. The additive terms are retained in both
directions. This is a theorem for the complete class, not an inference
from a finite list of source residues.

## 3. Normalize the physical source by its integer carry

The useful new coordinate is

\[
Y_i=q_i/2^{k_i}.
\]

Combining both equations in (2) gives the exact identity

\[
\boxed{Y_{i+1}=
\frac{3Y_i}{2^{b_i+2k_i}}+\frac1{2^{b_i+3k_i}}.}
\tag{7}
\]

The destination carry disappears from this expression. In particular,
when `k_i>=1`, positivity of Y gives the upper maps

\[
\begin{array}{c|c}
p_i=5/8&A(Y_i)=3Y_i/8+1/16\\
p_i=7/8&B(Y_i)=3Y_i/16+1/32.
\end{array}
\tag{8}
\]

This bound is uniform in arbitrarily large integer carries. Set

\[
F=B\circ A,\quad F(y)=\frac9{128}y+\frac{11}{256},\qquad
E(x)=\frac{3x+1}{4},\qquad G(y)=\frac{3y+1}{2}.
\tag{9}
\]

The entry from a low `7/8` state x uses gap one and gives the normalized
high value E(x). The map G is the forced final low transition from
`5/8` to `7/8`. All these affine maps are increasing. The fixed point
of F is `c=11/238`, and

\[
F(y)-c=\frac9{128}(y-c).
\tag{10}
\]

Thus for `y>=c` its iterates remain between c and y and decrease.

## 4. Every paid first excursion has the same upper map

A paid first excursion starts at scalar `7/8`, immediately takes gap
one into `13/8`, and stops on its first subsequent low scalar. If that
first low scalar is `5/8`, append its forced gap one so that the
normalized excursion ends at `7/8`. Its length is even, say `2*l`.

**R9-C2 (all-carry ordinary majorant).** If the initial ordinary source
is `x>=3` and the normalized endpoint is r, then

\[
\boxed{r\le P(x)=\frac{9x+5}{32}\le\frac x3.}
\tag{11}
\]

For a longer excursion (`l>=2`) the sharper bound is

\[
\boxed{r\le\frac{81x+605}{1024}<P(x).}
\tag{12}
\]

**Proof.** If the first low scalar occurs at the final even step,
all preceding interior carries are positive. Applying (8) in order
gives

\[
r\le A(F^{l-1}(E(x)))\le A(E(x))=P(x).
\]

If the first low scalar occurs at the penultimate odd step, necessarily
`l>=2`. The same comparison, followed by G, gives

\[
r\le G(F^{l-1}(E(x)))\le G(F(E(x)))
=\frac{81x+605}{1024}.
\]

Here `E(x)>=5/2>c`, so (10) justifies every iterate comparison. In the
first case with `l>=2`, its endpoint is also bounded by the latter
expression, since `A(y)<G(y)` for `y>=0`. Finally

\[
P(x)-\frac{81x+605}{1024}
=\frac{207x-445}{1024}>0
\]

for `x>=3`, and `P(x)<=x/3` is equivalent to `x>=3`. The only
two-step paid excursion is `(1,4)`, and it attains the P map exactly.

The proof also applies to a finite candidate carry path satisfying
(2), positive ordinary states, and the stated first-return pattern.
Its validity does not require that the candidate equals the actual
infinite scalar. Actual equality will be needed for guaranteed return
existence in the next section.

### Independent clock check

For a normalized excursion of length `2*l`, let `K=sum_(i<2l)k_i`
and `G_total=sum g_i`. Telescoping (2) gives

\[
G_{\rm total}=3l+2K.
\tag{13}
\]

For `l=1` one has `K=1`. For `l>=2`, first-return minimality gives
`K>=2l-2`, allowing the penultimate carry to be zero in the second
case above. When all actual source states are at least three, the
complete multiplicative physical equations imply

\[
\frac rx\le\frac{(25/18)^l}{4^K}
\le\frac{625}{5184}<\frac9{32}\quad(l\ge2).
\tag{14}
\]

The middle expression decreases after l=2 because its successive
factor is `25/288<1`. This is a second proof of the strict P majorant
for longer excursions. It uses complete equations, including each
factor `3+1/q_i`, rather than only the homogeneous slope.

## 5. Actual return existence and a finite budget

**R9-C3.** At an actual high state, the potential `W=q/2^h` obeys

\[
\frac{W'}W=\frac{3+1/q}{4^h}<\frac12,
\qquad W\ge\frac12.
\tag{15}
\]

Indeed `q>=3`, `h>=13/8>3/2`, and (1) gives the lower bound. Therefore
an actual high excursion cannot persist forever. If s is its first
high ordinary source and B is its binary bit length, `W(s)<s<2^B`.
There cannot be B+1 consecutive transitions from high states: their
endpoint would have W below one half. The first low state is reached
within B high transitions. Including entry and possible normalization,
the paid excursion has at most `bl(s)+2` odd transitions.

Now start at an actual `h(q)=7/8`. The shifted L identity is

\[
L(q)+7=\frac98(q+7).
\]

Writing `a=v_2(q+7)`, every unpaid L pair reduces a by three. An
exponent a=2 would force a gap at least three at scalar `7/8`; a=3
would force a gap at least two after the intervening scalar `5/8`.
Both violate (1). Exponent a=1 instead gives the required next gap
one into a high state. It follows that

\[
\boxed{v_2(q+7)=3m+1,\qquad m\ge0,}
\tag{16}
\]

and exactly m unpaid L pairs precede the first paid excursion.

Let `B_0=bl(q+7)`. Then `3m<=B_0-2`. If x is the last low boundary
and s the first high state, the elementary size bounds

\[
x+7=(9/8)^m(q+7)<2^{m+B_0},\qquad
s=(3x+1)/2<2^{m+B_0+1}
\]

give the complete normalized-return budget

\[
\boxed{\text{odd transitions from q through the first paid return}
\le2B_0+1.}
\tag{17}
\]

This is a bound for a true supplied scalar equality, not a bound for
termination of the entire ordinary orbit.

## 6. Descent for all paid excursions and the least-source gate

Combine the literal low prefix with R9-C2. Its normalized endpoint
satisfies

\[
r\le P(L^m(q))=A_m(q+7)-29/16.
\tag{18}
\]

**R9-C4 (all-return short-prefix descent).** If `m<=10`, then `r<q`
for every actual paid excursion after that prefix.

For `m=0,1`, `A_m<=81/256`, and the right side of (18) is strictly
below q for every `q>=1`. For `2<=m<=10`, (16) gives
`q=2^(3m+1)u-7>=121` with u positive and odd, so (6) applies. This
separate small-m check matters: general paid excursions need not have
the more restrictive P-only residue `u>=5` used in R9-C1.

Suppose the set

\[
\mathcal S=\{q\in\mathbb Z_{>0}:q\text{ odd and }h(q)=7/8\}
\]

is nonempty, and choose its least element q. R9-C3 supplies a return
to the same scalar set. Minimality and R9-C4 then imply

\[
\boxed{v_2(q+7)\in\{34,37,40,\ldots\},\qquad
q\ge2^{34}-7.}
\tag{19}
\]

Any actual residual denominator-eight source eventually supplies a
member of this set: high carries must exit, and `5/8` immediately maps
to `7/8`. Thus (19) is a necessary least-source constraint on any such
positive ordinary realization. The selected least source is not asserted
to be the source selected by any pressure construction.

## 7. Crossing the binary gate with inverse ternary congruences

Two actual predecessors preserve scalar equality at `7/8`.

If `q=2 mod 9`, then `p=(8q-7)/9` is a positive odd integer with
literal L image q and `p<q`. Hence a least element of the same global
set S must satisfy

\[
q\not\equiv2\pmod9.
\tag{20}
\]

If `3^24` divides `16q+29`, put

\[
u=(16q+29)/3^{24},\qquad p=2^{34}u-7.
\]

The integer u is positive and odd. Formula (5), with m=11, makes
`L^11P(p)=q` a literal ordinary word. Its slope exceeds one and its
additive term in (4) is positive, so `0<p<q`. Its scalar prefix also
preserves `7/8`. Thus a least element of S must satisfy

\[
\boxed{v_3(16q+29)\le23.}
\tag{21}
\]

These inverse constraints are about the global least source with the
specified scalar, so using a smaller predecessor is legitimate. They
are not silently applied to a minimum of a forward orbit alone.

The combined congruences do not contradict ordinary positivity. For
example, every integer

\[
q_j=2^{34}(1+18j)-7,\qquad j\ge0,
\]

has shifted binary valuation 34, is zero modulo nine, and has
`v_3(16q_j+29)=0`. These are controls of the remaining congruence
freedom, not realizations of the scalar equality. Excluding the
unchanged ordinary sources through their later returns remains open.

## 8. A total one-return procedure, and its exact limitation

Given a positive odd q and the candidate `h(q)=7/8`, the following
finite procedure either rejects that equality or returns a new actual
ordinary source r with an equivalent equality:

1. Reject at one, or if the shifted valuation fails (16).
2. Replay literal odd steps with integer candidate `H=8h`, starting at
   H=7 and updating `H'=3H-8g`.
3. Reject if `H<=4`, or if `3H>8bl(q_current)+24`, or if the ordinary
   state reaches one. These are necessary actual-scalar guards.
4. After the first high carry, return at the first H=7, appending the
   forced gap one if the first low state has H=5.
5. Reject if this has not occurred within `2bl(q_initial+7)+1` steps.

R9-C3 proves that a true candidate cannot be rejected. A returned
prefix of length N has the exact actual identity

\[
h(q)-\frac78=3^{-N}\left(h(r)-\frac78\right).
\tag{22}
\]

Consequently the return preserves the equality in both directions,
even when the supplied candidate is false. This is a total one-return
transformer. It is not a total recognizer for the entire denominator-eight
candidate, because repeated returns can increase the physical source
after long low prefixes. The parent expanding examples and R9-C1 rule
out making all such returns descend by assertion.

### Bounded reduction of a supplied denominator-eight candidate

For a supplied candidate `a/(8*3^r)`, with a an integer and `r>=0`,
the representation need not be reduced. If a is divisible by eight,
the candidate is already triadic and can be dispatched to the parent's
finite triadic recognizer. If `a mod 8` is `1,2,3,4,6`, the parent's
complete denominator-two, denominator-four, or upper denominator-eight
phase exclusion rejects it. The remaining residues are 5 and 7.

After r actual odd steps, the propagated candidate has integer
`H=8h` congruent to a modulo eight. A true surviving candidate cannot
hit one. Its high carry must exit within `bl(q_r)` further high
transitions by (15), and at most one forced transition then reaches
scalar `7/8`. Thus reduction to that scalar, or sound rejection of the
supplied equality, has the explicit budget

\[
\boxed{r+\operatorname{bl}(q_r)+1
\le2r+\operatorname{bl}(q_0)+1,}
\tag{23}
\]

because `q_r<=2^r q_0`. This also covers an initially low scalar and
an unreduced extra power of three. Finite backward substitution keeps
the supplied original equality equivalent to the returned `7/8`
equality. `reduce_supplied_candidate` implements this reduction with
the same necessary guards. Its triadic dispatch and `7/8` result are
explicit destinations, not assertions that the candidate was correct.
Repeated `7/8` returns remain the unresolved part.

## 9. Literature, formal scope, and missing step

Riho Terras's *A stopping time problem on the positive integers*,
Acta Arithmetica 30 (1976), 241--252, Definition 0.1, formulates the
stopping target as an actual iterate smaller than its original source.
The [publisher record](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/30/3/101028/a-stopping-time-problem-on-the-positive-integers)
and the indexed opening of the primary paper were inspected. This
motivates the physical-source comparison in (18); no almost-everywhere
or finite-prefix statement is promoted to a universal selector. The
two PDF download endpoints returned HTTP 403, so no uninspected later
theorem of that paper is imported.

The new normalization (7) and the first-return argument are elementary
deductions from the pinned actual scalar and ordinary equations. The
negative-cycle geometry and the finite `(2,1)^m,(1,4)` family were
already present in the parent packet. The contribution is the uniform
comparison over every carry excursion, its finite actual return
budget, and the resulting ordinary least-source constraints.

`CarryReturn.lean` provides finite arithmetic and monotonicity cores.
The real scalar, all-time return attachment, and the full least-source
argument remain written mathematics; the exact formal declarations and
their compilation receipt are listed in the accompanying report.
`carry_controls.py` exposes `run_checks()`, uses exact arithmetic, and
keeps all checks active under optimized Python. Its closed candidate
paths are explicitly distinguished from true infinite scalar equalities.

**First unsupported step:** control the unbounded sequence of actual
returns with long low prefixes, while retaining the same fixed positive
ordinary source. Neither the affine majorant, the binary and ternary
gates, nor the finite one-return procedure currently supplies that
global descent or exclusion.
