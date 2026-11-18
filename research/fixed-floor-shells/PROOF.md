# Counting predecessor patterns in short multiplicative intervals

**Status: PROPOSED, pending independent review.** Use the ordinary positive
shortcut map $T(n)=n/2$ for even $n$, and $T(n)=(3n+1)/2$ for odd
$n$. Write $B_b=\{n:T^i(n)=b\text{ for some }i\ge0\}$ and
$A_b(x)=|B_b\cap[1,x]|$. Fix $b>0$ with $3\nmid b$.

*Source pins.* The integrated base is
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The source-qualified [predecessor bound](../external/mazur-2026/predecessor-x090.md)
gives $A_b(x)\ge c_b x^{901/1000}$ eventually, with target-dependent
positive constant and cutoff. We use it only for corollaries. PR #134 at
`025f2683c19bfedc3eeff0303206b20c889c8005`,
`research/paired-comparison/endpoint-transplant/PROOF.md`, EPT-001/002,
supplies gates for any given finite offset pattern and establishes thickness
in a computable multiplicative window. We use its gate construction as a
source-qualified input for general patterns. The singleton gates used below
are elementary. The [critical-mass packet](../astra-critical-mass/PROOF.md)
already proves endpoint and weighted-odd criteria. None of these inputs
asserts a fixed-floor survivor upper bound.

## FS-001. Removing the odd-core multiplicity loss

For $n=2^v m$, $m$ odd, put $U=n$ if $3\nmid n$ and
$U=2^v(4m+1)$ otherwise. Then $U\le5n$, $U$ is a ternary unit, and
there are at most two possible inputs for each $U$: its valuation recovers
$v$, and each of the two formulas then determines $m$. If $n\in B_b$,
then $U\in B_b$. In the second case, $b$ is a unit, so the original
trajectory must pass $T(m)$ before or at its visit to $b$, and
$T^3(4m+1)=T(m)$. The same preservation holds for the set of all sources
never reaching one.

Choose $k\in\{1,2\}$ with $2^kU=1\pmod3$. The odd positive
$y=(2^kU-1)/3\le20n/3$ reaches $U$ in $k$ shortcut steps.
Each output has at most four inputs by trying each $k$ and inverting $U$.
Consequently the odd members of $B_b$ up to $20X/3$ number at least
$A_b(X)/4$. Under the predecessor bound, every exceptional component has
an eventual lower bound of constant times $X^{0.901}$ on its odd count.
In particular even a vanishing *liminf* of the unweighted odd eternal
survivor count divided by $X^{0.901}$ would suffice for Collatz: an
exceptional orbit contains a fixed ternary-unit target after an odd step.

## FS-002. Anchors of prescribed patterns in every relative shell

A fixed gate consists of nonnegative finite offsets $D$ including zero,
integers $M=2^L,A=3^Q$ with $Q\ge1$, integers $B,e$ with $3\nmid e$,
and a threshold $t_0$. Its premise is the literal equality

$$
 T^L(B+Mt+d)=At+e\qquad(d\in D,\quad t\ge t_0)
$$

on positive integer inputs. For every fixed $0<\epsilon<1$ there are
positive $a,c$ and a finite $N$, depending only on the gate and
$\epsilon$, such that for large $X$ at least
$c(A_b(aX)-A_b(N))$ **pairwise disjoint** translates $x+D$
lie wholly in $[X,(1+\epsilon)X]\cap B_b$. All members of each translate
reach $b$ at a common time while times across translates can differ.

**Preparation.** Put $P=2\cdot3^{Q-1}$, the order of 2 modulo $3^Q$.
Indeed $v_3(4^{3^j}-1)=j+1$ by successive cubing, starting with
$4-1=3$. The order triples with each lift, so 2 generates all units at
each precision. Fix the unit $s=-1/2\pmod{3^Q}$, for which $3s+1=s$
modulo $3^Q$. For $n\in B_b$ form $U$ as above. Choose
$1\le l\le3P$ with $2^lU=3s+1\pmod{3^{Q+1}}$;
the residue on the right is independent of the chosen lift of $s$.
Then $z_0=(2^lU-1)/3$ is positive odd, equals $s\pmod{3^Q}$, and
reaches $U$. Each $z_0$ has at most $6P$ original inputs, including
the two alternatives in FS-001. We have $z_0\ge(2n-1)/3$ and
$z_0\le 5\cdot2^{3P}n$.

**Legal rotation.** Starting from $z_i=s\pmod{3^Q}$, choose
$k_i\in\{P,2P,3P\}$ so $2^{k_i}z_i=3s+1\pmod{3^{Q+1}}$.
Such a choice exists because those three residues exhaust the three
unit lifts of $s$. Set $z_{i+1}=(2^{k_i}z_i-1)/3$; it is again odd,
is $s\pmod{3^Q}$, and its next odd iterate is $z_i$.
Writing $d_i=2^{k_i}/3\ge4/3$ and $D_j=\prod_{i<j}d_i$, iteration gives

$$
 z_j/D_j=z_0-\tfrac13\sum_{i=1}^j D_i^{-1}\in[z_0-1,z_0].
$$

Thus for $z_0\ge2$, uniformly in $j$, the circular distance modulo
$P$ between $\log_2 z_j$ and $\log_2 z_0-j\log_2 3$ is at most
$-\log_2(1-1/z_0)$. Also $z_j\le 2^{3Pj}z_0$.

