# The cost of reducing the first upper clock

Use the ordinary positive shortcut $T(2n)=n$, $T(2n+1)=3n+2$. A canonical source is $17$ modulo $48$. Consider every member of the canonical rank-three row
\[
 H=18+162t,\qquad 81z+271=2^H,\qquad t\ge0.
\]
Its upper $3z$ first hits $1$ at clock $H$. Its lower $z$ reaches $2^{H-7}-1$ at clock seven and ascends to $3^{H-7}-1$ at clock $H$. The three upper odd departures occur at zero-based clocks $0,1,8$. This row comes from the prior Mersenne analysis. [Prior row and offset analysis](../../six-hour-20261127/coupling/EARLIER_OFFSETS.md) · [Ordinary row proof](ClockBarrier.lean)

**Kernel-checked.** Suppose a canonical replacement $y$ satisfies $T^h(3y)=1$ for some $h<H$.

1. It obeys $2y+31\le z$.
2. If $T^i z=T^j y$ and $T^k(3z)=T^l(3y)$, then $H<5(B+9)+4$ for $B=\max(i,j,k,l)$. All four clocks may differ. The conclusion holds for every $t$ and every candidate $y$.
3. Even without an upper-arm meeting, suppose $T^i z=T^j y$ and $T^e(3y)=2^v$, $2\le e$, $e+v<H$. Then $H<6(B+7)+4$ for $B=\max(i,j,e)$. A candidate whose lower joins the row early must use a late last odd upper departure. Every good canonical upper has at least two initial odd departures, so its first terminal power-of-two tail occurs at a clock $e\ge2$.

The first bound is asymptotically sharp using upper certificates alone. For $H\ge180$ on the row, take $81y=2^{H-1}-15-2^{135}$. This gives a positive canonical integer: the congruence holds at $H=180$ and persists since $2^{162}\equiv1\pmod{243}$ and all powers have the required factor of $16$. Its upper has odd departures exactly at $0,1,135$, then reaches one at $H-1$. After two steps its value is $2^{133}(2^{H-136}-1)/3$. After the next $133$ even steps, the odd quotient takes one step to $2^{H-137}$. Thus $z-2y=(2^{136}-241)/81$ is constant and $y/z\to1/2$. This written sharpness example makes no assertion about a lower merger. [Affine certificate and factor-two bound](UpperClock.lean) · [Physical linear clock bounds](ClockBarrier.lean) · [Independent controls](UPPER_CLOCK_CONTROLS.json)

## Proof

For the $s$-step word at $x$, let $g_s$ count odd departures and define its integer intercept $A_s$ by $2^sT^s x=3^{g_s}x+A_s$. At an even step the intercept stays fixed. At an odd step it becomes $3A_s+2^s$. In particular $A_s+2^s\le3^s$. The first two departures from $3y$ are odd, with intercept five. If there is a third odd departure then $2^h\ge81y+5$. Since $h<H$, this gives $162y\le81z+271$. If there are just two odd departures then $2^h=27y+5$. The residue $2^H\equiv1\pmod{27}$ excludes $H-h=1,2$, supplying the same inequality. The residues of $y,z$ modulo $48$ give $2y+31\le z$. [Word extension and forced canonical prefixes](UpperClock.lean)

For the paired bound pad the native lower clock to $I\ge7$ and the native upper clock to $K\ge9$. Pad the comparison clocks by the same respective amounts to $J,E$, with $E\ge2$. All four new clocks are at most $M=B+9$. Suppose $H\ge5M+4$. At the padded lower meeting $L+1=2^{H-I}3^{I-7}$. At the padded upper meeting the point is $2^{H-K}>2$. The resulting upper certificate for $y$ has length $h'=E+H-K\le h$, since a power of two greater than two has its first hit at its exponent and the terminal $1,2$ cycle cannot have been entered before that meeting.

Let $p,r$ count the odd departures at $J,E$ on the lower and upper of $y$, with intercepts $A,D$. Eliminating $y$ from the two affine equations gives
\[
 2^{h'}3^p+3^{r+1}(A+2^J)
   =2^{J+H-I}3^{r+1+I-7}+3^pD.
\]
Both remainders lie below $2^{4M+3}$, while both leading terms are divisible by this power. Hence the remainders agree. The leading terms agree separately, so $h'=H+J-I$ and $p=r+1+I-7$. Both starting upper departures are odd, so $r\ge2$. There must be at least three even departures in the lower word. Otherwise, since $p\ge3$ and the canonical lower begins odd, even, odd, even, every departure after the fourth is odd. This gives $A+2^J=23\cdot3^{p-2}$. Together with equality of remainders it forces $3\mid D$, impossible because $3^{r+1}y+D=2^{h'}$. Consequently
\[
              H-h'=6-r-(J-p)\le3-r.
\]
A strict improvement forces $r=2$ and $H=h'+1$. The upper again has intercept five and $2^{h'}=27y+5$, contradicting $2^H\equiv1\pmod{27}$.

For the unpaired upper-tail version take $M=B+7$, keep the same padded lower meeting, and put $h'=e+v$. The upper certificate yields $y\le2^{h'}$. The ordinary step bound $T(n)\le2n$ gives $L\le2^{J+h'}$. The native lower satisfies $L+1\ge2^{H-I}$. Thus if $H\ge6M+4$ then $h'\ge4M+3$, and the same remainder argument applies. [Exact lower and upper paths, modular separation and the two physical corollaries](ClockBarrier.lean)

Earlier work gives depth obstructions for sparse hard anchors and postpeak comparisons with earlier Mersennes. These statements address the first upper hitting clock, all parameters in this rank-three row, and unrestricted candidate sources with independent physical clocks. The bounds still allow clocks proportional to $H$ or larger. They establish no implication between the two basin labels. **Collatz remains open.** [PR192 cut-walk depth](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-sixhour-20261127/descent/CUT_WALK_DEPTH.md) · [PR192 fixed-peak delays](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-unconventional-20261126/descent/POSTPEAK_DELAY.md) · [Prior all-visitor results](../../six-hour-20261127/coupling/PEAK_RIGIDITY.md)
