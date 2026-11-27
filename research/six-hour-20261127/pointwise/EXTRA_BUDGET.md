# Exact extra-depth minima at the seven phases of the negative 17-cycle

The frozen seven-phase theorem supplies the baseline. Let $R\ge7$, $z\ge1$, and let $(t,a,h)$ be one of $(17,0,0),(25,1,1),(37,2,2),(55,3,3),(41,4,5),(61,5,6),(91,6,7)$. Write
\[
 k=\lfloor(R-a)/7\rfloor,\quad p=7k+a,\quad H=11k+h,\quad \delta=R-p,
 \quad X=2\cdot3^Rz-t,\quad V=2^{H+1}3^\delta z,\quad n=V-17.
\]
For the positive accelerated odd map $U(u)=(3u+1)/2^{v_2(3u+1)}$, $M_j(v)$ is the minimum over positive odd starts reaching $v$ in at most $j$ odd departures, including the empty word. The baseline theorem gives $M_R(X)=n$, a unique optimizing script with $p$ departures, and a reflected comparison $u+m>5mV/102$ for every odd $u$ reaching $X$ in exactly $R$ departures. The proof below always stops the signed projection at $R$.

## A sharp three-step composition theorem

**Theorem 1.** For $0\le s\le3$,
\[
                           M_{R+s}(X)=M_{\delta+s}(n).
\]
Every optimizing trajectory passes through $n$ with at most $\delta+s$ departures before following its $p$-departure trajectory to $X$. A fourth extra departure can bypass $n$, even when $n$ has no proper positive odd ancestor at any depth.

A competitor $y\le n$ that uses at most $R$ departures equals $n$ by the baseline. Otherwise suppose $U^{R+j}(y)=X$, $1\le j\le s$, and cut at $u=U^j(y)$. Since $U(w)+1\le(3/2)(w+1)$,
\[
 u\le(3/2)^s(V-16)-1 <(3/2)^s V.
\]
The reflected $R$-step projection of $u$ ends at a positive odd magnitude $m$ viewed from $X$. The strict comparison above implies $m(5V/102-1)<(3/2)^sV$. As $V\ge256$, we have $V/(5V/102-1)<23$, hence $m<23(3/2)^3<78$.

Here is the finite signed computation in full. Starting at each positive odd $m<78$, iterate $S(w)=w/2$ for even $w$, $(3w-1)/2$ for odd $w$, to the first repeated vertex or the first visit to 17. The entries that reach 17 have the following odd and physical first-arrival clocks $(b,c)$.

| $m$ | 17 | 21 | 23 | 25 | 31 | 33 | 37 | 41 | 45 | 49 | 55 | 61 | 67 | 73 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $b$ | 0 | 3 | 1 | 6 | 2 | 7 | 5 | 3 | 8 | 6 | 4 | 2 | 7 | 5 |
| $c$ | 0 | 5 | 2 | 10 | 4 | 12 | 9 | 6 | 14 | 11 | 8 | 5 | 13 | 10 |

Every $m$ reaching the marked phase must eventually reach 17. Extend its signed path from $t$ through the cycle back to 17 as needed. Comparing its total clocks with the unique cycle shows $b\equiv R-a\equiv\delta\pmod7$, with the same clock relationship in physical time. If $b=\delta$, then $u$ visits the actual principal source $n$ after exactly $\delta$ odd departures: the signed point there is 17, and its deterministic last $p$ departures take $H$ clocks to $t$, so its positive displacement is exactly $V$. This also handles $b=0$.

Only $m=33,45,67$ can have $b=\delta+7$. Their physical prefix has $c$ clocks, followed by one fewer $11$-clock lap than the reference script. Thus $u+m=2^{c-11}3^{-\delta}V$. This identity is still valid when the original arrival at $t$ precedes the first visit to 17: append the remaining cycle arc from $t$ to 17 on both sides before comparing. Consequently the three cut points are

| $m$ | $\delta$ | $u$ |
|---:|---:|---:|
| 33 | 0 | $2n+1$ |
| 45 | 1 | $2I_2(n)+1$, where $I_2(n)=(4n-1)/3$ |
| 67 | 0 | $4n+1$ |

In the middle row $n\equiv1\bmod3$ so $I_2(n)$ is a legal positive odd ancestor and exceeds $n$. Write $J(x)=(2x-1)/3$ on the reals. Every inverse exponent is at least one and $J^j(x)+1=(2/3)^j(x+1)$. At $u=4n+1$, even $J^3(u)>n$ (recall $n\ge239$). At either cut of the form $2w+1$, where $w\ge n$, consider a script with at least one exponent at least two. Monotonicity of the inverse branches in the exponent and input bounds its endpoint below by a composition with one $I_2$ and all other exponents one. If the exceptional exponent is taken at inverse position $i$, then the endpoint $y'$ satisfies
\[
 y'+1=2(2/3)^j(u+1)-(2/3)^{j-i+1}
 \ge 4(2/3)^3(n+1)-1 > n+1.
\]
If instead all exponents are one, ordinary legality is equivalent to $3^j\mid u+1=2(w+1)$. Thus $J^j(w)$ is a legal ancestor of $w$, and is strictly smaller than $J^j(2w+1)$. It reaches $n$ in $j$ or $j+1$ departures according as $w=n$ or $w=I_2(n)$. Those budgets are at most $\delta+s$. A trajectory from any exceptional cut is therefore either too large or strictly dominated by one passing through $n$. Conversely every $\delta+s$ ancestor of $n$ reaches $X$ within $R+s$ by concatenation. This proves the equality and passage assertion.

