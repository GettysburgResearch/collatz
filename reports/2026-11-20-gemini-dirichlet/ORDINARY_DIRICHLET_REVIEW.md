# Independent review: ordinary Dirichlet coercivity

**Verdict:** the weighted coercivity argument is valid, conditional only on
the stated homogeneous ordinary variation lemma from the pinned PR146
source. The coarea extension, infinite summations, complex-valued scope,
rotation limit, and five-ray injection check out. Two minor presentation
clarifications identified during review have been incorporated in the frozen
draft; their reasons are recorded below. No Collatz closure or abstract LP
infeasibility follows.

Reviewed draft:
`agent_farkas_v3/ORDINARY_DIRICHLET_COERCIVITY.md`, Sections 1–7,
on 2026-11-20. The separate merger review owns the reconstruction of the
17-edge finite comparison and its bounded-congestion proof.

## 1. The two norm conventions give different displayed constants

Let

\[
d(n)=|f(3n)-f(n)|,\quad
E_s^{\rm odd}=\sum_{n\ {
\rm odd}}d(n)n^{-s},\quad
D^{\rm odd}(X)=\sum_{\substack{n\le X\\n\ {
\rm odd}}}d(n).
\]

Exact doubling invariance gives \(d(2n)=d(n)\), hence

\[
N_s(\delta_3 f)=\frac{E_s^{\rm odd}}{1-2^{-s}}\qquad(s>0).
                                                               \tag{R1}
\]

