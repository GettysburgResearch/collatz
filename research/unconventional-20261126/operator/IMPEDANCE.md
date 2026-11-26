# A computable first-parent hitting probability

**Status.** PROPOSED, with analytic proofs and a finite rational enclosure. Use the full and unit graphs and their counting-measure operators $L,L_U,G=L_U^{-1},Q=G1_HG$ from [the core analysis](CORE_HEAT.md). The function constructed here lives on ternary units. Its identification with an actual walk on positive integers below uses only specified ordinary off-cycle subtrees.

## OP-I1. A ternary function from the inverse electrical network

For $x\in\mathbb Z_3^\times$ unfold its unit inverse words into a rooted tree. A vertex labelled $y$ has a child $2y$ and, for $y\bmod9\in\{2,8\}$, another child $(2y-1)/3$. Two different words give different *vertices* of this tree, even if a label repeats. Connect one additional parent to the root by a unit edge. Write $h(x)$ for the probability that simple random walk from the root ever reaches this parent.

The effective resistance $R(x)$ from the root to infinity in the descendant tree alone satisfies $1\le R(x)\le7$. For the lower bound, a unit flow has flux one across every level and at most $2^k$ edges enter level $k$. Its energy is at least $\sum_{k\ge1}2^{-k}=1$ by Cauchy–Schwarz. For the upper bound, reach the first branch in at most three edges. Split a unit flow equally at every subsequent branch, transporting it unchanged through unary stretches. Each edge between successive branching vertices is subdivided into at most four unit edges, by the modulo-nine cycle in OP-G1. The energy following the first branch is at most $4\sum_{k\ge1}2^{-k}=4$. Thomson's principle, or its finite wired-level version followed by an increasing limit, gives the bounds. Putting the added parent at voltage one and wiring the distant level to zero gives
$$
 h(x)=\frac{R(x)}{1+R(x)},\qquad \frac12\le h(x)\le b=\frac78.
$$
The finite hitting events increase to ever hitting the parent, since a finite hitting path has finite maximal depth. This identifies the infinite voltage with the stated probability.

Let $e(x)$ be the indicator of the two branching residues. First-step decomposition gives
$$
 h(x)^{-1}=2+e(x)-h(2x)-e(x)h((2x-1)/3).
$$
The last term is omitted at a nonbranch. Indeed at each child the probability of reaching the extra parent is its own first-parent probability times $h(x)$ by the strong Markov property. The constant one also satisfies the formal equation; the construction and its strict upper bound select the hitting solution.

Kill at level $r\ge1$ of descendants and call the resulting probability $h_r(x)$. Killing at level zero gives $h_0=0$. The error is bounded uniformly:
$$
 0\le h(x)-h_r(x)\le b^{r+1}.
$$
After first reaching depth $r$, any path to the extra parent must successively hit each of the $r+1$ parents on its unique upward path. Until each success it lives in the corresponding descendant subtree, so the conditional success probability factors into $r+1$ terms, each at most $b$. This bounds even the unconditional error. The finite tree and that probability depend only on $x\bmod3^{r+1}$: each operation can lose at most one ternary digit, and deciding the branch at depth $r-1$ needs two digits. The limit $h$ is therefore computable and Hölder in the ternary metric, with exponent $\alpha=\log(8/7)/\log3>0$. For example, for $v_3(x-y)=k\ge2$ use $r=k-1$ and the shared value of $h_r$.

The reciprocal conductance identity also gives an exact conservation law. Put $C(x)=1/h(x)-1=1/R(x)$. Then
$$
 C(x)=\sum_{y\ {\rm child\ of}\ x}(1-h(y))
     =\sum_{y\ {\rm child\ of}\ x} h(y)C(y).
$$
The probabilities $p_x(y)=h(y)C(y)/C(x)$ sum to one. Iteration over the unfolded tree of depth $r$ yields $\sum_{\text{words }x=x_0,\ldots,x_r} C(x_r)\prod_{i=1}^r h(x_i)=C(x)$. The corresponding unweighted product sum lies between $C(x)$ and $7C(x)$. This identity concerns every inverse word with its exact weight.

## OP-I2. An anchored Green product and bounded harmonic functions

For the transient unit walk the probability to hit a specified $v$ from $u$ equals $G(u,v)/G(v,v)$. One derivation uses the discrete walk with transition matrix $J=I-L_U/3$ in OP-G3. Its holds leave hitting probabilities unchanged. The strong Markov identity for the expected number of visits to $v$ gives the ratio since $G=\frac13\sum J^k$.

