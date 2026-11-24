# A physical descent completes this guard comparison

For every natural \(r\), the ordinary source

\[
n=768r+295
\]

has the exact shortcut descent

\[
\boxed{T^8(n)=729r+281<n.}
\]

The decrease is \(39r+14\). This is a direct specialization of the checked
`CertificateBoundary.boundary_seven` theorem, with \(v=3r+1\):

\[
n=256(3r+1)+39,\qquad
T^8(256v+39)=243v+38.
\]

No source certificate, convergence premise, marked-band premise, or residue
exclusion on \(r\) is needed. Consequently this family is discharged by
ordinary value induction. It is **not** a remaining global Collatz family.

## Why a comparison of static guards alone misses this conclusion

Set

\[
p=24r+9,\quad q=4p+1=96r+37,\quad
S=4q=384r+148,\quad n=2S-1.
\]

Three independently useful filters leave these displayed inputs visible:

1. **The new source reset excludes this sibling.** Since \(3\mid p\), the
   `second_even_source_reset` guard fails. No nonempty positive odd-gap prefix
   can end at \(p\), because its last edge would give
   \(3z+1=2^a p\), impossible modulo three. This concerns that one
   source-certificate rewrite, not all possible source transformations.

2. **The four-valuation necessary cover permits it.** Exactly
   \[
   9n+1=32(216r+83),
   \]
   so \(v_2(9n+1)=5\). The four classes in `MergerDispatch.lean` are a
   necessary cover of possible no-descent sources. They are not the exact
   set surviving every eight-step descent test. The present class illustrates
   the difference.

3. **The listed initial-run diamonds do not apply directly.** In PR185 at
   `6d2765ef462fb575c49d4133b54286be7ffe68ec`, the relevant source files are
   `research/literature-orbit-closure-20261121/lean/HalfSourceMerge.lean` and
   `LongDiamondErasure.lean`. Here \(n+1=8q\), with \(q\) odd, so the maximal
   initial odd run has length three. The two-clock half-source test would
   require \(9q\equiv3\pmod4\), but \(9q\equiv1\pmod4\). The eight-clock
   half-source test would require
   \[
   9q=864r+333\equiv185\pmod{256},
   \]
   impossible already modulo 32. The quarter-source test would require
   \[
   3q=288r+111\equiv147\pmod{256},
   \]
   also impossible modulo 32. The eighth-source theorem requires an initial
   run of at least four, which this family does not have.

This checks only the specified direct guards. It is not a claim about every
PR185 mechanism, later orbit positions, or arbitrary common-future partners.
The unconditional eight-step descent above settles the family regardless.

## One fully supplied certificate example

At \(r=1\), the values are

\[
p=33,\quad q=133,\quad S=532,\quad n=1063.
\]

The source \(q\) has the complete odd-gap certificate
\([4,2,1,3,1,2,3,4]\), all in the low alphabet \(1,2,3,4\).
The sibling \(p=33\) is excluded by the new predecessor guard, but the wanted
ordinary source satisfies

\[
T^8(1063)=1010<1063.
\]

This explicit certificate is supplied only for the displayed instance. The
guard calculations make no claim that every \(q=96r+37\) is already known
to have a complete certificate.

## A contrasting finite frontier

Keeping the same \(p,q,S\), change only the wanted target to

\[
\widetilde n=32p-1=768r+287=256(3r+1)+31.
\]

This lies in the original source interval, above \(S+1\). Its exact
valuation is

\[
9\widetilde n+1=8(864r+323),\qquad
v_2(9\widetilde n+1)=3.
\]

The first eight shortcut states of the base residue 31 are
\(47,71,107,161,242,121,182,91\), with cumulative odd counts
\(1,2,3,4,5,5,6,6\). The affine lifting identity therefore shows that every
one of the first eight states of \(\widetilde n\) is larger than
\(\widetilde n\). In particular,

\[
T^8(\widetilde n)=2187r+820>768r+287.
\]

Here \(\widetilde n+1=32p\), with \(p\) odd, so the maximal initial odd run
has length five. The direct two-clock half-source guard still fails. The
eight-clock half-source and quarter-source guards now become, respectively,

\[
81p=1944r+729\equiv185\pmod{256},
\]

\[
27p=648r+243\equiv147\pmod{256}.
\]

Each is equivalent to \(r\equiv20\pmod{32}\). The eighth-source guard
would require \(9p=216r+81\equiv147\pmod{256}\), which is impossible
modulo eight. Thus, outside \(r\equiv20\pmod{32}\), none of these listed
direct diamond guards applies. This still says nothing about other physical
mergers, later visits, or the other PR185 constructions.

At \(r=1\), the already supplied source \(q=133\) and its complete word
\([4,2,1,3,1,2,3,4]\) now accompany the wanted target \(1055\), within
the source interval ending at \(1065\). Every coefficient prefix of the
supplied source word is below one, so the noncontracting-source-prefix rule
does not immediately remove this query either.

Two independent exact integer Python replays found that the first strict
ordinary descent of \(1055\) occurs at shortcut clock 80:

\[
T^{80}(1055)=628<1055,
\qquad T^j(1055)\ge1055\quad(0\le j<80).
\]

This is a bounded replay, **not a separately checked Lean theorem** in this
packet. The initial states are
\(1055,1583,2375,3563,5345,8018,4009,6014,3007\).
The arithmetic phase calculations in this section were also independently
checked; they are not new exported Lean declarations.

The example is an exact frontier for the specified direct tests and explains
why their union is not yet a complete dispatcher. It is a convergent,
explicitly descending example, not a counterexample to Collatz. No claim is
made that all source values \(q=96r+37\) have already supplied certificates,
that every member has the same first-descent clock, or that no stronger
uniform rule can handle the family.

## Consequence for the combined attack

Failure of a static inverse-prefix or diamond guard must be followed by a
check of the available physical descent identities before calling a class a
remaining problem. In this instance the composition succeeds for the whole
unbounded ordinary family, even though the listed symbolic guards fail.

The source-rank program still has other uncovered low-alphabet queries.
This audit establishes one exact family of native descents; it supplies
neither a universal common rank nor a complete global selector.
