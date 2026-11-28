# Early and late first visits to 1 on the shortcut clock

Write \(T(2n)=n,\ T(2n+1)=3n+2\), let \(\tau(n)\) be the first date at which \(T^t n=1\), and set \(\tau(n)=\infty\) if no such date exists. All logarithms without a subscript are natural. Put \(\mu=2/\log(4/3)\).

**Status.** Proposed written deductions from the stated analytic inputs, with finite arithmetic separately checked in Lean and by exhaustive census.

## A lower bound uniform in the deadline

There are absolute \(a,c,C>0\) such that for all sufficiently large \(X\) and every real \(0\le w\le a\log X\), each of the following sets has cardinality at least
\[
                  cX\exp\!\left(-C\,w^2/\log X\right).
\]

* Odd \(n\in(X/4,X]\) with \(\tau(n)\le\mu\log X-w\).
* Odd \(n\in(X/4,X]\) with \(\mu\log X+w\le\tau(n)<\infty\).

Moreover, at least \(c'X^2\exp(-C'w^2/\log X)\) unordered pairs of positive integers through \(X\), separated by more than \(3X/16\), first meet through \(1,4\mapsto2\) by \(\lfloor\mu\log X-w\rfloor\), after decreasing \(a\) if needed. At \(w=\delta\log X\) this gives a count of order at least \(X^{2-C'\delta^2}\) for every sufficiently small fixed \(\delta>0\). The constants come from a selected inverse-word estimate. The proof gives no numerical fraction at the median and makes no claim of optimality for the exponent or constants.

### One inverse stage with a chosen sign

We use the retained joint lower bound in Lyapunov Weaver's Lemma 13, including its dependencies on El Jaouhari's selected blocks, Fourier Wren's fixed-total construction and the averaged joint mixing estimates. The two-sided window in Weaver's Theorem 14 by itself allows all paths on one side. We use the individual central depths in its proof. The geometric probabilities below count compatible words, which reconstruct actual odd integer trajectories. [Weaver, Lemma 13 and Theorem 14, equations (39)–(41)](https://rstation.ai/problems/collatz/papers/12)

Let \(a_0\le M\) be a positive odd integer prime to 3. For each \(Y/M\) sufficiently large, Weaver chooses a direct odd predecessor \(r=(2^e a_0-1)/3\) on the selected ternary cylinder. Its height is comparable to \(M\), and \(e=\log_2(M/a_0)+O(1)\) with absolute constants. His choice ensures \(r>2B_0\) and \(r-B_0>R_0M\). In the notation of Lemma 13, \(A_i=3^i2^{-D_i}\), \(B_i=\sum_{j\le i}A_j/3\). The selected words have \(A_i\le R_0,\ B_i\le B_0\) for all \(i\le k\). Consequently every earlier odd value \((r-B_i)/A_i\) and \(r\) exceed \(M\).

Set \(L=\log_2(Y/r)\), \(\theta=\log_2 3\), \(\beta=2-\theta\) and \(k_*=L/\beta\). For a fixed small \(h>0\) use all integers \(k\) in either of the strips
\[
 [k_*-2h\sqrt L,k_*-h\sqrt L],\qquad
 [k_*+h\sqrt L,k_*+2h\sqrt L].
\]
Put \(d_k=\lfloor L+\theta k\rfloor\). Then \(|d_k-2k|\le 2\sqrt k\) for all sufficiently large \(L\), uniformly in either strip. Under geometric gap weights, each length-\(k\) word of total \(d_k\) has probability \(2^{-d_k}\). Its total-slice probability is \(\pi_k(d_k)=\binom{d_k-1}{k-1}2^{-d_k}\gg L^{-1/2}\) by Stirling's formula in this central range. Lemma 13 bounds the retained, compatible probability below by \(c_0 3^{-k}\pi_k(d_k)\). Therefore the number of retained words at this depth is
\[
 \gg 2^{d_k}3^{-k}L^{-1/2}\gg (Y/M)L^{-1/2}.
\]
The selected initial value \((r-B_k)2^{d_k}/3^k\) is odd and lies in \((Y/4,Y]\), since \(r-B_k>r/2\) and \(Y/(2r)<2^{d_k}/3^k\le Y/r\). Its first odd landing at or below \(M\) is \(a_0\) after \(k+1\) odd steps, or \(d_k+e\) shortcut steps. An earlier visit to 1 would already be an odd landing. For a fixed depth an actual source fixes its entire word. Distinct depths are disjoint by the first-landing condition, including at periodic targets. Summing the \(\gg\sqrt L\) depths gives at least \(\gamma Y/M\) distinct sources on **each** side, with an absolute \(\gamma>0\).

At \(k_*\) the unfloored total is \(2L/\beta=\mu\log(Y/r)\). Changing \(k\) changes it by \(\theta(k-k_*)\). Absorb the bounded cost of replacing \(r\) by \(M\) and rounding. Relative to \(\mu\log(Y/M)+\log_2(M/a_0)\), the actual durations have the chosen sign and absolute deviations in \([b\sqrt{\log(Y/M)},B\sqrt{\log(Y/M)}]\), with absolute \(B>b>0\) once \(Y/M\) exceeds an absolute constant.

### Joining stages without losing the first-hit time

Fix an integer \(m\ge1\). Set \(s=(\log X)/m\), \(Y_j=e^{js}\) and \(Y_0=1\), and require \(s\ge s_0\) for a sufficiently large absolute \(s_0\). Start from the root \(1\) with \(M_1=1\). At stage \(j\), apply the preceding estimate with upper height \(Y_j\) to each retained target. The resulting sources \(y\) are odd and belong to \((Y_j/4,Y_j]\). If \(j<m\), use for the next stage the targets
\[
 a(y)=y\quad(3\nmid y),\qquad a(y)=4y+1\quad(3\mid y),\qquad
 M_{j+1}=4\lfloor Y_j\rfloor+1.
\]
These are odd units. The map is injective on the band because its changed values exceed \(Y_j\). For odd \(y>1\), \(T^3(4y+1)=T(y)\), with no visit to 1 in the first three states of the new path. Hence \(\tau(4y+1)=\tau(y)+2\) whenever \(\tau(y)\) is finite. Every constructed source reaches its target before visiting 1, except for the terminal arrival when that target is 1. Its first-hit date is exactly the first-landing duration plus the target's first-hit date. This remains exact when a target has been replaced.

All targets of stage \(j+1\) are larger than \(Y_j/4\). Thus \(\log_2(M_{j+1}/a(y))\) is uniformly bounded, and \(\log(Y_j/M_j)=s+O(1)\) at every stage. Absorb this bounded shift and any two-date replacement by increasing \(s_0\). With the same sign chosen at every stage, the deviation per stage from \(\mu s\) lies, in absolute value, between \(b'\sqrt s\) and \(B'\sqrt s\) for fixed \(0<b'<B'\). More explicitly one may attach the cost of each replacement to the next first-landing duration, and use cost zero at stage 1.

Sources for distinct targets in one stage have distinct first-landing labels. The population therefore grows at stage \(j\) by a factor at least \(\gamma Y_j/M_j\). As \(M_j\le5Y_{j-1}\), the final population is at least \(X\kappa^m\) for \(\kappa=\min(\gamma/5,1/2)>0\). Its first-hit dates differ from \(\mu\log X\) in the prescribed direction by between \(b'\sqrt{m\log X}\) and \(B'\sqrt{m\log X}\). Take
\[
          m=\max\!\left(1,\left\lceil w^2/((b')^2\log X)\right\rceil\right).
\]
Choosing \(a>0\) sufficiently small ensures \(s\ge s_0\) uniformly for \(0\le w\le a\log X\) and large \(X\). The claimed two one-source estimates follow.

For the pair count, take the fast odd sources \(n\in(W/4,W]\) at \(W=X/16\). Use these and their dilates \(16n\) as the lower and upper bands. The upper first-hit date is \(\tau(n)+4\), so both bands reach 1 by \(\lfloor\mu\log X-w\rfloor\), since \(\mu\log16>4\). Shrink \(a\) to satisfy the one-source range at \(W\). If there are \(N\) lower sources, the finite parity and tie count gives at least \(3N^2/8\) first meetings through 1 and 4. Every gap exceeds \(X/4-X/16=3X/16\). This proves the pair assertion. [Finite pair proof, equation (1)](README.md#a-finite-construction-using-two-dilations)

## How a least counterexample would affect the median

Let \(d\) be the natural density of starts that ever reach 1, \(u=1-d\), and \(H_X=\lfloor\mu\log X\rfloor\). Define \(F_X\) to be the fraction of \(n\le X\) with \(T^{H_X}n\in\{1,2\}\). The minimum/time law restricted to minimum 1 gives \(F_X\to d/2\), since entry into \(\{1,2\}\) differs from the first visit to 1 by at most one date on this basin. A median lower bound \(F_X\ge1/2-o(1)\) therefore requires \(d=1\). [Leen, joint minimum and hitting-time law](https://doi.org/10.5281/zenodo.23269488)

Let \(\Delta\) be \(1/8\) minus the limit of the probability that two independent uniform starts through \(X\) agree at date \(H_X\). The phase formula gives \(d^2/8+R\) for this limit. Each other cycle \(C\) contributes \(d_C^2/(4P_C)\), where \(P_C\) is its least shortcut period and \(d_C\) its basin density. The only positive solutions of \(T^2 n=n\) are 1 and 2. Hence \(P_C\ge3\) for every other cycle, and disjointness gives \(0\le R\le u^2/12\). Subtraction yields
\[
              \frac{u(1+5d)}{24}\ \le\ \Delta\
                         \le\ \frac{u(1+d)}8 .
\]
[PR #214, equation (2) at the median](https://github.com/GettysburgResearch/collatz/blob/504d29d399efa941a62006d1ea4635385ce6bb5f/research/astra-critical-rigidity-20261128/ordinary/SYNCHRONOUS_PHASE_DISPERSION.md)

Suppose a least positive nonconvergent start \(r\) exists. It is odd, since an even counterexample halves to a smaller one. When \(3\nmid r\), all predecessors of \(r\) fail to reach 1. Otherwise use the odd unit \(4r+1\le5r\), which joins \(r\)'s path after three shortcut steps against one. Weaver's reciprocal lower density for predecessors of units now gives \(u\gg 1/r\). Conversely every nonconverging start avoids all of \([1,r-1]\), including all possible odd landings there. The uniform failure-atom estimate at threshold \(r-1\) therefore bounds the fraction of nonconverging odd starts in each sufficiently large quarter-to-full interval by \(O(r^{-\eta})\), with
\[
 \eta=1-H_2(\log_3 2)+7/2500=0.052844\ldots ,
\]
where \(H_2\) is binary entropy. Summing those intervals gives the same upper bound on their relative odd density. Doubling invariance gives the bound on all starts by summing over their initial powers of two. Thus
\[
             c_1/r\le u\le C_1 r^{-\eta},
             \qquad c_2/r\le\Delta\le C_2 r^{-\eta}.
\]
If every start converges, \(u=\Delta=0\). The constants in the cited upper estimate have no stated usable numerical values. A finite plateau with \(F_X>1/2\) cannot distinguish these alternatives without a uniform error estimate. The two powers leave a large gap even in the limit. [Weaver, Theorem 1](https://rstation.ai/problems/collatz/papers/12) · [Weaver, uniform bound for landing atoms including failure, Theorem 1](https://rstation.ai/problems/collatz/papers/102)

### Size of the contribution from other cycles

The classical lower bound for a cycle period sharpens the error \(R\). If a nontrivial cycle has \(g\) odd departures in its \(P\) shortcut dates, multiplying its transitions gives
\[
  0<P\log2-g\log3=\sum_{\text{odd }x\in C}\log(1+1/(3x))\le g/(3r).
\]
Simons and de Weger's Lemma 12, applying Rhin's two-logarithm bound, gives \(P\log2-g\log3\gg g^{-13.3}\) for such a cycle. Their \(K=g\) and \(K+L=P\). Consequently \(P\ge g\gg r^{10/143}\). Inserting this in the phase sum gives, with \(\gamma=10/143\),
\[
   0\le\frac{u(2-u)}8-\Delta=R
      \ll u^2 r^{-\gamma}\ll u^{2+\gamma}.
\]
The last inequality uses \(u\gg1/r\). In particular, for small positive \(\Delta\), the inversion is \(u=4\Delta+8\Delta^2+O(\Delta^{2+\gamma})\), with absolute constants. To see this, the earlier two-sided inequality first gives \(u\asymp\Delta\). Substituting \(u=4\Delta+O(\Delta^2)\) into \(u^2/2\) in \(u=4\Delta+u^2/2+4R\) gives the formula. This describes the sensitivity of the limiting collision statistic to a small missing density. The period bound is classical. [Simons and de Weger, Lemma 12](https://deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf)

A counterexample also has a finite-scale consequence independent of the phase law. Choose its odd unit representative \(a_0=r\) or \(4r+1\) as above. For every \(X\ge C r\), Weaver's first-landing theorem with \(M=a_0,\ Y=X\) gives \(\gg X/r\) odd nonconverging starts in \((X/4,X]\). Pair these with the fast converging starts through \(X/16\) from the first theorem. For \(X\) sufficiently large and \(0\le w\le a\log X\) this gives \(\gg X^2\exp(-C'w^2/\log X)/r\) separated unordered pairs for which the lower arm has reached 1 by \(\lfloor\mu\log X-w\rfloor\) and the two orbits never share any state, even at different dates. A common state would imply convergence of both arms. This is conditional on the existence of \(r\) and does not identify any such pair. [Weaver, Theorem 14](https://rstation.ai/problems/collatz/papers/12)

## Verification scope

[HalfMass.lean](HalfMass.lean) verifies the relation between cycle entry and first hit, the period-two classification, the affine block identity, the minimum number of steps needed to hit 1, the two-date replacement and its injectivity, finite counting by first-landing label, the product of stage lower bounds, and the displayed collision-gap algebra. [MedianMerger.lean](MedianMerger.lean) supplies the finite pair argument. The analytic lower bounds and timing laws used above remain written inputs. The selection of the signed strips, the multiscale deduction and the passage to limiting densities are written mathematical proofs.

## Exact finite census at the moving median

For each integer \(X\), write \(C_X=\#\{1\le n\le X:T^{H_X}n\in\{1,2\}\}\). The exhaustive [census](median_census_33.jsonl) gives \(5C_X>3X\) for **every** \(1\le X\le2^{33}\). Its dyadic endpoints include

| \(X\) | \(H_X\) | \(C_X\) |
| ---: | ---: | ---: |
| \(2^{30}\) | 144 | 662,035,081 |
| \(2^{31}\) | 149 | 1,328,251,613 |
| \(2^{32}\) | 154 | 2,659,546,489 |
| \(2^{33}\) | 159 | 5,319,073,578 |

The last row is 61.9222%. The exact minimum across **all** checked cutoffs is \(5{,}216{,}532{,}555/8{,}562{,}591{,}375=60.9223578\ldots\%\), attained at \(X=8{,}562{,}591{,}375\). For each octave the receipt records the minimum of \(5C_X-3X\) over all its individual cutoffs and an attaining integer \(X\). Dividing that minimum by five times the octave's upper endpoint gives a lower bound on \(C_X/X-3/5\) throughout it. Even this conservative use of the receipt gives \(C_X/X\ge6501361573/10737418240>0.60548\) over the full checked range.

The [census program](check_half.py) uses exact integer inequalities \(4^t\le3^t X^2\) for the deadline. A trajectory is already on the cycle at \(H\) exactly when its first visit to 1 has occurred by \(H+1\). For each start the program obtains that first-hit time capped at \(H_{\max}+2\). A \(w\)-step jump uses its exact affine formula on the residue modulo \(2^w\) and a cache of smaller starts. For \(n>2^w\), the inequality \(T^j n\ge n/2^j\) prevents a hidden visit to 1 in any skipped date \(j\le w\). A Python-integer fallback handles a potential unsigned multiplication overflow. At each increase in the deadline the entire previous histogram is counted at the new deadline. Within a constant-deadline segment, prefix sums handle every integer cutoff.

The reference scalar calculation uses direct single steps to first entry into \(\{1,2\}\), an independent evolving integer test for the deadline and a fresh sum of the histogram at each cutoff. It matched all octave counts and worst fifths slacks through \(262147\) with three distinct choices of jump width and batch size. Two full traversals with widths 11 and 14 agreed on the counts and minimum fifths slacks in all 34 octave records through \(2^{33}\). A width-13 traversal through \(2^{32}\) additionally tabulated the squared first-hit cohorts for the first-meeting bound. The asymptotic result above concerns arbitrarily large \(X\). No bound for the rate at which this finite statistic approaches \(d/2\) is obtained from these computations.

### A finite lower bound for actual first meetings

For every integer \(3\le X\le2^{32}\), two independent uniform starts through \(X\) have probability **strictly greater than \(7/50\)** of first meeting through \(1,4\mapsto2\) by \(H_X\). The limiting target is \(1/8\). The finite probability here counts ordered draws with replacement, with equal starting values contributing zero to this first-meeting event.

For an integer power of two \(E\), let \(D_t(E)\) count starts through \(E\) with first-1 date \(t\), and set \(S_E=\sum_{t=2}^{H_E+1}D_t(E)^2\). The receipt records this integer through \(E=2^{32}\). For \(E/2<X\le E\), the cohort at 4 at date \(j\) has size \(D_{j+2}(X)\), so its total squared cost in the finite gate identity is at most \(S_E\). Put \(m_E=\min_{E/2<X\le E}(5C_X-3X)>0\). The normalized gate identity, and \(A_H(1)^2+A_H(2)^2\ge C_X^2/2\), give a lower bound on the ordered probability of
\[
 \frac{(3E+m_E)^2-200(S_E+2)}{50E^2}.
\]
The two initial diagonals account for the 2. For each octave ending at \(2^7,\ldots,2^{32}\) the numerator exceeds \(7E^2\). For \(X\le64\) the verifier directly counts all arrivals from 1 and 4 at every date. The probability is zero at \(X=1,2\), and exceeds \(7/50\) at every cutoff from 3 through 64. The finite arithmetic implication from the mass, energy, and octave inequalities is also formalized as gate_octave_certificate. This proves the stated finite result. The same census gives an endpoint-equality probability greater than \(9/50\) through \(2^{33}\) immediately from \(C_X>3X/5\). [Finite gate identity, equation (2)](README.md) · [Exact arithmetic verification](check_half.py)

Run from the repository root with Python and NumPy. The complete \(2^{33}\) run uses an eight-GiB first-hit array and temporary working storage. Smaller limits are accepted.

    python -X utf8 -B research/median-merger-lower-20261128/check_half.py --limit 8589934592 --width 11
    python -X utf8 -B research/median-merger-lower-20261128/check_half.py --limit 8589934592 --width 14 --block 262144 --min-ratio
    python -X utf8 -B research/median-merger-lower-20261128/check_half.py --limit 4294967296 --width 13 --block 262144 --gate
    python -X utf8 -B research/median-merger-lower-20261128/check_half.py --verify-receipt research/median-merger-lower-20261128/median_census_33.jsonl
    python -X utf8 -B research/median-merger-lower-20261128/check_lean.py --lean /path/to/lean --mathlib /path/to/mathlib

The optional minimum-ratio search first screens whole segments with an exact bound on the fifths slack. It then selects the least occupied bin of width \(2^{-25}\) and compares every tied candidate by integer cross multiplication. This orders even very close fractions exactly.

The Lean runner expects Lean 4.34.1 and a built Mathlib at commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
