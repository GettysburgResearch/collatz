# Arbitrary compact phase sets with record lengths tending to infinity

**Status — PROPOSED symbolic sharpness, with a fixed-source exclusion.**
Let $\alpha=\log_2 3$. Call a nonempty chronological finite gap
word a *no-rise prefix* if $3^j/2^{S_j}<1$ at every positive prefix.
It prescribes a unique odd source class modulo $2^{S_m+1}$ via the
exact parity equation. Let $\mathcal D$ consist of the odd dyadic
points $x$ such that for every $b\ge1$ some no-rise prefix with
$S_m\ge b$ prescribes $x\bmod2^b$. Let $\mathcal R$ be the ternary
critical trace in [the gauge theorem](GAUGE.md). The set $\mathcal D$
is compact: it is the intersection of nested finite unions of the
specified depth-$b$ cylinders. For example $1\in\mathcal D$ by the
constant genuine gap two. Actual starts of first-ladder words whose
lengths tend to infinity have dyadic limit points only in
$\mathcal D$, by omitting the last gap of each long word.

**Theorem E.** For every nonempty compact
$K\subset\mathcal D\times\mathcal R$ there exists one infinite
chronological gap script with all these properties.

* Its true record blocks have lengths tending to infinity. Its
  coefficient $M_i$ tends to infinity through all odd times, and
  $\sum_i M_i^{-t}<\infty$ for every fixed $t>0$.
* For its unique dyadic seed, propagated with its genuine gaps, and
  for any ternary seed propagated by the same affine maps, the
  subsequential limits of their **paired coordinates at the same
  record indices** are exactly $K$.
* The dyadic seed is irrational over $\mathbb Q$. Every finite initial
  gap word can nevertheless be realized by arbitrarily large positive
  ordinary integers with the initial ternary seed simultaneously
  prescribed to any finite precision.

In particular neither a singleton pair of rational phase limits nor
the conjunction of critical record recurrence and real coefficient
escape distinguishes positive ordinary realization in this
infinite-alphabet model. No positive ordinary divergent orbit is
constructed.

## Completing prescribed beginnings and endings

Choose a sequence $(\xi_l,\zeta_l)$ with set of subsequential limits
exactly $K$; for instance concatenate finite $1/j$-nets in $K$. For
each depth $b$ and each of the finitely many dyadic classes of
$\mathcal D$ at that depth, fix a witnessing no-rise word $f$ with
clock at least $b$. Let $F_b$ exceed all their lengths and clocks. For
a given $\zeta\in\mathcal R$, choose a critical backward prefix $v$
of $b$ gaps representing it modulo $3^b$. For every $j\le b$ its
deficit is $\alpha j-S_j(v)\ge\{\alpha j\}>0$.

Put $c_b=\tfrac14\min(\alpha-1,\min_{1\le j\le b}\{\alpha j\})$.
There is a finite $B_b$ such that in every interval of $B_b$
successive integers some $m$ has
$c_b<\{\alpha m\}<2c_b$. This is the bounded-gap visit property of
an irrational circle rotation to a fixed open interval. One proof
covers the compact circle by finitely many backwards translates of
that interval, using density of every forward rotation orbit.

Choose integer depths $b_l\to\infty$ sufficiently slowly that,
eventually,

$$
 b_l+F_{b_l}+B_{b_l}\le l^{1/4},\qquad c_{b_l}\ge l^{-1/4}.
$$

Such a choice follows by assigning to each finite list of depths a
sufficiently late starting index and then taking successive stages.
Start with finitely many gap-one record blocks if necessary. At
record $l$ let $H_l=\log_2 M_{k_l}$; choose a length $m_l$ at least
$\lceil H_l\rceil$ and at most $\lceil H_l\rceil+B_{b_l}$ with
the fractional part just prescribed. Small initial stages can be
delayed and repeated at fixed depth until the following construction
has positive run lengths: at that fixed depth one can always use
larger $m$ with the same fractional-part bounds, and each resulting
record increases $H_l$ by at least the fixed $c_b$.

Take $f$ representing $\xi_l$ and $v$ representing
$\zeta_{l+1}$ at depth $b_l$. Write $p=|f|$, $b=b_l$ and denote their
clocks by $s_f,s_v$. The chronological word is

$$
     w_l=f\ \ 2^{[u]}\ \ 1^{[t]}\ \ {\rm rev}(v),\qquad
     u=\lfloor\alpha m_l\rfloor-m_l-(s_f-p)-(s_v-b),\qquad
     t=m_l-p-b-u.                                                  \tag{E1}
$$

