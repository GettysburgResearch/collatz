# A future long hold identifies the previous long hold's odd count

**Proposed written theorem with a finite arithmetic kernel.**
Keep the positive ordinary two-arm chart, physical root, changed
parity-word law, mismatch count \(J_H\) and Hellinger mass \(K_q(H)\)
of [the normalized-carry proof](HELLINGER.md). All nonmerged terminal
germs are permitted, with no final carry or relative-rank restriction.
For every fixed \(q\in(0,1)\setminus\{1/2\}\), including
\(q>\alpha=\log_3 2\), one has
\[
    K_q(H)\ll_q \exp\left[-c_q
                   \frac{\log^2(2+H)}{\log\log(4+H)}\right].        \tag{1}
\]
At the critical tilt the stronger estimate
\[
    K_\alpha(H)\ll \exp\left[-c H^{1/3}
              \left(\frac{\log(2+H)}{\log\log(4+H)}\right)^{2/3}
                        \right]                                    \tag{2}
\]
holds. It gives the same factor in place of \(\exp(-cH^{1/3})\) in
the joint high-odd-count native-grid estimate there. The separate
subcritical bound \(\exp(-c_q H/\log H)\) is stronger than (1) when
\(q<\alpha\). On rooted returns it holds also at \(q>\alpha\) by
the terminal potential in the preceding note.

## The certificate between two long holds

A hold means a maximal sequence of common clocks at rank zero.
For a nonzero integer entry carry \(c_i\), its full length is
\(n_i=v_2(c_i)\), independent of all its bits. After the complete
hold, its carry is \(b_i3^{p_i}\), where \(b_i=c_i/2^{n_i}\) is odd
and \(p_i\) counts its ones. In a fixed \(H\)-clock observation only
the final hold can be truncated. Define
\[
                D=\lceil\log_2(8H+1)\rceil.
\]
Call a hold long when its **full** length is at least \(D\); this
decision is known at entry, even when the final observation truncates
it. All other holds are short.

