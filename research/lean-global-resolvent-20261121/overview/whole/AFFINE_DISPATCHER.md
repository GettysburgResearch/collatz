# A total affine carry language with literal-source handoffs

## Outcome

`lean/Collatz/AffineDispatcher.lean` supplies a compositional transition language for **every signed affine carry state**, consuming arbitrary finite prefixes of an actual supplied source certificate. Each source edge refreshes exactly the binary horizon consumed on the target. The endpoint retains its literal source suffix, current ternary degree, signed offset, and physical clock.

The module proves a complete finite normalization alternative and integrates it with PR177's existing complete-source multiset rank. It also accepts an independent-clock partner merger after any dispatched prefix.

There are **13 public Lean theorems**, checked with Lean 4.34.1, `-j1 -DwarningAsError=true`. All public declarations were audited. Only standard Lean axioms occur.

This does not prove a universal cover. In particular, capture within one pass over the supplied source certificate is **false**, including for a remaining low-state shape. Section 5 gives the exact failure and credits an existing asynchronous repair. The full question is still whether every residual state admits a rank-paid capture, an independent-clock merger, or a different source rewrite.

## 1. Relationship to the existing work

**Late continuation:** PR183 at `68345f60a4f757acb42a69a4ac95910f8ce26163`
publishes an equivalent nonpositive-offset transition through its positive
complementary map. The [late-head comparison](LATEST_HEAD_INTEGRATION.md)
credits this overlap, its stronger accepted prefix language, and the
new joint source-grade/target induction. The signed lift and finite
dispatcher below remain unchanged; they are not claimed as a separate
historically new debt mechanism.

The following sources were read at their exact published commits:

| Source | Frozen commit | What is retained |
| --- | --- | --- |
| PR177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | The actual positive-gap certificate, literal prefix relation, complete-source grade, and interval induction hypothesis. |
| PR176, checkpoint8 | `03e40fa4d7506ad92682a49c850103b028a11dbe` | `TerminalCarry.lean` and `SourceEnvelope.lean`, imported byte for byte. |
| PR185 | `276be8154f4e867acc0230466b34d9cb224aacf5` | The carry language `1 {2,3}* 2 1`, its exact physical transport, and its explicitly escaped states. |
| PR178 | `be5696cc45a95ad1903802b08ba1dc3ebba66930` | Physical inverse backtracing and the independent-clock continuation obstruction. |
| PR183 | `907a540943090968bc683b1b9246208e9053c1f8` | Mixed-base normal forms, their common internal matrix rank, and the open physical erasure cover. |
| PR182 | `45354128f890fb479f6c23b547368bcddd9cebe6` | Affine rigidity's exact auxiliary-group hypotheses and its missing ordinary-source approximation input. |

The elementary signed high-bit lifting identity is already in checkpoint6's `TerminalCarry.lean`; this packet does not claim it as new. That module compiles a signed numerator after an arbitrary source prefix and tracks its explicit binary horizon. The present addition repeatedly **reanchors that proved identity at the next actual source edge**, changes the carried ternary degree, and retains the still-unused literal source certificate. This composition handles every gap and every signed offset, including the states outside PR185's two-state language.

The mixed-base normalizer's matrix rank is not silently identified with the source grade. Its physical mergers can be accepted when they meet the explicit source interval, but a mere matrix-rank decrease does not establish that interval condition.

`DEPENDENCIES.json` records the byte-identical source bindings and build order. The transitive project closure is the 14 PR177 modules used by `SourceEnvelope`, plus `SourceEnvelope`, `TerminalCarry`, and this new module: 17 modules in total.

## 2. The all-state source-edge transition

Let the actual source edge be

\[
3r+1=2^a u.
\]

Suppose the current ordinary target has the exact affine pin

\[
n=3^{p+1}r+d,
\qquad p\ge0,\quad d\in\mathbb Z.
\]

