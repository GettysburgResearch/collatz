# A least reverse-criterion failure has a bounded fourth valuation

**PROPOSED.** This is a conditional exclusion of all sufficiently large
fourth valuations for one *least failing ordinary antecedent*. It is
not an unconditional proof for every input with those valuations.

Use the ordinary positive shortcut map `T` and its actual basin `C`.
Call an integer `X=128k+1`, `k>0`, `4 ∤ k`, a **failure** when
`X in C` but `(X+1)/2 not in C`. By PR146's deep reverse criterion,
at `e238c63a5d57f96bb063b7472498d1977df51951`, full Collatz fails
if and only if at least one such ordinary failure exists. If so, let
`X_*` be the least one. This minimum is a positive ordinary integer,
and the same `X_*` is used in every implication below.

## H1. An exact height bound for the conditional descent paths

The 71 directed affine certificates in PR146's
`research/upper-bit-mergers/check_deep_reverse_basin.py` use ordinary
edges in either direction and extra arrows `v -> 3v` at positive odd
multiples of nine. They take every odd ternary unit `n>1` to another
positive ternary unit at most `24n/25`.

Replace an extra arrow at `v=9h`, `h` odd, by ordinary edges and the
two adjacent arrows

\[
64h+1\longrightarrow128h+1\longrightarrow256h+1.          \tag{1}
\]

The first uses index `h`, the second index `2h`; both indices are
positive and not divisible by four. To verify the ordinary connections,
`T^6(64h+1)=27h+1` and `T^8(256h+1)=81h+1`. The even endpoints halve
to `T(9h)` and `T(27h)`, respectively. Thus this replaces exactly
the original directed arrow `9h -> 27h` in its required orientation.

The larger upper antecedent in (1) is

\[
A(v)=256v/9+1.                                          \tag{2}
\]

For each source class `n=mt+r`, let `v=at+b` be an eligible tripling
source along its affine path. If `t_0=0`, except `t_0=1` when `r=1`,
the exact supremum of its antecedent ratio on the source domain is

\[
\sup_{t\ge t_0}\frac{(256a/9)t+(256b/9+1)}{mt+r}
=\max\left\{\frac{256a}{9m},
\frac{(256a/9)t_0+256b/9+1}{mt_0+r}\right\}.             \tag{3}
\]

The equality follows because a ratio of two affine functions with
positive denominator has derivative of constant sign. It is not an
estimate sampled at finitely many ordinary source values.

Replaying all 71 affine paths and all 284 eligible triplings gives

\[
\max\frac{A(v)}n=\frac{2025217}{23}<88053.               \tag{4}
\]

The maximum is attained at `t=0` on source class `432t+23`; the
relevant tripling source is `1327104t+71199`, at word position 21
with positions counted from zero. Its upper antecedent is `2025217`
and its original source is 23.

The exact source certificate is copied to
`deep_reverse_certificate.json` with its original SHA-256 and Git
pin. `check_least_failure_height.py` independently checks its complete
ordinary legality, residue coverage, affine contraction, the 284
ratio bounds, and their exact maximum. It does not import the source
author's replay function.

## H2. A proven initial interval under one least failure

Every positive integer `n` satisfying

\[
\boxed{176106\,n<X_*}                                   \tag{5}
\]

belongs to `C`.

First prove by strong induction that every positive ternary unit
`n<X_*/88053` belongs to `C`. The start 1 is already in the basin.
Even units halve. For an odd unit greater than 1, H1 gives a directed
path to a smaller positive ternary unit, which is in `C` by induction.
Every added adjacent arrow on this path has its upper antecedent
strictly below `88053*n<X_*`. By minimality of `X_*`, the implication
from that upper antecedent's convergence to its lower endpoint's
convergence is valid. Reading the directed path backwards from its
certified endpoint therefore proves convergence of the original `n`.
Ordinary edges preserve convergence in both directions. This argument
does not assume convergence of any larger unproved endpoint.

Now strip powers of two from a general `n` satisfying (5), obtaining
an odd `q<=n`. If `3 ∤ q`, apply the unit result. Otherwise `q>=3`
and its ordinary successor `(3q+1)/2` is a ternary unit less than
`2n<X_*/88053`, so it is again in `C`. This proves (5).

Notice that the number 176106 bounds the heights of **conditional
upper antecedents**, not the length or height of an ordinary stopping
certificate for every source.

## H3. The fourth valuation is at most 86

Use K1--K2 of `REVERSE_CERTIFICATE_KERNEL.md` on `X_*`. Put

\[
c=v_2(162k+4),\qquad z=(162k+4)/2^c,
\qquad X_*=\frac{2^{c+6}z-175}{81}.
\]

The values `c=1` or `c>=3` are the only possibilities. Suppose
`c>=3`, and set `r=floor((c-3)/2)`. The actual lower companion
shares a component with the positive integer

\[
R=\begin{cases}
3^r z,&c=2r+4,\\
2\,3^r z+1,&c=2r+3.
\end{cases}
\]

Since the lower companion is not in `C`, neither is this `R`.
On the other hand, in the even case

