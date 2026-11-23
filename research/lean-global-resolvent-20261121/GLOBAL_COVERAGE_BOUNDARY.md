# Final global coverage assessment

**No all-case selector or primitive-moment decay proof was obtained.**
This final pass identified an entrance-independent low-valuation obstruction
for the current fixed exit, and a genuine certificate-order obstruction for
the proposed shifted exit. Earlier frozen analytical and Lean files are
unchanged.

## The present exit cannot cover low ternary valuation

Put P=2^e with e odd and h=v3(e+1). Every use of the current
`target=2*source+1` middle and its certified exit requires

\[
2P-1=3^{\ell+2}w,\qquad w>0\text{ an integer}.
\]

The lifting identity gives v3(2P-1)=h+1. Consequently

\[
\ell\le h-1.
\]

This restriction is independent of the entrance, its odd count, or its
rational negative anchor. In particular h=0 is impossible even if the
entrance dictionary is allowed to grow without bound. These h=0 cases
include every positive odd exponent e=1 or 3 modulo 6. Enlarging only the
normalized-unit coverage of that same fixed exit cannot close the full
family. The stronger depth threshold of the presently compiled entrance
leaves additional cases uncovered.

For proper rational-anchor entrances one has the more specific selector
ell=h-1-v3(C_s+2^A), when v3(C_s+2^A) is smaller than the entrance's odd
count. That exact selector must not be used without its qualification:
otherwise cancellation in 3^r*m+(C_s+2^A) can change the valuation. The
entrance-independent inequality above has no such caveat.

## The shifted exit is an ancestral insertion

The proposed alternative with 81v=32P-31 uses source 2v-1 and target
16v-1. Its source prefix reaches

\[
H=\frac{27v+5}{16}=\frac{2P-1}{3},
\]

and then visits P, P/2, P/4. Its target reaches P-1. The source division
lengths (2,2,1,3) describe this partial ordinary prefix; the final three
divisions need not exhaust the valuation because P/4 can be even. The
target word (1,1,1,6) is an exact accelerated word.

Thus the new source certificate contains the entire old certificate from
P/2 as a suffix. This is stronger than failure of a particular numerical
bound. Any order that strictly decreases when consuming an ordinary source
prefix must rank the old suffix below the newly prefixed certificate.
Ranking the reset in the opposite direction would create a cycle in the
supposed well-founded relation. Changing weights cannot repair that while
retaining the stated consumption property.

An independently derived y=2x+1 version has 27v=32P-31: source 2v-1
uses exact initial valuations (4,1) to reach the same H, then visits
P,P/2,P/4; target 4v-1 uses (1,2,4) to reach P-1. It has the same
ancestral obstruction. Neither variant is a new decreasing reset.

## A possible normalization refinement, not a closing move

For an even initial source n define a marker which agrees with its least
positive odd predecessor on ternary units, and is set to n on multiples of 3:

\[
H(n)=\begin{cases}
n,&3\mid n,\\
(2n-1)/3,&n=2\pmod3,\\
(4n-1)/3,&n=1\pmod3.
\end{cases}
\]

Consider a multiset containing all odd states before the supplied hit,
H(n) if the initial source is even, and one zero-valued token per remaining
ordinary clock. This is a possible refinement of the separately compiled
odd-state measure. Its ordinary consumption checks are elementary:

- Odd-to-odd consumption removes the old odd state and one zero token.
- Odd-to-even consumption replaces that odd state by the equal marker
  H(Tn)=n and removes one zero token.
- Even-to-odd consumption removes the initial marker and one zero token.
- For an even-to-even halving n=2m, H(n) is respectively 2H(m), H(m), or
  4H(m)+1 as m is 0, 1, or 2 modulo 3. The marker never increases and a
  zero token is removed.

Each case strictly decreases the Dershowitz--Manna multiset order. A
strictly smaller positive replacement marker can also pay for arbitrarily
many newly added zero tokens in a longer reset. For the current good
resets, their bound below P/2 is stronger than the resulting bound below
H(P/2)=(2P-1)/3. This refinement could therefore help assemble normalization
and resets under one order.

It does not rescue the shifted exit: that exit inserts H(P/2) itself and
then the complete old suffix. The refinement is only a written observation
in this final pass; it has not been substituted into a compiled global
compiler, and it supplies no missing reset on the uncovered cases.

The actual remaining requirements are an entrance covering the remaining
normalized unit classes and genuinely non-ancestral decreasing transitions
for low h, or another global argument. Neither was proved here.

These are coverage requirements within this reset approach. Closing the
power-of-two boundary alone would still leave the all-state rule-selection
obligation for the other source/relation states identified in
[BROAD_RESET_AND_COVERAGE.md](BROAD_RESET_AND_COVERAGE.md).