Suppose the homogeneous variation inequality has constants \(C,C'\) and
put \(Q=2C'\). For nonnegative \(h\) with vanishing dyadic means,

\[
|a_{k+1}-a_k|
\le (C/2)2^{-k}D_h^{\rm odd}(Q2^k)
\]

has the correct scale and factor: the compared adjacent edges are
\((2n,2n+1)\) for \(2^k\le n<2^{k+1}\), lying inside the source
variation window starting at \(R=2^{k+1}\).

The telescoping estimate, followed by nonnegative summation, gives

\[
\begin{aligned}
N_s(h)
&\le\frac{C}{2(1-2^{s-1})}
       \sum_{j\ge0}2^{-sj}D_h^{\rm odd}(Q2^j)\\
&\le\frac{C Q^s}
 {2(1-2^{s-1})(1-2^{-s})}\,E_s^{\rm odd}(h).
\end{aligned}                                                   \tag{R2}
\]

The second geometric denominator is essential when the right side is
the **odd** norm. Using (R1) cancels it exactly, leaving the draft's

\[
K_s=\frac{C Q^s}{2(1-2^{s-1})},\qquad
N_s(h)\le K_s N_s(\delta_3h).                                  \tag{R3}
\]

An initial review concern about a missing factor was therefore a norm
convention mismatch, not an error in (R3). Both forms should remain
visible in the final proof.

All exchanges above are Tonelli exchanges of nonnegative quantities.
The estimate holds in the extended sense, including an infinite left
side. It is consequently valid at a subcritical abscissa without first
assuming convergence there.

## 2. Coarea and complex labels

The finite variation constants in the source are independent of the
labeling. Applying the binary statement to \(1_{h>t}\), then integrating
over thresholds, gives its real-valued total-variation version. For real
labels of either sign, integrate over all real thresholds; every pair of
finite labels gives a finite integral of the difference of indicators.

For complex labels, apply the real inequality to
\(\operatorname{Re}(e^{i\theta}f)\), integrate in \(\theta\), and use

\[
\int_0^{2\pi}|\operatorname{Re}(e^{i\theta}z)|\,d\theta=4|z|.
\]

The factor 4 cancels on both sides. Thus the same \(C,C'\) work for
complex labels. Coarea is applied only to the finite variation interval
and finite defect list in each instance, so no extra global integrability
hypothesis is hidden here.

For the summable complex theorem, use \(h=|f|\), which is still
invariant. Then
\(|\delta_3|f|(n)|\le|\delta_3f(n)|\). The claimed weighted norm
bound follows without assuming positivity of the original function.

## 3. Bounded labels modulo one constant

For \(R=2^k\), the logarithmic profiles
\(g_k(t)=f(\lfloor R2^t\rfloor)\) satisfy the stated bound

\[
\|g_{k+1}-g_k\|_1
\le \frac{C}{R\ln2}D_f^{\rm odd}(QR).
\]

Indeed, \(\lfloor2x\rfloor\) and \(2\lfloor x\rfloor\) differ by
at most one, and the logarithmic measure of an integer cell is at most
\(1/(R\ln2)\). The constant is conservative and valid.

If \(E_s^{\rm odd}(f)<\infty\) for \(0<s<1\), then

\[
D_f^{\rm odd}(X)\le X^s E_s^{\rm odd}(f).
\]

Consequently the consecutive-profile differences are summable in \(k\),
so the profiles converge in \(L^1\). This is full sequence convergence,
not only subsequential compactness.

The rotation comparison is also valid. For
\(\theta=\log_2 3\), the representatives
\(3\lfloor x\rfloor\) and
\(2^j\lfloor3x/2^j\rfloor\), \(j\in\{1,2\}\), differ by at most
four. For \(R\ge4\), their connecting edges lie inside \([2R,8R]\),
which the two source windows \([2R,4R]\) and \([4R,8R]\) cover.
Each adjacent edge is charged by at most four integers \(\lfloor x\rfloor\).
An odd part has at most one dyadic lift in \([R,2R)\), so the remaining
tripling comparison has no logarithmic multiplicity. The draft's bound

\[
\|g_k(\cdot+\theta)-g_k\|_1
\le\frac{1+8C}{R\ln2}
D_f^{\rm odd}(\max(2,4C')R)
\]

is safe and tends to zero.

The limit is invariant under an irrational circle rotation. Fourier
coefficients show it is constant almost everywhere: for each nonzero
integer \(m\), multiplication by \(e^{2\pi i m\theta}\ne1\)
forces the corresponding coefficient to vanish. Fourier uniqueness in
\(L^1\) completes this step for real and complex limits.

The lower bound \(1/(2R\ln2)\) for the logarithmic measure of each
integer cell proves that the dyadic means of \(|f-c|\) tend to zero.
Applying (R3) to that nonnegative invariant function gives the claimed
bound with the same \(K_s\). Uniqueness of \(c\) follows because any
nonzero constant has infinite \(N_s\) norm for \(s<1\). For binary
labels, an almost everywhere convergent subsequence shows \(c\in\{0,1\}\).

## 4. Five-ray comparison and abscissae

Direct shortcut arithmetic gives
\(T^2(20x+1)=15x+1\), hence

\[
|\delta_3f(x)|
\le|\delta_5f(3x)|+|\delta_5f(4x)|.
\]

For odd \(x\), the two parameter images are disjoint: \(3x\) is odd,
whereas \(4x\) has valuation exactly two. Their injectivity gives

\[
E_s^{\rm odd}(f)\le4^sN_s(\delta_5f),
\]

with no additional factor two. Combining this with (R2) yields the
draft's five-ray coefficient \(K_s4^s/(1-2^{-s})\).

For an invariant indicator with \(0<\sigma_K<1\), its dyadic means
tend to zero by choosing any exponent
\(\max(0,\sigma_K)<t<1\) where its Dirichlet series converges.
The upper comparisons with factors \(1+3^s\) and \(1+6^s\) are
correct. Thus the three series converge at exactly the same exponents
inside \((0,1)\), and their abscissae agree. The extended inequalities
also prove simultaneous convergence or divergence **at** a positive
subcritical abscissa.

The lower bounds for their normalized ratios hold whether the common
critical series is finite or infinite. Critical divergence is needed
only for interpretations in which normalizing by that series is meant
to remove every fixed finite prefix; it is not needed for the ratios
themselves.

## 5. Two incorporated scope clarifications

1. Near the five-ray inequality, say explicitly “for nonnegative \(f\)
   satisfying OD1, or for \(f\) satisfying OD2.” For a general signed
   or complex function, vanishing means of \(f\) are not the same
   hypothesis as vanishing means of \(|f|\). The existing proofs use
   the latter where needed.
2. If “abscissa” has its usual definition, finite supports have abscissa
   \(-\infty\). Comparisons only at positive exponents directly identify
   abscissae clipped at zero. Either define a nonnegative abscissa
   convention, or use the elementary positive lower bound for nonempty
   ordinary invariant sets and omit the zero case.

The latter alternative needs no new external predecessor theorem. Every
nonempty invariant set contains a positive odd ternary unit \(y\).
Among the six gaps \(1\le a\le6\), exactly two inverse letters
\((2^ay-1)/3\) are positive odd ternary units. Repeating these two
choices gives \(2^j\) distinct odd ancestors, each at most
\((64/3)^jy\); distinctness follows from uniqueness of the forward odd
orbit and its exact gaps at a fixed depth. Therefore the set's abscissa
is at least \(\log2/\log(64/3)>0\). This elementary observation is
already in PR146's `THREE_RAY_VARIATION.md`. The empty invariant set has
empty boundaries and all three ordinary abscissae \(-\infty\).

The final draft explicitly chooses the nonnegative abscissa convention,
states why the distinction is immaterial for a nonempty ordinary component,
and explicitly uses nonnegative \(f\) or means of \(|f|\) in Section 5.
Both review points are resolved. The frozen reviewed draft has SHA-256
`d5229d794b97ba4c7663f105388ed597251d34fd678cc2189c39ebf0c7b43c74`.

## 6. Endpoints and global scope

The proof establishes the whole open strip \(0<s<1\). As \(s\uparrow1\),

\[
K_s\sim \frac{C Q}{2\ln2}\frac1{1-s}.
\]

Accordingly it does not furnish a finite uniform constant at exponent
one. This is a limit of this proof, not an impossibility theorem for
other estimates at that endpoint.

All estimates concern actual ordinary invariant functions with all
their adjacent-integer comparisons. Abstract residue masses need not
possess those data or admit an ordinary realization. Nothing here proves
infeasibility of an arbitrary finite or infinite residue relaxation.
Finally, no new upper estimate on an actual exceptional component or
boundary has been established, so the argument does not resolve Collatz.
