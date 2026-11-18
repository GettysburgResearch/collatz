# Controlled first landing from a prescribed growing source cylinder

**PROPOSED, source-qualified.** Let $U(n)=(3n+1)/2^{v_2(3n+1)}$
on positive odd integers. Fix any odd ternary unit $b\le M$, $M\ge1$,
any list $w=(a_1,\dots,a_L)$ of positive forward valuations with total
$A$ (the empty list is allowed), and any class $r$ modulo $3^k$,
$k\ge0$. There are absolute positive constants $c,C$ such that, when
$$
             X\ge C M\exp(C(A+k+1)),
$$
at least
$$
                 c\,\frac X M\,2^{-A}3^{-k}                           \tag{1}
$$
odd $n\in[X/4,X]$ simultaneously satisfy the following conditions.

* Their initial $L$ valuations are exactly $w$, and $n\equiv r\pmod{3^k}$.
* Their first odd entry at or below $M$ is exactly $b$. It occurs
  within $C\log(X/M)$ odd steps.
* The sum of $\log(1+1/(3u))$ on the odd inputs before that entry
  is between $c/M$ and $C/M$.

The factor $2^{-A}3^{-k}$ is the normalized odd source Haar measure of
the cylinder, including the case of a nonunit $r$. The threshold admits a
small absolute constant times $\log(X/M)$ digits. [Paper 12, Theorem 14](https://rstation.ai/problems/collatz/papers/12/v1)
already gives the first-landing conclusion with no source congruences;
its proof controls the residue. Fixed arithmetic progression and clock
laws are also [prior](../profinite-orbit-averages/CLOCK_CHARACTERS.md).
[Previously routed large-trace examples](ORDINARY_PHASE_AVOIDANCE.md)
also prescribe a subsequent positive basin using existence of modular
words. The lower count (1) retains a uniform fraction of the source
cylinder scale and specifies the first low value and its distortion.
The additional ingredient for these varying source constraints is
[paper 48, Lemma 7 and (76)](https://rstation.ai/problems/collatz/papers/48/v2).
Only a one-sided count is asserted.

## Bounded-offset bridges on a fixed total

Write $f_a(x)=(3x+1)/2^a$. For a bridge of $q$ letters its forward
map is $x\mapsto Jx+\beta$, $J=3^q2^{-S}$, with total $S$.
There are absolute $B_0,d,c_0>0$ such that at any unit target $s$,
for every prescribed terminal inverse class $u$ modulo $3^h$, every
large $q$ with $h\le d(q-1)$ and $|S-2q|\le\sqrt q$, at least
$$
          c_0 \frac{2^S}{3^{q+h}\sqrt q}                               \tag{2}
$$
distinct compatible bridge words of that total have $\beta\le B_0$
and lead backwards to $u\bmod 3^h$. Indeed prescribe the offset class
$s-3^q2^{-S}u\pmod{3^{q+h}}$. It is a unit. Apply the
[fixed-total floor and bounded outer-letter spreading](../native-pressure-20261118/EVERY-DEPTH.md)
there, retaining the explicit real offset cut in paper 48, (76).
The bounded outer letter sends the old real mark $B$ to $(1+3B)/2^a$,
hence preserves a uniform cutoff. The central total probability is
$\gg1/\sqrt q$. Each word there has probability $2^{-S}$, proving (2).

## Picking the bridge length to realize the physical octave

Let $J_w=3^L2^{-A}$ and $f_w$ be the forward composition for $w$, with
real offset $0\le\beta_w\le(3/2)^L-1$. Put $h=k+L$ and take the
inverse terminal class in (2) to be $u=f_w(r)\pmod{3^h}$; it is
independent of the representative of $r$. A bridge terminating
backwards in this class can be extended by the reverse of $w$.
In fact the full word has integral starting point congruent to $r$
modulo $3^k$, and integrality successively forces the indicated
inverse congruences at each preceding letter. All inverse states are
positive odd integers since each is a legal inverse of such an
integer, and their forward valuations are exact.

Choose a unit $s=(2^v b-1)/3$ between $D M$ and $D' M$, where $D$
is a sufficiently large absolute constant depending on $B_0$ and
$D'$ is absolute. The eligible exponents occur in two classes modulo
six, so such a $v$ always exists; $U(s)=b$. Put $H=J_w X$ and
$q_0=\log(H/s)/\log(4/3)$. For each integer $q$ within
$\epsilon\sqrt{q_0}$ of $q_0$ choose the unique integer $S$ with
$$
                  H/2 < s\,2^S/3^q\le H .
$$
For a sufficiently small absolute $\epsilon$ this gives
$|S-2q|\le\sqrt q$. The hypothesis on $X/M$, with $C$ enlarged,
ensures that $q_0$ exceeds the fixed onset, $q\asymp\log(X/M)$,
$h\le d(q-1)$, and $s\beta_w/H\le1/2$.
The last estimate follows from $s\beta_w/H\le D'M 2^{A-L}/X$.
The combined offset at $s$ of the initial source word followed by its
bridge is $B=\beta+J\beta_w\le B_0+1$, since $J<2s/H$.
Its ordinary source $n$ satisfies
$$
             n/X=(s\,2^S/(3^q H))(1-B/s).
$$
Taking $D$ large gives $X/4<n\le X$.

Every partial inverse prefix at $s$ of the combined bridge and source
word has offset at most $B$ by positivity. Its multiplier $P$ is at
most $3B$, since the last contribution to its partial offset is $P/3$.
Every nonempty inverse prefix therefore has ordinary state at least
$(s-B)/(3B)>M$, with $D$ chosen once as above. The empty prefix
is $s>M$. Thus appending the edge $s\to b$ gives the first landing
below or at $M$, at clock $L+q+1=O(\log(X/M))$. Telescoping the
affine product shows that the log correction up to this landing is
$$
                 \log(s/(s-B))+\log(1+1/(3s))\asymp 1/M .
$$

At a fixed $q$ the ordinary word is recovered from its source and
clock by deterministic forward iteration. At distinct $q$ the first
entry below or at $M$ has distinct clock, so no source is counted twice.
By the choice of $S$, (2) contributes
$\gg (H/s)3^{-k-L}/\sqrt q\gg (X/M)2^{-A}3^{-k}/\sqrt q$ at each
$q$. There are $\gg\sqrt{q_0}$ such lengths, proving (1).

## Consequence for separating ordinary basins

In particular, take $M=b=1$. On sources in the basin of 1, simultaneous
finite-precision observation of ternary phase and prescribed valuation
prefixes retains a fixed fraction of its unrestricted source-cylinder
size, uniformly in the digit range in (1). More generally every union
of disjoint such cylinders, each satisfying the range condition, obeys
the sum of (1). One may specify any odd class modulo $2^a$ in place
of $w$, at a loss of at most two in the count: follow the forced
valuations until the next valuation is unresolved by the $a$ bits,
and choose its least possible value by fixing at most one further bit.
This produces a full word with total at most $a$ inside that class.
At each $j\le L$ the starting congruence determines
$U^j n\bmod3^{k+j}$, so it determines all truncated real-word
Stieltjes transforms at these phases up to inverse depth $k+j$.
The resulting lower counts are on genuine ordinary convergent sources.
No assertion about an all-depth itinerary of one fixed source follows.

## Escape distortion survives simultaneous source conditioning

Let $C_*$ be one hypothetical escaping component, let $V_\infty(n)$
be its whole reciprocal distortion product, and put $V_\infty=0$ on
periodic components. Write $D(w,r)$ for the source cylinder above,
$\rho=2^{-A}3^{-k}$, and let $\eta<1$ be a uniform dyadic-shell
exponent for the number of distinct points on an ordinary orbit.
There are absolute $c,C>0$ and an onset $R_{C_*}$ such that
$$
 \#\{n\in[X/4,X]\cap C_*\cap D(w,r):
          0<1-V_\infty(n)\le R^{-1}\}\ge c\rho X/R                  \tag{3}
$$
for $R\ge R_{C_*}$ and $X\ge C R^{1/(1-\eta)}\exp(C(A+k+1))$.
Indeed, use the [finite-shell sibling proof](COMPONENT_STIELTJES.md)
with (1) at each retained unit sibling $s_i$, taking $b=M=s_i$.
The pre-entry logarithmic correction stays $O(1/s_i)$ uniformly
over the imposed source conditions. The retained siblings have
$s_i\ll R^{1/(1-\eta)}$, are incomparable, and have total reciprocal
weight $\gg1/R$, giving (3). Integration in radius as in that proof
gives a lower bound $c\rho(\log u)/u$ for the shell mean of
$V_\infty/(1+u(1-V_\infty))$ restricted to this component and
cylinder whenever $u$ is large and
$X\ge C u^{1/(1-\eta)}\exp(C(A+k+1))$.
All cylinder and scale factors are retained simultaneously.

There is also a pointwise classification obstruction for any two
distinct merger components, one of which can be the basin of 1.
Choose one fixed unit $b_i$ in each. For every pair $a,k$ with
$a\ge1$ and $X\ge C\max(b_1,b_2)\exp(C(a+k+1))$, condition the
uniform odd source in $[X/4,X]$ on its two residue classes modulo
$2^a$ and $3^k$. In **every** resulting cell, the conditional probability
of component $i$ is at least $c/b_i$. Apply the dyadic-cylinder
version of (1) with $b=M=b_i$. The number of odd sources in the
cell is at most $X/(2^a3^k)+1$ by the Chinese remainder theorem,
and $X/(2^a3^k)\gg1$ in the indicated range. Thus every classification
rule based only on these residues misclassifies a fixed positive
fraction of the shell when predicting membership in component 1:
in each cell either assignment errs on one of the two selected
components. This applies even to a different rule at every $X$.
It distinguishes the low-digit information missing from a possible
separating functional from the unrestricted information in the
ordinary source itself.

## Shrinking physical intervals and prescribed components

Let $\tau=4.117$ and $d_*=1/(2\tau)$. Uniformly under the wide
theorem's hypotheses, with $0<w_0\le1$ and
$$
         w_0\ge C(\log(X/M))^{-d_*},\qquad M w_0\ge C,                  \tag{4}
$$
the same controlled first landing and source constraints hold for at
least
$$
            c\,w_0(X/M)2^{-A}3^{-k}                                    \tag{5}
$$
ordinary odd sources in $[X,(1+w_0)X]$. In particular the interval
width can be any fixed negative power of $\log(X/M)$ with exponent
strictly smaller than $1/8.234$, subject to the other conditions.

Keep $s,H,q_0$ from the wide proof. Let $q$ run over its consecutive
block of $N\asymp\sqrt{q_0}$ central choices. We require an integer
$S$ with
$$
       1+w_0/3 \le s2^S/(3^q H)\le 1+2w_0/3 .                          \tag{6}
$$
This restricts $\log_2(H/s)+q\log_2 3$ modulo one to an interval of
length $\asymp w_0$. The same central window $|S-2q|\le\sqrt q$
holds whenever (6) is met. Uniformly in the phase, the interval is
met at least $c w_0 N$ times. In fact use
$\|h\log_2 3\|\gg h^{-\tau}$ for every positive integer $h$, from
[Fan–Queffélec–Queffélec, Theorem 2.1, and the reciprocal conversion](../binary-run-occupancy/MELLIN_PHASE.md).
For the last continued-fraction denominator $d\le N$, its successor
$d'>N$ gives $d\gg N^{1/\tau}$. On any complete block of $d$ indices
the rotation differs from a translated complete $1/d$ mesh by at
most $1/d'$. It therefore gives at least a constant times $w_0d$
hits once $w_0d$ exceeds a sufficiently large absolute constant, as
ensured by (4). The complete blocks cover at least $N/2$ indices.
This lower count avoids a two-sided discrepancy estimate.

Now $J\le s/H$ and the combined offset in the wide proof is again
at most $B_0+1$. Condition (4) and $s\ge DM$ ensure $B/s\le w_0/8$.
Multiplying (6) by $1-B/s$ places the true source in $[X,(1+w_0)X]$.
For each selected $q$ the weight bound (2), positivity, pre-entry
correction bound and first-hit disjointness apply without change.
Using the count of selected lengths gives (5).

Let $C_*$ be any merger component containing a fixed odd unit $b_*$
(in particular the basin of 1 is allowed). For all $M$ sufficiently
large at least $cM/b_*$ odd units $b\le M$ lie in $C_*$: apply (1)
at physical scale $M$ with target and threshold $b_*$, empty valuation
word and source class $1\bmod3$. For each of these units use (5) at
threshold $M$. Different first-landing labels give disjoint sources.
Consequently every such interval contains at least
$$
              (c/b_*)\,w_0X\,2^{-A}3^{-k}                              \tag{7}
$$
sources in $C_*$ matching the prescribed cylinder. The same holds
with the corresponding odd dyadic residue in place of its full word.
For example one may take $M=\lceil w_0^{-2}\rceil$ for $w_0\to0$
and $w_0\ge C'(\log X)^{-d_*}$, and allow $A+k$ up to a sufficiently
small constant times $\log X$. The earlier [growing-clock result](../profinite-orbit-averages/GROWING_CLOCKS.md)
proves an asymptotic frequency statement on shrinking intervals with
exponent less than $5/143$. Estimate (7) is a lower bound, at shorter
intervals and with the growing source-cylinder factor retained.

The mass in (3) also localizes to the shrinking interval itself.
For example let $\gamma=1-\eta$, take $A+k\le c_1\log X$ with $c_1$
sufficiently small, and suppose $C(\log X)^{-d_*}\le w_0\le1$.
Uniformly for $R\ge\max(R_{C_*},C/w_0)$ and $R\le X^{\gamma/3}$,
the lower count (3) on $[X,(1+w_0)X]$ is $c w_0\rho X/R$.
The retained sibling heights in its proof are $s_i\ll R^{1/\gamma}$
and $s_i\ge y_i\ge1/S_j\gg R$, where $S_j$ was chosen of order
$1/R$. Thus $w_0s_i$ is large and $\log(X/s_i)\asymp\log X$.
At each sibling (5) applies with $b=M=s_i$; the prescribed $c_1$
ensures the wide theorem's source-digit budget at every such height.
The same disjoint summation proves the claim. In particular if
$u\to\infty$, $u\ge C/w_0^2$ and $u\le X^{\gamma/3}$, then
$$
 \frac1{w_0 X}\sum_{\substack{X\le n\le(1+w_0)X\\
              n\in C_*\cap D(w,r)}}
       \frac{V_\infty(n)}{1+u(1-V_\infty(n))}
       \gg \rho\,\frac{\log u}{u}.
$$
Indeed integrate the count for $R$ between
$\max(R_{C_*},C/w_0)$ and $u$. Its logarithmic range is at least
$(\log u)/2-O_{C_*}(1)$ and $V_\infty\ge1/2$ on the retained events.
This finite physical-source conclusion is conditional on the escape
of the specified component.
