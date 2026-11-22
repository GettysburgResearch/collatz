# Combining source-certificate descent with ordinary target descent

## Result

`lean/Collatz/SourceTargetInduction.lean` proves that the existing complete-source multiset induction can be combined with a second, inner induction on the current ordinary target. The same supplied source certificate is retained during an inner step. A paid source rewrite may change both source and target because it strictly decreases the outer grade.

This resolves a general **rank-compatibility** issue raised by PR183's new carry/compression bridge. It does not prove that the combined cases cover every input.

The module contains **12 public theorems**, compiled and audited with Lean 4.34.1, `-j1 -DwarningAsError=true`, exit 0. It adds no conjectural axiom. The frozen `AffineDispatcher.lean` and earlier packets are unchanged.

## 1. Precise comparison with the new PR183 carry packet

The new remote source was read at commit
`68345f60a4f757acb42a69a4ac95910f8ce26163`:

- `research/profound-step-20261122/mergers/ARBITRARY_DEBT.md`.
- `research/profound-step-20261122/mergers/AffineCarry.lean`.
- `research/profound-step-20261122/mergers/CarryCapture.lean`.
- `research/profound-step-20261122/arithmetic/CARRY_COMPRESSION_BRIDGE.md`.
- `research/profound-step-20261122/arithmetic/BlockCompression.lean`.

Those modules were inspected through `git show`; this comparison is not a claim to have replayed PR183's build.

### Substantial overlap

PR183 writes a target as \(n+D=3^p r\), with nonnegative debt \(D\), and uses the positive complementary map

\[
S(b)=\begin{cases}b/2,&b\text{ even},\\(3b-1)/2,&b\text{ odd}.\end{cases}
\]

Our signed offset is \(d=-D\). For positive \(b\), the finite signed shortcut satisfies \(T_{\mathbb Z}(-b)=-S(b)\), with the same parity sequence. Consequently PR183's `gap_transport` / `CarryRun` and our `affine_gap_transport` / `Dispatch` are the same renewed-horizon arithmetic mechanism on nonpositive offsets. Their all-gap scope must not be counted as a distinct new debt mechanism in each packet.

Our signed transition also permits positive offsets, and our module explicitly proves finite dispatch existence and the actual complete-source normal-form alternative. These are differences of interface and scope, not a proof of successful universal capture.

### Differences in capture budgets

PR183's `prefix_pays_padding` starts from old initial even exponent zero. A consumed prefix with maximum gap \(m\) pays any new initial exponent \(f<m\). Its coefficient test is \(3^p\le2^{f+1}\).

Our checkpoint8 and dispatcher rules for an existing positive initial exponent \(e\) retain the old even grade when useful, and pay the exact maximum

\[
f=\max\bigl(e,\max_{a\in W}(a-1)\bigr).
\]

They also retain the full numerical capture test including the signed offset, and allow independent-clock partner mergers. PR183's zero-initial-exponent case complements this interface. Neither budget automatically proves eventual capture of an arbitrary carried target.

### PR183's genuinely added successful language

The prefix language \(1\{2,3\}^{*}2\) is a real improvement over PR185's earlier \(1\{2,3\}^{*}21\). PR183 proves that it reaches \(3u-1\), then pays for source \(2u\) with one initial halving while retaining the original tail. This result is credited to PR183; it is not presented here as a newly discovered language.

Its debt-amplification family also has a useful, correctly scoped interpretation: intermediate exponents are unbounded even for prefixes of complete certificates, but the completed family has a large final source gap, and its targets already admit ordinary descent. It is not a remaining all-low counterexample to the combined program.

## 2. The joint induction hypotheses

At a current state with source \(S\), target \(n\), and supplied powered certificate \((e,A)\), retain the existing PR177 hypothesis

\[
\operatorname{Hyp}(\operatorname{Interval},\Gamma(e;A)).
\]

It supplies every activated child comparison whose complete source grade is strictly smaller. The child target may increase.

The new inner hypothesis is

```lean
def SameSourceHyp (source target : Nat) : Prop :=
  ∀ child, Interval source child → child < target → Basin child
```

During this induction the source, initial even exponent, and entire source word remain fixed. No certificate for the smaller target is chosen or charged to the rank.

`JointComplete` asks a local solver to close every activated query when both hypotheses are available:

```lean
def JointComplete : Prop :=
  ∀ source target e word,
    Interval source target →
    PoweredCertificate source e word →
    Hyp Interval (grades e word) →
    SameSourceHyp source target →
    Basin target
```

The theorem `complete_of_joint` fixes the actual supplied source certificate and proves all its target queries by strong induction on the target. This discharges `SameSourceHyp` and produces the existing `Complete Interval` without changing that interface. PR177's already-proved outer source-grade induction then applies.

Thus the effective order is lexicographic: complete source grade first, ordinary target second. The Lean proof uses the two nested inductions directly rather than introducing an unproved product-order termination principle.

The checked closing chain is

\[
\texttt{JointComplete}
\Longrightarrow\texttt{Complete Interval}
\Longrightarrow\forall n>0,\ \texttt{Basin}\ n.
\]

The universal local solver is a hypothesis. The module does not assert it.

## 3. Actual ordinary descent and smaller partners are compatible

The interval \(0<n\le2S+1\) is downward closed among positive integers. Therefore any actual descent

\[
0<T^k(n)<n
\]

