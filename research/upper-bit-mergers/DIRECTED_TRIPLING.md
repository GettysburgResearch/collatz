# Every forward tripling has a bounded directed return path

**Proposed theorem.** Allow an ordinary Collatz edge in either direction and a tripling edge only in the direction $n\to3n$. There are absolute constants $L,H$ such that, for every odd positive $x$, there is a directed path from $3x$ to $x$ of length at most $L$, all of whose vertices belong to $[x/H,Hx]$. All tripling sources on the path are odd. Moreover, each source is given by one of a fixed finite list of positive-slope rational affine functions of $x$. Combined with [forward generation from 1](THREE_RAY_ONE_SIDED.md), this makes the augmented directed graph strongly connected. The return path can use extra forward triplings, so it does not prove the ordinary merger of $x$ and $3x$.

## Descending through powers of three near $t-1$

Write $g(t)=t-1$, use $\sim$ for an ordinary undirected connection, and use $\leadsto$ for a directed path. The identity $T(2h-1)=3h-1$ gives $g(2h)\sim g(3h)$. The following path uses one forward tripling and at most seven edges:
$$
 g(12h)\sim g(8h)\longrightarrow 3(8h-1)
 \longrightarrow 4(9h-1)\longrightarrow 2(9h-1)
 \longrightarrow g(9h)\sim g(6h)\sim g(4h).
$$
Therefore for every $i\ge3$ and positive odd $u$,
$$
 g(3^i u)\sim g(12\cdot3^{i-3}u)\leadsto
 g(4\cdot3^{i-3}u)\sim g(3^{i-1}u). \tag{1}
$$
Each outer connection uses two exchanges. The sole tripling source is $8\cdot3^{i-3}u-1$.

Every block of four consecutive exponents $e$ contains one with $3^e u\equiv3$ or $5\pmod{16}$. Indeed $\langle3\rangle=\{1,3,9,11\}$ modulo 16 and the other coset contains 5. At either target $Y$, we have $Y\sim g(Y)$ by an ordinary meeting: $2,3$ meet after four steps with two odd steps per arm, and $4,5$ meet after three with one odd step per arm. Equal odd counts lift the respective words to shifts by multiples of 16 or 8.

Now take $x=3^5u$ with $u$ any odd number, including multiples of three. Choose $b\in[2,5]$ and $a\in[6,9]$ such that $3^b u$ and $3^a u$ both have these neighbor mergers. Starting from $3x=3^6u$, triple up to $3^a u$, cross to $g(3^a u)$, descend by (1) to $g(3^b u)$, cross to $3^b u$, and triple up to $x$. This constructs a bounded return whenever $3^5\mid x$.

## Connecting all remaining tripling edges to this case

For $3^5\nmid x$, write $x=3^j u$, where $0\le j\le4$ and $u$ is odd and prime to three. There exists an integer $j<a\le31110$ satisfying both
$$
 2^au\equiv1\pmod{3^6},\qquad 3^a u\sim 3^a u-1. \tag{2}
$$
For the first condition, $2$ generates the units modulo $3^6$, so choose $a_0$ in $[j+1,j+486]$ meeting it. For example $v_3(2^{2\cdot3^k}-1)=k+1$ proves the asserted order $486$. As $a$ runs through $a_0+486r$ for $0\le r<64$, the values $3^au$ run through every residue modulo 512 in their fixed class modulo 8. Indeed $v_2(3^{486}-1)=3$, and each subsequent squaring increases this valuation by one. Each of the four odd classes modulo 8 has an ordinary neighbor merger on a subclass, as shown in the table. Thus (2) holds in the stated range.

| $Y\bmod 8$ | Sufficient $Y\bmod 2^h$ | $h$ | Common endpoint of $Y-1,Y$ at the listed base | Odd steps per arm |
|---:|---:|---:|---:|---:|
| 1 | 369 mod 512 | 9 | 20 | 3 |
| 3 | 3 mod 16 | 4 | 2 | 2 |
| 5 | 5 mod 8 | 3 | 2 | 1 |
| 7 | 23 mod 32 | 5 | 20 | 3 |

