# Independent review of the sparse-script arithmetic obstruction

23 November 2026. Reviewer: root. Author: density_free_germ8.
Published parent PR182: c369ae3c426ec6aaf9a280ec9578b9910c2147d5.

**Verdict: VERIFIED for R10-A1--A4 at the written and finite-formal
scopes below. Arbitrary automatic scripts and full scalar rigidity
remain OPEN.** This is an independent reconstruction of the author's
proof. Root did not author the reviewed scientific files.

## Exact review boundary

All science paths are relative to
research/carry-tower-round10-20261123/.

| File | Git blob |
| --- | --- |
| ARITHMETIC_TOWER.md | 0dd85d7a3fbb2e49587e5b8fbb7e70fc4fa139d2 |
| arithmetic_tower_controls.py | 81062733ec34881679d526daf3172df6a05d8aba |
| ArithmeticTower.lean | b1b568e8344311db4ee06583a0fbd80cb02d115c |

The parent inputs are PR182 at the full published parent above:
ARITHMETIC_RIGIDITY.md, R9-A2--A3, blob
2c872eb9818be062e9444fde91555ba4e1e7230f, and CARRY_RETURN.md,
the complete L/P maps, blob 0b0d2ff63339522689f9984aad1bae3ab63d9e08,
both in research/scalar-rigidity-round9-20261123/.
The publication receipt identifies the containing commit for the new
blobs; this verdict does not extend to changed files.

## 1. Ordinary window and complete block legality

I independently substituted X=q+7 into the full two-step maps.
The unpaid and paid equations are respectively
8X'=9X and 32X'=9X+166. Positive odd ordinary sources give X>=8.
Thus the paid inequality 8X'<=9X is equivalent to 27X>=166
and is valid on the entire stated domain.

Iterating gives 8^j X_j<=9^j X_0. A run of m unpaid blocks gives
8^m X_(j+m)=9^m X_j. Its endpoint shifted coordinate is even,
so coprimality with 9^m forces the full divisor
2^(3m+1) into X_j. This includes the extra factor two furnished
by endpoint oddness. It yields precisely R10-A1,
2^(3m+1)8^j<=9^j(q+7), including m=0.

The Lean BlockEdge predicate retains positivity and oddness of both
ordinary endpoints and the full affine numerator. Its first two
theorems construct the odd intermediate state and both complete
ordinary edges. Consequently these hypotheses really do certify
the two specified valuations. The finite prefix, unpaid divisor,
and same-source window theorems preserve the same sequence q.

## 2. The rational-height obstruction is within the 2-adic field

I reconstructed the inverse iteration, including the sign and the
constant 166/9. For paid positions t_r, the inverse sum is

\[
F_s=\sum_{r\ge0}4^r(8/9)^{t_r},\qquad
q_*=-7-(166/9)F_s.
\]

The valuations 2r+3t_r strictly increase, so the series converges in
Q_2. The terminal shifted coordinate of every compatible finite
ordinary cylinder is even. This makes the inverse boundary term
vanish 2-adically and identifies the unique completion. The same
argument applies to a putative rational odd state with odd denominator.
Any rational value of this completion is 2-adically odd, so rational
values with an even reduced denominator do not create an omitted case.

Suppose F_s=a/b in lowest terms with b>0. Because F_s lies in Z_2,
b is odd. With D_R=9^(t_R) and the full positive numerator N_R from
the note, the first omitted term has strictly least valuation.
Thus the nonzero integer aD_R-bN_R has exact valuation
2(R+1)+3t_(R+1). Multiplication by the odd integers b,D_R does
not alter that valuation. Its absolute ordinary height is strictly
less than (|a|+b)4^(R+1)9^(t_R).

Divisibility of a nonzero integer supplies the opposite lower bound.
Canceling 4^(R+1) gives the necessary restriction
8^(t_(R+1))/9^(t_R)<|a|+b for every R. The stated limsup
hypothesis contradicts this. This verifies R10-A2 for rational
candidates of either sign. No equality between real and 2-adic
limits is used; no unproved transcendence theorem is required.

## 3. The automatic families and finite mismatch budgets

For the positive indices with at most k one-bits, the numbers
(2^k-1)2^n and 2^k2^n are consecutive paid positions. Every integer
strictly between has the k leading one-bits of the left endpoint
and at least one additional lower one-bit. Along these pairs the
height ratio is (8^(2^k)/9^(2^k-1))^(2^n).

For k=1,2,3,4 this base exceeds one. At k=4 the exact inequality
is 2^48>3^30, obtained from 256>243. Thus the irrationality
criterion applies. Each finite prefix still has its own ordinary
cylinder; this is fully compatible with an irrational 2-adic limit.
At k=5 the displayed ratio has base below one. The note correctly
makes no exclusion claim there and no claim for automaticity alone.

For the effective budget, let B=bl(q+7), choose the least dyadic h
with (35-2^(k+1))h>=11B+24, and consider the unpaid window
j=(2^k-1)h+1, m=h-1. It lies wholly within the first 2^k h
blocks. Raising R10-A1 to the eleventh power and using
9^11<2^35 and q+7<2^B gives
33m+11<2j+11B. Substitution contradicts exactly the chosen
budget. The least-power choice gives the claimed strict linear
upper bound in B. This verifies R10-A3--A4.

## 4. Evidence coverage and literature boundary

I inspected the full control script. It replays actual gaps and
complete affine edges, tests both lifts of all binary words through
length six, includes the four automatic families, and checks supplied
ordinary mismatch budgets. Its rational-height tests include negative
numerators and odd denominators. A zero finite truncation defect is
handled separately and is not mistaken for infinite equality.
The finite valuation controls do not claim to execute a 2-adic
infinite proof. Checks use explicit exceptions and remain active
under optimized Python.

The root combined execution and fresh Lean dependency audit are
recorded separately in EXACT_RECEIPT.json and LEAN_RECEIPT.json.
ArithmeticTower has twelve theorems and one definition. The Lean
scope is the literal finite block arithmetic, full source window,
and exponent/budget consequences. The automatic index argument and
infinite irrationality proof remain written mathematics.

Root directly opened Mahler's original paper, inspected the paired
real and 2-adic formulas (7)--(10) and the necessary-condition warning
in Section 6, and independently opened the Eliahou--Verger-Gaugry
preprint at Proposition 3.1, Corollary 3.2, and its open questions.
The note accurately uses them as context and respects their map and
digit-normalization boundaries.

**First unsupported inference:** showing that an arbitrary actual
exceptional scalar source has one of these sparse scripts, or
establishing a replacement height obstruction for all possible
carry schedules. Neither the verified finite window nor the four
automatic exclusions supplies that implication.
