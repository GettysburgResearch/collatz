# How large can a common-source preimage of two marked futures be?

**PROPOSED. The clock and height bounds below are Lean-checked. The extremal classification is a written proof with its unique word equation checked in Lean. The ordinary basin transfer is OPEN.** Put $T(2n)=n$, $T(2n+1)=3n+2$. For one ordinary $x>0$, write $X_i=T^i x$, $Y_i=T^i(9x+2)$; let $p_i,q_i$ count the odd inputs on their respective first $i$ steps and $S_i=p_i+q_i$. The residual question is $x\in C\Rightarrow 9x+2\in C$ for $x=9k+2$, where $C$ is the basin of one. The original arms $36k+8,72k+17$ reach these two values after two and three shortcut steps respectively. Every statement on pairs below also holds for unrestricted $x>0$ unless a residue is specified.

For a fixed clock $h$, retain the **ordered endpoint fiber**
$$
 \{x>0:T^h x=A,\ T^h(9x+2)=B\}.
$$
Take its maximal $x$ as zero when it is empty. If $A\ne B$, every member satisfies
$$
 \frac{x}{2^h}\ \le\ \max(A,B/9)\,
     3^{-\max(0,\sqrt{h+5}-3)/2}.
 \tag{1}
$$
On the diagonal $A=B=Z$, every member instead satisfies $x<2^h Z/27$. All members with $x\ge2^h Z/81$ lie on the **single** cylinder $x=46\pmod {64}$; their only possible value is
$$
     x=(2^hZ-38)/27.
     \tag{2}
$$
For every fixed positive ternary unit $Z$, (2) is attained on an infinite clock progression even under the original restriction $x=2\pmod9$. Thus the limsup of the maximal $x/2^h$ on the restricted fiber is exactly $Z/27$ on that diagonal, and zero for any fixed unequal ordered pair. For $3\mid Z$, the diagonal fiber is empty, since the right arm is a ternary unit at every clock. The separation is a theorem about **heights of original sources**, independent of any assumption on convergence, asymptotic distribution, or frequency of an endpoint.

## The determinant cannot vanish at unequal marks

For a length-$i$ physical parity word with $p$ odd positions $a_1<\cdots<a_p$ numbered from zero, put
$$
 c=\sum_{j=1}^p 2^{a_j}3^{p-j},\qquad
      2^iX_i=3^p x+c.
$$
Use $d,q$ for the right arm. Then $c\le 2^i3^p, d\le 2^i3^q$. If $p>0$, only the last summand of $c$ is a ternary unit, hence $3\nmid c$. The integer $2\cdot3^q+d$ is a ternary unit in both cases $q=0$ and $q>0$.

Set $D_i=3^pY_i-9\cdot3^qX_i$. If $D_i=0$, the word identities give
$$
   3^p(2\cdot3^q+d)=9\cdot3^q c .
$$
The left side is positive, so $p>0$. Comparing exact ternary valuations yields $p=q+2$; the definition of $D_i$ now gives the physical equality $X_i=Y_i$. This proves the implication for actual ordinary word pairs without choosing a signed extension.

If the arms differ at $i$, the nonzero integer $D_i$ has magnitude at most $12\cdot3^{p+q}$. Indeed $2^iD_i=3^p(2\cdot3^q+d)-9\cdot3^q c$, and the two nonnegative terms are bounded by $3\cdot 2^i3^{p+q}$ and $9\cdot 2^i3^{p+q}$, respectively. A joint run of $L$ even steps starting at $i$ forces $2^L\mid D_i$. Its length consequently satisfies
$$
   2^L\le12\cdot3^{S_i},\qquad L\le4+2S_i.
$$
A pair differing at $h$ differed at every earlier clock. Each event with at least one odd input increases $S_i$ by one or two. Thus the initial grades at maximal joint-even stretches through $h$ are distinct members of $0,\ldots,S_h$; the remaining event clocks number at most $S_h$. Summing gives
$$
 h\le S_h^2+6S_h+4.
 \tag{3}
$$
Using the logarithm of the power bound in place of its rounded bound gives the sharper written estimate $h\le S_h+(S_h+1)\log_2 12+\tfrac12 S_h(S_h+1)\log_2 3$. Finally $3^{p_h}x\le2^hA$ and $9\cdot3^{q_h}x\le2^hB$. The larger of the two grades is at least $S_h/2$; inserting $S_h\ge\max(0,\sqrt{h+5}-3)$ proves (1).

