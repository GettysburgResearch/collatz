# A sharp native gate deadline separates escape from every periodic component

Use natural logarithms and write \(D=\log(4/3)\), \(\mu=2/D\), \(\lambda=\log3/D\), \(\ell_X=\sqrt{2\log X/D}\). A true gate is an ordinary \(n\) with \(b_t(n)=2Q_t(n)-t>0\) for every positive shortcut date. Sample uniformly from these gates in \([X,2X)\). For each integer \(a\ge1\), let \(S_a\) be the native date of the \(a\)-th subsequent gate, set to \(+\infty\) if it is never reached. Test the deterministic deadline
\[
 H(X,a)=\left\lceil\mu\log(2X)+\lambda a+70000\right\rceil .
\]
Let \(d_\infty\) be the ordinary natural density of the union of all escaping components. Under the same physical first-hit and gate-sampling inputs as the [eventual-return law](../mass/SUPERCRITICAL_TRUE_GATE_RETURNS.md),
\[
 \lim_{X\to\infty}\Pr(S_a\le H(X,a))=
 \begin{cases}
 d_\infty+(1-d_\infty)e^{-t^2/2},& a/\ell_X\to t\in[0,\infty),\\
 d_\infty,&a/\ell_X\to\infty .
 \end{cases}                                                        \tag{1}
\]
Here the growing regime has no upper restriction on \(a\). The deterministic implication underlying (1) applies to **every individual escaping gate at every \(a\)**. The number 70000 is a conservative universal additive constant. The time coefficient \(\lambda\) is the reciprocal of the zero-height-drift gate frequency in native time. The source interval and the deadline are deterministic. Membership is decidable by the finite parity-record horizon. Testing for \(a\) returns by this deadline, including all gate-membership lookaheads, uses \(O(\log(2X)+a)\) actual shortcuts.

