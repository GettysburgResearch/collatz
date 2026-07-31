# Q-6802 — Canonical-displacement closure of the two exhaustive lanes

**Claim ID:** `Q-6802`  
**Status:** **OPEN**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Last updated:** 2026-07-31

## 1. Canonical variables

For a finite parity word `w` of length `j` and weight `q`, let

\[
(r_w,s_w)
\in[1,2^j]\times[1,3^q]
\]

be the canonical pair from `L-6803`, and put

\[
\Delta_w=s_w-r_w.
\]

When `2^j>3^q`,

\[
A_w=(2^j-3^q)r_w+2^j\Delta_w
\]

and therefore

\[
r_w>
\frac{A_w}{2^j-3^q}
\iff
\Delta_w<0.
\]

The residue lower bound and real no-descent threshold are one exact signed
integer displacement.

## 2. The two exhaustive theorem targets

### SC — source-corner exclusion

For supercritical prefixes, an ordinary all-time realization by one fixed
positive integer eventually has

\[
r_j=n,
\qquad
s_j=T^j(n).
\]

The exact target is

\[
\boxed{
\text{no infinite supercritical word has an eventually constant positive}
\text{ canonical source }r_j.}
\tag{SC}
\]

Equivalently,

\[
\boxed{m_N^{\mathrm{sup}}\to\infty.}
\]

### FC — finite-crossing displacement negativity

For every nontrivial least-counterexample-admissible first-crossing word,
prove

\[
\boxed{\Delta_w<0.}
\tag{FC}
\]

The universal form for every `r_w>=2` is Terras's Coefficient Stopping Time
conjecture. The least-counterexample form is narrower and sufficient.

`SC+FC` imply Collatz.

## 3. Positive cycles are already inside FC

`L-6814` proves that every nontrivial positive cycle, rotated to its minimum
and stopped at its first coefficient crossing, produces a **canonical**
first-crossing failure

\[
s_w\ge r_w.
\]

Indeed, if the cycle minimum is a higher lift

\[
n=r_w+t2^j,
\]

then

\[
T^j(n)-n
=(s_w-r_w)-t(2^j-3^q)\ge0
\]

forces `s_w-r_w>=0` already at the canonical member.

Thus FC contains both:

```text
Delta=0:
  a canonical positive-cycle word;

Delta>0:
  an acyclic canonical near-return.
```

A complete proof of FC automatically excludes nontrivial positive cycles.
No third cycle hypothesis is needed in the final implication.

## 4. One cofinal envelope would close both

Let

\[
F_j
=
\max_w{A_w\over2^j-3^{q(j)}}
=
{A_{\rm mech}(j)\over2^j-3^{q(j)}}.
\]

`L-6813` proves that any canonical failure satisfies

\[
\boxed{
m_{j-1}^{\rm sup}
\le r^+(w)
\le{A_w\over2^j-3^q}
\le F_j.}
\]

Hence the one cofinal theorem

\[
\boxed{m_{j-1}^{\rm sup}>F_j}
\tag{E}
\]

would force every late first crossing to descend. Since `F_j` is unbounded
along lower convergents, `(E)` would also force the monotone least-root
sequence to infinity.

The sharpened scalar sufficient envelope is

\[
F_j
<
{q(j)2^j
 \over
 3(2^j-3^{q(j)})}.
\]

The repository currently has no cofinal lower bound on `m_N^sup` at this
Diophantine scale. The envelope fusion is exact, but it does not by itself
prove source escape.

## 5. What is now closed in the acyclic part of FC

The present branch and PR #83 jointly close the following sectors.

### Mechanical representative

`T-6806/X-6801` prove at every length:

```text
j=2:
  word 10, root=endpoint=1;

every valid j>2:
  the upper-mechanical canonical representative descends,
  unless its finite segment contains a nontrivial positive cycle.
```

By `L-6814`, that retained cycle branch is itself another canonical FC
failure and remains inside the unified full-denominator target below.

### No-wrap nonmechanical sector

The clean `69xx` mechanical-wrap theorem on PR #83 supersedes closed PR #82
and proves that every no-wrap displacement has a strictly larger descent
defect than the mechanical representative. Thus every surviving
nonmechanical canonical failure is a genuine wrap.

### Low-complexity and sparse-repair sectors

`T-6803/T-6805/T-6807` exclude bounded-bank linear-complexity,
sub-square-root swap-area, and sub-`j^(2/3)` integrated-displacement families.

`L-6811/T-6810` strengthen the support side for acyclic failures:

\[
\boxed{
\liminf{R_j\over\sqrt j}
\ge\sqrt{\alpha/2},
\qquad
\alpha={\log2\over\log3}.}
\]

Thus every fixed-support, polylogarithmic-support, and `o(sqrt(j))` acyclic
repair family is excluded.

## 6. Exact geometry of any surviving acyclic FC obstruction

