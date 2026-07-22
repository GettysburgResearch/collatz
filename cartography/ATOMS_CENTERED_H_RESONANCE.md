# Atomic centered, H, and resonance problems

## 4. Centered \(64\to81\) / M1 atoms

### ACL-P020 — Exact centered M1 witness

**Statement.** Find \(\xi>0\) such that

\[
\left\|\xi(81/64)^n\right\|\le \frac1{81}
\quad\text{for every }n\ge0,
\]

and such that the nearest-integer reconstruction in PR #16 yields a nontrivial positive initial state \(A_0\ge2\) and exact integral chart states at every time.

**Full-conjecture implication.** The reconstructed \(64\to81\) chart orbit is positive and expanding forever, giving a Collatz counterexample through the exact embedding.

**Certificate.** A finite rule for \(\xi\) or its integer states plus an all-\(n\) proof; decimal or finite-prefix evidence is not enough.

---

### ACL-P021 — Eventual-zero appended-block itinerary

**Statement.** Give an explicit infinite binary itinerary \(e=(e_n)\), an index \(K_0\), and an ordinary \(A_0\ge2\) such that the native base-64 appended cylinder blocks \(q_K(e)\) satisfy

\[
q_K(e)=0\qquad(K\ge K_0),
\]

and the corresponding physical chart transitions replay exactly.

**Implication.** Equivalent operational form of `ACL-P020`.

**Known exclusions.** The itinerary cannot be eventually periodic of period at most nine, Thue–Morse or its covered encodings, low-complexity, or a small bounded-state output.

---

### ACL-N022 — All-itinerary native nonstabilization

**Statement.** Prove that for every nontrivial admissible \(64\to81\) itinerary, the native appended block \(q_K\) is nonzero for infinitely many \(K\).

**Implication.** The M1 survivor attractor has no nontrivial ordinary positive point; closes this direct counterexample lane.

**Required discipline.** Use the native \(64/81\) recurrence or another independently audited representation. Do not use the quarantined identity \(81/64=(3/2)^4\).

---

### ACL-N023 — Radius-\(1/81\) equality-language classification

**Statement.** Classify every \(\xi>0\) satisfying

\[
\limsup_n\left\|\xi(81/64)^n\right\|\le \frac1{81}
\]

at the exact endpoint. Prove that each endpoint itinerary belongs to a recurrence class already excluded by the native recurrence-cone theorem, or identify an explicit exceptional class.

**Implication.** If no exceptional ordinary class remains, this proves `ACL-N022`. If an explicit class remains, it becomes the sole M1 construction target.

**Why atomic.** Strict lower bounds below the endpoint are insufficient; the equality language is the whole issue.

---

### ACL-N024 — Period-ten special-vector irrationality

**Statement.** For each positive minimal period-ten word, prove irrationality in \(\mathbb Q_2\) of its prescribed ten-phase stack value—not full ten-dimensional independence—by either:

1. a coupled two-dimensional \(q\)-difference/Hermite–Padé construction; or
2. a quadratic reduced-height/common-content bound for the normalized combined-moment Cramer minors.

**Implication.** Closes fixed period ten and sharpens the nonstationary frontier. It does not by itself settle M1.

**Known no-gos.** Scalar unequal allocation, sparse scalar orders, naive adjacent-order combinations, and the visible Vandermonde factor do not supply enough gain.

---

### ACL-N025 — Period-uniform S-adic passage

**Statement.** Prove a value-theoretic or recurrence theorem uniform in the period/directive complexity that excludes every admissible balanced nonperiodic \(17/18\) S-adic stack from having an ordinary integral completion.

**Implication.** Combined with finite-period results, closes the remaining symbolic stack formats.

**Required feature.** Constants must remain effective as the directive's local period or substitution depth grows.

## 5. H-subsystem atoms

### ACL-P030 — Positive infinite H survivor

**Statement.** Exhibit \(n_0\in\mathbb Z_{>0}\) such that every iterate of the partial H map is defined and positive, and prove this for all times.

**Full-conjecture implication.** The established embedding \(N=8n+1\) yields a positive nonconvergent shortcut-Collatz orbit.

**Certificate.** A recurrence or invariant proving branch admissibility, integrality, and positivity forever.

---

### ACL-P031 — Stabilized H cylinder itinerary

**Statement.** Find an infinite H itinerary whose least positive cylinder representatives \(\nu_K\) are eventually constant at some \(n_0>0\), and prove that the stabilized integer realizes the itinerary exactly.

**Implication.** Produces `ACL-P030`.

**Known no-gos.** The `10/30` nested architecture, finite robustly descending suffix families, and raw `{30,60,70}` return do not work.

---

### ACL-N032 — Integral subcritical H finite trap

**Statement.** In the remaining subcritical renewal regime, construct an integer-valued height \(Z\) with a finite set \(F\subset\mathbb Z\) such that every hypothetical positive infinite H orbit eventually enters \(F\), while every state in \(F\) has no admissible positive integral successor.

**Implication.** Proves no positive infinite H orbit exists.

**Inputs.** The exact renewal sign law, future-core demand identity, completion-height bounds, and repaired ghost-boundary audit.

---

### ACL-N033 — Quantitative fresh-prime pressure

**Statement.** Strengthen the qualitative H fresh-prime dichotomy to show that any nonperiodic infinite exact H chain accumulates enough discounted new-prime logarithmic mass to violate the critical budget, or else repeats the complete central state and becomes periodic.

**Implication.** Closes the nonperiodic H alternative when combined with the existing periodic/finite-return exclusions.

**Acceptable bridge.** An effective \(S\)-unit/order bound, a plateau theorem, or a residue-capacity inequality with the correct discount.

## 6. Conditioned \(3\)-adic resonance atoms

### ACL-P040 — Coherent rare-event resonance with integer stabilization

**Statement.** Construct valuation prefixes \(a_0,a_1,\dots\) and affine states

\[
A_{j+1}=A_j+a_j,\qquad C_{j+1}=3C_j+2^{A_j}
\]

such that:

1. the necessary residues
   \[
   x\equiv-3^{-n}C_n\pmod{2^{A_n}}
   \]
   are nested;
2. their least positive representatives eventually stabilize to \(x>0\);
3. every prescribed valuation is exact;
4. the odd-step density forces an orbit avoiding \(1\).

**Full-conjecture implication.** The stabilized \(x\) is a counterexample.

**Not sufficient.** Persistent conditioned Fourier modes or a nonstabilizing \(2\)-adic limit.

---

### ACL-N041 — Uniform decay for a frozen resonance class

**Statement.** Freeze a finite-state conditioned transfer operator and prove a uniform spectral gap as depth and modulus increase in a specified regime, including exact dependence of constants.

**Implication.** Refutes that resonance class only; it does not prove Collatz.

**Use.** Prevents repeated numerical exploration of a mechanism already ruled out.
