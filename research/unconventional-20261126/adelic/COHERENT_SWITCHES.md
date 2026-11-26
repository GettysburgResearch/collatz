# Subexponential denominators and separation of every native phase

**Status.** Proposed mathematical proofs. The map is the shortcut Collatz map on positive rationals of odd denominator. All periods below are native least periods. The one-third obstruction in section 1 applies to the short switches of [PRIMITIVE_PRESSURE.md](PRIMITIVE_PRESSURE.md). The longer coherent switches used in the subsequent sections give different cycles.

**Theorem.** Fix $0<a<1/2$ and a finite prime set $S$. There are constants $\eta,\kappa>0$ and an infinite sequence of positive rational cycles with least periods $n\to\infty$ such that

* their exact reduced denominators $d>1$ satisfy $\log_2d\ll n^{1-\eta}$ and have no prime factor in $S$ or at most $n^a$;
* every real phase tends uniformly to infinity, and **every pair of distinct physical phases** in one cycle is at real distance $\gg n^\kappa$.

There is also a sequence for the stronger cutoff $\sqrt n/(\log(2n))^{3/2+\varepsilon}$, for every fixed $\varepsilon>0$, with $\log d=o(n)$ and minimum pairwise distance tending to infinity. These latter assertions use a diagonal sequence and assert no polynomial saving. All the examples have genuine nontrivial denominators. The ordinary condition $d=1$ remains open.

## 1. What short switches force

Suppose a cyclic binary word consists of a periodic template of fixed single digits and designated pairs that may independently be $01$ or $10$ on each passage. Suppose more than one distinct phase returns to the start of that template during the least cycle. Then two distinct native phases have real distance **strictly less than $1/3$**.

Indeed, track the distinct starting phases in increasing order through one template. Each fixed digit preserves strict order. A pair sends $x$ to $(3x+h)/4$ for $h\in\{1,2\}$. For $x<y$, a reversal under possibly different alternatives requires $3(y-x)<1$. Equality of the images cannot occur for distinct points on one primitive cycle because the native map permutes those points. If all physical gaps were at least $1/3$, the template would preserve the strict ordering and induce an increasing permutation of the finite set of boundary phases. That permutation would be the identity. Advancing by the template instead cycles the boundary phases. This proves the claim. Larger same-grade words can reverse the order of ordinary integers. For example the six-step words of $48$ and $49$ are $000011$ and $101000$ and their endpoints are $8$ and $7$.

## 2. Common slopes with two coherent choices

Use convergents $q/m<\beta=\log_3 2$ to set $B=2^m$, $A=3^q$, $\lambda=A/B=e^{-\delta}$, $0<\delta<\log(3)/m$. For every $0<j<m$ and $u\in\mathbb Z$ best approximation gives
\[
 |j\log2-u\log3|\ge\delta. \tag{1}
\]
Choose two distinct primes $r,t\ge5$. The clock will be $n=mrt$. We specify their growth at the end. The two adjacent motifs each have length $L=o(m)$ and grade $Q$, with $L\to\infty$ and $|\log\mu|$ small, where $\mu=3^Q/2^L$. Use the **same** word $w$ of length $L-2$ and grade $Q-1$ in the two alternatives
\[
 U=1w0,\qquad V=0w1.
\]
The full macro contains two such motifs followed by a common remainder $v$ of length $m-2L$ and grade $q-2Q$. At macro time $j$ choose $V$ in motif one precisely if $r\mid j$, and choose $V$ in motif two precisely if $t\mid j$. Both flags are individually readable from the first digit of their motif. Since $\gcd(m,q)=1$, any native least period dividing $mrt$ is a multiple of $m$. It must advance both flags by their periods, hence is $mrt$. The affine-word identity gives native parity and positivity of the unique periodic point. [The cycle-index packet, §1](CYCLE_INDEX.md)