Here superscript brackets mean a repeated gap letter. The total
clock is $\lfloor\alpha m_l\rfloor$ and the terminal log multiplier
is $h_l=\{\alpha m_l\}$. Every proper prefix of the prescribed
beginning is below the starting coefficient, including its end.
The subsequent run of twos lowers the coefficient. The following
run of ones increases it, with its endpoint still below the start:
its logarithmic multiplier is $h_l-(\alpha b-s_v)<0$. At every
remaining interior position the suffix budget gives the same
inequality with a shorter nonempty prefix of $v$. Thus the end is
exactly the next strict record.

For clarity the choices can be made without a circular induction.
At each $l$ for which (E1) would give $u<1$ or $t<1$, increase $m_l$
within the syndetic set until both are positive. This is always
possible, since with $f,v$ fixed their asymptotic proportions are
$\alpha-1$ and $2-\alpha$. All steps give $H_{l+1}-H_l=h_l$.
Consequently $H_l\ge c l^{3/4}$ eventually and $H_l=O(l)$.
The prescribed clocks and gaps $F_b,b,B_b$ are $o(H_l)$. Therefore
the preliminary increase is no longer needed at large $l$, and

$$
 m_l=H_l+o(H_l),\quad
 u=(\alpha-1)H_l+o(H_l),\quad t=(2-\alpha)H_l+o(H_l).
$$

Inside $f$ the logarithmic dip is at most $s_f$. The following twos
cost a further $(2-\alpha)u$. The ones then increase the coefficient,
and the final prescribed suffix stays above $-(\alpha-1)b$ in local
logarithmic coordinates by its suffix formula. Since
$(2-\alpha)(\alpha-1)\le1/4$, all global log multipliers in the
block are at least $H_l/2$ eventually. Its length is $O(H_l)$.
This proves the claimed real escape and summability.

## The coordinates and the obstruction at a fixed seed

The infinite word prescribes a unique dyadic seed by nested exact
odd-parity cylinders, with clocks tending to infinity. At record $l$
its dyadic coordinate agrees with $\xi_l$ modulo $2^{b_l}$ by the
initial word $f$. At the next record its ternary coordinate agrees
with $\zeta_{l+1}$ modulo $3^{b_l}$ by the last $b_l$ gaps,
independently of all earlier ternary coordinates. Thus both
coordinates at record $l$ approximate their indicated pair, with
precisions tending to infinity. This proves the exact cluster
statement. Given a finite initial script and any coordinate
$z_0\bmod3^a$, the canonical odd source class modulo $2^{S+1}$ and
the chosen ternary source class have arbitrarily large simultaneous
ordinary representatives by CRT. Their forward gaps and record
comparisons are exact on that finite prefix.

Suppose the unique dyadic seed were rational $a/d$, $d>0$ odd.
Then its genuine gap images have integral numerators over this fixed
denominator; no step reaches zero since the infinite word has finite
positive gaps. As real numbers their values are

$$
          x_i=M_i\left(a/d+\frac13\sum_{j<i}M_j^{-1}\right).
$$

The sum is bounded. At the end of $f$ in block $l$, the local
multiplier is below one, so $|x_i|\le C2^{H_l}$. Along $u$ genuine
twos, $x_{i+u}-1=(3/4)^u(x_i-1)$, whence
$4^u\mid d(x_i-1)$. The integer on the right is nonzero: if $x_i=1$,
its subsequent genuine gaps would all equal two, but this block
contains ones. Hence $4^u\le C_d(1+2^{H_l})$. This fails since
$2u/H_l\to2(\alpha-1)>1$. This proves irrationality of the one
supplied dyadic seed and explains exactly why its changing finite
ordinary witnesses cannot be stabilized.

A simpler special case for $K=\{(1,-1)\}$ uses only the individual
gap letters one and two. Choose $m_l=l+O(1)$ with
$3/8<\{\alpha m_l\}<1/2$; again the return gaps of the rotation
to this fixed interval are bounded. Set
$u_l=\lfloor\alpha m_l\rfloor-m_l$,
$t_l=m_l-u_l$, and take $2^{[u_l]}1^{[t_l]}$.
These are first-ladder words since $1/2<\alpha-1$. The within-block
minimum logarithm is at least
$(3/8)l-(2-\alpha)(\alpha-1)l-O(1)\ge l/8-O(1)$, while the
starting record logarithm is at most $l/2+O(1)$. The initial twos
force dyadic closeness to $1$ and the final ones force ternary
closeness to $-1$. The preceding divisibility argument again rules
out every fixed rational dyadic seed.
