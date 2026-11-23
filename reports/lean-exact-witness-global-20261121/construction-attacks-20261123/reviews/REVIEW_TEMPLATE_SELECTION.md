# Independent review: all actual rational templates and the power gap

23 November 2026. Reviewer: the finite-mass research lane.
**VERIFIED at the written, source-qualified scope of TS-A, TS-B, TS-C,
TS15--TS20, with an independent exact finite continued-fraction replay.**
The verdict does not establish a universal paid selector, exclude positive
cycles, or resolve an escaping ordinary trajectory.

## Frozen objects and independence

The reviewed files lie in
`research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/`:

| File | SHA256 |
| --- | --- |
| `TEMPLATE_SELECTION.md` | `90682f31bb3fa4a7d39ac779b9c4c749a1cc37c3bffa2a2a56b5e023a1d164d2` |
| `TemplateSelection.lean` | `1b6244a88168434637780507660bce382135caeeb65ad8242172bc95b0b47715` |
| `check_template_selection.py` | `12919fec4e6a42e2fca22e4fe38b2814eae64928dcc017e02715185f08c8b798` |

The publication parent is PR177 at
`3124c03a6a672cb70cdd5604eaf2d4eb19a467e3`; the present review binds the
new local contents by the hashes above. In particular it includes the
`c>0` hypothesis in the generic power-lifting inequality and TS-C's
coefficient-to-descent window.

The reviewer did not author this argument or supply the complete-carry
bound. The proof, quantifiers, actual-source interpretation, and finite
range were reconstructed independently. The additional replay script
does not import the author's checker and does not repeat its word census.
The external logarithmic-form theorem is a published input whose exact
application is reviewed; its full proof is not re-proved here.

## Primary theorem and large-exponent range

