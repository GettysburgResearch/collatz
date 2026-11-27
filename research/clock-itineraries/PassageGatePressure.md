# Fractional pressure of the ordinary principal seeds at the certified exponent

Let \(e_i=v_2(3x_i+1)\), \(x_{i+1}=(3x_i+1)/2^{e_i}\) and \(A_j=\sum_{i<j}e_i\). Use the independent geometric word law \(\Pr(w)=2^{-A_n}\), the gate \(W_n=\{4A_j\le7j\ (j\le n)\}\), and the least positive odd seed \(m=m(w)<2^{A_n+1}\) of each word. The payoff is
\[
 Z_n(z)=\frac{2^{A_n}}{m+zG_n},\qquad
 G_n=\sum_{i<n}\frac{2^{A_i}}{3^{i+1}},\qquad
 M_n(p,z)=\mathbb E[{\bf1}_{W_n}Z_n(z)^p].
\]
These are the original word probabilities and the actual positive integer in its dyadic cylinder. Write \(a=7/4,\ r=1/a,\ q=1-r,\ d=H_2(r),\ \gamma=2^{-a(1-d)}\) and \(p_c=1+\log_2\gamma\). The prior joint pressure estimate identifies the exponential rate through \(p_c\) and gives an upper exponential rate for \(p_c<p<1\). [PR 200, joint pressure](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/JOINT_GATE_FRACTIONAL_PRESSURE.md) · [PR 201, principal trace and source construction](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)

**Written conclusions.** For every fixed real \(p<p_c\) and fixed \(z\ge0\),
\[
 M_n(p,z)\asymp_{p,z}\gamma^n(1+n)^{-3/2}.                         \tag{1}
\]
The argument for (1) uses only the finite arithmetic and elementary ballot estimates below. Using the cited uniform dictionary-height theorem as an additional input, one obtains
\[
 \Pr(Z_n(z)\ge v\mid W_n)\ll v^{-p_c}\quad(v\ge1),                 \tag{2}
\]
uniformly in \(n\ge1,\ z\ge0\), and
\[
 \begin{split}
 M_n(p_c,z)&\ll\gamma^n(1+n)^{-1/2},\\
 M_n(p,z)&\ll_p 2^{-(1-p)n}
      \exp[-c_p\log(2+n)\log\log(3+n)]\qquad (p_c<p<1).
 \end{split}                                                        \tag{3}
\]
Here (2) is a uniform weak moment bound at the certified exponent. A positive lower bound on the centered first trace from a permanently passing seed is consistent with all three estimates.

## The word at the physical seed cutoff

Put \(b=A_n-n,\ k=\lfloor\log_2m\rfloor,\ l=c_k(m)\), where \(c_i(m)\) counts odd departures among the first \(i\) shortcut ticks. Then \(0\le k\le A_n\), including \(k=A_n\). For \(1\le i\le k\), let \(j\) be the first odd date whose completed clock satisfies \(A_j\ge i\). Its \(j\)-th departure already occurred at \(A_{j-1}<i\), so \(c_i(m)=j\). Consequently \(c_i(m)\ge ri\) for **all** \(i\le k\) and \(k-l\le b\). The ordinary integer \(y=U^l(m)\) follows the completion of the gap containing the cutoff. Its remaining \(n-l\) dates have total excess
\[
 R_{\rm true}=A_n-A_l-(n-l)\le R:=b-k+l.
\]
The shifted one-step height bound \(U(x)+1\le(3/2)(x+1)\) gives \(\log(y+2)\ll1+k\), since \(l\le k\). The prefix may be empty. These assertions hold in that case as well.

The modules [PassageGatePrefix.lean](mathlib/PassageGatePrefix.lean) and [PassageGatePressure.lean](mathlib/PassageGatePressure.lean) prove the stopped prefix and remaining excess inequalities on the actual orbit. The former also gives the exact number of source residues on each translated packet of length \(2^k\), with arbitrary odd stride, subject to the full bank constraint and an even-tick cap. Its integer recursion subtracts four units per even departure and adds three per odd departure.

