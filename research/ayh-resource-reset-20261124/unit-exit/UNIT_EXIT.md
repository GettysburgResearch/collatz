# A ternary escape law for true tripling disagreements

**Status.** Proposed written theorem with finite exact replay. No random law on a landed endpoint is used. Full Collatz remains open. The sharp octave error below uses the source-qualified PR146 native pair estimate, in addition to the arithmetic checked here. A version without that input is given explicitly.

Use the positive shortcut map \(T(2n)=n,\ T(2n+1)=3n+2\). Let \(f\) be an invariant binary label, and call an odd positive \(x\) a defect if \(f(x)\ne f(3x)\). Write \(D_U(Y)\) for the number of such defects \(x\le Y\) prime to three. For \(X\ge2\), \(1\le Z\le X\) and either prescribed direction of disagreement, every defect in \([X,2X)\), except for
\[
 O\!\left( X Z^{-2/5}/\sqrt{\log(2X)}\right),                 \tag{1}
\]
has an actual unit defect \(y\in[X,CXZ]\) with the **same ordered labels**. These witnesses can be chosen injectively on the octave. The unrestricted count consequently satisfies
\[
 \#\{X\le x<2X:x\text{ is a defect}\}
 \le D_U(CXZ)+O\!\left( X Z^{-2/5}/\sqrt{\log(2X)}\right).
                                                                    \tag{2}
\]
The exponent \(2/5\) in (1)–(2) can be replaced explicitly by \(\sigma=2001/5000\). Omitting the square root gives a version using just the finite arithmetic and combinatorics. Odd nonunit defects whose path never exits to a unit satisfy the stronger all-scale count \(O(X^{1/5})\) up to \(X\).

On geometrically spaced octaves put \(Z=(\log X)^{5/4}\). With the explicit exponent, (1) divided by \(X\) is \(O((\log X)^{-4001/4000})\), which is summable over those octaves. Thus, outside summable original weight, the same directed true disagreement is carried by a unit of height at most \(Cx(\log x)^{5/4}\). The terminal unit is an ordinary source and its label difference is genuine; its two trajectories need not meet. The theorem reduces the mass where the directed discrepancy stays exclusively on nonunits.

## The unique true branch

At an odd multiple \(x=3s\), with \(s\) odd, write \(y_4=16s+1\), \(y_5=32s+1\). The exact physical chain is
\[
 f(x)=f(y_4),\qquad f(3y_4)=f(y_5),\qquad f(3y_5)=f(3x).       \tag{3}
\]
These individual comparisons are the positive-neighbor identities in PR146, `THREE_RAY_WINDOWS.md` at `f431078244e868dc699fad011044f0d5e7f76437`. Indeed \(f(4u+1)=f(3u+1)\); also \(3(16u+1)\) and \(18u+1\) reach \(27u+2\) respectively after four and one clocks. The odd input \(3s\) has the label of \(9s+1\), and \(9s\) the label of \(27s+1\). Combining these gives (3). The all-parameter chain and its binary conclusion are checked in `NonunitExit.lean`.

Because there are exactly two endpoint labels and the outer ones differ, **exactly one** of \(y_4,y_5\) is a defect and its labels in the order \((f(y),f(3y))\) are those at \(x\). Follow it, stopping when it is prime to three. If \(3\mid s\), both candidates are units. Otherwise at most one candidate is nonunit. For a nonunit continuation it must have \(e=4\) when \(s=2\bmod3\), and \(e=5\) when \(s=1\bmod3\). Writing \(x_i=3s_i\), consecutive nonunit steps obey
\[
 x_{i+1}=2^{e_i}x_i/3+1,\qquad
 s_{i+1}=(2^{e_i}s_i+1)/3,\qquad e_i\in\{4,5\}.              \tag{4}
\]
Any finite path must actually satisfy its successive ternary integrality conditions. For a prescribed word of length \(t\) they give exactly one residue for \(s_0\bmod 3^t\): the final numerator has coefficient \(2^{\sum e_i}\), prime to three. Divisibility by \(3^t\) forces each preceding partial numerator to be divisible by its required power of three, by successive reduction modulo three. The choice of digit at each integral step is the unique one that makes the next numerator divisible by three. Each of the \(2^t\) words thus specifies a different residue; the claim does not require that every member of a residue class is a defect. Counting all such residues alone bounds the never-exiting sources by \(O(X^{\log_3 2})\) without the finite filter below.

