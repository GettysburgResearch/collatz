# Merger after a paid return and three light returns

A finite prefix now suffices for thirteen of the sixteen five-block continuations beginning with the first paid return. There is no spacing condition after the prefix. The three remaining prefixes are **PPLLL, PLLPP, PLLPL**. This result concerns the ordinary two-gap alphabet only. It does not establish universal descent.

Write $T(x)=x/2$ for even $x$ and $(3x+1)/2$ for odd $x$. An actual light block $L$ uses three shortcut clocks with two odd inputs and has output $(9q+7)/8$. A paid block $P$ uses five with two odd inputs and outputs $(9q+5)/32$. We choose the floor at the initial boundary $q_0$ or at its first light intermediate $(3q_0+1)/4$ when there is an initial light block.

## Changing the slope with the initial light run

**Theorem.** Given any actual finite prefix $L^rPLLL$ with $r\ge3$, there exists a positive **odd** $m$ below both floors that reaches the final source boundary in $2r+16$ ordinary shortcut clocks. The source uses $3r+14$ clocks. The rest of the trajectory is unrestricted.

Let $q$ denote the boundary immediately before the first $P$. Since $8(L(x)+7)=9(x+7)$ and $q$ is odd, coprimality of two and nine gives a positive integer $v$ with
$$q_0+7=2^{3r+1}v,\qquad q+7=2\cdot9^r v.$$
The identity $T^t(2^t v-1)=3^t v-1$ follows from the first $t$ inputs all being odd. Take $m=2^{2r+3}v-1$. Since $r\ge3$, $m+1\le(q_0+7)/2$. The displayed cofactor equation gives $q_0\ge 1017$, so $m$ is below both floors. At clock $2r+3$, the comparison orbit reaches $y=27(q+7)/2-1$.

Write $w$ for the final boundary after $PLLL$. Composition gives $16384w=6561q+52253$, hence $8192w=243y+3406$. This forces $y=8192t+7942$ and $w=243t+236$. The thirteen literal shortcut bits on this residue class are **0110001001100**, ending at $w$. The kernel theorem uses the original raw light and paid boundary equations and derives the cofactor internally. [descent_Extension.lean](descent_Extension.lean)

## A finite certificate for arbitrary suffixes

For any suffix $W$ beginning at $q$, write $2^A w=3^p q+C$. For a candidate integer $\ell$ with $2r+\ell\ge1$ and $\ell\le r$, the same construction starts at $m=2^{2r+\ell}v-1$ and reaches $y=3^\ell(q+7)/2-1$. Here $3^\ell$ can be rational for negative $\ell$ because the power of nine in $q+7$ supplies the denominator. The input $m$ is positive and below both floors whenever $q_0>11$. With $B=A-1$ and $u=p-\ell$, the only possible target carry is
$$K=(C-7\cdot 3^p)/2+3^u.$$
For $0\le u\le B$, compute $b=-K(3^u)^{-1}\bmod 2^B$, $0\le b<2^B$. Accept exactly if $B$ literal steps from $b$ contain $u$ odd inputs and $2^B T^B(b)=3^u b+K$. All allowable $\ell$ at this clock are covered by $0\le u\le B$. On acceptance, the target and the original share endpoint $w$ since $y\equiv b\pmod{2^B}$ and the shortcut word is constant on that residue. The older fixed half $m=(q_0-7)/2$ has the corresponding test $u=p$, $K=(C+7\cdot 3^p)/2$. Its transfer across the initial $L^r$ is proved in [descent_Triple.lean](descent_Triple.lean).

The following prefix code proves the thirteen cases. The listed target bits begin at the first paid macro after the comparison source has traversed its initial segment. The exact test above verifies each word and its affine identity.

| Accepted prefix after the initial light run | Partner | Target bits |
|---|---|---|
| PPP | fixed half | 01111000100010 |
| PPLP | fixed half | 01111000101001010 |
| PLPP | ramp, $\ell=1$ | 01110101001001000 |
| PLPL | ramp, $\ell=1$ | 011101010010001 |
| PLLL | ramp, $\ell=3$ | 0110001001100 |
| PPLLP | ramp, $\ell=1$ | 01110011010001001010 |

