# Session report — two-box closure attempt

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-31  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-entropy-01/75-supercritical-entropy`  
**Stacked base:** draft PR #77  
**Status:** no proof of Collatz; exact reductions and statement corrections committed

## 1. Requested target

The requested proof consisted of two statements:

1. the least depth-`N` ordinary coefficient-supercritical root tends to infinity;
2. every coefficient-first-crossing word has canonical source larger than its no-descent threshold.

Together, after the trivial cycle is separated, these would prove Collatz by least-counterexample descent.

## 2. Exact canonical start–end theorem

For every length-`j`, weight-`q` parity word,

\[
T_w(x)=\frac{3^q x+A_w}{2^j},
\]

`L-6803` constructs the unique pair

\[
1\le r_w\le2^j,
\qquad
1\le s_w\le3^q,
\]

satisfying

\[
2^j s_w=3^q r_w+A_w.
\]

Every ordinary realization is exactly

\[
x=r_w+t2^j,
\qquad
T_w(x)=s_w+t3^q.
\]

Thus

\[
T_w(x)-x
=(s_w-r_w)+t(3^q-2^j).
\]

This gives one complete finite coordinate for source, endpoint, coefficient, and ordinary lift.

## 3. Box 2 collapses to one displacement

When `2^j>3^q`, put

\[
D_w=2^j-3^q,
\qquad
\Delta_w=s_w-r_w.
\]

The exact identity is

\[
A_w=D_w r_w+2^j\Delta_w.
\]

Therefore

\[
r_w>\frac{A_w}{D_w}
\iff
\Delta_w<0.
\]

The proposed two-sided inequality was not hiding an extra degree of freedom. It is exactly the sign of the canonical endpoint displacement.

The literal strict statement has one trivial exception:

```text
word 10:
    r=s=1,
    A=D=1.
```

After excluding that trivial cycle, the universal sign theorem is precisely Terras's coefficient-stopping-time conjecture. It is not proved by the affine identity.

For a least-counterexample proof one may ask for less: prove `\Delta_w<0` only for first-crossing words satisfying the verified floor, all intermediate no-descent inequalities, the `485/306` ballot barrier, and the path/preimage constraints imported by PR #76.

## 4. Box 1 in bilateral canonical coordinates

For a hypothetical fixed ordinary all-time-supercritical root `n`, `L-6805` proves that the canonical pairs of its prefixes eventually satisfy

\[
r_k=n,
\qquad
s_k=T^k(n),
\]

and

\[
\frac{r_k}{2^k}\to0,
\qquad
0<\frac{s_k}{3^{q_k}}
\le\frac{n+k/2}{2^k}\to0.
\]

Thus Box 1 is exactly the nonexistence of a nested supercritical path whose source coordinate eventually stabilizes at one positive integer while the endpoint coordinate simultaneously approaches its opposite local corner.

This is the ordinary source/endpoint compatibility that average parity results do not address.

## 5. Record-growth correction

The earlier packet emphasized the proposed consequence

\[
X_N\ge nN^{0.035856\ldots-o(1)}.
\]

`L-6804` shows that this is dominated by an elementary fact. Under all-time coefficient supercriticality:

- every iterate is at least `n`;
- no state repeats;
- hence `N+1` distinct integers lie in `[n,X_N]`.

Therefore

\[
\boxed{X_N\ge n+N.}
\]

The nontrivial proposed content of `T-6802` is its logarithmic lower pressure on the maximum coefficient surplus, not its physical-record exponent.

This correction is recorded explicitly rather than leaving an inflated progress metric in the branch narrative.

## 6. Literature boundary

The universal corrected Box 2 is the longstanding CST conjecture. The strongest classical result leaves only the smallest member of an admissible parity cylinder as the possible exception. `L-6803` identifies that exceptional member exactly as `r_w` and its obstruction exactly as `\Delta_w>=0`.

Rozier--Terracol's paradoxical-sequence work and PR #76 constrain this obstruction sharply but do not eliminate it globally. Current pointwise/mixing papers likewise distinguish map-level or almost-everywhere balance from the ordinary-orbit statement required here.

## 7. Failed proof routes

### Separate residue and remainder estimates

Failed as a reduction: the two quantities differ exactly by the scaled displacement `\Delta_w`.

### Record growth

Failed as an extraction mechanism: even linear or faster physical growth is compatible with a divergent orbit and gives no lower bound on the fixed initial source.

### Entropy alone

High factor complexity constrains a hypothetical path but does not force its canonical source representatives to escape.

### Almost-everywhere balance

The positive integers form a countable exceptional set in the `2`-adic model; genericity does not imply pointwise exclusion.

### Finite-prefix nonemptiness

Every depth may contain positive ordinary roots while the nested minima escape. This is exactly the ordinary-extraction quantifier boundary already verified elsewhere in the repository.

## 8. Exact current targets

The complete positive route is now frozen as:

\[
\boxed{
\text{SC: no infinite supercritical word has eventually constant }r_k>0,}
\]

and

\[
\boxed{
\text{FC: every nontrivial least-counterexample-admissible first crossing has }\Delta_w<0.}
\]

`SC+FC` imply Collatz.

Neither is proved in this report.

## 9. Highest-value continuation

The best finite-crossing offense is a stability theorem around the upper mechanical remainder extremizer:

1. quantify remainder loss under each displacement away from the mechanical word;
2. prove that a word retaining enough remainder for no descent has controlled factor complexity;
3. convert that controlled complexity into a canonical source lower bound;
4. compare directly with the exact no-descent threshold, equivalently prove `\Delta_w<0`.

For the supercritical lane, only a theorem on the canonical **source coordinate** changes the result. Another downstream growth theorem does not.

## 10. Files added in this pass

```text
L-6803  canonical start-end rectangle and displacement identity
L-6804  elementary linear record floor and T-6802 scope correction
L-6805  bilateral canonical-corner stabilization
R-6802  two-box statement and proof-boundary correction
Q-6802  canonical-displacement closure target
this report
```

## 11. Honest conclusion

The attempt did not prove the two boxes. It did prove that the proposed joint quantity is exactly one canonical displacement, corrected the trivial boundary, exposed CST as the universal Box-2 obligation, strengthened the ordinary-path compatibility interface, and removed one misleading progress metric.

No theorem is promoted beyond `PROPOSED`; no Collatz proof or counterexample is claimed.