\[
X_*\ge\frac{849}{81}\,4^r z,
\qquad
\frac R{X_*}\le\frac{81}{849}(3/4)^r<(3/4)^r.
\]

In the odd case, `R<=3*3^r z` and

\[
X_*\ge\frac{337}{81}\,4^r z,
\qquad
\frac R{X_*}\le\frac{243}{337}(3/4)^r<(3/4)^r.
\]

These inequalities use only `z>=1` and `r>=0`, and therefore hold
for the same fixed least failing ordinary source. The exact integers

\[
4^{42}=19342813113834066795298816
>19269340499994115530860154=176106\cdot3^{42}
\]

show that `r>=42` forces `176106 R<X_*`. This contradicts H2.
Consequently

\[
\boxed{c\in\{1,3,4,\ldots,86\}.}                        \tag{6}
\]

The value four is independently impossible for a failure, because
K2 transfers its certificate completely. Thus it may also be removed
from the remaining list.

Keeping the two parity formulas instead of discarding their constants
gives a slightly smaller exact list. Write `H=176106`. In the even
case, `H*R<X_*` holds whenever

\[
(2^{2r+10}-81H3^r)z>175.
\]

For `r=34`, its left coefficient minus 175 is the positive integer
`64338362311137348850935`. In the odd case the sufficient inequality is

\[
(2^{2r+9}-162H3^r)z>81H+175.
\]

At `r=38`, its left coefficient minus the right constant is
`146945227679902514612563>0`. Each comparison persists for all larger
`r`: if `F_r=A*4^r-B*3^r-D>0`, with positive `A,B,D`, then
`F_(r+1)=3F_r+A*4^r+2D>0`. Since `z>=1`, these comparisons exclude
every even `c>=72` and every odd `c>=79`. After removing the solved
case four, the remaining list is

\[
\boxed{c\in\{1\}\ \cup\ \{3,5,\ldots,77\}
                 \ \cup\ \{6,8,\ldots,70\}.}             \tag{7}
\]

## H4. A least failure cannot have upper odd rank four

If the upper first-hit odd rank is four then `z=1` in K1. The
congruence `2^(c-2)z ≡ 1 (mod 81)` forces `c=54j+2`, `j>=1`, as
already established in PR146. Bound (6) leaves only `c=56`, `j=1`.
Its lower companion shares a component with `3^26` by K2. The
standalone checker verifies the complete actual ordinary trajectory
of `3^26` to 1: 219 shortcut clocks, with 112 odd inputs and peak
16286310253592. Hence this remaining case is not a failure either.

Hence any least failing upper antecedent has first-hit odd rank at
least five. This does not assert that every rank-four implication
has now been proved: a larger failure of rank four is excluded only
if it were the first failure. The theorem concerns the minimum of
the entire failure set, not a separate minimum within each rank.

## H5. Two complete rank-five families cannot contain the least failure

The same fixed least-source argument eliminates the rank-five cases
`c=1` and `c=3` from K3, in addition to the already solved `c=4`.

For `c=1`, put `a=162j+70`, `j>=0`. Its residual pure power is
`P=3^(81j+32)` and

\[
243(X_*-176106P)
=2^{162j+77}-653-243\cdot176106\cdot3^{81j+32}>0.          \tag{8}
\]

At `j=0`, the difference on the right is exactly
`71818029920988665229141`. Its positivity persists for all larger
`j`, since the positive exponential grows by `4^81` while the
subtracted exponential grows by `3^81`; the fixed positive
subtraction 653 is also dominated. Thus `176106P<X_*`, so H2
certifies `P`, contradicting a failure.

For `c=3`, the residual is `P=3^(81j+10)` and the corresponding
difference is

\[
243(X_*-176106P)
=2^{162j+31}-1037-243\cdot176106\cdot3^{81j+10}.           \tag{9}
\]

It is already positive at `j=1`, with exact value
`12554202350266279230985313864847138776593601623775633598729`,
and persists by the same growth comparison. The remaining `j=0`
case has residual `3^10`; its complete ordinary path reaches 1
in 89 shortcut clocks with 46 odd inputs and peak 1135052.

Consequently a least failure of upper rank five, if one exists,
must have `c>=5` in the finite list (7). No proof for all those
remaining rank-five families is inferred from the exclusions.

## What still has to close

The remaining finite list of fourth valuations still has an unbounded
ordinary parameter `z` and an unbounded input stopping certificate.
An exact remaining task is to produce, for each actual residual `R`,
a finite path to the already certified `z`, or to an integer below
`X_*/176106`, using only ordinary edges and eligible adjacent arrows
whose upper antecedents stay strictly below `X_*`. The path length
may depend on the numerical source and its supplied certificate.
A universally successful such construction would contradict
minimality and prove Collatz.

No such construction is supplied here. Merely having a finite list
of valuations does not make the remaining integer domain finite or
provide a uniform path-length bound. In particular a finite atlas
of bounded words is a stronger, separate requirement. The source's
conditional descent paths cannot simply be reused at a height where
their antecedents exceed `X_*`.
