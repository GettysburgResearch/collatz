# O-0006 — Recorded charts have sharply different normalized control widths

Claim ID: `O-0006`  
Title: Exact aspect-ratio audit for the principal collision charts  
Status: `EMPIRICAL` for the cross-file audit; each ratio is an exact consequence of its recorded chart  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `O-0001`--`O-0005`, `T-0010`, `L-0011`, `X-0006`  
Scope: finite comparison of recorded charts  
Related counterexample candidates: none

## Statement

For a supercritical collision chart with input radix \(M\), output radix \(N\), and offset alphabet \(D\), define

\[
\Delta=
\frac{\operatorname{diam}D}{N-M}.
\]

The five principal recorded charts have the following exact data.

| Chart | branches | \(\operatorname{diam}D\) | \(N-M\) | \(\Delta\) |
|---|---:|---:|---:|---:|
| `O-0001` | 2 | 1 | 17 | \(1/17\approx0.0588235294118\) |
| `O-0002` | 3 | 2 | 217 | \(2/217\approx0.00921658986175\) |
| `O-0003` | 6 | 5 | 46075 | \(5/46075\approx1.08518719479\cdot10^{-4}\) |
| `O-0004` | 18 | 94 | 588665 | \(94/588665\approx1.59683351312\cdot10^{-4}\) |
| `O-0005` | 339 | 17207 | 5284606410545 | \(17207/5284606410545\approx3.25606084224\cdot10^{-9}\) |

Thus the 339-branch chart has by far the richest recorded finite alphabet geometry, but its normalized real control window is more than seven orders of magnitude narrower than that of the original two-branch chart.

For `O-0005`, the natural signed return alphabet from `T-0008` is

\[
A=
[2595183923959,2595183941166]\cap\mathbb Z
\]

restricted to the 339 recorded digits. It lies inside \([0,(N-M)/2]\). Therefore any hypothetical infinite orbit in that chart would satisfy

\[
\left\{C\left(\frac NM\right)^t\right\}
\in
\left[
1-\frac{2595183941166}{5284606410545},
1-\frac{2595183923959}{5284606410545}
\right]
\pmod1
\]

for every \(t\), an arc of exact length

\[
\frac{17207}{5284606410545}.
\]

## Complete-dyadic-projection family

`X-0006` also reconstructs the examples underlying `T-0007`. Their branch count and dyadic correction scale grow, but their normalized aspect ratios collapse:

```text
b=1  branches=2   aspect=2.17037438958e-05
b=2  branches=4   aspect=2.29094219429e-12
b=3  branches=8   aspect=5.44351953165e-30
b=4  branches=16  aspect=1.10176568422e-93
b=5  branches=32  aspect=4.72338668751e-264
```

These values exactly satisfy the common-tail identity in `L-0011`.

## Interpretation

Branch cardinality, low-order modular coverage, and normalized real width are distinct resources.

The inverse-code and odd-tail program successfully produced:

- exponentially many branches;
- arbitrary finite 3-adic precision;
- complete dyadic projection at a growing scale;
- preserved finite difference geometry.

But a long common post-merger tail can make the signed rational-base alphabet extremely narrow relative to \(N-M\). By `T-0010`, that forces one real multiplicative orbit into an equally narrow fractional-part window.

This does not refute the construction. It changes the optimization target:

> future charts should be ranked by a joint profile of symbolic branching, 2-adic correction power, normalized aspect ratio, and renewal-code compatibility.

## Verification

`X-0006` verifies every negative-shadow identity for `O-0001` through `O-0005`, including all 339 branches of `O-0005`, and computes every displayed ratio with exact integers.

## Gap audit

- A tiny aspect ratio is not a proof of nonexistence.
- A large aspect ratio is not sufficient for finite 2-adic closure.
- The comparison covers recorded charts, not every possible chart.
- Graph-directed systems can combine several windows and are not summarized by one stationary \(\Delta\).

## Suggested next attack

Construct near-critical collision cores whose branch displacement diameter grows on the same scale as \(N-M\), or build a multi-target negative-template renewal graph whose combined graph-directed windows remain macroscopic through a full expanding cycle.
