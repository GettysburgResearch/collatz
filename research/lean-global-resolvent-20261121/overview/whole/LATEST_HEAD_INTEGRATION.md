# Combining the concurrent PR183 continuation with checkpoint 9

**Full convergence remains OPEN.** Before this checkpoint was published,
PR183 advanced from `907a540943090968bc683b1b9246208e9053c1f8` to
`68345f60a4f757acb42a69a4ac95910f8ce26163`. Its new packet is
`research/profound-step-20261122/`; its execution report records 52 public
theorem audits across five new modules. The coordinating agent read the
new entrypoint, reconstruction review, carry/compression bridge, full
operator note, and full asynchronous-residue note. The three parallel lanes
read the exact overlapping arithmetic, carry, and transport sources.

That update matters. It reaches the same qualitative independent-exponent
cycle classification and an equivalent nonpositive-offset carry mechanism.
Those are concurrent derivations and receive explicit credit. The useful
combined advances are described below. The 52 upstream declarations are
not added to our local audit count or claimed to have been recompiled here.

## 1. A smaller effective cutoff for the entire supplied word

PR183's written BC-8 sharpens quadratic height propagation to the real
factor \(\alpha=\log_2 3\). Combining it with this packet's exact
block-coefficient reserve and suffix rotation gives, outside the explicit
template-cycle cases,

\[
A\le\left(\sum_{i<r}\alpha^i\right)
\bigl(b+\kappa\log_2 A\bigr).
\tag{1}
\]

This concerns the complete supplied word, not only its primitive period.
The proof uses the same actual boundary sources throughout. Inactive
blocks are removed; a fixed block is retained as a replayable cycle case.
The published logarithm estimate remains the only transcendence input.

An exactly computable cutoff follows without numerical logarithm
rounding. For \(r\ge1\), put

\[
E_r=\left\lceil\frac{8^r-5^r}{3\cdot5^{r-1}}\right\rceil,
\quad P=\kappa E_r,\quad Q=bE_r,
\]

and let \(j\) be the least integer with \(4P\le2^j\). Then

\[
\boxed{A<\max(16,4Q,4Pj).}
\tag{2}
\]

The elementary chain uses \(\alpha<8/5\), certified by
\(3^5<2^8\). The cutoff's dependence on the number of pieces improves
from the earlier coarse \(4^r\) scale to a linear factor times
\((8/5)^r\), with its explicit coefficient constants retained. The
full proof and precise upstream comparison are in
[SHARPER_BLOCK_CUTOFF.md](SHARPER_BLOCK_CUTOFF.md).

This is a written refinement. The formal block-budget module still proves
its original conservative integer inequality. No claim is made that the
enormous finite classification enumeration was executed, or that every
cycle has a sufficiently short block description.

## 2. Ordinary descent and source-grade descent fit one induction

PR183's carry/compression bridge correctly distinguishes the source's
complete-certificate grade from ordinary target height. Its debt-growth
family has genuine ordinary descent, but such a descent must be connected
to the active source induction before it can be used there.

The new [SourceTargetInduction.lean](lean/Collatz/SourceTargetInduction.lean)
provides that general connection. The outer induction uses the existing
complete-source grade. The inner induction uses the current query's target
\(t\), while keeping the exact supplied source and word unchanged.
For the original interval \(0<t\le2S+1\), every positive \(x<t\)
is still in that same interval. Consequently two kinds of recursion are
compatible:

- A child paid by a strictly smaller complete-source grade may use its own
  checked source interval, even when its target is larger than the old target.
- A smaller positive target or independently timed smaller partner may keep
  the original complete source certificate and grade unchanged.

The theorem `complete_of_joint` discharges the inner hypothesis by strong
induction and returns the existing `Complete Interval` interface unchanged.
The existing outer induction then applies. The module also proves an actual
ordinary-descent rule and an independent-clock merger rule:

\[
0<x<t,\quad T^L(x)=T^R(t)
\quad\Longrightarrow\quad
\text{the same-source induction pays for the merger}.
\tag{3}
\]

Here \(x\) need not be inside the maximum *lower-grade* prefix envelope.
It is paid by the smaller-target induction instead. The original queried
target in (3) is essential: decreasing below an intermediate, larger carry
does not establish \(x<t\) for the earlier query.

`MixedWitness` and `MixedCover` expose the remaining successful-coverage
condition. A witness supplies a known terminal proof, a genuinely smaller
partner merger, or an explicitly certified lower-grade child with a valid
transport back to the target. `collatz_of_mixed_cover` proves the global
consequence of a universal cover. **The cover is not proved.** The new
contribution is the compatibility of the two available descent mechanisms,
not a claim that every remaining state has a successful branch.

