# Joint clock cancellation at an actual first entrance

Let $T(n)=n/2$ on positive even integers and $T(n)=(3n+1)/2$ on positive odd integers. A target set $A$ can be any subset of the integers in $[1,B]$. If the path from $n$ hits $A$, let $s$ be its first shortcut hitting time, $k$ its odd count before the hit, and $y=T^s(n)$ its actual landing. Record its final $\ell$ shortcut parity bits, padded by a fixed convention for $s<\ell$, as $v$. Its multiplicative survival mark is
\[
              b=\frac{3^k n}{2^s y}
                =\prod_{0\le j<s,\ T^j(n)\ {\rm odd}}
                         \frac{3T^j(n)}{3T^j(n)+1}\in(0,1].
\]
Let $W(y,v,b)$ be any complex function with modulus at most one, uniformly Lipschitz in $b$ with constant at most one. Its dependence on the discrete landing and suffix is unrestricted. Let $u,z$ be unit complex numbers and set
\[
       F(n)={\bf1}_{s<\infty}\,u^s z^k W(y,v,b),\qquad
       A_F(X)=X^{-1}\sum_{n\le X}F(n).
\]
All statements allow misses. They require no global stopping theorem and no lower bound on the density of the target basin. Their quantitative input is the counted consecutive synchronization estimate (4), a research-preprint input, and the power-law Diophantine specialization additionally uses the cited irrationality bound.

