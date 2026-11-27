# Positive ternary quotients at every phase of the bounded cycle alternative

Use the least-tripling-disagreement **bounded alternative**. The least bad positive integer \(s\) is the minimum of an odd cycle with phases \(s\le x_i\le(16s+7)/3\), and \(2^{e_i}x_{i+1}=3x_i+1\) with \(e_i\in\{1,2\}\). Every \(x_i-1,x_i+1\) reaches one. These are hypotheses proved on that particular alternative. The first-crossing alternative can reach an arbitrary cycle. [Bounded-alternative source](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/cycle/CANONICAL_FLOOR.md)

Put \(r_i=(-1)^{e_{i-1}}\). Then \(x_i\equiv r_i\bmod 6\), by oddness and the preceding edge. Define \(v_i=(x_i-r_i)/6\). For \(s\ge 25\),
\[
0<v_i<s,\qquad C(v_i),\qquad C(3v_i).
\]
Here \(C\) denotes ordinary convergence to one. Indeed \(v_i\le(16s+10)/18<s\) and \(3v_i=(x_i-r_i)/2\) is an ordinary successor of a good even neighbor.

Substitution into the ordinary edge gives
\[
2^{e_i}v_{i+1}=3v_i+
\frac{r_i-r_{i+1}}2.
\]
The defect is \(0\) on equal consecutive gaps, \(+1\) on a switch from two to one, and \(-1\) on a switch from one to two. In particular the nonzero defects alternate and all switch sources are odd.

Suppose a maximal run of \(a\) ones is followed by \(b\) twos and then another one. Let \(v,w,v'\) be the positive odd switch sources at the beginning, middle and end. The homogeneous interiors give
\[
2^a w=3^{a-1}(3v+1),\qquad
4^b v'=3^{b-1}(3w-1).
\]
Thus \(a=\nu_2(3v+1)\) and \(2b=\nu_2(3w-1)\) exactly. With \(U(v)=\operatorname{oddpart}(3v+1)\) and \(V(w)=\operatorname{oddpart}(3w-1)\), the two induced steps are \(w=3^{a-1}U(v)\) and \(v'=3^{b-1}V(w)\). This exposes the ordinary positive \(3v+1\) map at every up-switch and a positive \(3w-1\) map at every down-switch.

There is a quantitative obstruction to straightening the defects while retaining the same heights and total clock. For any positive integer cyclic path \(H_i\) of length \(p\) satisfying \(2^{b_i}H_{i+1}=3H_i+J_i\), with \(h=\sum b_i\) and \(J_i\ge0\), let \(M=\max H_i\) and \(t=\#\{i:J_i>0\}\). Multiplication gives
\[
\frac{2^h}{3^p}=\prod_i\left(1+\frac{J_i}{3H_i}\right)
 \ge \left(1+\frac1{3M}\right)^t.
\]
If \(t=p\) and the ordinary reference cycle has the same \(p,h\) and minimum \(s\), then its product is at most \((1+1/(3s))^p\), forcing \(M\ge s\). More sharply, another ordinary cycle of the same \(p,h\) cannot lie strictly below the reference cycle in phasewise comparison, since all factors in its product would be larger. This obstruction applies even if the individual clock exponents are redistributed. The displayed quotient bypasses this height obstruction through its negative defects. Its down-switches and the powers of three at run endpoints still require a changed-clock ordinary descent.

The Lean kernel proves the exact integral quotient, switch recurrence, height bound, switch oddness and homogeneous run compression. The source-specific goodness assertions and the cyclic product comparison are written deductions. [Lean kernel](TernaryQuotient.lean)