### A concrete capture of the credited debt-growth residue

PR183 identifies the ordinary five-clock class

\[
T^5(32a+23)=27a+20<32a+23.
\]

The new module checks this credited identity and installs it as a valid
same-source branch. It also proves a stronger paid handoff for the entire
associated source residue when the actual supplied source is already
\(S=8r\), \(r=32a+13\). For \(n=9r+2\),

\[
T^5(n)=243a+101
\le256a+105=8r+1.
\tag{4}
\]

Halving the supplied source changes its even exponent from three to two,
retains its entire odd certificate, and pays for (4). The theorem
`residue13_carry_paid_capture` is universal in the nonnegative parameter
and in the supplied complete odd word. It obtains no free padding from
an earlier query whose source was only \(r\).

PR183's fully certified debt-growth family also has an unbounded final gap;
it is not an alphabet-four residual counterexample. Its high terminal gap
is already a resource for PR177's high-gap rules. The capture above is a
valid broader residue rule, not evidence that this family was a new global
obstruction. [SOURCE_TARGET_INDUCTION.md](SOURCE_TARGET_INDUCTION.md) gives
the exact formal interface and evidence.

## 3. The canonical boundary permits an entire L² source class

PR183 already identifies one bilateral-shift channel per escaping ordinary
component and computes the asynchronous Abel and Cesàro residues. Its
complete-source extension assumes

\[
\sum_x |a(x)|/\sqrt{\nu(x)}<\infty,
\]

and it proves that condition for its original projected \(n^{-4}\) source.
We retain that result and its cycle-sensitive second-order pole.

This checkpoint's last-contact measure \(\eta=\nu\mathbf1_\Lambda\)
has a special additional property:

\[
\sum_{k\ge0}L^k\eta\le\nu,
\qquad \eta(\mathcal C)=C_{\mathcal C}.
\tag{5}
\]

It permits an extension to every boundary source \(a=\eta f\) with
\(f\in L^2(\eta)\). For
\(B_{r,\theta}a=\sum_{k\ge0}r^ke^{ik\theta}L^ka\) and
\(C_{J,\theta}a=J^{-1}\sum_{k<J}e^{ik\theta}L^ka\), weighted
Cauchy–Schwarz on the actual ancestor rows gives

\[
\boxed{
(1-r^2)\mathcal E_\nu(B_{r,\theta}a),\quad
J\mathcal E_\nu(C_{J,\theta}a)
\le\|f\|_{L^2(\eta)}^2.
}
\tag{6}
\]

The omitted-source error is controlled by its \(L^2(\eta)\) norm,
uniformly in frequency and the clock or discount parameter. Thus PR183's
finite-source formulas pass to this whole class without a square-root
summability premise or a bound on meeting times. At zero frequency, the
limiting residue is exactly

\[
\left\|\mathbb E_\eta[f\mid\text{component partition}]\right\|_2^2.
\tag{7}
\]

For the canonical source \(a=\eta\), this equals
\(\|\eta\|_1=\sum_\mathcal C C_\mathcal C\): the upper bound is
attained asymptotically. The proof is in
[LAST_CONTACT_CHANNEL_INTEGRATION.md](LAST_CONTACT_CHANNEL_INTEGRATION.md),
with an independent reconstruction of its Cauchy–Schwarz and uniform-tail
steps. These are source-qualified written deductions.

This extends the source class on the last-contact antichain. It does not
project arbitrary original sources onto that antichain, change their clocks,
or show that the positive component residue vanishes. The actual full-source
zero-residue estimate and cycle exclusion remain distinct global tasks.

## 4. The next step after combining the latest work

The arithmetic program can now mix ordinary descent, asynchronous smaller
partners, maximal lower-grade source intervals, and complete source rewrites
inside one proved induction. Its missing mathematical assertion is an
all-state successful cover using those mechanisms.

The analytic program now has both the exact possible escape contribution
and a canonical finite ordinary boundary carrying it. A little-oh estimate
for the original cycle-sensitive residue, or a sufficient quantitative
contact lower bound on the relevant marked roots, would be a new closing
input. The proved upper bounds and finite boundary structure do not supply
either one.

The classifier now has a better explicit cutoff. It still needs an upper
description bound for every hypothetical cycle to become a global cycle
argument. The forced band admits arbitrary long finite parity prefixes;
an argument based on successive returns of one fixed source must add
information beyond a single marked entrance.
