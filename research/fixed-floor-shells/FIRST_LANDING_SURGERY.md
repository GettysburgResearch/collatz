# A sparse perturbation preserving the first-landing estimates

Suppose the native Syracuse map $U$ has the selected first-landing paths
of rStation paper 12, Lemma 13 and proof of Theorem 14, and the finite-shell
upper bounds of paper 102, Theorem 1. For every finite set of initial
positive integers there is a deterministic map on positive integers
which agrees with Collatz along their entire orbits, halves every even
integer, and changes the odd rule at $O(\log(2X))$ points up to $X$.
Its odd updates never exceed $3n+1$. Its induced odd map has a new
escaping component of positive lower density. It retains the selected
first-landing lower bounds **including both clocks**, and the finite-shell
first-landing set and failure upper bounds at the original power.
[Paper 12 v1](https://rstation.ai/problems/collatz/papers/12/v1) ·
[Paper 102 v1](https://rstation.ai/problems/collatz/papers/102/v1).

## Construction

Write $\mathcal C=y\bmod 3^h$ for the fixed unit cylinder in paper 12,
with $h\ge1$. Choose the other nonzero residue $z\bmod3$ and fix an
integer $K\ge500$. At each level $j\ge j_0\ge1$, select the odd $u$ in
$[K,4K)$ satisfying $4^j u\equiv1+3z\pmod9$. They form a nonempty
class modulo 18 in that interval. List the integers
$$ r=(4^j u-1)/3 $$
by increasing level and increasing $u$ within each level, obtaining
$r_1<r_2<\cdots$. Each $r$ is an odd unit congruent to $z\bmod3$
and has native image $U(r)=u$. Adjacent values of $3r+1$ have ratio
at most $1+18/K$ within a level and at most $4(K+18)/(4K-18)$
between levels. Both ratios are below $6/5$. It follows that
$2r_{i+1}\le3r_i+1$. There are $O(K)$ points per level and
$O(\log(2X))$ levels up to $X$.

Let $D$ be the fixed finite set of odd integers in $[K,4K)$.
On any deterministic orbit a given $u$ has at most two distinct
immediate predecessors along that orbit. After the first repeated
visit to $u$, its return path is periodic. Each prescribed starting
orbit therefore encounters only finitely many candidates $r$ because
each such visit is followed by a member of $D$. Choose $j_0$ high enough
to avoid all of them and give $r_1>4K$. Set
$\widetilde U(r_i)=r_{i+1}$ and retain the native map at all other odds.
On ordinary integers implement each altered odd step as $r_i\mapsto
2r_{i+1}$ and keep standard halving. The entire finite catalogue follows
its original paths. The new spine tends to infinity.

## First-passage comparison

Write $W_X$ for a uniform odd source in $(X/4,X]$. For a threshold $M$,
record the first odd iterate at most $M$ together with the passage time,
using one cemetery label for infinite passage. Time zero counts. For
$M\ge4K$ and **each** starting odd integer the only possible change to the
record is a finite record at some $u\in D$ changing to the cemetery.
Indeed, before the first changed edge the two paths agree. If it is
taken before passage, its source is an $r_i>M$. Its native image belongs
to $D$ and its new trajectory stays strictly above $M$. This argument
also works with marked native valuation words or both clocks on finite
records, since all retained paths agree edge by edge.

For any source law, the total variation distance of these joint laws
equals the probability $e_M$ of such a changed record, since all
changed mass moves from finite records to the cemetery. For $W_X$,
$X\ge4M$, paper 102 gives
$$ e_M\le F_M(|D|/M+M^{-g}),\qquad
g=1-H_2(\log_3 2)+1/351,\quad
F_M=C_0\exp(C_1\sqrt{\log M}). $$
Every finite set of landing labels retains its original upper bound,
and the new failure probability is at most $F_M(|D|/M+2M^{-g})$.
Increasing the absolute prefactor covers $2\le M<4K$ as well.
The argument concerns finite-shell distributions and requires no
limiting law for the perturbed map.

For an odd unit $a\le M$ and $X\ge CM$, paper 12 certifies at least
$cX/M$ native paths with last predecessor in $\mathcal C$ and all prior
states strictly above $M$. If $M\ge4K$, no edited edge can occur before
that final edge, since its native image in $D$ would already be a
landing. The last predecessor lies in the other unit class modulo 3
from every edited vertex. Thus all certified paths survive. For
$1\le M<4K$, use the same proof at floor $4K$ and target $a$, and
increase the onset and decrease the lower constant by fixed factors.
Those paths also first hit floor $M$ at $a$; replacing $4K$ by $M$
in the two clock centers of paper 12, (41), costs only $O_K(1)$.
The ordinary count on these paths is still the sum of the odd and
shortcut counts.

For every $M\ge r_1$ let $t$ be the least spine state above $M$.
Then $M<t\le(3M+1)/2$. Each selected native source first reaching
$t$ at floor $t$ follows the same path to $t$ for both maps, then
lands in $D$ for the native map and escapes for the new map. Thus
$e_M\gg1/M$ whenever $X\ge C'M$. At the fixed floor and target
$r_1$, the retained count gives positive lower density in every
sufficiently high shell to the new escaping component. The component
of the fixed point 1 also retains positive lower density. Every source
still contributes exactly one unit of probability to each complete
first-landing record, including the cemetery.

The exact perturbation exploits the last edge into a fixed finite
anchor set. The native valuation rule on the edited spine fails, so
any closure using that arithmetic identity on exceptional forward
edges needs a separate argument. The conclusion identifies a limitation
of first-landing estimates and total ordinary probability. The original
Collatz dynamics on the prescribed finite catalogue remain as before.
See also the [minimum first-moment criterion](FIRST_MOMENT.md) and the
[earlier prefix-tree model](FLOOR_CONTROL.md).

## Preserving every fixed horizon of native valuation data

The surgery can also preserve, simultaneously, the native odd output
modulo any prescribed positive integer $m$, and the **entire first $H$
accelerated valuation labels at every positive odd starting integer**
for any prescribed finite $H$. Here an output on the ordinary odd
step means the even integer before any halving. In fact the accelerated
odd outputs themselves can be made congruent modulo $m$ as well.
The construction below replaces the single edge into an anchor with a
fixed-length native path.

Write $m=2^b m_o$ with $m_o$ odd. Choose an integer
$L\ge\max(2,H,b+1)$ and $a\in\{1,2\}$ so that $2^{-a}\equiv z\pmod3$.
Put $N=3^{L+3}m_o$ and choose the fixed anchor scale $K\ge500N$.
At level $j$ use every odd $u\in[K,4K)$ satisfying
$$ 2^a4^j u\equiv 2^a-6\pmod N. $$
These $u$ form one residue class modulo $2N$. Define
$$
 w=(4^ju-1)/3,\qquad v=(2^a w-1)/3,\qquad
 r=2^L(v+1)/3^L-1.
$$
The congruence makes $w$ an odd integer with
$2^aw+2\equiv0\pmod{3^{L+2}m_o}$. Hence $w\equiv z\pmod3$,
$v$ is an odd integer, and $r\equiv-1\pmod{3\cdot2^Lm_o}$ is an odd unit.

The native path starting at $r$ takes $L$ steps with valuation 1
to $v$, then one step with valuation $a$ to $w$, then one with
valuation $2j$ to $u$. Indeed the first $i$ steps give
$(3/2)^i(r+1)-1$, odd for $i<L$ and also odd at $i=L$ by the
formula for $v$. Every intermediate vertex before $u$ exceeds $r$
for all sufficiently large $j$: the first $L$ steps grow strictly,
and $w/r\to 3^{L+1}/2^{L+a}>1$ as $j\to\infty$.
The vertices $r$ increase in the same order as $4^ju$, since $r$
is a positive affine function of this quantity. Using spacing $2N$
in place of 18 and $K\ge500N$ gives ratios below $6/5$ for adjacent
$4^ju$; for large $j_0$ the resulting consecutive $r$ again satisfy
$2r_{i+1}\le3r_i+1$. The finite-catalogue argument also survives:
the $r$ in any one orbit are at the same fixed lag $L+2$ before a
member of $D$, so only finitely many can occur. This holds whether a
given anchor occurs once or subsequently lies on a periodic tail.

Make the same replacements $r_i\mapsto2r_{i+1}$ on the ordinary
map. Both the native odd output after halving and $r_{i+1}$ are
$-1\bmod m$, since $L\ge b+1$. Both ordinary outputs are consequently
$-2\bmod m$. The valuation of the actual modified output is 1.
After arrival at an edited vertex the modified orbit has valuation
1 forever, while its native counterpart has at least the next $L$
valuations equal to 1. Up to first arrival the paths agree. This
proves equality of all first $H$ valuation labels at every start.

For $r_i>M\ge4K$ the native continuation stays above $M$ up to $w$
and lands at $u\in D$, whereas the modified continuation escapes.
A paper 12 witness hitting an edited edge before landing would
therefore have last predecessor $w\equiv z\pmod3$, excluded by
$\mathcal C$. These are exactly the two facts used in the first-passage
comparison and lower-bound proofs above. Every conclusion there holds
for this strengthened construction. The perturbation still changes
the native affine equality on the exceptional odd updates.

## Short trajectories and relative accuracy

For any fixed $0<\eta<1/4$, one may additionally require
$(1-\eta)(3n+1)\le\widetilde C(n)\le 3n+1$ at **every** odd $n$,
where $\widetilde C$ denotes the ordinary perturbed update. Indeed by
increasing $K/N$ the ratios of consecutive candidates $r$ can be made
at most $1+\eta$ for sufficiently large $j_0$. After each retained
spine vertex take the largest candidate $r'$ at most $(3r+1)/2$.
The next candidate exceeds that bound, so
$2r'>(3r+1)/(1+\eta)\ge(1-\eta)(3r+1)$. The sequence increases
strictly. The selected vertices still have the protected ramp and the
spine has successive ratios bounded above by $(3r+1)/(2r)$.
This thinning gives the claimed relative error without changing any
previous conclusion.

There is a separate comparison for all short shortcut paths. A native
shortcut source at most $X$ encountering a splice by time $h$ visits
one below $(3/2+1/2)^h X$. The shortcut has at most two predecessors
per state, so the number of these sources is
$O(2^h(\log(2X)+h))$. Outside them the entire shortcut prefix is
identical for both maps. At $h=\lfloor(1-\epsilon)\log_2 X\rfloor$
this is $O_\epsilon(X^{1-\epsilon}\log(2X))$. A union bound applies
to each fixed number of shifted sources. In particular every
density-one fixed-gap synchronous coalescence conclusion at this
horizon survives, as does an $O(1/\sqrt{\log X})$ exceptional
fraction. This comparison transfers actual finite trajectories without
requiring uniform control over the eventual effects of the sparse
splice. [Leen, exact synchronization rates](https://doi.org/10.5281/zenodo.23268751).
