# Latest coefficient-envelope stack

**Updated:** 2026-07-31  
**Active draft PR:** #83  
**Namespace:** `69xx`  

No proof of Collatz is claimed.

## Complete claim map

```text
T-6901  finite no-descent coefficient threshold
T-6902  wave-minimum all-supercritical two-place tangent
T-6903  divergence / CST-violation dichotomy
R-6901  compactness does not extract an ordinary seed

L-6904  canonical first-crossing integer descent defect
L-6905  Box-1 / Box-2 envelope coupling
L-6906  upper mechanical word is the exact envelope
T-6905  explicit scalar envelope G_j

T-6904  logarithmic-bank zero-entropy exclusion
T-6906  bank--complexity repeated-factor ceiling

L-6907  exact one-wrap law for nonmechanical failures
L-6908  dual defect residue and unique late canonical candidate
L-6909  shifted full-denominator equation

T-6907  all-repetition single-pulse positive near-return exclusion
X-6901  exact post-Matveev and finite-case verifier
```

## Current global reduction

For a sufficiently late first-crossing word `w` of length `j`, weight `q`, and numerator `A_w`, every non-descending positive start is its canonical root and satisfies

\[
\boxed{
A_w=n(2^j-3^q)+d3^q,
\qquad
0\le d<j/2,
\qquad
T^j(n)=n+d.}
\]

The cases are:

```text
d=0:
  positive cycle;

d>0:
  coefficient-stopping-time failure.
```

Thus the cycle and delayed-crossing lanes are one shifted full-denominator problem.

## Exact envelope reduction

Let

\[
m_N^{\rm sup}
=
\min\{m>0:3^{q_k(m)}\ge2^k\text{ for all }k\le N\}.
\]

At each valid crossing length `j`, let `w_mech(j)` be the unique upper mechanical first-crossing word and put

\[
F_j=
\frac{A_{w_{\rm mech}(j)}}{2^j-3^{q(j)}}.
\]

Then

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

forces descent for every length-`j` crossing. Because `F_j` is unbounded along lower continued-fraction convergents, the same cofinal inequality also forces

\[
m_N^{\rm sup}\to\infty.
\]

A coarser explicit bound is

\[
F_j<
G_j=
\frac{q(j)2^{j-1}}{2^j-3^{q(j)}}.
\]

## Infinite regions already removed

Subject to the declared logarithmic-form input, an unbounded acyclic canonical-failure family cannot have:

```text
logarithmic coefficient bank + uniformly zero factor entropy;
```

or, more generally,

```text
polynomial factor complexity degree s
+ bank o(j^(1/s)).
```

In particular, every uniformly linear-complexity cofinal failure family needs a genuinely linear bank.

## New all-repetition closure

For a one-pulse lift of either known negative accelerated cycle, arbitrary repetition and rotation, a positive near-return `n -> n+d` gives

\[
D\mid g(2^\delta-1)-3d,
\qquad
0<D\le g(2^\delta-1).
\]

The same Matveev/continued-fraction architecture as the cycle theorem, with enlarged exact constants, excludes every repetition. `X-6901` closes the finite small cases.

The sole hit is

```text
(1,2) -> (2,2),
n=1,
d=0.
```

## Remaining frontier

The unrestricted target is now:

```text
exclude
A_w=n(2^j-3^q)+d3^q,
0<=d<j/2,
```

for arbitrary high-bank, positive-entropy, genuinely aperiodic first-crossing words.

Equivalent scalar form:

```text
prove m_(j-1)^sup > F_j
cofinally.
```

The one-pulse negative-cycle class, low-complexity/subcritical-bank classes, noncanonical lifts, and compactness shortcuts are closed by the current stack.