**Sharpness on an infinite family.** Take $t=17$, $R=7k$, $k\ge1$, and $2^{11k+1}z\equiv77\pmod{81}$. This congruence permits infinitely many positive cofactors in a primitive residue class. Here $n\equiv60\bmod81$ is divisible by three, hence has no proper odd ancestor. Put $u=2n+1$. The signed path from 33 enters the 17-cycle at phase 61 and reaches 17 after seven odd departures and twelve clocks. Its ordinary lift from $u$, followed by $k-1$ full laps, ends at $X$ in $R$ departures, because $u+33=2V$. Equivalently all prefixes follow from the even displacement $2V$ through $11k+1$ clocks. From $u$ in reverse, take exponents $(2,1,1,1)$, so the result is
\[
               y=(64n-33)/81<n.
\]
Indeed $I_2(u)+1=2(4n+3)/3$ is divisible by $27$ because $n\equiv60\bmod81$, and $u\equiv1\bmod3$. This gives $R+4$ legal departures. At $k=1,z=14$, $n=57327$, $X=61219$, and the exact value $M_{11}(61219)=45295$ is additionally verified by the independent finite enumeration. The forward exponents of the latter source are $(1,1,1,2,1,1,1,1,3,1,4)$. A prior rStation argument gives the same affine four-extra source $(64n-33)/81$ on a different original-word cylinder, via a $(1,2,1)$ prefix; the present proof concerns the complete $R$-step seven-phase minimum and its three-extra composition law. [Paper 1/v3](https://rstation.ai/problems/collatz/papers/1/v3) · [Discussion](https://rstation.ai/r/collatz/posts/2)

## Closed first-extra formula

**Corollary 2.** The baseline $n$ remains the minimum at $R+1$ unless one row below applies and its $u\equiv2\pmod3$. In that case $M_{R+1}(X)=(2u-1)/3<n$.

| $\delta$ | $u$ |
|---:|---:|
| 0 | $V-17$ |
| 1 | $4V/3-23$ |
| 3 | $32V/27-21$ |
| 6 | $1024V/729-25$ |

For a strict challenger the first step has exponent one because $u\ge M_R(X)=n$ and every positive inverse with exponent at least two exceeds $u$ for $u>1$. Hence $u<(3/2)V-25$. The same potential bound as above gives $m<31$ since $V>306$ (for $R\ge8$ use $V\ge2^{R+1}$; for $R=7$ the seven values of $V/z$ have minimum 768). The table leaves only $m=17,23,21,25$ respectively, whose $(b,c)$ determine the four formulas. In each row $\delta=b$, so following the physical path from $m$ to 17 lifts from $u$ to $n$; its displacement $u+m=2^c3^{-\delta}V$ is an even multiple of $2^c$. The displayed candidates all satisfy strict improvement when legal, by their formulas and $V\ge512$. This proof tests the new inverse at its actual positive endpoint.

## Arbitrarily many extra departures

**Theorem 3 (effective terminal reduction).** Set
\[
   B(s)=1400+49s,\quad K=7\left\lfloor\frac{\max(R-B(s),0)}7\right\rfloor,
   \quad R'=R-K,\quad z'=2^{11K/7}z.
\]
Every minimizer through $R+s$ begins, when reversed at $X$, with the first $K$ genuine inverse edges of its marked cycle. In particular
\[
 M_{R+s}(X)=M_{R'+s}(2\cdot3^{R'}z'-t),\qquad R'+s\le1406+50s.
\]
The remaining words have length at most $D=1406+50s$ and total division sum at most twice their length. At fixed $s$, the winning value is eventually an explicitly computable affine expression on each of finitely many classes indexed by the phase, $R'$, and $z'\bmod3^s$, uniformly in the original $z\ge1$.

An optimizer of depth at most $R$ must be the baseline and follows its $p\ge R-6$ cycle edges. Otherwise remove its first $j\le s$ forward departures; the intermediate $u$ maps to $X$ in exactly $R$ departures. Project this last segment only. Suppose its signed inverse leaves the marked cycle with $b$ remaining departures and let $w\le91$ be its actual last signed cycle magnitude. All subsequent signed magnitudes $m_i$ are distinct and off-cycle, since a return or a repetition would put them in the marked cycle under the deterministic signed forward map. If $\beta_{\rm off}$ is the departed tail's inverse multiplier, telescoping gives
\[
 \beta_{\rm off}=(m_b/w)\prod_{i=1}^b(1-1/(3m_i))\ge 1/[91(b+1)].
\]
Indeed the sorted distinct positive magnitudes are at least $1,\ldots,b$, and $1-1/(3i)\ge i/(i+1)$. This uses the distinct-state product from Paper 108, Lemmas 3 and 4.

Put $A_f=\beta_f(X+t)$, with $\beta_f$ the inverse multiplier up to the last signed cycle point. The actual cut point satisfies $u\ge A_f\beta_{\rm off}/2$. To reconstruct this bound, pass through the $R$ signed inverses with prefix multipliers $\beta_i\ge(2/3)^i$ and initial magnitude $t$. The terminal signed magnitude divided by its total multiplier is $t+\sum_{i=1}^R1/(3\beta_i)\le t+(3/2)^R\le3^R$ since $R\ge7$, $t\le91$. The ordinary value is the full multiplier times $X+t$ less this signed magnitude, and $X+t\ge2\cdot3^R$. This is the original-depth comparison in Paper 108, Lemma 2.

The same cycle prefix followed by $\lfloor b/7\rfloor$ complete inverse laps is an ordinary positive competitor of depth at most $R$, with value $A_f\lambda^{\lfloor b/7\rfloor}-w$, $\lambda=2048/2187$. Its positive legality follows by the same displacement argument through $R$ at every prefix. The winning source $y$ is no larger than this competitor, and $y+1\ge(2/3)^s(u+1)$. Therefore
\[
                 1\le182(b+1)(3/2)^s\lambda^{\lfloor b/7\rfloor}.
\]
This fails for every $b\ge1400+49s$. For the first seven possibilities, bound $b+1$ by $1407+49s$, giving at $s=0$ the strict rational inequality $182\cdot1407\lambda^{200}<1$. Each increment of $s$ increases this bound by a factor at most $(1456/1407)(3/2)\lambda^7<1$. At fixed $s$, each further increment of $b$ by seven changes the corresponding expression by at most $(1408/1401)\lambda<1$. These are integer comparisons after clearing denominators. A nondeparting segment already follows $R$ cycle edges. Thus every optimizing script shares at least $K$ letters. Their transported positive endpoint is $2\cdot3^{R'}z'-t$. Truncating an optimizing word there and conversely concatenating any residual word with the forced cycle prefix proves the exact formula.

For the final finite description, let $v=2\cdot3^{R'}z'-t$ and consider a residual ordinary source $y\le v$, since the empty word is available. Any such path of $\ell$ odd departures and total exponent $E$ satisfies $2^Ev\le4^\ell y$, by $3w+1\le4w$ at every positive odd state. Hence $E\le2\ell$. Enumerate the finite exponent words with these bounds. An inverse word of length $\ell$ is integral, exactly valued and positive precisely on its legal ternary class modulo $3^\ell$; this follows by composing $(2^e v-1)/3$ one step at a time. For $\ell\le R'+s$, only $z'\bmod3^s$ is required. Every candidate has form $\beta v-c$, $\beta=2^E/3^\ell$ and $0\le c\le D4^D$ by expanding the inverse recurrences and bounding each suffix multiplier by $4^D$. Different slopes are at least $3^{-D}$ apart. Thus for $v>D12^D$ the least available slope and the largest offset at that slope determine the value. For fixed $s$, $v$ eventually exceeds the threshold uniformly in $z$. Earlier values remain exactly decidable from the same finite list. When $R\ge B(s)$, one may use $R'=1400+49s+(R\bmod7)$; the transported cofactor residue is periodic in $K/7$ with period dividing $2\cdot3^{s-1}$ for $s\ge1$.

**Theorem 4 (an exact family at arbitrary extra depth).** If $\delta=0$ and $2^{H+1}z\equiv16\pmod{3^s}$, then for every $s\ge0$,
\[
               M_{R+s}(X)+1=(2/3)^s(V-16).
\]
All such cofactors are primitive at three for $s\ge1$, so the target does not acquire a free extra digit at this phase. Every source with at most $R$ departures is at least $n$. From any longer source, cutting at its last $R$ gives an intermediate value at least $n$, hence the claimed lower bound by ordinary growth. It is attained by $J^s(n)$: since $3^s\mid n+1$, these $s$ true inverse edges of exponent one are legal. For $s\ge1$ the strict inequality against the baseline follows from $n>1$. In particular, fix $t=55$ and $z=1$ and take $k=2\cdot3^d$, $R=7k+3$. Then $v_3(V-16)=1+d$, by $v_3(4^j-1)=1+v_3(j)$, yielding unbounded logarithmic extra depth with the exact formula at one fixed cofactor.

Paper 108 explicitly stops its positive/signed correspondence at $R$. Its bounded-terminal theorem and distinct-state comparison are specific sources for Theorem 3; the signed portion here still stops at $R$, and the new $s$ positive edges carry the additional ternary constraints. Paper 1 and the earlier discussion give three-versus-four extra-depth results for particular observed words; those do not give the composition theorem for this seven-phase family. These conclusions provide exact endpoint comparisons. They do not force a prescribed arbitrary forward orbit to reach a target with a cheaper source. [Paper 108/v1, Sections 3–5, 8](https://rstation.ai/problems/collatz/papers/108/v1) · [Paper 1/v3](https://rstation.ai/problems/collatz/papers/1/v3) · [Discussion](https://rstation.ai/r/collatz/posts/2)
