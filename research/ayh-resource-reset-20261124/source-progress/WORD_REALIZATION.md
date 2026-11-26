# Exact upper ranks and arbitrary ordinary words after the Mersenne ascent

**Theorem WR-1.** Use the positive shortcut map $T$, with
$T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Fix an
integer $q\ge2$ and any finite binary word $W$ of length $h$, including
the empty word. There is an effectively determined integer $s=s(q,W)$,
$1\le s\le h+1$, with this property. For **every** $r\ge3+s$ there
are arbitrarily large positive $z\equiv17\pmod{48}$ such that

1. the triple $3z$ first hits 1 on a certificate with exactly $r$ odd inputs,
2. $81z+271=2^{q+7}t$ for a positive odd $t$,
3. $T^7 z=2^q t-1$, and the next $q$ inputs are odd,
4. the ordinary inputs starting at $T^{q+8}z=(3^q t-1)/2$ have parity word $W$.

Moreover every sufficiently large member of this same $q,W$ family
whose triple converges has first-hit upper rank at least $3+s$.
Thus the cofinal spectrum of first-hit ranks within this family is the
whole integer interval $[3+s,\infty)$.

### The two ordinary arms

The congruence $2^{q+7}t\equiv 271+17\cdot81\pmod{243}$ specifies one
unit class of $t$ modulo 243. Take $t$ odd in this class and large.
Then $z=(2^{q+7}t-271)/81$ is positive, congruent to 2 modulo 3 and to
1 modulo 16, hence to 17 modulo 48. Also $z=128u+33$.
The first seven lower steps, as affine expressions in $u$, have successive
values
$$
192u+50,\;96u+25,\;144u+38,\;72u+19,\;108u+29,\;162u+44,\;81u+22 .
$$
The last is $2^qt-1$. For $0\le i\le q$ the next values are
$3^i2^{q-i}t-1$, so the following even input reaches
$U=(3^qt-1)/2$. For the triple, the first two odd steps give
$$
(27z+5)/4=64w,\qquad w=(2^{q-1}t-1)/3.
$$
Here $w$ is an odd integer. Six halvings, an odd step, and $q-2$
halvings reach $t$. These $q+7$ upper steps use exactly three odd
inputs.

### Choosing the post-ascent word and its exact upper rank

A length-$h$ shortcut parity word specifies precisely one residue
$u_W\pmod{2^h}$. For completeness, after fixing $i$ initial bits
the possible ordinary sources are $2^i k+a$, with current value
$3^p k+b$ for the $p$ odd steps taken. Its slope is odd, so the next
bit fixes precisely one parity of $k$. This proves existence and
uniqueness by induction, including words with all bits equal.

The condition $U\equiv u_W\pmod{2^h}$ therefore fixes one residue
$$
t\equiv 3^{-q}(2u_W+1)\pmod{2^{h+1}}.
$$
It is odd. Let $P$ be the $h+1$ forced bits of $t$ and let $s$
be their number of ones. For any prescribed $r\ge3+s$, append
$R=r-3-s$ ones to $P$, giving a word of length $d=h+1+R$ and
weight $v=s+R$. Let $B$ be its complete affine constant, so
$$
2^d T^d(t)=3^v t+B .
$$
The recurrence starts at zero and replaces $B_i$ by
$3^{\epsilon_i}B_i+\epsilon_i2^i$. Its last odd input gives
$B\not\equiv0\pmod3$, since $v\ge1$ and subsequent even inputs leave
the constant fixed.

Write $c$ for the required class of $t$ modulo 243. Choose arbitrarily
large $E$ such that
$$
 2^{E+d}\equiv B+3^v c\pmod {3^{v+5}}.
$$
This is possible because 2 generates the units modulo $3^m$ for each
$m\ge1$. Indeed $4^{3^j}=1+3^{j+1}u_j$ with $u_j\equiv1\pmod3$
by cubing, so 4 has exact order $3^{m-1}$ modulo $3^m$, and 2 has
order $2\cdot3^{m-1}$. The residue on the right is a unit. Set
$$
t=(2^{E+d}-B)/3^v .
$$
It lies in the required class modulo 243. Modulo $2^d$, it lies in the
unique class for the prescribed word since $3^v$ is odd and
$3^vt+B\equiv0\pmod{2^d}$. Thus its actual endpoint is $2^E$.
The $E$ remaining steps are halvings. Taking $E\ge2$ ensures this
endpoint exceeds 2, so no earlier point can have reached 1, whose
forward orbit stays in $\{1,2\}$. The first hit has exactly $3+v=r$
odd inputs. Distinct sufficiently large exponents give distinct ordinary
sources. Conversely, for fixed $q,W$ and sufficiently large $t$, the
triple cannot reach 1 through the initial $q+7+h+1$ clocks: during
the $P$ segment its value is at least $t/2^{h+1}$, and each earlier
upper vertex grows with $t$. Its first-hit rank must therefore include
all $3+s$ forced odd inputs.