Both alternatives in (3) grow by a factor greater than \(16/3\). For any odd successor \(y\) its previous odd input is unique: \(e=v_2(y-1)\) and \(x=3(y-1)/2^e\), since \(s\) was odd. Its previous inputs in an entire chain therefore form a sequence decreasing by factors greater than two. At most one lies in \([X,2X)\). This proves the injectivity even when different exits have different depths. Unit starting inputs use themselves as witnesses. They cannot collide with a second source in the same octave by the same growth estimate.

## The binary certificate on an arbitrary segment

Start any segment at an odd nonunit \(x_0\), without information about its high bits. Follow the indicated affine updates also from the rational starting value 1, obtaining a rational \(P_t/D_t\) with \(P_0=D_0=1\) and
\[
 P_{t+1}=2^{e_t}P_t+3D_t,\qquad D_{t+1}=3D_t.
\]
The true value satisfies
\[
 D_t x_t=P_t+2^{E_t}(x_0-1),\qquad E_t=\sum_{i<t}e_i .
\]
Thus \(D_t x_t\) and \(P_t\) agree modulo \(2^{H_t}\) for \(H_t=1+E_t\). On numerators use \(T_D(n)=n/2\) for even \(n\), and \((3n+D)/2\) for odd \(n\), with \(D=D_t\) odd. This commutes with multiplying an ordinary orbit by \(D\). At any \(j\le H_t\), a difference \(2^{H_t}q\) in the starting numerator contributes \(2^{H_t-j}3^{p_j}q\) to its endpoint, where \(p_j\) is the common count of odd steps through \(j\). Consequently an equality
\[
 T_D^j(P_t)=T_D^j(3P_t),\qquad p_j(P_t)=1+p_j(3P_t)
\]
proves that the ordinary \(x_t\) and \(3x_t\) meet at that clock for **every** compatible odd start. Such a word cannot occur on an unbroken defect path. The lift, denominator transfer and all-high-part implication are Lean theorems in the companion module.

Prune words if this happens at any prefix, and keep all unpruned length-22 words. Every contiguous length-22 window in a true path lies in this dictionary: restart the foregoing exact identity at the actual odd input of that window. Overlap is imposed by shifting one digit at a time. In the resulting binary graph the independently reconstructed dictionary has 4,218 vertices and 5,349 edges. The maximum number of 512-step paths beginning at one vertex is
\[
 1320285513209306106119482796965456045622649209648,
\]
whose fifth power is less than \(3^{512}\). Splitting a path into blocks of 512 edges, with its initial word and finite remainder absorbed in a constant, bounds the number of admissible itineraries of length \(t\) by \(C3^{t/5}\). With \(t=\lfloor\log_3 X\rfloor\), each surviving ternary residue contains only \(O(1)\) initial \(s_0\) in the original octave. This proves the asserted \(O(X^{1/5})\) permanent-exception count.

For the additional weight, give digits 4 and 5 rational weights \(652/1000\) and \(860/1000\), respectively. These are both strictly greater than \((2^e/3)^{2/5}/3\); this is an integer fifth-power comparison. The maximum 86-step row sum of the rationally weighted overlap graph is **strictly less than one**, by exact integer iteration. The row sums are outgoing path weights from a prescribed initial vertex. Submultiplicativity, with the starting 22 digits and the at most 85 residual edges bounded separately, now gives
\[
 \sum_{t\ge0}\ \sum_{w\ \mathrm{admissible},\ |w|=t}
       3^{-t} B(w)^{\sigma}<\infty,\qquad
 B(w)=\prod_{e\in w}(2^e/3),                                   \tag{5}
\]
at \(\sigma=2/5\). More explicitly, for \((e,w_e)=(4,652),(5,860)\), the checker verifies
\[
 w_e^{5000}3^{7001}>1000^{5000}2^{2001e}.
\]
Thus these very same rational weights also dominate \((2^e/3)^{2001/5000}/3\), proving (5) at \(\sigma=2001/5000\). In particular this argument does not treat the binary decisions as independent. The two finite row-sum certificates, the integer comparisons and the independent ordinary-modular versus rational-shadow decoder are in `check_nonunit.py`. The combinatorial enumeration is a reproducible finite computation; it was not kernel-replayed in Lean.

## Actual weights at the stopping words

Stop at the first unit or the first product \(B(w)\ge Z\), whichever occurs first. If both occur on the same step, assign the unit as a successful exit. Every exit assigned in this way lies in \([X,CXZ]\). This includes one last jump from a still smaller product, with factor at most \(32/3\): after any word the height is
\[
 B(w)\left(x_0+\sum_{i=1}^{|w|}B(w_{\le i})^{-1}\right),
\]
and the sum of corrections is at most \(3/13\). Otherwise take the first nonunit prefix whose product reaches \(Z\); this is an admissible stopping word. If its length is \(t\), then \(3^t\le 3Z^{\tau}\) where \(\tau=\log3/\log(16/3)<1\). For \(Z=1\) the empty stopping word is allowed. Each class for \(s_0\) contributes \(O(X/3^t)\) possible original sources in the octave, uniformly for \(1\le Z\le X\). Since \(B(w)\ge Z\), (5) bounds their total by \(O(XZ^{-\sigma})\).

