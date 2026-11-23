# Independent review: triadic denominator rank and finite closure

Date: 23 November 2026. Reviewer: the cycle lane, independently
reconstructing the duality lane's proof and performing a fresh narrow
Lean replay.

**Verdict: VERIFIED at the hashes below for the formal closing implication
and the written finite sufficient certificate.** The universal existence
of the source-dependent triadic residue remains **OPEN**. This review
does not assert full Collatz or turn a conditional theorem into an
unconditional one.

## 1. Exact subjects and execution

| File | SHA-256 |
|---|---|
| `research/global-closure-20261123/duality/TRIADIC_RANK.md` | `e4ad2b13c40b7f8906862143edc8c836def4b8f8c359bfec50d3c94146e2d120` |
| `research/global-closure-20261123/duality/lean/TriadicDualClosure.lean` | `62a3d8a9541080864deb4887ba8c014a82222892869b14597c3b6385538913c7` |
| `research/global-closure-20261123/duality/lean/TriadicDualAudit.lean` | `6bbfb6fa7bd6465e3e8702dbf3e0fd29e40d704a24d8fa46f39835416f7c5986` |

The reviewer strictly compiled the actual new module with Lean 4.34.1 and
Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, with
`-DwarningAsError=true`. The module exited zero with empty compiler
output. A separately generated audit imported the fresh object and
printed the axioms of all 20 authored public declarations: twelve
theorems, six definitions and two types. It also exited zero. Every
reported axiom is among `propext`, `Classical.choice` and
`Quot.sound`; no `sorryAx` or custom assumption occurred.

The source hash was identical before and after the replay. Objects were
written outside the repository. The exact commands, paths, timings and
log hashes are in [duality-review-replay.json](duality-review-replay.json);
the actual [compile output](duality-review-compile.log),
[axiom output](duality-review-axioms.log), and
[reviewer audit source](duality-review-audit.lean) are retained.

The author's broader audit also names constructors/projections. This
review inspected that source; its fresh execution claim above refers to
the reviewer's own 20-declaration audit. No old Lean corpus was rebuilt.

## 2. Reconstructing the rational dynamics

The stored state is \((x,w,r)\), with \(x>0\), \(w\in\mathbb Z\),
\(r\in\mathbb N\), representing \(y=w/3^r\). Since \(3^r\) is odd,
the rational parity of \(y\) is the parity of \(w\), even when this
fraction is unreduced.

If \(x\) is odd, complementary parity requires \(w\) even. The exact
updates are \(2x'=3x+1\), \(2w'=w\), \(r'=r\), so \(y'=y/2\).

