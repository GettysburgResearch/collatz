# Finite families of ordinary starts in a prescribed binary cylinder

**PROPOSED written construction.** Fix a finite set of nonnegative integer offsets $F$ containing zero, binary precision $v$ and residue $r$, and ternary precision $s$. There are integers $B,g$ such that for **every** $D\ge B$, **every** ordinary $y$ prime to three, and **every** $c\bmod3^s$, a positive integer $x$ satisfies
$$
x\equiv r\pmod{2^v},\qquad x\equiv c\pmod{3^s},\qquad
T^D(x+i)=y,\quad O_D(x+i)=g\quad(i\in F).
$$
Each $x+i$ first reaches $y$ exactly at $D$. The two moduli and the entire finite pattern are fixed before the target, source trits and clock are supplied. Taking $F=\{0,\dots,M-1\}$ gives arbitrary fixed block lengths. The same argument allows any finite list with repetitions.

## A finite refinement that gives one extra odd departure to a chosen arm

A binary cylinder with free high parameter $t$ represents an ordinary arm by the pair $(p,a)$, where $p$ is its cumulative odd count and its value is $A(t)=3^pt+a$. The ordinary dyadic lift identity reads
$$
T^j(n+2^j u)=T^j(n)+3^{O_j(n)}u,\qquad O_j(n+2^j u)=O_j(n).
$$
Thus on replacing $t$ by $t_0+2^j u$ the new profile has grade $p+O_j(A(t_0))$ and constant $T^j(A(t_0))$. Refinements compose, and equal profiles remain equal on every later refinement.

Suppose $A(t)=3^pt+a$ and $B(t)=3^qt+b$ with $p<q$. Since their slopes differ, choose $t_0\in\{0,1\}$ with $A(t_0)\ne B(t_0)$. Write their absolute difference as $2^j u$ with $u$ odd. The lift identity applied to the smaller of these values shows that their additional odd counts through clock $j$ agree, while their endpoints at that clock have opposite parities. Replacing $t_0$ by $t_0+2^j$ toggles both endpoint parities and preserves both counts up to that clock. Indeed each endpoint moves by the odd integer $3^{p+O_j(A(t_0))}$ or $3^{q+O_j(B(t_0))}$. Choose the orientation in which the first arm is odd and the second is even. After one more step the grade difference has fallen from $q-p$ to $q-p-1$. Repeat until grades agree.

At equal grade $p$, the starts have a fixed ordinary difference $d=|a-b|$ as $t$ varies. Apply the fixed-gap construction with precision $p$ and lower-source residue $\min(a,b)\bmod3^p$. Its endpoint can be chosen so large that its lower start is at least $\min(a,b)$. The selected lower start is then $3^pt+\min(a,b)$ for a nonnegative integer $t$. Both arms have the same endpoint and the same grade at this clock. Their refined profiles agree identically. This proves finite synchronization for arbitrary two profiles. Given a finite list, synchronize its first two members and then add one member at a time, always retaining earlier identifications.

## Closing the common profile at a supplied clock

Start with the binary cylinder $x=r+2^v t$. Run its $F$-arms for $v$ clocks and apply the finite refinement just proved. At some $H\ge v$, with $R\equiv r\bmod2^v$, every start $R+2^H u+i$ has the same grade $p$ and the same value $a+3^p u$, for every $u\ge 0$ and every $i\in F$.

Given $c$, solve $R+2^H u_0\equiv c\bmod3^s$. For any large enough remaining clock $L$, route an ordinary $w$ to $y$ in exactly $L$ steps and two odd departures while imposing
$$
                w\equiv a+3^p u_0\pmod {3^{p+s}}.
$$
The two-gap theorem works as soon as $L>6\cdot3^{p+s}$. The elementary height bound $2^L y\le16w$ ensures $w>a$ once $L\ge16(a+1)$. Thus $w=a+3^p u$ with $u>0$ and $u\equiv u_0\bmod3^s$. The decoded ordinary start realizes the entire prescribed pattern. Both the threshold and grade $p+2$ are independent of $y,c,L$. Use the off-orbit predecessor from the first-arrival theorem to make the final clock the first visit simultaneously for all arms. This adds at most ten to the clock threshold and one to the common grade.

The earlier whole-interval theorem in PR146 also constructs synchronized blocks and controls their typical binary depth by $O(\log^2(2M))$, simultaneously with fivefold companions. The finite argument above uses an explicit deterministic one-count adjustment and makes no efficiency claim for $H$. Its role here is to match the exact-clock two-gap router, mixed source residues, and first arrivals. [PR146 whole-interval synchronization](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md)

## Relative windows and the fixed-source requirement

The common grade-$g$ clock theorem above can replace the two-arm certificate in the [relative-window construction](FAST_FIRST_HIT_PAIRS.md). At its one fixed initial clock, all $x+i$ hit the same chosen unit $w$ with that grade, and the start $x$ satisfies the same two-sided affine bounds. At most $\max F$ is added to its position to cover the whole family. For every fixed $\delta>0$ the entire pattern therefore fits inside each $[X,(1+\delta)X]$ once $X\ge C y$. Its common first-hit clock is at most $\log_2(X/y)+K$, with equal odd counts bounded by $G$. Here $C,K,G$ depend only on $F,v,r,s,\delta$. The written construction with two time/count residue constraints also applies.

If a positive component misses $1$, it contains a unit $y$ and then has arbitrarily long consecutive blocks in each such macroscopic window, with prescribed mixed residue of the lower endpoint. The unit follows by halving to an odd state and taking its next step whenever that state is a multiple of three. Thus it would suffice to establish, for one fixed block length and one fixed residue of its first member, a sequence of unbounded macroscopic windows in which every such block contains a source that reaches $1$. This pointwise covering statement remains open. The constructed block's first member varies with the window.

