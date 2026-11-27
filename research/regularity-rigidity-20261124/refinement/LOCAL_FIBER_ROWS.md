# Paired fibers in every prescribed coarse ternary cell at one central clock

**PROPOSED, source-qualified written theorem.** At each sufficiently large scale, one clock and one odd count yield polynomially many inverses relative to the natural scale on a polynomial fraction of all fine ternary cells. One can require these bounds in every cell of a prescribed coarser precision simultaneously, still at the same physical clock. The hypotheses are the ratio-five marked renewal law and positive probability for its bounded real offset. The proof does not use fine-scale mixing for the Syracuse distribution or a one-arm ordinary predecessor estimate. The fixed-ordinary-target assertion PT and Collatz remain open.

## Clock, map and source inputs

Use the positive shortcut map $T(2n)=n$, $T(2n+1)=3n+2$. Put $U=\mathbb Z_3^\times$. A marked word starts with an odd source at ratio five, both arms having equal odd counts. Each block runs to the first positive equal-count ratio-five root, then consumes the zero bits before the next odd source. The odd sentinel starts the next block. A complete word is a concatenation of such blocks. For word length $e$, number $p$ of odd inputs and chronological source carry $C_w$, write
$$F_w(z)=(3^p z+C_w)/2^e,\qquad G=2^e/3^p,\qquad \beta_w=C_w/2^e.$$
Throughout let $N_{e,p}(r)$ count distinct complete words at $(e,p)$ with $\beta_w\le 1/2$ and $r\in F_w(U)$. This is a function of the unit class $r\bmod 3^{p+1}$. A positive odd ordinary representative $q$ has exactly the counted positive sources $x=G(q-\beta_w)$, with $T^e(x)=q$, $T^e(5x)=5q$ and $p$ odd inputs on each arm. Each such $x$ is odd and prime to three.

We use the following written inputs at frozen heads.

* PR146 at `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md`, first-return equation (1) and the section on marked gaps. Under chronological binary Haar conditional on an initially odd source, successive marked blocks are iid, a particular block of length $l$ has probability $2^{-l}$, and their common length $L$ has $c(1+t)^{-1/2}\le\Pr(L>t)\le C(1+t)^{-1/2}$. The chronological source bits after the first are independent fair bits. [Marked renewal law](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md)
* PR200 at `abf36c63b4d0181541d7e029d390d6f636940750`, `research/regularity-rigidity-20261124/pointwise-fibers/PAIRED_FIBERS.md`, §§1–2. In outermost-first order, the same iid block list has a ternary coordinate $Q$ and nondecreasing real prefix offsets converging almost surely to $R$. The event $A=\{R\le1/2\}$ has fixed mass $d>0$. In particular real offsets at all its boundaries are at most $1/2$. The section's proof uses the reverse-prefix estimate and the elementary marked $A$-branch. Equations (F) and PF2, which invoke Tao, are not inputs below. [Bounded joint submeasure and exact incidence](https://github.com/GettysburgResearch/collatz/blob/abf36c63b4d0181541d7e029d390d6f636940750/research/regularity-rigidity-20261124/pointwise-fibers/PAIRED_FIBERS.md)

## A polynomial lower bound for both multiplicity and number of good cells

**Theorem 1.** There are fixed $D,C,c>0$ such that for each sufficiently large integer $H$ one can choose a single $(e,p)$ satisfying
$$H\le e\le DH,\qquad |2p-e|\le C\sqrt H,$$
for which at least $c3^p/H$ distinct unit residues $r\bmod3^{p+1}$ each satisfy
$$N_{e,p}(r)\ge c\,G/H. \tag{1}$$
The clock, grade and offset bound are common. The same choices work for every positive odd ordinary representative of each selected fine class.

**Proof.** Couple two readings of the same iid list $W_1,W_2,\ldots$. Let $S_j=\sum_{i\le j}|W_i|$ and $P_j=\sum_{i\le j}p(W_i)$. For the joint coordinates, $W_1$ is outermost, so through the $j$th boundary the chronological physical word is $W_j\cdots W_1$. For the balance estimate, concatenate $W_1W_2\cdots$ in its original chronological order. Regeneration identifies the latter bit stream with an initially prescribed one followed by independent fair bits. The totals $S_j,P_j$ coincide at each boundary in the two readings. No parity independence inside the reversed stream or conditional on $A$ is required.