Suppose $u,z$ are $m$th roots of unity, at least one different from one. Put $B'=2^\ell B$ and $L=\log(X/B')\ge2$. Write $q_j$ for the continued-fraction denominators of $\log_2 3$. Uniformly in $A,B,\ell,W,u,z$ and $m$,
\[
 |A_F(X)|\ll m\inf_{j\ge1}\left(\frac1{q_j}+\frac{q_j}{\sqrt L}\right).
                                                                    \tag{1}
\]
If $|\log_2 3-P/Q|\gg_\eta Q^{-(M+\eta)}$ for every $\eta>0$, then for every $\gamma<1/(2M)$,
\[
                         |A_F(X)|\ll_\gamma m L^{-\gamma}.             \tag{2}
\]
The classical primary input permits $M=5.116201$. [Bondareva–Luchin–Salikhov, 2018, Theorem 1](https://www.mathnet.ru/eng/cheb619) · [Input conversion and alternatives](PERIOD_SPECTRUM.md)

If $\varphi$ is a Schwartz function on the real line with smooth compactly supported Fourier transform, the logarithmic source window instead satisfies the sharper
\[
 \left|\sum_{n\ge1}\frac{F(n)}n\,
                    \varphi\big(\log(n/X)\big)\right|
                   \ll_{u,z,\varphi} L^{-1/2}.                         \tag{3}
\]
This still holds for arbitrary unit complex $u,z$ provided the support of $\widehat\varphi$ has no common real solution of $e^{-it\log2}=u$ and $e^{-it\log3}=z^{-1}$. Every nontrivial finite character has no such solution anywhere. No finite irrationality-measure exponent is needed in (3).

## Physical source comparisons

Use the following counted synchrony statement for a positive interval of length $H$. Apart from at most
\[
                       O(H/\sqrt{t+1}+2^t)                             \tag{4}
\]
consecutive starts $n$, the shortcut paths from $n$ and $n+1$ agree both in their state at date $t$ and in their cumulative odd-input counts. Only the two-sibling case is used. The sharp pair estimate is a preprint input from Leen, also stated in the multi-sibling source with periodicity and the finite interval error. [Leen, exact rates in Collatz synchronization](https://doi.org/10.5281/zenodo.23268751) · [Paper 124/v1, Theorem 1 and equation (18) at $D=2$](https://rstation.ai/problems/collatz/papers/124/v1)

If $n>2^t B'$, neither trajectory can hit $A$ before date $t+\ell$, because $T^j(n)\ge n/2^j$. A counted merger by $t$ gives both starts the same hitting status, first time, odd count, landing, and final $\ell$ parity bits. On a hit the two survival marks have ratio $n/(n+1)$. The test discrepancy there is at most $1/n$. Let $Y\ge e^2B'$ and choose $t=\lfloor\tfrac12\log_2(Y/B')\rfloor$. The small sources $n\le2^t B'$, failures in (4) and harmonic discrepancy then give
\[
       \sum_{n\le Y}|F(n+1)-F(n)|\ll Y/\sqrt{\log(Y/B')}.             \tag{5}
\]
This also works for the untwisted test. The prefix clearance is why arbitrary moving targets and long terminal words are allowed.

Outside $n\le 2B'$, first shifting a source across the even edge gives $F(2n)=uF(n)$. On odd $n>2B'$, the two sources $n$ and $3n+1$ reach the same $(3n+1)/2$ after one shortcut step. Their odd counts differ by one, their total times agree, and their marks have ratio $3n/(3n+1)$. Hence $|F(3n+1)-z^{-1}F(n)|\le1/(3n)$. By (5) the sum of $|F(3n)-z^{-1}F(n)|$ on odd $n\le Y$ is $O(Y/\sqrt{\log(Y/B')})$. The same sum on **all** $n\le Y$ has that bound. To see this write $n=2^j d$ with $d$ odd. When $d>2B'$ both terms reduce by the same even phase to those at $d$. For $j\le \tfrac12\log_2(Y/B')$, the sources with $d\le2B'$ cost $O(B'\log(Y/B'))$, and the remaining normalized bounds sum geometrically. The sources with larger $j$ have total $O(\sqrt{YB'}+1)$ because all are divisible by one power of two exceeding a constant times $\sqrt{Y/B'}$.

Group the integers up to $2Y$ or $3Y$ in blocks of length two or three. Replacing each value in a block by its final multiple costs at most a fixed multiple of (5), including the incomplete block. We have proved the two simultaneous mean relations
\[
 |A_F(2Y)-uA_F(Y)|+|A_F(3Y)-z^{-1}A_F(Y)|
                      \ll [\log(Y/B')]^{-1/2}.                        \tag{6}
\]

## Sharp cutoff and the joint distribution

Consecutive convergent pairs $(P_{j-1},q_{j-1}),(P_j,q_j)$ form a unimodular integral basis. At least one pair $(a,b)$ has $u^az^b\ne1$, and therefore $|u^az^b-1|\ge2\sin(\pi/m)\ge4/m$. Both vectors have size $O(q_j)$ and satisfy $|a\log2-b\log3|\ll1/q_j$. Iterate (6) **upwards** from $X$, where all later errors are bounded by the initial error, and compare the means at $2^aX$ and $3^bX$. The latter comparison costs $O(|a\log2-b\log3|+1/X)$ solely from $|F|\le1$ and the normalized cutoffs. This proves (1).

For (2) take any $d>M-1$ so that $q_{j+1}\ll_d q_j^d$, by the standard convergent approximation bound and the hypothesis. Set $R=\sqrt L$ and choose the first $q_j\ge R^{1/(d+1)}$. Then $q_j\ll R^{d/(d+1)}$, giving $1/q_j+q_j/R\ll R^{-1/(d+1)}$. This proves (2) after choosing $d$ close enough to $M-1$.

Fourier inversion now applies to the actual pair $(s,k)\bmod m$. After any allowed terminal test, the mass assigned to a specified residue pair differs from $1/m^2$ of the entire tested hitting mass by $O_\gamma(m L^{-\gamma})$. The error is normalized by $X$. For any function of modulus one on the joint discrete records $(s,k)\bmod m,y,v$, expand as a finite Fourier sum on the clock pair with the discrete records fixed. All its Fourier coefficients have modulus at most one, so the total-variation discrepancy between the joint subprobability and Haar clocks times the true terminal marginal is $O_\gamma(m^3 L^{-\gamma})$. A continuous real mark may be retained with bounded-Lipschitz tests in that coordinate by the same argument. Total variation on the **exact real mark** is not asserted.

Fixed source intervals $[cX,dX]$ with $0<c<d<\infty$ follow by subtraction. For a fixed source arithmetic progression modulo $r$, (5) lets one replace its sum by $1/r$ of the full sum with $O_r(XL^{-1/2})$ error, by comparing a bounded number of neighbours in every block. If the relevant basin or weighted mark has a natural limit, this gives genuine conditional limiting equidistribution whenever its mass is positive. In particular both clocks before the first hit of any site on any positive integer cycle have joint Haar residues, including after an arbitrary terminal-cylinder selection of positive density. The statement also holds at nonperiodic targets. Choosing $A$ to be a whole cycle conditions jointly on its actual entry phase. None of these conclusions presupposes a compatible character of the primitive lap since an actual first hit stops at its initial target.

## The exact filtered rate and real resonances

Write $S_\psi(X)=\sum F(n)\psi(\log(n/X))/n$. Abel summation gives the exact integral representation
\[
        S_\psi(X)=\int_{\mathbb R}(\psi(t)-\psi'(t)) A_F(Xe^t)\,dt .
\]
Here $A_F(Y)=0$ for $Y<1$. By (6), on $t\ge-L/2$ both dilation errors are $O(L^{-1/2})$. On $t<-L/2$ the Schwartz tail pays for using the trivial bound. Hence for Schwartz $\psi$,
\[
 |S_\psi(2X)-uS_\psi(X)|+
 |S_\psi(3X)-z^{-1}S_\psi(X)|\ll_\psi L^{-1/2}.
\]
Use the Fourier convention $\widehat\psi(t)=\int e^{-itx}\psi(x)\,dx$. Increasing $X$ by $d$ translates the test to $\psi(x-\log d)$ with multiplier $e^{-it\log d}$. Put $D_2(t)=e^{-it\log2}-u$ and $D_3(t)=e^{-it\log3}-z^{-1}$. In a neighbourhood of the given compact support define
\[
             \widehat\psi_i(t)=
           \frac{\overline{D_i(t)}\widehat\varphi(t)}
                      {|D_2(t)|^2+|D_3(t)|^2}\quad (i=2,3),
\]
and extend by zero, with a harmless smooth cutoff equal to one on the support. These are smooth compactly supported functions. The identity $\widehat\varphi=D_2\widehat\psi_2+D_3\widehat\psi_3$ writes $S_\varphi(X)$ exactly as the sum of the two dilation errors. This proves (3). Common real zeros are unique if present by multiplicative independence of two and three. If $u,z$ have finite orders, a nonzero common frequency would make $\log2/\log3$ rational, and frequency zero requires the trivial character.

At a genuine common zero $t$, $u=2^{-it}$ and $z=3^{it}$. On a hit one has the **exact** identity
\[
                       u^s z^k=(yb/n)^{it}.
\]
Thus such a frequency is an ordinary source logarithmic character times the actual terminal landing and mark. The forbidden common zero can carry a genuine term. For example take $A=\{1\}$. The uniform reciprocal packing of first-hit paths gives $b\ge b_0>0$ on every such path, since the departed states are distinct and $-\log w(x)\le1/(3x)$. A positive constant multiple of $W(b)=\max(b,b_0)^{-it}$ meets the Lipschitz restriction on the whole interval. The remaining source phase is exactly that constant times $n^{-it}$ on the root-one basin, which has positive natural density under the cited entrance inputs. [First-visit packing and its source](CYCLE_TRACE_LAW.md) This explains the role of the real coordinate without assuming a local Gaussian law.

The comparison is absolute in ordinary-source mass. It gives no relative bound on a target whose mass shrinks faster than its error, nor does it localize the physical return diagonal at a single site or control the unweighted number of components. The first-passage cancellation therefore leaves the possibility of a single extra positive cycle open.

[Exact native record, clock-character and semiprime incidence controls](check_stopped_semiprimes.py) · [Recorded finite counts](../../../reports/astra-global-20261128/cycles/STOPPED_SEMIPRIMES.json)

## Concurrent native eigenfunction results

At PR 215 commit 7902faf, native unit-modulus branch eigenfunctions satisfy both eigenvalue equations at every positive integer. The cited proofs classify their smooth source profiles, give an exact physical-order flux for the sole Mellin resonance, and give arbitrarily high logarithmic decay for smooth compact source windows and nontrivial root-of-unity phases with $M\le(\log X)^{1/11}$. They also prove an ordinary component probability distribution in total variation and Haar relative clocks on each component modulo the subgroup generated by the actual cycle lap, with no such quotient on an escaping component. Those results use signed native ternary transport at the complete endpoint and odd count. Our arbitrary possibly moving bounded stopping set may interrupt the branch recurrences. Here the marks are the unquotiented two clocks to the first hit, with an arbitrary discrete landing and terminal word and Lipschitz real survival test. The sharp ordinary-cutoff argument above uses counted neighbor fusion; its frequency-window result assumes compact Mellin support. [PR 215, native resonance and boundary coefficient](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase5/NATIVE_MELLIN_RIGIDITY.md) · [PR 215, smooth source rates and component clock groups](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/escape/phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md)