Put $z=(2^a u-1)/3$. This is a positive odd multiple of $3^5$. Applying the odd ordinary step followed by halvings gives $z\sim u$. The native exchanges give
$$
 3z=g(2^a u)\sim g(3^a u)\sim 3^a u.
$$
Now travel from $3x=3^{j+1}u$ up to $3^a u$ by forward triplings, take these ordinary connections to $3z$, use the previously proved directed return $3z\leadsto z$, take $z\sim u$, and triple $j$ times to $x$. All paths stay positive, including when $u=1$, since $a>0$ and $3^5\mid z$.

The source list can be specified without enumerating large integers. For the high case with input $3^5v$, use the forms $3^i v$ for $0\le i\le9$ and $8\cdot3^i v-1$ for $0\le i\le6$. For the low case add the forms $3^i u$ for $0\le i\le31110$, and the high-case forms with $v=(2^au-1)/3^6$. Here $u=x/3^j$ with $0\le j\le4$. In the original high case $v=x/3^5$. Each form is injective on its applicable inputs, with positive slope. All loops and ordinary words in the construction have bounded lengths. Each elementary move changes height by at most a factor of three in either direction, giving the asserted height bounds. The resulting absolute constants are large.

## Consequences for directed cuts

Let $A$ be any union of ordinary merger components. Write $E_+$ for odd $d\in A$ with $3d\notin A$ and $E_-$ for odd $d\notin A$ with $3d\in A$. For every $x\in E_+$ the return path starts outside $A$ and ends inside, so it contains a tripling at a source in $E_-$. Interchanging the colors gives the converse. By the finite affine source list and its injectivity, for absolute $K,H$ and either sign,
$$
 |E_\pm\cap[R,bR]|\le K\,|E_\mp\cap[R/H,HbR]|,\qquad
 |E_\pm\cap[1,X]|\le K\,|E_\mp\cap[1,HX]|. \tag{3}
$$
Thus either directed count controls the total cut. In particular a real-valued ordinary invariant satisfying $f(n)\le f(3n)$ for every $n$ must be constant: it is nondecreasing on the directed graph, which is strongly connected. An individual nonempty ordinary component closed under forward tripling would imply full Collatz, regardless of which component it is.

If Collatz is false, take $A$ to be the basin of 1. There are absolute $B>1$ and $c>0$ (with the coefficient allowed to depend on a fixed second component) such that every sufficiently large $R$ has at least $cR^{0.164}$ odd $d$ of **each orientation** in $(R,BR]$. Thus one set consists of convergent $d$ with nonconvergent $3d$, and the other of nonconvergent $d$ with convergent $3d$. Indeed apply (3) to the [fixed-ratio cut lower bound](ODD_TRIPLING_SHELLS.md) after rescaling $R$. Its uniformity over cuts also gives $cR^{0.164}$ edge-disjoint **directed** paths between any two specified distinct components in the graph of forward triplings from that window, in each specified direction separately, by directed max-flow/min-cut.

For each fixed $c>0$, each orientation separately also has at least $cS^{0.84}$ sources in $[S,2S)$ for some dyadic $S\in[Y,Y^{32}]$, for every sufficiently large $Y$. The chosen $S$ may depend on the orientation. In the [two-scale proof](TWO_SCALE_TRIPLING.md#comparing-two-different-dyadic-scales), use the cut indicator of $A$ and its total crossing count in (2) there. The cumulative inequality (3) bounds that total by either directed count at a fixed dilation. This changes only the absolute constants $C_0,C_1$ in that argument. The available ordinary upper bound still leaves a gap above both lower exponents. [Ordinary upper bound](THREE_RAY_UPPER.md)
