# Asynchronous terminal normalization and the two local repairs

**PROVED IN LEAN: ordinary reductions and exact conditional equivalences.**
**OPEN: both local repair implications and full Collatz closure.**

The map is the positive ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\qquad C=\{n>0:\exists d\ge0,\ T^d(n)=1\}.
\]

`TerminalFive.lean` imports the dependency-free `Collatz.Closure` toolbox
from PR174 at `7034109ed60a26bc49824e1ed43c239ceca81194`. The map and basin
are the imported definitions, not newly assumed predicates. Lean 4.34.1
checks the whole file, including the ordinary arithmetic identities.
There are no added axioms, `sorry`, or `native_decide` calls.

## Frozen comparison and dependency boundary

| Source | Full head | Relevant statement |
|---|---|---|
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | `research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md`: balanced same-clock terminal reduction, effective last-return deadline, ordinary terminals in every surviving finite binary prefix. |
| PR146 | Same head | `research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md`: a failed five comparison generates long blocks of failed comparisons; the required opposing upper bound remains open. |
| PR171 | `2bd243b3e05eaa5543adeb2894637b053c9662ca` | `research/adaptive-closure-20261121/VALUATION_ONE_TRANSPORT.md`, V5: the valuation-one two-antecedent route has the form \(u,5u\in C\Rightarrow5u-2\in C\) on its specified unit domain. |
| PR171 | Same head | `research/adaptive-closure-20261121/AFFINE_SECTION_ROOT_RETURN.md`: the complete positive return kernel has infinite subcritical pressure; Haar coverage does not supply a pointwise closure proof. |
| PR157 | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md`, GCM-002: forward-five closure on certified odd ternary units is equivalent to full Collatz. Its all-lift certificate is **not formalized or reverified in this module**. |

The Lean results below prove equivalences to **forward-five closure**. The
further implication to full Collatz uses the separately pinned PR157
criterion. No Lean theorem in this module claims to have formalized that
external certificate or proved either closure statement.

## TF1. A failure has no late proportional return, even at independent clocks

Call \((x,5x)\) a failed comparison if \(x\in C\) and \(5x\notin C\).
Suppose an ordinary certificate \(T^d(x)=1\) is supplied. Then

\[
\boxed{\quad
s\ge d\ \Longrightarrow\ T^t(5x)\ne5T^s(x)
\quad\text{for every }t\ge0.\quad}
\tag{TF1}
\]

Indeed \(T^s(x)\in\{1,2\}\) after clock \(d\). Its five-multiple is
therefore 5 or 10, both of which have explicit paths to 1. Equality would
give an ordinary path from \(5x\) to a convergent value, contradicting
failure.

This argument needs neither equal odd-input counts nor equal clocks. It
also needs no analytic return estimate or absolute deadline. Unlike the
unconditional last-root bound in PR146, it is a statement **under the
hypothesis that the comparison fails**.

Lean names: `five_after_hit`, `failure_no_late_return`.

## TF2. Component-preserving asynchronous terminal normalization

Define an **asynchronous terminal** to be a positive source \(q\) with

\[
T^t(5q)\ne5T^s(q)
\qquad\text{for every }s>0\text{ and }t\ge0.
\tag{4}
\]

Every failed pair with a certificate \(T^d(x)=1\) has a failed
asynchronously terminal descendant. More precisely, there exist natural
\(q,s,t,e\) such that

\[
\begin{gathered}
s+e=d,\qquad T^s(x)=q,\qquad T^t(5x)=5q,\\
T^e(q)=1,\qquad5q\notin C,\qquad q\text{ satisfies (4)}.
\end{gathered}
\tag{TF2}
\]

If the current source is not terminal, choose a return with source clock
\(s>0\). TF1 gives \(s<d\). The new source has a certificate of length
\(d-s<d\), and the failed target transfers by the exact ordinary return.
Strong induction on the supplied source clock proves (TF2). The two
ordinary components are preserved throughout; the source and target
clocks may change independently.

This is an existence theorem, using classical choice for a return when
one exists. It is **not** an algorithm deciding absence of all future
returns, and no bound on the target clock \(t\) is asserted. The source
clock strictly decreases at each nontrivial normalization step, even if
the numerical source value increases.

Consequently,

\[
\boxed{\quad
(\forall x\in C,\ 5x\in C)
\iff
(\forall q\in C\text{ satisfying (4)},\ 5q\in C).
\quad}
\tag{TF2a}
\]

Lean names: `failure_has_async_terminal_descendant`,
`forward_five_iff_async_terminals`.

### Exact controls for the new terminal notion

The source 5 belongs to PR146's balanced-terminal rank-one family, but it
is not an asynchronous terminal:

\[
T^4(5)=1,\qquad T^{12}(25)=5=5T^4(5).
\]

Thus the asynchronous terminal set is genuinely smaller. It is still
nonempty. The source 17 is an asynchronous terminal, although both arms
converge: \(T^9(17)=1\) and \(T^8(85)=1\). After the target's first
step it follows \(128,64,\ldots,1,2,1,\ldots\). Direct finite checks
before those two certified clocks, followed by the \(1,2\) cycle, prove
there is no proportional return at independent clocks.

Lean proves both controls in `five_not_async_terminal` and
`seventeen_successful_terminal`. Terminality is not nonconvergence.

## TF3. A rank-minimal failure certifies every strict future comparison

There is a second, stronger normalization that need not remain in the
same two components. If any failed five comparison exists, choose one
with a certificate clock \(d\) least among **all** failed comparisons
and all their finite source certificates. Then

\[
\boxed{\qquad
q\in C,\quad5q\notin C,\quad
5T^s(q)\in C\quad\text{for every }s>0.
\qquad}
\tag{TF3}
\]

For \(0<s<d\), the source suffix has a certificate of length \(d-s\),
so another failure there would contradict the choice of \(d\). For
\(s\ge d\), the cycle argument in TF1 applies. A return of any kind in
(4) would now make \(5q\) converge, so this witness is also an
asynchronous terminal.

The normalized source is odd. If it were even, then
\(T(5q)=5T(q)\), whereas the latter value is certified by (TF3).

This chooses a least **finite source-certificate clock**, not a least
nonconvergent hitting time. No hitting time is assigned to the failed
target. Nor is numerical height assumed to decrease along the source
trajectory.

Lean names: `failure_has_rank_minimal`, `rank_minimal_successor_closed`,
`failure_has_terminal`, `rank_minimal_odd`,
`forward_five_iff_successor_closed`.

## TF4. Exactly two local arithmetic repair implications suffice

Consider the following statements, with both certified antecedents
explicit:

\[
\begin{aligned}
\mathsf A:\quad&
\forall k\ge0,\quad
3k+1\in C\ \land\ 15k+5\in C
\ \Longrightarrow\ 15k+4\in C,\\
\mathsf B:\quad&
\forall k\ge0,\quad
6k+5\in C\ \land\ 30k+25\in C
\ \Longrightarrow\ 30k+23\in C.
\end{aligned}
\tag{5}
\]

Equivalently, \(\mathsf A\) asks for
\(u,5u\in C\Rightarrow5u-1\in C\) on \(u\equiv1\pmod3\),
and \(\mathsf B\) asks for
\(u,5u\in C\Rightarrow5u-2\in C\) on \(u\equiv5\pmod6\).

The exact conditional equivalence is

\[
\boxed{\qquad
\forall x\in C,\ 5x\in C
\quad\iff\quad \mathsf A\ \land\ \mathsf B.
\qquad}
\tag{TF4}
\]

Here is the whole ordinary calculation. At an odd source, split its two
residue classes modulo four:

| Source | Certified smaller-clock source | Five-multiple of that source | Target endpoint requiring repair |
|---|---|---|---|
| \(x=4k+1\) | \(T^2(x)=3k+1\) | \(15k+5\) | \(T^2(5x)=15k+4\) |
| \(x=4k+3\) | \(T(x)=6k+5\) | \(30k+25\) | \(T(5x)=30k+23\) |

The two middle entries are certified for the minimal witness of TF3.
Thus a failure would violate at least one repair. More constructively,
induct on any supplied source certificate clock. The induction
hypothesis proves \(5T(x)\in C\). For an even source, ordinary
commutation \(T(5x)=5T(x)\) completes the step. For \(x=4k+1\),
halving \(5T(x)=2(15k+5)\) supplies the antecedent in \(\mathsf A\).
For \(x=4k+3\), \(5T(x)=30k+25\) supplies the antecedent in
\(\mathsf B\). The base case is the explicit certificate for 5.

Conversely, forward-five closure proves each repair by taking the
corresponding source \(4k+1\) or \(4k+3\), whose convergence follows
from the first antecedent. This direction does not need the second
antecedent.

Lean names: `OneOffsetRepair`, `TwoOffsetRepair`, `one_step_repair`,
`forward_five_of_offsets`, `offsets_of_forward_five`,
`forward_five_iff_offsets`.

The second repair includes PR171's already isolated valuation-one
two-antecedent obstruction. This packet does not claim that obstruction
as new. The additional content relative to the frozen comparison is the
complete two-branch equivalence, its global source-rank witness, the
stronger asynchronous terminal normalization, and machine-checked
ordinary proofs. Neither branch has been discharged.

## TF5. What the normalization does and does not settle

The normalized failed target cannot be reached from any certified
five-multiple farther along the source path. That rules out a proof
which merely consumes the source certificate and silently transfers
five-closure across its next ordinary step: the two exact missing
transfers are (5).

A different certificate for the source, with more steps but a smaller
well-founded certificate rank, could still help. TF3 uses source clock
only and does not rule out such changes. The separate C5 prefix
certificate below provides actual examples of longer certificates with
strictly smaller source states; it does not cover every terminal or
either repair implication.

The first unsupported step in this lane is to prove at least one of
\(\mathsf A\) or \(\mathsf B\) from the supplied ordinary antecedent
certificates, and ultimately both, or to give a complete alternative
descent for the asynchronous terminals. Haar return probabilities,
finite-prefix coverage and a formal conditional equivalence do not
supply that implication.

## C5-G. Exact input for a rank-changing prefix kernel

The separate `c5-prefix-certificate.json` records both C5 bypasses from
the earlier note whose SHA256 is
`dc846bbce7fa74f1235cab5049a8ac7fd269bab666abde656c51c86c977cb258`.
The generator `make_c5_prefix_certificate.py` verifies all 138 ordinary
shortcut steps as identities of affine functions of every natural
parameter \(t\). States exclude the common endpoint, which is recorded
separately. This is exact affine data for a later Lean prefix kernel,
not a claim that the generator itself proves an unbounded search.

There is a stronger guard than the old paired-height statement. With
\(X(k)=128k+1\), **every state of the child upper prefix is strictly
below the parent's initial \(X(k)\)**:

| Rule | Parent initial upper | Maximum child upper prefix state | Slope ratio |
|---|---|---|---|
| A | \(241864704t+215856897\) | \(100663296t+89838914\) | \(8192/19683\) |
| B | \(241864704t+153151233\) | \(201326592t+127482050\) | \(16384/19683\) |

Both affine coefficients decrease strictly. Thus any multiset rank that
permits replacing a removed state by finitely many strictly smaller
states can absorb the added ten odd inputs and fourteen or fifteen
shortcut clocks on these two source families. The unchanged suffix is
retained. This is a genuine compatibility fact between the old
height contractions and a certificate rank; it is not coverage of all
possible certificates.

There is also a shorter exact target merger than the original displayed
shared endpoint. For both rules,

\[
T^{14}(Y(k'))=Y(k)\quad\text{in A},\qquad
T^{15}(Y(k'))=Y(k)\quad\text{in B},
\qquad Y(k)=64k+1.
\]

The JSON supplies these shortened prefixes as well. The parent target
prefix is empty in this representation. Every state of the shortened
child target prefix is also strictly below the parent's initial
\(Y(k)\). The maximum is \(80621568t+71952299\) in A and
\(100663296t+63741026\) in B. This last guard applies to the shortened
prefix before it reaches \(Y(k)\); the original longer displayed target
prefix includes the subsequent ordinary rise above \(Y(k)\).

## Validation boundary

The core Lean module compiled with exit code 0 on Lean 4.34.1. Its
`#print axioms` output lists only the standard Lean foundations
`propext`, `Quot.sound`, and, for the classical selection statements,
`Classical.choice`; no `sorryAx` appears. The exact small terminal controls
are checked with kernel `decide`.

The C5 generator passed its declared affine identities, parity,
positivity, endpoint equality, early target merger and coefficientwise
source-prefix guards. Its output is intended for the root agent's
independent Lean replay. No broad historical regression suite was run
for this narrow new-work checkpoint.
