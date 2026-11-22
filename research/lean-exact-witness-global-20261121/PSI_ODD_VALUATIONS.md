# Every odd initial valuation closes its ψ query

`lean/Collatz/PsiOddValuations.lean` proves the following whole-branch
result in the original complete-source interval induction.

Let

\[
S=2^e q,
\]

where the supplied complete odd certificate is for \(q\), and suppose
\(e\) is odd. Then the query

\[
\operatorname{Basin}(2S-1)
\]

follows from the existing lower-\(\Gamma\) interval induction hypothesis.
There is no upper bound on \(e\), \(q\), the source word length, or any
of its gaps. In particular, this closes the entire initial-valuation-three
ψ branch as well as initial valuation one.

## The actual target merger

First suppose \(q\equiv1\pmod4\). Because \(e\) is odd,

\[
a=3^e q-1\equiv2\pmod4.
\]

The ordinary shortcut map has the exact two-step diamond

\[
T^2(a)=T^2(3a+2).
\]

Indeed, write \(a=4b+2\). Its two ordinary images end at \(3b+2\),
and those of \(3a+2=12b+8\) end at the same integer.

The initial odd-run identities give

\[
T^e(2^e q-1)=3^e q-1=a,
\]

\[
T^{e+1}(2^{e+1}q-1)=3^{e+1}q-1=3a+2.
\]

Consequently the complete ordinary merger is

\[
\boxed{
T^{e+3}(2^{e+1}q-1)=T^{e+2}(2^e q-1).
}
\]

Both clocks grow with the initial valuation. This is an exact ordinary
common future, with no convergence assumption on either target arm.

The child known source is

\[
S'=2^{e-1}q=S/2,
\]

and its target is precisely \(2S'-1=S-1\). It lies in the existing
interval \(0<t\le2S'+1\). The entire supplied odd word is unchanged.
Only the initial even run decreases, so its complete grade satisfies

\[
\Gamma(e-1;W)<\Gamma(e;W).
\]

The induction hypothesis supplies convergence of the smaller target. The
actual merger transfers it to the original ψ target.

## The other odd-core phase

If \(q\equiv3\pmod4\), the first supplied odd gap is necessarily one:
\(3q+1\equiv2\pmod4\). The existing `first_gap_one_rule` consumes that
actual gap, retains the initial even run, and increases the known source.
Every original interval target, including \(2S-1\), remains active, while
the whole source grade strictly decreases. Thus this phase closes with no
condition on the rest of the supplied word.

Together the two phases cover every odd certified \(q\).

## Initial valuation three explicitly

For \(e=3\) and \(q=4j+1\), the common endpoint is

\[
z=\frac{81q-1}{4}=81j+20.
\]

The ordinary positive-gap prefixes can also be written

| Original target | Prefix | Total shortcut clock | Correction |
| --- | --- | --- | --- |
| \(16q-1\) | \([1,1,1,3]\) | 6 | 65 |
| \(8q-1\) | \([1,1,2,1]\) | 5 | 73 |

Their exact identities are

\[
81(16q-1)+65=64z,
\qquad
81(8q-1)+73=32z.
\]

The endpoint may be even; the ordinary-prefix interface permits that. The
child known source \(4q\) retains the full source word and changes only
the initial grade from seven to five.

## Formal statements and scope

The five public Lean declarations are:

- `CollatzPsiOddValuations.two_step_diamond`
- `CollatzPsiOddValuations.odd_valuation_target_merge`
- `CollatzPsiOddValuations.odd_valuation_target_equivalence`
- `CollatzPsiOddValuations.psi_odd_valuation_rule`
- `CollatzPsiOddValuations.psi_valuation_three_rule`

The module passed Lean 4.34.1 with `-DwarningAsError=true` and uses the
existing ordinary map, orbit, complete certificate, and grade relation.

The endpoint diamond is the same arithmetic mechanism used by the earlier
physical smaller-partner work in PR184 `RisingMerge.lean` and PR185
`AL27_HALF_ROUTE.md`. The new result integrates its entire odd-valuation
phase with one actual complete supplied witness: the child source is the
halved original source, its word is unchanged, and its original grade is
strictly smaller. It does not restart an induction at a larger intermediate
ordinary value.

This proves the stated ψ branches under the common lower-rank interval
induction hypothesis. It does not prove that all interval queries are
covered, nor assert a global Collatz conclusion. A ψ case rule alone must
not be substituted for complete coverage of the larger interval domain.
