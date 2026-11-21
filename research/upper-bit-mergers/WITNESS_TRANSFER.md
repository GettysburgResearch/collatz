# Transferring a certified path to the companion start

**PROPOSED.** Write $T$ for the positive shortcut Collatz map, $C$ for the basin of 1, $\tau(z)$ for the first clock at 1 and $r(z)$ for the number of odd inputs before that clock when $z\in C$. Put $x=16k+1$ and $y=32k+1$. The [one-sided criterion](THREE_RAY_ONE_SIDED.md) says that $x\in C\Rightarrow y\in C$ for all $k\ge0$ is equivalent to full Collatz.

* In any interval of $N\ge2$ indices, outside $O(N/\sqrt{\log(2N)})$ exceptions, $x,y$ have the same convergence status. Whenever they converge, $\tau(y)=\tau(x)+1$ and $r(y)=r(x)$. The proof gives a common tail of their two finite certificates.
* For every fixed $\eta>0$, every sufficiently large interval $[R,(1+\eta)R]$ contains $\gg_\eta R^{2/5}$ indices whose first arm **provably reaches 1**. For each of them the second arm either never reaches 1 or satisfies both $r(y)-r(x)\gg_\eta\log R$ and $\tau(y)-\tau(x)\gg_\eta\log R$. The first arm in this construction has $\tau(x)=O_\eta(\log R)$.

Thus even assuming full Collatz, there are polynomially many indices in every fixed relative interval where transferring a witness costs a positive fraction of its length. The convergence of the second arm at all exceptional indices remains open.

## Four steps followed by one extra clock

The first four steps from $x$ reach $X=9k+1$, with two odd inputs. The first four from $y$ reach $2X-1$ with two odd inputs. One more odd step reaches $3X-1$. From these endpoints the canonical pair process starts at level one and offset $-1$. Its absorption by clock $h$ identifies the two endpoint words at equal clocks and equal affine slopes in $X$. Since the right slope initially has one more factor of three, the left word has exactly one more odd input through absorption. The total odd counts from the original starts therefore agree. [Pair process and absorption bound](THREE_RAY_UPPER.md)

For $h=\lfloor\tfrac12\log_2 N\rfloor$, every full block of $2^h$ indices represents every binary history once, since $9$ is odd. The excursion bound leaves $O(N/\sqrt{\log(2N)}+2^h)$ indices unabsorbed. Discard also the $O(2^{h+5})$ indices with $k\le2^{h+5}$. Both starts elsewhere exceed $2^{h+5}$, so neither can have reached 1 by its meeting clock, since every step retains at least half the previous value. At the meeting the original clocks differ by one, and the rest of the paths coincide. This proves the first assertion.

## The odd terminal input and the shortest witnesses

Write $X=2^a u$ with $u$ odd. Then $3\nmid u$ and $2^a u\equiv1\pmod9$. Conversely every such $a\ge0,u\ge1$ gives a unique index $k=(2^a u-1)/9$. The first arm after its four clocks halves down to $u$. The second starts its next segment at $2^{a+1}u-1$. Its first $a+1$ inputs there are odd, with successive endpoints $3^i2^{a+1-i}u-1$ through $i=a+1$. Consequently the universal implication is exactly

$$
 u\in C \quad\Longrightarrow\quad 3^{a+1}u-1\in C
 \qquad(u\text{ odd},\quad 2^a u\equiv1\pmod9).
$$

In particular the first arm for $k>0$ has the minimum possible two odd steps before reaching 1 exactly when $9k+1=2^{6m}$ with $m\ge1$. Its stopping time is $6m+4$. The second arm then makes $6m+1$ consecutive odd steps after clock four, reaching $3^{6m+1}-1$. Convergence even on this minimum-rank witness family asks for convergence of every one of these shifted powers. If a universal bound $\tau(y)\le c\tau(x)+O(1)$ holds on all certified first arms, it requires $c\ge1+\log_2 3$, by the extra halvings or other steps required to descend from $3^{6m+1}-1$ to 1.

For a fixed $u$, the admissible $a$ form one progression of difference six. Its successive targets are $Z$ and $729Z+728$. The same excursion bound with level six and offset 728 shows that in any interval of $M$ successive exponents of this progression, all but $O(M/\sqrt{\log(2M)})$ targets merge with the preceding target (omit the initial term). Indeed $3^6$ has order $2^{h-3}$ modulo $2^h$ for $h\ge3$, by repeated squaring from $v_2(3^6-1)=3$. The $Z$ values sample one full binary class modulo eight per period, and conditioning on it multiplies the full-block failure bound by at most eight. Choose $h=\max(3,\lfloor\tfrac12\log_2 M\rfloor)$ and absorb the final partial period. The implied constant is uniform in $u$.

