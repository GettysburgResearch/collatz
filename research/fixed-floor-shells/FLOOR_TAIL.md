# A divergent orbit forces an inverse-power floor tail

**FS-020. PROPOSED, conditional on an actual divergent positive orbit and
the source-qualified Lau predecessor estimate from [FS-008](TIMED_BLOCKS.md).**
Let $S_B$ comprise all positive integers whose entire ordinary Collatz
orbit stays above $B$. Put $p=25/11$ and
$h=H_2(\log_3 2)=0.9499555\ldots$, with $H_2$ binary entropy. If one
positive trajectory escapes to infinity, then for every sufficiently
large $B$,
$$
 \underline d(S_B)\gg B^{-p-(92/33)h}.
$$
In fact at every sufficiently large $B$ one single integer
$u_B\in(B,(3B+1)/2]$ on that escaping orbit occurs as the exact global
minimum of a set of starts of lower density at least the same bound.
The exponent is less than $4.93$. The constant is absolute given Lau's
constant, and the starting cutoff may depend on the escaping seed.
On a positive cycle with sufficiently large odd minimum $m$, the same
bound holds at $B=m-1$. Thus a floor upper of smaller asymptotic order
would exclude divergence and leave only finitely many positive cycles.

**Tail and pollution.** Choose the odd state $t$ just after the escaping
orbit's last odd value at most $B$. Then $B<t\le(3B+1)/2$, and all
its later odd and intermediate even values exceed $B$. It is prime to 3.
For every odd unit $y$, an inverse Syracuse step of exponent $a$ sends
it to $(2^a y-1)/3$ when integral. In any six consecutive exponents,
two give an odd unit output. Choose a single fixed-range exponent between
12 and 17 to obtain a root $r\asymp B$ above $100 B$. Its forward tail
also stays above the floor.

Any integral seed at most $B$ whose trajectory enters this inverse tree
and escapes has a last odd value $s\le B$. Distinct incomparable
vertices, each with an entirely above-floor future, that admit such
small ancestors require distinct last exits $s$. There are only
$O(B^h)$ possible exits: $s\ge(2B-1)/3$, and the subsequent shortcut
states exceed $B$ (including even intermediates). For
$L=\lfloor\log_2 B\rfloor$, if the first $L$ shortcut steps have $q$
odd inputs, then
$$
 B<T^L(s)\le s\,3^q2^{-L}\exp(O(L/B)).
$$
Thus $q\ge L\log_3 2-O(1)$. Each parity word fixes a unique residue
modulo $2^L$, occurring at most three times below $B$; the binomial
tail is $O(2^{hL})$ by Stirling. Write $M=\lceil C B^h\rceil$ with
a sufficiently large universal constant to bound the number of exits.

**Inverse antichain.** The [integer replay](check_floor_tree.py) checks
the following finite inequality for every odd unit $y$. Take all blocks
of six inverse Syracuse steps with $1\le a_i\le13$, each intermediate
an odd unit, and $D=2^{\sum a_i}/3^6\ge11/10$. Then
$$
 \sum_{\rm blocks}D^{-3/5}\ge17937772/16777216>1.
$$
The replay enumerates the starting unit residues modulo $3^7$, since
one factor of 3 is removed at each inverse step. It computes a lower
integer approximation to each weight by testing fifth powers, and the
displayed minimum is attained for the rounded sum at residue 2023.
The endpoint is $z=Dy-e$ with $e\ge0$ bounded by an absolute constant
over this finite dictionary. Thus for sufficiently large $B$, every
block endpoint from $y\ge r$ is at least $1.05y$ and at most $C_0 y$.
Intermediate steps are at least $(2/3)^6(y+1)-1>B$. All forward
routes from these nodes through $r$ stay above the floor.

Give each endpoint $z$ weight $(r/z)^{3/5}$. Its children have total
weight at least its weight by the displayed inequality. Stop each branch
at its first block endpoint above $Y=r(3M)^{5/3}$. This is a finite cut
since each block expands, and every leaf lies in $(Y,C_0Y]$. Total
weight is at least one, giving at least $3M$ leaves. Distinct leaves
are incomparable even for their entire forward basins: a route to the
nonperiodic root is unique, and the first-crossing stopping criterion
makes its block paths prefix-free. If an unaligned depth were involved,
each depth to the root is a multiple of six, so their difference is
also a multiple of six.

At most $M$ leaves admit any ancestor at most $B$. Every remaining leaf
has its entire predecessor basin in $S_B$. These basins are disjoint
and their finite sum of lower densities is at least
$2M D_A^{-1}(C_0Y)^{-p}$ by Lau. Substituting $r\asymp B$ and
$M\asymp B^h$ gives the claim.

For the atom refinement take $u_B$ to be the minimum of the odd tail
from $t$ onward. All tree routes stay above $u_B$ before reaching $t$:
the intermediate inverse states are at least $(2/3)^6(r+1)-1>2B$.
The tail from $t$ attains $u_B$ and never goes below it. Count polluted
leaves with a predecessor at most $u_B-1$ in place of $B$, using the
last-exit argument at that floor and increasing the universal constant
in $M$. On every remaining full basin the exact ordinary global
minimum is $u_B$. The same argument gives the atom at the minimum of
each sufficiently high cycle. In particular, if $p_u$ is the limiting
minimum law, divergence or infinitely many cycles implies
$\sum_u p_u u^{p+(92/33)h}=\infty$: infinitely many distinct atoms
each supply a term bounded below by a fixed positive constant.

For the cycle claim use $B=m-1$ and start at the cycle minimum $m$.
Among the unit predecessors with exponents between 12 and 17, there
are two, at most one of which is on the cycle. Choose the other as $r$.
It is nonperiodic and its entire future stays above $B$. The argument
for last departures and the stopping cut applies verbatim. Infinitely
many distinct cycles would have unbounded minima since their state
sets are disjoint.

Without the finite replay, a weaker inverse-power lower follows by taking
two increasing unit predecessors per step with $2\le a\le7$ for
$\lceil\log_2(2B)\rceil$ steps, then discarding at most $B$ leaves.

**Summability boundary.** Even summing the available *absolute* Lau
coefficients $D_A^{-1}u^{-p}$ over every possible integer target $u>B$
gives only $O(B^{1-p})$. A joint estimate over many tail edges using
only additive contributions of these coefficients cannot produce an
inverse-logarithmic floor lower. The known upper estimates of every
fixed inverse-logarithmic order permit the polynomial lower above.
