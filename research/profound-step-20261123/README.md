# Actual fibres, stationary renewal, and full complementary denominators

Date: 2026-11-23. Continuation of PR180 from
`a436db7b85f37abafea25f42d6f34afed02a29c0`.

**Collatz remains unresolved in this checkpoint.** This pass attacks the
original-law collision estimate, the real stationary realization, and the
complete positive-cycle arithmetic in parallel. It adds a source-qualified
density theorem without extra generator averaging, exact stationary
real-series and atomic classifications, an all-period complementary
denominator restriction, and a Lean reconstruction of the arithmetic
holonomicity consumer.

The five newly advanced peer branches were inspected at their exact heads:
PR175 `53ba1e1f...`, PR176 `fb402404...`, PR177 `aaa132e9...`,
PR178 `e6ed7f14...`, and PR182 `a7fd3ac9...`. The complete identities are in
[SOURCES.json](SOURCES.json) and the
[source refresh](../../reports/2026-11-23-profound-step/SOURCE_REFRESH.json).
The preceding whole-repository survey is retained; the old proof corpus was
not recompiled for this pass.

## 1. What the parallel attacks established

| Route | New deduction | Exact remaining closing step |
|---|---|---|
| Actual boundary and entropy rigidity | Almost every actual common boundary point has a tail-dense **unthickened** physical fibre trajectory in the full \(2,3\)-solenoid. Every nonempty open set has infinite summed mass under the original moving conditional fibre laws. In the maximum-Shannon branch, every fixed global scale-clock residue is uniform and independent of the entire limiting gap process. | Quantitative control of the original endpoint/source/carry labels, or an actual arithmetic confinement that contradicts the density theorem. |
| Stationary affine recursion | An exact finite logarithmic renewal identity; a conditional-drift classification of real series convergence; a quantitative critical lower-tail bound; classification of ternary atoms as rational-cycle components. The conditionally critical ternary factor is nonatomic. | A closing estimate on the same actual law at the required height and resolution. Neither nonatomicity nor the moving bound \(R_{m,j}<q_j\) supplies it. |
| Full-cycle arithmetic | For a primitive nontrivial positive integer shortcut cycle of length \(A\), with \(p\) odd states and full complementary reduced denominator \(b\), \(b>3(2p-A)\), with a sharper coprimality-sensitive finite product. | A positive-source constraint on the complete complementary carry and denominator strong enough to contradict that lower bound. |
| Arithmetic holonomicity | For the actual weighted parity coefficients, an eventual polynomial recurrence implies a constant recurrence. The written consumer then forces eventual parity and state periodicity. Ten new Lean declarations cover this recurrence core and the interval geometry above. | Construct the polynomial recurrence for every fixed actual source; eventual periodicity alone would still leave the positive-cycle problem. |

These are different statements on different explicitly identified objects.
The common real boundary, stationary real series, compact physical fibre,
and original ternary endpoint law are not equated.

## 2. The actual fibre theorem

Let \(q_j\) be the actual odd-unit orbit and
\[
 \chi_j=3^j2^{-A_j}.
\]
Retain the earlier canonical whole-path probability, its common boundary
\(Z\), and the source-qualified conclusion that its actual boundary law
\(\mu\) has upper local dimension one almost everywhere.

For escape the positive correction product gives
\[
 \chi_j\to\infty,\qquad 0<\chi_{j+1}\le\tfrac32\chi_j.
\]
A deterministic first-crossing argument proves that the set of real
points whose scaled phases eventually avoid a fixed circle interval is
uniformly porous and has upper box dimension below one. An elementary
restriction and Borel–Cantelli argument shows that \(\mu\) assigns that set
zero mass. Applying this simultaneously at every denominator \(6^k\) gives
\[
 \boxed{\{\iota(-\chi_jZ):j\ge N\}\text{ is dense in }X_6
        \text{ for every }N,\quad\mu\text{-a.e. }Z,}
\]
where
\[
 X_6=(\mathbb R\times\mathbb Q_2\times\mathbb Q_3)/
       \operatorname{diag}\mathbb Z[1/6].
\]
These are the actual physical classes
\([(B_\infty,q_j,q_j)]\). No extra powers of two have been inserted.

