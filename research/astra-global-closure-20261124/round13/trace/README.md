# Attained clocks give a central source count without renewal

**PROPOSED written results on positive ordinary integers.** A failure
of Collatz forces central inverse-word counts at actual selected
balanced rows with the natural real width and the square-root
population loss, without a Fourier or renewal floor. It forces
consecutive nonconvergent blocks in the same thin original-source
intervals without either proposed input F or S. At fixed precision the
selected patterns recur as exact translates perpetually.

## Which rows can be selected

Let $a$ be a fixed positive odd unit that does not reach one. With
$U$ the odd accelerated map, let $q_i=U^i(a)$ and $A_i$ be the sum
of the first $i$ positive valuations. All $q_i$ are units at least
five. Put $L_i=2i-A_i$. Then $L_0=0$,
$L_{i+1}-L_i=2-\nu_2(3q_i+1)\le1$, $L_i\le i$ and
$$
 L_i\ge \alpha i-\log_2 a,\qquad \alpha=\log_2(5/4)>0.
$$
Indeed $2^{A_i}q_i=a\prod_{j<i}(3+1/q_j)\le a(16/5)^i$.
For **every** integer $t\ge0$ the first index $i(t)$ with $L_i\ge t$
has $L_{i(t)}=t$ and
$t\le i(t)\le\lceil(t+\log_2 a)/\alpha\rceil$.
This applies to a hypothetical nontrivial cycle as well as escape.

Fix $k,h,J$ with $h,J\ge1$ and $h+J\le k/10$. Prescribe an odd
residue $r\bmod2^h$ and a unit $v\bmod3^J$. Its binary parity prefix
has $p$ odd inputs, $1\le p\le h$. Define
$$
 n=k-p-1,\quad H=h+2n,\quad
 P=2\cdot3^{k+J-1},\quad W=C_*\,2^H/3^k.
$$
Here $C_*$ is one absolute constant. For every sufficiently large
$k$, in **every** full period $[S_0,S_0+P)$ of integer clocks with
$S_0>\max(H,2k)$, at least $cP/\sqrt{k}$ clocks $S$ have the
following property. Use the actual $i=i(S-2k)$, $b=i+k$,
$q=q_i$, and $Z=a2^S/3^k$. In $[Z-W,Z)$ there are at least
$$
             c\,\frac{W}{2^h3^J\sqrt{k}}                         \tag{1}
$$
distinct positive ordinary units $x\equiv r\pmod{2^h}$,
$x\equiv v\pmod{3^J}$. Each reaches $a$ after exactly $S$
shortcut steps and $k$ odd inputs and reaches the **same actual**
$q$ at the balanced row $(b,2b)$. Each has relative affine carry
at least $1/(3a+1)$ at $q$, because the appended true suffix has
$i\ge1$ and its distortion product includes $1+1/(3a)$.
Choosing a different cell can change $S,i,b,q,Z$.

