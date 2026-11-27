# A two-place integer test for the no-adjacent-twos trajectory

An infinite Syracuse word on \(1,2\) with no adjacent twos parses into the two chronological tokens \(A=1\) and \(B=21\). Every complete token ends in exponent 1. After the first token the odd state has the form \(x=6t-1\) with \(t\) a positive ordinary integer: a last exponent 1 gives \(U(z)+1=3(z+1)/2\) and \(4\mid z+1\). Substitution at these boundaries gives the partial expanding integer map
\[
 A(t)=3t/2\quad(2\mid t),\qquad
 B(t)=(9t+1)/8\quad(t=7\bmod 8).                                  \tag{1}
\]
For \(B\) the intermediate odd value is \((9t-1)/2\). The congruence modulo eight makes it odd and gives exponent 1 at the next step. Conversely an infinite legal path of (1) gives a genuine positive Syracuse survivor from \(6t-1\). The ranges of the two branches are respectively \(3\mid y\) and \(y=8\bmod9\). On these disjoint ranges their inverses are \(2y/3\) and \((8y-1)/9\). Both inverses take a legal positive integer to a positive integer with the required source parity. Thus both time directions in (1) are deterministic where defined.

For a token word \(W\), write \(H=H(W)\) for its sum of dyadic costs \(h_A=1,h_B=3\), and \(V=V(W)\) for its sum of ternary costs \(v_A=1,v_B=2\). Its real slope is \(g_W=3^V/2^H\). Its terminal ternary legality ball \(C_W\) has radius \(3^{-V}\). Its starting dyadic legality ball has radius \(2^{-H}\). Distinct words stopped at a specified precision in either reading direction have disjoint balls, since that direction is deterministic. The affine intercept of \(F_W\) lies in \([0,g_W-1]\). Indeed \(A(t)\ge(3/2)t,\ B(t)\ge(9/8)t\), while \(A(t)+1\le(3/2)(t+1)\) and \(B(t)+1=(9/8)(t+1)\). In particular
\[
                 g_W t_0\le F_W(t_0)<g_W(t_0+1)
                 \quad(t_0\text{ a positive integer}).             \tag{2}
\]

## Two stop rules and their dimensions