Every five-letter word beginning with $P$ has one of these prefixes except for the three named above. For $r\ge3$ all listed partners are smaller. Any even fixed-half partner has a positive odd part no larger than the partner, reached by stripping its initial factors of two. It inherits nonconvergence if the shared orbit is nonconvergent. For $r=0$, the first paid boundary drops below $q_0$ whenever $q_0>1$. For $r=1,2$, the paid boundary is respectively $(81q_0+103)/256$ or $(729q_0+1391)/2048$, strictly below the first light intermediate on every genuine such prefix ($q_0\ge9$). Thus these cases need no auxiliary orbit.

## A repeatable fixed-half merger

After the initial $L^rP$ the actual half partner, one shortcut clock behind the source, has value $3q-4$ at the new boundary $q$. For each table entry, substituting an ordinary input boundary into the left expression and following the indicated number of literal clocks produces the right expression at the next boundary.

| Input partner | Block | Output partner |
|---|---|---|
| $3q-4$ | L | $9q'-19$ |
| $9q-19$ | P | $3q'-2$ |
| $3q-2$ | L | $3q'-4$ |
| $3q-4$ | P | $3q'-1$ |
| $3q-1$ | P | $q'$ |
| $3q-1$ | L | $q'-1$ |
| $q-1$ | P | $q'$ |

The first three lines return to the original comparison formula. Hence **every** $L^rP(LPL)^jP(P\mid LP)$ merges with its fixed half after one fewer clock, for arbitrary $r,j\ge0$. The table can be checked by substituting $q=16t+9$ on L and $q=64t+3$ on P. Other ordinary lifts follow by affine linearity. This language and the finite prefix code are written proofs with exact integer controls.

There is also an isolated-pair resonance. After $PP$ the half partner is $3q-1$. One L sends it to $q'-1$. The next L sends it to $(q''+7)/9-1$ because $q'-1$ is divisible by eight. If a total of $s\ge2$ L's occur between this pair and the next P, all $3(s-2)$ subsequent comparison bits through the remaining light run are odd: the starting $q''+7$ is divisible by $8^{s-2}$ and the denominator nine is odd. The partner at the next paid boundary $u$ is $3^{s-4}(u+7)-1$. One more odd clock gives $3^{s-3}(u+7)/2-1$. For $s=6$ or $7$ the exponents are three and four, both accepted by $PLLL$. Thus $L^rPP L^sPLLL$ merges for these two values of $s$, with no condition on the suffix.

## Why a lone close pair does not settle the matter

For the **fixed** half, no $PL^sP$ merges at its end with one fewer clock, for any $s\ge0$. Just after the first P, its formula $3q-4$ takes the value $-25$ at the signed light fixed point $q=-7$. During $s$ light blocks, the comparison follows the signed orbit of $-25$ modulo the required powers of two because $8^s$ divides $q+7$. The signed shortcut cycle has length eleven and seven odd visits. At the end the comparison slope relative to the boundary is $3^{k_s}$, where
$$k_s=1+\#\{\text{odd visits among the first }3s\text{ iterates of }-25\}-2s.$$
Thus $k_{s+11}=k_s-1$, and the eleven initial exponents are $1,2,2,1,1,1,2,0,1,1,1$. Equality after the last five paid clocks requires $u=2-k_s$ odd target visits. For $s\ge66$, $u>5$. The exact carry test rejects all $0\le s<66$. This rules out the fixed-half affine merger at the specified clock uniformly over a cylinder. An individual ordinary orbit could still meet through some later continuation or accidental equality.

Past the finite prefix code, collections of paid returns with at most two intervening L's contract the source, but any bound is relative to the boundary at entry. The first $r$ light steps may have placed that boundary far above $q_0$. For example, the prefix PPLLL has no accepting endpoint for either of the two specified carry tests, even when all allowable ramp exponents are tried. Recovering the *initial* floor through arbitrary such defects remains necessary. Gaps outside L/P require a further argument.

## Verification

The three declarations in [descent_Extension.lean](descent_Extension.lean) were accepted by Lean 4.34.1, commit 5045d0056413266e57c625dcd7c365b10e377c52, with `-j1 -DwarningAsError=true` and only `Std`. The printed transitive axiom inventories use `propext` and `Quot.sound`, with `Classical.choice` also present for the ramp and raw merger theorems. The remaining certificate tables and the signed-cycle proof above were verified by [descent_Extension.py](descent_Extension.py), run both normally and with Python optimization. Its 396 ordinary endpoint comparisons complement the symbolic whole-residue proofs.
