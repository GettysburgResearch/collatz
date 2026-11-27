# Arbitrarily many prescribed earlier parents merge in every parameter progression

**PROPOSED written theorem and a complete obstruction to its fixed-index
extension.** Fix a finite set of nonnegative offsets $F$ containing zero.
In *every* prescribed arithmetic progression of the original parameter
$m$, there is a subprogression on which all parents $Z_{m-i}$, $i\in F$,
have an actual common endpoint on their lower arms. Each has its own certified upper
hit at one. All sufficiently large members of the subprogression work.
Nevertheless infinitely many actual indices have no merger to an earlier
parent of the particular synchronized, grade-compensated post-peak form
constructed here, even at unbounded clocks.

Use the shortcut map $T$, let $j_m=11+162m$, and set
$Z_m=(2^{j_m+7}-271)/81$. As in [the arithmetic packet](../arithmetic/README.md),
the lower arm reaches $x_m=3^{j_m}-1$ after $7+j_m$ steps and the
upper $3Z_m$ first reaches one after $7+j_m$ steps. The two arms
take different physical words. A reference to a post-peak clock below
always starts the clock at $x_m$.

## An effective subprogression for any finite comparison

Let $J=\max F$. Factor a prescribed modulus as $2^v d$ with $d$ odd,
and fix the prescribed residue $m_0$. Select a nonnegative representative
$m_*\ge J$ of that residue. For $m\ge J$ put
$$
 n_m=3^{11+162(m-J)},\quad s_i=162(J-i),\quad x_{m-i}=3^{s_i}n_m-1.
$$
All $n_m$ are $3\bmod8$. Write $B=3^{162}$. Its power orbit
through $n_{m_*}$ is **the entire** $3\bmod8$ cylinder at every
finite precision: $\nu_2(B^t-1)=3+\nu_2(t)$ for $t>0$, by odd
factorization and successive squaring of a number $1\bmod8$.
Hence modulo $2^H$ for $H\ge3$, $B$ has order $2^{H-3}$ and runs
through every unit $1\bmod8$. In particular
$$
 n_m=n_{m_*}\bmod2^{v+3}\quad\Longleftrightarrow\quad
 m=m_*\bmod2^v\qquad(m,m_*\ge J).
$$
The sign of $m-m_*$ is immaterial, by comparing the larger index
to the smaller. This uses ordinary nonnegative exponents throughout.

Set $h_0=v+3$ and fix the indicated first $h_0$ bits of the free
parameter $n$. For any chosen further prefix $n=r+2^h w$,
$0\le r<2^h$, the $i$th physical post-peak form is
$$
                3^{s_i+p_i}w+B_i,\qquad
 B_i=T^h(3^{s_i}r-1),\quad p_i=P_h(3^{s_i}r-1),
$$
where $P_h$ is the actual number of odd inputs. Indeed the initial
free slope is $3^{s_i}$, and each odd step multiplies the remaining
free coefficient by three. Our prescribed $r=3\bmod8$ is at least
three, so all canonical starting points are positive. The augmented
grade is $s_i+p_i$. Its difference between two branches is an
ordinary integer. Their relation, after ordering the grades, is
exactly $Y=3^\sigma X+D$ with $D$ a signed integer. The coefficient
of $w$ in $X$ is odd.

