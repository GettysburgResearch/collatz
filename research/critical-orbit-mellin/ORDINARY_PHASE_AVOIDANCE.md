# Ordinary orbits leave every finite collection of deep rational ternary neighborhoods

**PROPOSED.** Fix a nonempty finite set \(F\) of rational ternary units. There is an effectively computable \(C_F\) with the following property. Starting at any sufficiently large positive odd integer \(x\), among the first \(\log_2(x+1)+O_F(1)\) odd steps, including the start, there is a state \(y\) satisfying
\[
        \max_{r\in F} v_3(y-r)\le C_F\log(2+\log x).                  \tag{1}
\]
Here \(v_3(0)=+\infty\). Both negative rational cycles and their positive rational forward images can be included in \(F\). The theorem concerns an actual single ordinary orbit. It allows visits of much greater precision at other times.

Let \(H\) be the largest absolute numerator or denominator of the reduced elements of \(F\), enlarged to at least two. Put \(m=1+\lceil\log_2((x+1)H^2)\rceil\), \(y_i=U^i(x)\) and \(a_i=v_2(3y_i+1)\). As \(y_i+1\le(3/2)^i(x+1)\), all \(a_i\ll_F 1+\log x\) on this interval. For every ordered pair \(r,s\in F\), whenever \(2^a s\ne3r+1\), Yu's rational \(p\)-adic logarithm bound yields
\[
               v_3(2^a s-(3r+1))\ll_F\log(2+a).                     \tag{2}
\]
Apply it at \(p=3\) to \(2^a[s/(3r+1)]-1\). Both rational bases are ternary units. Since \(3r+1\) is a ternary unit, its removed factor does not change the valuation. The bound allows multiplicatively dependent bases provided the product being compared is different from one. The two-base constant can be maximized over the given finite set. [Yu's bound in rational form, Evertse, Theorem 1.10](https://www.math.leidenuniv.nl/~evertsejh/dio2011-linforms.pdf) · [Yu, p-adic logarithmic forms](https://doi.org/10.1515/forum.2007.009)

Suppose every \(y_i\), \(0\le i\le m\), were closer than (1) allows to some \(r_i\in F\). The equation \(2^{a_i}y_{i+1}=3y_i+1\) gives the same high divisibility at \(2^{a_i}r_{i+1}-(3r_i+1)\). By (2) this difference must be zero at every step. The two exactly parallel rational trajectories then satisfy
\[
             y_m-r_m=3^m2^{-A_m}(x-r_0),\qquad A_m=\sum_{i<m}a_i.
\]
The starting difference is nonzero for \(x>H\) and has binary valuation at most \(\log_2((x+1)H)\), by clearing the denominator. The ending difference has binary valuation at least \(-\log_2 H\), since \(y_m\) is ordinary. Hence \(A_m\le\log_2((x+1)H^2)<m\), contradicting \(a_i\ge1\). This proves (1). For \(F=\{-1\}\) the local estimate needs only lifting the exponent in \(2^a-2\).

## What this removes from the escape test

Suppose an escaping ordinary orbit carries a nonnegative statistic \(K(y)\ge c\log y\) at every sufficiently late state, for a fixed \(c>0\). It then has a sequence of states \(t_k\to\infty\) with the same lower bound and
\[
                v_3(t_k-r)=o(\log t_k)\quad
                \text{for every fixed rational ternary unit }r.       \tag{3}
\]
Indeed list the countably many rationals and apply (1) to successively larger finite initial sets. Start each interval at an arbitrarily large minimum of a forward tail of the orbit, so all the subsequent states in the interval are at least the starting value. The minima tend to infinity on an escaping positive orbit. The starting value can be chosen large enough that the upper bound in (1) is at most \((\log x)/k\).

For the canonical unnormalized inverse real fibre \(G_y\) (normalized to have total mass \(\lim_q g_q(y)\)), take \(K(y)=\int(1+B)^{-1}G_y(dB)\). The compact side branches of an escaping orbit give the required positive logarithmic lower bound. To see the mechanism, start at a fixed odd unit on that spine and write its successive states as \(y_i\). For every \(i<j\), use a unit sibling \(s_i=4y_i+1\) or \(16y_i+5\) with the same next state and retain its uniform positive reservoir at bounded real offset. These are disjoint first departures on reversed paths from \(y_j\), since later reversal along the original spine is prescribed. Along the remaining segment the homogeneous multiplier is comparable to \(y_j/y_i\) by the simple-orbit reciprocal bound. Its inherited offset is at most a constant times \(y_j\sum_{k=i}^j 1/y_k\) by the positive affine product identity. Consequently the \(i\)-th reservoir contributes at least a fixed multiple of \((1/y_i)/(\sum_{k=i}^j 1/y_k)\) to \(K(y_j)\). The adjacent suffix sums have bounded ratios since \(y_{i+1}\le(3y_i+1)/2\). Summing this lower bound is therefore comparable from below to the logarithm of the ratio between the first and last suffix sums, at least \(\log y_j-O(1)\). [Bounded-offset reservoir](../terminal-residue/ENDPOINT_ODOMETER.md) · [Simple-orbit distortion](../integrated/orbitwise-boundaries/README.md)

For comparison, \(K(t)\) can have logarithmic size on ordinary integers \(t=2\cdot3^k-1\). The long initial reverse sequence of ones admits a distinct unit departure at each of its first \(k-O(1)\) levels. Its multiplier and inherited real offset are both comparable to \((3/2)^i\), so the bounded reservoir at each departure contributes at least a constant to \(K(t)\). Property (3) excludes this example and every analogous polynomially precise approach to a fixed rational phase on the required sequence. The following construction disproves the corresponding upper bound on arbitrary sequences satisfying (3).

## Large values at every prescribed ternary phase

In fact, **for every ternary unit** \(\alpha\), there are positive odd integers \(t_q\to\alpha\) in the ternary topology with \(t_q\to\infty\) in ordinary size and \(K(t_q)\gg\log t_q\). In particular when \(\alpha\) is irrational, \(v_3(t_q-r)\) eventually equals the finite value \(v_3(\alpha-r)\) for each fixed rational unit \(r\). The implied lower constant is independent of \(\alpha\).

To verify this, let \(d=\lfloor q/32\rfloor\). Choose a legal reverse word of length \(d\) at \(\alpha\) keeping every inverse state a unit and every exponent at most four. At each step two exponents of the required parity differing by two are available among the first four. If the smaller yields a multiple of three, its alternative yields four times that state plus one. In forward order use the reversed word \(w\). It carries every ternary origin into the class of \(\alpha\) modulo \(3^d\). For the dyadic condition choose an ordinary odd \(n\) realizing \(w\) and satisfying \(n\equiv-1\pmod{3^q}\). The Chinese remainder theorem permits taking \(P\le n<2P\), with \(P=3^q2^{1+A(w)}\). The same construction allows appending any prescribed word with letters at most four, provided the total number of prescribed letters is at most \(q/16\).

At this actual \(n\) there is a legal inverse word consisting of \(q\) ones. Its forward affine offset is \((3/2)^q-1\). For every subsequent target on the prescribed segment the same incoming word, extended along the actual orbit, has offset at least
\[
                 2^{-q/4}((3/2)^q-1).
\]
Indeed its extra forward multiplier is at least \(2^{-A}\) with \(A\le q/4\), and all added offsets are nonnegative. The targetwise [real-fibre lower bound](STIELTJES_ESCAPE_FLOOR.md) gives \(K(y)\gg q\) at every such target. Their ordinary logarithmic heights are comparable to \(q\): the lower bound follows from \(y\ge 2^{-A}n\ge3^q\) and the upper bound from \(y+1\le(3/2)^{q/16}(n+1)\). The end of the first \(d\) letters supplies \(t_q\).

### A growing ordinary segment also avoids low-height rationals

Fix \(A_0>0\). There are actual positive odd trajectories with a segment of at least \(c\log y\) odd steps starting at \(y\to\infty\) such that at **every** state \(z\) of the segment
\[
 K(z)\gg\log z,\qquad z\ge y,\qquad
 \max_{\substack{r\text{ rational ternary unit}\\
             H(r)\le(\log y)^{A_0}}}v_3(z-r)\ll_{A_0}\log\log y,      \tag{4}
\]
where the rational height is the maximum absolute numerator or denominator in lowest terms. The number of steps and lower trace constant can be chosen independently of \(A_0\).

Use the same CRT construction, now selecting \(2d\) independent fair forward letters from \(\{1,2\}\) and using the last \(d\) steps as the segment. For \(i\ge d\) and \(k\le d\), the last \(k\) letters determine the target modulo \(3^k\), and any specified residue has probability at most \(2^{-k}\). Indeed the residue modulo three determines the last letter uniquely in this alphabet. Undoing that letter and reducing the precision by one recovers the others. This argument applies to the finite word distribution even though its ordinary CRT representative depends on the entire word.

There are \(O(q^{2A_0+2})\) rationals of height at most \((Cq)^{A_0}\), for an absolute \(C\) bounding all logarithmic heights above. A union bound over these rationals and the \(d+1\) times excludes a match modulo \(3^k\) with probability tending to one when \(k=\lceil (2A_0+6)\log_2 q\rceil\). Meanwhile the homogeneous forward multiplier throughout the last segment stays at least one with probability bounded below independently of \(d\). The iid logarithmic increments have mean \(\log3-\tfrac32\log2>0\). For small \(\theta>0\), the negative exponential of their partial sums with parameter \(\theta\) is a supermartingale. Starting with a fixed initial string of ones builds a positive buffer, after which its maximal inequality bounds the probability of losing the buffer by a constant strictly less than one. These two requirements therefore hold simultaneously for some word. Positive affine offsets give \(z\ge y\), and the preceding offset and height bounds give (4).

This refutes a pointwise sublogarithmic trace bound even after excluding very good approximations to every fixed rational shadow. It also explains why a growing finite run with high trace, forward growth and avoidance of rational phases can be witnessed unconditionally. The starting integers vary with the horizon. Establishing or excluding persistence on one fixed positive trajectory remains open.

An [integer replay](check_phase_avoidance.py) constructs a target in the class of the ternary square root of 10 modulo \(3^{64}\). Its separate trajectory fixture checks the exact incoming-offset inequality at 65 consecutive ordinary states and tests all 2,506 distinct residues of rational units of height at most 64 at the stated precision. The infinite canonical trace lower bound uses the analytic fibre theorem.

## Prescribing the subsequent ordinary destination

**Additional source-qualified conclusion.** The preceding large-trace examples can all be chosen in the basin of **any fixed positive odd ternary unit** \(b\). In particular every prescribed initial ternary phase and every finite segment in (4) can occur on an orbit subsequently reaching 1. For the constructed trajectories that subsequent visit costs only \(O_b(\log y)\) shortcut steps. This version uses the modular inverse-routing theorem, which supplies a bounded cost as the prescribed precision grows. [Modular inverse routing, Theorem 8 and (80)–(82)](https://rstation.ai/problems/collatz/papers/48/v2)

For a chosen chronological word \(w\) of length \(m\le q/16\) from either construction, prescribe the final unit class
\[
                    u\equiv F_w(-1)\pmod{3^{q+m}} .
\]
Its denominator is a power of two, and the last forward step makes it a ternary unit. Routing backwards from \(b\) gives a positive odd integer \(u\) in this class that goes forward to \(b\) with total valuation at most \(C(q+m+1)\). Hence \(u\le 2^{C(q+m+1)}b\). Now apply the reversed word from \(u\). Each step is integral by the chosen congruence and positive since it starts from a positive odd target. Its initial source \(n\) satisfies \(n\equiv-1\pmod{3^q}\): the inverse composition divides the difference from the reference by \(3^m\) and multiplies by a power of two. The resulting ordinary forward trajectory realizes every chosen letter to \(u\), then reaches \(b\).

Here \(3^q-1\le n\le 2^{A(w)}u\), and every state on the displayed word is at least \(2^{-q/4}n\). Its logarithmic height is again comparable to \(q\) for sufficiently large \(q\) at fixed \(b\). The original incoming ones, the large offsets, and all ternary observations survive the extra routing. The finite destination certificate is an existence consequence of the cited routing theorem; the preceding integer replay checks the direct CRT version. Earlier work already used CRT to prescribe forward letters after a peak in a different first-landing statistic. [First-landing peaks and prescribed words, Section 14](https://rstation.ai/problems/collatz/papers/12/v1)
