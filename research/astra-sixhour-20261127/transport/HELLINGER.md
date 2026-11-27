# A stretched-exponential all-rank bound at the critical odd frequency

**PROPOSED written theorem.** Take the two-arm shortcut chart
\((Y,3Y-1)\) and its deterministic bijection between length-\(H\) lower
and upper parity words. Delete a word as soon as its two affine germs
merge. Write \(a,b\) for its respective odd counts. For \(0<q<1\) let
\(\mu_q(w)=q^{|w|_1}(1-q)^{H-|w|_1}\) on binary words. Set
\[
    K_q(H)=\sum_{\rm unmerged}\sqrt{\mu_q(w_{\rm low})\mu_q(w_{\rm up})},
    \qquad \alpha=\log_3 2.
\]
All ranks and carries reached from the physical root are permitted.
For constants depending only on the fixed \(q\),
\[
 K_q(H)\ll_q
 \begin{cases}
       \exp[-c_q H/\log(2+H)] & 0<q<\alpha,\quad q\ne1/2,\\
       \exp[-c H^{1/3}] & q=\alpha .
 \end{cases}                                                       \tag{1}
\]
In particular the number of unmerged \(H\)-clock pairs with
\(a,b\ge\alpha H-D\), \(D\ge0\), is at most
\[
        C\left(\frac{\alpha}{1-\alpha}\right)^D
           2^{H H_2(\alpha)}\exp(-c H^{1/3}).                       \tag{2}
\]
This beats the one-arm critical entropy count by a superpolynomial
factor. Its exponential rate remains \(H_2(\alpha)\) in this upper
bound. A comparable-height upper-certified ordinary rooted return has
\(a=b\ge\alpha H-\log_3(BD(X_0))\) by [the physical height estimate](CERTIFIED_RANK.md).

## The changed law and its deterministic coordinates

Let \(A=a_t,\ B=1+b_t,\ m=\min(A,B)\), with signed rank \(r=B-A\).
At the current state \((r,c)\) the two parity bits \(e,f\) are equal
if \(c\) is even and opposite if it is odd. On a common clock draw
\(e=f\) with odd probability \(q\); on a mismatch choose either
orientation with probability \(1/2\). The total Hellinger mass equals
\[
       \mathbb E[{\bf1}_{\rm unmerged}\, k^{J_H}],
       \qquad k=2\sqrt{q(1-q)}
\]
where \(J_H\) counts mismatch clocks. This follows by multiplying
the one-clock factors, which are \(1-q,q,\sqrt{q(1-q)}\) on the three
types. All decisions concern a symbolic counting law; no ordinary
orbit is presumed typical. At the actual root a nonmerged finite word
has nonzero integer carry throughout by the physical ternary-unit proof
in [PR192](../../astra-unconventional-20261126/operator/PAIRED_CAPACITY.md).
For its application to germs take any positive lift larger than the
finitely many accidental intersections of distinct prefix affine
functions. Two identical affine germs remain identical on the whole
cylinder and all its descendants.

