# All positive visitors through the native odd rank and the extra ternary depth

Use the ordinary shortcut $T$, the full odd map $U(x)=(3x+1)/2^{v_2(3x+1)}$, and any $m=11+162j$, $j\ge0$. Set
\[
 N=2^m,\qquad 81z+271=128N,\qquad H=v_2(3^{m+1}-1),\qquad
 V=(3^{m+1}-1)/2^H,\qquad R=v_3(N-590).
\]
Here $V$ is an ordinary positive odd endpoint, $H=2+v_2(m+1)$, and $R\ge5$. The native source $N-1$ reaches $V$ in $m+1$ full odd departures and $m+H$ physical shortcut steps.

**Exact classification.** Every positive $y\le z$ that visits $V$ using at most $m+1+R$ odd departures appears in the following table. There is no restriction on the physical clock. Each row occurs at the displayed ordinary clock if its odd rank fits the budget. At $R=5$ the row with $r=6$ drops out. All other rows occur for every parameter.

| Positive start $y$ | Extra rank $r$ relative to $m+1$ | Extra physical steps relative to $m+H$ | Residue modulo 16 |
|---|---:|---:|---:|
| $3N/2-1$ | $-1$ | $-1$ | $15$ |
| $(8N-13)/9$ | $2$ | $3$ | $11$ |
| $N-1$ | $0$ | $0$ | $15$ |
| $(256N-623)/243$ | $5$ | $8$ | $11$ |
| $(32N-61)/27$ | $3$ | $5$ | $9$ |
| $(4N-5)/3$ | $1$ | $2$ | $9$ |
| $(1024N-2735)/729$ | $6$ | $10$ | $9$ |
| $(128N-271)/81=z$ | $4$ | $7$ | $1$ |

In particular, any such $y$ satisfies $16y\ge9z$, and the only canonical $17\bmod48$ visitor is $z$ itself. The smallest source attains $16y=9z+7$. Through the shorter budget $m+1$ the only visitors are $N-1$ and $3N/2-1$. At $m=11$ the eight starts in increasing order are $1819,2047,2155,2425,2729,2873,3071,3233$, with odd ranks $14,12,17,15,13,18,11,16$ respectively.

The eight affine forms are the prior PR195 fixed-word result at the simultaneous limiting coordinates $N_2=0,N_3=590$. The later PR195 terminal-even-cost calculation reuses the positive and reflected readout with a wider slope cap and minimizes first-hit even cost on the upper triple. Its two fixed-word minimizers include the $619$ and $929$ rows above. The common ancestor-exchange identity in that source gives a separate upper certificate for inverse shifts of the original parent. The new classification is for every actual member of the hard progression, every source-dependent ordinary path in the stated rank range, and its native physical endpoint $V$ after the full long ascent. PR192's earlier results concern the first valuation-scale window near the peak, or the total length of an undirected walk under separate controls. [PR195 eight forms](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/FINITE_COVER_BARRIER.md) · [PR192 native window](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/POSTPEAK_DELAY.md) · [PR192 cut-walk depth](https://github.com/GettysburgResearch/collatz/blob/75eac0cbc744469ae2886bc2f140685c484e9fe7/research/astra-sixhour-20261127/descent/CUT_WALK_DEPTH.md) · [PR195 terminal even cost](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/cycles/TERMINAL_EVEN_COST.md) · [PR195 actual upper minima and ancestor exchanges](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/ordinary/EVEN_MINIMUM.md)

## A reflected fixed point is forced on the actual long tail

Read a terminal segment of $q\le m+1$ full odd departures backwards from $V$. Let $x_i$ be its positive ordinary vertex after $i$ reverse steps, $D_i$ the accumulated physical divisions and $B_i=D_i-i$ their excess over the odd count. Define the scaled signed magnitude $A_i$ by
\[
                2^H x_i+A_i=2^{D_i}3^{m+1-i}.
\]
Then $A_0=1$ and at a reverse step of exponent $1+e$,
\[
                 3A_{i+1}=2^{1+e}A_i+2^H .
\]
Consequently $0<A_i\le2^H2^{B_i}$. When $D_i\ge H$, the displacement equation shows that $a_i=A_i/2^H$ is a positive integer. It is odd when $D_i>H$. Every noninitial magnitude satisfies $3A_i>2^H$.

Suppose first that a magnitude reaches $A_i=2^H$. Up to free exponent-one loops at that point, its reverse itinerary from $A_0=1$ must be either $(H+1)$ or $(H-1,2)$. Indeed, reading in the forward direction from the normalized magnitude one, one reversed leg gives $1/2^e$ for a total exponent $1+e$. An intermediate value must exceed $1/3$, leaving the choices $1$ and $1/2$. From $1/2$ every next positive value is at most $1/4$ and must be the terminal $2^{-H}$. This costs at least $H-1$ excess divisions. Every subsequent integral reverse step has $3a'=2^{1+e}a+1$, preserves the reflected ordinary predecessor graph of $1$, and satisfies $a'\le2^e a$ for $a\ge1$. Therefore at an arbitrary endpoint after this visit
\[
 A_q=2^H a,\qquad 0<a\le2^{B_q-(H-1)},
\]
and $a$ reaches $1$ under the reflected full odd map $(3a-1)/2^{v_2(3a-1)}$.

