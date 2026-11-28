# The height boundary of the finite ternary harmonic densities

**Written result.** Even before taking a pointwise harmonic limit, the physical height cutoff has a term linear in the time. If an escaping component \(C\) of density \(d_C\) existed, its coefficient in (4) below would be strictly positive under the indicated source inputs. A termwise depth/height exchange that drops this boundary would fail. The identities use the actual shortcut map; they never identify a sampled ordinary integer with a generic ternary point.

Put \(\kappa_0=\log2-\tfrac12\log3\) in natural logarithms and let \(T\) be the shortcut map. For \(x>0\) set
\[
 A_t(x)=3^{Q_t(x)}2^{-t},\quad
 R_t(x)=\frac{T^tx}{A_t(x)x}
       =\prod_{\substack{0\le j<t\\T^j x\ {\rm odd}}}\left(1+\frac1{3T^jx}\right).
\]
Define the finite-depth ternary densities on positive integers by \(H_0=1\) and
\[
 H_{t+1}(y)=\tfrac12 H_t(2y)+\tfrac32\,1_{\{y\equiv2\ (3)\}}H_t((2y-1)/3).
\]
The latter term is evaluated only on its indicated class. The function \(H_t\) is periodic modulo \(3^t\), of period mean one. This follows from the fixed parity-word formula \(H_t(y)=\sum_{w}2^{-t}3^{|w|}1_{y\equiv B_w\pmod{3^{|w|}}}\). A legal inverse word at a positive ordinary endpoint remains positive under all legal inverse steps. Thus
\[
 H_t(y)/y=\sum_{x:T^t x=y} \frac1{xR_t(x)}.                         \tag{1}
\]