Choose $w,v$ with uniformly bounded prefix-grade discrepancies from their respective rational slopes. Section 3 permits prescribed congruences while retaining this property. All four macro words have prefix-grade discrepancy $O(1)$ from $q/m$, because $Q-Lq/m=O(1)$, there are just two motifs, and the alternatives have the same grade. Thus every subword inside one macro has its multiplier in $[c,C]$ with absolute $c,C>0$. This holds also on cyclic arcs of at most $m$ bits in any selection of the four macros starting at a fixed physical offset. The normalized carry of an arc of length $h$ is $O(h)$, and is $\gg h$ for $h$ beyond a fixed constant because each odd step contributes half the multiplier of its suffix and there are $\gg h$ odd steps.

Let the map of $w$ be $x\mapsto R x+b$. The alternatives $U,V$ have the same slope $3R/4=\mu$. Their normalized carries are $R/4+b/2$ and $1/2+3b/2$, respectively, so
\[
 b_V-b_U=b+(2-R)/4\asymp L,\qquad
 C_V-C_U=4C_w+2^{L-1}-3^{Q-1}. \tag{2}
\]
Here $C_z$ is the integer carry in $F_z(x)=(3^{|z|_1}x+C_z)/2^{|z|}$. Both $b_U,b_V$ are between positive absolute multiples of $L$. Let $C_0$ be the integer carry of $UUv$, and $c_1,c_2$ the increments from turning on the first and second flag. Equal motif grades give exact additivity. Put $a_i=c_i/A$. The two identical adjacent motifs and the uniformly bounded remainder multiplier give
\[
 a_2\asymp L,\qquad a_1/a_2=\mu. \tag{3}
\]
In particular both $c_i$ are positive and $c_i\ll BL$. At the macro boundaries the recurrence is $x_{j+1}=\lambda x_j+C_0/B+\lambda a_1{\bf1}_{r\mid j}+\lambda a_2{\bf1}_{t\mid j}$.

## 3. The actual reduced denominator and growing local tests

Let $Y$ be the full part of $D_n=B^{rt}-A^{rt}$ supported at the tested primes, including $S$. It is coprime to $6$. Provided the patch cost $P=O(\log(2Y)\log\log(3Y))$ is $o(L)$, both switch increments and $C_0$ can be made divisible by $Y$. To do so, partition each of $w$ and $v$ into blocks of a fixed width, say 8, with cumulative boundary grades the floors of their linearly interpolated grades. Fix the possible shorter final block. For large $m$ every full block has grade between 1 and 7. Arbitrary choices in the blocks have prefix discrepancies bounded by an absolute constant. The Fourier patch for this block library realizes **any prescribed** residue of $C_w$ modulo $Y$ with $O(P)$ bits, including the solution to $4C_w\equiv3^{Q-1}-2^{L-1}\pmod Y$. The patch only uses that $Y$ is coprime to 6. By (2) both complete-macro increments are multiples of $Y$ since extending a difference through fixed-grade exterior words only multiplies it by powers of 2 and 3. After freezing those motifs, the coefficient of $C_v$ in $C_0$ is $2^{2L}$, a unit, so the same argument makes $C_0\equiv0\pmod Y$. Each macro translation is now divisible by $Y$, hence so is the full period numerator. The actual reduced denominator is prime to $Y$. [Fourier patch proof and Yu bound](../renewal/CYCLE_SIEVE_REVIEW.md)

Write $D_h=B^h-A^h$ and $Q_h=D_h/(B-A)$. By the single-pulse superposition at the boundary,
\[
 x_0=\frac{C_0}{B-A}+\frac{c_1 A^{r-1}}{D_r}+\frac{c_2 A^{t-1}}{D_t}.
 \tag{4}
\]
Hence $\log_2 d\le m(r+t)$. To check $d>1$, remove from $Q_r$ the primes dividing $B-A$. The remainder $Q'_r$ is at least $Q_r/r$. Indeed $Q_r\equiv r A^{r-1}\bmod (B-A)$, and when $r\mid B-A$ the binomial expansion of $((A+(B-A))^r-A^r)/(B-A)$ has valuation exactly one at the odd prime $r$. Every prime of $Q'_r$ gives multiplicative order $r$ for $B/A$, so it divides neither $D_t$ nor $B-A$. In (4) the reduced denominator is therefore divisible by $Q'_r/\gcd(Q'_r,c_1)\ge B^{r-1}/(r c_1)$. This exceeds one in both parameter regimes below. Reduction is the same at every native phase.

