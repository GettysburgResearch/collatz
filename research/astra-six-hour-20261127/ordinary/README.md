# Ordinary Mersenne returns at the bounded three-odd gap

Use \(T(2n)=n,\ T(2n+1)=3n+2\), and write \(C(x)\) when \(x\) reaches one. On the bounded-cycle branch, a surviving least canonical three-odd reverse disagreement has
\[
 j=11+162m,\quad M_j=2^j-1,\quad P_j=3^j-1,\quad 81z+271=128\cdot2^j .
\]
Its actual lower trajectory satisfies \(T^7z=M_j\), then \(T^jM_j=P_j\). The [bounded minimum estimate](../../astra-unconventional-20261126/renormalization/BOUNDED_RANK_THREE.md) gives the strong floor
\[
            w>0,\quad1024w<243z\quad\Longrightarrow\quad C(w).        \tag{1}
\]
All physical peak identities below are unconditional. Only the implication from a peak meeting to \(C(z)\) uses (1).

## The two signs at the original positive sources

Write \(m=4^rv\) with \(r\ge43\), and let \(v\) be the given positive integer. In each of the following two cases the two original peaks \(P_j,P_{j-5}\) agree at the indicated common postpeak clock. Accordingly (1) gives \(C(z)\) for every source satisfying either row.

| Supplied arithmetic condition | Common clock | Odd counts in the final block, original and earlier |
|---|---:|---:|
| \(3^r v\equiv 1\bmod2^{64}\) | \(2r+67\) | 30, 33 |
| \(3^r v\equiv-1\bmod2^{62}\) | \(2r+65\) | 27, 30 |

To see the floor comparison, put \(n=j-5\). Already \(n+2\le j\) implies \(1024(2^n-1)<243z\) by the source identity. Thus \(M_n\) is positive and good. Its \(n\) native ascent steps reach \(P_n\), the stated merger transfers its label to \(P_j\), and the original lower prefix transfers the label to \(z\). This works with every supplied peak meeting having \(n+2\le j\).

For the two signs put \(A=3^{162}\), \(B_s=(A^{2^s}-1)/2^{s+3}\). These are odd integers and
\[
 B_{s+1}=B_s+2^{s+2}B_s^2,\qquad B_s\equiv B=164232366001155405\bmod2^{64}\quad(s\ge62).
\]
Write \(u=(A^m-1)/2^{2r+3}\) and \(U=3^ru\). A binomial expansion shows \(u\equiv vB\bmod2^{64}\). A perturbation by \(2^Hc\) has the same first \(H\) parities and displaces the final site by \(3^pc\), with \(p\) the actual odd count. At clock 89 the positive anchors \(P_{11},P_6\) are at 1 and 2 with 45 and 47 odds. Each subsequent two-step cycle lap contributes one odd. Applying the perturbation identity at \(H=2r+3=89+2(r-43)\) therefore gives the exact ordinary sites
\[
                T^H P_j=1+3^{13}U,\qquad T^H P_{j-5}=2+3^{10}U.
\]
At \(U=B\), the two displayed rays meet at \(2922489638071279607\) after 64 steps. At \(U=(-B)\bmod2^{62}=4447453652426232499\), they meet at \(11724704031194517008\) after 62 steps. In each case the earlier branch takes exactly three more odd steps, so the meeting persists on every lift of that \(U\) residue. Both branches use only positive integer anchors. [Physical lifts and exact terminal blocks](OrdinaryDerivative.lean) · [Normalized power and both signs](OrdinaryPower.lean) · [Independent exact replay](check_ordinary.py)

The stronger bounded-cycle floor is essential to the new choice of earlier gap. The [earlier logarithmic family](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/unconventional/LOGARITHMIC_POWER_FIBER.md) paid a factor \(2^{40}\). The earlier positive and negative derivative blocks use 2,957 and 334,711 clocks, respectively, at gaps 63 and 40. [Earlier negative control](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/unconventional/GEOMETRIC_SLICES.md)

## Uniform perfect powers and signed multipliers