Let \(C\) be any invariant subset \(1_C(Tx)=1_C(x)\) with natural density \(d_C\). Each fixed binary residue class \(w\bmod 2^t\) then has joint density \(2^{-t}d_C\) with \(C\), under the source result that consecutive ordinary integers coalesce on a set of density one: every fixed shift preserves \(C\) outside a density-zero set, giving equal densities of the finitely many classes by comparison of their counts. For \(C=\mathbf N_{>0}\) this independence is elementary. [Omar Javier Said Duran, density-one coalescence, author-reported formal verification](https://doi.org/10.5281/zenodo.23003524)

For fixed \(t\), the following physical increasing-height series converges:
\[
 B_t(C)=\lim_{Y\to\infty}\ \sum_{\substack{y\le Y\\y\in C}}
                  \frac{H_t(y)-1}{y}
       = t\kappa_0d_C-\sum_{x\in C}\frac{1-R_t(x)^{-1}}x.           \tag{2}
\]
Indeed reindex (1) at that finite cutoff. The correction part is absolutely summable at fixed \(t\), since \(T^j x\ge 2^{-j}x\) implies
\(0\le1-R_t^{-1}\le\log R_t\le(2^t-1)/(3x)\).
For a fixed true word \(w\), the other part compares reciprocal weights on \(x\le(Y-B_w)/A_w\) and \(x\le Y\), where \(T^t x=A_wx+B_w\). By its class density and partial summation, this difference tends to \(-2^{-t}d_C\log A_w\). Summing gives (2). The correction has the exact positive expansion
\[
 \sum_{x\in C}\frac{1-R_t(x)^{-1}}x
 =\sum_{s<t}\sum_{\substack{y\in C\\y\ {\rm odd}}}
                     \frac{H_s(y)}{y(3y+1)}.                        \tag{3}
\]
Telescope each reciprocal product and group by its actual \(s\)-step endpoint. All terms in (3) are nonnegative.

If \(C\) is an escaping component, every one of its prefixes is simple and above the verified \(2^{68}\) floor. The high-simple-segment estimate gives \(\log R_t\le b=0.21645\) uniformly. The correction on \(x\le2^t\) in (2) is at most \((1-e^{-b})\sum_{x\le 2^t,\,x\in C}1/x\); the remaining correction is \(O(1)\), using \((2^t-1)/(3x)\) and all integers. Natural density gives
\[
 \liminf_{t\to\infty}\frac{B_t(C)}t
 \ \ge\ [\,\kappa_0-(1-e^{-b})\log2\,]\,d_C
 \ > 0.008\,d_C .                                                  \tag{4}
\]
The numerical sign uses only the displayed value of \(b\). The external simple-orbit calculation and its finite-computation dependency are those in [Weaver 175/v1, (23)](https://rstation.ai/problems/collatz/papers/175) and [the pinned repository's use of this bound](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase4/HARMONIC_SOURCE_PHASE.md).

For perspective, a pointwise harmonic \(H\) for the same operator satisfies
\[
 T_*(H/y)(y)-H(y)/y=
 3\,1_{\{y\equiv2\ (3)\}}H((2y-1)/3)
        \left(\frac1{2y-1}-\frac1{2y}\right)\ge0 .
\]
The finite-height series in (2) involves another term of critical order \(1/y\), while this local defect has a second denominator. Controlling the latter at individual positive sites supplies no upper bound for (4).

## The uncolored finite statistic

For \(C=\mathbf N_{>0}\), periodicity gives a single finite rational observable. In each word \(w\) let \(r_w\in\{1,\ldots,3^{|w|}\}\) be the least positive representative of \(B_w\bmod3^{|w|}\), taking \(r_w=1\) if \(|w|=0\). Then
\[
 B_t(\mathbf N_{>0})
       =\mathbf E_{\rm fair}\left[\frac{3^{|w|}}{r_w}\right]
                       -\tfrac12t\log3+O(1),                       \tag{5}
\]
with an absolute error. To see this, cut the zero-mean periodic series in (2) after its first period \(Q=3^t\). Subtract the constant \(1/((j+1)Q)\) from weights on each subsequent complete period \((jQ,(j+1)Q]\). Its error is \(O(1/(j(j+1)))\) since \(\sum_{y\le Q}|H_t(y)-1|\le2Q\). In the first period a word of grade \(q\) contributes a shifted harmonic progression
\[
 \sum_{i=0}^{3^{t-q}-1}\frac1{i+r_w/3^q}
       =\frac{3^q}{r_w}+(t-q)\log3+O(1)
\]
uniformly in the shift, including the singleton case. Averaging and subtracting the ordinary harmonic sum proves (5).

Equivalently the \(2^t\) native sources \(1\le n\le2^t\) give \(r_{w_t(n)}=T^t n\): the other source \(n-2^t\le0\) with the same word ends at \(T^t n-3^q\le0\). This gives the exact finite equality
\[
 \mathbf E_{\rm fair}\frac{3^{|w|}}{r_w}
            =\sum_{n=1}^{2^t}\frac1{nR_t(n)} .
\]
For the single all-even word, \(n=2^t,\ T^t n=1\), consistent with the least-positive convention. The unconditional binomial grade distribution does not determine this correlated reciprocal moment. [Native ratio identity and reflected sign, earlier checkpoint](README.md)

If an escaping component has positive natural density \(d_C\), then this *uncolored* reciprocal moment satisfies the stronger source-qualified inequality
\[
 \liminf_{t\to\infty}\frac1t\mathbf E_{\rm fair}\frac{3^{|w|}}{r_w}
 \ \ge\ \tfrac12\log3 + e^{-0.21645}\kappa_0 d_C .                 \tag{6}
\]
For fixed small \(\epsilon>0\) split the exact native sum at \(e^{(\kappa_0+\epsilon)t}\). On the upper range outside a fixed density-zero exceptional set, Inselmann's Theorem 3.1 ensures every state through physical time \(t\) exceeds \(n^{c_\epsilon}\): its exponent \(1-\kappa_0 s/\log n\) for \(0\le s\le t\) is bounded below by \(\epsilon/(\kappa_0+\epsilon)\); use half this constant as the approximation tolerance. Hence \(R_t(n)=1+o(1)\) uniformly on these large regular inputs. The exceptional set has harmonic mass \(o(t)\) by partial summation. The upper range therefore contributes at least \((\log2-\kappa_0-\epsilon)t-o(t)\). On the disjoint lower range keep only \(n\in C\), each contributing at least \(e^{-0.21645}/n\). Their harmonic mass is \((d_C+o(1))(\kappa_0+\epsilon)t\). Send \(\epsilon\downarrow0\), yielding (6). [Inselmann, Theorem 3.1, uniform-in-date native trajectory bounds](https://arxiv.org/html/2402.03276v3#S3.Thmtheorem3.1)

Weaver 176, Theorem 1, already proves the exact weighted escape coefficient for the harmonic moment at a fixed number of **odd** steps under geometric gap sampling, with a stronger local occupation formula. Its Section 5.1 gives the earlier tilted reciprocal-square extinction test. Here the clock is a fixed number of **shortcut** steps, so the modulus \(3^{|w|}\) itself is random. The source identity and lower bound above give the physical boundary at that clock. [Weaver 176, Theorems 1 and 3](https://rstation.ai/problems/collatz/papers/176)

This explicitly identifies the harmonic coefficient that a full-conductor upper estimate would have to achieve. The present proof is a lower bound. Its strict excess detects escape given a positive-density escaping component; it does not classify nonstandard cycles, whose multiplicative correction can accumulate over repeated laps.

## Why clock marking and relative prevalence do not supply the missing upper bound

Weaver's finite-to-limiting predecessor comparison gives \(\#(C\cap[Y,2Y])/Y\ll d_C\), uniformly in \(Y\), for an escaping component \(C\). Apply its theorem to the nested fixed-target predecessor basins exhausting the component, with the usual even-source decomposition. Thus for a component of minimum \(a\) and \(\alpha>0\),
\[
 \sum_{y\in C}y^{-1-\alpha}\ll_\alpha d_C a^{-\alpha}.
\]
This makes the late rational spatial envelope small at suitable finite scales. It does not provide the analogous factor **inside a growing parity cylinder**: a word of length \(t\), grade \(q\), maps its source class to one ternary class in an interval of length approximately \(3^q X/2^t\). Dropping that class costs \(3^q\) relative to the needed \(d_C X/2^t\). [Weaver 12, Theorem 17 and direction of the comparison](https://rstation.ai/problems/collatz/papers/12)

The time-marked positive kernel \(K_z f(y)=\tfrac13 1_{y>1/2}\sum_{e\ge0}z^{e+1}f(2^e(2y-1)/3)\) obeys, for an invariant color \(C\) and \(|z|=1\),
\[
 \sum_y3\,1_{\{y\equiv2\ (3)\}}C(y)K_z f(y)
       =\sum_x C(x) z^{1+v_2(x)}f(x)
\]
for summable tests. This is an exact physical clock mark. At the broad \(g=k^\gamma,\ \gamma>1/2\) residual-time resolution, the rational clock estimate itself gives
\(\mathbf E_{\mu_{2^k,r}}|e^{i\xi(\sigma_r-2r)/g}-1|=o(1)\) for bounded \(\xi\), uniformly for \(r=O(k)\). The claim holds against any bounded terminal test by domination. It gives no sign for (2), whose positive-height flux survives the fixed-grade and time unmarking. The structural team's separate gauge calculation keeps the associated height phase.
