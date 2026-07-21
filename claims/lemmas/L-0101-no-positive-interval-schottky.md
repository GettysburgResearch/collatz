# L-0101 — Supercritical inverses never preserve a positive interval

Claim ID: `L-0101`  
Title: No supercritical Collatz inverse branch maps a positive interval into itself  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: real inverse branches of supercritical parity words with \(B(w)>0\)  
Related counterexample candidates: none (obstruction)

## Statement

Let \(w\) be a chronological parity word with \(a(w)\ge 1\), \(B(w)>0\), and
forward slope \(\mu=3^{a(w)}/2^{|w|}>1\). Write

\[
g(y)=\frac{y-\beta}{\mu},
\qquad
\beta=\frac{B(w)}{2^{|w|}}>0.
\]

Then for every real \(A>0\),

\[
g(A)<A.
\]

Consequently there does **not** exist a nonempty interval
\(I\subseteq(0,\infty)\) with \(g(I)\subseteq I\).

In particular, no finite set of supercritical inverse branches can form a
real Schottky system on a positive interval in the sense of `D-0102`
(hypotheses (1)–(3) on \(I\subset(0,\infty)\)).

## Definitions

As in `D-0101`. The hypothesis \(B(w)>0\) holds for every word containing at
least one odd step in the standard encoding.

## Motivation

This kills the most naive geometric certificate suggested by classical IFS
ping-pong on the positive ray, and forces the packet to change domains
(chart at infinity, mixed sub/supercritical generators, or integer ports with
general moduli).

## Proof

Compute

\[
g(A)-A=\frac{A-\beta}{\mu}-A
=A\Bigl(\frac1\mu-1\Bigr)-\frac\beta\mu.
\]

Since \(\mu>1\), one has \(1/\mu-1<0\). Since \(A>0\) and \(\beta>0\),

\[
A\Bigl(\frac1\mu-1\Bigr)<0
\quad\text{and}\quad
-\frac\beta\mu<0,
\]

hence \(g(A)-A<0\).

If \(I\subseteq(0,\infty)\) were nonempty and \(g(I)\subseteq I\), take any
\(A\in I\). Then \(g(A)\in I\subseteq(0,\infty)\), but also \(g(A)<A\).
Iterating gives a strictly decreasing positive sequence \(g^{\circ n}(A)\) in
\(I\). That alone is not yet a contradiction. The interval-preservation
failure is sharper: let \(A=\inf I\) if \(I\) is closed and bounded below by a
positive number; more elementarily, for a closed interval \(I=[A,B]\) with
\(0<A\le B<\infty\), interval preservation requires \(g(A)\ge A\), contradicting
\(g(A)<A\). For a general nonempty \(I\subseteq(0,\infty)\) with
\(g(I)\subseteq I\), pick \(A\in I\) and note \(g(A)\in I\) and \(g(A)<A\); this
does not forbid unbounded \(I\) such as \((0,B]\). 

**Refined statement used by the packet:** no compact interval
\(I=[A,B]\subset(0,\infty)\) satisfies \(g(I)\subseteq I\).

Proof: \(g([A,B])=[g(A),g(B)]\) with \(g(A)<A\), so \(g(A)\notin[A,B]\).

Open rays \((0,B]\) and half-lines \([A,\infty)\) are likewise impossible:
\([A,\infty)\) fails by \(g(A)<A\); \((0,B]\) fails because
\(g(B)<B\) is fine but \(g(y)\to -\beta/\mu<0\) is irrelevant — actually
\(g((0,B])=(g(0^+),g(B)]\) with \(g(0^+)=-\beta/\mu<0\), which exits
\((0,\infty)\). Explicitly \(g(\beta/2)=(\beta/2-\beta)/\mu<0\).

Thus no nonempty interval of \((0,\infty)\) that is a closed bounded segment,
closed half-line, or open initial segment \((0,B]\) is preserved. This covers
every interval shape used in `D-0102` and `X-0102`.

## Dependency audit

- Affine inverse formula: `D-0101`.
- No external lemmas.

## Gap audit

- Words with \(B(w)=0\) (the all-even word) are excluded; they are not
  supercritical with \(a\ge 1\).
- Critical words \(\mu=1\) are excluded.
- The lemma does not forbid Schottky systems after a coordinate change
  (e.g. \(t=1/x\)), nor systems mixing subcritical and supercritical
  branches, nor integer certificates.

## Adversarial tests

`X-0102` checked \(g(A)<A\) on 400 supercritical samples with zero
counterexamples, and found zero interval hits up to length 12.

## Remaining uncertainty

None for the compact-interval statement. The open-set wording in the first
paragraph is sharpened in the refined statement; reviewers should use the
refined statement as the official claim.

## Suggested next attack

Move Schottky search to (i) the chart at infinity \(t=1/x\), (ii)
general-modulus integer ports, (iii) mixed sub/supercritical generator sets.
