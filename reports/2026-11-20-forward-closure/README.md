# Forward Collatz closure investigation — 20 November 2026

**Collatz has not been resolved by this work.** This packet reconstructs
and extends the classification of ordinary representatives retained by the
latest merger filter, constrains
short asynchronous mergers, derive exact forward consequences of an
all-word inverse potential, and identify why two proposed closure routes
still lack a proof.

The main conclusions below have written proofs and separate mathematical
agent review. Their finite arithmetic interfaces were replayed exactly.
They are research results for review, not a claim of formal verification
or an official institutional announcement.

## 1. Exact classification of persistent convergent rows

The invariant and nonnegative classification in this section also appear
in concurrent [PR #148](https://github.com/GettysburgResearch/collatz/pull/148),
frozen at 6ff18e4f63be8f3bece76215fcfe44d83b001d7f and discovered during
the final publication readback. Its convention is $g=-\kappa$.
Our derivation is an independent reconstruction of that overlapping
result. The negative-class results, Fibonacci diagonal bound and
shifted-power rigidity below are separate extensions.

For a source that reaches 1, let $d$ be its first-hit shortcut time, $a$
its number of odd inputs, and $\kappa=d-2a$. Two such sources eventually
have the same state and the same odd count at a common clock exactly when
their $\kappa$ values agree.

Among sources congruent to 1 modulo 3, the convergent rows retained at
every eligible depth of PR #146's filter are precisely the least sources
in their $\kappa$ classes. All nonnegative minima are explicit:

$$m_{2r}=4^r,\qquad m_1=7,\qquad
m_k=5\cdot2^{k-2}\quad(k\ge3\text{ odd}).$$

This adds the persistent family $10,40,160,\ldots$ and row 7 to the
previously identified powers of four. Twelve negative minima are also
certified by complete bounded enumeration; for example $m_{-11}=31$.
Thus 31 survives the filter forever while reaching 1 in 67 shortcut
steps. Persistence alone cannot diagnose a counterexample.

The same investigation proves a limitation of the shifted-power tail
reduction. Among the $2^j$ lower rows at separation exponent $j$, at most
$F_{j+3}$ have already reached 1 by time $j$. Their fraction is
$O((\varphi/2)^j)$, which tends to zero exponentially. A theorem for
each fixed row's eventual tail does not cover the natural growing
diagonal of rows.

This diagonal limitation concerns use of the condition $j\ge d(n)$
uniformly over growing rows. It does not contradict PR #148's treatment
of the finitely many pre-tail exceptions within its explicitly classified
sector.

[Full classification and proof](../../research/persistent-defect-classes/README.md).

## 2. Short shifted-power mergers are rigid

For $c,d\in\{0,1,2\}$, any actual merger

$$T^p(3^k+c)=T^q(3^l+d)$$

with unequal clocks has $\max(p,q)\ge\min(k,l)$.
Below that threshold, exact two-word cancellation forces equal clocks,
matching homogeneous powers, and matching affine constants.
Such a certificate propagates along a specified progression of exponents.

This supplies a genuine ordinary certificate-propagation rule and a
linear clock lower bound. It does not construct a merger for every
exponent.

[Proof and scope](../../research/persistent-defect-classes/SHIFTED_POWER_RIGIDITY.md).

## 3. An exact potential, and an audit of its missing global bound

On ternary units, define

$$W(z)=\sup_{\text{legal inverse words}}(8k-5A),$$

including the empty word and requiring every endpoint to remain a unit.
The elementary source-cover proof gives

$$h\{W\ge B\}\le(5/6)^B.$$

Nevertheless $\{W=\infty\}$ is dense and $G_\delta$. No finite ternary
observation separates a supplied ordinary integer from that null set.

On an actual escaping ordinary orbit, set

$$c_*=\frac3{\log_2(3/2)},\qquad Z(n)=W(n)-c_*\log_2(n+1).$$

Exact exponent-one cancellation and the count of longer-division events
give

$$\liminf\frac{Z(n_k)}{\ln\ln n_k}
\ge\frac{c_*-5}{\ln(\log_2 3)}
=0.2790812603\ldots>\frac14.$$

Every nontrivial positive ordinary cycle also forces infinite $W$.
These conclusions would be contradicted by a suitable global ordinary
upper bound. **No such bound is proved.**

The independent audit found and proved an important equivalence:
all the proposed global upper-bound shapes are equivalent to

$$\text{Collatz holds}\quad\text{and}\quad W(1)<\infty.$$

They therefore cannot be presented as a proof obtained by substituting
a Haar estimate for an ordinary pointwise estimate. If $W(1)$ is finite,
$W(n)\le5\log_2n+W(1)+1$ is proved on the actual basin of 1. Extending
that statement to another component is precisely an unsupported step.

[Packet overview](../../research/forward-inverse-defect/README.md) ·
[Exact closure boundary](../../research/forward-inverse-defect/CLOSURE_BOUNDARY.md).

## 4. Explicit arithmetic controls

For any positive odd ordinary unit, fixed binary and ternary precisions,
and real floor, the construction supplies a positive **noninteger
rational** cycle agreeing at both precisions, remaining above the floor,
and having infinite $W$. The common reduced denominator is greater than
one and coprime to six; it is never discarded.

There are also immediate ordinary convergers

$$n_q=\frac{2^{3^{q+1}+1}-1}{3},\qquad U(n_q)=1,\qquad W(n_q)\ge3q.$$

The last inequality is a certified finite-word lower bound; it does not
establish finiteness of the full supremum. Large observed scores are
compatible with immediate forward convergence.

[Construction and proof](../../research/forward-inverse-defect/RATIONAL_CYCLES.md).

## 5. The inverse operator's exact remaining boundary

Using the source-qualified ordinary harmonic trace from PR #145, the
new note computes the strong asymptotic limit
$A=\operatorname{s-lim}(P^*)^nP^n$. It is zero on periodic basins.
An escaping component contributes infinitely many rank-one clock-level
blocks with eigenvalues approaching one. Hence

$$A\text{ compact}\iff A=0
\iff\text{every ordinary orbit is eventually periodic}.$$

This is not cycle exclusion. Compactness remains unproved.
Moreover, for every finite time and every finite height cutoff,
both physical-tail operator norms are exactly one. This remains true
when the time is any finite function of the cutoff, even if Collatz is
true. Finite-time norm contraction cannot prove this compactness.

The general operator mechanism is credited to established weighted-shift
theory; the new note identifies the Collatz quantities and proves the
explicit arithmetic truncation bounds.

[Operator packet and exact comparison controls](../../research/asymptotic-inverse-operator/README.md).

## Verification actually executed

Five research programs were run from this complete checkout, using normal
Python with exact integers or rational numbers. All passed.

| Replay | Executed scope |
|---|---|
| Potential | 6,558 residue comparisons between independent path and source-domain implementations; 480 higher-lift checks; 667 actual forward edges; all sources 1–32; eight immediate-converger controls; three rejected mutations. |
| Persistent classes | 67,584 defect identities; 2,048 exact products; 17 nonnegative minima through source 65,536; 12 negative minima; 8,191 prefix source/depth pairs; 1,300 preimage counts; 11 exact small-unit closing inequalities. |
| Shifted powers | 44,648 actual merger pairs, including 41,222 unequal-clock pairs; 194 exponent-progression replays. |
| Rational cycles | Nine noninteger rational cycles and 1,405 inverse edges; seven immediate-converger controls; exact local congruences, valuations, positive floors and nontrivial denominators. |
| Operator controls | 4,160 telescoping identities; 1,188 prefix-extension identities; 21 shared-prefix paths; 32 tail witnesses; 1,644 inverse edges; three rejected mutations. |

Reports:
[potential](potential-report.json),
[persistent classes](persistent-defects-report.json),
[shifted powers](shifted-power-report.json),
[rational cycles](rational-density-report.json),
[operator controls](operator-controls-report.json).

The published content commit
[9dcb3b35a8e407af7635469f5643e9fa2f5a1077](https://github.com/GettysburgResearch/collatz/commit/9dcb3b35a8e407af7635469f5643e9fa2f5a1077),
with tree 755adedd59c3c5ed4a26d41689a98bad849e9398, passed all 11 commands
of the clean-checkout validator with regressions. The
[exact receipt](content-validation.json) was generated in a clean complete
checkout fetched from that published commit. It is attached by this later
documentation commit, which is not represented as self-certified.
Repository integrity and bounded arithmetic replay do not establish
the missing infinite pointwise assertions.

## Review and dependencies

- [Frozen source pins and primary-literature attribution](PROVENANCE.md).
- [Independent arithmetic and operator review](ARITHMETIC_REVIEW.md).
- [Independent classification and closing-equivalence review](CLASSIFICATION_REVIEW.md).
- [Separate forward-defect review and basin-only bound](FORWARD_REVIEW.md).

The source-qualified statements are isolated: all-negative-defect-class
existence uses PR #147 under UQ(6), and the operator packet imports the
harmonic-trace and reciprocal-summability inputs from PR #145.
The core finite-word potential, ordinary drift, rational construction,
nonnegative class classification, Fibonacci bound and shifted-power
rigidity have local proofs.

## Unresolved result

No universal forward descent, complete merger selector, denominator-one
cycle exclusion, or proof of the required ordinary potential bound has
been obtained. This publication preserves the exact unsupported steps
instead of marking the conjecture solved.
