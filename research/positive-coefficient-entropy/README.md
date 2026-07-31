# Positive coefficient canonical-pressure packet

**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-entropy-01/75-supercritical-entropy`  
**Base:** draft PR #77 at `1c8ed3c7edbb190d59490d2f92a3c342c2f856eb`  
**Status:** draft mathematical research

## Objective

The packet attacks the two exhaustive coefficient-stopping lanes for a least
positive counterexample:

```text
SC — supercritical lane:
  no finite prefix has coefficient below one;

FC — finite-crossing lane:
  the first subcritical coefficient occurs but the orbit does not descend.
```

The exact canonical closure target is:

```text
SC:
  no infinite supercritical word has an eventually constant positive
  canonical source;

FC:
  every nontrivial least-counterexample-admissible first crossing has
  canonical displacement endpoint-source < 0.
```

`SC + FC` would prove Collatz. Neither unrestricted statement is proved here.

## 1. Canonical start–end duality

For every finite parity word,

\[
T_w(x)=\frac{3^q x+A_w}{2^j},
\]

`L-6803` constructs the unique pair

\[
1\le r_w\le2^j,\qquad
1\le s_w\le3^q,\qquad
2^j s_w=3^q r_w+A_w.
\]

Every positive realization is exactly

\[
x=r_w+t2^j,\qquad
T_w(x)=s_w+t3^q.
\]

For a subcritical word, put

\[
\Delta_w=s_w-r_w.
\]

Then

\[
A_w=(2^j-3^q)r_w+2^j\Delta_w
\]

and

\[
r_w>\frac{A_w}{2^j-3^q}
\iff
\Delta_w<0
\iff
s_w<r_w.
\]

Thus the residue and remainder sides of FC are one exact integer displacement,
not independent estimates.

The strict universal statement has the trivial exception

```text
word 10, root=endpoint=1.
```

After removing the trivial cycle, the universal FC statement is Terras's
Coefficient Stopping Time conjecture.

## 2. Supercritical ordinary pressure

`L-6801` proves that equal length-`L` parity factors on one ordinary orbit
begin at states differing by a multiple of `2^L`.

`T-6801/T-6802` convert this into deterministic factor and coefficient-surplus
pressure. In particular, every ordinary all-time-supercritical path has
unbounded surplus and a logarithmic lower surplus envelope.

`L-6804` records the stronger elementary physical fact:

```text
all states are distinct and at least n
  -> X_N >= n+N.
```

The useful content of the entropy packet is the coefficient-surplus pressure,
not the earlier weaker polynomial-record corollary.

PR #80 independently adds a stronger product/packing estimate for the same
hypothetical ordinary lane, including an `8/9` logarithmic mean-surplus floor.
Neither theorem moves the canonical source coordinate, so Box 1 remains open.

## 3. Bilateral ordinary corner

`L-6805` proves that a fixed ordinary supercritical realization eventually has

\[
r_k=n,\qquad s_k=T^k(n),
\]

while

\[
\frac{r_k}{2^k}\to0,
\qquad
0<\frac{s_k}{3^{q_k}}
\le\frac{n+k/2}{2^k}\to0.
\]

Thus Box 1 asks whether one path can simultaneously occupy:

```text
critical/supercritical real drift;
an eventually constant positive 2-adic source corner;
a vanishing normalized 3-adic endpoint corner;
exact physical replay.
```

No contradiction among these four coordinates is yet proved.

## 4. Low-complexity first-crossing exclusions

`L-6802/T-6803` show that repeated parity factors force an exponential lower
bound on the same canonical source that no descent bounds only polynomially,
after an effective two-logarithm lower bound.

Consequently, modulo the positive-cycle alternative, sufficiently long
bounded-bank linear-complexity first-crossing families descend.

`L-6806/T-6805` quantify distance from the upper-mechanical remainder
extremizer. An unbounded acyclic FC-obstruction family cannot remain
`o(sqrt(j))` close in integrated adjacent-swap distance.

## 5. Complete upper-mechanical closure — `T-6806/X-6801`

The newest theorem makes the mechanical conclusion explicit at every length.

```text
j=2:
  word 10, root=endpoint=1;

every valid j>2:
  the upper-mechanical canonical source descends,
  unless the segment already contains a nontrivial positive cycle.