Take $k=\lfloor(\log_3 B)/2\rfloor$ for a large observation scale
$B$, so $P=o(B)$ uniformly over the stated cells. In $[B,2B)$
there are $\gg B/\sqrt{k}$ successful attained clocks, giving as many
distinct balanced rows with $B-k\le b\le 2B/\alpha+O_a(k+1)$.
Thus $k\asymp\log b$ and $W=\exp(\Theta(k))$ is polynomial in $b$,
while $Z\ge\exp(cB)$. The selected rows can be different for each
cell, but the full period and the actual first-passage rule are fixed.
The global terminal-uniform input F of Weaver–Wren remains separate.
[Paper 48, v2, (76), (82)–(83)](https://rstation.ai/problems/collatz/papers/48)

## Exact original-source phase ledger

After the prescribed $h$ bits append any binary word of length
$2n$ with exactly $n$ ones. The concatenated physical word $w$
has $k-1$ odd inputs. Write $2^H y=3^{k-1}x+C_w$ and
$\beta_w=C_w/2^H$. Append one odd gap of length $S-H$ from $y$ to
$a$. Eliminating $y$ gives
$$
 D_w=2^H+3C_w,\qquad 3^k x=a2^S-D_w,\qquad Z-x=D_w/3^k.          \tag{2}
$$
In particular $D_w$ is a ternary unit. The single congruence
$$
                  a2^S\equiv D_w+3^k v\pmod{3^{k+J}}               \tag{3}
$$
selects exactly one $S\bmod P$ for each $w$. The order of 2 modulo
3 is 2, and $\nu_3(4^{3^j}-1)=j+1$ by induction: cubing
$1+3^m u$ with $3\nmid u$, $m\ge1$, increases the valuation by one.
This gives the full unit group at every power.
Since $S>H$, (3) gives the odd integral $y=(2^{S-H}a-1)/3>0$
and the integral source in (2); the first divisibility uses
$D_w\equiv2^H\pmod3$. Reading $w$ backwards, a final even bit
takes $y$ to $2y$, and a final odd bit takes $y$ to $(2y-1)/3$.
For an odd bit the required divisibility follows from the remaining
affine equation modulo three. Both inverse moves preserve positivity
when integral. Equivalently, forward parity decoding of the scaled
equation is exact (see the Lean kernel). The prefix for $r$ has
precisely that source class, since successive binary digits fix
successive parities bijectively through the odd free coefficient.
Different words at this $S$ give different sources by determinism.

The central-clock bounded-offset estimate needs no target mixing.
For a uniformly chosen length-$2n$ word with $n$ ones, let $X_l$
count the ones in any specified $l$ positions. With $z=\sqrt3$,
expanding $\prod(1+(z-1)\epsilon_j)$ gives
$$
 \mathbb E z^{X_l}\le(1+(z-1)/2)^l .
$$
The probability that all $d$ selected positions are one is
$(n)_d/(2n)_d\le2^{-d}$ (zero when $d>n$). The real affine offset
over the middle word is
$\frac12\sum_{j=1}^{2n}\epsilon_j 3^{X_{2n-j}}2^{-(2n-j)}$ with
$X_{2n-j}$ on the suffix after $j$. The triangle inequality for
square roots and the preceding bound give
$\mathbb E\sqrt{\beta_{\rm middle}}\le
2^{-1/2}\sum_{l\ge0}\rho^l$ with
$\rho=(1+\sqrt3)/(2\sqrt2)<1$. The initial offset is at most
$(3/2)^h$ by the elementary carry recurrence. Its propagated
contribution to $\beta_w$ is at most
$(3/4)^n(3/2)^h\le1$ for large $k$. Consequently at least half
the words have $1+3\beta_w\le C_*$ for one absolute $C_*$.

Retain exactly those words. At every attained $S$ their sources
lie in $[Z-W,Z)$ by (2). Over a complete period the sum of source
counts equals the total number of retained words by (3), between
$\tfrac12\binom{2n}{n}$ and $\binom{2n}{n}$. The mean is therefore
$\asymp4^n/(P\sqrt n)\asymp W/(2^h3^J\sqrt{k})$. An individual
clock contributes at most $1+W/(2^h3^J)$ by the original-source
integer lattice. Uniformly under $h+J\le k/10$ this quotient grows
exponentially: $2^{2n}/3^{k+J}\gg(4^{9/10}/3)^k$, using $p\le h$
and $\log4>\log3$. Splitting at half the mean gives the asserted
$\gg P/\sqrt k$ successful clocks. This also proves a matching
upper in the full-period mean and a pointwise upper at a fixed
positive fraction of the attained clocks by Markov. These estimates
concern this explicitly cut pre-pad family, not every inverse
source at the terminal.

For fixed $k,r,v$ the whole retained word set is identical at
$S$ and $S+P$. Its complete original-source packet translates by
$a(2^{S+P}-2^S)/3^k$, an integer divisible by $2^h3^J$.
Any one successful packet thus recurs at arbitrarily late actual
rows. Along escape the $q_i$ are distinct; for an eventual cycle
they can coincide. On escape, a single forward trajectory contains
**at most one** member of a given packet: if $x'=T^d(x)$ were a
different member, applying the common gate clock $S$ would give
$T^d(a)=a$. Thus a translated upper bound for the vertices of one
simple path cannot upper-bound this packet in its inverse basin.

## Consecutive blocks at a common row

The [constructive synchronization lemma](STEERING.md) gives an odd
residue modulo $2^h$, $h\le C M^A$, on which $M$ successive starts
have equal physical endpoints **and grades** at $h$. Apply (1) at
that cell with $J=1,v=1$. For each such $x$, all $x+j$, $0\le j<M$,
reach $a$ after $S$ physical steps with $k$ odd inputs and $q_i$
after $2b$ with $b$ odd inputs. Every member lies below $Z$:
its affine carry to $a$ is strictly positive since $k\ge1$.
The whole block is thus in the original band. Even or ternary-divisible
members are counted as ordinary shortcut starts, not odd units.
Greedy selection of intervals discards at most $2M-1$ first starts
per retained interval, giving at least
$$
       c\,W/(2^h\sqrt{k}\,M)
$$
pairwise disjoint blocks. In fact the starts in this particular
construction have spacing at least $2^h3$, so whenever $M\le2^h3$
they are already disjoint. The displayed bound needs no spacing check.

For $M=\lfloor c_0(\log k)^{1/A}\rfloor$ with $c_0$ small, take
$h\le\log_2 k$; these blocks cover at least $cW/k^{3/2}$ starts.
Since $W=\exp(\Theta(k))$, their covered population exceeds
$W^{1-\delta}$ for every fixed $\delta>0$ at large $k$. Taking
instead $M=\lfloor c_0 k^{1/A}\rfloor$ gives $h+1\le k/10$,
so there are still $\exp(\Omega(k))$ disjoint blocks, with the
weaker relative density stated above. Both alternatives hold at
$\gg B/\sqrt{\log B}$ actual balanced rows of scale $b\asymp B$
for the indicated choice $k\asymp\log B$.

## A provably convergent family refutes a gate-uniform sparse upper

At every finite observation scale the entire packing can occur on
ordinary integers with an explicit path to one. Fix an integer
$m>2B+1$, put $d=3^m$, and define
$$
 u=(2^d+1)/3^m,\qquad a_m=2^m u-1 .
$$
Cubing an integer $-1+3^l t$ with $3\nmid t$, $l\ge1$, increases
the valuation of its sum with one by exactly one. Starting at $2$
gives $\nu_3(2^{3^m}+1)=m+1$, so $u$ is a positive multiple of
three and $a_m$ is an odd ternary unit. For $0\le j\le m$,
$$
            T^j(a_m)=3^j2^{m-j}u-1,\qquad T^m(a_m)=2^d .
$$
All $m$ shortcut inputs are odd and then $d$ halvings reach one.
The **accelerated** clock satisfies $A_i=i$ for $0\le i<m$.
The final accelerated gap through $2^d$ has length $d+1$.
For every clock $S\in[B,2B)$ above $2k$, $i=S-2k<m$ is its
actual first passage. Equations (1)–(3) and the complete block
argument therefore apply at this finite scale on known convergent
integer sources, with actual endpoints $q_i>1$.

It follows unconditionally that a bound $o(W/(2^h3^J\sqrt{k}))$
uniform in the supplied gate at all such actual rows is false,
even if restricted to convergent sources. A bound $O(W^{1-\delta})$
on the total number of convergent starts in the asserted common
row and band is equally false for fixed $\delta>0$. The gates vary
with $B$. Their carry threshold $1/(3a_m+1)$ tends to zero, and
their terminals can exceed the round-twelve height cutoff.
Consequently neither counterexample concerns a uniform positive
carry threshold on one fixed escaping gate. A deficit involving
those restrictions is still open.

## An upper bound on the harmonic mass of all the indicated bands

Fix $c,C,A>0$. For each $b$, allow at most $b^A$ positive integer
gates, $cb\le S\le2b$, $0\le k\le C\log b$, and **every** integer
in the band $[a2^S/3^k-b^A,a2^S/3^k)$. Their union for all $b$
has finite sum of reciprocals. Indeed each level supplies at most
a polynomial in $b$ many integer slots, with every slot beyond
$2^{cb}/\operatorname{poly}(b)$ for large $b$. The tail over
$b\ge B$ is at most $\operatorname{poly}(B)2^{-cB}$. This applies
even if every allowable source slot is filled. For any one fixed
nonconvergent gate the block theorem would give arbitrarily long
consecutive runs within that union, hence upper Banach density
one alongside logarithmic density zero. All its constructed
sources already descend to a value at most that fixed $a$.
[Tao's logarithmic-density orbit-minimum theorem](https://arxiv.org/abs/1909.03562)

Moreover two such bands for odd ternary-unit gates can overlap at
large $b$ only if the triples $(a,S,k)$ coincide. Indeed factor
the difference of their centers by
$2^{\min(S,S')}/3^{\max(k,k')}$; the remainder is a nonzero integer
unless the centers agree. In the equality case the binary and
ternary valuations first force $S=S'$ and $k=k'$ and then $a=a'$.
The nonzero spacing exceeds every allowed polynomial width.
Thus comparing two independently supplied unit gates by intersecting
their long-pad original bands cannot yield a common source. An odd
multiple of three cannot itself be an accelerated output, since
$3x+1$ is prime to three.

## Boundary of the argument

PR201 provides an elementary lower count across its full logarithmic
menu in a wider band and a conditional F and S refinement with
longer blocks and stronger density. Its elementary construction uses
two legal inverse choices per turn, a two-gap modular router and a
long pad at the actual gate. The pad cancels out of the absolute
source width in (2). We use that cancellation, and select actual
rows by the surplus clock so that the central words can be counted
directly over one ternary period. PR192's unrestricted-height opening
lifts need no transfer here: each source and its entire block are
recovered at the row's actual exponential height. We did not
compile the pinned PR201 file or independently verify its global
equivalence theorem.
[PR201 thin bands, frozen 02fb390](https://github.com/GettysburgResearch/collatz/blob/02fb390a76fb2ffb00fee612649ca23a82d99d31/research/killed-green-head-closure-20261124/thin-band/README.md)

The count supplies no deficit on the exceptional rows and no
pointwise upper for the unrestricted basin at these centers. The
big clock and the queried terminal move with the phase. At fixed
$k$ the intervals shift to exponentially separated heights. At
growing $k$ the swept period restricts the argument to logarithmic
pre-gate depth at the asserted row scale. It does not replace F
for the diffusive indices of round twelve or exclude nonconvergence.

[Finite Lean kernels](AttainedClock.lean) · [Exact integer controls](check.py)

[Finite-family physical mergers and their fixed-index obstruction](FINITE_FAMILY.md)