## A uniform counting estimate

For a Bernoulli walk of mean \(r=4/7\), subtract \(r\) at each tick. The probability of staying nonnegative to time \(k\) and ending exactly at \(u\ge0\) is
\[
 G_k(0,u)\ll (1+u)(1+k)^{-3/2}.                                    \tag{4}
\]
Here \(u\) ranges over a translate of the integers. For completeness, stop the centered walk on exit from \([0,M)\), where \(M=1+\sqrt k\). Its overshoots have magnitude at most one. The nonnegative stopped quadratic \((s+1)(M+1-s)\) loses \(r(1-r)\) in conditional mean each live step. The resulting expected exit time from \(x<M\) is \(O((x+1)M)\). The stopped linear martingale bounds the upper-exit probability by \((x+1)/(M+1)\). Markov's inequality gives forward survival \(O((x+1)/\sqrt{1+k})\), including \(x\ge M\), and the same argument applies to the reversed increments. Take three independent consecutive blocks of comparable length. Forward survival from zero and reverse survival from \(u\) cost \(O((u+1)/(1+k))\). Given the two outside blocks, the middle sum has one prescribed value, of probability \(O((1+k)^{-1/2})\) by the binomial maximal atom bound. This proves (4), increasing the constant for bounded \(k\). This is the marked-ballot argument of PR 201 at the fixed tilt \(4/7\), where \(r(1-r)>1/5\). [PR 201, critical source sector, equation (7)](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/escape/CRITICAL_SOURCE_SECTOR.md)

Write \(\lambda=q/r<1\). A binary word ending at excess \(u=l-rk\) has tilted probability \(2^{-dk}\lambda^{-u}\). Multiplying (4) by its reciprocal counts all passing words in that endpoint slice. Each binary word gives one source residue modulo \(2^k\) and hence at most one integer in \([2^k,2^{k+1})\). The physical evolution of that integer determines its continuation. With \(T=b/q\), the permissible endpoints satisfy \(u\ge0,\ u\ge q(k-T)\). For \(p\ge0\), the contribution of an individual \((k,b,u)\) cell to \(2^{(1-p)n}M_n(p,z)\) is thus at most
\[
 C(1+k)^{-3/2}(1+u)
       2^{-(1-p)b+(d-p)k}\lambda^u.                                \tag{5}
\]
The same upper bound holds with the shell payoff \(2^{A_n-k}\) in place of \(Z_n(z)\). In particular it preserves the joint dependence of the division count and the least physical seed.

The gate probability has order \(\gamma^n(1+n)^{-3/2}\). For the upper bound apply (4) to \(k=A_n\) with \(l=n\) and \(u=n-rA_n\), counting the words at the true completed clock. For \(j=an-A_n\ge0\), their original mass is at most
\(C\gamma^n(1+n)^{-3/2}(1+j)(2q)^j\). The possible \(j\)'s have spacing one and \(2q<1\). For the lower bound take \(A=\lfloor an\rfloor\). The \(\binom{A-1}{n-1}\) positive compositions each have a cyclic rotation satisfying \(A_i\le(A/n)i\), obtained at a maximum of the centered partial sums. Each resulting word has at most \(n\) preimages under the chosen rotation. Stirling's formula and the word weight \(2^{-A}\) give the lower bound. Bounded \(n\) is absorbed into the constants.

## Subcritical and critical profiles