The formal integer version has no logarithms. If $2^h\le Dx$, $A,B\le M$ and $DM<3^{g+1}$, unequal marks require $h\le4g^2+12g+4$. The proof applies fiber member by fiber member, even if an endpoint or parity prefix was chosen after observing the other arm's future. [Lean, `proportionalForcesMeeting`, `jointHalvingBound`, `separatedClock`, and `boundedMarkedFiber`](PairedPrefix.lean)

## The unique upper part of the diagonal

For any positive $v$ with $p$ odd inputs through clock $h$,
$$
   3^p v\le2^hT^h v\le4^p v .
$$
An even step keeps the scaled value unchanged; an odd step multiplies it by $3+1/T^i v\le4$.

Suppose $X_h=Y_h=Z$. If $q_h=0$, then $2^h Z=9x+2$; the two scalar bounds force $p_h=2$. But a two-odd left word has intercept at least $3+2=5$, whereas equality would require intercept 2. Thus $q_h\ge1$. If $q_h\ge2$, then $2^h Z\ge9(9x+2)>81x$. If $q_h=1$, let $j$ be its unique odd position. Then $27x<2^hZ\le36x+8<81x$, so $p_h=3$. Writing the left odd positions $a<b<c$, the physical word equation becomes
$$
    9\cdot2^a+3\cdot2^b+2^c=6+2^j .
$$
For $j\le3$ the right side is less than the minimum 19 of the left. For $j\ge4$, comparison of binary valuations gives $a=1$, then $b=2$: after removing $18$, the right side is $2^j-12$ of valuation two. Subtracting both contributions from the original equation gives $2^c=2^j-24$. At $j=4$ it is negative; at $j\ge5$ it has valuation three. Hence $c=3, j=5$. The original right arm is $32\pmod {64}$, or $x=46\pmod {64}$, and the intercept is 38.

Conversely, intersect this cylinder with $x=9k+2$; it becomes $k=64v+12$, or $x=576v+110$. The six physical steps on the two arms then land at $243v+47$. For every ternary-unit target $Z$, choose arbitrarily large $\ell$ with $2^\ell Z=47\pmod {243}$. Such exponents form a single class modulo 162, since 2 generates the units modulo 243; successive cubing gives $v_3(4^{3^j}-1)=j+1$. Put $v=(2^\ell Z-47)/243\ge0$, and follow the six steps by $\ell$ halvings to the **same** $Z$. Thus at $h=6+\ell$, (2) actually holds. This uses the companion note's physical cylinder; its first-landing count is a separate result. [Paired landing construction](../renewal/README.md)

## Why this does not yet transport the marked basin

Consider an alleged fixed failure $x_0\in C$, $9x_0+2\notin C$. Fix a pair of future values on those arms. Try to generate higher original sources $x\ge2^h/D$, with fixed $D$, whose two $h$-clock endpoints equal those marks. The integer version of (1) rules out arbitrarily large $h$: the marks lie in different components and hence are unequal. The argument still works if the clocks are $h+r,h+s$ for bounded nonnegative offsets: take the larger clock, move the earlier mark forward by the bounded difference, and use the resulting finite set of possible endpoint heights. Everything in this argument concerns preserved ordinary futures of the original marks.

Even when both original arms converge, synchronous equality can fail. At residual parameter $k=0$, $(x,9x+2)=(2,20)$; at clock 6 the marks are $(2,1)$, opposite phases of the physical cycle forever. Thus a proof requiring a synchronizing lift preserving both equal-clock futures at every residual source is false as a sufficient construction for all the true basin pairs.

A source-preserving inverse step can actually be constructed, even with the original residue retained. For $u=4096v+2830$, the two twelve-step endpoints are
$$
  T^{12}u=81v+56,\qquad T^{12}(9u+2)=9(81v+56)+2.
$$
At $v=0$ the two source words are respectively `011101000000` and `000000011101` in chronological order. Both have four odd inputs. The parity-cylinder lift gives the displayed identities for every $v\ge0$, adding $81v$ and $729v$ to the base endpoints. Requiring $v=9t+7$ makes $u$ and $81v+56$ both $2\bmod 9$. Consequently, a genuinely failing original parameter $k=81t+69$, if supplied, produces a genuinely failing parameter $4096t+3500$, with an explicit twelve-step path on each marked arm back to the given pair. No resampling or exchange of colors is involved.

On the unrestricted physical coordinate, this inverse branch is $R(x)=(4096x-146)/81$. One has $4015R(x)-146=(4096/81)(4015x-146)$. Each legal repetition removes four factors of three from that integer. No positive starting $x$ allows arbitrarily many repetitions of this branch, since $4015x-146$ is positive. This makes concrete both the availability of a fixed-source sibling and the need for a genuinely varying unbounded family to use the sparse-failure estimate.

