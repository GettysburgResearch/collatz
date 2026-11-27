# All-clock protection after a maximal postpeak word

**Written classification of actual ordinary meetings.** Let the original shortcut word be \(O^H w\), with \(t=|w|\), \(f\) odd letters, \(q=t-f\) even letters, and \(h=H+f\). Write \(C_w=A_w-3^f\), where \(2^tT_w(x)=3^f x+A_w\). Call \(w\) maximal if no word of length \(t\) with this same \(C_w\) has greater weight. Each full prescribed word \(O^H w\) is one dyadic source cylinder. Below, density means natural density *relative to that cylinder*, with \(H,w\) fixed before the source height tends to infinity.

For **\(H\ge600,\ t\le H/100\)**, the density of sources whose original orbit has **no meeting with any smaller positive start, at any visitor clock, through the end of \(O^H w\)** exceeds \(1/3\) if \(w\) is maximal. If \(w\) is nonmaximal, every source in the cylinder has a smaller visitor at the endpoint. The theorem classifies positive-density protection against complete smaller orbits, not only a bounded odd budget. The upper source need not converge for either conclusion. When \(H\) is required to be the length of the maximal initial ascent, consider words \(w\) beginning in \(E\).

More generally let \(H\ge12(t+2)\), \(L=\lfloor H/12\rfloor\), and \(s=284051/829440\). For maximal \(w\) the density is at least
\[
                             s-5\,6^t4^q2^{-L}.
\]
The corresponding lower fraction contributed by sources \(n=0\bmod3\), still normalized by the entire dyadic cylinder, is at least \(1041139/4147200-5\,6^t4^q2^{-L}\). Positive lower bounds apply whenever the displayed errors permit them. The estimate is uniform in the indicated words and heights, after taking their individual natural-density limits. The final section proves a separate uniform finite-shell theorem when the ramp height grows at most logarithmically with the sample.

The proof extends Weaver's pure-odd cylinder protection analysis to general maximal postpeak words. It uses the physical long-arrival transfer and the squared-gain stopping bound from Weaver 177–178. The signed trap, common-binary-scale set and equal-offset classification are from this sprint. Weaver 178/v1 already proves a stronger lower proportion above \(0.510269713938\) on a pure ascent. [Weaver 178/v1 §§2,7](https://rstation.ai/problems/collatz/papers/178/v1) · [Weaver 177/v1 §8 (3)](https://rstation.ai/problems/collatz/papers/177/v1) · [Signed trap](../SignedEscape.lean) · [Equal-offset classification](../POSTPEAK.md) · [Sharp cone at six times the even count](../../../root/phase4/MIRROR_ENERGY.md) · [Common-scale count](../../../root/phase5/COMMON_PROTECTION.md)

## The signed target and a stopped reverse path

Write the ordinary source as \(n=2^H v-1\), \(v>0\). Its target and the gain of its prescribed word are
\[
 Y=\frac{3^h v+C_w}{2^t},\qquad
 R=\frac{C_w}{2^t},\qquad g_*=\frac{3^h}{2^{H+t}} .
\]
As \(n\) runs through the dyadic cylinder, it is uniform at each fixed ternary precision. In \(\mathbb Z_3\), varying a Haar variable \(N\) in place of \(n\) makes
\(Y=R+3^h(N+1)/2^{H+t}\) uniform on \(R+3^h\mathbb Z_3\). Here a legal reverse odd step at \(y\) sends it to \((2y-1)/3\) when \(y=2\bmod3\), and an even inverse doubles it. A fixed reverse word with \(b\) odds is legal on a single class modulo \(3^b\).

For maximal \(w\), the previous cone theorem excludes every actual smaller visitor of grade at most \(h\) once \(H\ge6q+3\), as is the case here. Consider a competitor of grade greater than \(h\). Stop its reverse word **immediately after its \(h\)-th odd inverse**. The stopped part \(S\) has \(h+\ell\) letters, including \(\ell\) evens. Its legality on the target ball is exactly its legality at the fixed dyadic rational \(R\), since only \(h\) ternary digits are tested. Its gain is \(g_S=3^h/2^{h+\ell}\). For a full word of gain larger than \(g_*\), the remaining continuation must have gain greater than \(g_*/g_S=2^{\ell-q}\). Equality of full gains is impossible for a word with more than \(h\) odds by unique factorization.