If there is no such visit, every magnitude continued after $i\ge H+1$ is odd, exceeds one, and cannot be three because the next inverse equation would contradict divisibility by three. It is therefore at least five after normalization. This yields $15a'\le11\cdot2^e a$. With $n=q-(H+1)>0$, the cap at the initial part of the history and the positive integral terminal give
\[
                      15^n\le11^n 2^{B_q},\qquad 3n<7B_q,
\]
where the last inequality uses $15^7>8\cdot11^7$. The dichotomy follows along the *same* inverse history. [Kernel projection, center cost and spectral bound](NativeShadow.lean)

## Sources at or below native rank

Take an odd $y\le z$ reaching $V$ in $q\le m+1$ departures. Write $B=B_q$, $t=m+1-q$. At its starting endpoint the displacement and cap imply
\[
 2^H y+2^H2^B\ \ge\ 2^{q+B}3^t
  =2^B\,2^{m+1}(3/2)^t .
\]
For $m\ge H+2$, $B\ge H$ would force $y\ge2^{m+1}-2^H>z$. Thus $B\le H-1$. Also $(3/2)^t\le2^H$ follows by dividing and using $y+1\le2^{m+1}$, so $t\le2H$. Under $3(m-3H)\ge7H$ the unmarked alternative $3(q-H-1)<7B$ is impossible. The marked alternative now forces $B=H-1$ and $a=1$. Hence $2(y+1)=2^q3^t$. The cap excludes $t\ge2$, leaving exactly the first native ascent point and its successor. [Kernel native classification](NativeVisitors.lean)

## Projecting the extra departures back to small positive integers

For an odd visitor with rank $m+1+r$, cut off its initial $r\le R$ departures at $u$. They obey $2^r(u+1)\le3^r(y+1)\le3^r2^{m+1}$. On the remaining $m+1$ departures the cap for $A$ and $2^H u+A=2^{m+1+B}$ give $2^B2^m\le2^H u$. Thus
\[
 2^{B+r}\le2^{H+1}3^r,\qquad 5B\le5(H+1)+3r,
\]
using $3^5<2^8$. If $7(5(H+1)+3R)\le15(m-H)$, the unmarked lower bound is again impossible. Hence, with $\ell=B-(H-1)$, the cut has the exact form
\[
 u=2^\ell N-a,\qquad 1\le a\le2^\ell,
 \qquad a\text{ reaches }1\text{ under the reflected full odd map}.
\]

Set $c=590\cdot2^\ell-a$. Since $u-c=2^\ell(N-590)$ is an even multiple of $3^r$, the initial $r$ steps from $y$ to $u$ project to a positive odd ordinary $w$ reaching $c$ in the same word of physical cost $f$. The relations are
\[
   w u\le c y,\qquad y=w+(2^{f+\ell}/3^r)(N-590).
\]
Using $u\ge2^\ell(N-1)$ and $c\le590\cdot2^\ell$ gives $w\le932$ when $N\ge2048$. Indeed $933(N-1)>590\cdot128N/81$ in this range. [Kernel positive projection and actual physical word](AnchorRoute.lean)

The complete positive odd forward union from the 466 odd inputs $w\le932$ has maximum $83501$. Each reaches one. The only value in this union satisfying $589\cdot2^\ell\le c<590\cdot2^\ell$ for any $\ell\ge1$ is $18863=590\cdot2^5-17$. But the reflected odd orbit of $17$ cycles through $17,25,37,55,41,61,91$, and cannot reach one. Thus $\ell=0$, $a=1$, and $c=589$. The seven positive starting values reaching $589$ are exactly $523,589,619,697,785,825,929$, at the ranks and clocks in the table. These lifts all occur because $N-590$ is an even multiple of $3^r$ for each retained rank. Each listed start is odd. Doubling any of them exceeds $z$, so initial even steps cannot add a positive visitor below the cap. [Kernel finite positive and reflected lookup](AnchorLookup.lean) · [Kernel classification and realizing paths](NativeClassification.lean)

## Applying the numerical hypotheses throughout the progression

For all $m=11+162j$, LTE gives $H=2+v_2(m+1)$ and $R\ge5$. Since $3^R<N$ and $8^R\le9^R$, one has $3R<2m$. Hence $m\ge50H+35$ suffices for both rank estimates. This comparison holds for all integers $m\ge659$ with this definition of $H$: on $659\le m\le1022$ use $H\le11$, and at each later binary boundary $m=2^b-1$ the left side increases by at least $1024$ while the bound increases by $50$. It also holds at $m=335,497$. At $m=173$ use the direct numbers $H=3,R=5$ in the two rank estimates. The full $m=11$ case is a finite exhaustive comparison of every positive $y\le3233$ and every permitted odd departure count. [Exact checker](check_native_shadow.py) · [Archived controls](NATIVE_SHADOW_CONTROLS.json)

The Lean statements give the uniform necessary rows and the realizing odd paths at the displayed numerical hypotheses, including the lower height and canonical cutoff. The all-progression LTE and small-exponent specialization, and the reduction of an initial even source, are written deductions with the stated finite replay. The theorem needs no basin, least-counterexample, cycle or verification-floor hypothesis. It concerns visitors reaching this particular normalized endpoint. A later merger, a different endpoint on the same component, and larger odd rank remain possible. The [positive-anchor construction](ANCHOR_OVERHEAD.md) produces subfloor canonical visitors on explicit subclasses beyond the present bound.