stays inside the same source interval. `same_source_descent` applies the inner hypothesis to that ordinary endpoint and transfers convergence back through `iterate_basin`.

The more general `same_source_merger` accepts

\[
0<x<n,\qquad T^L(x)=T^R(n),
\]

with independent physical clocks. The smaller partner need not fit the maximal *lower-grade* literal-cut envelope: it is paid instead by the inner target induction, while the source certificate remains unchanged.

This permits source-bounded smaller-partner results such as existing arithmetic rays to be combined with complete-source rewrites in one proof. It does not claim those rays form a complete cover.

**Original-target guard.** The decrease is measured against the original target \(n\) of the current activated query. If an intermediate carry value \(v=T^j(n)\) is larger than \(n\), proving \(T^k(v)<v\) does not meet this condition. One must prove \(T^k(v)<n\), or first pay for a genuinely new source-grade query whose target is \(v\). The theorem's strict inequality preserves this guard explicitly.

## 4. Concrete combined witnesses

`MixedWitness source target old` has three constructors:

1. A previously proved actual basin certificate for the target.
2. An actual independent-clock merger with a positive partner strictly smaller than this current target.
3. A child comparison with its explicit powered source certificate, strict complete-source grade decrease, active interval, and a proved transfer from the child target's basin to the current target's basin.

`mixed_witness_sound` checks all three alternatives against the two hypotheses. `MixedCover` asks for such a witness at every activated supplied source/target state. The theorems

\[
\texttt{MixedCover}\Longrightarrow\texttt{JointComplete}
\Longrightarrow\forall n>0,\ \texttt{Basin}\ n
\]

leave that universal coverage premise visible. The paid branch is compatible with the exact source-tail and partner constructions in `AffineDispatcher.lean`; the smaller-target branch adds the new ordinary descent option without obtaining a fresh uncontrolled source certificate.

## 5. The new PR183 debt family is paid in its actual padded-source query

PR183 gives the ordinary identity

\[
T^5(32a+23)=27a+20<32a+23.
\tag{1}
\]

It is checked in this module as `residue23_descent`, with explicit credit to PR183. `residue23_mixed_witness` then installs the entire class as a sound branch of the combined induction for every current source at which the target is active.

There is also a stronger paid capture for PR183's specific carried shape. Write

\[
r=32a+13,\qquad n=9r+2=32(9a+3)+23.
\]

Equation (1) gives

\[
T^5(n)=243a+101.
\]

If the **already supplied** source is \(S=8r\), halve it once to obtain child source \(4r\), retaining the complete odd word. Its interval ceiling is

\[
2(4r)+1=256a+105\ge243a+101.
\]

The new theorem `residue13_carry_paid_capture` consequently proves

\[
\operatorname{Certificate}(32a+13,A)
\quad\land\quad
\operatorname{Hyp}(\operatorname{Interval},\Gamma(3;A))
\quad\Longrightarrow\quad
\operatorname{Basin}(9(32a+13)+2).
\]

Its rank payment is simply the initial exponent decrease \(3\to2\), with \(A\) unchanged. It needs no inner-target induction for this particular shape.

For PR183's family, \(5r=2^{15k}v+1\) with \(k\ge1\) implies \(r\equiv13\pmod{32}\), so this applies whenever \(8r\) is the actual supplied source of the query.

**Padding guard.** This does not add three initial halvings for free to an earlier query whose supplied source was \(r\) with initial exponent zero. The proof requires the larger source's actual certificate and the corresponding old grade \(\Gamma(3;A)\). If the carry was reached from another source, that earlier proof still owes its own rank payment.

**High-gap scope.** The fully certified variant in PR183 uses source word \([3,\ldots,3,h]\), where \(h\) is even, \(h\ge4\), and \(5\,2^h\equiv8\pmod{3^{5k+1}}\). For \(k\ge1\), \(h=4\) is impossible because \(5\cdot16-8=72\) is not divisible by \(3^6\). Hence \(h\ge6\), and PR177's high-gap dispatcher already provides a different conditional source-grade route. The new paid capture is an exact compatibility result, not the elimination of an alleged surviving all-low obstruction.

## 6. What compression still does not prove

PR183's compression inequality limits repetitions along an actual fixed-source trace, or identifies an actual bounded-period cycle. The long debt family spends a growing source-height budget and therefore does not violate that inequality. Once the word changes, the next block may use a different displacement budget.

The joint kernel now permits a valid direct-descent terminal case to coexist with source-grade capture. The first unsupported global assertion is still coverage: **every required original query must supply one of the accepted mixed witnesses, with all inequalities measured against the correct current target and all source-grade changes paid**. Neither finite transition totality, a bounded-language classifier, nor the absence of a particular debt cutoff proves this.

The source-history, debt and grade data must remain visible when seeking that witness. No terminal debt is declared convergent merely because the supplied source program has ended.

## Verification

The integrated replay uses `check_whole.py` and the exact import/source
manifest `DEPENDENCIES.json`. It compiles the 16 imported project modules,
all three new proof modules, and both separate audits in a fresh output
directory. All 37 public theorem audits are recorded in
[checkpoint9-lean.json](../../../../reports/2026-11-22-whole-repository/checkpoint9-lean.json).
This module contributes 12 of those declarations; its source is unchanged
from the separately successful agent compile and audit.

The PR183 sources were read without replay. The older frozen proof modules
remain byte-identical to their published source pins. The written analytic
and transcendence arguments are outside this formal audit.