For the square-root improvement retain the deficit of the *original* pair \((x_0,3x_0)\) inside each ternary class. Write \(s_0=c+3^t m\); the map \(m\mapsto x_0=3c+3^{t+1}m\) is a permutation on every complete binary residue grid. The positive parameters in the original octave occupy an interval of length \(\asymp X/3^t\), whose logarithm is comparable to \(\log X\) from the preceding bound. Cover by a bounded number of full binary periods at that depth. The finite native tripling-pair failure estimate counts at most \(O(X/(3^t\sqrt{\log X}))\) original sources there. Restricting to odd starts or actual nonunit histories only lowers the count. The native test is made on the unconditioned affine parameter in its own original ternary strip. Summing over stopping words as before proves (1). The PR146 input is the complete-grid bound for \((x,3x)\) at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md`. No conditional law of the actual successor has been imposed.

For reciprocal sums, choose \(Z=(\log X)^{5/4}\). For each unit exit \(y\), its original ancestors over **all** octave scales form one backward chain as long as its predecessors exist. Those assigned to it above satisfy \(1/x\ll (\log y)^{5/4}/y\). Summing reciprocals along this chain costs at most a fixed multiple of its largest reciprocal, by geometric decrease in forward height. Together with the summable discarded original rows this proves
\[
 \sum_{y\text{ odd unit defect}}\frac{(\log(2y))^{5/4}}{y}<\infty
 \quad\Longrightarrow\quad
 \sum_{x\text{ odd defect}}\frac1x<\infty .                      \tag{6}
\]
In (1) and (6) each orientation of the binary disagreement may be treated separately. The constants depend only on the fixed comparisons.

## A single positive source cylinder and what is still open

Apply the previous [four-suffix routing](../crossing-step/FOUR_SUFFIX_ROUTING.md) with \(p=3, a=1, r=57\). It sends every odd unit tripling defect \(y\) into a literal discordant head \(h=81m+57\asymp y\) with bounded multiplicity and the same parent, child color order. One may impose one prescribed row congruence, one fixed open head arc, and any fixed number of initial even steps for the child, as in the preceding periodic schedule. Thus the weighted moment in (6) can be bounded using this **one** true head suffix, with an additional factor \((\log R_j)^{5/4}\) in the original normalized row sum. With the separately source-qualified positive-density input M and the PR146 actual-label variation argument, its convergence forces universal convergence for the basin label. The nonunit escape estimate itself has no density hypothesis.

There is also a conclusion using the published Krasikov–Lagarias predecessor exponent instead of M. PR146's actual-label variation and dyadic-limit argument show that a counterexample forces \(cX^{.84}\) true basin-label tripling defects on an unbounded sequence of odd-parameter octaves (apply the proof to the basin label and its complement, not merely to failed synchronous certificates). Using (2) without the native square root at \(Z=X^{2/5}\), or with \(Z=KX^{2/5}\) for fixed large \(K\), shows
\[
 \limsup_{Y\to\infty}D_U(Y)/Y^{3/5}>0 .
\]
Here \((2/5)^2=.16\) and \(.84/(1+2/5)=.6\). The explicit pressure exponent alone improves the power to \(42021/70025>3/5\): take \(Z=KX^{800/2001}\). With the native factor in (1), the simpler choice \(Z=KX^{2/5}/(\log X)^{5/4}\), followed by sufficiently large fixed \(K\), gives \(\limsup_Y D_U(Y)/(Y^{3/5}(\log Y)^{3/4})>0\). The corresponding fixed-power lower bound transfers to the single scheduled suffix on an unbounded sequence of rows: otherwise summing the little-o bounds over geometric rows through the routed cutoff would contradict it. In particular, eventual absence of actual defects just at this one scheduled suffix would settle Collatz without M, already from the elementary \(\log_3 2<.84\) census before the finite filter. Under M, (2) also shows that any fixed power saving on the unit count would give a fixed power saving on all odd tripling defects, hence universal convergence; take \(Z=X^\epsilon\) with \(\epsilon>0\) small compared with the specified saving.

No argument here bounds the actual unit-defect series in (6), proves that its routed heads cross, or rules out every individual indefinitely continuing nonunit integer. The strict loss and the finite tests concern the explicit nonunit-only continuation.
