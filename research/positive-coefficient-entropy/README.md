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

## 1. Canonical start--end duality

For every finite parity word,

\[
T_w(x)=\frac{3^q x+A_w}{2^j},
\]

`L-6803` constructs the unique pair

\[
1\le r_w\le2^j,
\qquad
1\le s_w\le3^q,
\qquad
2^j s_w=3^q r_w+A_w.
\]

Every positive realization is exactly

\[
x=r_w+t2^j,
\qquad
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
pressure. Every ordinary all-time-supercritical path has unbounded surplus
and a logarithmic lower surplus envelope.

`L-6804` records the stronger elementary physical fact:

```text
all states are distinct and at least n
  -> X_N >= n+N.
```

PR #80 independently adds a stronger product/packing estimate, including an
`8/9` logarithmic mean-surplus floor and density-zero visits to each fixed
surplus band. These are genuine individual-orbit restrictions, but none moves
the same canonical source coordinate.

`L-6805` proves that a fixed ordinary supercritical realization eventually has

\[
r_k=n,
\qquad
s_k=T^k(n),
\]

while

\[
\frac{r_k}{2^k}\to0,
\qquad
0<\frac{s_k}{3^{q_k}}
\le\frac{n+k/2}{2^k}\to0.
\]

The exact SC theorem remains

\[
\boxed{
\min_{w\in\mathcal W_N^{\rm sup}}r_w\to\infty.}
\]

Physical growth, average mixing, finite compatibility, and free completion do
not prove this source-coordinate escape.

## 3. One relative envelope couples the two boxes

`L-6813` incorporates the clean coupling observed independently on PR #83.
If a length-`j` first crossing fails canonical descent, then

\[
\boxed{
 m_{j-1}^{\rm sup}
 \le r^+(w)
 \le {A_w\over2^j-3^q}
 \le F_j,}
\]

where

\[
F_j
=
{A_{\rm mech}(j)\over2^j-3^{q(j)}}
\]

is the exact upper-mechanical threshold.

Therefore the cofinal inequality

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\]

would simultaneously force every late first crossing to descend and force
`m_N^sup` to infinity, since `F_j` is unbounded along lower convergents.

`L-6812` sharpens the universal scalar envelope to

\[
F_j
<
{q(j)2^j
 \over
 3(2^j-3^{q(j)})}.
\]

This replaces the earlier `q/2` remainder ceiling by the exact termwise
`q/3` ceiling. The repository still has no polynomial or cofinal lower bound
for `m_N^sup` strong enough to dominate this envelope.

## 4. Complete upper-mechanical closure — `T-6806/X-6801`

For the upper-mechanical first-crossing word at every valid length:

