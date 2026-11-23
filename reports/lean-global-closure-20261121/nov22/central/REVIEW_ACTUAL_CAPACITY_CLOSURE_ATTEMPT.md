# Scoped independent review of the fixed-source capacity attempt

Date: 2026-11-22.

**Verdict: VERIFIED under the displayed source qualifications, for the
fixed-source crossing calculation, the moving contact-threshold
calculation, and their source and predecessor-floor obligations.**
The reviewed note correctly reports an unsuccessful closure attempt.
This receipt does not certify a vanishing theorem or a Lean proof.

## Exact artifact and scope

Reviewed file:
agent22_merger/central/ACTUAL_CAPACITY_CLOSURE_ATTEMPT.md

SHA256:
452d5c10183681e47c8acf09a6f96fd93e828de110e2a207d7b9273084eb4b9f

I independently reconstructed Sections 2--4 and checked their interfaces
against the following exact source files:

- PR176, 31c4a880ea4acf6eec4783e68bfc75e2cf8e7fe6:
  research/lean-global-resolvent-20261121/overview/profound/ALL_DEPTH_FIRST_CROSSING.md.
- PR185, 53f01ca5b443ef57ef2160b4996dbb2cc87f7395:
  research/multiple-attacks-20261122/CONTACT_RETURN_FINITE_REFERENCE.md.
- PR180, ab3973099f0d285bbe88972382ad599bb02cd460:
  research/lean-joint-20261122/FINITE_SPIKE_CLOSURE.md.

The ordinary harmonic flow, its positive lower bound and bounded path
correction, and the imported path-count estimate were treated as the
explicitly qualified inputs stated in the note. I did not replay their
earlier construction. I also did not independently recertify the external
censored moving-bin criterion mentioned in Section 6.

## 1. Fixed-source weighted crossings

For the hypothetical escaping unit source \(x\), let \(c=\nu(x)>0\).
Harmonicity gives \(\nu(z)\ge c\) at every later odd state. Thus
\(G(z)\ge\delta c z\), with no replacement of the original source.

For \(H=2^m>x\), a sufficiently late odd endpoint \(q\ge3^m\)
exists on an injective positive orbit. The last shortcut state \(n_H<H\)
before that endpoint is odd, remains a ternary unit, and satisfies
\((2H-1)/3\le n_H<H\). Its subsequent segment stays above the floor
and hits \(q\) for the first time. It is therefore a source in the
actual first-crossing set, not a formal inverse word.

The exact coefficient identity is
\[
\omega_q(n_H)=\frac q{n_H}\Lambda_{n_H,q}.
\]
Using \(\Lambda_{n_H,q}\ge\delta\) and
\(G(n_H)\ge\delta c n_H\) gives the stated lower bound
\[
\omega_q(n_H)G(n_H)\ge\delta^2cq.
\]
The unweighted theorem applies because
\[
q+1>3^m=H(3/2)^m,\qquad
\lfloor\log_2 H\rfloor=m.
\]
Its constants \(19497/H+6H^{-1/20}\) were transcribed correctly.
There is no contradiction between that estimate and the weighted lower
bound: the arriving \(G(n_H)\) grows at least linearly in \(H\).
For the unit-domain operator, the weighted sum may equivalently be
restricted to unit crossing sources; the canonical zero extension on
nonunits leaves it unchanged.

The statement that a transported original atom \(x^{-2}\) remains
\(x^{-2}\), rather than becoming \(n_H^{-2}\), is the correct
source-retaining interpretation. No collision or return multiplicity
is needed for this single tracked atom.

## 2. Exhausting contact thresholds

At a record maximum \(Q=q_k\), every state in the finite odd prefix
lies below \(Q\). Setting
\(M_Q=\max(2,V(q_0),\ldots,V(q_k))\) makes precisely those \(k\)
successive edges into contact returns along the prefix. The estimate
\(M_Q\ge\delta cQ\) follows from the retained flow at the endpoint.

The imported path count yields \(k\le5Q^{39/40}\). Hence
\[
k\varepsilon_{M_Q}
\le \frac{15\gamma}{64c}Q^{-1/40}.
\]
The source supplies \(0<\varepsilon_{M_Q}\le3/64\). Using
\(-\log(1-u)\le u/(1-u)\) gives
\[
0\le-k\log\rho_{M_Q}
\le\frac{15\gamma}{61c}Q^{-1/40}.
\]
Thus \(\rho_{M_Q}^{\,k}\to1\) on the unbounded record sequence.
Both constants and the direction of the limit are correct. The note
properly identifies this as a failure of the guaranteed contraction
bound, not as a lower bound on actual surviving mass or an estimate
of actual harmonic-flow growth.

## 3. The real predecessor floor and the normalization cost

For a fixed-threshold contact \(q\) and any unit ancestor \(y\),
\[
\frac\gamma y\le\nu(y)\le\nu(q)\le\frac M{\delta q}
\]
does prove the all-ancestor floor \(y\ge\delta\gamma q/M\).
It is a genuine floor, not the minimum of a forward suffix.
The finite-horizon theorem may therefore use that floor, while
retaining its own conditions \(9^m\le b\) and its tested depth.

The note does not substitute that finite theorem for an all-depth
bound. It also correctly keeps the normalization distinction:
on a fixed contact section, \(G(q)\) and \(q\nu(q)\) are bounded
above and below by positive constants, whereas the finite theorem
controls \(D_s(q)/q\). Restoring the factor \(q\) is necessary
before estimating a normalized stopped Doob payoff.

The last-contact killing in the induced return operator is explicitly
distinguished from ordinary termination, and periodic states remain
outside the ordinary harmonic escape argument. No substantive correction
was identified in the requested scope.
