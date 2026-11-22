# Scoped review of the direct canonical-charge attempt

Date: 2026-11-22. Reviewer: `global_merger22`.

**Result: VERIFIED as a source-qualified record of an unsuccessful closing
attempt.** No canonical-charge vanishing or Collatz theorem follows from the
reviewed calculations.

Target: `agent22_analytic/central/DIRECT_CANONICAL_CHARGE_ATTEMPT.md`.

Frozen SHA256:
`32dca808c0a7e01e1bebf2968b0ee340e56a76c096760c45225f16f233b01727`.

The actual frozen file was read and hashed. This review reconstructs the reset
density, its bounds and compensation, the canonical-source transport, and the
last finite-horizon martingale/floor test. It does not revalidate the upstream
harmonic construction, population estimates, contact theorem, or stationary
normalization. For the last test, the displayed definitions in the pinned
`ENERGY_SYNTHESIS.md`, E1–E4, were inspected to verify the exact normalization
being imported. No new Lean verification is claimed. The reviewer contributed
the flow-increment observation underlying (9)–(10) during collaboration; the
complete argument was reconstructed here rather than treated as a blind
independent review of that contribution.

## 1. The exact reset density retains the right sources

Fix \(y\) in the last-contact set \(\Lambda\). Its future states
\(q_t=U^t y\), \(t\ge1\), are distinct noncontacts. A contact source
\(x\) contributes to a reset ending at \(y\) precisely when
\(Ux=q_t\) for one such \(t\). Every such parent \(x\) is itself a
last contact, since \(q_t\) has no future contacts. The actual inverse
path from \(q_t\) to \(y\) has no earlier contact, and its telescoping
probability is \(\nu(y)/\nu(q_t)\).

The target states \(q_t\) are distinct, so a source \(x\) is not counted
twice. Nonnegative summation gives exactly

\[
(Q_*\eta)(y)=\nu(y)\sum_{t\ge1}\beta(q_t).
\]

The Markov row sums and \(\|\eta\|_1=C\) then imply (5). No assumption
that \(\eta\) is stationary, or that inverse hitting times have finite
expectation, enters this argument.

## 2. Constants, summation, and compensation check

The contact upper bound \(\nu(x)\le2/(\delta x)\), together with
\(\sum_{Ux=q}1/x\le6/q\), gives the factor twelve in (7).
The explicit noncontact parent has mass strictly greater than
\(3\gamma/(2^{54}q)\), so the weaker non-strict upper bound in (8)
is valid. Its parent belongs to the retained domain whenever its target
does, as required.

For \(t\ge2\), the spine parent \(q_{t-1}\) is excluded from the
contact-parent sum. Harmonicity therefore gives (9). The scalar inequality
\((b-a)/b\le\log(b/a)\) telescopes against the increasing masses
\(\nu(q_t)\to C\), proving (10) with its stated first-step deficit.

The reciprocal-path bound (11) follows from the pinned retained path count
and \(\nu(q_t)\ge\nu(y)\). The diagnostic lower bound (12) is in the
correct direction: it is a lower bound on the **displayed upper-bound
expression**, not on \(H(y)\). Since
\(1/(\delta\nu(y))\ge y/2\) and \(m_y\le2y\), that expression cannot
certify contraction below one.

Integrating (10) uses a finite term
\(\sum\nu(y)/(Uy\,\nu(Uy))\le C/\gamma\). The logarithmic term is
nonnegative and may be infinite. Subtracting the finite common total \(C\)
is legitimate and gives (13), without an infinity-minus-infinity operation.
No strict inequality in the desired opposite direction has been obtained.

## 3. Canonical weights and the energy coefficient

After an original source has passed its last contact, its reset law has
density \(\nu(y)/\nu(q_k)\) on the last-contact ancestors of \(q_k\).
These ancestor sets increase to \(\Lambda\), with masses
\(\nu(q_k)\to C\). This proves total-variation convergence to \(\eta/C\).
Each original charge retains mass \(d(p)\); the variation error is bounded
by \(2d(p)\). Summability of the original component charge therefore
justifies (14) by dominated convergence, with no new endpoint factor.

The limiting source measure \(F\eta\) has mass \(D\). The distinct
measure \(F^2\eta\) is correctly introduced to represent the energy
coefficient \(D^2/C\). Since \(F=D/C\) is constant on this component,
the reset preserves that latter total exactly as stated in (15). The
argument does not silently identify these two measures.

## 4. The finite-cylinder floor and optional-stopping direction

The pinned normalization uses the unit indicator
\(g=\mathbf1_{3\nmid x}\), with stationary density bounded below by
\(\chi^{-1}g\) almost everywhere. The finite \(D_j\) are the canonically
specified cylinder averages. A unit cylinder is contained in the unit set,
so its average is at least \(\chi^{-1}\). This verifies (16) at every
ordinary unit for \(j\ge1\), without assigning an arbitrary
almost-everywhere representative to an ordinary integer. The stationary
density in this source quotation is distinct from the component charge
also denoted \(D\) earlier in the note.

For \(t\ge s+1\), stopping at \(\tau_M^0\wedge s\) keeps every density
horizon positive. The imported bounded martingale is therefore applicable.
On early entrance, its value is at least \(1/(\chi M)\), and on the
complement it is nonnegative. Thus

\[
\Pr_q^G(\tau_M^0\le s)
\le\chi M\,D_t(q)/G(q),
\]

exactly as in (17). It is an upper bound on early entrance. Reversing its
direction would invalidate the attempted closure.

Finally, an actual contact atom \(y\) at inverse depth \(\ell\) belongs
to the predecessor collection once the tested horizon reaches \(\ell\).
Any floor required for that collection is then at most \(y\). Before
that depth this atom contributes nothing to the early-entrance event.
The final incompatibility check is therefore correct.

## Verdict

The frozen note accurately identifies the uncompensated arithmetic term
and preserves the original canonical masses. Its source-qualified and
no-closure verdict is supported by the calculations. No correction is
required within this review scope.
