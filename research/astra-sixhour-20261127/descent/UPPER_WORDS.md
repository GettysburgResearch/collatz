# Clearing the full upper word at the original positive source

**PROPOSED.** Write \(T(n)=n/2\) on even inputs and \(T(n)=(3n+1)/2\) on odd inputs. Let \(P_j(n)\) count the odd departures before shortcut clock \(j\). A supplied upper hit \(T^H(3z)=1\) of grade \(r=P_H(3z)\) gives
\[
             3^{r+1}z=2^H-B,\qquad B\in\mathbb Z_{\ge0}.
\]
The standard affine word identity gives this equality, and \(B<2^H\). The residue \(B\equiv 2^H\bmod3\) is nonzero. The argument below includes every positive ordinary \(z\) admitting the supplied upper hit. The value \(z\) is never replaced by a residue representative.

## A signed reduction with a joint time and height estimate

Start at \(a/3^k\) with \(a\in\mathbb Z\), \(k>0\), and \(3\nmid a\). For even \(a\) replace \(a\) by \(a/2\), retaining \(k\). For odd \(a\) replace it by \((a+3^{k-1})/2\) and reduce \(k\) by one. In positive debt the new numerator remains a ternary unit. In particular a nonzero even numerator can be halved only finitely often before the next odd departure. The process stops at an integer \(c\) after precisely \(k\) odd departures in a finite number \(t\) of clocks. These are rational forward steps on an odd denominator. Integer input data in the ordinary Collatz problem continue to use the positive shortcut map.

For \(M(a)=\max(1,|a|)\) the resulting trace satisfies
\[
       2^t M(c)\le M(a)\prod_{i=0}^{k-1}(1+3^i).                         \tag{1}
\]
At an even departure \(a=2b\ne0\) one has \(2M(b)=M(a)\). At an odd departure with remaining debt \(j\), \(2|b|\le |a|+3^{j-1}\) and \(2\le |a|(1+3^{j-1})\). Multiplying the inequalities proves (1). If \(c<0\), every prior state is negative, and an odd step subtracts \(3^{j-1}\) from the absolute numerator before halving it. This strengthens (1) to
\[
                       2^t |c|\le |a|.                                  \tag{2}
\]

Suppose the **same positive original integer** satisfies \(3^k z=2^{t+d}q+a\) for some integer \(q\) and \(d\ge0\). The signed and physical branches agree at each of the first \(t\) departures because an unspent factor of two makes their numerators have the same parity. Each odd departure cancels one denominator three. Thus
\[
                     0<T^t z=2^d q+c,\qquad P_t(z)=k.                   \tag{3}
\]
For the unpadded full upper word, \(a=-B,\ k=r+1,\ q=1\). If \(c<0\), (2) gives \(2^t\le B<2^H\). Hence \(t<H\) and (3) already supplies a strictly positive physical endpoint. No hypothesis on a final halving gap occurs here. [SignedCenter.lean](SignedCenter.lean)

## Paying the binary budget at every rank

