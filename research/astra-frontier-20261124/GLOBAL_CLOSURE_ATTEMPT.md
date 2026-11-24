# Odd-step cost of a smaller ordinary merger

**PROPOSED, elementary written proof.** Use the shortcut map $T(z)=z/2$ for even $z$ and $T(z)=(3z+1)/2$ for odd $z$. Let $p_a(x)$ count odd inputs among the first $a$ clocks. All sources and merger endpoints in the theorem are positive ordinary integers. A signed integer used in the proof is stated explicitly.

## A source-fixed necessary condition

**Theorem.** Suppose $n\equiv-1\pmod {2^b}$, $e=v_3(n)$, and $0<x<n$. If $T^a(x)=T^b(n)$, then

$$p_a(x)>b+e,\qquad a>b+e.$$

The condition on $n$ means its first $b$ inputs are odd. The claim applies to every ordinary competing history, including unequal clocks and arbitrary alternative parity words.

For a length-$h$ word used by a source $z$, write $2^hT^h(z)=3^p z+C$. The carry $C$ is nonnegative and at most $3^h-2^h$. Appending a parity $i\in\{0,1\}$ changes it to $3^iC+i2^h$, which proves the bound by induction. The all-odd word attains the bound. In particular $T^d(z)+1\le(3/2)^d(z+1)$ on positive integers. Since $T^b(n)+1=(3/2)^b(n+1)$, a competing smaller source must have $a>b$.

Put $D=a-b$. Let $p_1,p_2$ be the odd counts on the first $D$ and last $b$ competing clocks, and put $k=b-p_2$. With $C$ the carry on those last $b$ clocks, the equality of endpoints gives

$$T^D(x)=3^k n+m,\qquad m=(3^b-2^b-C)/3^{p_2},\qquad 0\le m<3^k.$$

Here $m$ is an integer by the first equality. Suppose $p_1\le k+e$. Then $J=3^kn/3^{p_1}$ is a positive integer, and $x_0=x-2^D J$ is an integer congruent to $x$ modulo $2^D$. Extend $T$ by the same parity formula to signed integers. Congruence modulo $2^D$ gives the same first $D$ parities, by one application of the map at a time. Subtracting the two affine equations yields $T^D(x_0)=T^D(x)-3^{p_1}J=m$. Every negative integer stays negative under $T$, so $x_0\ge0$. If $x_0=0$, then $p_1=0$ and $x=2^D3^kn\ge n$. If $x_0\ge1$, nonnegativity of the prefix carry gives

$$3^{p_1}x_0\le 2^D m<2^D3^k.$$

Hence $2^D3^k>3^{p_1}$ and $x=x_0+(2^D3^k/3^{p_1})n>n$. Both cases contradict $x<n$. Thus $p_1>k+e$ and $p_1+p_2>b+e$, proving the theorem.

## A logarithmic obstruction, attained within a constant factor

Define $\tau(n)$ as the minimum $\max(a,b)$ in a merger with $0<x<n$, with value infinity if no such merger exists. For $H\ge1$, all positive members of the single class

$$n\equiv-1\pmod {2^H},\qquad n\equiv0\pmod {3^H}$$

have $\tau(n)>H$. Indeed every $b\le H$ satisfies the theorem, so a successful $a$ must exceed $b+H$. The class has ordinary density $6^{-H}$ and has a member $3^H\le n<6^H$. Thus a bound $o(\log n)$ for all two-clock searches cannot hold.

There is a subprogression where a smaller partner is explicitly supplied just beyond the forbidden clock box. Put $s=\lceil H\log_2(3/2)\rceil$. Write $n=2^H j-1$ and further require $3^Hj\equiv1\pmod{2^s}$. This specifies one class of $n$ modulo $2^{H+s}$, compatible by CRT with $3^H\mid n$. Its first $H$ inputs are odd. Its next $s$ inputs are even since $T^H(n)=3^H j-1$ is divisible by $2^s$. Moreover