## 4. Separation between distinct physical offsets

Replace the carry of each coherent motif by its mean, with weight $1/r$ or $1/t$ on $V$ as applicable. Its slope remains $\mu$. The resulting single-macro periodic boundary value is the average of the actual boundary values, since their common-slope recurrence has mean forcing $C_0/B+\lambda a_1/r+\lambda a_2/t$. The response to a single pulse of amplitude $\lambda a$ and period $h$ has values
\[
 u_j=a\lambda^{v_j}/(1-\lambda^h),\qquad
 v_j\in\{1,\ldots,h\},\quad v_j\equiv j\pmod h. \tag{5}
\]
Its range has length at most $a$ for all $0<\lambda<1$. Thus actual boundary values differ from their mean by $O(L)$ uniformly in $r,t$.

For each averaged motif and **either** chosen branching order $U$ or $V$, realize its averaged map by retaining the digit multipliers and multiplying every odd additive offset $1/2$ in that motif by the common factor $b_{\rm mean}/b_{\rm chosen}$. This factor is between two positive absolute constants by (2). Thus the averaged endpoints are identical for both choices. An intermediate averaged value at physical offset $h$ depends only on the choice in its own motif if it is interior. Choose that order to match the actual flag for the physical phase being compared. Its distance from the actual value is $O(L)$: the boundary difference is $O(L)$, the preceding two motifs contribute $O(L)$ in changed offsets, and propagation through any remaining common segment has bounded multiplier. We call these averaged values virtual phases.

Every such positive virtual $m$-periodic system has heights uniformly $\asymp m/\delta$. At any phase its complete return slope is $e^{-\delta}$; its full affine carry is $\asymp m$ by the prefix-discrepancy bound and the fixed positive upper and lower bounds for its odd offsets. Its distinct phases have separation $\gg m$, uniformly over the motif choices. To prove this, consider complementary arcs of positive lengths between two distinct phases. Their logarithmic defects add to $\delta$ and by (1) each has absolute value at least $\delta$. One of the two multipliers is greater than one. If the shorter cyclic time is at least $c_0m$, that expanding arc increases height by at least its positive offset $\gg c_0m$. If the shorter cyclic time $h<c_0m$, the multiplier on this arc differs from one by at least $c\delta$ by (1) and boundedness of its multiplier. Applied to its source of height $\gg m/\delta$, the multiplicative contribution to the absolute displacement is $\gg m$, while its offset is at most $Ch$. Choosing $c_0$ sufficiently small proves linear separation in this case as well. This also sharpens the base-cycle separation in [CYCLE_INDEX.md, §3.1](CYCLE_INDEX.md).

