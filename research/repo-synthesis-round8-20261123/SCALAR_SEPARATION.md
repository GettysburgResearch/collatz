# A quantitative separation from incorrect triadic candidates

23 November 2026. **PROPOSED written corollary**, independently reviewed
at the blob pins in the accompanying report. This uses R8-G1--R8-G4 in
[GERM_BRIDGE.md](GERM_BRIDGE.md), with exactly the same actual ordinary
map and scalar. It does not supply a successful candidate for every source.

## R8-S1: a finite precision threshold

Let q be a positive odd integer, let a be any integer, and let r be a
nonnegative integer. Put

\[
c=a/3^r,\qquad K=4r+3\operatorname{bl}(q),\qquad
\varepsilon=3^{-(K+1)}.
\]

Then the actual, unconditionally defined real scalar satisfies the
dichotomy

\[
\boxed{h(q)=c\quad\hbox{or}\quad |h(q)-c|\ge\varepsilon.}
\tag{1}
\]

This is a lower bound for the distance to an **incorrect** candidate
on this specified triadic grid. It is not an assertion that h is rational.

**Proof.** Run the total exact recognizer R8-G4 on c. At its decision
clock k, where `0<=k<=K`, write the propagated candidate as `t=N/d`,
where

\[
d=3^{\max(r-k,0)}.
\]

No reduction of the fraction is needed. Repeated use of the actual
scalar recurrence gives

\[
h(q_k)-t=3^k(h(q)-c).
\tag{2}
\]

If the recognizer accepts, finite backward substitution proves h(q)=c.
Otherwise there are three possible rejection mechanisms.

* At `q_k=1`, the candidate differs from one, so
  `|h(q_k)-t|=|d-N|/d>=1/d`.
* If `2t<1`, then `d-2N` is a positive integer. Since the actual
  scalar is strictly greater than one half,
  `|h(q_k)-t|>=(d-2N)/(2d)>=1/(2d)`.
* If `3t>bl(q_k)+3`, then `3N-(bl(q_k)+3)d` is a positive integer.
  The actual upper bound gives
  `|h(q_k)-t|>=1/(3d)`.

In every case the current discrepancy is at least `1/(3d)`. Divide
by `3^k` in (2) and use

\[
k+\max(r-k,0)=\max(r,k)\le K.
\]

This yields (1). The endpoint and lower-guard estimates are stronger
than the common constant retained in (1).

## What a real approximation would have to provide

Suppose an independently certified approximation gives
`|h(q)-x|<=delta`. If a supplied triadic candidate c satisfies

\[
\boxed{|x-c|+\delta<3^{-(4r+3\operatorname{bl}(q)+1)},}
\tag{3}
\]

then h(q)=c, and R8-G2 proves that q reaches one. Equivalently, an
interval containing both h(q) and c, with diameter strictly below the
right side of (3), certifies equality.

The rational interval construction in R8-G1 computes h to any requested
precision. That alone does not produce a c meeting (3). Ordinary
rounding to denominator `3^r` has an error of order `3^-r`, whereas
this sufficient threshold has order `3^-4r` with an additional source
factor. A universal supply of such unusually accurate candidates is
still an unproved global arithmetic assertion.

Thus the finite verifier has a concrete interface for a future analytic
or arithmetic construction: the source, denominator exponent, and
required precision are explicit. Increasing numerical precision on
arbitrary candidates is not itself a Collatz proof.

## Evidence boundary

`scalar_controls.py` replays supplied candidates on explicitly convergent
ordinary sources, checks the exact discrepancy transport and rejection
lattice margins, and checks (1) against independently computed rational
scalar values. These are bounded controls of the written proof. The
all-source separation statement is not claimed as a newly compiled Lean
theorem; its finite decision arithmetic depends on the precise Lean
core and written attachment described in R8-G1--R8-G4.