We have \(h+\ell\ge t\). Read the first \(t\) reverse letters in forward order as \(\beta\), of weight \(u\). At their end the signed rational has become
\[
                       z_0=(C_w-A_\beta)/3^u\in\mathbb Z,\qquad
                       |z_0|\le2\,3^{t-u}.
\]
Integrality follows from ternary legality at \(R\), since the powers of two in its denominator have canceled. The magnitude bound follows from \(0\le A_\beta<3^t\) and \(|C_w|\le3^t\). Before these \(t\) reversals have finished, formal branch evaluations at \(R\) need not be integer walks. After reaching \(z_0\), all further reverse edges are genuine native edges on signed integers. In forward order this residual signed prefix goes from a signed origin \(z_*\) to \(z_0\), with \(h-u\) odds and \(\ell-(t-u)\) evens. Because we stopped at an odd inverse and \(h>t\), \(z_*\) is odd. At the actual or ternary target the corresponding stopped endpoint is
\[
                          Z_S=z_*+2^{\ell-q}(N+1).
\]
For each fixed \(S\), this is Haar-uniform on \(\mathbb Z_3\). Multiplication by a power of two, including a negative exponent, is a ternary unit.

## Short even totals give the same common-scale obstruction

Suppose \(\ell\le L\). The signed prefix has at least \(H-q\ge9L+3\) odds, at most \(L\le2L\) evens, and final absolute value at most \(2\,3^L\), because \(L\ge t+2\). The kernel-checked signed trap forces \(z_0=-1\). Thus \(C_\beta=C_w\). Maximality yields \(\delta=f-u\ge0\). Set \(\ell'=\ell-(t-u)=\ell-q-\delta\ge0\). Now \(z_*=-M\) for a positive odd integer \(M\) which reaches 1 under the reflected native map with exactly \(\ell'\) even departures. Reverse odd steps weakly decrease its magnitude, so \(1\le M\le2^{\ell'}\). Therefore
\[
             Z_S=2^{\ell'+\delta}(N+1)-M,\qquad
             g_*/g_S=2^{\ell'+\delta}.
\]

Take the nested finite common sets of the cited protection theorem, excluding all potentially productive first strict crossings at up to \(K\) odd inverses. They can use all reflected origins, or the same nested supersets used for the seven-even count. Their decreasing intersection \(F_\infty\subseteq\mathbb Z_3\) has Haar mass at least \(s\), with at least \(1041139/4147200\) of full Haar mass in the zero class. On \(F_\infty\) no legal continuation at any of the displayed common origins has gain strictly above \(2^{\ell'+\delta}\): its earliest such prefix has some finite odd count and would have been removed at that precision. Thus all short-even stopped words are simultaneously harmless on this single Haar set.

## Long even totals have a summable tail

At an integer signed state each legal reverse odd has absolute value at most the previous absolute value, except that zero has no odd inverse. Each reverse even doubles absolute value. Consequently \(|z_*|\le2\,3^t2^\ell\). For fixed \(\ell,\beta,z_*\) the residual forward signed prefix of clock \(h+\ell-t\) is determined by native integer iteration. Appending the fixed formal suffix \(\beta\) recovers the entire stopped word. Thus the number of eligible \(S\)'s at this \(\ell\) is at most
\[
           2^t(4\,3^t2^\ell+1)\ \le\ 5\,6^t 2^\ell .
\]
This bound does not grow with \(H\).

For \(\ell>L\), the needed continuation threshold \(2^{\ell-q}\) exceeds one. At the corresponding Haar-uniform \(Z_S\), Weaver's prefix-free squared-gain bound gives probability at most \(4^{q-\ell}\) of some legal continuation with strictly larger gain. The stopped endpoints need not be independent. A union bound over all such branches loses at most
\[
                 \sum_{\ell>L}5\,6^t2^\ell4^{q-\ell}
                          =5\,6^t4^q2^{-L}.
\]
Therefore that fraction is the only additional loss to subtract from either common-set lower bound.

## Passing back to complete physical orbits

A smaller visitor to any earlier point through \(Y\) can be continued along the original orbit to \(Y\), and a visit at \(Y\) already counts. It suffices to consider the single endpoint. Fix a reverse deadline \(J\). There are finitely many words through that deadline and all are affine on fixed ternary classes. An ordinary inverse source has the form \(Y/g-c\) with constant \(c\) depending on its word. If its gain \(g\) is strictly less than \(g_*\), then \(Y/g-c>n\) for all sufficiently large \(n\) in the cylinder, uniformly over this finite list. An equal-gain word must use exactly \(h\) odds and is already excluded as a smaller visitor by the maximal cone. Hence any late-size failure of this finite test lies in the larger-gain ternary events bounded above. The finite test has a natural density by periodicity of its legality classes and eventual stabilization of affine comparisons. In particular, finite testing transfers lower bounds from Haar measure without assuming that \(F_\infty\) itself has a natural density of its ordinary points.

To remove \(J\), choose the least positive ancestor of any \(Y\) missed at the truncated deadline but actually reached from below. This minimum exists since \(Y\) is its own ancestor, and it is strictly below \(n\) because a smaller visitor is assumed. Its first arrival stays at or above that least source. For \(n\le X\) both source and target are at most \(C_{H,w}X\), and \(n\mapsto Y\) is injective on the fixed dyadic cylinder. Weaver 177/v1 §8 (3) bounds the relative upper density of such missed targets by \(O_{H,w}(\rho^J)\), where \(\rho<1\). Letting \(J\to\infty\) gives the complete physical density, including its zero-class restriction and the same lower bounds.

If \(w\) is nonmaximal, choose \(\beta\) of the same length and offset with \(u>f\). Put \(p=H+f-u\ge1\). Then \(m=2^pv-1\) is positive and strictly below \(n\). After its \(p\) initial odd steps it reaches \(3^p v-1\). The formal word \(\beta\) takes that integer to \(Y\), by \(p+u=H+f\) and equality of offsets. An integral endpoint forces native parities, so this is an actual smaller visitor for every source. For maximal words, \(H\ge600,\ t\le H/100\) gives \(5\,6^t4^q2^{-L}\le2^{4+5t-H/12}\le2^{-16}\), and \(s-2^{-16}>1/3\).

## Counting postpeak choices

At a fixed weight \(f\), distinct words of length \(t\) have different signed offsets. Otherwise they have the same unsigned intercept and the same unit slope numerator. The equation \(3^f x+A\equiv0\bmod2^t\) fixes a unique dyadic source class, whose members have a unique physical length-\(t\) parity word. Thus the central weight alone supplies \(\binom{t}{\lfloor t/2\rfloor}\) distinct offset fibres, each with a maximal member. Conditional on the initial \(H\) odd letters, the \(2^t\) postwords have equal dyadic density. At least
\[
                      \frac13\,2^{-t}\binom{t}{\lfloor t/2\rfloor}
\]
of those ascent-cylinder sources therefore have no smaller ordinary visitor through \(H+t\) shortcuts in the stated range. This final estimate is normalized by the all-\(H\)-odd cylinder; it does not condition the next bit to be even.

## Uniformly growing heights in actual integer shells

A stronger finite-sample form holds without taking a separate height cutoff for each cylinder. For all sufficiently large \(X\), simultaneously for **every** \(600\le H\le(\log_2 X)/100\) and \(t\le H/100\), on each maximal cylinder \(O^H w\) more than one third of its representatives in \([X,2X)\) have no smaller visitor through its endpoint. More than one quarter of the cylinder's representatives both have this protection and are divisible by three. Every nonmaximal cylinder still has a smaller visitor for each of its sources. Both proportions use the full cylinder count as denominator.

Write \(B=H+t\le(\log_2 X)/90\), \(J=\lfloor(\log_2X)/2\rfloor\). The cylinder has \(M=X/2^B+O(1)\gg X^{89/90}\) representatives. Its targets lie below \(Z=4X(3/2)^B\ll X^{151/150}\), by \(\log_2(3/2)<3/5\).

First consider a visitor of clock \(d\le J\) and grade \(k>h\). Suppose its gain \(g=3^k/2^d\) is smaller than \(g_*\), so
\[
        D=g_*/g=\frac{2^d3^h}{2^B3^k}>1,\qquad
        D-1\ge \frac{1}{2^B3^k}.
\]
With \(A\) its forward affine numerator, its source is
\(m=D(n+1)+(2^dR-A)/3^k\). Therefore \(m<n\) would imply
\[
               n<2^B(3^d+2^d|R|)\ \le\ 2 X^{1/90+4/5}<X
\]
for large \(X\). Here \(A\le3^d\), \(|R|\le(3/2)^t\), and \(2^J(3/2)^t\le X^{1/2+1/150}\). Thus a finite-clock competitor of larger grade must have strictly larger gain, even with these growing clocks and source heights. Equal gain and grade at most \(h\) are already covered by the pointwise cone.

The event of some larger-gain legal word through \(J\) of grade greater than \(h\) is a union of ternary classes modulo \(3^J\) in \(N\), by the displayed affine target map. The preceding short- and long-even bounds apply to this event unchanged. In the dyadic source progression all ternary classes are cycled uniformly. Replacing its Haar proportion by the shell count costs \(O(3^J/M)=o(1)\) relatively, uniformly, since \(3^J\le X^{4/5}\). The same is true after intersecting with \(n=0\bmod3\).

If the finite test misses any actual smaller visitor, the least ancestor's first arrival is later than \(J\), so the injective target map charges a member of \(E_J(Z)\). The uniform bound proved in the companion note gives relative error
\[
 \frac{|E_J(Z)|}{M}\ll
 X^{\,151/150-1/50-89/90}+X^{\,(151/150)(49/50)-89/90}=o(1).
\]
Both exponents are strictly negative. All constants here are absolute and the same bound holds on each cylinder. Since \(s-2^{-16}>1/3\) and \(1041139/4147200-2^{-16}>1/4\), the claimed strict proportions follow. Summing these per-cylinder estimates also gives the central-binomial survival lower bound in the finite shell, up to the \(O(1)\) dyadic count rounding per cylinder. [Uniform long-arrival proof](SCALED_TARGETS.md)
