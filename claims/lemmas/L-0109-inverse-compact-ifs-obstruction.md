# L-0109 — Compact positive inverse IFS with \(\{g_0,g_1\}\) is impossible

Claim ID: `L-0109`  
Title: Inverse branches \(g_0(x)=2x\) and \(g_1(x)=(2x-1)/3\) admit no compact positive IFS attractor  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: real inverse IFS for the two elementary inverse branches of \(T\)  
Related counterexample candidates: none (obstruction)

## Statement

Let

\[
g_0(x)=2x,
\qquad
g_1(x)=\frac{2x-1}{3}.
\]

1. There is no nonempty compact interval \(I\subset(0,\infty)\) with
   \(g_0(I)\subseteq I\). Indeed \(g_0([a,b])=[2a,2b]\) properly escapes any
   bounded interval.

2. The unique fixed point of \(g_1\) is \(x=-1\). Any IFS using only iterates
   of \(g_1\) has attractor \(\{-1\}\) (on the reals / 2-adics in the natural
   sense), not a positive integer.

3. Therefore there is no compact positive real Schottky / IFS certificate
   built from the elementary inverse pair \(\{g_0,g_1\}\).

## Proof

(1) If \(0<a\le b<\infty\) and \(g_0(I)\subseteq I\) for \(I=[a,b]\), then
\(2b\le b\), hence \(b\le0\), contradiction.

(2) Solve \(x=(2x-1)/3\) to get \(x=-1\). The map \(g_1\) is affine with slope
\(2/3\in(0,1)\), hence globally contracting on \(\mathbb R\) toward \(-1\).

(3) Combines (1)–(2): any IFS that includes \(g_0\) cannot live on a compact
positive interval, and any IFS that excludes \(g_0\) collapses to \(-1\).

## Motivation

Closes the elementary inverse reformulation of ping-pong left open after
`L-0108` killed forward branching.

## Gap audit

- Accelerated inverse branches (inverses of long words) are the same objects
  as \(g_w\) in `L-0101`, already obstructed on compact positives.
- Unbounded domains / cones / multi-dimensional state remain open but are no
  longer “classical Schottky”.

## Adversarial tests

`X-0113`.

## Suggested next attack

Either abandon classical Schottky geometry for this packet, or import a
genuinely new state (e.g. collision-fiber digits + boundary) from the other
program under a bridge issue.
