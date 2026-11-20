# Independent review of the three-family positive renewal

**VERIFIED at the stated internal-review scope.** This is a reconstruction
of the written elementary argument, plus a separate exact rational audit.
It is not external referee acceptance, formal proof-assistant verification,
or a proof of finite uncovered energy.

Reviewed source:

* `research/global-forcing-20261121/energy/COUPLED_RENEWAL.md`;
* SHA-256 `1ac74226cc170ca3000ccd24359093dc9c2d652db1a23d323211f4b4f90ada11`;
* claims CR1--CR3, including the full unbounded safe carry domain.

The reviewer authored the neighboring carry identities, but independently
reconstructed the energy proof and its constants. The energy author did
not author the carry compiler. The separate source dependencies in PR166
are credited in the reviewed note; the estimates needed from them are
also reconstructed below. The calculation originally checked hash
`8a260dad90395adce8dd36cfe68abcd0721715f8bd95bd02f3952cbd77d4a16f`.
The final version deletes only the word "two" from its first-line title;
reversing that one edit reproduced the original hash exactly. Thus all
reviewed mathematics and constants are unchanged. This review does not
extend to subsequent changed bytes.

## Ordinary domains and endpoint accounting

For an ordinary-invariant metric label, each physical block gives exactly
`e(x)=e(q)`, not merely an average inequality. In every block the output
`q` is positive, odd and a ternary unit. The known path `5->1` gives
`e(1)=0`. Therefore every nonzero endpoint contribution has `q>=5`.
No density or random-residue hypothesis is needed.

The three source domains really are disjoint. The old ladder starts with
a nonempty run of valuation two and then a valuation at least four. The
short new block starts with three valuation-one steps. The carry family
starts with `2,1`. Within the carry family, the number `r` of consecutive
ones after the fixed entry is uniquely determined by the source, since
the next valuation is exactly three. Thus inverse summation does not
count one source several times under different runs.

The full carry theorem permits every `b>=2`. CR3 explicitly restricts
to `b>=r+2`. This is essential to the stated height and kernel estimates;
the proof does not assign them to the larger domain.

## The inverse kernels

For the old ladder, the exact source is

\[
 x=1+(4/3)^r(2^bq-4)/3.
\]

At a fixed endpoint and run, integrality forces one exponent class of
period `2*3^r`. Increasing the exponent by that period increases `x`
by more than its corresponding power-of-two multiple, because the
constant subtracted from the leading term is positive. For `q>=5`,
the lower bounds on `x/q` are `(4/3)^r*76/15` for `b>=4`, and
`(4/3)^r*52/5` for `b>=5`. These reproduce the two weights used in
CR2--CR3. The source-unit condition deletes fibers and cannot enlarge
the sums.

For the short block, the correction `65` gives
`x=(2^Lq-65)/81`, with `L>=9`. Integrality selects one class of
period 54. Its lower ratio is `499/81`; if `q=7 mod27`, the same
integrality forces `L=15 mod18`, improving it to `32755/81`.
The source is at least 271, and direct substitution gives `q<x/6`.

For the carry family, independent substitution of the entry, one-run,
and exit gives

\[
 x=\frac{2^{r+b+18}}{3^{r+9}}q
   -\frac{1351}{81}
   -\left(\frac23\right)^r\frac{65536}{19683}.
\]

With `b=r+2+delta`, `delta>=0`, and `q>=5`, the bound in the source is
correct:

\[
 x/q\ge\frac{4849051}{98415}(4/3)^r2^\delta,
 \qquad \frac{4849051}{98415}>49.
\]

Indeed its constant is exactly
`2^20/3^9-(1351/81+65536/19683)/5`. The discarded subtraction only
decreases as `r` grows, whereas the factor multiplying the displayed
constant is at least one. At fixed `r,q`, the legal exponent class has
period `2*3^(r+8)`. The same positive affine-offset calculation proves
the geometric ratio bound. There is no reset to an unconditioned source
distribution.

## The common endpoint constraint and the infinite run sum

The carry correction is
`1351*3^(r+5)+2^(r+16)`. Reducing its exact inverse congruence modulo
27 and dividing by the unit `2^(r+16)` gives directly

\[
 2^{b+2}q=1\pmod{27},\qquad 2^bq=7\pmod{27},
\]

for **every** `r>=0`. This also independently checks the note's separate
last-three-letter argument at `r=0` and `r>=1`.

Let `b_0` be the corresponding residue modulo 18. The first allowed
excess satisfies `delta>=(b_0-r-2) mod18`. Using the stated rational
upper bounds for `(3/4)^(21/25)` and `2^(-21/25)`, grouping the entire
sum over `r>=0` by its residue modulo 18 gives exactly the finite
polynomial divided by `1-(393/500)^18` in equation (16). This step
accounts for all unbounded run lengths, rather than truncating them.

The endpoint cases exhaust the ternary units. The three residues
`7,16,25 mod27` are exactly those congruent to seven modulo nine.
Their carry exit residues are respectively `0,12,6 mod18`. Outside
those classes, even the old ladder's first run cannot use last gap
four. Thus the three different joint upper bounds use compatible
constraints at one actual endpoint; they do not add mutually
incompatible worst cases.

## Exact arithmetic reconstructed independently

A separate Python calculation using only `fractions.Fraction` and
integers, without importing the author's checker, performed **44 exact
checks**. The source hash was checked before calculation. These checks
included:

* all seven rational power bounds, after clearing positive denominators
  and taking the 25th power;
* the harmonic interpolation inequality `5^25<6^4*4^25`;
* the carry ratio constant and both inherited old-ladder constants;
* all 18 endpoint congruence classes and the three-case partition;
* the three finite geometric-polynomial bounds, respectively below
  `1/300`, `1/8`, and `1/8`;
* the three combined kernel comparisons and the finite-energy factor.

The recomputed maximal subcritical coefficient is

\[
 \frac{330293}{331700}+\frac1{300}
   =\frac{248549}{248775}<1.
\]

The second case gives
`8865224/10365625+1/8`, and the third gives
`1026910336/1086897975`; both are strictly smaller than the displayed
maximum. Its reciprocal gap is exactly `248775/226`.

These are finite exact arithmetic checks of the printed constants.
The infinite-fiber and infinite-run quantifiers are supplied by the
geometric arguments above. No additional large search was run.

## Finite cutoffs and the remaining mathematical input

For each nonzero contribution, all three domains have `q<=x/6`.
Multiplying the endpointwise inverse-fiber inequality by `e(q)` and
summing positive terms therefore proves the claimed cutoff `X/6`.
The harmonic estimate follows by multiplying each subcritical ratio
by `(q/x)^(4/25)<=6^(-4/25)<4/5`. This remains valid before any
summation or limiting operation.

At finite `X`, every metric energy sum is finite. Replacing
`E_s(X/6)` by `E_s(X)` and subtracting the resulting **finite** quantity
is valid. Monotone passage to larger cutoffs proves precisely the
stated equivalence between finite total energy and finite uncovered
energy. It never subtracts two infinite sums.

The unresolved premise remains finiteness, or another adequate bound,
for the full complementary energy `Q_s`. The conditional finiteness
equivalence does not establish that premise. The grade obstruction in
the separate phase note involves known zero-defect inputs, and supplies
no refutation of this defect-energy argument.
