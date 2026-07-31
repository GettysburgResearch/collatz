# Q-6801 — Pointwise closure target for a proof of Collatz

**Claim ID:** `Q-6801`  
**Status:** **OPEN**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31

## 1. Least-counterexample split

Assume Collatz is false and let `n` be its least positive counterexample.

Draft PR #76 proposes the exhaustive alternative

\[
\tau(n)=\infty
\quad\text{or}\quad
\tau(n)\ge217{,}976{,}794{,}617.
\]

A proof of Collatz through this route must eliminate both lanes.

## 2. Lane A — ordinary all-time-supercritical extraction

For a depth `N`, let

\[
\mathcal S_N
=
\left\{
 m\in\mathbf Z_{>0}:
 3^{q_k(m)}\ge2^k
 \text{ for every }1\le k\le N
\right\},
\]

and put

\[
m_N^{\mathrm{sup}}=\min\mathcal S_N.
\]

The sets are nested. Therefore

\[
\boxed{
\exists m>0\text{ with }\tau(m)=\infty
\iff
(m_N^{\mathrm{sup}})\text{ is bounded}
\iff
(m_N^{\mathrm{sup}})\text{ eventually stabilizes}.}
\tag{1}
\]

The exact negative theorem needed is

\[
\boxed{m_N^{\mathrm{sup}}\longrightarrow\infty.}
\tag{2}
\]

This statement is weaker than Collatz: it excludes only the all-time coefficient-supercritical lane.

`T-6802` gives a necessary condition for any hypothetical stabilizing root:

\[
B_N\ge(\kappa_*-o(1))\log_2N
\]

and

\[
X_N\ge mN^{\delta_*-o(1)}.
\]

It does not prove `(2)`.

### Exact next lemma

A successful continuation must connect the parity-language pressure to the **canonical initial residue**, not merely to later orbit height.

For every supercritical parity word `w` of length `N`, let `r(w)` be its least positive parity-cylinder representative modulo `2^N`. Prove a uniform escape theorem such as

\[
\min_{w\in\mathcal W_N^{\mathrm{sup}}}r(w)\to\infty.
\]

A count of words, a measure-one statement, or a free `2`-adic completion is insufficient.

## 3. Lane B — delayed first coefficient crossing

Let `w` be a first-crossing word of length `j` and weight `q`:

\[
3^{q_m}\ge2^m\quad(m<j),
\qquad
3^q<2^j.
\]

Write its affine map as

\[
T_w(x)=\frac{3^q x+A_w}{2^j}.
\]

Put

\[
D_w=2^j-3^q>0
\]

and let `r^+(w)` be the least positive representative of its parity cylinder:

\[
3^q r^+(w)+A_w\equiv0\pmod{2^j}.
\]

A positive integer in this cylinder can avoid descent at time `j` only if

\[
\boxed{
r^+(w)\le\frac{A_w}{D_w}.}
\tag{3}
\]

Thus the exact all-candidate theorem is

\[
\boxed{
 r^+(w)>rac{A_w}{2^j-3^q}
 \quad\text{for every admissible late first-crossing word}.}
\tag{4}
\]

PR #76 controls the right side of `(4)` by a mechanical extremizer and excludes the first forced Farey candidate. It does not control the canonical residue on the left.

### Exact next lemma

Prove a joint residue--remainder pressure inequality. The high-value form is:

```text
large affine remainder
    forces a near-mechanical low-surplus word;

near-mechanical low-surplus word
    forces a large ordinary parity-cylinder residue;

large canonical residue
    exceeds A_w/(2^j-3^q).
```

`T-6802` supplies the middle mechanism qualitatively: a long ordinary near-mechanical path cannot remain in a bounded surplus strip without paying physical height. The missing step is to place that height at the **initial canonical representative** rather than only at a later state.

## 4. Complete implication

If `(2)` and `(4)` are both proved, then no least positive counterexample exists:

- `(2)` excludes `tau=infinity`;
- `(4)` makes every finite first coefficient crossing descend below its start;
- least-counterexample minimality then gives a contradiction.

This would prove Collatz.

## 5. What does not count

The following do not close `Q-6801`:

- a longer finite verification range by itself;
- almost-everywhere parity statistics;
- high subword complexity without residue control;
- a compatible `2`-adic path;
- a probability-zero exceptional set;
- conditional divergence after assuming one ordinary root;
- another rational approximation without the full inequality `(4)`.

## 6. Recommended offense

Attack the joint quantity

\[
\boxed{
\Phi(w)
=
\log r^+(w)
-
\log\!\left(\frac{A_w}{2^j-3^q}\right).}
\]

The target is `Phi(w)>0` for every late admissible first-crossing word.

The natural decomposition is by Ostrowski blocks of the slope `alpha=log 2/log 3`, while retaining the exact parity-cylinder residue under concatenation. This directly couples the two global blockers instead of adding another independent encoding.
