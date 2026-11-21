# Attacking the forced dyadic section

## Status and exact input

**Full Collatz convergence remains OPEN.** This continuation uses the new
forward-section theorem in [PR #173](https://github.com/GettysburgResearch/collatz/pull/173),
frozen at `fa0c9e2a2851e6324391e39c17afcb5913185aec`. The goal was to turn its
unconditional forward visit into a complete induction or a well-founded
return rank. The results below are proved statements about that same ordinary
section; no universal descent assumption is supplied as an axiom.

For the shortcut map

\[
T(n)=n/2\quad(n\text{ even}),\qquad T(n)=(3n+1)/2\quad(n\text{ odd}),
\]

put \(d(n)=\lfloor\log_2 n\rfloor\). The source marks precisely the odd integers
satisfying

\[
(d(n)+1)(n-2^{d(n)})\le70\,2^{d(n)}.
\]

The source proves that every positive ordinary start reaches a mark at a
shortcut clock less than \(4\lfloor\sqrt n\rfloor+\lfloor\log_2n\rfloor\),
and proves an explicit density-zero counting bound for the marks. These are
**upstream results**, not new contributions of this continuation.
The four files in [vendor/pr173](vendor/pr173) are exact, unmodified copies;
[SOURCE.json](vendor/pr173/SOURCE.json) records their paths, commit, and hashes.

Write \(R(n)\) for the first marked point at a strictly positive clock.
The source proves its totality and

\[
\texttt{Universal}\quad\Longleftrightarrow\quad
\forall n>1\text{ marked},\ \exists k,\ R^k(n)<n.
\]

The existence of this variable number of returns for every marked start is
still unproved. None of the results below changes that status.

## 1. An exact constructive transfer from a smaller offset

[BandOffset.lean](CollatzGlobalClosure/BandOffset.lean) proves the following
without a statistical or asymptotic hypothesis. If \(a>0\) and
\(T^k(a)<a\), then for every natural \(v\),

\[
T^k(a+2^kv)<a+2^kv.
\]

Indeed the actual shared parity prefix has an identity

\[
2^kT^k(a)=3^p a+C,\qquad C\ge0,
\]

so descent forces \(3^p<2^k\). The exact lift formula
\(T^k(a+2^kv)=T^k(a)+3^pv\) then proves descent at the **same clock**.
In particular, descent of the offset transfers to \(2^d+a\) whenever
\(k\le d\). A supplied hitting certificate for \(a>1\) gives such a witness
when its clock fits this guard. The terminal offset \(a=1\) is handled
separately: \(2^d+1\) descends in two shortcut steps for \(d\ge2\).

The contrapositive is also formalized: if \(2^d+a\) survives at or above
itself through clock \(d\), then its smaller offset survives through those
same clocks. This is a finite statement, not an infinite nonconvergent orbit.
[SectionBridge.lean](CollatzGlobalClosure/SectionBridge.lean) proves equality
with the source's map and exports the transfer in that map.

### Why the binary-length guard does not follow from the band

For every \(m>0\), define

\[
a_m=2^{4m}-1,\qquad n_m=2^{5m}+2^{4m}-1.
\]

Lean proves that \(n_m\) is marked, \(d(n_m)=5m\), and

\[
2^m(n_m-2^{d(n_m)})<2^{d(n_m)}.
\]

Nevertheless, at **every** clock \(0\le j\le5m\),

\[
T^j(n_m)\ge n_m,\qquad T^j(a_m)\ge a_m.
\]

The relative offset is exponentially smaller than the original section
width. This rules out the proposed binary-length clock bound even for these
much thinner marks, beyond any finite exception range.

The general proved statement is stronger than that example: for any
\(u>0\), if \(2^{b+h}\le3^b\), then

\[
T^j(2^bu-1)\ge2^bu-1\qquad(0\le j\le b+h).
\]

The first \(b\) steps are genuinely odd steps. Their multiplicative surplus
is large enough that even an all-halving suffix of length \(h\) could not
give descent. Taking \(b=rm\), \(b+h=qm\), with
\(r<q\) and \(2^q\le3^r\), gives the analogous obstruction for other
rational relative-width exponents. This is not a nonconvergent family.

## 2. A first-return resource can reset upward

The source already disproves strict decrease of ordinary size at every
first return. A natural repair is to charge the long run of trailing binary
ones, measured by \(\kappa(n)=v_2(n+1)\). During an odd shortcut step inside
such a run this depth falls by one.

[SectionResetReturns.lean](CollatzGlobalClosure/SectionResetReturns.lean)
proves that this resource can reset before the next marked return:

\[
\boxed{\forall C,L\in\mathbb N\;\exists n>L:\quad
n>1,\quad n\text{ marked},\quad \kappa(n)=1,\quad
R(n)>Cn,\quad\kappa(R(n))>C.}
\]

The endpoint is the **first strictly positive return**, not a later chosen
mark. The theorem holds beyond every finite cutoff.
It excludes every coordinatewise monotone function of ordinary size and
trailing-one depth as a strict first-return rank, with any preordered
codomain. Nonlinear functions and ordinal-valued monotone ranks are included.

The explicit seed and the complete proof are in
[SECTION_RESET_RETURNS.md](SECTION_RESET_RETURNS.md). The seed has depth one;
its first two steps expose a very long odd run. A rational-grid visit and
integer-power separation locate the first return inside that run and bound
it away from the beginning. Those two facts give both increases.

An independently reduced finite example in
[MarkedResetWitness.lean](CollatzGlobalClosure/MarkedResetWitness.lean) uses

\[
n=(2^{525}\cdot3073-5)/3,\qquad
m=2^{512}\cdot3^{11}\cdot3073-1.
\]

Both endpoints are marked, \(T^{13}(n)=m>n\), their binary exponents are
\(535\) and \(541\), and their trailing-one depths are \(1\) and \(512\).
This calculation uses ordinary kernel reduction and has no axiom dependency.
It is a finite check alongside the unbounded theorem, not its proof.

## 3. High-bit marking leaves every finite odd-source prefix possible

[MarkedCylinders.lean](CollatzGlobalClosure/MarkedCylinders.lean) constructs,
for every \(r<2^k\) with \(r\) odd and every cutoff \(B\),

\[
n=2^{2(k+B+1)}+r>B.
\]

It proves exact markedness, \(n\equiv r\pmod{2^k}\), equality of the first
\(k\) parity inputs and odd counts, and the full affine endpoint formula.
The restriction to odd residues is essential because marks are odd.
Thus the band does not itself enforce a fixed finite future parity pattern.
The statement is about actual natural numbers, not only compatible residues
or a 2-adic completion.

## 4. Complete ordinary words and interval selection

[BandWord.lean](CollatzGlobalClosure/BandWord.lean) constructs ordinary
source/endpoint pairs for every \(p\ge2\), \(t\ge p+2\), and
\(L\ge5\cdot3^p\). The endpoint lies in

\[
L<m<L+8\cdot3^p,
\]

both source and endpoint are \(1\pmod4\), and

\[
T^t(n)=m,\qquad
3^p n+5\cdot3^{p-1}=2^t m+2^{p+1}.
\]

The proof supplies two ordinary CRT constructions, an explicit interval
representative, exact natural division, and the whole legal forward word:
one odd step, one halving, \(p-1\) odd steps, and the remaining halvings.
There is no assumed parity realization or omitted source positivity guard.

This constructor chooses an endpoint in an interval. It does **not** prove
that a particular prescribed endpoint satisfies the required ternary
congruence at a nearly balanced clock. That distinction prevents turning
the construction into a universal recursive selector without another proof.

## 5. Equal features exclude arbitrary two-feature ranks

[BandCollision.lean](CollatzGlobalClosure/BandCollision.lean) combines that
ordinary-word constructor with the source's rational-grid approximation.
For every cutoff \(B\), it constructs distinct marked \(n,m>B\) and \(t>0\)
such that

\[
T^t(n)=m,\qquad d(n)=d(m),\qquad
n\equiv m\equiv1\pmod4,\qquad (B+1)2^t\le n.
\]

In particular, \(\kappa(n)=\kappa(m)=1\). The last inequality retains an
essential domain guard: **every intermediate ordinary state exceeds the
cutoff**, not merely the two endpoints.

[SectionFeatureRanks.lean](CollatzGlobalClosure/SectionFeatureRanks.lean)
proves the complete return-path composition. A rank strictly decreasing at
each positive marked return would strictly decrease along the displayed
path, yet any function of \((d(n),\kappa(n))\) has the same value at its two
ends. Thus **no function of binary exponent and trailing-one depth**, valued
in any preorder, is a strict first-return rank beyond a finite cutoff.
Unlike the preceding size/depth obstruction, this result does not assume
monotonicity of the function. It is an obstruction to every-return descent,
not to eventual descent after a variable number of returns.

The construction uses \(N=B+64\), \(P=2^{8N}\), and
\(Q=\lfloor P/(N+1)\rfloor\). Near-balanced powers of two and three and
the exact CRT word place both endpoints in \([P,P+8Q]\), within the same
marked octave. The [complete argument](EQUAL_FEATURE_COLLISIONS.md) records
the ratio estimates, interval margins, source positivity, actual path, and
intermediate-state floor.

## 6. Where the full-theorem attempts stop

The offset route has two separate obligations. First, knowing that a smaller
offset converges supplies no bound putting its witness inside the available
\(d\)-bit prefix. After that prefix expires the exact unresolved pair is
\((T^d(a),T^d(a)+3^{p_d})\). No complete certificate transfer across this
ternary difference was obtained.

Second, ordinary descent below a marked start is weaker than descent among
marked returns. The lower ordinary endpoint may be unmarked and its next
marked visit may overshoot the starting mark. An induction only on marked
integers cannot silently assume convergence of every smaller ordinary
integer. A global least counterexample may itself be unmarked. The
[offset attempt record](BAND_OFFSET_ATTEMPT.md) retains this distinction.

The rank route has to handle the upward reset proved above and must show
actual strict descent in a well-founded domain. The proved obstruction is
to strict decrease at **every** first return within its stated rank class;
it does not exclude a rank on richer state or eventual descent after a
variable number of complete returns. That latter universal assertion is the
remaining source criterion, and it is still open.

The final [segment-minimum attempt](SEGMENT_MINIMUM_ATTEMPT.md) re-roots the
phase estimate at an actual ordinary minimum, follows the entire supplied
offset certificate, and examines the published inverse mesh cost. It records
the exact missing height comparison and the scope of the written cost bound;
no additional closing theorem is claimed there.

## Replay and evidence

The package pins Lean 4.34.1 and mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The source-manifest check and direct
compiler replay are in [build_band.py](build_band.py). The driver writes each
project module from its source into a fresh output directory, treats warnings
as errors, and records commands, source hashes, outputs, exit codes and axiom
reports. It reuses only the pinned mathlib/dependency cache. `--full` also
rebuilds the earlier proof modules and the project entrypoint.

No search output, observed finite sample, custom axiom, `sorry`, `native_decide`,
or unsafe evaluator supplies a mathematical premise. The preserved source
pin identifies exactly which upstream theorem this continuation builds on.
No scholarly novelty priority is claimed without a literature comparison.
The [actual published-checkout validation](../../reports/lean-global-closure-20261121/band/VALIDATION.md)
records the successful fresh build of all 17 compilation units, its 96 axiom
reports, and the separate complete-checkout repository gate.
