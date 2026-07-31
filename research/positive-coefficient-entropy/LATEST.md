# Latest state — two coefficient lanes, one complete first-crossing language

**Snapshot:** 2026-07-31  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**PR:** #81  
**Status:** draft mathematical research

All theorem-level statements below remain **PROPOSED** pending independent
reconstruction. Claims using Rhin or PR #34's full-order theorem are explicitly
source-qualified.

**No proof of Collatz is claimed.**

## 1. Exactly two global targets remain

### SC*

\[
\boxed{
\min_{w\in\mathcal W_N^{\rm sup}}r_w\to\infty.}
\]

This excludes an ordinary integer whose coefficient is supercritical at every
prefix.

### FC*

Apart from the trivial first-crossing word `10`, prove that no complete
first-crossing tuple satisfies

\[
\boxed{
A_w=(2^j-3^q)r+2^jd
=(2^j-3^q)(r+d)+3^qd,}
\]

with

\[
\boxed{0\le d<q/3}
\]

and every first-crossing, prime-power, and canonical-source gate.

`d=0` is the positive-cycle level; `d>0` is an acyclic CST near-return.
`L-6814` proves that every nontrivial positive cycle generates a canonical
first-crossing failure. Thus FC* already contains cycle exclusion.

Therefore

\[
\boxed{\text{SC* + FC* imply Collatz.}}
\]

No third cycle premise is required.

## 2. One relative envelope would close both

Let

\[
F_j
={A_{\rm mech}(j)\over2^j-3^{q(j)}}
\]

be the exact upper-mechanical no-descent threshold. Every first-crossing
failure satisfies

\[
\boxed{
m_{j-1}^{\rm sup}\le r^+(w)\le F_j.}
\]

Hence the cofinal inequality

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

would force every late first crossing to descend. Because `F_j` is unbounded
along lower convergents, the same inequality would force `m_N^sup` to
infinity.

The universal scalar envelope is sharpened to

\[
\boxed{
F_j
<
{q(j)2^j\over3(2^j-3^{q(j)})}.}
\]

No matching cofinal lower bound for `m_N^sup` is currently proved.

## 3. Complete sectors already closed in FC

Subject to the stated source dependencies:

```text
upper-mechanical canonical word:
  descends at every nontrivial length;

no-wrap nonmechanical word:
  is easier to descend than the mechanical word;

bounded-bank / low-complexity families:
  eventually descend;

sub-square-root-support repair families:
  impossible;

fixed-support cycle/near-return families already covered by the
existing exact cycle packets:
  excluded within their declared scopes.
```

Every surviving acyclic member is a genuine nonmechanical dyadic wrap.

## 4. Thin across words, rough inside each word

PR #83 `T-6911` gives the source-free cardinality bound

\[
|\mathcal E_j|
<
{j\over3(1-e^{-\lambda_j})},
\qquad
\lambda_j=j\log2-q\log3,
\]

and hence, under an effective logarithmic-form bound,

\[
|\mathcal E_j|=O(j^{\mu+1}).
\]

Thus the bad language has zero family entropy.

But `L-6811/T-6810` show that every unbounded **acyclic** bad family has

\[
\boxed{
R_j
\ge
\sqrt{{\log2\over2\log3}\,j}
-O(\log j),}
\]

where `R_j` is the number of odd positions displaced from the upper-mechanical
word.

The same family also satisfies

\[
I_j=\Omega(j^{2/3})
\]

for total displacement, leaves the mechanical word within `O(log j)` bits,
and leaves its own old parity tail within `O(log j)` bits after the near-return.

The surviving FC language is therefore:

```text
polynomially sparse across candidate words;
square-root-supported inside every acyclic candidate;
two-thirds-scale in integrated displacement;
early departing at both boundaries;
and synchronized across the complete denominator by one d<q/3.
```

Counting alone and sparse-edit arguments are both exhausted.

## 5. Lossless complete-prime-power object

Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

`L-6809` proves that one exact first-crossing non-descent is equivalent to:

```text
1. generalized-CRT-compatible local excess paths modulo all h_s;
2. the unique monotone physical lift in the full-order window;
3. every proper first-crossing coefficient inequality;
4. one common ordinary 0<=d<q/3;
5. every complete prime-power congruence A == 3^q d;
6. the canonical positive source (A-2^j d)/D.
```

An order-cover may decode a word but does not certify omitted prime powers.
A proper-factor hit is not a first-crossing near-return.

## 6. Highest-value next theorem

The next proof must attack one of the following equivalent global objects.

### Relative-envelope route

\[
\boxed{m_{j-1}^{\rm sup}>F_j\quad\text{cofinally}.}
\]

### Complete-denominator route

Prove that the thin, rough wrapped language has no complete tuple with

\[
0\le d<q/3,
\]

apart from the trivial word `10`.

### Source-corner route

Directly prove

\[
\boxed{m_N^{\rm sup}\to\infty.}
\]

Another physical growth theorem, measure-one statement, proper-factor sieve,
or compatible free completion does not change these targets.

## 7. Review order

1. `claims/L-6803-canonical-start-end-rectangle.md`
2. `claims/L-6812-bilateral-shifted-near-return.md`
3. `claims/L-6814-positive-cycles-absorb-into-first-crossing.md`
4. `claims/L-6813-sharpened-box-coupling-envelope.md`
5. `claims/T-6806-upper-mechanical-all-length-closure.md`
6. `experiments/X-6801-mechanical-cst/`
7. `claims/L-6811-support-sensitive-factor-complexity.md`
8. `claims/T-6810-square-root-displaced-support.md`
9. `claims/T-6811-polynomially-sparse-square-root-rough.md`
10. `claims/L-6809-near-cycle-prime-power-compiler.md`
11. `Q-6802-canonical-displacement-closure.md`
12. latest session report
