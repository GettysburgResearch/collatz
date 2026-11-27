# The late loss of a small ordinary source occurs on the loop at one

**Status.** The finite first-failure and terminal-clock implications below are kernel-checked. The logarithmic asymptotics and the discussion of the decay rate are written deductions. The weighted number of entries into 1 during a prescribed old-source window remains open.

Use the original positive odd map \(U(m)=(3m+1)/2^{v_2(3m+1)}\). Write \(x_i=U^i(m)\), \(e_i=v_2(3x_i+1)\), and \(A_j=\sum_{i<j}e_i\). A word passes through \(n\) if \(4A_i\le7i\) for every \(i\le n\). Let \(F\) be its first failing date, when it exists. For positive odd \(m\) and \(n\ge1\), set
\[
                    3^{12n}m^{12}(2n+1)^2<2^{21n}.                     \tag{C}
\]
This exact integer comparison holds for all later dates once it holds at \(n\). The ratio on incrementing \(n\) is controlled by \((2n+3)^2\le3(2n+1)^2\) and \(3^{13}<2^{21}\). In physical-source terms, (C) covers every \(m<2^{(7/4-\log_2 3)n}/(2n+1)^{1/6}\).

## Exact classification

If (C) holds and \(F\ge n\), an actual departure from \(1\) occurs strictly before \(F\). Writing \(\tau\) for the first arrival at 1, one has
\[
             F+4A_\tau=8\tau+1,\qquad F\equiv1\pmod4.                  \tag{1}
\]
Every later date also fails. If \(m\) has passed through \(n\), for every \(h\ge n\)
\[
 \left[\exists j\in(n,h],\ 4A_j>7j\right]
          \quad\Longleftrightarrow\quad 4A_h>7h.                       \tag{2}
\]
The theorem allows the source to be nonprincipal. Applied to the actual principal population \(\mathcal M_n\), it identifies its entire contribution below (C)'s cutoff to the PR200 loss \(D_{n,2n}\). These sources can be tested just at \(2n\).

Equivalently, their loss is exactly the reciprocal mass of old passing sources reaching 1 with
\[
                         n\le 8\tau-4A_\tau<2n.                          \tag{3}
\]
Here membership can be checked by running through \(2n\) only. A first arrival before or at \(n\) can create a loss after \(n\), since the gate may retain surplus at entry. For example, the true odd source 27 first arrives at 1 at \(\tau=41\), has \(A_{41}=70\), and first fails at \(F=49\). Condition (C) already holds at \(n=40\). No pre-entry cutoff is applied at a terminal value less than three without retaining the factor \(x_j\) below.

## A sixth-power budget on every simple finite path

For \(j\) distinct departed odd integers at least 3,
\[
                 (2^{A_j}x_j)^6\le (3^j m)^6(2j+1).                    \tag{4}
\]
The terminal \(x_j\) can repeat an earlier state or equal 1. The exact product identity divides \(2^{A_j}x_j\) by \(3^jm\), giving \(\prod_{i<j}(1+1/(3x_i))\). Each factor satisfies
\[
 (1+1/(3x))^6\le x/(x-2)\quad(x\ge3).
\]
Writing \(x=u+3\), the difference \((3x)^6x-(3x+1)^6(x-2)\) is
\[
1701u^5+27405u^4+176715u^3+570087u^2+920087u+594323.
\]
Since \(x/(x-2)\) decreases, the product over any \(j\) distinct odd heights at least 3 is at most its value at \(3,5,\ldots,2j+1\), which telescopes to \(2j+1\). The Lean proof establishes the integer product inequality for an arbitrary finite set of odd heights and then applies the ordinary edge equations, with no division or unproved asymptotic assumption.

To apply (4) at a first failure before any departure from 1, suppose instead that two departure states repeat. The intervening nontrivial lap has length \(l>0\) and gap sum \(E\), with \(4E<7l\). Indeed every state on the lap is at least 3, so \(3(3x+1)\le10x\); multiplying around it yields \(3^l 2^E\le10^l\), and \(10^4<3^4 2^7\). Determinism makes the remaining suffix after both occurrences identical. Removing the lap keeps an earlier prefix from this *same* source and makes \(4A-7j\) strictly larger, contradicting first failure. Thus the departed states in question are distinct. A failure at \(j\ge n\) would then imply
\[
          2^{21j}\le (2^{A_j})^{12}
               \le 3^{12j}m^{12}(2j+1)^2,
\]
incompatible with (C). This argument includes a hypothetical nontrivial positive cycle. On the true loop at 1, \(A_t=A_\tau+2(t-\tau)\), giving (1) and (2).

For a source that never reaches one, let \(M_j=A_j-7j/4\). Its earliest global maximum exists: before any repeated departure, (4) bounds it by \(\log_2 m-(7/4-\log_2 3)j+\frac16\log_2(2j+1)\), which tends to \(-\infty\); after a repeat the negative lap excess decreases it on each repetition. If \(B=\log_2 m\), that maximum occurs by
\[
   \frac{B+\tfrac16\log_2(2+B)+O(1)}{7/4-\log_2 3}.
\]
Translation to this actual maximizing phase gives a permanently passing suffix. The leading coefficient is \(6.059\ldots\), compared with PR200's earlier kernel-checked \(80B\) cutoff. The same argument before first arrival applies to a terminating source, with a maximum over that finite initial segment.

## What exponential decay of the old mass would require

As a scope check, the stronger estimate \(\limsup J_n^{1/n}<1\) is equivalent to convergence of all positive inputs together with a uniform accelerated stopping bound \(\tau(m)=O(1+\log m)\). The ordinary vanishing criterion in PR201 gives convergence from exponential decay. If a terminating source passes through \(n\), then \(n\le4\tau\): when \(\tau\le n\) substitute the loop formula and \(A_\tau\ge\tau\); otherwise \(n<\tau\). Thus a uniform logarithmic stopping bound forces every such \(m\) to be exponentially large in \(n\). PR201's sparse-source tail \(\sum_{m>X,\ m\in\cup_n\mathcal M_n}1/m\ll X^{H_2(4/7)-1}\) then gives exponential decay.

Conversely, if \(\tau(m)/(1+\log m)\) is unbounded, take a sequence with the ratio tending to infinity. Up to \(\tau\) the earliest maximizing phase above has date \(t=O(1+\log m)\). Its odd source \(u=U^t m\) satisfies \(\log u=O(1+\log m)\), since \(U(x)+1\le(3/2)(x+1)\). Its word through \(r=\tau-t\) passes, with \(r/(1+\log u)\to\infty\). Its least positive representative at that depth is at most \(u\), so \(J_r\ge1/u=\exp(-o(r))\). Nothing here proves a logarithmic stopping bound. In particular a polynomial or reciprocal-logarithmic loss criterion makes a substantially weaker quantitative demand.

The two first-failure Lean modules use the earlier positive ordinary path uniqueness theorem from PR201. OldHeadOrdinary.lean imports the *exact actual map and state* from PR200, with parents PermanentSafeDebt.lean and PermanentSafeOrdinary.lean at commit eb91086951b66923787f696801f0c3ca52a0077d. [PR200 actual state and valuation](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/PermanentSafeOrdinary.lean) · [PR200 earlier entrance bound](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/SAFE_BIT_CLOCK.md) · [PR200 target](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/NEXT_FIRST_MOMENT_TARGET.md) · [PR201 source envelope](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md).