For the retained events \(E_j\uparrow\Omega\), probabilities \(p_j\), and
conditional physical fibre laws \(\kappa_j\),
\[
 \sum_j p_j\kappa_j(V)=\infty
 \qquad(V\subset X_6\text{ nonempty and open}).
\]
Thus eventual confinement of a positive portion of this actual boundary
to a proper closed solenoid subset is excluded.

A compact representative changes its ternary coordinate by the integer
part of the real scaling. It is consequently not the observable
\(q_j\bmod3^m\). Infinite occupation also gives no chronological
positive-frequency bound. These distinctions are retained in
[ENTROPY_ARITHMETIC.md](ENTROPY_ARITHMETIC.md).

The same note proves the fixed-modulus clock result in the actual
maximum-Shannon equality branch:
\[
 (\omega,\{j\ell\},(\lfloor j\ell\rfloor-A_j)\bmod m)
 \ \Longrightarrow\
 \eta\otimes\operatorname{Haar}_{\mathbb R/\mathbb Z}
      \otimes\operatorname{Unif}_{\mathbb Z/m\mathbb Z},
 \qquad\ell=\log_2 3.
\]
Every joint limit along the selected original subsequence has this product
law for each fixed \(m\). The proof uses the exact skew update, Fourier
ergodicity, and the domination of any finite-fibre lift by \(m\) times the
uniform lift. It does not assert a growing-modulus rate or independence
of a window from its own total gap.

## 3. What happens on the same stationary real series

For the retained stationary reversed-gap process, define
\[
 R_m=\sum_{i=1}^m3^{i-1}2^{-(G_1+\cdots+G_i)},\qquad
 h(x)=\log(1+1/(3x)).
\]
The finite logarithms are integrable, and
\[
 \mathbb E\log R_{m+1}-\mathbb E\log R_m
 =\log3-(\log2)\mathbb EG_1+\mathbb Eh(R_m).
\]
This exact identity is valid without independence.

Writing \(\bar g=\mathbb E[G_1\mid\mathcal I]\), the resulting full
classification is
\[
 \{R_\infty<\infty\}=\{\bar g>\log_2 3\}\quad\text{modulo null sets},
\]
together with
\[
 \mathbb Eh(R_\infty)
 =\mathbb E[(\bar g\log2-\log3)_+].
\]
In the conditionally critical branch the real partial sums diverge almost
surely. In its geometric iid equality case,
\[
 \eta(R_m\le H)\le
 \frac{\log(m+1)+2(\log2)\sqrt{\ell(\ell-1)(m+1)}}
      {m\log(1+1/(3H))}.
\]
The same ternary factor has an exact atomic classification: every atom
belongs to a rational Syracuse cycle, whose mean gap is a rational
number \(A/h\). Such atoms are impossible on a conditionally critical
component, since \(\log_2 3\) is irrational.

[STATIONARY_REAL.md](STATIONARY_REAL.md) also proves a finite inequality
on the original word, retaining its artificial periodic seam and a
specified bridge oscillation \(V_N\). Its minimum-source reconstruction
records that the first descending ladder time is infinite; localizing
a uniform actual time sample near the selected minimum costs
\(O(1/N)\) in probability and at least
\(\rho\log N-O(1)\) in relative entropy for a fixed positive target mass.
A recurrent iid affine law is not substituted for this source.

## 4. The full complementary cycle restriction

For a primitive positive integer shortcut cycle let
\[
 D_o=2^A-3^p,\qquad E_c=2^A-3^{A-p},\qquad
 b=E_c/\gcd(E_c,C_c),
\]
where \(C_c\) is the complete complementary carry.

The companion has distinct positive numerators with common reduced
denominator \(b\). Its positive product contributions can occur only at
odd numerators \(0<w<b\), each at most once. A convex midpoint integral
gives
\[
 \boxed{
 2^{\,2p-A}
 \le \prod_{\substack{0<w<b\\w\ {\rm odd}\\\gcd(w,b)=1}}
          \frac{3w+b}{4w}
 <2^{b/3}.}
\]
This proves \(b>3(2p-A)\) for all periods. If the original minimum is \(m\),
then
\[
 b>\frac{3\log(4/(3+1/m))}{\log(3+1/m)}A.
\]