```

Proof layers:

```text
bank < 1;
Sturmian factor complexity <= L+1;
dyadic repeated-factor separation;
Rhin lambda >= j^(-13.3);
exact finite replay for j<373;
three-residue integer induction from j=373.
```

`X-6801` freezes:

```text
valid finite rows:       234
nontrivial failures:       0
analytic bases:      373,374,375
semantic digest:
5d88f47548ca6716b7c10cf839dc7d65eb6efdff748b35cca9d709aa36771d2e
```

PR #82 proves that every no-wrap nonmechanical word is easier to descend than
the mechanical word. Therefore, subject to the positive-cycle alternative:

\[
\boxed{\text{every surviving FC obstruction is a nonmechanical modulus wrap.}}
\]

## 6. Growing-support wrap barrier

`L-6808` introduces the prefix-excess path above the mechanical word. If

```text
I = integrated adjacent-swap distance;
H = maximum integer prefix excess;
B = coefficient bank;
R = number of displaced odd positions,
```

then

\[
I\ge H^2,\qquad
B<H+1\le\sqrt I+1,\qquad
H\le R.
\]

For a canonical no-descent word, every individual displacement obeys

\[
h_i<1+\log_2j+(B+1)\log_2 3.
\]

Combining this elementary geometry with PR #82's source-qualified
bank–displacement uncertainty yields:

\[
\boxed{
\liminf\frac{I_j}{j^{2/3}}
\ge
\left(\frac{\alpha}{2}\right)^{2/3}
=0.463412\ldots
}
\]

and

\[
\boxed{
\liminf\frac{R_j}{j^{1/3}}
\ge
\left(\frac{\alpha^2}{2}\right)^{1/3}
=0.583862\ldots.
}
\]

Thus a surviving acyclic FC obstruction must be simultaneously:

```text
nonmechanical;
wrapped across the full dyadic modulus;
at least two-thirds-scale far from the extremizer;
supported on cube-root many displaced odd positions;
and accepted by one of fewer than j/2 full-denominator defect levels.
```

## 7. Two logarithmic boundary departures

`T-6809` proves that a target-failure word cannot initially shadow the
mechanical extremizer for long. If `ell` is their common-prefix length, then

\[
\frac{2^{\lfloor(\ell-1)/3\rfloor}+1}{3}-\frac\ell2
<\frac{1}{2^{j/q}-3},
\]

and, under the quoted Rhin exponent,

\[
\boxed{
\limsup\frac{\ell}{\log_2j}\le42.9.
}
\]

`L-6810` supplies the independent post-return boundary. If

\[
T^j(r)=r+\Delta,
\qquad0<\Delta<j/2,
\]

and the parity sequences from `r` and `r+Delta` agree for `ell_tail` steps,
then

\[
2^{\ell_{\rm tail}}\mid\Delta,
\]

so

\[
\boxed{
\ell_{\rm tail}\le v_2(\Delta)<\log_2(j/2).
}
\]

Every surviving acyclic obstruction therefore branches away early at both
ends: from the mechanical extremizer near its start, and from its own old
parity tail immediately after the near-return.

## 8. Full-denominator near-cycle and prime-power compiler

`L-6807` proves that every non-descending first crossing is an exact
small-displacement near-cycle:

\[
2^j-3^q\mid A_w-2^j\Delta,
\qquad0\le\Delta<j/2,
\]

with

\[
T^j(r_w)=r_w+\Delta.
\]

The cycle case is exactly `Delta=0`. Acyclic FC obstructions are the common
small-displacement extension of the repository's full-denominator cycle
problem.

PR #82 `T-6609` gives a necessary-and-sufficient fixed-length classification
through fewer than `j/2` full-denominator levels.

`L-6809` adds a lossless factorwise reconstruction. Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad h_s=\operatorname{ord}_{Q_s}(2).
\]

Under PR #34's source-qualified order window, compatible local excess paths
modulo the `h_s`, the explicit first-crossing prefix barrier, one common
ordinary `Delta<j/2`, every complete prime-power congruence, and the canonical
positive range are necessary and sufficient for one exact ordinary near-return.

A subset of factors may decode the word when its lcm-order exceeds `j-q`, but
all omitted prime powers and the first-crossing gate remain mandatory.

## 9. Exact current blockers

### SC

Prove

\[
\boxed{
\min_{w\in\mathcal W_N^{\rm sup}}r_w\to\infty.
}
\]

Physical growth, average mixing, finite compatibility, and free completion do
not establish this source-coordinate escape.

### FC

Prove that the growing-support, early-departing wrap language avoids every
short full-denominator target level of PR #82 `T-6609`, while retaining the
cycle level separately.

## 10. Literature boundary

The closest rigorous literature remains:

- Rozier--Terracol on paradoxical sequences and CST;
- Angeltveit on exact finite verification/descent sieves;
- Chang on map balance versus still-open pointwise orbit balance;
- Kramer on simultaneous real, `2`-adic, and `3`-adic exponent-code
  compatibility;
- Fernández--Ibáñez on Christoffel words as rotation-class maximizers for the
  cycle numerator functional.

The Christoffel theorem is complementary rather than a direct replacement:
it optimizes a rotation-invariant cycle minimum, while this packet treats a
fixed-start first-crossing canonical source and its wrap displacement.

Almost-everywhere statements remain blocked by `R-6801`: positive ordinary
integers form a countable Haar-null subset of `Z_2`.

## 11. Review order

1. `claims/L-6803-canonical-start-end-rectangle.md`
2. `claims/T-6806-upper-mechanical-all-length-closure.md`
3. `experiments/X-6801-mechanical-cst/`
4. `claims/L-6808-bank-area-displacement-geometry.md`
5. `claims/T-6807-two-thirds-mechanical-distance.md`
6. `claims/T-6808-cuberoot-displaced-support.md`
7. `claims/T-6809-logarithmic-early-departure.md`
8. `claims/L-6810-near-return-self-shadowing.md`
9. `claims/L-6809-near-cycle-prime-power-compiler.md`
10. `claims/L-6807-small-displacement-full-denominator-bridge.md`
11. `claims/L-6805-bilateral-corner-stabilization.md`
12. `Q-6802-canonical-displacement-closure.md`
13. earlier entropy claims, reports, and literature audit

## Status boundary

All theorem-level claims remain **PROPOSED** pending independent
reconstruction. Claims using Rhin, generic effective linear forms, or the PR
#34 order theorem are explicitly source-qualified.

No proof of Collatz, counterexample, nontrivial cycle, or `K-####` object is
claimed.
