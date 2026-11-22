# Complete ψ closure at initial valuation two and first gap four

`lean/Collatz/PsiEvenHeadFour.lean` closes every query

\[
S=4q,\qquad \operatorname{Basin}(2S-1),
\]

whose complete supplied odd certificate for \(q\) is \(4::\tau\).
There is no restriction on the source value, the length of \(\tau\), or
any of its entries. Every recursive child keeps the literal supplied tail
and has strictly smaller rank than \(\Gamma(2;4::\tau)\).

The conclusion uses the existing lower-rank interval induction hypothesis.
It adds a complete case rule; it does not assume that the remaining global
interval dispatcher has already been proved.

## First transform the target

Peeling the actual supplied gap gives

\[
3q+1=16u,\qquad \operatorname{Certificate}(u,\tau).
\]

Thus \(u\) is odd and \(u\equiv1\pmod3\). Set

\[
n=8q-1,\qquad x=27u-2,\qquad y=\frac{81u-5}{2}.
\]

The ordinary target prefixes are

\[
n\xrightarrow{[1,1,2,1,3]}y,
\qquad
x\xrightarrow{[1]}y.
\]

The first word has five odd steps, total shortcut clock eight, and
correction 251. Its exact identity is

\[
243(8q-1)+251=256y.
\]

The other identity is \(3x+1=2y\). These prove basin equivalence of
the two targets through actual integral ordinary prefixes. For example,
writing \(u=6j+1\) gives

\[
n=256j+39,\qquad x=162j+25.
\]

The new target is therefore smaller than the original one throughout the
family, but the proof also supplies the exact source-certificate budget
needed to use it.

## An exhaustive ternary source rewrite

The three possibilities \(u\bmod9\in\{1,4,7\}\) cover every
admissible endpoint. In each case the new complete source is explicit.

| Endpoint cell | New odd source equation | Child known source | Child complete odd word |
| --- | --- | --- | --- |
| \(u\equiv1\pmod9,\ u>1\) | \(9p+7=16u\) | \(8p\) | \([2,2]\mathbin{++}\tau\) |
| \(u\equiv4\pmod9\) | \(9p+11=32u\) | \(8p\) | \([3,2]\mathbin{++}\tau\) |
| \(u\equiv7\pmod9\) | \(3p+1=4q\) | \(2p\) | \([2,4]\mathbin{++}\tau\) |

The first two rows end their inserted prefixes directly at \(u\). In
the third row, \(u\equiv7\pmod9\) and \(3q+1=16u\) force
\(q\equiv1\pmod3\); the new gap two ends at \(q\), so the old
leading gap four is retained.

The wanted child target is \(x=27u-2\). The interval bounds are exact:

- In the first row, \(u>1\) and \(u\equiv1\pmod9\) give
  \(u\ge10\), which implies \(27u-2\le16p+1\).
- In the second row, \(9p+11=32u\) gives
  \(27u-2\le16p+1\) for every admissible \(u\).
- In the third row, the two source equations give
  \(27u-2\le4p+1\). After clearing denominators, the required
  inequality is just \(1\le13u\).

All child targets are positive.

## The endpoint-one case

For \(u=1\), the first row still constructs \(p=1\) and child known
source eight, with complete word \([2,2]\mathbin{++}\tau\). The
wanted partner is 25. It has the exact ordinary prefix

\[
25\xrightarrow{[2,1,3]}11,
\]

and \(11\le2\cdot8+1\). Thus the same child rank closes this case
after an additional target transport. No fresh numerical convergence fact
or bounded verification threshold is required. The supplied certificate
for endpoint one may contain terminal-cycle padding; it is preserved.

## Rank accounting

The parent front grades are \([5,8]\). The unchanged tail cancels.
The three child front grade lists are respectively

\[
[7,4,4],\qquad[7,6,4],\qquad[3,4,8].
\]

For the first two, grade eight is removed and every inserted grade is
smaller. The old initial grade five is also removed. For the last, grade
eight is retained, while grade five is replaced by grades three and four.
Every case strictly decreases the original common multiset order.

## Formal statements and verification

The four public declarations are:

- `CollatzPsiEvenHeadFour.head_four_target_equivalence`
- `CollatzPsiEvenHeadFour.replaced_four_rank`
- `CollatzPsiEvenHeadFour.retained_four_rank`
- `CollatzPsiEvenHeadFour.psi_even_head_four_rule`

The module passed Lean 4.34.1 with `-DwarningAsError=true`. It uses the
existing prefix compiler and full supplied certificate throughout.

This closes the entire stated valuation-two, leading-four ψ branch. Other
ψ branches and arbitrary targets in the larger interval require their own
proved case rules; this result does not identify ψ coverage with complete
interval coverage.
