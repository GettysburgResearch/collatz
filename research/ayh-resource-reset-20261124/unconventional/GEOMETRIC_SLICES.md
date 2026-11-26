# Uniform ordinary coverage on every geometric sequence

**Written theorem.** There is an absolute $C$ such that for every integer
base $b\ge0$, every $N\ge2$, and every interval of $N$ consecutive
nonnegative **exponents** $n$, all but at most $CN/\sqrt{\log(2N)}$ of its
members have the following property. At the original e6 parameter $m=b^n$
(with $0^0=1$), either $m=0$, or the ordinary peak
$P_j=3^j-1$, $j=11+162m$, meets an earlier peak $P_{j-d}$ at a common
postpeak clock, for some $d\in\{40,42,63\}$. For $m=1$ use $d=42$.
Consequently none of the selected original parents is a least reverse
defect. The constant is independent of the base and the interval's
location. The full slice estimate is a written consequence of the
affine two-arm absorption estimate in the cited repository source.
The positive single-band and perfect-power theorems, the ordinary
two-arm coordinates there, and the dyadic scaling law have separate
kernel proofs. The negative terminal now has a kernel-checked ordinary trace as well.

The exceptional count is for each base separately. In particular, choosing
a different base at every exponent does not produce a common exceptional
set. The individual parameters outside the selected cases remain open.

## Arithmetic used for transferring the count

