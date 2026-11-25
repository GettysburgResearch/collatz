# Arbitrarily deep ordinary mergers and a necessary denominator bound

**Status.** The Lean theorems give an unbounded family of strict smaller queries and exclude every bounded-denominator cover of the e=6 family by normalized shrinking lower-phase meetings. They do not construct a query for every ordinary parameter.

Use the positive shortcut map and write $M_j=2^j-1$. PR197 at `10d87fee615d1095990d6b7ea329126b4cf7aa5a` supplies the parent $j=11+162m, 81z+271=128\cdot2^j, T^7z=M_j$. A least reverse defect would have residue 17 modulo 48, a triple reaching one, and a lower arm that never reaches one. A smaller ordinary query with the same labels excludes that parent.

## A rational periodic center gives arbitrarily large savings

For each lap count $n\ge0$ there are cofinally many ordinary parameters $m$ with a positive $w<z$, $w\equiv17\pmod {48}$, and
$$
 T^{18+11n}(w)=M_j,\qquad T^{20+11n}(3w)=2^{j-2}.
$$
The two walks have exactly $12+7n$ and $11+7n$ odd inputs, respectively. Moreover **for every prescribed factor $F$ and parameter lower bound $L$** there is an $m\ge L$ with these meetings and $Fw<z$. This includes arbitrarily large savings on actual positive inputs. Neither the triple's basin status nor any global convergence claim is needed to obtain the lower meeting.

Start with $b=-2692031/3^{12}$, the center for the published $m\equiv5903\pmod{6561}$ row. A second rational $c=-2399/81$ has $S^7 c=-17, S^7(3c)=-55$; each entry uses four odd inputs. Both entries lie on the same eleven-step negative cycle with seven odd inputs. Define
$$
 b_n=c+(2048/2187)^n(b-c),\qquad
 w_n=c+(2048/2187)^n\left((2^{j+18}-2692031)/3^{12}-c\right).
$$
Here $b-c=13047808/3^{12}$ has binary valuation 11. The lower center reaches $-1$ at clock $18+11n$, and the upper center reaches zero at $20+11n$. The denominator of $b_n$ in lowest terms is $3^{12+7n}$, since 13047808 is prime to 3. At a parameter for level $n\ge1$, every earlier chart value $w_i$, $0\le i<n$, has reduced ternary denominator $81$. Indeed $v_3(w_n-c)=-4$ and $w_i-c=(2187/2048)^{n-i}(w_n-c)$ has strictly positive ternary valuation. The construction proceeds directly on the ordinary branches of $w_n$.

Set $N=2^{j-2}$. Choose the ternary class making
$$
 81w+2399=128\cdot 2^{11n}t,\qquad 6561\cdot 3^{7n}t=8192N+101936
$$
hold for ordinary integers $t,w\ge0$ with the specified residue. At clock seven the two values are $2^{11n}t-17$ and $3\cdot2^{11n}t-55$. Every eleven-step lap removes eleven binary digits and adds seven ternary factors to these displacements. After $n$ laps the values are $Q-17$ and $3Q-55$, where $Q=3^{7n}t$. The terminal equation gives $Q=8192k+48, N=6561k+26$. On these full affine rows eleven and thirteen further steps give $4N-1$ and $N$, respectively. In particular the paths use only positive ordinary states, even when the base chart has no ordinary comparison source at this parameter. The inequality $2048<2187$ gives strict height decrease. Its powers give arbitrarily large multiplicative savings.

**Which parameters occur?** Write $A=13047808, g=8+7n$. Integrality and the ternary query digit together require exactly
$$
 2^{11n}(2^{29+162m}+A)
 \equiv 3^g(2399+2\cdot81)\pmod {3^{g+5}} .
$$
The numerator is then divisible by $3^{12+7n}$; the quotient for $w$ has residue 2 modulo 3. Its binary residue is 1 modulo 16, since $A$ and $2^{29+162m}$ are divisible by 16 and $81w+2399$ is divisible by 16. Positive parameters large enough in the progression make $w$ positive. Modulo $3^5$ the normalized target for $2^{29+162m}$ is $-A\equiv 2^{29}\pmod{243}$. The base $2^{162}$ has exact ternary distance $3^{-5}$ from 1, and cubing increases the valuation by one. Its powers consequently cover all $1\bmod243$ classes modulo $3^{g+5}$, once per block of $3^g$ exponents. This gives exactly **one progression modulo $3^{8+7n}$** for each $n$. The Lean cofinal construction uses the previously kernel-proved ternary lifting theorem with the exact ordinary quotients. The uniqueness calculation is written.

| Laps | First residue for $m$ | Period for $m$ |
|---:|---:|---:|
| 0 | 5903 | 6561 |
| 1 | 534563 | 14348907 |
| 2 | 26990356238 | 31381059609 |
| 3 | 60756572548781 | 68630377364883 |

These are disjoint for all $n$: the congruence forces $v_3(2^{29+162m}+A)=8+7n$. At every $n\ge1$ the common congruence $2^{29+162m}=-A\pmod {3^{14}}$ gives $m=3122\pmod {19683}$. This residue lies outside the seventeen published rows. The countably many new progressions do not cover that whole residue or the whole parameter space. [RationalCenterPump.lean](RationalCenterPump.lean) · [Independent physical and modular replay](check_rational_pump.py)