### An unconditional positive descent through the expanding segment (WR-2)

Choose $W=0^h$ with $h=q+40$. The endpoint after those $h$ steps is
the positive integer
$$
n=T^{q+8+h}z=(3^q t-1)/2^{h+1}.
$$
The residue gives $z\ge17$, so $128z>81z+271=128\cdot2^q t$.
As $3^q\le4^q$ and $h=q+40$, $2^{40}n<2^qt<z$.
This establishes the second alternative of SourceProgress on the
constructed infinite families, with basin equivalence by ordinary
iteration. For each fixed $q$, it supplies arbitrarily large sources
at **every** rank at or above its explicit threshold. The number of forced
expanding odd steps on the lower arm, $q$, is independently unbounded.
No convergence assumption on the lower endpoint enters the construction.

**Theorem WR-3 (dense positive descent).** Fix $q\ge2$, a word $W$ of
length $a$, any desired first-hit upper rank $r\ge q+44+2a$, and any
size bound $L$. There is a source $z\ge L$ with this exact rank whose
lower arm has precisely the prescribed word at clock $q+8$ and then
makes a native descent below $z/2^{40}$. For a construction, apply
WR-1 to the concatenation of $W$ and $q+40+a$ zeros. Its total length
is $q+40+2a$, so $3+s\le q+44+2a$. Each of the first $a$ steps
multiplies a positive input by at most two; the extra $a$ final
halvings pay for all of them. If $U=T^{q+8}z$, the resulting endpoint
$n=T^{2q+48+2a}z$ satisfies $2^{q+40}n\le U$ and
$2U+1=3^qt$, giving the same strict comparison as WR-2.
The same descent holds pointwise for *every* source in the prescribed
arm with these final halvings, independently of whether its triple
reaches 1. In particular, the positive progressing members occur in
every finite post-ascent parity cylinder.

The original $t=1$ rank-three progression has $q=11+162m$, always odd.
Thus $3^q$ is 3 modulo 4 and its post-ascent $U$ is odd. The immediate
all-even test WR-2 does not remove any member of this original family.

Taking $W=1^h$ instead realizes an arbitrarily long second expanding
segment at the same fixed $q$, despite an ordinary convergence
certificate on the upper arm. WR-1 precludes a universal finite
post-ascent forbidden word using only this upper-hit information and an
arbitrarily high exact rank. It does not constrain all the upper ranks
when $q,W$ vary simultaneously below their thresholds. These are existence
and local descent statements. A putative least reverse defect could have an
upper certificate outside the constructed converging endpoints or have a
different lower word. The unrestricted HigherRankProgress remains open.

### Source boundary

PR 197 at `b27a6fe31a487adf5615e173329ad009b975a3cd`,
`research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean`,
establishes the original $t=1$ three-odd family and its prefix bound.
The same head's `FinalProofProposal.lean` defines SourceProgress and
HigherRankProgress. PR 146 at `f431078244e868dc699fad011044f0d5e7f76437`,
`research/upper-bit-mergers/RANK_THREE_MERSENNE.md`, uses a different pair
of arms, $x,2x-1$, with a variable terminal target. WR-1 concerns
$z,3z$ in the required residue and fixes the post-ascent lower word and
the *first-hit* upper odd rank simultaneously.

### Formal scope and replay

In dependency order, compile `TernaryPowerLift.lean`, `WordRank.lean`,
`OrdinaryWordRealization.lean` and `PositiveWordDescent.lean`, with
the pinned ordinary `ReverseBasin.olean` on the Lean path. The
constructive inclusion in WR-1, both exact ordinary arms, the first-hit
rank, the pointwise tests WR-2 and WR-3, and the cofinal exact-rank
WR-2 and WR-3 families are kernel theorems. The converse showing
sharpness of the cofinal rank interval is the written argument above.
The axiom audit of the public realization and descent theorems reports
only `propext`, `Classical.choice` and `Quot.sound`.

Run `python -B check_word_realization.py` or its optimized counterpart.
The checker solves the exact congruences directly from each word and
its complete affine constant, independently of the Lean progression
construction. It distinguishes literal complete first-hit replays
from symbolic large-exponent constructions.