Apply the deterministic two-form procedure in
[the steering proof](STEERING.md#a-deterministic-merger-of-any-two-current-forms).
It fixes more bits of this **one** $n$, gives the selected two forms
identical augmented grades and endpoints, and preserves the prescribed
prefix and each earlier equality. Repeating at most $|F|-1$ times
gives a single residue $r_F\bmod2^H$ with one common endpoint form
on all the arms. No compression estimate, probabilistic absorption,
renewal floor or precomputed tower grade menu is needed here.

The procedure terminates effectively at
$$
                    H\le C^{|F|}(v+162J+4)
$$
after enlarging an absolute $C$. At starting clock $h$ the grade
difference is at most $162J+h$, so dropping the grade takes at most
$4(162J+h)$ extra bits. At the resulting clock $t$,
$B_i+1\le(3/2)^t(3^{162J}2^t+1)$, since the canonical parameter
is less than $2^t$. A remaining equal-grade disparity has logarithm
$O(t+162J+1)$, which bounds the additional bits by the deterministic
contraction proof. Thus each merge multiplies $h+162J+1$ by at most
an absolute constant. Gates in huge residue classes can be specified
by modular powers and finite binary words; no efficiency in the
binary size of $J$ or in the eventual ordinary heights is asserted.

As $r_F$ extends the chosen $h_0$ bits, the power orbit gives one
class $m\bmod2^{H-3}$ mapping to it, entirely inside the prescribed
$m\bmod2^v$. CRT with the original $m\bmod d$ is possible, furnishing
one class modulo $d\,2^{H-3}$. For each $m\ge J$ in this class all
actual $n_m$ are nonnegative lifts of the same physical row, and
all original parents reach the common ordinary endpoint at clocks
$$
                      7+j_{m-i}+H\qquad(i\in F).
$$
The endpoint can vary with $m$. The times differ by $162(i'-i)$
for two original parents. If $F=\{0,\ldots,J\}$, a single such $m$
works simultaneously with **every one** of the $J$ specified smaller
parents. In particular no arithmetic progression can consist entirely
of failures for a fixed finite comparison. The explicit three-parent
classes in the arithmetic packet supply much more specific clocks,
residues and densities for their chosen offsets.

**A growing number of simultaneous comparisons in every ordinary
interval.** For $N\to\infty$, put $J=\lfloor c\log\log N\rfloor$
with $c>0$ so small that $c\log C<1$. Take $F=\{0,\ldots,J\}$
and $v=0,d=1$. The bound above gives
$H=O((\log N)^{c\log C}\log\log N)=o(\log N)$. Every interval
of $N$ consecutive ordinary indices $m\ge J$ therefore contains
at least $\lfloor N/2^{H-3}\rfloor=N^{1-o(1)}$ indices where all
the previous $J$ lower arms and the supplied one have a common
endpoint. This is a lower count, with its exponent uniform in the
interval location. It does not say that the fraction tends to one.
For sets $F$ of bounded cardinality the same conclusion holds for
arbitrary prescribed offsets with $\max F=o(\log N)$.

## Every actual augmented class is finite

On the nonnegative indices define $m\sim l$ if, at some common
post-peak clock $h$, both endpoints and both augmented grades agree:
$$
 T^h x_m=T^h x_l,\qquad j_m+P_h(x_m)=j_l+P_h(x_l).
$$
These equalities persist for any further common time, which proves
transitivity by advancing both witnesses to their larger time.
They hold in the preceding construction since
$j_{m-i}=s_i+j_{m-J}$. We now reconstruct the finite-class argument
of [round twelve](../../round12/arithmetic/README.md) with the
**shifted height** $y+1$. With ordinary positive source $x$ put
$$
 D'_h(x)=\frac{2^h(T^h x+1)}{3^{P_h(x)}(x+1)}
        =\prod_{\substack{0\le j<h\\T^j x\ {\rm even}}}
                         \left(1+\frac1{T^j x+1}\right).
$$
For odd $y$ the shifted update is $3(y+1)/2$; for even $y$ it is
$(y+2)/2$. The uniform elementary simple-path reciprocal bound in
round twelve, for **all** physical sites, gives
$\sum_{y\ge M}1/y\le480M^{-1/80}$ on any positive simple departed
prefix. This controls the logarithm of the new product and its
tail, despite the interchange of the marked parity.

Fix a class reference $x_l$ with a non-eventually-periodic forward orbit.
All its class members have nonperiodic orbits. For $m\ne l$ the
meeting clock $h$ is positive and $D'_h(x_m)=D'_h(x_l)$ by the two
equalities and $x_m+1=3^{j_m}$ for every index $m$.
The reference is even, so $D'_h(x_l)\ge1+1/(x_l+1)$. Choose a
fixed $M$ with $480M^{-1/80}<\log(1+1/(x_l+1))$. Each such
source must visit an even gate $y<M$ before its meeting. If two
class members visit the same gate at clocks $i,i'$ and have a
common endpoint at equal clock $t$, then
$T^{t+i'}y=T^{t+i}y$, by advancing that common endpoint by $i+i'$.
Nonperiodicity gives $i=i'$. Each fixed gate and fixed time has
finitely many positive ancestors since $2T(z)\ge z$. Thus the class
is finite.

If the reference is eventually periodic, choose one phase $z$ on its
positive cycle, with least period $\ell$ and $q=P_\ell(z)$. The cycle
contains an even site: if every site were odd then $T(y)+1=3(y+1)/2$
would increase strictly at every step. Hence
$2^\ell/3^q=D'_\ell(z)>1$. Every class member visits $z$. At its
first such clock $h$, put $p=P_h(x_m)$. The integer
$I=\ell(j_m+p)-qh$ is the same across the class: after a common
augmented meeting advance to a shared visit at $z$ later than both
first visits. Adding a whole number of cycle laps from each first
visit preserves this expression. The departure prefix up to the
first visit at $z$ is simple (a repetition would already traverse
the cycle containing $z$). Therefore
$$
 I=(\ell-q\log_2 3)(j_m+p)
     +q\log_2(z+1)-q\log_2 D'_h(x_m),\qquad \log D'_h(x_m)\le480 .
$$
The leading coefficient is positive and the other terms are bounded
on the class. This bounds $j_m$, hence $m$.

There are consequently infinitely many distinct finite classes,
and infinitely many ordinary class-minimum indices $m$. At every
positive minimum, **no** earlier $x_l$ meets $x_m$ at a common
post-peak clock with augmented grade paid. The subprogressions
nevertheless furnish classes of unbounded finite size. This proves
a genuine pointwise failure of the proposed merger architecture.
It identifies no divergent orbit and excludes no meetings at
unequal post-peak clocks or with unmatched augmented grades.