Let `v_j` be an unbounded family of acyclic canonical target failures. It must
satisfy all of the following.

### A. Nonmechanical dyadic wrap

It leaves the mechanical representative through the wrap branch.

### B. Two-thirds-scale integrated displacement

\[
\liminf
\frac{I_j}{j^{2/3}}
\ge
\left(\frac{\alpha}{2}\right)^{2/3}.
\]

### C. Square-root growing support

\[
\liminf
\frac{R_j}{\sqrt j}
\ge
\sqrt{\frac\alpha2}.
\]

### D. Early departure from the extremizer

If `ell_j` is the initial common-prefix length with the mechanical word, then,
source-qualifiably,

\[
\limsup
\frac{\ell_j}{\log_2j}
\le42.9.
\]

### E. Early self-departure after the near-return

Write

\[
T^j(r_j)=r_j+d_j.
\]

If the parity tails from `r_j` and `r_j+d_j` agree for `u_j` steps, then

\[
2^{u_j}\mid d_j,
\qquad
u_j<\log_2(q/3).
\]

### F. Bilateral full-denominator identity

`L-6812` gives

\[
\boxed{
A_w=(2^j-3^q)r+2^jd
=(2^j-3^q)s+3^qd,}
\]

with

\[
\boxed{0<d<q/3}
\]

in the acyclic case. The source is `(A-2^j d)/D`; the endpoint is
`(A-3^q d)/D`.

## 7. Lossless complete-prime-power target

Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

`L-6809` proves that one exact ordinary first-crossing non-descent is
equivalent to the complete tuple:

```text
1. compatible local excess paths modulo all h_s;
2. one unique monotone ordinary excess path in the full-order window;
3. the exact first-crossing prefix inequalities after reconstruction;
4. one common ordinary displacement 0 <= d < q/3;
5. every complete prime-power congruence A == 3^q d;
6. the canonical positive source (A-2^j d)/D.
```

An order-cover subset may decode the word but does not certify omitted prime
powers. A proper-factor hit is not a near-return.

The exact unresolved finite-crossing theorem is therefore:

\[
\boxed{
\begin{array}{c}
\text{Apart from the trivial word }10,\text{ no complete first-crossing tuple}\\
\text{passes every prime-power equation with one common }0\le d<q/3\\
\text{and all first-crossing/canonical gates.}
\end{array}}
\tag{FC*}
\]

For `d>0`, every unbounded acyclic family is additionally subject to the
wrap, early-departure, two-thirds-displacement, and square-root-support
restrictions in Section 6. For `d=0`, `(FC*)` is the positive-cycle equation.

Thus `(FC*)` proves FC in full, including nontrivial cycle exclusion.

## 8. Exact state of SC

For a hypothetical fixed ordinary all-time-supercritical root, `L-6805`
gives

\[
r_j=n,
\qquad
s_j=T^j(n),
\]

and

\[
\frac{r_j}{2^j}\to0,
\qquad
0<\frac{s_j}{3^{q_j}}
\le
\frac{n+j/2}{2^j}	o0.
\]

PR #80 and the present packet impose strong ordinary pressure:

```text
full divergence;
all states distinct;
linear physical record floor;
unbounded coefficient surplus;
logarithmically diverging mean surplus;
density-zero visits to every fixed low-surplus band.
```

None moves the same canonical source `r_j=n`. The exact missing theorem
remains

\[
\boxed{
\min_{w\in\mathcal W_N^{\rm sup}}r_w\to\infty.}
\tag{SC*}
\]

## 9. Complete positive implication

Assume `(SC*)` and `(FC*)`. If Collatz were false, let `n` be its least
positive counterexample.

- `(SC*)` excludes infinite coefficient stopping time.
- At the finite first crossing, minimality gives no descent and all
  least-counterexample admissibility conditions.
- The canonical word supplies a nontrivial complete tuple forbidden by
  `(FC*)`, whether its displacement is zero or positive.

Contradiction. Hence no least counterexample exists.

Equivalently, the stronger cofinal envelope theorem `(E)`, together with the
finite trivial-cycle audit, would close both lanes at once.

## 10. What does not count

The following do not close the target:

```text
another long finite prefix;
a proper denominator factor;
a factor tuple without a common displacement;
a reconstructed parity word that fails the first-crossing barrier;
physical growth after assuming an ordinary root;
measure-zero exceptional sets;
high factor complexity without canonical source control;
a compatible 2-adic point without Archimedean stabilization;
confusing the endpoint quotient with the source quotient;
excluding only d>0 while leaving the cycle level d=0.
```

## 11. Review boundary

Neither `(SC*)` nor `(FC*)` is proved in this file. `Q-6802` records the
smallest exact remaining objects after the current exclusions and prevents
partial factorwise, symbolic, or downstream-growth results from being
mistaken for the full Collatz implication.