Append \(r\) physical laps \(1\to2\to1\) to the supplied upper hit. The resulting word has \(H'=H+2r\) clocks and \(R=2r\) odd departures. Either the ordinary lower reaches one before \(H'\), or
\[
                             P_{H'}(z)\ge R+1.                           \tag{4}
\]
Indeed, in the latter case every odd departed lower state is at least three. Each such departure multiplies the height by at most \((10/3)/2\), while an even departure multiplies it by \(1/2\). If \(p=P_{H'}(z)\le2r\), then \(2^H\ge3^{r+1}z\) gives
\[
             0<T^{H'}z\le \frac{z(10/3)^{2r}}{2^H4^r}
                    \le \frac13(25/27)^r<1.
\]
This contradiction proves (4) on cyclic and nonperiodic lower trajectories alike. Use \(t\) at the departure that completes the first \(R+1\) lower odds. The signed shadow of \(a=3^{R+1}z-2^{H'}\) matches the ordinary lower through \(t\), since \(t\le H'\). At exactly that clock its full ternary denominator clears. Equations (1) and (3) now hold with \(d=H'-t\), \(q=1\). Padding consumes real upper clocks but makes no assumption that an odd rank decreases. [LapBudget.lean](LapBudget.lean)

## Every supplied good suffix has cofinal negative exits

The following ordinary family prevents turning (3) into a bound on \(|c|\) in terms of upper first-hit rank. Fix any odd \(u>1\) with \(3\nmid u\) that first hits one in \(h\) clocks using \(s\) odd departures. Write \(A=2^h-3^s u>0\). There are arbitrarily large \(e\) such that
\[
       2^{e+5}u\equiv103\pmod {243},\qquad 81z+271=2^{e+9}u.            \tag{5}
\]
The first congruence makes the second define an integer \(z\equiv17\pmod {48}\): multiplying the first congruence by \(16\) gives equality modulo \(3888=81\cdot48\). For existence, two generates the unit group modulo \(243\), with period \(162\). This can be checked by \(2^{162}\equiv1\) and \(2^{81},2^{54}\not\equiv1\pmod{243}\).

The existing ordinary seven/nine-clock identity on (5) puts the lower at \(2^{e+2}u-1\) after seven clocks and four odds, and the upper at \(2^e u\) after nine clocks and three odds. The subsequent \(e\) upper halvings reach \(u\). For sufficiently large \(e\) every state on the fixed nine-clock opening exceeds one. The supplied suffix therefore gives a genuine first hit at \(H=e+9+h\) of grade \(r=s+3\). [PR192, original Mersenne row](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/SignedMersenne.lean)

PR197 already realizes cofinal prescribed exact upper ranks together with a specified finite post-ascent parity word, by fixing the ascent and varying the cofactor. Here the entire convergent cofactor suffix is fixed while the ascent length varies. The new conclusion concerns its exact signed integral exit, its size, and the clock through which the original lower remains high. [PR197, Theorem WR-1](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/source-progress/WORD_REALIZATION.md)

The signed lower center for this *entire* supplied upper certificate is
\[
       -\frac{271}{81}-\frac{2^{e+9}A}{81\,3^s}.
\]
The first term alone takes seven signed steps and four odds to reach \(-1\). The full center therefore reaches \(-1-2^{e+2}A/3^s\) at the same clock. If \(e+2\ge s\), the next \(s\) steps follow the odd branch of \(-1\), clearing the denominator at exactly
\[
                     t=7+s,\qquad c=-1-2^{e+2-s}A.                     \tag{6}
\]
The original lower stays positive throughout. Since \(A>0\), (6) is unbounded in absolute value at a *fixed* supplied suffix and a fixed upper first-hit rank. All \(s\ge1\) occur: begin at \(u=5\), and given an odd ternary unit \(u\) already known to converge, choose a sufficiently large \(j\ge4\) with \(2^j u\equiv4\) or \(7\bmod9\). Then \((2^j u-1)/3\) is an odd ternary unit greater than \(u\), with exactly one additional odd departure before \(u\). On these families the negative exit size varies at every fixed first-hit rank \(r\ge4\).

The lower slopes through the first seven clocks in (5) are \(1,3/2,3/4,9/8,9/16,27/32,81/64,81/128\). All their affine corrections are nonnegative. The next \(e+2\) lower steps are all odd and end at \(3^{e+2}u-1\), which exceeds \(8\cdot3^e u\). Each subsequent ordinary step reduces by at most a factor two. Since \(z<(512/81)2^e u\), the original lower exceeds \(z\) for at least \(\lfloor e\log_2(3/2)\rfloor\) clocks after this peak. Thus it stays at least \(9z/16\) through this expanding deadline, including the *entire* upper first hit and unboundedly many clocks beyond it for any fixed supplied suffix. This excludes lower forward contraction by a factor greater than \(16/9\) by a uniform number of clocks after the upper first hit. It leaves independent earlier positive preimages and unbounded later meetings available.

The required implication at the least reverse disagreement is still open. Paying the full binary budget gives a physical lower at \(2^d+c\). Its strict positivity does not put it below the certified \(z/2^{40}\) floor, and (6) precludes treating \(|c|\) as a bounded-rank repair cost.