If an ordinary unit $x$ lies off a periodic orbit, the descendants of $x$ in its unit component are precisely the unfolded tree: a coincidence across distinct depths would force $x$ periodic, and equal-depth coincidences with different words violate forward determinism. Removing the edge $x\to Tx$ disconnects that descendant tree from its parent. Hence the actual first-parent probability on the ordinary unit component equals $h(x)$. For a good unit $n\ge3$, put $\tau_2(n)=\min\{k:T^kn=2\}$. All pre-terminal vertices are off-cycle. Consequently
$$
 \frac{G(n,2)}{G(2,2)}=\prod_{j=0}^{\tau_2(n)-1}h(T^jn).
$$
The ratio vanishes on all other components. At $1,2$ the ratio is one, and no off-cycle equality for $h(1)$ or $h(2)$ is used.

Bounded harmonic functions on the full undirected graph correspond isometrically, in the supremum norm, to those on its unit graph. On each half-line the harmonic recurrence says the successive increments are constant, hence zero for a bounded function. The attachment equation then reduces to the unit equation. Conversely extend constantly down each half-line. Equivalently excursions into a half-line return to the attachment almost surely and the successive core moves have the unit walk's law.

Each component already has nonconstant bounded harmonic functions. Choose an off-cycle branching unit $v$; such vertices exist arbitrarily far along the unbounded doubling chain in each component. Its two distinct unit children $y,z$ have disjoint transient descendant trees. Let $E$ be the event of eventually staying on the $y$ side of the bridge $y,v$. From $y$ its probability is at least $1-h(y)\ge1/8$. From $v$ there is positive probability to step to $z$ and never return to $v$, so the probability ever to hit $y$ is strictly less than one. The harmonic function $x\mapsto\Pr_x(E)$ therefore has a strictly smaller value at $v$ than at $y$, by the strong Markov identity. In the known basin use $v=8$, $y=5$, $z=16$. This supplies a bounded nonconstant harmonic function entirely inside one verified component. A binary-valued harmonic function on a connected graph is constant by its averaging equation; these two kinds of harmonic rigidity have different implications.

For unit $u,v$ in a component whose underlying *simple* graph is a tree (in particular $G_1\cap U$), let $[u,v]$ be its geodesic. The Green function factors at a separating vertex $c$:
$$
 G(u,v)=G(u,c)G(c,v)/G(c,c)\qquad(c\in[u,v]).
