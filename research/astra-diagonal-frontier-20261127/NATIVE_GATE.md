# An equivalent finite mass criterion and its complete native budget

**Status: PROPOSED research packet; the named Lean declarations below are formal proofs.** The extinction and divergent-hazard premises remain **OPEN**. This is a native-clock formalization of the principal-source strategy in [PR201 at its frozen head](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md), not a new proof of the required decay. The packet's main README and replay receipt delimit the computational evidence.

## The observable is defined directly on positive integers

Use the shortcut map

\[
T(x)=\begin{cases}x/2,&2\mid x,\\(3x+1)/2,&2\nmid x,\end{cases}
\qquad q_k(x)=\#\{0\le j<k:T^j(x)\text{ odd}\}.
\]

Define the finite set and its rational mass by

\[
 C_k=\{1\le x\le2^k:\ 4j\le7q_j(x)\text{ for every }j\le k\},
 \qquad J_k=\sum_{x\in C_k}\frac1x.
\]

Every element is an ordinary positive integer, and every predicate uses its own actual orbit. In particular, this definition contains neither a generic map parameter nor a conditional random law. The initial set is \(C_0=\{1\}\). For \(k\ge1\) every member is odd. These are native-clock rows; the accompanying recent-cohort packet uses odd-clock rows. No equality of those differently indexed finite rows is assumed.

The following finite-observable premise suffices for universal convergence:

\[
 \boxed{\quad
 \text{For every integer }L>0\text{ there is }k\text{ with }
 L\le2^k\text{ and }J_k<1/L.
 \quad}                                                     \tag{1}
\]

`NativeGate.extinction_implies_collatz` proves this implication in Lean for the actual map. `finite_certificate` proves the finite version: one pair \((L,k)\) satisfying the displayed strict inequality certifies convergence of every \(1\le x\le L\). The converse is now also formalized in `NativeCriterion.collatz_iff_extinction`, using the reserve estimate below. Thus (1) is equivalent to Collatz. Neither equivalent statement is established unconditionally.

Here is the minimum argument. A least positive nonconvergent source \(m\) would be at least three and every forward state would be at least \(m\). For every \(x\ge3\),

\[
 (3x+1)^4\le128x^4.
\]

Multiplying the actual even and odd step inequalities gives

\[
 2^{4k}(T^k m)^4\le2^{7q_k(m)}m^4.
\]

Since \(T^k m\ge m\), every prefix passes. Once \(m\le2^k\), the finite sum contains its unchanged atom \(1/m\), contradicting (1) with \(L=m\). The fourth-power calculation, orbit composition, positivity, minimum argument and finite-sum comparison are all included in `NativeGate.lean`.

## Exact cylinder transport and the two children

For arbitrary natural \(t\), the actual \(k\)-step cylinder law is

\[
 q_k(x+2^k t)=q_k(x),\qquad
 T^k(x+2^k t)=T^k(x)+3^{q_k(x)}t.                         \tag{2}
\]

The corresponding prefix gates are identical. `NativeTransfer.cylinder_lift` and `gate_lift` prove these statements, including zero inputs where appropriate for the algebra. All sums below still exclude zero.

Each member \(x\in C_k\) has precisely the two possible representatives \(x\) and \(x+2^k\) at the next binary clock. Their endpoints at clock \(k\) differ by the odd integer \(3^{q_k(x)}\), so their next parity bits are opposite. Filtering these two representatives by the next gate gives exactly \(C_{k+1}\), with no duplicates. This completeness is `candidate_children`, and `sum_children` is its finite-sum form.

Let \(B_k\) be the reciprocal mass of the surviving new representatives \(x+2^k\). Let \(D_k\) be the reciprocal mass of the old representatives \(x\in C_k\) whose own next gate fails. Thus

\[
 J_{k+1}+D_k=J_k+B_k,
 \qquad
 0\le B_k\le \frac{|C_k|}{2^k}.                           \tag{3}
\]

In the birth bound there is at most one new representative per parent, and its integer value exceeds \(2^k\). This does not replace a surviving source by a newly sampled cylinder representative. `mass_identity` and `births_le_budget` prove (3).

## The reserve pays for every birth

For a passing source put

\[
 d_k(x)=7q_k(x)-4k\ge0,\qquad
 R(d)=2d+8,\qquad
 V_k=2^{-k}\sum_{x\in C_k}R(d_k(x)).
\]

The odd child changes debt by \(+3\), and the even child by \(-4\). At debt at least four both survive and

\[
 1+\frac{R(d+3)+R(d-4)}2=R(d).
\]

Below four the even child is removed, and \(1+R(d+3)/2\le R(d)\). Grouping the **actual** children using (2) therefore proves

\[
 \frac{|C_k|}{2^k}+V_{k+1}\le V_k.
\]

Combining this with (3) and \(J_0+V_0=9\) gives the unconditional theorem

