# Exact connection to the existing odd-psi frontier

`BandParityBridge.lean` imports only `BandTransport`. It defines the local
property

\[
\mathrm{PsiComparison}(n):\quad
\mathrm{Basin}(n)\iff\mathrm{Basin}(2n-1),
\]

and the same parity rank used by PR 180:

\[
R(n)=\begin{cases}2n,&n\text{ even},\\n,&n\text{ odd}.\end{cases}
\]

This checks whether the new supplied-source structure turns the complementary
band phase into a strictly smaller odd-psi query.

## The complementary transfer reproduces the original odd query

Let `r ≥ 1`, `u > 0`, and

\[
3^r u=4z+1,\qquad
n=2^{r+1}u-1,\qquad m=2^r u-1.
\]

The module proves all three ordinary basin identifications:

\[
\mathrm{Basin}(n)\iff\mathrm{Basin}(9z+2),
\]

\[
\mathrm{Basin}(m)\iff\mathrm{Basin}(z),
\]

\[
\mathrm{Basin}(2n-1)\iff\mathrm{Basin}(z).
\]

The last one does not use an auxiliary comparison hypothesis. Since `m` is
odd and `n = 2m+1`, the ordinary inverse lift `4m+1` has the same basin status
as `m`; but `4m+1 = 2n−1`.

Consequently,

\[
\boxed{
(\mathrm{Basin}(z)\iff\mathrm{Basin}(9z+2))
\iff\mathrm{PsiComparison}(n).
}
\]

The directional version is also exact:

\[
\boxed{
(\mathrm{Basin}(z)\Rightarrow\mathrm{Basin}(9z+2))
\iff
(\mathrm{Basin}(2n-1)\Rightarrow\mathrm{Basin}(n)).
}
\]

Thus the smaller supplied source establishes the antecedent of the reverse
direction of the **original** odd-psi query. It does not establish a different
query at a smaller parameter. The module proves `n` is odd and `R(n)=n`.
Transport through the supplied certificate therefore leaves the required
query's rank unchanged. Applying PR 180's `OddRankStep` induction hypothesis
here would be circular: that hypothesis supplies comparisons only at rank
strictly below `n`.

The declarations recording this are:

- `complementary_identifications`
- `complementary_transfer_is_same_odd_psi`
- `complementary_forward_is_reverse_same_psi`
- `complementary_query_rank`

## Positive connection for the solved phase

For the other phase,

\[
3^r u\equiv3\pmod4,
\]

the unbounded word exchange already proved in `BandTransport` gives
`Basin(n) ↔ Basin(m)`. The ordinary inverse lift above then proves

\[
\boxed{\mathrm{PsiComparison}(2^{r+1}u-1)}.
\]

`solved_phase_odd_psi` is an unconditional two-way odd-psi theorem for this
entire unbounded family. It requires no auxiliary lower-rank query. This
places the successful band deduction directly into the earlier project's
comparison framework while exposing the exact unchanged query in the
complementary phase.

## Validation

Lean 4.34.1 compiled the new module successfully with
`-j1 -DwarningAsError=true` and produced `BandParityBridge.olean`. All five
printed axiom audits contain only `propext`, `Classical.choice`, and
`Quot.sound`. The original `BandTransport.lean` checkpoint was not modified.
