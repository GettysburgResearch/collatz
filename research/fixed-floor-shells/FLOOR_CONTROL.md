# A prefix-tree control with a power-small floor tail and escape

**FS-021. PROPOSED logical control.** This altered deterministic map
has an escaping component of positive lower natural density, while its
eternal survivor fraction above $B$ is of order $1/B$. Every positive
integer target, including even targets, retains an explicit fast
predecessor coefficient $c/t$. Off $O(\log X)$ odd targets up to $X$,
the squared first-hit pressure is exactly $3/2$. These simultaneous
properties limit arguments using the numerical strength of absolute
density and pressure bounds. The true Collatz odd formula is changed.

Begin with the ordinary rule that halves evens, sends odd $x>1$ to
$x-1$, and sends $1$ to $2$. Its odd map clears the final binary 1
and strips trailing zeros. Hence the odd first-hit ancestors of an odd
$t$ are exactly the odd integers whose binary expansions begin with
the expansion of $t$. At suffix length $l\ge1$ there are $2^{l-1}$
such integers. The affine derivative along their odd path is $2^{-l}$,
as $l$ halving steps remove the suffix and all subtractions have slope
one. The empty path contributes one, so
$H_2(t)=1+\sum_{l\ge1}2^{l-1}2^{-2l}=3/2$.

Order the spine vertices
$$
  2^j+3,\quad 3\cdot2^{j-1}+3\qquad (j\ge5)
$$
by increasing size, and replace the ordinary odd output at each vertex
$m$ by twice the next vertex $m'$. The raw odd output never exceeds
$3m+1$ since $m'/m<3/2$. Keep all even transitions. The spine vertices
have binary words $10^k11$ or $110^k11$ with positive and growing $k$,
so no vertex's word prefixes another's. Every original odd ancestor
of the first vertex still hits it, then escapes. This component has
positive lower natural density. Define the modified odd chart at a
spine vertex to have derivative $m'/m$, for instance by using the
affine map $z\mapsto(m'/m)z$ there. One fixed source then contributes
$(m/m_0)^2$ to $H_2(m)$ along the spine.

An original odd continuation from a spine vertex visits only its
immediate odd parent $(m-1)/2$, then $1$ or $3$, then $1$. A modified
continuation remains on the spine. All first-hit ancestor lists and
derivatives therefore agree with the base map off the spine, these
parents, and $\{1,3\}$. The exceptional set has counting function
$O(1+\log X)$. In particular $F(t)=H_2(t)/t^2=3/(2t^2)$ elsewhere.

**Floor tail.** A survivor above $B\ge1$ must meet the spine, since
every unaltered trajectory reaches 1. Its first such meeting must be
at some $m>B$ via an original path. There are at most $2N/m$ original
odd ancestors of $m$ below $N$, by summing the geometric counts by
suffix length. Including initial even halvings gives at most $4N/m$
ordinary ancestors. The two geometric spine sequences give
$\sum_{m>B}1/m=O(1/B)$. Thus the number of eternal survivors below
$N$ is $O(N/B)$. Conversely select a spine $B<m\ll B$ for large $B$.
Its original odd prefix subtree has lower density $\gg1/m$, meets
no earlier modified vertex, and never visits an odd or even value
below $m$ before or after reaching it. The floor density is bounded
below by a constant times $1/B$ as well.

**All target clocks.** Write an arbitrary positive integer $t=2^v s$
with $s$ odd. Set $a=\max(2,v)$, $w=2^as+1$, and $u=4(16w+1)+1$.
The binary expansion of $u$ ends in the marker $000101$, which occurs
nowhere in a spine word. Every odd source $x$ with prefix $u$ therefore
reaches $u$ in the modified map as usual. Its continuation through
$16w+1$ and $w$ is also unmodified since those vertices end in $01$.
The original edge at $w$ reaches $2^as$ and then visits $t$ and $s$.
If $x$ has suffix length $l$ relative to $w$, the part reaching $w$
takes at most $2l$ raw steps and $l$ odd steps, with
$l\le\log_2(x/w)$. From $w$ the additional costs are at most three
raw steps to $t$ and one odd step to $s$. Since $x\ge64w\ge64t$,
these totals are at most $10.46\log(x/t)$ and $3.4881\log(x/t)$
respectively.

Finally $u\le325t$. If $N\ge8u$, all odd binary extensions of $u$
by exactly $\lfloor\log_2(N/(2u))\rfloor$ bits are strictly below
$N$, giving at least $N/(8u)$ sources. If $N<8u$, then
$\lfloor N/(3000t)\rfloor=0$. Thus at every $N$ there are at least
$\lfloor N/(3000t)\rfloor$ simultaneous timed predecessors. In
particular the stronger floor bound and stronger absolute predecessor
coefficients coexist with pointwise pressure spikes.

[FS-018](SPARSE_PERTURBATION.md) gives a separate sparse modification
of the true Collatz map preserving its exact first-hit laws off a
sparse set. The prefix-tree control above additionally provides the
explicit survivor upper bound, and uses a different underlying odd map.
