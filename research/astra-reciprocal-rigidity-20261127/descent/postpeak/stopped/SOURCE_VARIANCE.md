# A finite-source variance criterion beyond the binary coding horizon

For the shortcut map \(T\), write \(F_t(y)\) for the number of odd departures among the first \(t\) steps from \(y\). For each positive integer \(X\), set
\[
 L_X=\left\lceil(\log_2(2X))^2\right\rceil,\qquad
 Z_X(y)=F_{L_X}(y)/L_X,\qquad
 V_X=\operatorname{Var}_{1\le y\le X} Z_X(y)
\]
under the uniform measure on the displayed finite set. Using the two source-qualified inputs below, universal positive-integer convergence is equivalent to
\[
                              \liminf_{X\to\infty}V_X=0.              \tag{1}
\]
Under convergence \(V_X\to0\); if there is a counterexample, \(\liminf V_X>0\). The same implications hold for any deterministic integer clock \(L_X/\log X\to\infty\). The result is a written reduction. There is no proof or numerical evidence here that (1) holds.

## Source-qualified inputs

- Mazur's July 2026 arbitrary-threshold theorem gives an absolute \(C\) such that, for **every** \(b(n)\to\infty\), a natural-density-one set of positive starts visits a positive integer below \(b(n)\) within \(C\log n\) ordinary, unaccelerated steps. The fixed threshold \(1\) is not allowed by this statement. The repository has an earlier structural audit and source pins at public revision `ca3dd0d63920411213403092aecc6946619eb082`. [Repository digest](../../../../external/mazur-2026/natural-density-log-time.md) · [Primary theorem](https://www.proofatlas.ai/formalizations/natural-density-log-time-collatz/)
- Mazur's September positive-predecessor theorem gives ordinary predecessor density bounded below by a positive target-dependent constant for every fixed positive target prime to three. Its explicit corollary says that existence of a counterexample forces positive lower natural density of nonconvergent positive starts. [Primary theorem](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

Mazur separately proves a fixed positive fraction reaches \(1\) in the sharper \((523/50)\log n\) raw clock. The argument below uses its two listed inputs and derives its own slower log-time statement. These external results were not rebuilt for this reduction. [Sharper positive-density clock](https://www.proofatlas.ai/formalizations/positive-density-log-time-collatz/)

## Log-time arrivals within any fixed target basin

Fix a positive integer \(a\), and write \(P(a)\) for the starts that ever visit it under the raw map. For each \(r\), let \(D_a(r)\) be the maximum first raw visit time over \(m\le r\) in \(P(a)\), taking zero for an empty collection. It is finite for every fixed \(r\), without assuming universal convergence or effective basin membership. For sufficiently large \(n\) let \(b_a(n)\) be the largest \(r\le n\) with \(D_a(r)\le\sqrt{\log(n+2)}\); assign the value one if the defining set is initially empty. Then \(b_a(n)\to\infty\), since each fixed \(D_a(r)\) is finite.

The July theorem supplies a density-one set of sources reaching some \(m<b_a(n)\) within \(C\log n\) raw steps. For such an \(n\in P(a)\), either its first visit to \(a\) has already occurred, or the reached \(m\) itself belongs to \(P(a)\) and has remaining first-visit time at most \(D_a(b_a(n))\). Therefore
\[
 \#\{n\le X:n\in P(a),\ \text{first raw visit to }a>C\log n+\sqrt{\log(n+2)}\}
                  =o(X).
\]
The constant \(C\) is the July absolute clock, while the exceptional set may depend on the fixed target. In particular a target with positive lower predecessor density has a positive lower fraction of logarithmic-time arrivals, and the proportion missed *inside its basin* tends to zero. For odd \(a\), a raw visit also supplies a shortcut visit no later, since shortcutting removes only even intermediate states. Thus for each fixed odd target, off \(o(X)\) actual starts in its raw basin, \(F_{L_X}(n)/L_X\) differs from \(F_{L_X}(a)/L_X\) by \(O(\log X/L_X)\): shifting a binary count window by its first arrival clock changes at most that many odds. We only need \(a=1\) for the variance comparison.

## A counterexample forces two separated populations

A nonconvergent positive orbit never encounters \(1\) or \(2\). More precisely, if \(a\) is the least positive member of its entire eventual-meeting component, all its states stay at least \(a\ge3\). For any member \(y\le X\) and \(t\ge1\), multiplying the shortcut ratios gives
\[
 a\le T^t(y)\le X\,2^{-t}(3+1/a)^{F_t(y)},\qquad
 \frac{F_t(y)}t\ge\frac{1-\log_2(X/a)/t}{\log_2(3+1/a)} .
\]
The bound with floor \(3\) alone applies uniformly to all nonconvergent positive starts. At \(t=L_X\) their odd fraction is at least \(p_0-o(1)\), where \(p_0=1/\log_2(10/3)>1/2\). If any counterexample exists, the positive-predecessor theorem puts at least \(\delta X\) such starts below every sufficiently large \(X\), for some \(\delta>0\).

Independently, the predecessor bound for target \(1\) and the log-time basin lemma together supply at least \(cX\) starts for some fixed \(c>0\), each hitting the shortcut cycle \(1,2\) by \(O(\log X)\). Their subsequent odds alternate; hence \(Z_X(y)=1/2+O(\log X/L_X)\) on this entire population. For large \(X\) the two groups are separated by at least \((p_0-1/2)/2\) in \(Z_X\).

For independent uniform \(y,y'\le X\), \(2V_X=\mathbb E[(Z_X(y)-Z_X(y'))^2]\). Keeping the two cross-group orders yields \(V_X\ge c'\delta((p_0-1/2)/2)^2>0\) for large \(X\), with \(c'>0\) independent of \(X\). This proves the counterexample implication. For a fixed canonical pair with convergent lower member, the same product bound gives a source-wise dichotomy: if its upper member converges too then the signed odd-count gap stays bounded once both tails alternate; otherwise its lower asymptotic gap per step is at least \(p_0-1/2\). The variance test uses separated populations of starts and does not assume adjacent positive boundary pairs have positive density.

## Convergence implies collapse at the specified clock

If every positive integer reaches \(1\), the log-time basin lemma applies to all starts except \(o(X)\) up to \(X\), with target \(a=1\). On those starts \(Z_X=1/2+o(1)\) uniformly. Since \(0\le Z_X\le1\), the empirical second moment about \(1/2\) tends to zero, and so does \(V_X\).

The clock separation matters. At cutoffs \(X=2^m\), any \(t\le m\) sees all \(t\)-letter parity words equally often, because they are exactly the dyadic classes modulo \(2^t\). Consequently \(\operatorname{Var}_{y\le2^m}(F_t(y)/t)=1/(4t)\) there without any information on complete ordinary orbits. That calculation does not extend to the explicit superlogarithmic deadline in (1).
