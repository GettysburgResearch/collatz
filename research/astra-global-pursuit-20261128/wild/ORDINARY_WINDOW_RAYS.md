# Ordinary predecessors in every sufficiently large translated window

**Proposed written theorem, 28 November 2026.** Fix a positive odd integer
$a$ prime to three, a shortcut parity word $v$ of length $t$, and a
residue $r$ modulo $3^k$, with $k\ge0$. Write $b$ for the odd count
of $v$, $P=2\cdot3^{b+k}$, and $\gamma=\log_2 3$. There is one
explicit two-parameter family of positive integers such that every member

* has the prescribed first $t$ native shortcut parities and is $r\bmod 3^k$,
* subsequently reaches the prescribed ordinary integer $a$, and
* is certified by $O_{a,v,k}(\log (2+n))$ shortcut steps.

For every sufficiently large real $X$, this same family has a member in

$$
                 [X,\,X 2^{6P/q(X)}],                                      \tag{1}
$$

where $q(X)$ is the largest convergent denominator of
$\alpha=(2-\gamma)/P$ no greater than
$K=\lfloor\log_2 X/[8(3P+3)]\rfloor$.
Thus the family meets every interval of length $C_{a,v,k}X/(\log X)^c$
starting at $X$, for some $c>0$. The exact version (1) requires only
irrationality and continued fractions. The uniform power-log form uses a
classical two-logarithm bound. Along an unbounded sequence the width is
$O_{a,v,k}(X/\log X)$. A prescribed binary residue modulo $2^t$
determines $v$, so the congruence conditions can be given in either form.

The guarantee concerns a fixed ordinary target, every window location, and
a sparse explicit certificate family. The widths in (1) exceed known
almost-everywhere counted coalescence block lengths.

## One increasing spine

Use $U(n)=(3n+1)/2^{v_2(3n+1)}$ on positive odd integers and
$I_e(y)=(2^e y-1)/3$ whenever this is an integer.
Set $J=b+k$. Powers of two generate the units modulo every $3^h$.
Indeed $v_3(2^{2m}-1)=1+v_3(m)$ by the binomial theorem or LTE, giving
the full order $2\cdot3^{h-1}$.

First take $x_0=I_e(a)$ with $3\le e\le3P+2$ and
$2^e a\equiv4\bmod3^{J+2}$. At each subsequent step take the unique
$e_i$ in the same interval such that $2^{e_i}x_{i-1}\equiv4\bmod3^{J+2}$,
and put $x_i=I_{e_i}(x_{i-1})$. All these integers are positive odd,
congruent to $1\bmod3^{J+1}$, and $U(x_i)=x_{i-1}$, with $U(x_0)=a$.
Every $e_i$ for $i\ge1$ is $2\bmod P$. The bounds

$$
          (7/3)x_{i-1}\le x_i\le 2^{3P+2}x_{i-1}
$$

ensure strict growth. For $D_i=e_1+\cdots+e_i$, the physical
one-step identity gives

$$
 \log_2 x_i=\log_2 x_0+D_i-i\gamma
       -\sum_{j=1}^i\log_2(1+1/(3x_j)).
$$

The infinite sum converges. With $\theta$ equal to $\log_2 x_0$ minus
that sum, we have

$$
             \log_2 x_i=\theta+i(2-\gamma)+P m_i+O(1/x_i),
                         \qquad m_i\in\mathbb Z.                        \tag{2}
$$

The remainder is the positive tail, bounded by a geometric series. It
is exponentially small in $i$ along this same ordinary spine.

## A freely lifted last edge and a prescribed forward prefix

For the word $v$ write $F_v(n)=(3^b n+C_v)/2^t$. Put

$$
     d=(C_v+3^b r)2^{-t}\pmod{3^J}.
$$

The residue is unrestricted when $J=0$. Choose $s\bmod P$ with
$2^s\equiv3d+1\bmod3^{J+1}$. For every $i$ and every positive
$E\equiv s\bmod P$,

$$
       z=I_E(x_i),\qquad n=(2^t z-C_v)/3^b                              \tag{3}
$$

