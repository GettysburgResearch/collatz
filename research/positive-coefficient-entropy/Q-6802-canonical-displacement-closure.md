# Q-6802 — Canonical-displacement closure of the two exhaustive lanes

**Claim ID:** `Q-6802`  
**Status:** **OPEN**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31

## 1. Why this target replaces the earlier two-estimate plan

For a finite parity word `w`, let

\[
(r_w,s_w)
\in[1,2^j]\times[1,3^q]
\]

be the canonical pair from `L-6803`, and put

\[
\Delta_w=s_w-r_w.
\]

When `2^j>3^q`, the exact identity

\[
A_w=(2^j-3^q)r_w+2^j\Delta_w
\]

gives

\[
r_w>
\frac{A_w}{2^j-3^q}
\iff
\Delta_w<0.
\]

Therefore the proposed residue lower bound and remainder upper bound are not independent estimates. Their complete difference is one signed integer `\Delta_w`.

The highest-value finite-crossing offense is consequently:

\[
\boxed{
\Delta_w<0
\text{ for every nontrivial least-counterexample-admissible first-crossing word}.}
\tag{FC}
\]

The universal version over every `r_w>=2` is Terras's CST conjecture.

## 2. Supercritical lane in the same coordinates

For a supercritical prefix,

\[
3^{q_m}\ge2^m
\qquad(m\le j),
\]

an ordinary all-time realization by one fixed `n` has, eventually,

\[
r_j=n,
\qquad
s_j=T^j(n),
\]

and `L-6805` proves

\[
\frac{r_j}{2^j}\to0,
\qquad
\frac{s_j}{3^{q_j}}\to0.
\]

Thus Box 1 becomes:

\[
\boxed{
\text{no infinite supercritical word has an eventually constant positive source coordinate }r_j.}
\tag{SC}
\]

Equivalently,

\[
m_N^{sup}\to\infty.
\]

## 3. Complete positive implication

Assume `(SC)` and `(FC)`.

If Collatz were false, let `n` be its least positive counterexample.

- `(SC)` rules out coefficient stopping time `+infinity`.
- Let `j` be the finite first coefficient crossing. Every proper prefix has coefficient at least one, hence every proper iterate is at least `n`. Minimality also gives no descent at time `j`. The parity word is therefore least-counterexample-admissible.
- `(FC)` says its canonical endpoint lies below its canonical source, contradicting no descent.

Hence `(SC)+(FC)` imply Collatz.

## 4. What the current branch actually proves

The present packet proves only necessary interfaces:

```text
L-6803:
    exact canonical start/end rectangle and displacement identity;

L-6804:
    automatic linear record floor X_N >= n+N;

L-6805:
    bilateral normalized corner stabilization for a hypothetical ordinary
    supercritical path;

T-6802 (proposed):
    logarithmic pressure on the maximum coefficient surplus;

PR #76 (proposed):
    microscopic Farey window and exclusion of the first forced
    least-counterexample crossing candidate;

PR #77:
    all-time supercritical ordinary paths diverge to +infinity.
```

None decides `(SC)` or `(FC)`.

## 5. Exact nonreductions

The following implications are false or insufficient:

```text
supercritical symbolic path
    -> ordinary source stabilization;

high factor complexity
    -> canonical source escape;

large physical records
    -> canonical source escape;

almost-everywhere residue balance
    -> pointwise balance on every positive integer;

small real coefficient gap
    -> negative canonical displacement;

separate estimates for r_w and A_w/(2^j-3^q)
    -> a new variable beyond Delta_w.
```

The last item is algebraic, not methodological: `L-6803` proves the two sides differ exactly by a positive scalar multiple of `-\Delta_w`.

## 6. Two plausible theorem forms that would genuinely close the lanes

### A. Source-corner exclusion

Prove that every nested supercritical path satisfies

\[
\limsup_{j\to\infty}r_j=+\infty.
\]

Because `r_j` are compatible canonical representatives, any eventual positive ordinary realization would make them eventually constant. This theorem is exactly `(SC)`.

A stronger quantitative form would be

\[
\min_{w\in\mathcal W_j^{sup}}r_w\ge f(j),
\qquad
f(j)\to\infty.
\]

### B. Least-counterexample displacement negativity

Let `w` be first-crossing and impose simultaneously:

```text
- the PR #76 microscopic q/j window;
- every intermediate no-descent inequality;
- the 485/306 ballot barrier;
- exact path-merging and preimage exclusions;
- the verified ordinary floor.
```

Prove

\[
\Delta_w<0.
\]

This is weaker than universal CST and is sufficient for the least-counterexample contradiction.

## 7. Recommended mathematical offense

The most promising noncircular route is a **stability theorem for the mechanical remainder extremizer coupled to the canonical displacement**:

1. quantify the exact additive-remainder loss caused by each leftward `01 -> 10` displacement from the upper mechanical first-crossing word;
2. show that a word retaining enough remainder to satisfy no descent must lie in a controlled low-complexity neighborhood of that mechanical word;
3. use `L-6802` or a sharper completion-height argument to force its canonical source above the no-descent threshold;
4. conclude `\Delta_w<0`.

This directly attacks `(FC)`. It avoids another free encoding and keeps the ordinary source and real remainder in one proof.

For `(SC)`, the corresponding target is not another record theorem. It is a source-residue theorem for the supercritical ballot language—equivalently, deterministic escape of its least canonical representatives.

## 8. Nonclaim

Neither `(SC)` nor `(FC)` is proved in this file. The purpose of `Q-6802` is to prevent the remaining Collatz implication from being obscured by algebraically redundant quantities or downstream growth conclusions.