The sharp gate probability used above also appears in PR 213 by the fluctuation generating identity. Its relative loss theorem concerns the recent cohort of ordinary odd-clock sources and certain large principal representatives. For the centered payoff its equation (3) already bounds each shell \(2^{s-1}<Z_n(0)\le2^s\) by \(O(2^{-p_c s})\) in conditional probability for \(s\le n/2-O(1)\). Indeed the harmonic mass of sources with payoff at most \(2^s\) is \(O(\gamma^{-s}\Pr(W_n))\) there, and \(2^{-s}\gamma^{-s}=2^{-p_c s}\). The argument for (2) retains that exponent through every higher payoff shell as well. [PR 213, recent-cohort loss and gate probability](https://github.com/GettysburgResearch/collatz/blob/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127/mass/GLOBAL_RECENT_COHORT.md)

At \(p=p_c\) the exponent of two in (5) vanishes at \(k=T,\ u=0\). For \(k<T\) it falls with distance from \(T\), since \(d-p_c=(a-1)(1-d)>0\). For \(k>T\), spend \(u\ge q(k-T)\) in the tilt. The slope in \(k\) is then \(d-p_c+q\log_2\lambda=\log_2a-p_c<0\). Both slopes are strict, so a constant \(c>0\) can be retained in front of both \(|k-T|\) and \(u\). Absorbing the polynomial factors from \(1+u\) and \(1+b\ll(1+k)(1+|k-T|)\) gives the critical bound
\[
 C(1+b)^{-3/2}\exp[-c D],\qquad D=|k-T|+u.                         \tag{6}
\]
In particular its sum over \(k,u\) is \(O((1+b)^{-3/2})\). Taking the sum over all depths in the source shell alone gives the additional sharp law for the union \(\mathcal D\) of all distinct passing principal seeds
\[
 \#\{m\in\mathcal D:m\le X\}\asymp
      (1+X)^d(1+\log(2+X))^{-3/2}\qquad(X\ge1).                    \tag{7}
\]
For the upper bound count the passing **binary prefixes** in each shell just once using (4), including all possible endpoints. For the lower bound use \(n=4j,\ A=7j\), with \(j\) maximal such that \(2^{7j+1}\le X\). The rotation count gives \(\gg 2^{7jd}(1+j)^{-3/2}\) distinct ordinary principal representatives below \(X\). A finite adjustment handles small \(X\). Geometric annuli and (7) yield \(\sum_{m\in\mathcal D,\ m>X}m^{-d}\asymp(1+\log X)^{-1/2}\) for \(X\ge2\). For the lower estimate choose a fixed large annulus ratio so the lower bound at its top exceeds twice the upper bound at its bottom.

For any \(p\in(\log_2 a,p_c)\), use the same two strict slopes in (5). After normalization by \(\gamma^n\), the central value picks up
\(2^{-(p_c-p)(n-b/(a-1))}\). Since \(b\le (a-1)n\), summing the analog of (6) over \(b\) now costs \(O_{p}((1+n)^{-3/2})\). For all \(0\le p<p_c\), use conditional power mean at a larger exponent still below \(p_c\). At fixed \(z\), the positive floor \(Z_n(z)\ge1/(2\max(1,z))\) supplies the lower estimate. Indeed \(m<2^{A_n+1}\) and the principal terminal \(3^n2^{-A_n}(m+G_n)<2\cdot3^n\). For \(p<0\) this floor supplies the upper bound. A bounded conditional positive moment gives a uniform conditional probability that \(Z_n(z)\) is below a fixed large number and hence supplies the lower bound. This proves (1).

## Cost of the actual remaining word

Independently of the gate, put \(\alpha=\log_2 3\), \(L=\log_2(m+1)\), \(H=(L+\alpha)/(\alpha-1)\), and let \(I_n\) count the exponents above one. A direct inequality at every positive odd seed is
\[
 n+v_2(x_n+1)+H
 \ \le\ \alpha^{I_n}\bigl(v_2(m+1)+H\bigr).                         \tag{8}
\]
On an exponent-one step \(2(x_{i+1}+1)=3(x_i+1)\), so the sum of the time and the valuation is constant. On any step, \(\log_2(x_{i+1}+1)\le L+(\alpha-1)(i+1)\). Adding \(i+1+H\) gives at most \(\alpha(i+H)\). This proves (8) by induction. The argument counts interruptions individually even when an exponent is very large. Applying (8) to \(y\) at the stopped shell gives the kernel-checked, explicit consequence \(n+1\le8(k+1)\alpha^R\). In particular the normalized critical moment already has a power saving without a Diophantine input. Indeed \(n+1\ll(1+b)(1+D)\alpha^D\), and hence for some \(\eta>0\), (6) is at most
\(C(1+b)^{-3/2}((1+b)/(n+1))^\eta e^{-cD/2}\).
Reduce \(\eta\) below \(1/2\) and sum \(b,k,u\) to obtain \(O((1+n)^{-\eta})\). The same elementary argument at fixed \(p_c<p<1\) saves a positive inverse power of \(n\) beyond \(2^{-(1-p)n}\). [PassageGateMoment.lean](mathlib/PassageGateMoment.lean) · [PassageGatePressure.lean](mathlib/PassageGatePressure.lean) · [PR 200, earlier run-count argument](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/FIXED_SOURCE_DELAY.md)

For (2) and (3), Weaver's uniform dictionary-height theorem gives the following extra bound on \(s\) odd steps with at most \(E\) non-one exponents from a positive odd integer \(y\):
\[
 1+s\ll (1+\log(y+1))\exp[C(E+1)/\log(E+2)].                       \tag{9}
\]
Use the dictionary consisting of the single word (2), whose only positive phase is \(1\). Each exponent above one is at most one counted piece when parsed individually. Theorem 5, equation (R2), applies up to the first arrival at \(1\), inclusive as an endpoint. Every further step then has exponent two and there are at most \(E\) of them. Increasing the absolute constant in (9) absorbs these steps. This use of the cited arithmetic theorem is a written input. [Lyapunov Weaver, Theorem 5, (R2)](https://rstation.ai/problems/collatz/papers/15/v2)

Apply (9) to the actual \(n-l\) remaining steps from \(y\). Since \(R=u-q(k-T)\le D\), the shell has
\[
 \frac{1+n}{1+b}\ll (1+D)\exp[C(D+1)/\log(D+2)].
\]
For each fixed \(J>0\) this pays for \(((1+n)/(1+b))^J\) out of half the exponential slack in (6), uniformly in the source. Taking \(J=3/2\) bounds **each** critical cell by \(C(1+n)^{-3/2}e^{-c'D}\). At fixed \(t=A_n-k\ge0\), \(k-T=n-t-b/(a-1)\). The sum of its exponential distance over integer \(b\) is uniformly bounded, as is the sum over the admissible unit-spaced \(u\). The total original probability of this payoff shell is consequently at most
\[
 C\,\gamma^n(1+n)^{-3/2}\,2^{-p_ct}.
\]
Here (5) was used with the exact shell payoff \(2^t\). The genuine \(Z_n(z)\) is bounded by that payoff. Summing \(t\ge\log_2 v\) proves (2). There are \(O(1+n)\) possible shells, giving the first line of (3).

For fixed \(p_c<p<1\), the exponential portion of (5) is affine in \(p\) on a logarithmic scale. At \(p_c\) it is at most \(e^{-cD}\). At \(p=1\) it is \(2^{-(1-d)k}\lambda^u\). Interpolation leaves \(e^{-c_p(k+b+u)}\), since \(b\le q(k+|k-T|)\). For \(k>\sqrt n\) this yields an exponentially small tail in \(\sqrt n\). For \(k\le\sqrt n\), apply (9) at the original seed with \(E=b\), so \(b\gg\log n\log\log n\) for large \(n\). Indeed the logarithm of \(n/(1+k)\) is at least \(\frac12\log n-O(1)\), and inversion of \((b+1)/\log(b+2)\) gives the assertion. Retain half the exponential cost to sum over \(k,b,u\). This proves the second line of (3).

At \(p=1\) the physical shell bound has no exponential cost in \(b\) for bounded \(k\). A bounded ordinary seed can stay principal while its own excess grows indefinitely. Its first-power contribution at \(z=0\) remains \(1/m\) whenever its actual trajectory passes. The still-needed assertion is that every such seed eventually violates the gate. PR 201 proves that assertion equivalent to positive Collatz. No estimate above establishes it. [PR 201, global prefix trace](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md)