**Selection.** Fix $0\le r<P$ integral with $2^rs=e\pmod{3^Q}$.
The points $j\log_2 3\pmod P$ are dense because $\log_2 3/P$ is
irrational. For any fixed tolerance $\delta>0$, finitely many of these
points, $0\le j\le J$, are a $\delta$-net by compactness. Use
$\delta=\tfrac1{10}\log_2(1+\epsilon)$ and enlarge $N$ until the above
logarithmic error is at most $\delta$. There exist $j\le J$ and
$k=r\pmod P$ with

$$
 \left|\log_2((M/A)2^kz_j)-
 \log_2(X\sqrt{1+\epsilon})\right|\le 2\delta .
$$

Choose $a>0$ small enough that $(M/A)2^{3PJ}5\cdot 2^{3P}a<1$.
Then $k\ge0$. The positive relative margins on each side of the selected
logarithmic subinterval absorb the gate's fixed additive offsets for large
$X$. Specifically $t=(2^kz_j-e)/A$ is an integer exceeding $t_0$,
and $x+d=(M/A)2^kz_j+B-Me/A+d$ belongs to the shell for each $d$.
The gate ends at $2^kz_j$, then $k$ halvings reach $z_j$, which has
a path back through $z_0,U$ to $b$.

**Counting.** From the anchor $x$ recover $t=(x-B)/M$, hence $At+e$.
Its odd core recovers $z_j$, even if $k$ is very large. For each of
$J+1$ possible $j$, its next $j$ odd iterates recover $z_0$.
Thus each anchor accounts for at most $6P(J+1)$ inputs. A chosen
translate intersects at most $|D-D|$ translates counting itself, since
their anchor differences belong to $D-D$. Greedy thinning proves the
claim with $c=(6P(J+1)|D-D|)^{-1}$.

## Consequences and remaining obstacle

For every fixed $K$ and $0<\epsilon<1$, using the cited gate with
$D=\{0,\ldots,K-1\}$, the predecessor lower bound now yields
$\gg_{b,K,\epsilon} X^{0.901}$ disjoint $K$-blocks in **every**
sufficiently large relative shell, conditional only on those stated inputs.
A single binary parity cylinder can alternatively be imposed with a
singleton gate: any length-$L$ word gives $B\pmod{2^L}$, and
$T^L(B+2^Lt)=3^Qt+e$, with $Q$ its odd count. For $Q>0$ the final
state is a ternary unit after the last odd step; words of weight zero can
be refined by appending an odd step. In particular this shell statement
applies to each dyadic residue class separately.

Hence a cofinal sequence of shells with $o(X^{0.901})$ wholly exceptional
$K$-blocks would suffice for Collatz, even if the total exceptional count
were larger. No such upper bound is established. All counting here is for
genuine positive integer sources and one fixed target. No assertion about
uniform constants over targets or growing $K$ is used.

## FS-003. A shrinking-shell estimate with elementary constants

For a fixed gate, there are constants $C,H>0$ such that under the same
predecessor hypothesis of exponent $\gamma>0$ all large $X$ satisfy

$$
 \#\{\text{disjoint gate translates in }B_b\cap
 [X,X(1+C/\log\log X)]\}
 \ \ge\ c_{b,\mathrm{gate}} X^\gamma
             \exp(-H\sqrt{\log X}).
$$

Here the count is the maximum size of such a disjoint family and $\log$
denotes the natural logarithm. The argument is uniform in shell location.
It uses a quantitative rotation mesh and keeps the size loss from the
$J$ legal inverse steps.

**Mesh.** Put $\alpha=\log_2(3)/P$. For integer $m\ge2$, pigeonhole gives
$1\le q\le m$ with $\beta=\|q\alpha\|\le1/m$. For a nearest integer $p$,
$3^q$ and $2^{pP}$ are distinct positive integers, both at most
$2^P3^m$. The mean value theorem for $\log$ yields
$\beta\ge(2^P3^mP\log 2)^{-1}$. Multiples of $q\alpha$ from zero through
$\lfloor1/\beta\rfloor q\alpha$ leave gaps at most $\beta$ on the unit
circle. The same holds with the sign reversed. Thus the mesh modulo $P$
from $0\le j\le J_m=\lceil m2^P3^mP\rceil$ has gaps at most $P/m$.

Set $J=\lfloor\sqrt{\log X}\rfloor$ and
$m=\lfloor(\log J)/(2\log 3)\rfloor$. For large $X$, $J_m\le J$.
In the proof of FS-002 use $\delta=P/m$ and set
$\epsilon=2^{10P/m}-1=O_P(1/\log\log X)$. For
$N=\lceil 10m+10\rceil$, $n>N$ guarantees that the logarithmic error is
below $\delta$ by $z_0\ge(2n-1)/3$. The interior margins for each additive
gate offset have width at least a constant times $X/m$, which tends to
infinity. One can take
$a=\min(1,A/(10M))\,2^{-3P(J+1)}$. Hence $aX\to\infty$,
$A_b(aX)\ge c_b(aX)^\gamma$, and $A_b(N)\le N=O(\log\log X)$.
The loss from the input scale is $\exp(-O_{P,\gamma}(\sqrt{\log X}))$,
and the additional counting divisor $6P(J+1)|D-D|$ is absorbed by slightly
increasing $H$. This proves the displayed estimate, with constants
independent of $b$ except for its lower coefficient and cutoff.

The finite replay `python -B research/fixed-floor-shells/check.py` found a
maximum fiber of four on inputs up to 10,000, checked 2,880 exact modular
rotation steps, and reconstructed 303 two-source gates in shells of relative
width 1/20. The largest selected rotation depth was 47. This checks the
displayed constructions in those ranges only.