Suppose a long hold completes and a later long hold starts. Fix the
intervening sequence of nonzero-rank clocks and all mismatch clocks
with their bit pairs, together with the lengths and odd counts of
the intervening short rank-zero holds. Rank evolution is thereby
specified. Every individual complementary clock has an integral
affine carry update \(2c'=3^j c+h\), with \(j\in\{0,1\}\) and the
integer \(h\) depending only on the ranks and indicated bits,
including a crossing into or out of zero. More explicitly,
\(r'=r+f-e\), \(j=(-r')_++f-(-r)_+=(r')_++e-(r)_+\in\{0,1\}\),
and \(h=3^{(-r')_+}f-3^{(r')_+}e\). A short
rank-zero hold contributes the single linear update \(2^n c'=3^p c\).
Composition from immediately **after** the first long hold up to,
but excluding, the next one gives
\[
            2^s c_{\rm next}=3^u b_i3^{p_i}+v .                      \tag{3}
\]
The integers \(s,u,v\) are fixed by the intervening data. Thus
\(2^D\mid 3^u b_i3^{p_i}+v\), and \(3^u b_i\) is odd.

There is at most one eligible \(p_i\in[0,H]\). Every nonfinal long hold closes before the observation ends, so its full length equals its observed length and is at most \(H\). Indeed if
\(p<p'\) both worked, odd cancellation would give
\(2^D\mid 3^{p'-p}-1\); for \(1\le d\le H\),
\(2^{v_2(3^d-1)}\le4d\le4H\). One can use the looser \(8H\)
by factoring \(9^d-1\) with its odd cofactor. The
[Lean arithmetic kernel](HoldPinning.lean) proves precisely the
resulting uniqueness for arbitrary signed odd coefficient, signed
translation and full preceding clock budget. It proves the dyadic
order bound by elementary factorization.
[Compiler output](../../../reports/astra-sixhour-20261127/transport/hold_pinning_lean.txt).

## Encoding the time outside long holds

Fix a large parameter \(E\) (the choices below satisfy
\(\log H\ll E\ll H/\log H\)). We can restrict to \(J_H\le E\) at
Hellinger cost \(k^{\lfloor E\rfloor}\) on the complementary event,
where \(k=2\sqrt{q(1-q)}<1\). Let \(B\) count all clocks outside
rank-zero common holds. With probability \(1-O_q(e^{-c_qE})\) on
\(J_H\le E\),
\[
                         B\le B_*=C_q E\log(2+H).                    \tag{4}
\]
Indeed the \(J_H\) mismatch clocks are already accounted for. Each
remaining run of nonzero-rank common clocks has, conditional on its
entry, an exponential moment bounded by
\(C_q\exp(t(2+\log_2(H+1)))\) for fixed \(t=t_q>0\), by the elementary
valuation countdown and geometric release bound in the preceding
note. Sum the first \(\lfloor E\rfloor+1\) such lengths, truncating at
clock \(H\) and padding nonexistent runs with zeros. Iterated
conditioning and exponential Markov give (4) for a large enough
constant, even with error \(O_q(\exp(-c_q E\log H))\). In applying
(1) below one may if desired stop on the \((\lfloor E\rfloor+1)\)-th
mismatch and use the sharper rank cap \(E+2\).

Construct the changed law with four independent bit streams, one for
mismatches (fair orientation) and three Bernoulli-\(q\) streams for
nonzero-rank common clocks, short rank-zero holds and long rank-zero
holds. State, mismatch status, and the prospective **full** rank-zero
hold length are known before revealing the corresponding bit. In
particular the stream choice is predictable. Now condition on all
streams except the one for long holds. Record the following finite
information about a putative surviving trajectory with \(J_H\le E\),
\(B\le B_*\).

* The number of mismatches. In each of the at most \(\lfloor E\rfloor+1\)
  inter-mismatch common intervals (including the initial and terminal
  intervals), record whether it is empty, is a nonzero-rank common
  run, or is a short or long rank-zero hold.
* The observed lengths of the nonzero-rank common runs, with total
  at most \(B_*\), and the observed lengths of the short holds, each
  less than \(D\).

Zero-length intervals may be given the empty type. No bits or
lengths of large holds are recorded. Inter-mismatch intervals have
constant rank since common clocks never change it, so the record
covers every clock. Its number of possibilities is at most
\[
 \exp\{C E[\log(2+B_*/E)+\log(2+D)]\}
             \le \exp\{C_q E\log\log(4+H)\}.                         \tag{5}
\]
For example, sum lengths for at most \(\lfloor E\rfloor+1\) padded
nonzero slots and bound by the weak-composition binomial coefficient;
for the short slots allow each length from zero to \(D\) independently.
The bound includes the type flags and number of intervals.

Fix one record and the conditioned streams. Its initial segment
up to the first long hold is determined. Equation (3) identifies
the odd count in that long hold from its entry carry and the
record up to the next long hold: the bits consumed from the three
fixed streams and their indices are now known from the type/length
record. The order of bits within the first long hold has no effect on
its exit carry once its odd count is known. If the identified count
does not exist, or a specified intervening edge is inconsistent, the
record contributes zero. Repeating determines each of the nonfinal
long initial carries, full lengths and odd counts. Their bits come
from consecutive fresh blocks of the unconditioned stream. The
conditional probability of the record is therefore at most
\[
                 \prod_{\substack{i\ {\rm long}\\
                             \text{another long hold follows}}}
                    \min(1,C_q/\sqrt{n_i}),                         \tag{6}
\]
by the maximum point probability of a binomial \((n_i,q)\). The
final long hold may run to the horizon or end before a terminal
string of other clocks; its count is left unrestricted in either
case. This proof conditions on **independent preassigned streams**;
it does not condition a binomial sample on the future occurrence
of a long hold. Summing (6) over the putative records by (5) is the
required treatment of that future event.

## Paying the cost of the recorded lengths

Let the lengths below be observed lengths, including any terminal
truncation. At every rank-zero hold entry its full length obeys
\[
     n_i \le C\left(2+B+\sum_{j<i} n_j\right).                       \tag{7}
\]
Here it suffices to use the observed lengths of preceding holds.
The initial carry has magnitude one. Each complementary stretch of
length \(b\) starts at rank zero or initially one and increases
the absolute carry by at most \(18^b\), by the integral-carry
telescope in [the gap proof](../../astra-unconventional-20261126/operator/GAP_ENTROPY.md).
Each rank-zero common step grows its magnitude by at most \(3/2\).
Since \(2^{n_i}\le|c_i|\), (7) follows. The right side also bounds
the observed length of the very last hold.

For \(S\ge2,\ 0\le n\le CS\),
\[
                 \log^2(S+n)-\log^2 S\le C'\log(2+n).               \tag{8}
\]
For \(n\ge S\), use the bounded \(\log(1+n/S)\) and
\(\log S\le\log n\). For \(0<n<S\), bound the difference by
\(C(n/S)\log S\le C'\log(2+n)\), using that
\(\log s/s\) decreases for \(s\ge e\), and treat \(n\le2\) directly.
Sum (8) with \(S=2+B+\sum_{j<i}n_j\). The total terminal
\(S=H+2\); the initial square log is at most \(\log^2(2+B_*)\).
Short holds contribute at most \(C(E+1)\log(2+D)\), and removal
of the final long hold costs at most \(C\log(2+H)\). Thus
\[
 \sum_{\text{long except last}}\log n_i
 \ \ge\ c\log^2(2+H)-C\{\log^2(2+B_*)+
                 (E+1)\log(2+D)+\log(2+H)\}.                        \tag{9}
\]
Factors \(C_q\) in (6) cost only \(O_q(E+1)\) in the logarithm.
Take \(E=\epsilon_q\log^2(2+H)/\log\log(4+H)\). Here \(B_*\)
is polylogarithmic, and (5), (6), (9) give
\(O_q(e^{-c_q\log^2 H})\) for the surviving small-mismatch event
with (4), taking the fixed \(\epsilon_q\) sufficiently small. The
discarded large-\(J_H\) Hellinger mass and (4) give (1).

## Extra information at zero drift

At \(q=\alpha\), the normalized carry recurrence and bounded
conditional increments in [the critical proof](HELLINGER.md) give,
except on an event \(O(e^{-c E})\), for all prefixes
\[
              \log(2+|d_t|)\le C\sqrt{HE}.
\]
Indeed union-bound Hoeffding over all subintervals at threshold
\(C_0\sqrt{HE}\); the polynomial number of intervals is absorbed
because \(E\gg\log H\). Every observed rank-zero hold then has
\(n_i\le A=C\sqrt{HE}\). For the choice of \(E\) below, (4) gives
\(B_*=o(H)\), and all short holds have total at most \((E+1)D=o(H)\).
Accordingly the long holds account for at least \(H/2\) clocks. The
last long hold may be dropped since \(A=o(H)\). On all remaining
long holds \(D\le n_i\le A\); since \((\log n)/n\) decreases for
\(n\ge3\),
\[
       \sum_{\rm long\ except\ last}\log n_i
               \ge c H(\log A)/A
               \ge c'\sqrt{H/E}\,\log H .                            \tag{10}
\]
If the last fully long hold is observed shorter than \(D\), this
does not affect (10), where it has already been dropped.

Apply (5) and (6), and take
\[
     E=\epsilon H^{1/3}
           (\log(2+H)/\log\log(4+H))^{2/3}.
\]
For small fixed \(\epsilon>0\) the right side of (10) dominates
\(C E\log\log H\) with arbitrarily large constant ratio. The length
and probability estimates prove (2). The normalized-carry
concentration, entropy of records, binomial bound, and asymptotic
combination are written arguments. Individual ordinary trajectories
are never assigned a probabilistic law.