**Arbitrarily varying bounded inverse branches still have a power loss.** Fix $H\ge1$ and an ordinary terminal pair $(z,9z+2)$. Permit any number of inverse steps with independent clocks: a prior pair $(u,9u+2)$ qualifies for a current pair $(v,9v+2)$ whenever $T^a u=v$ and $T^b(9u+2)=9v+2$ for some $0\le a,b\le H$. Omit the unchanged zero-clock step. There is no bound on the choices or their dependence on the physical integers. Even on the full positive line, the number of such ancestors $u\le X$ is
$$
       O_{H,z}\bigl(X^{\,1-(\log_2(64/63))/H}\bigr).
       \tag{4}
$$
Thus unrestricted branching within any fixed clock budget cannot produce enough original witnesses from one failure to contradict the $O(X/\sqrt{\log X})$ upper count. This holds for every fixed terminal pair, whether it passes or fails the basin test.

To prove (4), split into the finitely many binary classes modulo $2^H$ and choices of $a,b$. The two outputs on each class are affine in the initial integer. An isolated solution of $T^b(9u+2)=9T^a u+2$ can occur at most once per nonidentical pair of forms. Choose $L$ larger than $z$, one, and all such exceptional positive solutions. At $u>L$ a successful test is consequently an identity on its class. Comparing its slopes gives $3^{q}2^{a}=3^{p}2^{b}$, so $a=b$ and the counts agree. It is therefore an equal-clock return of the affine pair to the same form. It may be split at the earliest such return, always preserving the ordinary marked endpoints. Repeat within the same word to get first-return pieces of lengths at most $H$. At an intermediate split the still unexposed binary quotient has odd slope; an affine identity on its subcylinder is again an identity on the corresponding next word's parity cylinder.

Beginning at the form $(u,9u+2)$, the binary classes of the positive-length first-return pieces are disjoint by prefixes. Their summed full-grid probability is at most $63/64$. Indeed on $u=46\bmod64$ the arms have the ordinary common value at clock six, and none of the first five clocks gives an identically returned form. This last assertion can be checked at $u=46$: the paired states through clock six are $(23,208),(35,104),(53,52),(80,26),(40,13),(20,20)$. Equality at six persists forever and precludes all later positive returned forms. At a successful first return of length $j$, write $u=2^jt+r$. The new left coordinate is $3^p t+c$, whose odd coefficient permutes every fresh binary grid. Therefore the probability of $n$ successive first returns of lengths at most $H$ is at most $(63/64)^n$, exactly as a count on the original full grid modulo $2^{Hn}$.

For $X/2<u\le X$, choose $n=\lfloor\log_2(X/(2L))/H\rfloor$, assuming it is positive. Since a step retains at least half its input, the first $n$ bounded pieces cannot yet have reached the terminal $z<L$; their starts exceed $L$. Equivalently, inspect the path until its first passage to $[1,L]$: more than $nH$ ordinary left-arm clocks are required. All preceding bounded jumps start above $L$ and hence are genuine affine returns as just proved. At least $n$ first-return pieces are available. Counting their residues in $(X/2,X]$ costs at most $(X+2^{Hn})(63/64)^n$, which proves (4) after summing dyadic intervals. This leaves variable, unbounded physical clocks open; the constants and the exponent in (4) depend on $H$.

PR197's adaptive projection retains both endpoints and grades from the same source, and allows siblings at high density for most records. Its typical terminal heights may grow rapidly with the native clock. Inequality (1) applies to every one of its unequal record members, but a lower bound on the number of **distinct such records in the two specified components** does not follow. A fixed forced merger cylinder only gives equal-component records. The first unsupported step toward the basin implication would be to grow one failing source into enough genuinely disparate-component original sources at the smaller heights allowed by (1), or to control both arms at larger, variable clocks. No such generation or contradiction is established here.

**Exact sources.** The restricted ordinary basin implication is PR193, `67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e`, `research/astra-global-resolution-20261124/rewriting/SingleReturn.lean`, theorem `collatzIffEvenChild`. The ordered-source comparisons are PR197, `6eb986b0ce0b1836a356474d25d709ed4e948b67`, `research/ayh-resource-reset-20261124/two-class-descent/{ADAPTIVE_PAIRED_PROJECTION,HIGH_GRADE_SHADOW}.md`, respectively the future-record census and the real offset on high relative grade. Their relative grade is distinct from our sum of the two actual odd counts. PR192, `301b84491ffafe283bd63d104c1b60ddf0e97f06`, `research/astra-two-centre-20261124/integer.md`, constructs a mixed binary/ternary bounded-word obstruction and a distinct sparse-digit theorem. The clock and source-height proofs here only use the ordinary shortcut equations. The diagonal attainment uses the cited physical row.
