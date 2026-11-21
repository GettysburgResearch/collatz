# Retaining two initial halvings after an eightfold source

This note accompanies `lean/Collatz/RetainedEvenReset.lean`. It proves a
whole-witness reduction inside the low-gap interval boundary. It does not
assert that the remaining interval cases close.

## The exact source replacement

Let a supplied certificate represent the known source

\[
S=8q
\]

with its complete odd certificate `tail` for \(q\). Assume that \(q\) is a
ternary unit and that

\[
q\ne1,\qquad q\not\equiv7\pmod9,\qquad
q\not\equiv19\pmod{27}.
\]

There is an ordinary predecessor \(p\ge2q\) of \(q\), given by exactly one
of the following four formulas. The word is written in forward order from
\(p\) to \(q\).

| Condition | Word | Exact identity |
| --- | --- | --- |
| \(q\equiv2\pmod3\) | `[3]` | \(3p+1=8q\) |
| \(q\equiv4\pmod9\) | `[3,2]` | \(9p+11=32q\) |
| \(q\equiv10\pmod{27}\) | `[3,2,2]` | \(27p+65=128q\) |
| \(q\equiv1\pmod{27},\ q>1\) | `[2,2,2]` | \(27p+37=64q\) |

These four cells cover all the stated hypotheses. Each formula gives a
nonnegative integral \(p\), and its identity implies \(p\ge2q\).
For the last row, \(q>1\) and \(q\equiv1\pmod{27}\) give \(q\ge28\).

The replacement source is

\[
S'=4p\ge8q=S.
\]

Its complete supplied witness is the initial halving run of length two,
followed by the table's word and the unchanged literal `tail`. The existing
prefix compiler proves the complete certificate, including ordinary-path
legality. This is a transformation of the supplied witness, with no search
for a fresh convergence certificate.

## Strict rank decrease and the target interval

The multiset rank assigns grade \(2e+1\) to a positive initial halving run
of length \(e\), and grade \(2a\) to each odd gap \(a\).
The old initial run has grade seven. The replacement has initial grade
five and only new odd grades at most six. Every old tail grade is retained.
Consequently

\[
\Gamma(2,\mathrm{word}\mathbin{++}\mathrm{tail})
 < \Gamma(3,\mathrm{tail}).
\]

Because \(S'\ge S\), every target satisfying

\[
0<t\le2S+1
\]

still satisfies \(0<t\le2S'+1\). The target itself is unchanged. No bound
on the length or exponents of the supplied tail is needed.

The Lean theorem names are:

- `CollatzRetainedEvenReset.doubling_prefix`
- `CollatzRetainedEvenReset.retained_even_rank`
- `CollatzRetainedEvenReset.whole_witness_interval_reset`

The module was checked with Lean 4.34.1 and `-DwarningAsError=true`.

## Meaning of the excluded cells

The exceptions are exact obstructions for this particular construction:
an ordinary predecessor at least \(2q\), using only gaps at most three.
The following converse explanation is written mathematics; the Lean module
proves the positive cover and the whole-witness reduction above.

For an odd endpoint \(q\equiv1\pmod3\), an inverse odd gap at most three
can only be two: integrality requires \(2^a q\equiv1\pmod3\), so \(a\)
must be even. The unique predecessor is \((4q-1)/3\).

If \(q\equiv7\pmod9\), that predecessor is divisible by three, and no
further odd predecessor exists. Its value is less than \(2q\).

If \(q\equiv19\pmod{27}\), the first predecessor is congruent to seven
modulo nine. The only possible second predecessor is
\((16q-7)/9\), which is divisible by three and still less than \(2q\).
The reverse path ends there.

For \(q=1\), the only gap at most three is two, returning to one.
Thus none of the excluded endpoints admits a predecessor of the required
size with this gap alphabet. This does not rule out another rewrite that
consumes part of the supplied tail, changes the target by a proved basin
equivalence, or uses a different rank reduction.

## Closing the length-one, first-gap-four boundary

The separate module `lean/Collatz/RetainedEvenBoundary.lean` supplies a
second reduction, with no residue or tail restriction. Suppose the known
source is \(S=2q\), and its supplied odd certificate starts with a gap
\(a\ge4\). Then

\[
q=4p+1,\qquad p>0,
\]

and the complete certificate for \(p\) has first gap \(a-2\), followed
by the same literal tail. Use the child source

\[
S'=8p=S-2.
\]

The old initial and first-gap grades are \(3,2a\). The corresponding
child grades are \(7,2a-4\), both less than \(2a\), so the child has
strictly smaller multiset rank.

Every odd target in the original interval except its two largest odd
values already lies in the child interval. The two boundary targets close
by explicit ordinary transports:

\[
16p+3
 \xrightarrow{\text{gap }1}24p+5
 \xrightarrow{\text{gap }3}9p+2,
\]

and \(9p+2\le16p+1=2S'+1\). The uppermost target is
\(16p+5=4q+1\), which has the same basin membership as the already
certified odd value \(q\). Even targets are handled by halving the known
source once and halving the target once; that child also has strictly
smaller rank and remains in the interval.

Consequently, this case closes **every target** \(0<t\le2S+1\) from
the common lower-rank interval induction hypothesis. In particular, it
removes the entire initial-length-one, leading-gap-four cell from the
low-alphabet residual. The first gap and suffix length remain unbounded
in the formal theorem.

The second module's theorem names are:

- `CollatzRetainedEvenBoundary.sibling_certificate`
- `CollatzRetainedEvenBoundary.boundary_prefix`
- `CollatzRetainedEvenBoundary.leading_large_gap_interval_rule`

This module was also checked with Lean 4.34.1 and
`-DwarningAsError=true`.

The broader interval residual still includes initial halving runs of
length two, length-one sources with first odd gap at most three, nonunit
length-three endpoints, and the excluded length-three cells above. These
results remove the stated cells; they supply no unconditional global
Collatz conclusion.
