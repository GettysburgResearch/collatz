# L-0107 — Expanding periodic block schedules realize only their negative rational fixed point

Claim ID: `L-0107`  
Title: The unique 2-adic realization of a supercritical periodic block schedule is the negative rational fixed point  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `L-0103`, `L-0105`  
Scope: eventually periodic concatenations of a finite supercritical word  
Related counterexample candidates: none (obstruction)

## Statement

Let \(w\) be a chronological parity word of length \(L\), odd-weight \(a\), with
supercritical slope \(\mu=3^a/2^L>1\) and affine map

\[
f(x)=\mu x+\beta,
\qquad
\beta=\frac{B(w)}{2^L}>0.
\]

Let \(r=r(w)\) be its native residue. Suppose an element
\(x\in\mathbb Z_2\) (2-adic integers) follows the infinite parity itinerary
\(w^\omega\). Then necessarily

\[
x=\mathrm{fp}(w)=-\frac{\beta}{\mu-1}=-\frac{B(w)}{3^a-2^L}<0
\]

in \(\mathbb Q\subset\mathbb Z_2\). In particular \(x\notin\mathbb Z_{>0}\).

Consequently no ordinary positive integer has shortcut-parity itinerary
\(w^\omega\) for a supercritical word \(w\).

The same conclusion holds for an eventually periodic schedule whose cyclic
block \(W=w_1\cdots w_m\) is supercritical as a concatenation
(\(3^{a(W)}>2^{|W|}\)): the unique 2-adic realization is the negative rational
fixed point of the composed affine map.

## Definitions

Itinerary \(w^\omega\) means that for every \(k\ge0\), after \(kL\) shortcut
steps the current value lies in the native residue class of \(w\) and follows
\(w\) for the next \(L\) steps.

## Motivation

Kills expanding self-loops / periodic Schottky cycles as positive counterexample
certificates, even though the real affine map sends positives to \(+\infty\).
The residue tower selects the negative fixed point, not the diverging ray.

## Proof

If \(x\) follows \(w\) once then \(T^L(x)=f(x)\) in the 2-adic sense on the
cylinder of \(w\), and \(x\equiv r\pmod{2^L}\). Iterating the itinerary gives

\[
x\equiv r\pmod{2^L},
\qquad
f(x)\equiv r\pmod{2^L},
\qquad
f^{\circ2}(x)\equiv r\pmod{2^L},
\qquad\ldots
\]

and \(T^{kL}(x)=f^{\circ k}(x)\). Because \(f\) is affine with coefficients in
\(\mathbb Z[1/2]\) and \(\mu=3^a/2^L\), on the cylinder one has the exact
identity \(f(x)=(3^a x+B(w))/2^L\). The unique fixed point of \(f\) in
\(\mathbb Q_2\) is \(\mathrm{fp}(w)\).

Now suppose \(x\in\mathbb Z_2\) satisfies \(f^{\circ k}(x)\equiv r\pmod{2^L}\) for
all \(k\) and follows \(w\) each time. Then \(x\) lies in the nested cylinders
defining the infinite itinerary \(w^\omega\). That itinerary’s coding map is
the standard Terras / 2-adic conjugacy sending the sequence \(w^\omega\) to the
periodic point \(\mathrm{fp}(w)\). Equivalently: the inverse branch
\(g=f^{-1}\) is a 2-adic contraction toward \(\mathrm{fp}(w)\) on a
neighborhood of that point, and the nested cylinder intersection is exactly
\(\{\mathrm{fp}(w)\}\).

Since \(\mu>1\) and \(\beta>0\), \(\mathrm{fp}(w)<0\), hence not a positive
integer.

For a concatenated supercritical block \(W\), apply the same argument to \(W\)
in place of \(w\).

## Dependency audit

- Affine blocks: `D-0101`.
- Periodic schedules: `L-0103`.
- Nested cylinders / unique solution: same arithmetic as `L-0105`.
- Sign of fixed point: supercritical \(+\beta>0\).

## Gap audit

- Uses the standard identification of infinite parity sequences with 2-adic
  points via inverse branches; this is classical but should be spelled with
  the same chronological conventions as `D-0101`. An auditor may demand a fully
  elementary nested-congruence writeup without naming Terras.
- Subcritical periodic words are outside scope (they give positive rational
  cycles — the algebraic cycle hunt).
- Aperiodic itineraries are not covered.

## Adversarial tests

- Word `1`: \(\mathrm{fp}=-1\), itinerary of the negative cycle.
- Word `11`: \(\mu=9/4\), \(\mathrm{fp}=-1/5\)? Compute:
  \(B(11)=1\cdot3+2\cdot1=5\), \(\mathrm{fp}=-5/(9-4)=-1\).
- `X-0110` / `L-0104` pair concatenations: maximal finite periods on ordinary
  seeds; fixed points of concatenations are negative rationals.

## Remaining uncertainty

Low for single supercritical words. The elementary (Terras-free) writeup of
the nested cylinder intersection can be expanded on request.

## Suggested next attack

Extend to eventually periodic schedules with a supercritical cyclic part, then
attack aperiodic finite CRT automata (`D-0103`, `X-0111`).