For every ordinary base \(b\ge0\) and \(d\ge494\), set the original supplied parameter \(m=b^{2^d}\). Its \(z\) reaches one under (1). For an even base \(d\ge63\) suffices. At \(b=0\) the actual parent is 3233 and reaches one in 107 shortcuts.

For a positive even base write \(b=2^a c\) with \(c\) odd. Put \(2r=a2^d\) and \(v=c^{2^d}\). Then \(r\ge43\) and \(3^r v\equiv1\bmod2^{64}\), by the elementary odd-power rotation modulo powers of two. More generally, every preassigned positive multiplier \(f\) with \(f\equiv1\bmod2^{64}\) or \(f\equiv-1\bmod2^{62}\) gives the actual parent at \(m=b^{2^d}f\) the corresponding merger in the table. The negative-sign statement permits all positive \(f=2^{62}q-1\), \(q\ge1\).

For an odd base, \(m\equiv1\bmod2^{496}\). At \(m=1\) the ordinary peaks \(P_{173},P_{164}\) meet at clock 499 with 241 and 250 odd inputs. Their common site is \(206172918000360585496211725112706136396363302641\). Writing \(s=162(m-1)\), one has \(3^s\equiv1\bmod2^{499}\), so the physical lift gives the same meeting for peaks \(P_{173+s},P_{164+s}\). Both augmented grades are 414. The prior general least-defect theorem used \(d\ge2956\) and a weaker floor. The present universal-base bound applies to the bounded branch with (1). [Kernel implications for all bases and both signed even-base branches](OrdinaryPower.lean)

## Ordinary controls for changing the earlier exponent

At the following positive e6 indices the native terminal charge \(2(j+p)-h\), measured at the first \(T^hP_j=1\), exceeds the charge of every \(P_t,\ 1\le t<j\). Two extra steps at 1 preserve the charge. A synchronized merger with equal augmented grades would force equal terminal charges, at any length and with any choice of earlier exponent. Thus these ordinary sources show that even an input-dependent earlier exponent cannot always give such a merger.

| \(j\) | Clock, odds at first one | Native charge | Maximum charge at smaller exponents | First clock below (1) | First native clock meeting any complete earlier Mersenne orbit |
|---:|---:|---:|---:|---:|---:|
| 11 | 89, 45 | 23 | 16 | 54 | 58 |
| 983 | 7,803, 3,940 | 2,043 | 1,791 | 2,636 | 7,726 |
| 2,117 | 16,934, 8,567 | 4,434 | 4,078 | 5,941 | 16,913 |

For example \(T^{7726}P_{983}=T^{1887}P_{277}=1178\), and \(T^{16913}P_{2117}=T^{198}P_{27}=89\). The exhaustive replay includes every initial ascent, the complete forward orbit through the first one, and the \(1,2\) tail for every earlier positive exponent. It computes the earliest native meeting across all earlier clocks. Each example has a direct subfloor return well before this first meeting. [Exact receipt](../../../reports/astra-six-hour-20261127/ordinary/exact-controls.json) · [Reproducer](check_ordinary.py)

At the auxiliary derivative unit \(U=5\), the pair in the table has unequal terminal charges. This tests a pair of ordinary affine branches and does not identify \(5\) as the normalized unit of any original e6 exponent. A claim that a fixed menu of earlier peaks covers every derivative input needs a separate argument. [Nearly linear ordinary windows and all-clock simple-segment bounds](CLOCK_SEPARATION.md)

The moving-clock families do not establish closure for every original \(m\). A proof that every surviving actual gap-six parent has some ordinary subfloor return, paid canonical comparison or other contradiction is still missing.

## Sharpness of the odd-base bound

On odd bases, \(d=494\) is the exact threshold for a uniform bound on both postpeak clocks, including both full ascents and allowing any input-dependent earlier exponent. More generally, over every positive power degree \(n\), such a finite uniform budget exists precisely when \(2^{494}\mid n\), and then it is exactly 499. Below it every fixed budget fails on arbitrarily large original ordinary bases. The lower bound uses a single rational control whose complete signed-offset fiber has a finite 257-exponent test, followed by a lift back to actual odd-base powers. [Exact quantifiers, obstruction and positive theorem](SHARP_ODD_POWER.md)