## Many terminal inputs of controlled odd rank

Use the accelerated odd map $S(v)=(3v+1)/2^{v_2(3v+1)}$. Grow a tree backwards from $5$, whose first odd successor is 1. A child of $u$ has the form $v=(2^b u-1)/3$ with $1\le b\le18$ and $v$ a positive odd ternary unit. Then $S(v)=u$ and $r(v)=r(u)+1$. Distinct branches give distinct vertices because the forward map is deterministic and the root stays off its cycle. All vertices are at least 5. For $Q(u)=2^{11r(u)/10}u$, the cost ratio for an edge is

$$
 1<2^{11/10}(2^b-1/u)/3=Q(v)/Q(u)<c_b=2^{b+11/10}/3.
$$

Each four-generation block has total mass greater than one when a path with exponents $b_1,\ldots,b_4$ has weight $\prod_i c_{b_i}^{-2/5}$. This is a finite inequality on the 162 units modulo 243. At a node modulo $3^{d+1}$, $d$ further divisions, including the last output modulo three, are determined by these residues and the exponent choices. At each edge require $2^b u-1\equiv3$ or $6\pmod9$. The [exact checker](check_witness_transfer.py) rounds each edge weight down to a multiple of $1/1000$ by comparing its 25th power with $3^{10}/2^{10b+11}$. It sums products of the rounded weights and obtains a minimum of $1.022566376746$ at depth four.

Normalize these four-edge weights to transition probabilities. Each block probability is at most $(Q(\mathrm{end})/Q(\mathrm{start}))^{-2/5}$. Starting at 5, stop upon first reaching a block endpoint with $Q(u)\ge L$. Individual edge ratios are uniformly greater than one, so every path stops. Its endpoint has $Q(u)\le c_{18}^4 L$, and the probability of each endpoint is $O(L^{-2/5})$ by multiplication. Thus there are $\gg L^{2/5}$ distinct such $u$. Their odd ranks satisfy $r(u)\asymp\log L$ by the uniform upper and lower cost ratios.

## Placing witnesses in an arbitrary relative interval

Let $j(u)\in\{0,\ldots,5\}$ satisfy $2^{j(u)}u\equiv1\pmod9$, and let $\lambda(u)=\log_2 u+j(u)\pmod6$. The allowed logarithms $\log_2(2^a u)$ all have exactly this phase. We can rotate the phase of a terminal input while preserving convergence. Choose $b$ among 18 consecutive integers starting at a large fixed $B$ with $2^b u\equiv13\pmod{27}$. The order of 2 modulo 27 is 18. The new child $v=(2^b u-1)/3$ is $4\pmod9$. Hence

$$
 2^{b+j(v)-j(u)}\equiv (3v+1)/v\equiv1\pmod9.
$$

The exponent on the left is divisible by six. Therefore $\lambda(v)=\lambda(u)-\log_2 3+\log_2(1-1/(2^b u))$ modulo six. These inverse steps multiply size by at least two for $B\ge4$, so the sum of absolute errors in any number of steps is $O(2^{-B})$. Fix $0<\eta\le1$ and an arc strictly inside the phases of the interval $[9R(1+\eta/4),9R(1+3\eta/4)]$. Take its width and margins fixed in terms of $\eta$. Irrational rotation by $-\log_2 3$ modulo six hits the middle of every translate of this arc within $H_\eta$ steps, by compactness and density. Choosing $B$ with error smaller than the margins puts the actual phase inside the interval within this bound. Larger $\eta$ follows by restriction.

Start the preceding four-generation construction with $L=\delta_\eta R$ for a fixed sufficiently small $\delta_\eta>0$. The at most $H_\eta$ adjusting steps cost at most a fixed factor, so the adjusted node $w$ has $Q(w)\le R$. Also $r(w)\asymp_\eta\log R$. Choose $a\equiv j(w)\pmod6$ to place $2^a w$ in the displayed interval. The inequality $2^a w>9R$ gives $a\ge11r(w)/10$. The index $(2^a w-1)/9$ belongs to $[R,(1+\eta)R]$ for large $R$. From each output index recover $w$ as the odd part of $9k+1$. There are at most $H_\eta+1$ possible original tree nodes, by following the deterministic odd map. This gives $\gg_\eta R^{2/5}$ distinct indices.

