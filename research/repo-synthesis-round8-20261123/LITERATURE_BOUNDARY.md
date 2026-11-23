# Discounted potentials: a useful idea with a necessary arithmetic gate

23 November 2026. The following primary sources were inspected in this
round. No priority claim is made for discounted gap observables or for
recasting dynamics as arithmetic of a scalar. No claimed Collatz proof
is imported.

## R8-L1: an exact failure of an overlapping uniform-descent claim

Sebastian Schepis's author-hosted preprint, dated 3 September 2025,
*The Collatz Conjecture via a State-Only, Well-Founded Lyapunov Function
in a Prime-Resonant Framework*, defines a discounted valuation sum and
claims strict descent of a logarithmic potential. Its hosting page uses
the title *The Collatz Conjecture Proven via Entropy Collapse in
Prime-Resonant Hilbert Space*.

[Primary source](https://www.academia.edu/143743604/The_Collatz_Conjecture_Proven_via_Entropy_Collapse_in_Prime_Resonant_Hilbert_Space),
section 3, the stated uniform strict descent lemma. The parameters are
`alpha=1/4`, `B=7/10`,

\[
S(q)=\sum_{k\ge0}4^{-k}g(U^kq),\qquad
L(q)=\log q-\frac7{10}S(q).
\]

**Verdict for that lemma: REFUTED.** This is checked on one actual
ordinary transition, including its complete eventual standard tail:

\[
7\longmapsto11\longmapsto17\longmapsto13\longmapsto5\longmapsto1,
\qquad (g_0,\ldots,g_4)=(1,1,2,3,4).
\]

At one, every subsequent gap is two. Exact geometric summation gives

\[
S(7)=\frac{553}{384},\qquad S(11)=\frac{169}{96},
\qquad S(11)-S(7)=\frac{41}{128}.
\]

Consequently

\[
\boxed{L(11)-L(7)=\log(11/7)-\frac{287}{1280}>0.}
\]

This sign requires no floating-point logarithm: for x>1,
`log(x)>=1-1/x`, and `4/11>287/1280` by exact integer comparison.
The correct one-step identity for general parameters is

\[
\Delta L=\log(3+1/q)+(B/\alpha-\log2)g
-B(1/\alpha-1)S(q).
\]

The lower estimate `S>=g` does not yield the preprint's claimed negative
constant. `scalar_controls.py` independently checks the orbit, the
two exact sums, and the positive rational lower bound.

The useful overlap is the discounted future valuation observable. Our
R8-G2 argument contracts only **after the actual triadic scalar's
denominator has cleared**, when its integer value is at least one.
That gate is explicitly unproved for an arbitrary initial source. The
preprint's universal descent claim is not a dependency.

## A distinct earlier rationality programme

Kenneth G. Monks and Jonathan Yazinski, *The Autoconjugacy of the
3x+1 Function*, author PDF dated 10 July 2002,
[Theorem 2.1](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
connect the arithmetic of the complementary 2-adic autoconjugacy with
the absence of divergent positive-integer trajectories. The paper also
keeps the separate nontrivial-cycle question explicit.

That is a useful conceptual precedent for arithmetic targets. The
observable here is the **real derivative `2B'_q(1)`**, with an odd-step
recurrence multiplying by three. We have not identified it with their
2-adic autoconjugacy, and their theorem supplies neither its triadic
rationality nor the actual full-germ hypotheses from PR177. The
denominator-clearing proof in this packet is elementary and independent
of that imported rationality implication.
