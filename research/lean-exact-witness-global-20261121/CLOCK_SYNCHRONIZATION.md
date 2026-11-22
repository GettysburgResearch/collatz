# Whole-prefix clock repayment and low-even psi returns

**Status: the source rewrites, rank comparisons, and coverage families below
are proved in Lean core. A complete coverage theorem for Collatz and the
original residue implication is not claimed.**

Formal source:
[Collatz/ClockSynchronization.lean](lean/Collatz/ClockSynchronization.lean).
The module imports the shared odd-source cap from
[Collatz/LowGapGlobal.lean](lean/Collatz/LowGapGlobal.lean).

## 1. Exact local clock consumption

For a supplied powered certificate, write

\[
 s=2^e q,\qquad
 \operatorname{Certificate}(q;(a)\Vert\tau),\qquad
 3q+1=2^a u.
\]

The encoded source clock is

\[
 H(e;w)=e+\operatorname{total}(w).
\]

Suppose \(e\ge1\), \(0<t\le2s+1\), and an actual target gap satisfies

\[
 3t+1=2^b v,\qquad 1\le b\le e+a.
\]

The child source is \(s'=2^{e+a-b}u\), carrying the literal supplied tail
\(\tau\). The exact identity is

\[
 2^b(2s')=6s+2^{e+1}.
\]

Thus \(0<v\le2s'\), because \(3t+1\le6s+4\) and
\(2^{e+1}\ge4\). The source clock satisfies

\[
 H(e+a-b;\tau)+b=H(e;(a)\Vert\tau).
\]

The theorem `paired_step` proves the complete child certificate, interval,
clock identity, strict clock decrease, and basin equivalence. It permits
target gaps below the previous one-step threshold \(\min(a,e+1)\).
Such a step can increase the graded multiset; the theorem does not use its
clock decrease as a replacement for that order.

## 2. Returning below the original rank after a whole prefix

Let the supplied source prefix \(w\) have length \(k>0\), total
\(A\), and correction \(C_s\). Let an actual target prefix \(z\)
have the same odd-step count, total \(B\), correction \(C_t\), and
endpoint \(v\). Write

\[
 3^kq+C_s=2^Au,\qquad
 3^kt+C_t=2^Bv.
\]

The literal tail at \(u\) remains certified.

For a nonempty source prefix,

\[
 3^k\le3C_s.
\]

Consequently, if \(C_t\le C_s\) and \(e\ge1\), then

\[
 3^k+C_t\le4C_s\le2^{e+1}C_s.
\]

Choose a child even exponent \(f\) satisfying the clock budget

\[
 e+A\le f+B.
\]

The old interval bound yields

\[
 \begin{aligned}
 2^Bv
 &=3^kt+C_t\\
 &\le 2^{e+1}3^kq+3^k+C_t\\
 &\le 2^{e+1}(3^kq+C_s)\\
 &=2^{e+A+1}u\\
 &\le2^{f+B+1}u.
 \end{aligned}
\]

Hence the new target lies in the stronger child bound
\(0<v\le2(2^fu)\). This is
`funded_prefix_interval`.

The rank uses an initial-even grade \(2e+1\) and an odd-gap grade
\(2a\) for every supplied gap \(a\). There are two ways to pay for
the child:

- If \(f=e\), deleting the nonempty source prefix strictly lowers the
  complete rank.
- If some consumed source gap \(a\) satisfies \(f<a\), the inserted
  grade \(2f+1\) is below the removed grade \(2a\). Remove the old
  initial grade and the consumed source grades, insert the new initial
  grade, and retain the entire common tail.

`funded_prefix_rank` proves these alternatives in the original graded
multiset order. Intermediate ranks are unrestricted.

## 3. A first clock repayment controls the corrections

The correction has the prefix-sum expansion

\[
 C(w)=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j},
 \qquad
 A_j=\operatorname{total}(w[0:j]).
\]

Thus \(C_t\le C_s\) whenever every proper target prefix has consumed
no more clock than the corresponding source prefix:

\[
 B_j\le A_j\qquad(0\le j<k).
\]

The inductive relation `PrefixClockOrder` expresses exactly these proper
prefix inequalities. The Lean proof of correction domination uses the
equivalent recurrence

\[
 C(w\Vert(a))=3C(w)+2^{\operatorname{total}(w)}.
\]

The final cumulative totals are unrestricted by this relation.
`first_repayment_rule` therefore applies to any actual target path at its
first return to \(B\ge A\), even after an arbitrarily long interval of
clock debt and intermediate rank increases.

The stronger `funded_repayment_rule` can return earlier. It suffices to
reach

\[
 B\ge A+e-f
\]

for a child exponent \(f\) paid by one consumed source gap. For example,
a removed gap four can fund \(f=3\). The theorem is a concrete path
reduction under the original interval induction hypothesis; it does not
assume that a first repayment exists for every target.

## 4. An unbounded explicit family for every source prefix

For any nonempty positive source word \(w\), put

\[
 k=\operatorname{length}(w),\qquad A=\operatorname{total}(w).
\]

Use the target word

\[
 z=(\underbrace{1,\ldots,1}_{k-1},\ A-k+1).
\]

Its length is \(k\), its total is \(A\), and its correction is the
minimum possible correction at that length:

\[
 C(z)+2^k=3^k.
\]

The source positivity gives \(A\ge k\) and \(C(z)\le C(w)\).
The complete original source prefix can therefore be deleted while
retaining the initial even exponent and the literal tail.

Theorem `delayed_repayment_rule` proves this family for arbitrary source
length, gap sizes, source value, and inherited tail. The direct arithmetic
interface `delayed_affine_rule` constructs the complete target path from

\[
 3^k(t+1)=2^k+2^Av.
\]

No list of intermediate target iterates is required.

For the concrete source prefix \((2,2)\), the target word is \((1,3)\).
Its legality condition is precisely \(t\equiv3\pmod{16}\). The theorem
`two_twos_residue_rule` covers every such target in the old interval and
every initial exponent \(e\ge1\). Its first target gap is one, so this
family passes through a source-rank increase before returning below the
original complete rank.

## 5. Automatic low-even psi handoffs

The special target \(\psi(s)=2s-1\) supplies further unguarded families.

### Initial exponent one, first source gap two

Suppose \(s=2q\) and \(3q+1=4u\), with the literal tail certified at
\(u\). Then

\[
 3s+2=8u,\qquad 0<u<s.
\]

The target prefix \((1,3)\) sends \(2s-1\) to \(3u-1\).
The ordinary psi identity identifies its basin with that of \(2u-1\).
The old initial grade three and the first odd-gap grade four are removed.

Theorems `psi_head_two_handoff` and `psi_head_two_rule` retain the exact
tail and close this entire family under the original interval hypothesis.
There is no additional congruence guard on the source or target.

### Initial exponent two or three, four leading source gap-twos

For the supplied source prefix \((2,2,2,2)\),

\[
 81q+175=256u,\qquad
 \operatorname{Certificate}(u,\tau).
\]

Both low-even branches reach the same target carry:

| Initial exponent | Exact target prefix | Target endpoint |
|---|---|---|
| \(e=2\) | \((1,1,2,3,4)\) | \(3u-2\) |
| \(e=3\) | \((1,1,1,5,4)\) | \(3u-2\) |

These are five odd target steps against four consumed odd source steps.
The theorems retain the exact numerical identity

\[
 81s+175\cdot2^e=256\cdot2^eu,
 \qquad 0<u<s.
\]

The source \(u\) is odd and certified by the literal supplied tail.
The shared `CollatzLowGapGlobal.odd_source_cap` handles every positive
target at most \(3u+2\): if \(u\ne1\), its actual next source step
satisfies \(2T(u)+1=3u+2\) and strictly lowers the source rank; \(u=1\)
has the exact finite terminal range at most five. Thus \(3u-2\) closes
with the inherited original rank budget.

`psi_four_twos_handoff` proves the two exact target paths, and
`psi_four_twos_rule` closes both families. No separate convergence
assumption for the carry \(3u-2\) is introduced.

## 6. The source-clock terminal boundary

The local source-clock decrease does not itself prove complete interval
coverage. Once the supplied odd word is exhausted, the known source is
\(2^e\). Its interval is

\[
 0<t\le2^{e+1}+1.
\]

The remaining exponent \(e\) is not bounded by the original low values:
a paired step with source gap \(a\) and target gap one changes it to
\(e+a-1\).

The terminal core one can be represented by its gap-two loop, but adding
that loop first adds two source clocks. Pairing it with a target gap one
leaves a child clock one larger than the original empty-word clock.
This does not justify an induction descent at the terminal boundary.

The proved whole-prefix returns avoid that issue whenever the target
repays the relevant clock debt before the supplied source budget ends.
What remains unproved is a universal selection argument ensuring a
successful funded return, an applicable carry handoff, or another
already proved original-rank rewrite for every remaining source-target
state. The module contains no claim of that missing selection theorem.

### Exact obstruction to a universal funded-repayment selector

The pair

\[
 s=34=2\cdot17,\qquad t=63
\]

lies in the remaining narrow initial-exponent-one strip:

\[
 3\cdot17+2<63\le4\cdot17+1,\qquad63\equiv3\pmod4.
\]

The complete odd source path is

\[
 17\xrightarrow{2}13\xrightarrow{3}5\xrightarrow{4}1,
\]

so its entire source alphabet is at most four. The first three exact odd
target gaps are \((1,1,1)\). At the three possible nonempty source
prefixes, the required child exponent \(1+A-B\) and largest funded
exponent are

| Consumed source prefix | Required exponent | Largest funded exponent |
|---|---:|---:|
| \((2)\) | 2 | 1 |
| \((2,3)\) | 4 | 2 |
| \((2,3,4)\) | 7 | 3 |

There is no funded repayment before the supplied source word ends.

This remains true after appending **any number** of terminal gap-two loops
to the source certificate. The exact target path to its first one has 39
odd steps and total clock 68. Comparing every target prefix against the
source word \((2,3,4,2,2,\ldots)\) gives a strictly positive funding
shortfall at every prefix; its smallest value is one. After 39 odd steps,
the accumulated source clock is 81, so the required exponent is

\[
 1+81-68=14,
\]

while the largest funded exponent remains three. Both terminal odd values
are then one. Each additional exact odd gap is two on both sides, and

\[
 1+(A+2)-(B+2)=1+A-B=14.
\]

For a padding length \(m\), if \(3+m\le39\), every eligible source
prefix is covered by the exact finite replay. If \(3+m>39\), all later
prefixes have the constant shortfall \(14-3\). These two cases prove
failure of the funded-repayment selector for every \(m\ge0\).
Allowing an even target endpoint by shortening its last gap can only
decrease \(B\), so it cannot improve the budget.

The optimized-safe script
[repayment_obstruction.py](gap-search/high/repayment_obstruction.py) checks
the exact source and target certificates, all 39 relevant prefix budgets,
the first-one endpoint, and the terminal cycle identity. It performs no
numerical search and has no adjustable cutoff. The universal padding
conclusion follows from the displayed invariant.

The target 63 does converge. This is an obstruction to the proposed
universal selection mechanism, so a complete proof needs a different
handoff or an independent terminal-target resolution for this pair.

## Validation

The module is checked with Lean 4.34.1 core and
`-DwarningAsError=true`. It uses no `sorry`, `native_decide`,
or custom axiom. All existing source modules remain unchanged.