For these indices $x$ reaches 1 with $r(x)=2+r(w)$ and $\tau(x)=4+a+\tau(w)$. One has

$$
 \tau(w)=\log_2 w+r(w)\log_2 3+O(\log(2+r(w))).
$$

Indeed telescoping the positive step ratios to the **first** hit of 1 leaves the error $\sum_i\log_2(1+1/(3w_i))$, where all odd inputs $w_i$ are distinct. The harmonic sum bounds this error. If $y$ reaches 1, its forced odd run gives $r(y)\ge2+a+1$ and $\tau(y)\ge4+a+1+\log_2(3^{a+1}w-1)$. Subtraction yields both claimed logarithmic gaps because $a-r(w)\ge r(w)/10$. The same identity gives $\tau(x)=O_\eta(\log R)$.

## A range of short witness lengths in every interval

The phase adjustment also permits a prescribed number of inverse generations. For any integer $1\le d\le c\log_2 R$ with sufficiently small absolute $c>0$, use exactly $d$ inverse generations from 5 with $1\le b\le6$. Each unit has at least two legal children: among the three exponents of the appropriate parity exactly one gives $2^b u\equiv1\pmod9$. This gives at least $2^d$ distinct $u$ of rank $d+1$ and size at most $5(64/3)^d$. Apply the same at most $H_\eta$ phase-adjusting moves and select $a$ for the target interval. Then $\log_2 w=O_\eta(d+1)$, $r(w)=d+O_\eta(1)$ and $a=\log_2 R-\log_2 w+O_\eta(1)\ge0$ for large $R$. Bounded inverse multiplicity gives $\gg_\eta 2^d$ distinct indices. Their first arms have

$$
 r(x)=d+O_\eta(1),\qquad \tau(x)=\log_2 R+O_\eta(d+1).
$$

If the companion converges, its forced odd segment and peak give

$$
 r(y)\ge\log_2 R-O_\eta(d+1),\qquad
 \tau(y)\ge(1+\log_2 3)\log_2 R-O_\eta(d+1).
$$

For example, $d=\lfloor\sqrt{\log_2 R}\rfloor$ gives unbounded amplification of the odd count and a stopping-time ratio at least $1+\log_2 3-o(1)$ whenever the companions converge, for $\gg_\eta 2^d$ certified antecedents in every such interval.

## A language obstruction on the two-odd-step witnesses

Encode each ordinary route by $O$ for an odd step and $E$ for an even one. For the minimum-rank inputs indexed by $m\ge1$, the first arms' first-hit words form the regular language $OEOE(E^6)^+$. Let $\mathcal L$ be a context-free language **all of whose words** are valid parity routes from some companion $y_m=32(2^{6m}-1)/9+1$ to 1. Then its words represent only finitely many distinct $m$. This holds independently of which of the $y_m$ actually reach 1.

First suppose the words end at the first hit of 1. After the initial $OEOE$ there are exactly $p=6m+1$ consecutive $O$'s, followed by an $E$ since their endpoint $3^p-1$ is even and greater than 1. A finite-state relabeling gives this run its own letter. The new language remains context-free. Parikh's theorem makes the set of triples $(p,r,h)$ semilinear, where $r$ counts all odd inputs and $h$ is the word length: these three counts are integer linear combinations of the relabeled letter counts. A semilinear set is a finite union of integer base points plus nonnegative integer combinations of finitely many periods. If $p$ were unbounded, it would therefore contain a full arithmetic ray with fixed integer increments $(\Delta p,\Delta r,\Delta h)$ where $\Delta p>0$. Since $r\ge p$ throughout that ray, $\Delta r\ge\Delta p$. [Parikh, *On Context-Free Languages*](https://doi.org/10.1145/321356.321364)

Now $\log_2 y_m=p+O(1)$. The first-hit telescoping identity above gives $h=p+r\log_2 3+O(\log(2+r))$. Divide by the ray parameter and let it tend to infinity. This forces $\Delta h=\Delta p+\Delta r\log_2 3$, impossible since $\log_2 3$ is irrational and $\Delta r>0$.

For words allowed to include later returns to 1, take the right quotient of $\mathcal L$ by $(OE)^*$, then intersect with the regular language of words not ending in $OE$. These operations preserve context-freeness. Every removed terminal $OE$ at a hit of 1 begins at 1, by reversing the two specified branches, and all later returns consist exactly of such cycles. The resulting first-hit language represents the same indices, so the preceding result applies. The conclusion concerns descriptions whose entire output language consists of valid words for this prescribed family. The existence of a general computable witness transformation remains open.
