# T-0101 — Precision accounting for accelerated Collatz schedules

Claim ID: `T-0101`  
Title: Unified 2-adic precision accounting for arbitrary finite block schedules  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `L-0105`, `L-0106`, `L-0107`  
Scope: all finite sequences of chronological parity blocks; ordinary and 2-adic realizations  
Related counterexample candidates: none (meta-obstruction / accounting theorem)

## Statement

### Setup

Let \(w_1,\ldots,w_m\) be chronological parity words of lengths \(L_i\) and
odd-weights \(a_i\), with affine maps

\[
f_i(x)=\mu_i x+\beta_i,
\qquad
\mu_i=\frac{3^{a_i}}{2^{L_i}},
\qquad
\beta_i=\frac{B(w_i)}{2^{L_i}}.
\]

A **schedule** \(\sigma=(w_1,\ldots,w_m)\) acts on a parameter line
\(n=Mu+R\) by successively enabling each \(w_i\) (imposing
\(n\equiv r(w_i)\pmod{2^{L_i}}\) after transport) and applying \(f_i\).

Write \(\Lambda=\sum_i L_i\) and \(A=\sum_i a_i\). The composed affine map on
any fully enabled lift is

\[
F_\sigma(x)=\mu_\sigma x+\beta_\sigma,
\qquad
\mu_\sigma=\frac{3^A}{2^\Lambda}= \prod_i\mu_i.
\]

### A. Tax additivity (generic odd transport)

Starting from the universal line \(M=1\) and applying \(\sigma\) with each
intermediate image step odd before the next constraint (automatic after any
block of odd-weight \(\ge1\)), the total 2-adic tax on the free parameter is
exactly \(\Lambda\). Odd intermediate moduli never decrease the cumulative tax
below \(\Lambda\) (`L-0106`).

### B. Unique cylinder

The set of ordinary integers that follow \(\sigma\) for one full pass is a
single residue class modulo \(2^\Lambda\) (Terras coding of the concatenated
word \(W=w_1\cdots w_m\)). Equivalently, there is a unique cylinder
\(2^\Lambda\mathbb Z+r(W)\).

### C. Nested schedules and inverse limits

Let \(\sigma^{(1)},\sigma^{(2)},\ldots\) be a sequence of schedules with
concatenated lengths \(\Lambda_N\to\infty\), and suppose an element
\(x\in\mathbb Z_2\) realizes every prefix schedule \(\sigma^{(1)}\cdots\sigma^{(N)}\).
Then \(x\) lies in a nested sequence of cylinders of moduli \(2^{\Lambda_N}\),
hence is uniquely determined as a 2-adic integer.

### D. Expanding periodic case

If some schedule \(\sigma\) is supercritical (\(\mu_\sigma>1\)) and an element
of \(\mathbb Z_2\) realizes \(\sigma^\omega\), then necessarily

\[
x=\mathrm{fp}(F_\sigma)=-\frac{\beta_\sigma}{\mu_\sigma-1}<0
\]

in \(\mathbb Q\) (`L-0107` generalized to arbitrary concatenations). In
particular \(x\notin\mathbb Z_{>0}\).

### E. Finite prepaid state bound

If a certificate format stores only finitely many 2-adic bits of state
(modulus \(2^A\) with \(A\) fixed) and enables blocks only through that state,
then it cannot impose an unbounded independent tax tower. Any infinite accepted
run’s dyadic constraints are among the finitely many cylinders of depth
\(\le A\). Combined with forward determinism on \(\mathbb Z/2^A\mathbb Z\)
(`L-0108`), branching certificates require either growing \(A\), odd-side
state with new mechanisms, or a non-forward format.

## Motivation

Unifies `L-0105`–`L-0108` into a single accounting theorem usable by other
packets (collision fibers, rewrite grammars, automata) without rediscovering
precision drain case-by-case.

## Proof

**A.** Induct on \(m\). The \(m=1\) case is the tax formula of `L-0106` with
odd modulus \(1\). After a block of odd-weight \(a\ge1\), the image step is
odd (`L-0106` transport), so the next tax equals the next length. Summing
gives \(\Lambda\).

**B.** Concatenation \(W=w_1\cdots w_m\) is a single chronological word of
length \(\Lambda\). By the residue↔word bijection (`L-0108`(1)), followers of
\(W\) are exactly one class mod \(2^\Lambda\).

**C.** Compatibility of nested cylinders of increasing 2-power modulus yields
a unique element of \(\mathbb Z_2\) (standard inverse-limit description of
\(\mathbb Z_2\)).

**D.** On the cylinder of \(W\), the accelerated map equals \(F_\sigma\). An
infinite periodic itinerary \(W^\omega\) forces
\(F_\sigma^{\circ k}(x)\) to remain in that cylinder for all \(k\), hence \(x\)
equals the unique fixed point of \(F_\sigma\) in the cylinder’s 2-adic
closure. Supercriticality and \(\beta_\sigma>0\) (which holds whenever \(A\ge1\)
for the standard \(B\)-encoding) give \(\mathrm{fp}<0\).

**E.** A state in \(\mathbb Z/2^A\mathbb Z\) distinguishes at most \(2^A\)
cylinders of depth \(A\). Enabling a block of length \(L\le A\) uses only
already-stored bits (`D-0103`). An infinite run therefore never creates a
constraint of depth \(>A\) beyond what the deterministic residue orbit already
encodes. Forward out-degree one on that residue graph is `L-0108`.

## Dependency audit

- `D-0101`, `L-0105`, `L-0106`, `L-0107`, `L-0108`.
- Terras coding / residue↔word bijection.

## Gap audit

- Partial pre-alignment when intermediate moduli are even can make some step
  taxes \(<L_i\); clause A’s “exactly \(\Lambda\)” is the generic odd-transport
  case. The inequality \(\mathrm{tax}\le\Lambda\) always holds, with equality
  generically.
- Clause D assumes \(\beta_\sigma>0\); true for standard positive \(B\) with
  \(A\ge1\).
- Does not by itself rule out aperiodic 2-adic points that happen to lie in
  \(\mathbb Z_{>0}\) — only the expanding periodic subclass, plus the
  accounting constraints on how certificates may try to construct them.

## Adversarial tests

- `X-0110`: tax tables for many schedules; drain pair tax \(=14k\).
- `X-0114`: random schedule census confirming cylinder uniqueness and
  negative fixed points for supercritical concatenations.
- Specializations: `L-0104`, `L-0105`, `L-0107`.

## Remaining uncertainty

Low for A–D in the generic/standard-encoding setting. Clause E is structural
and should be read as a constraint on certificate formats, not a Collatz
resolution.

## Suggested next attack

Specialize to digit-transfer charts (`T-0102`) and morphic schedules (`L-0110`).