```text
j=2:
  word 10, root=endpoint=1;

every valid j>2:
  the canonical source descends,
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

PR #83's clean `69xx` packet supersedes the closed/colliding PR #82 packet.
Its exact mechanical wrap law proves that every no-wrap nonmechanical word is
easier to descend than the mechanical word. Therefore, subject to the
positive-cycle alternative,

\[
\boxed{
\text{every surviving FC obstruction is a nonmechanical dyadic wrap.}}
\]

## 5. Geometry around the mechanical extremizer

For a first-crossing word relative to the upper-mechanical word, put

```text
I = integrated adjacent-swap distance;
H = maximum integer prefix excess;
B = coefficient bank;
R = number of displaced odd positions.
```

`L-6808` proves

\[
I\ge H^2,
\qquad
B<H+1\le\sqrt I+1,
\qquad
H\le R.
\]

Under canonical no descent, every individual displacement also obeys

\[
h_i<1+\log_2j+(B+1)\log_2 3.
\]

The earlier `T-6807/T-6808` consequences were

\[
I=\Omega(j^{2/3}),
\qquad
R=\Omega(j^{1/3}).
\]

They remain valid, but the support conclusion is now strengthened below.

## 6. Square-root displaced support — `L-6811/T-6810`

If only `R` odd positions are displaced, the binary Hamming support has size
at most `2R`. A length-`L` factor that avoids those edited positions is a
Sturmian factor. Therefore

\[
\boxed{p_v(L)\le L+1+2RL.}
\]

Taking

\[
L_R
=
\left\lfloor{j-2\over2(R+1)}\right\rfloor
\]

forces a repeated factor. In an acyclic canonical failure, its two physical
starts are distinct, so exact dyadic separation and the return/gap theorem
apply.

Using the source-qualified Rhin bound gives the explicit floor

\[
\boxed{
R
\ge
\left\lfloor
{-A_j+\sqrt{A_j^2+2(\log_2 3)(j-2)}
 \over2\log_2 3}
\right\rfloor,}
\]

where

\[
A_j=14.3\log_2j+1+\log_2(3/2).
\]

Hence

\[
\boxed{
\liminf_{j\to\infty}{R_j\over\sqrt j}
\ge
\sqrt{\alpha/2}
=0.5615\ldots.}
\]

Every fixed-support, polylogarithmic-support, and `o(sqrt(j))` repair family is
therefore excluded. This strictly strengthens the old cube-root support
barrier.

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
\limsup\frac{\ell}{\log_2j}\le42.9.}
\]

`L-6810` supplies the independent post-return boundary. If

\[
T^j(r)=r+\Delta
\]

and the parity sequences from `r` and `r+Delta` agree for `ell_tail` steps,
then

\[
2^{\ell_{\rm tail}}\mid\Delta.
\]

The sharpened one-third window gives

\[
\boxed{
\ell_{\rm tail}
\le v_2(\Delta)
<\log_2(q/3).}
\]

Every surviving acyclic obstruction therefore branches away early at both
ends: from the mechanical extremizer near its start, and from its own old
parity tail immediately after the near-return.

## 8. Bilateral one-third near-return equation

`L-6812` records the coordinate-safe exact identities. If

\[
T^j(r)=s=r+d,
\]

then

\[
\boxed{
A_w=(2^j-3^q)r+2^jd
=(2^j-3^q)s+3^qd.}
\]

Thus

```text
source  = (A_w-2^j d)/(2^j-3^q);
endpoint= (A_w-3^q d)/(2^j-3^q).
```

The congruences are equivalent, but the quotients are not interchangeable.
Every first-crossing non-descent satisfies

\[
\boxed{0\le d<A_w/2^j<q/3<j/3.}
\]

The cycle case is exactly `d=0`; an acyclic CST failure has `1<=d<q/3`.

This also corrects a coordinate ambiguity in the first version of PR #83's
shifted equation: `A=nD+d3^q` uses the endpoint as `n`, while the source form
is `A=nD+d2^j`.

## 9. Lossless complete-prime-power compiler

`L-6809` factors

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

Under PR #34's source-qualified order window, one exact ordinary
first-crossing near-return is equivalent to the complete tuple:

```text
1. generalized-CRT-compatible local excess paths modulo every h_s;
2. the unique monotone ordinary excess path in the physical window;
3. the exact first-crossing inequalities after reconstruction;
4. one common ordinary 0 <= d < q/3;
5. every complete prime-power congruence A == 3^q d;
6. the canonical positive source (A-2^j d)/D.
```

A subset of factors may decode the word when its lcm-order exceeds `j-q`, but
all omitted prime powers and the first-crossing gate remain mandatory.
A proper-factor hit is not a near-return certificate.

## 10. Exact current blockers

### SC*

\[
\boxed{
\min_{w\in\mathcal W_N^{\rm sup}}r_w\to\infty.}
\]

### FC*

No nonmechanical, wrapped, logarithmically early-departing word with

```text
R >= sqrt(alpha*j/2)-O(log j)
```

passes every complete prime-power equation with one common

\[
0<d<q/3
\]

and the first-crossing/canonical gates.

The positive-cycle level `d=0` remains separate. `SC*+FC*`, together with
absence of nontrivial positive cycles, imply Collatz. Neither theorem is
proved here.

## 11. Literature boundary

The closest rigorous literature remains:

- Rozier--Terracol on paradoxical sequences and CST;
- Angeltveit on exact finite verification/descent sieves;
- Chang on map balance versus still-open pointwise orbit balance;
- Kramer on simultaneous real, `2`-adic, and `3`-adic exponent-code
  compatibility.

Almost-everywhere statements remain blocked by `R-6801`: positive ordinary
integers form a countable Haar-null subset of `Z_2`.

## 12. Review order

1. `claims/L-6803-canonical-start-end-rectangle.md`
2. `claims/L-6812-bilateral-shifted-near-return.md`
3. `claims/L-6813-sharpened-box-coupling-envelope.md`
4. `claims/T-6806-upper-mechanical-all-length-closure.md`
5. `experiments/X-6801-mechanical-cst/`
6. `claims/L-6811-support-sensitive-factor-complexity.md`
7. `claims/T-6810-square-root-displaced-support.md`
8. `claims/L-6808-bank-area-displacement-geometry.md`
9. `claims/T-6809-logarithmic-early-departure.md`
10. `claims/L-6810-near-return-self-shadowing.md`
11. `claims/L-6809-near-cycle-prime-power-compiler.md`
12. `claims/L-6807-small-displacement-full-denominator-bridge.md`
13. `claims/L-6805-bilateral-corner-stabilization.md`
14. `Q-6802-canonical-displacement-closure.md`
15. earlier entropy claims, reports, and literature audit

## Status boundary

All theorem-level claims remain **PROPOSED** pending independent
reconstruction. Claims using Rhin, generic effective linear forms, or the PR
#34 order theorem are explicitly source-qualified.

No proof of Collatz, counterexample, nontrivial cycle, or `K-####` object is
claimed.