A positive integer \(t\) meets the future test at its own height if its deterministic path in (1) can gather \(2^H\ge t\) before the first illegal branch. Let \(D_2\) denote these integers, including \(t=1\) at the empty word. The [stopped cylinder argument](PRINCIPAL_SAFE_TRACE.md) gives
\(\#(D_2\cap[1,X])\ll X^{d_2}\), where
\[
 2^{-d_2}+8^{-d_2}=1,\qquad d_2=0.5514630897\ldots .
\]
Indeed, in \(2^j<t\le2^{j+1}\) stop at the first token with \(H\ge j+1\); the overshoot is at most two bits. Each word determines one residue modulo at least \(2^{j+1}\). The number of words of a specified cost \(H\) is \(O(2^{d_2H})\).

The corresponding backward stop at ternary precision \(3^V\ge t\) uses \(3^{-d_3}+9^{-d_3}=1\), with \(d_3=\log_3((1+\sqrt5)/2)=0.4380178794\ldots\). Both exponents are also the Hausdorff dimensions of the entire respective one-sided compact sets in \(\mathbb Z_2,\mathbb Z_3\). The disjoint stopped balls give covers of bounded critical cost, and assigning weights \(2^{-d_2 h_s}\) or \(3^{-d_3v_s}\) to each letter yields the reverse bound: a ball of prescribed radius in either space meets at most a bounded number of comparable stopped balls. The strict sum \(d_2+d_3<1\) already follows from the rational bounds \(d_2<5/9,d_3<4/9\). For example the defining growth roots are below \(22/15\) and \(13/8\), which are respectively below \(2^{5/9}\) and \(3^{4/9}\).

A positive survivor with fixed source \(t_0\) eventually passes **both** own-height tests at every subsequent state, since (2) implies \(t_n<3^{V_n}\) once \(2^{H_n}\ge t_0+1\). The independent codings do not give independence at an integer. Ordinary digit sets invariant under multiplication on the real circle are different objects. Even the dyadic high digits of the symbolic family contain the exponents' changing units: the infinite word \(A^pB^\infty\) has dyadic source \(-2^p/3^p\). Discarding the initial \(p\) zero bits exposes \(-3^{-p}\), varying with \(p\) through a positive fraction of the odd residue classes at every higher precision.

## A translated Hausdorff estimate and the unshifted ordinary equivalence

Fix \(C>0\). Consider \(\eta\in\mathbb Z_3\) admitting infinitely many token words \(W\) of unbounded length with positive integers \(t\) such that
\[
         t\le Cg_W,\qquad t\in D_2,\qquad t+\eta\in C_W.            \tag{3}
\]
At \(\eta=0\), the condition for some \(C\) is **equivalent** to the existence of a positive ordinary survivor of (1). For the forward implication, the last condition gives a positive ordinary inverse seed using all of \(W\). By (2) that seed is at most \(C\). Among the finitely many candidates, one has legal words of unbounded length. Determinism makes its path infinite. Conversely every actual positive survivor gives (3) along its complete consecutive prefixes and their actual endpoints with \(C=t_0+1\). The forward implication even works without \(t\in D_2\). That extra condition improves the estimate for translations.

For general \(\eta\), the exceptional set in (3) has Hausdorff dimension at most \(d_2\) in \(\mathbb Z_3\). For each fixed word of length \(n\), the count of candidate ordinates is \(O_C(g_W^{d_2})\), and each candidate covers one translate of \(C_W\). The cost at exponent \(s>d_2\), summed over all words of length \(n\), is bounded by
\[
 O_C(1)
 \left((3/2)^{d_2}3^{-s}+(9/8)^{d_2}9^{-s}\right)^n .             \tag{4}
\]
At \(s=d_2\) the bracket equals \(2^{-d_2}+8^{-d_2}=1\). Above it the sum in \(n\) converges. Covering arbitrary tails proves the dimension bound. A countable union over \(C\) preserves it. This excludes Haar-almost every translation while leaving open the specific translation zero.

There is additional rigidity if the \(W_n\) are the nested chronological prefixes of one fixed itinerary with an ordinate \(t_n\) at **every** sufficiently late depth. Put \(p_s=3^{v_s},q_s=2^{h_s}\) and \(c_A=0,c_B=1\), so \(F_s(x)=(p_sx+c_s)/q_s\). The consecutive legality balls give
\[
       q_s t_{n+1}-p_s t_n-c_s=(p_s-q_s)\eta=\eta
                          \pmod{3^{V_{n+1}}}.
\]
Both branches have \(p_s-q_s=1\). The ordinary integers on the left have size \(O_C(g_{W_{n+1}})\). Consecutive ones are congruent modulo \(3^{V_{n+1}}\), and their difference is eventually smaller than that modulus by \(2^{-H_{n+1}}\) and the bounded next slope. They therefore stabilize. It follows that \(\eta\) is an ordinary integer, and \(t_n+\eta\) eventually follows the actual affine recurrence exactly. If these translated states grow without bound, their tail is a positive ordinary survivor. This is a coherence conclusion; the dimension estimate (4) also allows the words and ordinates to change freely from depth to depth.

## Finite unshifted computation

The scan uses **\(\eta=0\) and both own-height tests only**. It imposes no fixed source-cost bound \(C\) from (3). For every integer \(1\le t\le3^{42}=109418989131512359209\) it tests whether the forward and backward paths can accumulate respectively \(2^H\ge t\) and \(3^V\ge t\) before becoming illegal. It finds 23 hits, including the empty tests at 1. Each of the 23 exits (1) at finite future time. The largest hit is \(87225845784394502268\). Its future accumulates 54 ordinary Syracuse departures and 70 shortcut clocks before the next token fails. Passing both finite height probes at this state therefore coexists with an actual finite exit. The computation addresses the compressed states \(t\), not a census of full Collatz convergence.

For example this finite scan independently excludes an infinite (1) path from any \(t_0<2^{41}\). Take the first token with \(2^{H_n}\ge t_0+1\). The previous total \(H_{n-1}\) is at most 40, and \(V_{n-1}\le H_{n-1}\). The last token adds at most two ternary digits, so \(V_n\le42\). Equation (2) makes \(t_n<3^{V_n}\), hence \(t_n\) would be a joint hit at most \(3^{42}\) with an infinite future. All recorded hits exit. This modest range is already below much larger existing general Collatz verification ranges.

For shell \(3^{m-1}<t\le3^m\) the necessary reverse precision is \(V\ge m\). Looking backwards, the first crossing word either totals \(V=m\), or totals \(V=m+1\) with **oldest** letter \(B\). Enumerate these words in chronological order. If an existing terminal class is \(r\bmod Q\), its next two classes are
\[
 \frac{3(r+(r\bmod2)Q)}2 \bmod 3Q,\qquad
 \frac{9(r+jQ)+1}{8}\bmod9Q,\qquad j=-(r+1)Q^{-1}\bmod8 .
\]
Here \(0\le r<Q,\ 0\le j<8\). Both displayed representatives are already in their new least nonnegative interval. A class contributes at most one candidate in its shell. Replaying the future then tests its dyadic half exactly. The largest intermediate forward state for this search fits in 128 unsigned bits: before a tested step the dyadic precision is \(<t\), the overshoot is at most a factor eight, and the real enlargement is at most \((3/2)^{H}\) per \(H\) bits up to the additive unit correction in (2). [Exhaustive checker](safe_diagonal.cpp) · [Independent controls](check_safe_diagonal.py) · [Retained counts](SAFE_DIAGONAL_CONTROLS.json)

Mahler's original \(3/2\) survivor problem and the recent real shadow reduction for a different class of tame Syracuse trajectories give related precedents. The all-clock no-adjacent-twos cone is Weaver's, and PR200's two expanding, ternary-decodable blocks already give arbitrary finite protected integer trajectories. The specific two compressed branches, actual principal trace, translated scale estimate and unshifted two-sided tests here concern the fixed language above. [Mahler](https://doi.org/10.1017/S1446788700005371) · [Paper 168](https://rstation.ai/problems/collatz/papers/168) · [Weaver, Paper 1/v3](https://rstation.ai/problems/collatz/papers/1/v3) · [PR200, actual-word compensation](https://github.com/GettysburgResearch/collatz/blob/07ae08382588992c1b7f7a60cd331a6647177495/research/six-hour-20261127/pointwise/ACTUAL_WORD_COMPENSATION.md)

[SafeDiagonal.lean](SafeDiagonal.lean) kernel-checks the exact integer domains and ranges, the arbitrary-word affine height envelope, the finite-source compactness implication, the principal jump inequality, and the consecutive-congruence equality used for the coherent translation.