The published-in-repository affine estimate says that for fixed $s,D$, the
fraction of binary residues $x\bmod2^h$ on which the forms
$x,3^s x+D$ have failed to acquire equal profiles by clock $h$ is
$O_{s,D}(1/\sqrt h)$. Equal profiles mean that ordinary endpoints and
total powers of three agree as functions of the unexposed digits. A form
with an arbitrary positive ordinary lift therefore gives a real physical
merger. Here $s\le71$ and $|D|\le2\cdot3^{71}$. We use only this
fixed-size special case. [Oriented affine absorption estimate at pinned
commit](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md#reaching-a-small-normalized-offset)

Suppose a parameter $t$ on a fixed residue class parametrizes $x\bmod2^h$
with period $2^{h-c}$ and no repetitions in that period for $h>c$.
Taking $h=\lfloor\log_2 N\rfloor$, a consecutive interval of at most $N$
values of $t$ needs at most $2^{c+1}+1$ such periods. Hence it contains
$O(2^cN/\sqrt{\log(2N)})$ failures. Use the trivial bound for $h\le c$.
It suffices that $c$ be bounded by an absolute constant. When a formula
holds only after an initial $O(h+1)$ values of $n$, the discarded members
contribute $O(h+1)$ even for an interval starting at zero.

For $L\equiv1\pmod4$, $L>1$, and $v_2(L-1)=c$, we use
$v_2(L^{u+t}-L^u)=c+v_2(t)$ for $t>0$. This follows by squaring
$L^{2^a}=1+2^{a+c}(\text{odd})$ and then taking an odd multiple of
the exponent. Thus the parameter has exactly the above period and injection
after an odd multiplier and a translation. For $L\equiv3\pmod8$ split
the exponent into its two parities and use $v_2(L^2-1)=3$.
In particular $v_2(3^{162t}-1)=3+v_2(t)$.
[Exact finite dyadic precision](DyadicPowerPrecision.lean)

## The negative unit at the zero anchor

Let $A=3^{162}$ and $B_k=((A^{2^k}-1)/2^{k+3})$. The $B_k$
stabilize modulo every $2^h$. Write $B$ for these compatible residues.
For $m=4^r v$, set $u=(A^m-1)/2^{2r+3}$. When $2r\ge h$,
$u\equiv vB\pmod{2^h}$ by one binomial expansion. For $r\ge58$ the
unconditional ordinary coordinates of $P_j,P_{j-63}$ at clock $2r+3$
are $1+3^{71}U,1+U$, where $U=3^{r-58}u$.
When $3^r v\equiv1\pmod{2^{2957}}$ and $2r\ge2955$,
the positive certificate joins these peaks after 2957 additional clocks.
[Kernel-checked gate and positive band](LogTower.lean)
[All finite derivative precisions](LogTowerCore.lean)

For the opposite sign use $P_{j-40}$. The signed rational anchor
$3^{-29}-1$ reaches one in 62 steps with 34 odd inputs. For the actual
positive lower peak, its state at clock 62 is therefore
$1+2^{2r-59}3^5u$. Taking $r-30$ two-step laps at one leaves
$1+2\cdot3^{r-25}u$, then one odd step gives $2+3^{r-24}u$ at clock
$2r+3$. The actual upper state at this clock is $1+3^{r+13}u$.
Set $V=3^{r-24}u$. Their states are $1+3^{37}V,2+V$.

Take $H_-=334711$ and the least residue
$V_*=-3^{-24}B\pmod{2^{H_-}}$. At this integer the two states first
have matching endpoints and compensated grades at clock $334711$.
The upper has 167282 odd inputs and the lower has 167319.
Thus the merger lifts to every positive $V\equiv V_*\pmod{2^{H_-}}$.
In particular when $2r\ge H_-$ and $3^r v\equiv-1\pmod{2^{H_-}}$,
the original positive peaks with gap 40 meet. The ordinary negative terminal is kernel-checked in 164 small blocks.
The identification of its explicit integer with the stabilized negative
derivative uses the written argument below and two independent exact
integer replays. [Ordinary negative terminal](NegativeProfile.lean)
[Formal lift and reconstruction](SegmentTrace.lean)
[Exact residue and block replay](check_geometric.py)

For the latter formula, write $L=\lim_s((1-4)^{2^s}-1)/2^s$ in finite
binary residues. The binomial expansion gives terms
$(-4)^i\binom{2^s-1}{i-1}/i$. For fixed $i$ the binomial coefficient
approaches $(-1)^{i-1}$ by its product formula. Each summand has 2-adic
valuation at least $2i-v_2(i)$ uniformly in $s$, so the limit may be
taken termwise at every finite precision. Raising the base to 162
multiplies this first-order limit by 162, whence
$$
                     -B=81\sum_{i\ge1}4^{i-1}/i .
$$
At $H_-$ the terms with $i>(H_-+80)/2+1$ all vanish. For
$i\le2H_-$ use $v_2(i)\le20$, and beyond this range use
$v_2(i)\le i$. The rational sum has odd denominator after reduction.
The replay uses binary splitting, modular inversion, and ordinary
shortcut-word evaluation. The independently implemented squaring
recurrence gives the same first clock and grades.

## Odd bases

The bases zero and one give the already certified $m=0,1$. Fix an odd
$b\ge3$, split $n=2t+\eta$, and put $L=b^2$,
$c=v_2(L-1)$. If $c\le1144$, take
$x=P_{j-42}$ and the companion $3^{42}x+(3^{42}-1)=P_j$.
For two parameters $t,t'$ in this parity class,
$$
 v_2(x(t')-x(t))=3+c+v_2(t'-t)\qquad(t'>t).
$$
The previous period argument applies with an absolute loss.

If $c>1144$ then exactly one of $b-1,b+1$ has valuation $c-1$.
For even $n$, or when it is $b-1$, one has
$m\equiv1\pmod{2^{1141}}$. The positive clock-1143 merger with gap 42
applies to every such $n$. For the remaining odd $n$, write
$p=v_2(b+1)=c-1$ and $m+1=2^pv$. This $p$ is independent of $t$.
Take the signed anchors at $m=-1$. The upper $3^{-151}-1$
reaches one at clock 327 with 151 odd inputs, and the lower
$3^{-191}-1$ reaches one at clock 389 with 191 odd inputs.
At common clock 389 their augmented grades are 31 and 0.

Set $u=(A^{m+1}-1)/2^{p+3}$, let
$\epsilon=(p+3-389)\bmod2$, and $l=(p+3-389-\epsilon)/2$.
Lifting the anchor words, then taking $l$ laps, gives ordinary
$x=1+2^\epsilon3^l u$ and $1+3^{31}(x-1)$ from $P_{j-40}$ and $P_j$.
The input map is now uniformly nondegenerate even for arbitrarily large
$p$. Indeed for $t'>t$,
$$
 v_2(u(t')-u(t))=c-p+v_2(t'-t)=1+v_2(t'-t).
$$
So the scale loss for $x$ is at most two binary digits; the waiting
clock $389+2l$ may depend on the actual base. This proves the assertion
on all odd bases without putting a bound on $b$.

## Even bases

Let $b=2^a c$ with $a\ge1$ and $c$ odd; split
$n=2t+\eta$. Put $s=an$, $r=\lfloor s/2\rfloor$,
$\epsilon=s-2r$, $v=2^\epsilon c^n$, so $m=4^r v$.
Use $h=\lfloor\log_2 N\rfloor$. After discarding the initial
$O(h+H_-)$ terms, $2r\ge\max(h,H_-)$ and $r\ge58$. At the positive
gate the lower state $x=1+3^{r-58}u$ satisfies, modulo $2^h$,
$$
 x\equiv1+2^\epsilon B\,3^{\lfloor a\eta/2\rfloor-58}
                   c^\eta (3^a c^2)^t .
$$
Negative powers of three here mean units modulo $2^h$. If $a$ is odd,
$3^a c^2\equiv3\pmod8$. Splitting $t$ by parity gives period scale
at most four. If $a$ is even, write $D=3^{a/2}c>1$; the rotation is
$D^2$. When $v_2(D^2-1)\le H_-+2$, the period has an absolute
scale bound $H_-+3$. The affine companion in each case is
$1+3^{71}(x-1)$.

Finally, if $v_2(D^2-1)>H_-+2$, then
$D\equiv1$ or $-1\pmod{2^{H_-}}$, since one of $D-1,D+1$ has
valuation one. Here $s$ is even, $3^r v=D^n$ and the applicable sign
is fixed by $D$ and the parity of $n$. The positive or negative terminal
already verified gives an ordinary meeting on the entire class.
All branches have either a supplied physical merger, or a uniform
finite-period count on the actual exponent interval. The earlier source
$M_{j-d}$ is positive and satisfies $2^{40}M_{j-d}<z$ for
$d\in\{40,42,63\}$ whenever its branch applies. The original
least-parent conclusion follows.