\[
 \boxed{\quad
 J_N+V_N+\sum_{k<N}D_k\le9\quad\text{for every }N.
 \quad}                                                     \tag{4}
\]

This entire chain is formal: `reserve_children`, `reserve_decreases`, `envelope_step`, `envelope_budget` and `total_loss_budget` refer to the actual definitions. In particular \(\sum_{k=K}^{K+N-1}D_k\le9\) for every finite interval. Cached Mathlib dependencies are used in the replay; no custom mathematical axiom is introduced.

## Exponential reserve decay and a fixed ordinary cutoff

The reserve does decay unconditionally. Put \(t=25/24\) and

\[
 W_k=2^{-k}\sum_{x\in C_k}t^{d_k(x)}.
\]

Before filtering the actual two children, their average exponential weight is
\(\tfrac12(t^3+t^{-4})t^d\le(99/100)t^d\). Filtering can only reduce a positive sum. Since \(W_0=1\), and Bernoulli's inequality gives \(2d+8\le48t^d\) for every integer \(d\ge0\),

\[
 \boxed{\quad W_k\le(99/100)^k,\qquad V_k\le48(99/100)^k.\quad} \tag{5}
\]

[NativeDecay.lean](NativeDecay.lean) proves these finite rational estimates on the actual candidate sets. They control arrivals, not extinction of a fixed surviving source's reciprocal atom.

For a fixed clock \(k\), let
\[
 H_{k,n}=\sum_{\substack{x\in C_{k+n}\\x>2^k}}1/x.
\]
The two-child partition and birth budget show that
\[
             H_{k,n}+V_{k+n}\le V_k \qquad(n\ge0).                 \tag{6}
\]
Every source in this sum is its actual ordinary integer at the later clock. Sources below the fixed cutoff \(2^k\) can only disappear as the gate length grows. Equation (6), proved in [NativeTightness.lean](NativeTightness.lean), bounds every future contribution above that cutoff at once.

If an old source reaches 1, the eventual native orbit alternates 1 and 2 and its odd count grows at half the native clock. It therefore fails the gate at a finite time. If every member of the finite set \(C_k\) reaches 1, one common finite clock kills all those old sources. From that clock onward, \(J_n\le V_k\). Under universal convergence this applies to each \(k\), and (5) proves (1). [NativeCriterion.lean](NativeCriterion.lean) closes this converse and supplies another finite consumer: if \(V_k<1/L\) and all members of \(C_k\) have supplied convergence proofs, then every positive source through \(L\) converges.

No limit theorem or real-valued analytic axiom is needed for this formal converse. The proof uses the elementary rational bound \((99/100)^k\le100/(k+100)\), hence \(V_{4800L}<1/L\). That deliberately coarse index supplies the quantifier in the equivalence; it is not a practical search recommendation.

## The decay statement still needed

An explicit sufficient target is a nonnegative sequence \(h_k\) satisfying

\[
 h_kJ_k\le D_k,\qquad
 \sum_{k\ge K}h_k=\infty\quad\text{for every }K.              \tag{7}
\]

Zero values can leave unused native clocks out of the target. `loss_hazard_implies_collatz` proves that (7) implies universal convergence, using (4) and the actual-source finite criterion. The formal divergence hypothesis is stated with arbitrarily large finite rational partial sums. **No such sequence is constructed here.** In particular a loss estimate for recent sources alone cannot replace the factor \(J_k\) in (7).

The separate mass packet obtains a relative loss only for recent odd-clock cohorts and identifies an obstruction to bounded-weight reanchoring inside a hypothetical bad component. Converting one of those estimates into (1) or (7) is not a formalization task: it is the missing mathematical assertion about old ordinary sources.

## Finite controls

`check_native_gate.py` independently compares a direct orbit enumeration with the affine two-child tree through native clock 14. It verifies the exact mass identity, reserve inequality, exponential bound and cumulative budget at every tested clock, 120 old-cutoff/future-clock comparisons, and 2,640 cylinder lifts. Its rational comparisons stay active under Python optimization. The displayed floating values are only summaries; the assertions use exact fractions, and the potentially large exact masses are fingerprinted in hexadecimal numerator/denominator form.

The source 27 passes all native gates through clock 85 and first fails at 86. This is a finite lifetime control, not an exceptional orbit. The finite mass itself can rise: \(J_{13}\approx0.56025\) and \(J_{14}\approx0.62016\), whereas \(J_k+V_k\) decreases. The reserve is therefore material to the accounting.

The checker is not a proof of (1) or (7). The universal reserve estimate (5) is a formal theorem, separate from those open mass assertions. The source strategy, gate slope and equivalence to extinction precede this packet; the new formal contribution is the connected native-map realization, complete finite loss budget, exponential reserve estimate, fixed-source tightness and both directions of the criterion.