$$T^{H+s}(n)=\frac{3^H(n+1)-2^H}{2^{H+s}}<n.$$

Indeed $2^{H+s}-3^H$ is a positive integer and $n\ge3^H>3^H-2^H$. All earlier iterates on this word are at least $n$, since $(3/2)^H>2^{s-1}$. Thus every source in this progression has first forward descent exactly at $H+s$, and

$$H+1\le\tau(n)\le H+s=\lceil H\log_2 3\rceil.$$

Its least positive source is below $2^{H+s}3^H<2\cdot9^H$. This also disproves a uniform $o(\log n)$ merger-clock bound restricted to sources with a certified strict descent. The upper certificate uses $x=T^{H+s}(n)$ and $a=0$.

## Cost in any prescribed ordinary basin

For each fixed odd $t$ coprime to three, the fixed-basin counting comparison in `QUANTITATIVE_GLUING.md` applies to the progression in the preceding paragraph. Thus in $B_t$ the subset with the displayed two-sided clock bound has both the full lower and upper logarithmic counting exponent of $B_t$ for each fixed $H$. The constants in the counting comparison may depend on $H$.

An explicit size bound within $B_t$ also follows directly. Choose the unique $1\le r\le 2\cdot3^{2H-1}$ satisfying

$$2^r t\equiv 3^H2^{-H}-1\pmod {3^{2H}}.$$

The right side is a ternary unit, and $2$ generates the units of this modulus. Put $j=(2^rt+1)/3^H$ and $n_H=2^Hj-1$. Then $3^H\mid n_H$, $n_H\equiv-1$ modulo $2^H$, and the literal path has $T^H(n_H)=2^rt$, $T^{H+r}(n_H)=t$. Positivity and integrality follow from the congruence. It follows that

$$3^H\le n_H\le (t+1)2^{2\cdot3^{2H-1}},\qquad \tau(n_H)>H.$$

For $3^H>t$ this is itself a finite smaller merger. For each such fixed basin these sources rule out a bound $o(\log\log n)$ on $\tau(n)$ even among starts known to reach its specified target. The elementary logarithmic lower bound from the preceding paragraph uses sources from an unspecified basin.

## Global boundary and sources

The source-bounded induction from PR184 needs a partner below each originally prescribed source. The theorem forces a growing odd-count excess for an entire arithmetic class at arbitrarily many fixed finite horizons, including in each prescribed target basin. The explicit descent subprogression meets the required source inequality for each of its members. The proof supplies neither an eventual upper bound for $\tau$ on the larger class nor a merger for every positive input. It excludes uniformly short menus and leaves the unrestricted Collatz conjecture open.

Source pins for the induction interface are [PR184, packet](https://github.com/GettysburgResearch/collatz/blob/366dab89ee9548084ab9b5e4e90ff82abf287a20/research/lean-band-coupling-20261121/README.md) and [PR184, combination attempts](https://github.com/GettysburgResearch/collatz/blob/366dab89ee9548084ab9b5e4e90ff82abf287a20/research/lean-band-coupling-20261121/LATEST_CONNECTIONS.md). The comparison-localization theorem has a different pair of endpoints and preserves its fixed-source coverage obligation. [PR146, five closure](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md). The integrated first-edge barrier for multiples of three bounds peak rank for a different rank function; the statement above concerns ordinary value order and alternative odd counts. [Earlier rank barrier](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass5/MERGING_BARRIERS.md).

## Finite controls

The independent ordinary-step replay in `check_global_barrier.py` tested every smaller source among $1\le n\le1500$, every competing clock $0\le a\le20$, and every $0\le b\le v_2(n+1)$. All 7,413 exact mergers satisfied the odd-count inequality. Sixteen had both $b>0$ and $v_3(n)>0$. It also verified the stated first forward descent for three sources in each of the 120 subprogressions $H=1,…,120$, and the finite basin constructions for $H=1,…,4$ and $t=1,5,7,11,13$. These checks exercise the arithmetic separately from the written proof.