The eventual-return test at the same \(a\) has limit \(1-d_1(1-e^{-t^2/2})\), where \(d_1\) is the basin density of one. Thus the fraction completing the returns **after** this deadline has limit \((1-d_1-d_\infty)(1-e^{-t^2/2})\), with \(e^{-t^2/2}=0\) in the growing regime. These two real native observables distinguish the total mass of positive nontrivial cycles from the total mass of escape. Earlier source work already separated the fates through the affine correction. This comparison instead tests an ordinary successive-return clock at a specific deterministic boundary. [Prior critical affine-correction separation, PR215](https://github.com/GettysburgResearch/collatz/blob/8a50018b6a861e810b18512fdd59aaf45214bba1/research/astra-nine-hour-20261128/escape/CRITICAL_CORRECTION.md)

## A uniform sourcewise bound on every simple completed trace

For any shortcut segment \(n\to y\) of \(s\) departures with \(q\) odd ones set
\[
 E_s=\sum_{i<s:\,T^i n\ {\rm odd}}\log(1+1/(3T^i n)).
\]
The exact product gives
\[
  s=\mu\log(n/y)+\lambda b_s(n)+\mu E_s .                         \tag{2}
\]
For a completed \(a\)-return segment both endpoints are gates and \(b_s=a\), by the suffix-minimum cocycle. In particular intermediate gate meetings are included with their actual multiplicity. On every finite segment of distinct departed states, \(E_s<10000\), uniformly in its source and length. Here are explicit details for that loose bound.

For the dyadic octave \([2^m,2^{m+1})\) with integer \(m\ge16\), its \(2^m\) representatives give every \(m\)-bit word exactly once. At most \(2^m e^{-m/200}\) of them have at least \(0.55m\) odd letters by the binomial Chernoff bound. Each other start visits below \(F=2^{.99m}\) within \(m\) departures. Indeed otherwise its final height is at most \(2(3+F^{-1})^{.55m}<2^{1+.88m}<F\), using \(3+F^{-1}<2^{1.6}\). Along a segment of distinct states the starts with \(m\) available subsequent departed states inject into pairs of a lower state and a clock offset from 1 to \(m\). There are at most \(m(F+1)\) such pairs. The up to \(m\) terminal starts without that window cost at most \(m\) more. Dividing counts by \(2^m\), the reciprocal sum over that octave is at most \(e^{-m/200}+m2^{-.01m}+2m2^{-m}\). Earlier octaves cost at most 16 in total. The geometric sums satisfy \((1-e^{-1/200})^{-1}<201\) and \((1-2^{-.01})^{-1}<160\). Hence the total reciprocal sum is below 30000, even restricting the segment only at its final departure. Dividing by three bounds \(E_s\). The packing mechanism is established prior work. [Weaver 176, §5.1](https://rstation.ai/problems/collatz/papers/176) · [Parity cocycle, record horizon, and simple-path occupation](../cycles/RARE_ODD_ASCENTS.md)

Any positive escape has pairwise distinct states and infinitely many future gates. So (2), \(y\ge1\), \(n<2X\), \(\mu<7\) give \(S_a\le H(X,a)\) at every \(a\). A terminating gate also meets this deadline whenever it completes the requested returns: all departures through its last gate precede the first hit of one and are distinct. More generally all completions on a simple initial segment pass the same audit. A periodic continuation can accumulate further positive affine correction after the first repeat; its rate is computed below. The stated lookahead bound follows because every state through \(H\) is at most \((3/2)^H(2X+1)\), and each gate test requires \(O(\log(2x))\) further shortcuts at state \(x\).

## Gate count and clock on first entry into a fixed periodic orbit

Fix a positive cycle \(C\) and use a single odd ternary unit \(c\) on it, with first native arrival date \(\tau\) from the sampled gate. Its basin is the entire component. Write \(g=-\min_{s\ge0}b_s\) and \(G=\sum_{i<\tau}1_{\mathcal P}(T^i n)\). For \(n\) a gate, the cocycle gives \(b_\tau=G+g(c)\). The segment up to \(\tau\) has no repeated departed state: repetition would force periodicity before first hitting \(c\), and on this cycle no state can repeat before meeting \(c\). By (2), uniformly in these starts on the octave,
\[
                 \tau=\mu\log X+\lambda G+O_c(1).                    \tag{3}
\]

Under sampling from the true gates of this fixed basin,
\[
                    G/\ell_X\ \Rightarrow\ R,\qquad
                    \Pr(R>z)=e^{-z^2/2}\quad(z\ge0).                 \tag{4}
\]
To check the extension of the previously proved \(c=1\) Rayleigh law, use the incoming functional first-hit law on \(B_c\). For an ordinary physical output \(y\in B_c\), its mark pair is \(g(y), b_{\tau_c(y)}(y)\). The actual future floor differs by at most the fixed \(g(c)\) from the minimum of its incoming path through the hit. Hence these jointly scale to \(-\min B,B(1)\) for one standard Brownian motion. Fixed-shift merging changes the two premerger native counts by \(o(\sqrt{\log Y})\) at the physical output scale outside a vanishing fraction. A fixed-target label discrepancy requires an early visit to \(c\), negligible by the counted merger argument. Thus the pair has the same joint limit on fixed congruence classes. Both marginals are continuous, so the joint rectangular comparisons are uniform in their two thresholds. The physical transfer weights this test by the coarse \(\rho_m\) using its Haar \(L^1\) approximation by fixed trit depth. In the sharp-gate three-block proof both the future-floor test and the terminal-surplus threshold apply to this same \(y\). The initial short positive-ballot block supplies the explicit probability \(p\asymp(\log X)^{-1/2}\) before the middle-column approximation. Its test errors are \(o(p)\) on the full octave. The terminal Brownian segment then supplies the negative minimum and the final value jointly as in the terminating-basin proof. This gives the Rayleigh endpoint of the fair geometric walk conditioned to stay positive. The fixed \(g(c)\) changes \(b_\tau/\ell_X\) to \(G/\ell_X\) by \(o(1)\). [Physical incoming functional law](../mass/TRUE_GATE_SOURCE_LAW.md) · [Rare gate-conditioned transfer](../mass/SUPERCRITICAL_TRUE_GATE_RETURNS.md) · [Full pair-marked column and physical comparison](../mass/SHARP_TRUE_GATE_SAMPLING.md)

Let a nontrivial cycle have \(p\) odd and \(s\) total native departures per primitive lap. The true number of gate departures per lap is \(2p-s\) by the cocycle. All its odd values are at least three. The height product round the lap gives
\[
             3^p<2^s\le(10/3)^p<4^p.
\]
Its gate rate \(r=(2p-s)/s\) therefore satisfies \(0<r<1/\lambda\). From the fixed waypoint \(c\), counting any initial partial lap and any number of further complete laps shows that the \(j\)-th subsequent gated occurrence has native delay \(j/r+O_c(1)\). Consequently for \(a\ge G\),
\[
                 S_a=\tau+(a-G)/r+O_c(1)
                     =\mu\log X+\lambda a+
                       (1/r-\lambda)(a-G)+O_c(1).                    \tag{5}
\]
This indexing allows \(c\) itself to be a gate: when \(a=G\) the bounded final piece can have zero duration. For \(a<G\) the \(a\)-th subsequent gate occurs strictly before \(\tau\), with a simple prefix, and passes the deadline. By (5), in this component the deadline event is sandwiched between \(G>a\) and \(G\ge a-C_c\) for a fixed \(C_c\), uniformly in \(X,a\). On the cycle of one the exact condition is \(a<G\), since one and two are both outside the gate. In both cases (4) and continuity give limit \(e^{-t^2/2}\) when \(a/\ell_X\to t<\infty\), and tightness gives zero when \(a/\ell_X\to\infty\). No uniform cycle-specific incoming law or uniform cycle-period bound is required.

Finally the ordinary gate sampler converges in total variation on the countably many component labels. Each of them has the previously established positive natural density. Escape components pass deterministically as a union, and an arbitrarily large finite collection of cycle components approximates their total mass, with the omitted sampling mass small by total variation. This proves (1), including all increasing sequences in its supercritical regime. The sharp probability comparison is source-qualified. The per-integer escape deadline and the cycle-rate gap use only the actual map. Proving a vanishing upper bound on this deadline event at \(a/\ell_X\to\infty\) would exclude every positive escape by component positivity.

[Finite native power gap and positive cycle grade](NativeCycleGrade.lean) formalizes the two strict cycle inequalities before taking logarithms. The uniform simple-path packing estimate, source transfer, and limiting deadline law remain written mathematics.