Put \(z=d-3^p\). Run the ordinary signed shortcut map for exactly \(a\) steps from \(z\), recording its actual odd-step count \(k\) and endpoint \(z'\). Then

\[
\boxed{T^a(n)=3^{p+k}u+z'.}
\tag{1}
\]

This is `affine_gap_transport`. The proof factors the original target as

\[
n=3^p u\,2^a+(d-3^p)
\]

and applies the existing signed-path lift on precisely its valid horizon \(a\). Each following source edge provides a new horizon. No interpretation of a rational intermediate value as an ordinary integer is needed.

The signed map is only a finite carry computation. Equation (1) identifies its lift with the actual positive ordinary target. No assertion about an infinite negative orbit is used.

### Relation to PR185's small states

For the failed-diamond carry \(9r+2\), take \(p=1,d=2\), so \(z=-1\). All \(a\) signed steps are odd and remain at \(-1\), recovering exactly

\[
T^a(9r+2)=3^{a+1}u-1.
\]

For a debt \(3^s r-1\), the new signed input is \(-1-3^{s-1}\). The previously unsupported state \(s=2\), source gap one, becomes

\[
T(9r-1)=3u-2.
\]

The last identity is represented by `debt_two_gap_one`. It is an enabled transition in the larger language, not a claim that the subsequent trajectory is already resolved.

## 3. Total composition and exact source retention

The inductive proposition `Dispatch p d W out final` records the repeated transitions (1). The starting target is \(3^p q+d\), the supplied source prefix is \(W\), and the endpoint is \(3^{\mathrm{out}}u+\mathrm{final}\).

The source prefix has physical shortcut clock

\[
B=\operatorname{total}(W)=\sum_{a\in W}a.
\]

`dispatch_transport` proves

\[
\boxed{T^B(n)=3^{\mathrm{out}}u+\mathrm{final}}
\tag{2}
\]

for every such program and every actual supplied source prefix \(q\xrightarrow{W}u\).

The language is total on finite supplied words in the following precise sense. For any starting degree and offset, `dispatch_exists` consumes either the entire supplied word or a prefix ending at degree zero. It makes no finite-state or bounded-debt assumption. Its termination measure is the length of the supplied source word, not the Collatz trajectory.

If \(d<0\), then every updated offset remains negative. The signed input at a transition is strictly negative, and the signed shortcut preserves strict negativity. These are `signed_path_negative` and `dispatch_negative`.

Given an actual complete certificate \(\operatorname{Certificate}(q,A)\), `complete_dispatch_normal_form` consequently produces an exact literal split

\[
A=W\mathbin{+\!+}\tau,
\qquad q\xrightarrow{W}u,
\qquad\operatorname{Certificate}(u,\tau),
\]

with the physical identity (2), a negative final offset, and one of these alternatives:

1. The output degree is zero.
2. The literal tail is empty and \(u=1\), leaving the explicit target \(3^{\mathrm{out}}+\mathrm{final}\).

The second alternative carries no convergence theorem for that residual target. It also retains its originating source and program; the residual must not be replaced by an unconstrained assertion about all signed shifted powers.

### Every low target is admitted

For \(q>0\) and \(t\le16q+1\),

\[
t=3^3q+(t-27q),\qquad t-27q<0.
\tag{3}
\]

This is `low_target_initialization`. All targets in PR177's \(e\le3\) low interval satisfy this height bound. Thus admission into the affine language has no missing residue class or source-size restriction. Successful capture remains a separate matter.

## 4. One common rank pays the handoff

For a nonempty consumed prefix \(W\), keep checkpoint8's exact maximal paid exponent

\[
f=\max\bigl(e,\max_{a\in W}(a-1)\bigr),\qquad e\ge1.
\]

`boosted_prefix_rank` proves directly, for arbitrary prefix length,

\[
\Gamma(f;\tau)\prec\Gamma(e;W\mathbin{+\!+}\tau).
\tag{4}
\]

The target is then captured if

\[
\boxed{3^{\mathrm{out}}u+\mathrm{final}
\le2^{f+1}u+1.}
\tag{5}
\]

`dispatch_interval_rule` combines the exact physical transport, the complete literal suffix, (4), and (5) with the **existing** PR177 lower-rank interval hypothesis. Positivity comes from the actual positive target orbit.

Two useful positive consequences hold without any extra target-specific comparison:

- If the starting offset is negative and \(3^{\mathrm{out}}\le2^{f+1}\), `coefficient_paid_interval_rule` proves capture. The full condition (5) may succeed even when this coefficient-only condition fails.
- A degree-zero stop with negative offset always captures after a nonempty source prefix (`zero_degree_interval_rule`).

The asymmetric merger interface is also retained. Given the exact dispatched endpoint \(v=3^{\mathrm{out}}u+\mathrm{final}\), it suffices to find

\[
0<x\le2^{f+1}u+1,
\qquad T^L(x)=T^R(v).
\tag{6}
\]

`dispatch_merger_interval_rule` pays for \(x\) with the same source suffix and grade, then transfers through the merger. The original target clock is \(B+R\); the partner clock is \(L\). They need not be equal, and \(R\) is not restricted to the signed lift's previous horizon because (6) uses actual ordinary iterations.

This is a compositional soundness theorem for any supplied merger at any dispatched state. It does not construct such a merger in every case.

## 5. One source pass does not give universal capture

Consider the genuine low-state data

\[
e=1,\quad q=17,\quad A=[2,3,4],\quad t=63.
\]

The source is \(S=34\), and checkpoint8's exact envelope is \(E=26\). The target is odd, satisfies \(S+1<t\le2S+1\), and lies above \(2E+1=53\). The source first gap is two and the target first odd gap is one. All source prefix coefficient inequalities are strict. Thus the example is not excluded by the leading-one, high-gap, high-even, or \(e=1\) leading-gap-four rules.

The simultaneous source-cut comparisons are:

| Source prefix | Source endpoint | Maximal paid exponent | Paid interval ceiling | Target at that source clock |
| --- | ---: | ---: | ---: | ---: |
| `[2]` | 13 | 1 | 53 | \(T^2(63)=143\) |
| `[2,3]` | 5 | 2 | 41 | \(T^5(63)=485\) |
| `[2,3,4]` | 1 | 3 | 17 | \(T^9(63)=91\) |

For the universal initialization (3), the degree/offset states are

\[
(3,-396)\longmapsto(4,-910)
\longmapsto(6,-3160)\longmapsto(6,-638).
\]

The last identity is \(91=3^6-638\). Neither coefficient payment nor the full inequality (5) succeeds at any of these cuts. The empty-prefix halving option covers only through 35. Therefore **the assertion that every low state is captured within this one supplied source pass is refuted**, rather than installed as an open hypothesis.

An independent-clock repair is nevertheless available:

\[
T^8(63)=182=T^7(31),\qquad31\le53.
\]

This repair is already encoded in PR185's `prefix_language_rules.json` as row `[1,8,63,31,1]`. It is credited here, not claimed as a new family. Its exact ordinary affine lift is

\[
T^8(256w+63)=729w+182=T^7(128w+31),\quad w\ge0,
\]

with \(2(128w+31)=(256w+63)-1\). Both base paths have six odd steps. Replacing the larger input slope 256 by 768 would give slope 2187 at its endpoint and would not preserve the displayed merger.

The example explains the purpose of (6): a total source-driven transition system is compatible with a successful asynchronous merger, but totality of its transitions alone does not produce the merger.

## 6. Precise global verdict

This pass establishes an all-state, all-gap, arbitrary-prefix **sound dispatcher language**, an exact source-retaining normal form, and rank-paid target or partner handoffs. Its transitions do not lose an integrality guard, swap the signed intercept, replace the supplied source certificate, or identify different ordinary clocks.

It does not establish a complete successful dispatcher. A proof must additionally show that every remaining low source/target state admits a successful handoff, possibly after an independent-clock continuation or another source rewrite. The theorem gives no finite uniform degree bound for the source1 residual, and there is no proved finite terminal debt dictionary. This is not an assertion that the degrees in every constrained residual family are unbounded.

The latest normal forms, affine rigidity, and finite merger populations do not themselves supply that universal source-bounded witness. This packet therefore keeps full Collatz closure open while making the compositional carry mechanism total and its missing successful-handoff premise explicit.

## Verification receipt

The integrated replay driver is `check_whole.py`; its pinned dependency
closure is `DEPENDENCIES.json`. It freshly compiles the 16 imported project
modules, this new module, its public audit, and the independent block-budget
module. The integrated execution receipt is
[checkpoint9-lean.json](../../../../reports/2026-11-22-whole-repository/checkpoint9-lean.json).
It records the exact source hashes before and after execution. Written
counterexample computations are replayed separately in `check_examples.py`.

The imported sources remain byte-identical to their stated pins. None of
the universal coverage assertions is an axiom of the formal development.
