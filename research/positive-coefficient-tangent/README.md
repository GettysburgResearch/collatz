# Positive coefficient tangent: two-place limits and direct first-crossing pressure

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Issue:** independent continuation of issue `#75`  
**Namespace:** isolated `69xx`  
**Status:** theorem-level claims are **PROPOSED** pending independent reconstruction  

**No proof of the Collatz conjecture is claimed.**

## Purpose

The active positive coefficient program leaves two exact possibilities for a least counterexample:

```text
all-time coefficient supercriticality;
a finite first coefficient crossing that does not descend.
```

This packet attacks only those global blockers.

On the divergent side, it proves that every divergent orbit creates escaping tail minima whose coefficient stopping depths tend to infinity and an all-supercritical 2-adic tangent. The tangent need not be an ordinary integer: its ordinary realizers escape in the real place.

On the finite-crossing side, it identifies the exact integer descent defect, couples the two final PR #81 boxes through one relative envelope, and excludes every unbounded acyclic canonical-failure family having logarithmic coefficient bank and uniformly zero factor entropy.

## Claims

| ID | Status | Content |
|---|---|---|
| `T-6901` | `PROPOSED` | A no-descent start above the exact finite threshold `H_L` has coefficient stopping depth greater than `L`. |
| `T-6902` | `PROPOSED` | Every divergent orbit has escaping tail minima with `tau->infinity` and an orbit-supported all-supercritical 2-adic tangent. |
| `T-6903` | `PROPOSED` | Divergence gives either one ordinary `tau=infinity` start or infinitely many increasingly deep CST violations. |
| `R-6901` | `PROPOSED` | Compactness does not fuse those lanes into one ordinary seed; Archimedean tightness is still required. |
| `L-6904` | `PROPOSED` | The Box-2 inequality is exactly positivity of the integer defect `r^+(w)-T^j(r^+(w))`; equality is a positive cycle. |
| `L-6905` | `PROPOSED` | A canonical crossing failure forces `m_(j-1)^sup <= r^+(w) <= F_j`; the two final boxes reduce to the single envelope inequality `m_(j-1)^sup>F_j`. |
| `T-6904` | `PROPOSED / SOURCE-DEPENDENT` | Logarithmic-bank, uniformly zero-entropy, acyclic first-crossing failures cannot occur at unbounded lengths. |

## Exact direct blocker

For a first-crossing word `w`, write

\[
T_w(x)=\frac{3^q x+A_w}{2^j},
\qquad
D_w=2^j-3^q,
\]

and let `r=r^+(w)`, `y=T_w(r)`. Then

\[
D_w r-A_w=2^j(r-y).
\]

Thus the desired inequality

\[
r^+(w)>\frac{A_w}{D_w}
\]

is exactly canonical descent `r>y`. If it holds, every positive lift in that cylinder descends. If equality holds, the word closes to a positive cycle.

## One-envelope reduction

Let

\[
m_N^{\rm sup}=\min\{m>0:3^{q_k(m)}\ge2^k\text{ for }k\le N\},
\]

and let `F_j` be the largest rational fixed-point threshold `A_w/D_w` among first-crossing words of length `j`.

Any canonical failure satisfies

\[
m_{j-1}^{\rm sup}\le r^+(w)\le F_j.
\]

Therefore

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

forces descent for every length-`j` first crossing. The envelope `F_j` is unbounded along lower continued-fraction convergents to `log 2/log 3`; hence the same cofinal inequality also forces `m_N^sup->infinity`.

The two former global boxes are therefore one relative-growth theorem.

## Infinite class now closed

Subject to the quoted Baker lower bound, no unbounded acyclic canonical-failure family can simultaneously have

```text
maximum proper-prefix surplus = O(log j);
uniformly zero factor entropy.
```

A surviving late failure must instead have a superlogarithmic coefficient bank, positive factor entropy at logarithmic scales, or a repeated physical state leading to the cycle lane.

This is a genuine exhaustive-class exclusion, not a bounded scan.

## Read first

1. `claims/L-6905-box-coupling-envelope.md`
2. `claims/L-6904-canonical-first-crossing-gap.md`
3. `claims/T-6904-zero-entropy-log-bank-crossings.md`
4. `claims/T-6901-finite-coefficient-threshold.md`
5. `claims/T-6902-wave-minimum-supercritical-tangent.md`
6. `claims/T-6903-divergence-cst-dichotomy.md`
7. `claims/R-6901-no-compactness-fusion.md`
8. `LITERATURE_AUDIT.md`
9. `../../reports/gpt56-positive-tangent-01/2026-07-31-75-positive-tangent.md`
