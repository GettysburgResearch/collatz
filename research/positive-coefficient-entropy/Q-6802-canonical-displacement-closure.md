# Q-6802 — Canonical-displacement closure of the two exhaustive lanes

**Claim ID:** `Q-6802`  
**Status:** **OPEN**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31

## 1. Canonical variables

For a finite parity word \(w\) of length \(j\) and weight \(q\), let

\[
(r_w,s_w)
\in[1,2^j]\times[1,3^q]
\]

be the canonical pair from `L-6803`, and put

\[
\Delta_w=s_w-r_w.
\]

When \(2^j>3^q\),

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

The residue lower bound and real no-descent threshold are not independent.
Their complete difference is the one signed integer \(\Delta_w\).

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
\text{ canonical source }r_j.
}
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

The universal form for every \(r_w\ge2\) is Terras's Coefficient Stopping
Time conjecture.  The least-counterexample form is narrower and sufficient.

`SC+FC` imply Collatz.

## 3. What is now closed in FC

The present branch and PR #82 jointly close the following complete sectors,
modulo the explicitly retained positive-cycle alternative.

### Mechanical representative

`T-6806/X-6801` prove at every length:

```text
j=2:
  word 10, root=endpoint=1;

every valid j>2:
  the upper-mechanical canonical representative descends,
  unless its finite segment contains a nontrivial positive cycle.
```

### No-wrap nonmechanical sector

PR #82 `T-6607` proves that every no-wrap displacement has a strictly larger
descent defect than the mechanical representative.  Thus all acyclic no-wrap
words descend.

### Low-complexity and sparse-repair sectors

`T-6803/T-6805/T-6807/T-6808` exclude cofinal acyclic target-failure
families with bounded-bank linear complexity, sub-square-root mechanical
repair, sub-\(j^{2/3}\) integrated displacement, or sub-\(j^{1/3}\) displaced
support.

## 4. Exact geometry of any surviving acyclic FC obstruction

Let \(v_j\) be an unbounded family of acyclic canonical target failures.  It
must satisfy all of the following.

### A. Nonmechanical dyadic wrap

It leaves the mechanical representative through the wrap branch of PR #82
`T-6607/L-6602`.

### B. Two-thirds-scale displacement

\[
\liminf
\frac{I_j}{j^{2/3}}
\ge
\left(\frac{\alpha}{2}\right)^{2/3},
\qquad
\alpha=\frac{\log2}{\log3}.
\]

### C. Cube-root growing support

\[
\liminf
\frac{R_j}{j^{1/3}}
\ge
\left(\frac{\alpha^2}{2}\right)^{1/3}.
\]

### D. Early departure from the extremizer

If \(\ell_j\) is the initial common-prefix length with the mechanical word,
then, source-qualifiably,

\[
\limsup
\frac{\ell_j}{\log_2j}
\le42.9.
\]

The exact source-free candidate inequality is `T-6809` equation `(3)`.

### E. Early self-departure after the near-return

Write

\[
T^j(r_j)=r_j+\Delta_j,
\qquad0<\Delta_j<j/2.
\]

If the parity tails from \(r_j\) and \(r_j+\Delta_j\) agree for \(u_j\)
steps, then

\[
2^{u_j}\mid\Delta_j,
\]

so

\[
u_j<\log_2(j/2).
\]

### F. Small-displacement full-denominator identity

\[
\boxed{
2^j-3^q
\mid
A_w-2^j\Delta,
\qquad
0<\Delta<j/2.
}
\]

The level \(\Delta=0\) is the positive-cycle case.

## 5. Lossless complete-prime-power target

Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

`L-6809` proves that one exact ordinary first-crossing near-return is
equivalent to the following complete tuple:

```text
1. compatible local excess paths modulo all h_s;
2. one unique monotone ordinary excess path in the full-order window;
3. the exact first-crossing prefix inequalities after reconstruction;
4. one common ordinary displacement 0 <= Delta < j/2;
5. every complete prime-power shifted-numerator congruence;
6. the canonical positive source range.
```

An order-cover subset may decode the word but does not certify the omitted
prime powers. A proper-factor hit is not a near-return.

Therefore the exact unresolved FC theorem is:

\[
\boxed{
\begin{array}{c}
\text{No growing-support, early-departing wrapped excess path}\
\text{passes every complete prime-power equation with one common}\
0<\Delta<j/2\text{ and the first-crossing/canonical gates.}
\end{array}}
\tag{FC*}
\]

Together with no nontrivial positive cycle, `(FC*)` proves `(FC)`.

## 6. Exact state of SC

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

PR #80 and the present entropy packet impose strong ordinary pressure:

```text
full divergence;
all states distinct;
linear physical record floor;
unbounded coefficient surplus;
logarithmically diverging mean surplus;
density-zero visits to every fixed low-surplus band.
```

None moves the same canonical source \(r_j=n\).  The exact missing theorem
remains source-coordinate escape:

\[
\boxed{
\min_{w\in\mathcal W_N^{\mathrm{sup}}}r_w\to\infty.
}
\tag{SC*}
\]

A physical growth theorem, almost-everywhere mixing theorem, or compatible
free completion does not prove `(SC*)`.

## 7. Complete positive implication

Assume `(SC*)`, `(FC*)`, and absence of nontrivial positive cycles.  If
Collatz were false, let \(n\) be its least positive counterexample.

- `(SC*)` excludes infinite coefficient stopping time.
- At the finite first crossing, minimality gives no descent and all the
  least-counterexample admissibility conditions.
- The canonical word must therefore supply either a positive cycle or the
  acyclic tuple excluded by `(FC*)`.

Both alternatives are impossible. Hence no least counterexample exists.

## 8. What does not count

The following do not close the target:

```text
another long finite prefix;
a proper denominator factor;
a factor tuple without a common Delta;
a reconstructed parity word that fails the first-crossing barrier;
physical growth after assuming an ordinary root;
measure-zero exceptional sets;
high factor complexity without canonical source control;
a compatible 2-adic point without Archimedean stabilization.
```

## 9. Review boundary

Neither `(SC*)` nor `(FC*)` is proved in this file.  `Q-6802` records the
smallest exact remaining objects after the current exclusions and prevents
partial factorwise, symbolic, or downstream-growth results from being
mistaken for the full Collatz implication.
