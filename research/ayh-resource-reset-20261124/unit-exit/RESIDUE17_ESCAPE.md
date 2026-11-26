# A second escape law localizes the remaining unit direction to 17 modulo 48

**Written theorem with finite exact replay.** Let \(f\) be a binary label constant along each positive ordinary shortcut orbit. Write \(D_1(I)\) for the number of \(x\in I\) with \(x=1\bmod16\) and \(f(x)\ne f(3x)\). Let \(D_{17}(I)\) count just \(x=17\bmod48\). With \(\sigma=200/3599>1/18\), for \(2\le X,\ 1\le Z\le X^{1/10}\),
\[
 D_1([X,2X))\ \le\ 3 D_{17}([X,CXZ])
       + O\bigl(XZ^{-\sigma}/\sqrt{\log(2X)}\bigr).                \tag{1}
\]
The estimate also holds in each prescribed ordered direction. The escaped witnesses carry the same ordered pair of labels. The positive integer defects in this input class that never escape number \(O(X^{93/100})\) up to \(X\). The square-root factor invokes the complete-grid tripling-pair input of PR146. All other losses use counting on the actual original integers.

## Genuine exchanges and their stopping rule

For \(x\equiv1\bmod16,\ x>1\), stop if \(x\equiv2\bmod3\), exactly the target \(17\bmod48\). If \(x\equiv1\bmod3\), move to \(y=(4x-1)/3\), keeping both labels in order. Indeed \(T(y)=2x\), while the three labels at \(3y=4x-1,\ 6x-1,\ 6x\) coincide by the ordinary odd-step exchange and the same-clock adjacent merger at \(6x=96m+6\). This exchange is in PR146, THREE_RAY_ONE_RESIDUE.md, at commit f431078244e868dc699fad011044f0d5e7f76437, blob 3d4d195b0e1e767e02dc4c32111f9f96e39d6468. If \(3\mid x\), move to the unique actual defect among \(16x/3+1,\ 32x/3+1\), as in [UNIT_EXIT.md](UNIT_EXIT.md). Each new input is again \(1\bmod16\), and its two labels in order are those of its predecessor. The choice uses the existing labels. The sole positive input in this class below 17 is 1, whose tripling pair has a common visit to 1.

These are three affine letters
\[
 F_e(x)=(2^e x+b_e)/3,\qquad
 (e,b_e)=(2,-1),(4,3),(5,3).
\]
The exponent of two in \(y-1\) determines the entire previous step. The values 4 and 5 signify those letters and return \(3(y-1)/2^e\), whereas an exponent of at least 6 signifies letter 2 and returns \((3y+1)/4\). Every step grows by a factor of at least \((4-1/17)/3\), whose cube exceeds 2. Hence at most three sources from one octave can share an exit across all stopping depths, including the exit itself. Along one backward chain over every octave the reciprocals grow geometrically.

## Simultaneous constraints on the same source

Every word of \(t\) letters requires at most one residue for \(x_0\bmod3^t\), by the unit coefficient \(2^{\sum e}\) in the composed numerator. This upper bound allows different words to specify the same residue. The original class \(x_0\equiv1\bmod16\) independently supplies 4 binary bits. Starting from shadow \(P/D=1\), propagate
\[
 P'=2^eP+b_eD,\qquad D'=3D.
\]
At the end \(Dx_t=P+2^{\sum e}(x_0-1)\). Thus \(x_t\equiv P/D\bmod 2^{4+\sum e}\). At this precision a same-clock ordinary merger of the shadow tripling pair with the homogeneous odd-count difference one implies an actual merger at every positive lift, by [UNIT_EXIT.md](UNIT_EXIT.md). Each contiguous segment may restart this comparison at its own actual \(1\bmod16\) input. For a small hand check the word \(4,4,5\) gives \(x_t=10081\bmod2^{17}\). The ordinary starts \(10081,30243\) both reach 1010 at clock 16, with odd counts 8 and 7. Thus this word is impossible anywhere on an unbroken defect path.

