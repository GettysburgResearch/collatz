# Direct attempt to eliminate one fixed ordinary escape

Date: 2026-11-22. **Outcome: no closing inequality obtained.** This records
the actual fixed-source calculation, rather than proposing another operator
equivalence or presenting a finite family as a universal argument. No new
Lean module or full Collatz claim is attached.

## 1. Inputs and the fixed object that must disappear

The frozen sources inspected in this pass are:

| Source | Head | Material used |
|---|---|---|
| PR185 | `53f01ca5b443ef57ef2160b4996dbb2cc87f7395` | `research/multiple-attacks-20261122/CONTACT_RETURN_FINITE_REFERENCE.md`, `CONTACT_EXIT_ACCOUNTING.md`, `EXCURSION_RESOLVENT_INTERFACE.md`, `HARMONIC_KERNEL_FACTORIZATION.md`, and `STRICT_GREEN_VOLTERRA.md` |
| PR176 | `31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6` | `research/lean-global-resolvent-20261121/overview/profound/ALL_DEPTH_FIRST_CROSSING.md`, `MOVING_TILT_WINDOW.md`, and `ENDPOINT_TILT_CRITICALITY.md` |
| PR180 | `ab3973099f0d285bbe88972382ad599bb02cd460` | `research/lean-joint-20261122/ORDINARY_BOUNDARY.md`, `CONTACT_CLOCK.md`, and `FINITE_SPIKE_CLOSURE.md` |

The exact paths and local source hashes are in `SOURCE_SNAPSHOT.json`.
The ordinary harmonic reference retains the population and canonical-envelope
qualifications of these sources. It is not an unconditional theorem supplied
by this note.

Use the ordinary shortcut map \(T\), its accelerated odd map \(U\), and the
nonperiodic odd ternary-unit domain used by the cited sources. Their reference
obeys

\[
L\nu=\nu,\qquad \frac\gamma n\le\frac{G(n)}n\le\nu(n),
\qquad G(n)\ge\delta n\nu(n),\qquad G\le V.
\tag{1}
\]

Every retained finite path has survival product at least \(\delta>0\).
Fix a hypothetical escaping odd unit \(x\), and put \(c=\nu(x)>0\).
Its ordinary source label is retained throughout the following calculations.
At every later odd state \(z\) on its trajectory,

\[
\nu(z)\ge c,\qquad G(z)\ge\delta c z.                       \tag{2}
\]

The aim was to contradict this fixed positive flow using the new all-depth
crossing estimate and contact contraction. The obstruction in the attempted
combination occurs before any generic spectral theorem is relevant.

## 2. All-depth crossing: the actual weight survives the sparse source count

Choose a dyadic floor \(H=2^m>x\). Choose a sufficiently late odd endpoint
\(q\) of this same escaping trajectory with \(q\ge3^m\). Let \(n_H\) be
the last state below \(H\) on the actual shortcut segment from \(x\) to
\(q\). Then

\[
n_H<H,\quad T(n_H)\ge H,\quad
T^j(n_H)\ge H\text{ until the first hit of }q.
\]

The source \(n_H\) is odd: an even step cannot upcross. It is also a ternary
unit, because the original unit orbit stays in the unit classes. Since the
trajectory is nonperiodic, the hit of \(q\) is unique. Therefore it belongs
to the exact physical set \(E_H(q)\) in PR176's crossing theorem, and

\[
\frac{2H-1}{3}\le n_H<H.                                    \tag{3}
\]

Let \(\omega_q(n_H)=3^s2^{-A}\) be the coefficient of this actual segment.
The exact forward product identity and the retained survival bound give

\[
\omega_q(n_H)=\frac q{n_H}\Lambda_{n_H,q},
\qquad \Lambda_{n_H,q}\ge\delta.
\]

Combining this with (2) yields

\[
\boxed{\omega_q(n_H)G(n_H)\ge\delta^2 c q.}                 \tag{4}
\]

Consequently the canonical weighted crossing sum on these actual targets
satisfies

\[
\sum_{n\in E_H(q)}\omega_q(n)G(n)\ge\delta^2 c q.
\tag{5}
\]

In contrast, the new **unweighted** theorem gives

\[
\sum_{n\in E_H(q)}\omega_q(n)
\le q\left(19497/H+6H^{-1/20}\right).
\tag{6}
\]

These formulas are compatible. The fixed flow has arrived at a sparse
boundary source whose canonical value has grown:

\[
G(n_H)\ge\delta c(2H-1)/3.                                  \tag{7}
\]

Thus the attempted substitution of a bounded contact value at that boundary
is invalid. The crossing state is no longer a contact at a fixed threshold.
In particular the proposed sufficient assumption
\(\sup_{n\in E_H(q)}G(n)=o(H^{1/20})\) would already exclude the tracked
escape; it does not follow from the unweighted estimate.

This calculation does not use histories that never cross the floor. It
retains a source that really does cross, with all its actual clocks.
That makes the first missing estimate precise even within the part of the
inverse kernel for which all-depth counting has been proved.

The same issue appears directly for the original weights of the moving-bin
criterion. The fixed atom \(x^{-2}\) arrives at \(n_H\) unchanged; it does
not become \(n_H^{-2}\). Replacing the former by the latter is an unproved
source reset, and would erase exactly the fixed counterexample being tested.

## 3. Exhausting contact thresholds do not recover a useful contraction rate