are integers and $n\equiv r\bmod3^k$. In particular $z$ is odd,
$z\equiv d\bmod3^J$, and $U(z)=x_i$. Retain $n>0$. To check the
prefix, peel the last branch backwards. An even step gives its even
predecessor $2y$. For a last odd step the remaining divisibility
implies $3\mid 2y-1$, so its predecessor $(2y-1)/3$ is odd.
Repeating gives the claimed word and the positive trajectory because
the actual shortcut map preserves positivity. Prescribing a residue
modulo $2^t$ is equivalent to prescribing a parity word, by the usual
binary parity bijection.

Equation (3) gives the real identity

$$
 \log_2 n=\log_2 x_i+E+t-(b+1)\gamma
   +\log_2\!\left(1-\frac{1+3C_v/2^t}{2^E x_i}\right).                 \tag{4}
$$

For $i$ of order $K$ and $E$ of order $\log_2 X$ the last term is
exponentially small in $K$, uniformly across the chosen indices. The
clock is $t+E+D_i+e$, using the original initial lift $e$. It is
$O_{a,v,k}(\log(2+n))$ throughout the retained family because
$i\ll\log(2+x_i)$, $D_i\ll_P i$, and (3) gives $2^E x_i\ll_v n+1$.

## Every window

Take $q=q(X)$ and $K\le i<K+q$. A convergent $p/q$ satisfies
$|\alpha-p/q|<1/q^2$. Thus these $q$ rotation phases form a
$2/q$-net modulo one, by comparison to a translated complete
$q$-grid. In view of (2), choose such an $i$ and then $E\equiv s\bmod P$
so that

$$
 \left|\theta+i(2-\gamma)+P m_i+E+t-(b+1)\gamma
                 -(\log_2 X+3P/q)\right|\le2P/q .
$$

Here $\log_2 x_i<\tfrac12\log_2 X$ for all sufficiently large $X$
at these indices. Consequently the selected $E$ is positive of order
$\log_2 X$. The combined errors in (2) and (4) are eventually
less than $P/(2q)$, since $q\le K$. The inequalities give (1).

For completeness, a classical lower bound for nonzero integer linear
forms $u\log2-v\log3$ gives $|q\alpha-p|\gg_P q^{-M}$ for some
absolute finite $M$ and nearest $p$. Consecutive denominators then
satisfy $q_{j+1}\ll_P q_j^M$. Because $q(X)\le K<q_{j+1}$, this
gives the claimed power-log width. Taking $K=q_j$ on a sequence gives
the stated $X/\log X$ width directly.

## Limit of this certificate family

For fixed $i$, increasing $E$ by $P$ more than doubles a positive
$n$ in (3). An octave $[X,2X)$ contains at most one such member per
$i$. Its admissible indices satisfy $x_i\ll_v X$, and so there are
$O_{a,v,k}(\log X)$ of them. Even after adding the endpoints of the
octave, one subinterval of length $\gg_{a,v,k}X/\log X$ is empty of
this family. The argument gives no empty interval of the complete
predecessor basin. A short-interval proof at a scale $X^{o(1)}$ needs
additional rays or a different mechanism.

Classical sufficiency of every arithmetic progression concerns a meeting
with the orbit of some member. Here the constructed member actually
visits a fixed target, with an all-location real bound and a finite
chronological path. Weaver's first-landing minorant supplies larger
counts in multiplicative-width source windows. The real-ternary
stationary law supplies exact coded integer fibres and a noncycle gap.

[Monks, sufficiency of arithmetic progressions](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf)
· [Weaver, first-landing bounds, §13](https://rstation.ai/problems/collatz/papers/12)
· [Weaver, geometry of the joint affine law, §9](https://rstation.ai/problems/collatz/papers/19)
· [Bondareva, Luchin and Salikhov, two-logarithm bound](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&option_lang=eng&paperid=619&what=fullt).

These analytic statements are written proofs. The finite replay checks
exact lifts, residues, parities and ordinary paths. Historical priority
for the irrational leading-digit rotation mechanism is unassessed.
Universal Collatz convergence remains open.