## A lower meeting alone forces a new ternary digit

For $m=3^kt$, take a positive ordinary $w\equiv17\pmod {48}$ and a normalized typed lower word with $d+u$ odd and $E$ even inputs, where $0\le u\le j$. Its clock is $h=d+E+u$. Assume
$$
 T^h(w)+1=2^{j-u}3^u,\qquad 81\cdot2^{d+E}<128\cdot3^d.
$$
**Then $d\ge k+5$**. No upper word, common upper phase, numerator, ordinary height bound, bound on $u$, or bound on the comparison clock is needed. For a two-center query to $(-1,0)$, $d$ is precisely its reduced denominator exponent, as derived in PR197's *CENTER_PHASE_OBSTRUCTION.md*. This closes the former $p-d\ge12$ alternative. A fixed finite bank, including arbitrarily long or extra-odd lower words, misses arbitrarily large actual parameters. Taking $m=0$ excludes the displayed normalized meeting for every $d$.

For every positive ordinary $x$, every clock $s$ and actual odd count $q$,
$$
 3^q(x+1)\le2^s(T^s x+1)\le3^q(x+2^{s-q}).
$$
The odd shortcut multiplies the height shifted by one by $3/2$. At each even input the upper error allowance doubles. Induction proves the two inequalities together.

Suppose $d\le k+4$. Write $a=11+d+E$ and $2^{162m}=1+3^d V$, with $3\mid V$, by successive cubing. The signed integer $x=w-2^aV$ is $17\bmod48$. Applying the lower word inequality and the shrinking guard gives $x<3236$. Up to $a$ clocks the signed and ordinary starts follow the same parities. If $u\le11$, the full lower word fits, gives the positive endpoint $2^{11-u}3^u-1$, and hence forces $x>0$. The prior all-clock small-parent theorem excludes all such $x<3233$, and allows $x=3233$ only at clock $7+u$. Strict shrink then forces $d\ge5$, contradicting $3^d(3233+1)\le2^{18}$.

For $u>11$, let $p$ be the odd count before cutoff $a$, and set $r=p-d$. Exactly $r-11$ even inputs remain, so $r\ge11$. Apply the two-sided error bound to the physical *remaining* word and subtract the known signed displacement at $a$. One obtains
$$
 3^r-2^{r-11}\le S^a x\le3^r-1 .
$$
The left endpoint is positive, so $x>0$ in this case as well. The 68 candidates, including the parent, all reach 1 by clock 107. Their greatest value is 638468. For $r\ge13$ the lower bound already exceeds it, by induction. The other possible values are 177146, 531439 and 531440. Across all clocks these yield just $x=3233, a=18, p=15, r=11$. This forces $d=4,E=3$, exactly equality in the strict shrinking guard. The finite check continues through first arrival at 1, and the proof handles all later clocks using the two-cycle. [AllDepthCenter.lean](AllDepthCenter.lean)

## Why repeating one fixed chart misses the zero address

The unbounded positive construction uses an index-dependent lap count around one fixed periodic center. Trying to center such a construction on the $3$-adic parameter $m=0$ fails for a further reason. This is a written consequence for the stated class of pumps. Consider a fixed typed lower base chart with center $b$, slope $2^{d+E}/3^d$, and conjugation $w_n=c+(2^L/3^P)^n(w_{\rm base}(m)-c)$. Suppose $P>0$, $2^L<3^P$, and the signed lower orbit of $c$ eventually lies on a cycle of period $L$ with $P$ odd inputs. All starts and centers here have odd denominators. Along any sequence of integer $w_n$ with lap count tending to infinity, $w_{\rm base}(m)-c=(3^P/2^L)^n(w_n-c)$ tends to zero ternarily. If $m$ also tends to zero ternarily, continuity of $2^{162m}$ forces $c=b+2^{11+d+E}/3^d$.

This last rational specialization has a positive signed iterate. If $u\le11$, it follows the base's full lower word and reaches $2^{11-u}3^u-1$. If $u>11$, let $r$ be the number of lower odds up to cutoff $a$ minus $d$ as above. At cutoff the specialized state differs from the base center's state by $3^r$. Inverting the remaining word from $-1$ keeps the signed values at most $-1$, and their magnitudes are at most $2^{r-11}$ since an odd inverse contracts there. Thus the specialized state is at least $3^r-2^{r-11}>0$. Positive rationals remain positive under both legal branches. A positive cycle with an odd input satisfies $2^L>3^P$ by its positive affine intercept. This contradicts a contracting pump. The proof leaves open sequences with changing base charts, more general phase meetings, and direct physical descent.

**Sources.** PR197 at the head above supplies *MersenneBarrier.lean*, *CenterPhaseObstruction.lean*, *MersenneTwoCenter.lean*, the signed integer lift, and *TernaryPowerLift.lean*. PR192 at `1f1d3d690d7517e1b2a44b5f2f4930bd45b63302`, *research/astra-diagonal-closure-20261125/cycle/README.md* and *transport/README.md*, proves inverse optimality under its bounded-cycle hypotheses and a first-crossing surplus for supplied upper hits. Neither supplies the positive residue query here; the present proofs use no PR192 lemmas. The first unsupported global claim would assign a successful query or sufficient ordinary drop to every surviving actual parent.