The reviewer opened the original English
[Matveev PDF](https://www.mathnet.ru/links/11696330cc866d273c92c771a63da235/im314_eng.pdf)
through the cached primary source and read Section 1's parameter
definitions and Section 2's theorem statements, printed pages 1218--1219.
Corollary 2.3 permits the coefficient maximum `B*` from (1.4), and the
second choice in (2.6) is `2^(6n+20)`. This is a statement-level source
check, not an independent verification of the paper's proof.

For the actual use, the number field is the rationals, degree one; the
two positive algebraic numbers are two and three. Their absolute
logarithmic heights and selected logarithms give admissible
`A1=log2`, `A2=log3`, both greater than 0.16. Unique factorization makes
`Lambda=L log2-p log3` nonzero. The height product is less than one.
Consequently the corollary indeed gives the weaker bound

`log|Lambda| > -5*10^9*(1+log(max(L,p)))`.

No bound for `exp(Lambda)-1` has been silently substituted for a bound
for the linear form itself: this corollary directly concerns `Lambda`.
The specialization loses constants in a safe direction.

For fixed positive p it is enough to use the least L with `2^L>3^p`.
This L is at most `2p`. Failure of TS6 gives

`0 < Lambda < (3/2)*2^(-p)`.

For `p=Tt`, `T=10^12`, `t>=1`, the manuscript's comparison reduces to

`(T/2-5*10^9)*t-150*10^9-1 >= 345*10^9-1 > 0`.

The bounds `log2>1/2`, `log(3/2)<1`, `log t<=t-1`, and
`log(2T)<30` suffice. The last follows from the exact comparison
`(8/3)^30>2T` and the elementary series bound `e>8/3`. Thus all
`p>=10^12` are excluded; the finite certificate is not being used as
an extrapolation to that infinite range.

## Independent complete finite range

For `p>=5`, failure implies

`|log_2(3)-L/p| < 1/(2p^2)`.

The sufficient inequality `2^p>(9/2)p` has the valid base p=5 and is
preserved on incrementing p. Reducing `L/p=a/b` gives `p=tb`, `L=ta`
with positive integer t, and `b<=p`. Therefore the same approximation is
strictly better than `1/(2b^2)`, so Legendre's theorem applies to the
reduced fraction. The reviewer also read the exact reduced-rational
statement `Real.exists_rat_eq_convergent` in the pinned Mathlib source;
it has precisely this hypothesis.

The independent script [review_template_cf.py](review_template_cf.py)
computes the 128-term logarithm enclosures by iteratively updating the
odd powers. Its strict remainder bound follows from the geometric series
and the increasing odd denominators. It then certifies, one at a time,
that each transformed interval lies strictly between the listed partial
quotient and its successor. The recurrence's determinant is also checked
to have absolute value one, retaining reduced convergents.

All 26 digits in the manuscript are certified. The last denominator below
the cutoff is `753110839881`, and the next is `5409303924479`. Denominators
increase after the initial denominator-one entries; the interval replay
therefore covers every relevant convergent with denominator below the
cutoff. It does not merely check a selected list of good approximations.

The upper convergents in the finite range separate as follows:

| Reduced fraction | Treatment |
| --- | --- |
| `2/1` | Exact power-gap base and the power-lifting argument |
| `8/5`, `65/41` | Direct exact lower bound exceeding `(3/2)*2^(-b)` |
| All remaining upper convergents below the cutoff | Exact lower bound exceeding `2^(-100)` |

For the third row, `b>=102` gives
`2^(-100)>(3/2)*2^(-b)`. The independent replay checks the limiting
comparison at b=102 explicitly. For every positive multiplier t,

`t*(a log2-b log3) > (3/2)*t*2^(-b) >= (3/2)*2^(-tb)`.

Thus reduction to lowest terms has not lost the cases with a common
factor in L and p.

For `2/1`, the generic power-lifting step is valid as now stated. From
`X,Y>=a>=1` and `c>0`, the geometric sum is positive and is at least
`sum_(k=0)^(t-1) a^k`. Multiplying the strict base-gap inequality by this
sum gives the claimed strict inequality, including the edge case a=1.
The choice `(X,Y,a,c)=(4,3,3/2,3/2)` covers every multiple. The explicit
small exponents p=1,2,3,4 are also checked with their minimal lengths and
exact gaps. These are all the finite cases.

The independent execution was:

```sh
python -X utf8 -B reports/lean-exact-witness-global-20261121/construction-attacks-20261123/reviews/review_template_cf.py > reports/lean-exact-witness-global-20261121/construction-attacks-20261123/reviews/template_cf_review.json
```

Working directory: the complete `collatz-lean-global` checkout. Observed
exit code: **0**. The saved [exact result](template_cf_review.json) says
`PASS` and includes the reviewed source hashes and all 26 convergents.

| Independent replay artifact | SHA256 |
| --- | --- |
| `review_template_cf.py` | `a28ad268a1ae320ed7a3b0e48ea6e6240c88539610cbd1c3f058906638a39f7c` |
| `template_cf_review.json` | `42e38750ff0036da786cdefe5648cd4369b8c4440b1e6e7b0bc8798587f05aa1` |

## Carry bound, actual source lattice, and TS-A/TS-C

For the chronological two-letter actions, replacing `10` by `01`
changes `(3x+1)/4` to `(3x+2)/4`. A suffix multiplies this difference by
a positive number. Sorting zeros before ones therefore maximizes the
complete carry while preserving L and p, giving

`C <= 2^(L-p)*3^p-2^L`.

This maximum is over formal parity words; intermediate sorted words need
not be legal at the original source. That does not affect this algebraic
bound. Ordinary legality is separately and correctly used for the source
lattice. Combining this carry bound with TS-B gives a strict center bound
`c/d<2Q/3` whenever `P<Q`, including p=0 separately.

For an actual endpoint y, the exact fixed-point identity implies
`Q*(dy-c)=P*(dx-c)`. Since P and Q are coprime, `Q` divides `dx-c`.
A nonintegral reduced center has an odd denominator at least three and
cannot have zero displacement at an integer source. For x<Q its absolute
displacement is therefore at least Q, hence greater than x. For x>=Q,
the center bound gives

`dx-c > d*(x-2Q/3) >= 3x-2Q >= x`.

An expanding word has a negative center, so its nonintegral displacement
is directly greater than x. Zero carry gives only the integral center
zero. This establishes every branch of TS-A without replacing an actual
ordinary source by a rational point or a binary completion.

TS-C is also valid: a contracting affine map moves a source strictly
toward its fixed center, and `x>=2Q/3>c/d` puts that center strictly below
x. This is a finite window statement. It does not assert that a first
contracting prefix occurs soon enough to satisfy that window.

## Exact finite rank and cycle equivalence

The one-step actual prefix supplies a nonzero score at most x+1. The
source lattice makes every nonzero score at least `2^L`, so every
minimizer occurs within `L<=floor(log_2(x+1))`. There is one actual
prefix per length. This proves complete finite evaluation, not just a
bounded approximation. For properness, `|c|<=C<3^L`, `d>=1`, and the
triangle inequality give the stated finite sublevel bound.

The elementary rank phi is supplied residue by residue: centers zero,
one, two and minus one work for x congruent to zero, one, two and three
modulo four, respectively. At x=1 and x=2 the one-step scores give the
separately defined value two. Nonintegral templates have score greater
than x; even when phi equals x+1, integrality of the score prevents a
strict improvement. Negative centers and center zero also cannot improve
phi under their actual-prefix conditions.

A positive integer formal fixed center is a genuine ordinary cycle
point: reduction modulo two recovers the first prescribed branch; the
remaining affine equation after that branch recovers the next, and so
on. Every intermediate ordinary value remains positive. Centers one and
two have the alternating ordinary orbit and yield only the existing
scores. Thus a strict improvement necessarily supplies a nonstandard
positive cycle center greater than two.

Conversely, if c>2 is such a cycle point with word length L, then L>=2.
The integer `x=c+2^L` has the same full length-L parity prefix, has
nonzero displacement `2^L`, and satisfies
`phi(x)=2^L+phi(c)>2^L`. This proves both directions of TS19. The
equivalence concerns cycles only; an escaping trajectory has not been
excluded by this rank calculation.

## Supplied-witness compiler and formalization boundary

From a complete actual word x to one, `Q=Px+C` gives
`d=Q-P=P(x-1)+C`. For x>1 and Q>2, this integer d is at least two.
The unreduced center is permitted by the inherited paid-macro format.
Its complete changing-center carry is
`F=C-(Q-P)=-P(x-1)`, and therefore

`P+|F|=Px<=Q<Qd`.

The source displacement is exactly `Q(x-1)` and the target displacement
is zero. The sole actual Q=2 termination word is the even step from two
to one; adjoining the actual `10` cycle changes Q to eight and removes
the strict-budget exception. The source-one case starts at zero rank.
TS20 is consequently a valid compiler of a supplied complete witness.
It contains no procedure constructing that witness from an arbitrary
input or constructing a witness for `(x+1)/2` from one for x.

The 13 Lean declarations were inspected against these finite algebraic
claims. They keep their center/carry estimates as explicit hypotheses;
the imported logarithmic-form theorem is not inserted as a custom axiom.
This reviewer did not repeat the author's strict Lean run or ordinary
word census. Their execution receipts remain separate evidence. The
independent computation in this review is exactly the finite CF replay
documented above.

No further scientific correction was required at the frozen hashes.