The needed opposite restriction on the complementary denominator has not
been obtained. The exact negative cycle through \(-17\) demonstrates why
original integrality alone cannot give it: its complementary numerator
and denominator are \(5296\) and \(1967\), with gcd one. The note uses this
only against a sign-independent inference; positive original closure
remains the missing input.

See [ARITHMETIC_CLOSURE.md](ARITHMETIC_CLOSURE.md) for the full proof,
literature attribution, and exact control. No priority claim is made for
the general rational-cycle budget.

## 5. The literature and Lean recurrence route

For the fixed actual itinerary put
\[
 b_k=e_k3^{-p_{k+1}},\qquad B_n(z)=\sum_k b_kz^k.
\]
Its coefficients lie in \(\{0\}\cup\langle3\rangle\). The
Bézivin/Pólya-series theorem, as presented by Bell–Smertnig, says that
D-finiteness forces rationality. This pass supplies an elementary
finite-window reconstruction: normalize a polynomial recurrence by
\(3^{p_k}\), obtain a finite family of window polynomials, eliminate their
finitely many exceptional natural roots, and extract one nonzero
constant-coefficient recurrence.

The normalization for arbitrary binary itineraries and the complete
recurrence-collapse core are formalized. The subsequent finite-state
and odd-denominator arguments are written out in
[HOLONOMICITY.md](HOLONOMICITY.md). No polynomial recurrence is assumed
for every Collatz input. The exact tail equations were pursued, but their
integer indices do not close into a finite family.

The primary literature investigation also inspected higher-rank solenoid
rigidity, entropy inverse theorems, scenery normality, zero-exponent
invariance principles, critical affine renewal, and the full rational
cycle formulas. Each note states the actual theorem hypotheses and the
first missing interface. In particular, neither a finite real invariant
probability lift nor an independent convolution is asserted merely because
a related auxiliary law has those properties.

## 6. The central contradiction still sought

The preceding checkpoint proves that every fixed actual ternary time
limit \(\rho\) has a process-dependent strict collision gap:
\[
 \operatorname{Col}_m(\rho)
 \ge\exp[-m(\Phi(\log_2 3)-\delta)+O(1)]
 \quad\text{for some }\delta>0,
\]
where
\(\Phi(t)=t\log t-(t-1)\log(t-1)\).
An upper estimate
\[
 \operatorname{Col}_m(\rho)
 \le\exp[-m\Phi(\log_2 3)+o(m)]
\]
on that **same actual limit** would contradict escape.

The results above now exclude an atomic critical factor and eventual
compact fibre confinement, and control every fixed global clock residue
in the iid equality branch. They do not yet supply the required
collision exponent. The latest PR182 source boxes retain the exact carry
and source quotients; their cross-box dependence remains present.

The arithmetic route has its own precise open comparison in the complete
positive-cycle denominator. Neither issue has been hidden inside a
formal theorem premise.

## 7. Verification and reproduction

[THEOREMS.json](THEOREMS.json) lists ten freshly compiled declarations:
six in `ParityRecurrence.lean` and four in `ScaleAvoidance.lean`. The
compiler is Lean 4.34.1 at commit
`5045d0056413266e57c625dcd7c365b10e377c52`; Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The axiom audits contain
only `propext`, `Classical.choice`, and `Quot.sound`. The complete
measure-theoretic deductions and the cycle integral remain written
proofs with independent reviews.

With those runtimes installed:

```sh
python -X utf8 -B research/profound-step-20261123/check_lean.py \
  --lean /path/to/lean --mathlib /path/to/mathlib --report-dir /tmp/parity-replay
python -X utf8 -B research/profound-step-20261123/check_scale_lean.py \
  --lean /path/to/lean --mathlib /path/to/mathlib --report-dir /tmp/scale-replay
python -X utf8 -B research/profound-step-20261123/check_companion_control.py
python -X utf8 -B research/profound-step-20261123/check_packet.py --check-sources
python -X utf8 -B tools/validate.py
```

The packet identity check verifies exact file/source pins, review bindings,
and recorded formal scope. It is not itself a proof checker for the
written mathematics and does not recompile Lean.
[REVIEW_BINDINGS.json](REVIEW_BINDINGS.json) binds each review to the
actual reviewed bytes. Publication checks are run in a clean complete
checkout, with the execution receipts outside that checkout.
