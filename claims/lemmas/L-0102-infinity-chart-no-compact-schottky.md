# L-0102 — Infinity-chart supercritical maps preserve no compact positive interval

Claim ID: `L-0102`  
Title: In the chart \(t=1/x\), supercritical forward blocks still preserve no compact subinterval of \((0,\infty)\)  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `L-0101`  
Scope: real Möbius charts for supercritical affine Collatz blocks  
Related counterexample candidates: none (obstruction)

## Statement

Let \(f(x)=\mu x+\beta\) with \(\mu>1\) and \(\beta>0\). In the chart \(t=1/x\),

\[
h(t)=\frac{t}{\mu+\beta t}\qquad(t>0).
\]

Then \(0<h(t)<t/\mu<t\) for every \(t>0\). Consequently no compact interval
\([a,b]\subset(0,\infty)\) satisfies \(h([a,b])\subseteq[a,b]\).

Moreover, for every \(\varepsilon>0\),

\[
h((0,\varepsilon])=(0,h(\varepsilon)],
\]

so the images of any common 0-neighborhood under a family of such maps are
nested intervals based at \(0\) and cannot form a pairwise disjoint compact
IFS ping-pong cover of that neighborhood.

## Proof

\[
h(t)-t=\frac{t-\,t(\mu+\beta t)}{\mu+\beta t}
=\frac{t\bigl(1-\mu-\beta t\bigr)}{\mu+\beta t}<0
\]

because \(\mu>1\) and \(t,\beta>0\). Also \(h(t)=t/(\mu+\beta t)<t/\mu\).

If \(h([a,b])\subseteq[a,b]\) with \(0<a\le b<\infty\), then \(h(a)\ge a\),
contradiction.

The identity \(h((0,\varepsilon])=(0,h(\varepsilon)]\) follows because \(h\) is
continuous and strictly increasing on \([0,\infty)\) with \(h(0)=0\).

## Motivation

Blocks the second naive geometric domain after `L-0101` killed positive-ray
inverse IFS certificates.

## Dependency audit

- Change of chart: elementary.
- Parameters \(\mu,\beta\) from `D-0101`.

## Gap audit

- Does not forbid ping-pong on domains that are unions of intervals not
  preserved by each generator individually but swapped among generators in a
  more elaborate pattern (true free-group ping-pong with \(g_i(X\setminus D_i)\subset D_i\)).
- Does not forbid integer/modular certificates.

## Adversarial tests

`X-0104`: 0/350 unexpected self-preservations; 0 annulus pair hits on mild maps
up to length 12.

## Remaining uncertainty

The classical free-group ping-pong with complementary domains
\(X\setminus D_i\) is not fully excluded — only the compact IFS-into-itself
format.

## Suggested next attack

Either (i) implement complementary-domain Möbius ping-pong on \(\mathbb{RP}^1\),
or (ii) abandon real IFS certificates and commit to modular/Syracuse automata.