For a fixed threshold \(M\), PR185 proves contraction with

\[
\varepsilon_M=\frac{3\delta\gamma}{64M},\qquad
\rho_M=1-\varepsilon_M.
\]

Its induced operator kills the last-contact exit, even if that exit is an
infinite ordinary escape. The escape-labelled terminal flux is explicitly
retained in `CONTACT_EXIT_ACCOUNTING.md`; its geometric decay in contact
time is not ordinary absorption.

I also tried increasing \(M\) to include the whole prefix of the fixed
trajectory. The loss can be quantified on actual record maxima. Write
\(q_i=U^i x\), and let \(Q=q_k\) be a record maximum. Set

\[
M_Q=\max\bigl(2,V(q_0),\ldots,V(q_k)\bigr).
\]

Every displayed state is then a contact, so there are exactly \(k\)
contact returns along this prefix. But (2) gives \(M_Q\ge\delta cQ\).
The source-qualified retained-path count imported by PR185 is
\(\#\{i:q_i\le Q\}\le5Q^{39/40}\). Therefore

\[
k\varepsilon_{M_Q}
\le\frac{15\gamma}{64c}Q^{-1/40}.
\tag{8}
\]

Since \(\varepsilon_M\le3/64\),

\[
0\le-k\log\rho_{M_Q}
\le\frac{15\gamma}{61c}Q^{-1/40}\longrightarrow0.
\tag{9}
\]

Thus the guaranteed contraction factor \(\rho_{M_Q}^k\) tends to one
along this exhausting sequence. It does not tend to zero. This concerns
the available bound, not a claim that the actual flow has no growth.
The attempted fixed-to-moving-threshold passage cannot supply the desired
ordinary-time estimate from the proved constants.

## 4. A contact does have a large inverse floor, but that is not a stopped trace bound

There is one useful exact compatibility check with PR180's finite-horizon
theorem. If \(q\in\mathcal C_M\) and an ordinary unit \(y\) reaches \(q\),
then harmonic monotonicity and the contact upper bound give

\[
\frac\gamma y\le\nu(y)\le\nu(q)\le\frac M{\delta q},
\qquad\text{hence}\qquad y\ge\frac{\delta\gamma}{M}q.
\tag{10}
\]

Thus a contact root really has an inherited inverse-basin floor comparable
to its height. It is legitimate to use that floor in the finite-horizon
spike theorem. It does not justify replacing a finite horizon by all depths.

More specifically, that theorem controls \(D_s(q)/q\). The stopped
Doob error in PR185 is normalized by \(G(q)\), or by \(q\nu(q)\), which
lies between fixed positive constants on a fixed contact section. Dividing
by \(q\) has therefore removed a factor which must be restored in the
actual trace estimate. The finite-horizon bound does not establish small
\(|D_t-D_s|/G\) at arbitrarily fine, adaptively selected precision.
Nor does (10) give the ordinary-time tail of the next contact excursion.

The maximal Haar estimate in `STOPPED_MIXING_INTERFACE.md` remains a
statement for its displayed Haar law. Applying it to this fixed ordinary
source would require the arithmetic stopped-correlation estimate stated
there. I did not obtain that estimate.

## 5. A source-flow bound on reset influx, and its remaining strictness gap

For the analytic lane's contact-reset attempt, fix an escaping last contact
\(y\) and write \(q_t=U^t y\), \(t\ge0\). Let

\[
a_t=\sum_{\substack{z\in\mathcal C_2\\Uz=q_t}}\nu(z),
\qquad\beta(q_t)=a_t/\nu(q_t),\qquad
C=\lim_t\nu(q_t).
\]

The first contact-parent mass satisfies \(a_1\le\nu(q_1)\). For
\(t\ge2\), the spine parent \(q_{t-1}\) is noncontact, so harmonicity
gives the sharper source-flow charge

\[
a_t\le\nu(q_t)-\nu(q_{t-1}).
\]

Using \((b-a)/b\le\log(b/a)\) for \(0<a\le b\),

\[
\sum_{t\ge1}\beta(q_t)
\le\beta(q_1)+\log\frac C{\nu(q_1)}.
\tag{11}
\]

This charges distinct incoming contact mass against actual harmonic-flow
growth instead of merely summing an ordinary-time reciprocal-height bound.
It does not give the required upper bound by one. In particular, the
positive noncontact branch at \(q_1\) has not been shown to dominate all
later contact influx. I sent this exact inequality and its strictness gap
to the analytic lane; I have not treated it as a capacity-vanishing proof.

## 6. The unresolved fixed source and cycles

The censored moving-endpoint statistic at \(\sigma_t=1/t\) retains a
positive contribution from every fixed source which misses one. Neither
the unweighted crossing saving nor the available contact-time contraction
has bounded that retained contribution to zero. Equations (4)–(9) identify
the concrete failure of the two attempted combinations on the same original
source. The ordinary harmonic argument also kills periodic points, so it
does not by itself address a hypothetical additional cycle. Such a cycle
is retained by the censored moving-bin criterion and cannot be discarded
when comparing the two constructions.

The first genuinely missing arithmetic estimate is still a source-preserving
bound that makes the canonical weighted arrival or the terminal contact
flux vanish. A bound proved only for fresh boundary points, Haar-typical
residues, fixed positive endpoint tilts, or a fixed contact threshold does
not provide it. No such estimate was obtained in this pass.