Define the signed normalized carry
\[
 d=3^{m-B}y-3^{m-A}x=3^{-|r|}c .
\]
Writing primed letters for the next state and \(\xi=m'-m\), direct
substitution gives
\[
      d'=(3^\xi/2)d+\tfrac12(3^{m'-B'}f-3^{m'-A'}e).
                                                                    \tag{3}
\]
The additive term has absolute value at most \(1/2\). The increment
\(\xi\) is either zero or one. On common clocks its mean is \(q\);
at a mismatch and unequal incoming grades its mean is \(1/2\), and
at a mismatch and equal incoming grades it vanishes. Thus its
conditional mean is at most \(\max(q,1/2)\). The process may be
continued at a merged state with common draws for purposes of
concentration.

At any nonzero rank let \(e_r=v_2(3^{|r|}-1)\). A common run there
has length stochastically bounded by \(e_r+G\), where
\(\Pr(G\ge j)\le(1-p_*)^{j-1}\), \(p_*=\min(q,1-q)>0\).
In fact for nonzero even \(c\) the available next carries are
\(c/2\) and \((3c\pm(3^{|r|}-1))/2\). If \(0<v_2(c)<e_r\), both
remove exactly one dyadic factor. If \(v_2(c)\ge e_r\), one of the
two choices leads to valuation \(e_r-1\), with probability at least
\(p_*\). After that the countdown is deterministic. This extends
the fair holding estimate in [PR146, the physical return proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)
to the changed common-bit law. Since \(|r|\le H+1\),
\(e_r\le 2+\log_2(H+1)\) by elementary factorization. At rank zero,
every common step divides the nonzero carry by two times an odd
factor; the number of consecutive common clocks is exactly \(v_2(c)\),
or at most this value if the observation ends earlier.

## Critical tilt

Put \(S_t=\sum_{i<t}(\xi_i\log3-\log2)\). For \(q=\alpha\) the
increments have nonpositive conditional mean, and their range has
length \(\log3\). For every \(u<v\le H\), conditional Hoeffding or
the elementary exponential-supermartingale proof gives
\[
 \Pr(S_v-S_u>H^{2/3})\le
       \exp[-2H^{4/3}/((v-u)(\log3)^2)] .
\]
Union over the at most \((H+1)^2\) subintervals. Outside probability
\(O(e^{-cH^{1/3}})\), (3) then gives simultaneously
\[
           |d_t|\le (|d_0|+H/2)e^{H^{2/3}}\qquad(0\le t\le H).
\]
In particular every rank-zero nonmerged run has at most \(C H^{2/3}\)
common clocks, since there \(d_t=c_t\) is a nonzero integer.
For nonzero-rank runs the preceding geometric tail and a union over
the at most \(H+1\) possible start clocks give the same upper bound
outside probability \(O(e^{-c H^{2/3}})\). Truncated terminal runs
are included in these statements. Therefore on the surviving good
event
\[
             H\le J_H+(J_H+1) C H^{2/3},
\]
so \(J_H\ge c' H^{1/3}\) for large \(H\). Since \(k<1\), the
Hellinger expectation proves the second line of (1).

At \(q=\alpha>1/2\), on the event in (2), each Hellinger weight is
\((1-\alpha)^H[\alpha/(1-\alpha)]^{(a+b)/2}\ge
2^{-H H_2(\alpha)}[\alpha/(1-\alpha)]^{-D}\).
This proves (2).

## Strictly subcritical tilt

Let \(H_0\) count just the common rank-zero holds, \(p_0\) their odd
count, and \(H_1=H-H_0\). The nonzero-carry telescope in
[the gap-entropy proof, §1](../../astra-unconventional-20261126/operator/GAP_ENTROPY.md)
gives
\[
                  2^{H_0}\le 3^{p_0}18^{H_1}.                         \tag{4}
\]
For clarity a nonempty complementary stretch with \(j\) active clocks
starts at rank zero or initially one, never reaches a rank of magnitude
above \(j+1\), and increases the absolute carry by at most a factor
\(18^j\); common zero clocks inside it only contract. Each rank-zero
hold contributes exactly \(3^e/2\) to absolute carry. Multiply and use
initial magnitude one, final nonzero integer magnitude at least one.
This works also when the final rank differs from the initial rank.

Choose \(q<q'<\alpha\). The common rank-zero bits can be drawn from
a separate iid Bernoulli-\(q\) stream since the decision to use this
stream is made from the past. Except with probability \(O_q(e^{-c_qH})\)
there is no prefix of that stream of length between \(H/2\) and \(H\)
with mean above \(q'\). On an unmerged path (4) now implies
\(H_1\ge c_q H\): use \(H_0<H/2\) directly, or insert
\(p_0\le q'H_0\) in (4).

There are at most \(J_H+1\) positive or negative nonzero-rank common
runs. Conditional at the start of each, its length has an exponential
moment bounded by \(C_q e^{t e_{\max}}\) for some fixed \(t>0\), where
\(e_{\max}=2+\log_2(H+1)\). Truncate at time \(H\) and use a zero
length for a nonexistent run. By iterated conditioning the exponential
moment of the sum of the first \(n\) such lengths is at most
\((C_qe^{t e_{\max}})^n\). If \(J_H<n=\lceil\varepsilon H/\log(2+H)\rceil\),
these runs plus the mismatch clocks account for all \(H_1\). On
\(H_1\ge c_qH\), their total is at least \(c_qH-n\). Markov's
inequality with sufficiently small fixed \(\varepsilon>0\) thus makes
this event \(O_q(e^{-c'_q H})\). On the complementary large-\(J_H\)
event the factor \(k^{J_H}\) proves the first line of (1).

No estimate above bounds the probability of permanent disagreement
for fair bits by a stretched exponential. At \(q=1/2\) the mismatch
killing factor is exactly one. Likewise the prior unnormalized
odd-grade kernel has a growing factor per clock when normalized in this
way; formula (1) does not remove that exponential factor.


## Positive common-bit drift at a rooted endpoint

Suppose \(q>\alpha\) and restrict the Hellinger sum to unmerged words
ending with \(\log(2+|d_H|)=o(H)\) uniformly in the selected family.
In particular this covers all contextual root returns. Then
\[
       \sum_{\rm selected}\sqrt{\mu_q(w_{\rm low})\mu_q(w_{\rm up})}
             \ll_q \exp[-c_q H/\log(2+H)] .                       \tag{5}
\]
In the stated little-o form the first sufficiently large clock may also
depend on the specified terminal envelope. At a rooted return the
two grades are equal, so its Hellinger weight is exactly its single
lower-word probability \(\mu_q(w_{\rm low})\).

Indeed put \(V(d)=\log\max(K,|d|)\) with fixed \(K>2\) large. From (3),
on \(|d|\ge K\),
\[
 V(d')-V(d)\ \ge\ \xi\log3-\log2 +\log(1-1/K).
\]
On \(|d|<K\) the difference is nonnegative. On high common clocks
\(\xi\) is the fresh Bernoulli-\(q\) bit; the decision to select
such a clock uses the preceding state. Fix \(\alpha<q'<q\) and then
\(K\) so large that \(q'\log3-\log2+\log(1-1/K)>0\).
Except on an event \(O_q(e^{-c_qH})\), every prefix of the separately
prepared high-common stream of length between \(H/3\) and \(H\)
has average at least \(q'\). High mismatch clocks each lose at most
\(\log2-\log(1-1/K)\). If the path has at least \(H/3\) high common
clocks and \(J_H=o(H)\), summing the increments forces
\(V(d_H)-V(d_0)\gg_q H\), contrary to the selected envelope.

During any rank-zero common run, after the first low state
\(|d|=|c|<K\) the remaining run has length at most \(\log_2K\)
because its dyadic valuation counts down. Thus the total **low**
rank-zero common time is at most \((J_H+1)(1+\log_2K)\), even if
the run crosses the high threshold several times. On the event
\(J_H<\varepsilon H/\log(2+H)\), the bounded conditional run moments
proved above bound all nonzero-rank common time by \(H/3\) except
with probability \(O_q(e^{-c_qH})\), for sufficiently small
\(\varepsilon\). The remaining common clocks exceed \(H/3\) for all
large \(H\); they are high rank-zero clocks. This proves (5) after
applying the mismatch factor \(k^{J_H}\) on the other event.

**Verification scope.** The [strict Lean kernel](HellingerCarry.lean)
proves the normalized one-step recurrence from the ordinary affine
step, the absolute error and both minimum-grade increment identities.
[Compiler output](../../../reports/astra-sixhour-20261127/transport/hellinger_carry_lean.txt).
The [separate ordinary-grid checker](check_hellinger.py) compares the
symbolic propagation with every large positive representative on
complete grids up to 15 clocks for the listed rational tilts. It
tests both valuation regimes and each physical normalized update.
[Exact numerators](../../../reports/astra-sixhour-20261127/transport/hellinger_grid.json).
The inequalities in the large-clock limit are written proofs.