Two different physical offsets with compatible choices lie on one such virtual system. This includes offsets in different motifs and offsets within the same motif with identical flags. Their actual distance is at least $c m-O(L)$. If both cuts are inside the **same** motif with opposite choices, measure their virtual positions from the identical averaged boundary of that motif. Their positive prefix multipliers have ratio $3^u/2^{h-h'}$ and are individually bounded away from zero and infinity. For $h\ne h'$ inequality (1) bounds their difference below by $c\delta$; if $h=h'$ the ratio is 3 or $1/3$, because the two prefixes have followed the same initial part of $w$ after opposite first digits. Their common boundary input is $\gg m/\delta$ and the two local offsets are $O(L)$. Including the $O(L)$ deviations of the actual phases proves separation $\gg m$ for distinct offsets in this incompatible case and for the equal-offset opposite-flag case. All actual heights are also $\asymp m/\delta\gg m^2$.

## 5. Separation at a common physical offset

At a common offset it remains to compare macro times $j\ne j'\pmod{rt}$ whose flags agree in the currently occupied motif if there is one. Their prefix multipliers $R_h$ are the same and satisfy $R_h\ge c>0$. Dividing their height difference by $R_h$ expresses it as the sum of the two track differences from (5). For each motif entirely processed before the offset, replace $u_j$ by $u_j+a{\bf1}_{h_0\mid j}=u_{j+1}/\lambda$ where $h_0=r$ or $t$ is the track period. Indeed the full normalized contribution of a processed motif at this cut, divided by the cut's prefix multiplier, is $a=c_i/A$. A partly processed motif with equal flags contributes identical additional constants to both compared inputs. Unprocessed motifs contribute none. Consequently every track is compared either before or after its pulse, at the same stage for both macro times.

Assume $\max(r,t)\delta=o(1)$. For $1\le v,v'\le h_0$, the mean value theorem applied to $e^{-\delta v}$ gives
\[
 \frac{\lambda^v-\lambda^{v'}}{1-\lambda^{h_0}}
     =\frac{v'-v}{h_0}+O(h_0\delta), \tag{6}
\]
and the same estimate holds after multiplication by $1/\lambda$. The error bound is uniform. Before or after the pulse, $v$ is a bijection of the phase modulo $h_0$. Thus the normalized difference, divided further by $a_2$, has the form
\[
 \mu\,i/r+j_0/t+O((r+t)\delta),\qquad
 |i|<r,\quad |j_0|<t,\quad (i,j_0)\ne(0,0).
\]
Coprimality gives $|i/r+j_0/t|\ge1/(rt)$. If $|\mu-1|+C(r+t)\delta\le1/(2rt)$, all these actual gaps are $\gg L/(rt)$. Together with section 4 this covers **all pairs** of distinct physical phases.

## 6. Parameter choices

For the first theorem, the fixed two-logarithm inequality yields a finite $A_0\ge1$ with $\|j\beta\|\gg j^{-A_0}$ for all $j\ge1$. Any interval of $M$ consecutive integers, $M$ large, contains an $L$ with $\|L\beta\|\ll M^{-1/A_0}$. Indeed if $h$ is the last convergent denominator at most $M$ and $h'>M$ is the next, then $h'\ll h^{A_0}$ by the two-log lower bound and the convergent upper bound. The first $h$ multiples of $\beta$ are within $1/h$ of the uniform grid of denominator $h$, by comparing to its coprime convergent numerator. The translated grid therefore comes within $2/h$ of zero. [Two-log input used in Lagarias, proof of Theorem 3.2](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf)

Choose $2a<b<1$ and $e>0$ small enough that $2a(1+2e)<b$, $2e<b/A_0$ and $3e<1$. Take distinct primes $r,t\asymp m^e$ by Bertrand. In $[m^b,2m^b]$ use the preceding net to choose $L$ with $|\mu-1|\ll m^{-b/A_0}$, choosing $Q$ the closest integer to $L\beta$. Also $(r+t)\delta\ll m^{e-1}$. Both errors are $o(1/(rt))$, and $n=mrt\asymp m^{1+2e}$. The Yu bound and the patch estimate give $P\ll n^{2a}(\log n)^{O(1)}=o(L)$. Equations (3)–(6) imply the claimed polynomial gaps with $\kappa=(b-2e)/(1+2e)>0$, and the denominator bound gives $\eta=e/(1+2e)>0$.

For the logarithmic cutoff, fix distinct $r,t$ first and let $m\to\infty$ along the same convergents. The endpoint estimate in the [sieve review](../renewal/CYCLE_SIEVE_REVIEW.md) gives $P\ll_{r,t,\varepsilon}m/(\log m)^{2\varepsilon}$ for all large $m$. Take $L\asymp m/(\log m)^\varepsilon$ nearly neutral by the net above. Then $P=o(L)$, $L=o(m)$, $L/(rt)\to\infty$, and the required errors are $o(1/(rt))$ at fixed $r,t$. For a sequence of growing pairs of primes, choose $m$ separately so the minimum and the least gap exceed any successive target. Equation (4) gives $\log_2 d/n\le1/r+1/t\to0$ along this diagonal.

As a consequence the primitive pressure formula $(\theta-s)_+$ of [PRIMITIVE_PRESSURE.md](PRIMITIVE_PRESSURE.md) holds with both the least phase and the separation of every pair required to exceed $R$, even at this logarithmic sieve cutoff. The high-entropy lower branch already has increasing physical separation, and the cycles above provide the zero lower branch at genuine least periods. The upper bound is unchanged by restricting the counting set.