The file [check_residue17.py](check_residue17.py) reconstructs the entire nine-letter dictionary independently by rational-numerator and ordinary modular replay. It checks 12,969 vertices and 35,778 one-digit overlaps. The maximum 96-step outgoing walk count is \(2777580184767497805179551250248269312150842\). Its hundredth power is less than \(3^{96\cdot93}\). Multiplication of blocks gives at most \(C3^{.93t}\) length-\(t\) admissible words. At \(t=\lfloor\log_3 X\rfloor\) each ternary class has bounded occupancy up to \(X\), proving the permanent-exception bound. The two decoders and row counts use exact finite Python arithmetic. The two ordinary exchange identities for all positive inputs in their respective classes are kernel-checked in [UnitResidueExchange.lean](UnitResidueExchange.lean).

Give letters integer weights \(w=(3388,3659,3802)\), divided by 10000. The inequalities \(3^{19}w_e^{18}>10000^{18}2^e\) give strict domination of \(3^{-1}(2^e/3)^{1/18}\). The maximum 34-step weighted row sum is strictly less than one. The checker also verifies \(w_e^{3599}3^{3799}>10000^{3599}2^{200e}\) for each letter, yielding the explicit \(\sigma=200/3599>1/18\). Splitting overlap walks into blocks of 34 edges and absorbing the initial word and bounded remainder gives
\[
 \sum_{t\ge0}\sum_{|w|=t,\ w\ {\rm admissible}}3^{-t}B(w)^\sigma<\infty,
 \qquad B(w)=\prod_{e\in w}(2^e/3).
\]

Stop at the first actual target or the first prefix with \(B(w)\ge Z\). Count a simultaneous target as a success. Since \(B\) grows by at least \(4/3\) per letter and the individual additive corrections have magnitude at most 1, the actual height is bounded by \(B(w)(x_0+3)\). At a target the overshoot \(B(w)\le(32/3)Z\) gives the upper height in (1). Otherwise there is an admissible stopping prefix with \(B(w)\ge Z\), of length \(t\le1+\log Z/\log(4/3)\). Thus \(3^t\le3Z^4\le3X^{2/5}\). Its original ternary residue contains \(O(X/3^t)\) sources in the octave. Write \(x_0=a+3^t m\) on that residue. Since its coefficient is odd the positive interval of \(m\) dominates full binary-grid tests through a clock comparable to \(\log X\), with bounded period-cover cost. Dropping the \(1\bmod16\) restriction here only enlarges the upper bound. Any actual defect must fail the native original tripling comparison on this grid, which gives the additional uniform factor \(O(1/\sqrt{\log X})\). The weighted word sum and bounded witness multiplicity prove (1).

## Consequences of the localized bound

Take \(Z=(\log X)^9\) above a fixed threshold. The discarded measures after division by \(X\) are summable on dyadic rows because \(9\sigma+1/2>1\). For one actual exit \(y\), its assigned sources have \(1/x\ll(\log(2y))^9/y\). The sum along its backward chain is a constant multiple of the largest such reciprocal. Hence
\[
 \sum_{y=17\bmod48,\ f(y)\ne f(3y)}
      \frac{(\log(2y))^9}{y}<\infty
 \quad\Longrightarrow\quad
 \sum_{x=1\bmod16,\ f(x)\ne f(3x)}\frac1x<\infty .
\]
PR146's bounded-size, bounded-multiplicity reduction \(D(X)\le C D_1(C'X)\), established in the pinned one-residue source above for all odd defects, transfers this to all odd inputs by partial summation. Thus, **under the separately source-qualified fixed-target positive-density premise M**, this single unit class weighted estimate implies universal convergence for the basin label. Any fixed power saving \(D_{17}([1,Y])=O(Y^{1-\delta})\) would likewise suffice by (1) with \(Z=X^\epsilon\) and small \(\epsilon>0\). The source escape bound itself has no density premise.

There is a descending alternative description of the remaining class. For \(x=48t+17\) put \(y=(2x-1)/3=32t+11\). The ordinary odd steps give \(T(y)=x,\ T(3y)=3x-1\). Since \(3x=16m+3\), the two starts \(3x-1,3x\) reach \(9m+2\) in four steps. Thus \((f(y),f(3y))=(f(x),f(3x))\), exactly and unconditionally. This bijection transfers counts and logarithmic reciprocal moments to \(11\bmod32\), with bounded scaling constants. A single exchange lowers the source by a factor smaller than \(2/3\).

The exponent \(0.93\) exceeds the classical predecessor threshold \(0.84\), so the permanent-exception count for this finer class does not yield an unconditional counterexample obstruction there. Its actual unit moment and indefinite strict descent remain open.