For $M(H)=\#\{j\ge1:S_j\le H\}$, independence gives
$$\mathbb E M(H)\le \sum_{j\ge1}(1-\Pr(L>H))^j\ll\sqrt H.$$
Also for integer $J,n\ge1$,
$$\Pr(S_J>n)\le J\,\mathbb E\min(L,n)/n\ll J/\sqrt n.$$
Indeed $S_J>n$ implies $\sum_{i\le J}\min(|W_i|,n)\ge n$, and the upper gap tail bounds the truncated mean by $O(\sqrt n)$. Choose a fixed $K$ large enough that $\Pr(M(H)>K\sqrt H)<d/8$. Put $J=\lceil(K+2)\sqrt H\rceil$. Next choose a fixed integer $D$ large enough that $\Pr(S_J>DH)<d/8$. Off these two exceptions there are at least $\sqrt H$ positive boundaries in $(H,DH]$.

In the chronological reading, the centered sum of the fair signs after the first bit is a martingale with variance at most $DH$ through time $DH$. The maximal $L^2$ bound gives
$$\Pr\!\left(\max_{1\le n\le DH}\left|2\,\#\{\text{ones through }n\}-n\right|>C\sqrt H\right)<d/8$$
for a sufficiently large fixed $C$, absorbing the prescribed initial sign. Intersect $A$ with the complements of all three exceptions. This event has probability at least $d/2$. Each of its samples contributes at least $\sqrt H$ different boundaries in the displayed central strip. The strip has $O_{D,C}(H^{3/2})$ integer pairs. Summing the boundary indicators and choosing one pair yields
$$u=\Pr\{A,\ (S_j,P_j)=(e,p)\text{ for some }j\}\ge c_0/H. \tag{2}$$
The use of the event $A$ on the same samples keeps the carry bound through the pigeonhole even though $A$ can depend on the clocks.

Let $m(r)$ be the part of (2) projecting to fine target class $r$. A sample projecting there begins with one of the $N_{e,p}(r)$ complete words in the outermost-first reading. Its prefix probability is $2^{-e}$ by the block law and unique marked parsing. Hence
$$m(r)\le 2^{-e}N_{e,p}(r)\le (1+G/2)2^{-e}\le \tfrac32\,3^{-p} \tag{3}$$
for large $H$, since the central strip gives $G>1$. The middle bound follows because the distinct carries lie in $[0,2^{e-1}]$ in one class modulo $3^p$. To see distinctness, the binary valuation of the carry recovers the first odd position. Subtract its term and continue with the known list of powers $3^{p-1},\ldots,1$. The first bound in (3) puts at most $u/2$ total event mass on cells with $N_{e,p}(r)<uG/4$, since there are at most $2\cdot3^p$ such cells. The remaining mass is at least $u/2$, and the last bound in (3) requires at least $u3^p/3$ remaining cells. Equation (2) proves (1). QED.

PR195 round six at `0e8a7f9f965416189b30b57b8aa818fbcb7757c7`, equation (5), supplies a central symbolic row of mass $\gg1/(H\sqrt{\log H})$ before restricting the real carry, and identifies its endpoint average. Here the bounded-carry joint event is retained from the start. The two readings at complete boundaries give the $O(\sqrt H)$ strip, and (3) then bounds each individual cell contribution. The earlier PR200 PF2 conclusion had an upper clock $2H^4$, a subexponential cell fraction and a subexponential loss in $N/G$. [Prior central row and exact router](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round6/renewal/README.md)

## One row simultaneously inside every coarse cell

**Theorem 2.** Fix any integer $k\ge1$ (allowed to depend on $H$), and put $j=\lceil k/4\rceil$. Use the single $(e,p)$ of Theorem 1 and set
$$E=e+119j,\qquad P=p+4j,\qquad G'=2^E/3^P.$$
In **every** ternary unit class $C$ modulo $3^k$, at least $c_1 3^{P+1-k}/H$ fine classes $r\bmod 3^{P+1}$ each satisfy
$$N_{E,P}(r)\ge \frac{c_1G'}{H}\left(\frac{81}{2^{119}}\right)^j. \tag{4}$$
Here $c_1$ is absolute given the two source inputs, independently of $k,C,H$. Thus $k=o(H)$ preserves the balanced limit and the exponent $1-o(1)$ in the multiplicity at every selected fine cell. For $k=O(\log H)$ the pressure loss is polynomial. This is uniformity in **all low $k$ digits, at the same fine type**.

The elementary completed $A$-block has chronological six-bit word $101000$ and map $(9z+7)/64$. Until the first return to ratio five with equal counts it follows the parity cylinder $z=49\bmod64$. Padded with common halvings to clock $a\ge6$, its inverse at an odd unit $q$ is $A_a(q)=(2^aq-7)/9$ whenever this is integral, with a physical endpoint and sentinel. Two outward exponents $119-t,t$ have composite inverse
$$A_t A_{119-t}(q)=(2^{119}q-C_t)/81,\qquad C_t=7\cdot 2^t+63. \tag{5}$$
For any $q\in U$, choose $6\le t\le113$ such that $C_t\equiv 2^{119}q\pmod{81}$ yet $C_t\not\equiv2^{119}q\pmod{243}$. For existence, $2^{119}q-63$ and 7 are units. Two has order 54 modulo 81 and order 162 modulo 243, by successive cubing of $4=1+3$. The 108 allowed consecutive exponents contain two candidates in the required class modulo 54 and their values of $2^t$ differ modulo 243. At most one fails the second test. Both exponents are at least six. The composite inverse is a unit and its intermediate inverse is integral and a unit. Indeed $81x=2^{119}q-C_t$ implies $2^t(2^{119-t}q-7)=9(9x+7)$. This first forces divisibility by 9, and $2^t A_{119-t}(q)=9x+7$ forces the intermediate to be a unit. For ordinary odd $q$ both inverses are positive and odd. The pair formula itself is the two-$A$ construction of PR195 round six, equation (3). Its elementary coverage at this constant clock suffices here.

Choose one representative $q_*$ of $C$. Apply (5) outward $j$ times. The resulting common suffix $S$ consists chronologically of $2j$ completed $A$-blocks, has $119j$ clocks and $4j$ odd inputs, and maps every $z\in U$ into $C$. Indeed it maps one $z_*$ to $q_*$ and its slope is $81^j/2^{119j}$, of ternary valuation $4j\ge k$. Every $A$-block maps real $[0,1/2]$ into $[0,1/2]$, since its endpoint map at most $(9/2+7)/64<1/2$ there. The suffix preserves the offset cap on every selected inner word.

Send each good base class $r_0\bmod3^{p+1}$ to its image class $F_S(r_0)\bmod3^{P+1}$. Distinct base classes have distinct images because $v_3(F_S(z)-F_S(z'))=4j+v_3(z-z')$. In fact the image of each entire base cell is exactly the indicated fine cell: the power of two is a ternary unit. Each of its $N_{e,p}(r_0)$ chronological words can be followed by $S$. The words remain distinct, realize the same two endpoint labels, and have the required final offset. This gives $cG/H$ words in each image class, exactly the bound in (4) after the fixed scale change. The number of image cells is still at least $c3^p/H$. Since $0\le4j-k\le3$, this is at least a fixed fraction of $3^{P+1-k}/H$. The suffix can vary with $C$, but its clock and odd count are fixed before $C$ is supplied. Finally $|2P-E|\le C\sqrt H+111j$ and $\log(G'/G)=j\log(2^{119}/81)$ prove the rate claims. QED.

This construction imposes a coarse class at the **later target** by mapping an already large family into it. A fixed ordinary endpoint and an independently prescribed earliest inverse class are a different requirement. PR195 round six supplies that latter distribution at higher clock cost. Formula (4) does not improve the fixed-ordinary-target lower exponent $1/9$ proved by PR200's finite pressure certificate.

For example, in each prescribed $C$ the number of unit fine classes with a positive representative at most $3^{P+1}/H^2$ is at most $1+3^{P+1-k}/H^2$. As $3^{P+1-k}\ge 3^{p+1}$, this is $O(1/H)$ times the guaranteed count in Theorem 2. Even the relative abundance (4) thus leaves room for every small ordinary representative to be missed. The first missing step for PT is a lower count at **the class of one fixed ordinary $q$ at full precision $P+1$**, along balanced types, for that same $q$. Theorems 1 and 2 allow the fine class to change. A subsequent opposing estimate on genuine failed-five comparisons would also be needed for the proposed global route.