$$
This is the same hitting probability identity; every path from $u$ to $v$ visits $c$. Project each attachment $h'$ to its nearest geodesic vertex $c$. Applying the identity to $u,h'$ and $v,h'$ gives
$$
 \frac{Q(u,v)}{G(u,v)}
 =\sum_{c\in[u,v]}\frac{1}{G(c,c)}
      \sum_{\substack{h'\in H\\{\rm proj}(h')=c}}G(c,h')^2 .
$$
The inner sum is at most $(G^2)(c,c)\le g^{-1}G(c,c)$. For each geodesic vertex choose an attachment at distance at most five. Each chosen attachment serves at most eleven geodesic vertices, since all lie within five positions of its projection. For that projection $c$ one has $G(c,h')\ge3^{-6}$ and $G(c,c)\le g^{-1}$. Writing $d=d(u,v)$ gives the two-sided estimate
$$
 (g3^{-12}/11)(d+1)\ \le\ Q(u,v)/G(u,v)\ \le\ (d+1)/g .
$$

## OP-I3. Ordinary height on every good doubling ray

Let $\mu$ be Haar probability on $\mathbb Z_3^\times$ and put
$$
 \chi=-\int\log h(x)\,d\mu(x),\qquad \beta=\chi/\log2.
$$
Then for $k\ge1$, uniformly in every good unit $u\ge3$,
$$
 \log\frac{G(2^ku,2)}{G(u,2)}=-k\chi+O(k^{1-\alpha}).
$$
The same formula holds for $u=2$ since the preterminal doubled inputs are off-cycle. For $u=1$ start the product at 2. In particular along each such fixed ordinary ray the Green entry is $(2^k)^{-\beta+o(1)}$; the heat coefficient $Q(2^ku,2)$ has the same exponent, by OP-I2. This is an actual height law on explicit families.

Indeed let $F=-\log h$. By $h\ge1/2$ and OP-I1, its oscillation on any unit class modulo $3^r$ is $O(b^r)$. Let $F_r$ be its conditional average on those classes. The differences $F_r-F_{r-1}$ for $r\ge2$ have global mean zero, period dividing $2\cdot3^{r-1}$ along doubling, and supremum norm $O(b^{r-1})$. For $F_1-\chi$ the corresponding period is two and its norm is bounded. Every complete period has sum zero because doubling cycles through all unit classes. For a partial sum of length $k$, each difference up to level $R$ therefore contributes $O(3^r b^{r-1})$. The tail $F-F_R$ contributes $O(k b^R)$. Take $R\ge1$ with $3^R$ comparable to $k$. The geometric sum gives $O(k^{1-\alpha})$, including small $k$ after changing the constant. OP-I2 on the $k$ even edges proves the formula.

The exact finite rational control gives
$$
 0.387648\ \le\ \beta\ \le\ 0.387892 .
$$
Here is the certificate method. Partition into the 1,458 unit classes modulo $3^7$. Start each $h$ interval at $[1/2,7/8]$. The first-parent equation is increasing in each child value. The even child lies in its single doubled class. At a branch the odd child ranges over three lifts modulo $3^7$ of its class modulo $3^6$; use the smallest lower endpoint and largest upper endpoint. Round the new bounds outwards to multiples of $10^{-9}$ and intersect with the previous interval. Induction preserves the enclosure at every iteration. Average the resulting lower and upper values for $-\log h$ using uniform Haar mass, and divide by the corresponding bounds for $\log2$. For rational $1\le v\le2$, the first 16 terms of $2\sum_{j\ge0}x^{2j+1}/(2j+1)$, $x=(v-1)/(v+1)$, give a lower bound for $\log v$; add $2x^{33}/(33(1-x^2))$ for an upper bound. All rounding and the rational series are implemented in [controls.py](controls.py); [the receipt](CONTROLS.json) gives the exact integers. No model of orbit randomness enters the enclosure.

There is a complementary obstruction to a height-only law. For every odd $k\ge1$ choose arbitrarily large good units $n\equiv2^k-1\pmod{2^k3}$ by OP-L1. These have $k$ odd steps, with $T^j n+1=(3/2)^j(n+1)$ for $j\le k$. Taking $n$ large ensures all these vertices exceed 2. Thus $y=T^k n\ge(3/2)^k n$, yet
$$
 G(n,2)/G(y,2)=\prod_{j<k}h(T^j n)\le b^k.
$$
In particular no positive nonincreasing function of ordinary height is comparable, up to fixed constants, to this marked Green value over all known good unit inputs. The doubling-ray exponent and this failure both hold inside the basin of 1. The remaining question is positive anchored communication for every ordinary unit, as distinguished from the diagonal law on each component.

## OP-I4. The exact size of the anchored columns

For positive units put $f(n)=G(n,2)/G(2,2)$. With counting measure on **all** such integers, as $t\downarrow0$,
$$
 \#\{n:f(n)\ge t\}\asymp t^{-1},
 \qquad
 \#\{n:Q(n,2)\ge t\}\asymp t^{-1}\log(1/t).
$$
Both estimates are unconditional, even if there are other components. In particular $f$ belongs to weak $\ell^1$ and to every $\ell^p$, $p>1$, while its $\ell^1$ sum diverges.

The only predecessors of 2 are 1 and 4, and the only predecessor of 1 is 2. Thus every good unit besides 1 and 2 belongs to the full ordinary pruned descendant tree of 4. No other unit contributes to either superlevel set. On this tree $f(y)=h(y)f(x)$ for a child $y$ of $x$. Give each vertex the mass $C(x)f(x)$. OP-I1 gives exact conservation from parent to children. Stop when $f$ first falls strictly below $t<f(4)$. Since $h\le7/8$, the stopped tree is finite. Its terminal vertices have $t/2\le f<t$ using $h\ge1/2$, and $1/7\le C\le1$. Their masses sum to $C(4)f(4)$. The number $m$ of terminal vertices therefore lies between $C(4)f(4)/t$ and $14C(4)f(4)/t$.

The vertices with $f\ge t$ in this rooted tree are exactly the nonterminal vertices. They number at least $m/2$, since each terminal has a parent and each parent has at most two children. To bound them above, contract maximal unary strings. Between successive branching vertices, or a branch and a terminal, there are at most three interior unary vertices; the initial unary string likewise has length at most three. After contraction a binary tree with $m$ terminals has $m-1$ branching vertices and $2m-2$ edges. Thus the original size is $O(m)$, including the case of an initial single string. Adding 1 and 2 leaves the asserted asymptotic order. The membership and nonmembership claims follow by integrating the distribution function.

On the good tree $f(n)$ lies between $2^{-d}$ and $(7/8)^d$ up to constants, where $d=d(n,2)$; for $n\ge3$ use the product formula. The comparison for $Q/G$ in OP-I2 therefore gives uniformly for small $f$
$$
 Q(n,2)\asymp f(n)\log(1/f(n)).
$$
The function $s\log(1/s)$ increases for $0<s<e^{-1}$, and its inverse near zero lies between constant multiples of $t/\log(1/t)$ (substitute such a multiple directly). The already proved count for $f$ gives the second superlevel estimate. This count yields no positive lower bound indexed by ordinary integer height: zero entries from any other component are invisible to positive superlevel sets.