If \(x\) is even and \(r>0\), complementary parity requires \(w\) odd.
Then
\[
\frac{3(w/3^r)+1}{2}
=\frac{w+3^{r-1}}{2\,3^{r-1}}.
\]
The numerator \(w+3^{r-1}\) is even, so this is exactly the stored
update \(w'=(w+3^{r-1})/2\), \(r'=r-1\). No lowest-terms premise is
needed. When \(r=0\), the update is \(w'=(3w+1)/2\), an integer.

The three constructors of `TriadicStep` state precisely these
relations. The new `step_rational` theorem checks their rational
meaning. The deterministic `next` and `trajectory` definitions do
not choose fresh candidates: `trajectory_x` proves that their first
coordinate is the literal shortcut orbit of the original input.
`compatible` is an actual parity test on each stored state, and
`next_step` turns a passed test into the exact integer relations.

## 3. Reconstructing the all-time rank proof

An all-time zero numerator would remain zero and force every subsequent
ordinary state to be odd. For such an ordinary tail,
\[
2(x_{i+1}+1)=3(x_i+1).
\]
Integrality and coprimality of 2 and 3 imply
\(2^k\mid x_0+1\) for every \(k\). Since \(x_0>0\), this is impossible.
The Lean proof retains this fixed initial positive integer; it does not
replace it by one integer for each finite prefix.

For a nonzero numerator put
\[
P=x|w|,\qquad E=2P+\mathbf1_{\{w=1\}},
\qquad \mathcal R=(r,E)\in\mathbb N^2.
\]

- At an original-odd step with \(x>1\),
  \(4P'=(3x+1)|w|<4P\).
- At an original-even step with \(r>0\), the first coordinate decreases.
  The second coordinate is allowed to increase.
- At an original-even integral step with \(w\ne0,1\),
  \(|3w+1|<4|w|\), so \(P'<P\). This includes negative \(w\).
- If \(w=1\), then \(w'=2\) and \(P'=P\), while the indicator drops
  from one to zero.

A strict decrease of the integer product is at least one, so the factor
two in \(E\) pays for any indicator increase. The lexicographic rank
therefore strictly decreases at every nonterminal compatible step.

The theorem `triadic_pair_reaches_one` applies the well-foundedness of
the lexicographic order on \(\mathbb N^2\). Its positive ordinary path
and its nonzero-numerator lemma have exactly the hypotheses needed.
The final theorem `alltime_triadic_candidate_reaches_one` connects this
rank argument to the actual ordinary orbit and one fixed initial
\((n,a,r)\). It explicitly assumes all-time compatibility; no theorem
constructing that compatibility for every \(n\) appears in the module.

## 4. Independent reconstruction of the finite certificate

This section reviews a **written proof**, not a Lean theorem.

Let
\[
N=\operatorname{bl}(n),\quad
B=\max(1,|a|,3^r),\quad L=\operatorname{bl}(B),\quad
R=rL,\quad E=N+L+R,\quad H=R+8E+2.
\]
The complementary carry uses the actual original word:
\[
D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i,\qquad
b_i=\sum_{j<i}(1-e_j).
\]
The condition
\[
2^H\mid3^{b_H}a+3^rD_H
\]
puts the terminal affine value in the odd-denominator rationals.
Pulling backward along the prescribed branches imposes each earlier
parity and preserves odd denominators. Thus the condition certifies the
entire supplied prefix, not only the final affine equality.

Before the denominator exponent is exhausted, \(|w_i|\le B\):
halving does not increase the absolute value, and the other relevant
update has absolute value at most
\((B+3^{r_i-1})/2\le B\). A nonzero integer numerator cannot undergo
\(L\) consecutive exact halvings, because \(2^L>B\).
Unless convergence or a zero numerator occurs earlier, each positive
denominator level is therefore exhausted within \(L\) clocks, giving
\(j\le R\).

The finite zero-numerator case is handled separately in the note.
If it occurs at \(j\le R\), the remaining compatible prefix is all odd,
so \(2^{H-j}\mid x_j+1\). The ordinary height bound gives
\[
x_j+1\le 2^{N+R},
\]
while \(H-j\ge H-R>N+R\). This is a contradiction.
The all-time nonzero lemma is **not** being imported into a finite
prefix. The reviewer raised this distinction before the note was
finalized; the reviewed note contains the correct finite argument.

At the first integral pair,
\[
P_j=x_j|w_j|\le nB2^R<2^E.
\]
If the original coordinate has not reached 1, an original-odd step has
\(x\ge3\), so its product contraction factor is at most \(5/6\).
An original-even step with positive odd \(w\ne1\) has \(w\ge3\),
giving the same bound; a negative \(w\) gives a stronger bound.
The exceptional tie \(w=1\) is followed by \(w'=2\), which forces the
next ordinary state to be odd. Unless it is 1, that next step contracts.
Thus every two nonterminal compatible integral steps multiply \(P\) by
at most \(5/6\).

Since \(6^4>2\cdot5^4\),
\[
(5/6)^{4E}2^E<1.
\]
After \(8E\) further steps, the positive integer product would be below
one. Because \(j+8E\le R+8E<H\), the certificate forces the original
orbit to reach 1 by \(H\). The stated constants and clock coverage are
valid; no parity test beyond the supplied prefix is used.

## 5. Converse, coupled carries, and the precise unresolved step

The written converse is correct. Given an actual finite original path
to 1, put the complementary value 2 at its endpoint and pull backward
by \(y=2y'\) or \(y=(2y'-1)/3\), according to the original parity.
These operations preserve \(\mathbb Z[1/3]\) and impose opposite
parity. The paired core \((1,2)\leftrightarrow(2,1)\) then supplies the
tail. Signed numerators are allowed, as required.

The reviewer opened the primary Monks--Yazinski PDF and checked
Theorem 2.1 and Example 2 on printed page 3. The note correctly retains
the distinction between rationality of \(\Omega\) on positive integers,
which excludes divergence, and the stronger triadic condition used
here. The quoted example \(\Omega(3)=-4/9\) also agrees with direct
branch replay. No other part of the primary theorem is needed for the
elementary closing rank.

The determinant recurrence (25), congruence (26), and forced real-product
recurrence (27) were independently expanded from their definitions.
Their signs, powers and branch assignments are correct. They provide
no stated upper bound for the actual centered residue. The counting
bound (23) is a safe upper bound: a qualifying pair has \(r\le K\)
and \(|a|<2^{\lfloor K/8\rfloor}\); counting all such pairs can only
overcount the residues represented.

The remaining statement is exactly:
\[
\forall n>0\ \exists K,a,r:\quad
K\ge H(n,a,r),\qquad
2^K\mid3^{b_K}a+3^rD_K,
\]
with \(b_K,D_K\) computed from that same original \(n\).
The converse and finite sufficient certificate show why this would
settle full convergence. Neither the rank theorem nor a centered
representative of an arbitrary residue proves this source-dependent
existence. No independent absence-of-cycles premise has been hidden
inside the closing implication.

## 6. Fixes and review boundary

No mathematical correction was needed in the final note or Lean source.
The finite-zero issue was explicitly discussed, and the supplied final
proof resolves it. The review does not certify the universal small-residue
existence, any absent quantitative theorem in Lean, a generic
approximation-to-source transfer, or the rest of the repository.

Only the exact file hashes in Section 1 carry this verdict. Subsequent
scientific changes require a new binding.
