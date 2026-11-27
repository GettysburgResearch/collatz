# Odd work and the first physical crossing

**PROPOSED. Universal convergence and a pointwise replacement of every least reverse defect remain OPEN.** All heights below are ordinary positive integers. Write $T$ for the shortcut map, $Q_t(n)$ for the number of odd inputs before clock $t$, and $C(n)$ for a finite hit at one. A supplied hit may contain extra laps at one unless a first hit is explicitly stated. The source exponent $j$ in $3^jz$ and the supplied certificate's odd count $Q_H(3^jz)$ are different integers.

## Descent or a strictly cheaper suffix at the original source

Fix odd $z$, $j>0$, and an actual supplied upper hit $T^H(3^jz)=1$. Choose any integers $M,D\ge0$ with

\[
j+Q_H(3^jz)+D\le M,\qquad 3\cdot 3^D < 2M.
\]

One of the following alternatives holds.

* At some $i\le H$ the actual lower arm reaches a positive value $T^i z<M$.
* At $H$, the lower arm has used **more** than $j+Q_H(3^jz)+D$ odd inputs. There is a first $0<t<H$ at which $Q_t(z)=j+Q_t(3^jz)$. At this clock put $y=T^t(3^jz)$ and $x=T^t z$. Then $x=y+c$ with $c$ a positive integer. The original remaining $H-t$ steps take $y$ to one with exactly $Q_H(3^jz)-Q_t(3^jz)$ odd inputs. This number is strictly less than the upper hit's original cost. If $z$ is bad then $x$ is bad and $y$ is good.

Taking $M=\lceil z/2^{40}\rceil$ makes the first alternative a sufficient physical descent for the previously proved quantitative return from a canonical reverse defect. No bound on the original hitting clock is used. The hypotheses restrict the odd count of the supplied upper certificate. The second alternative gives an ordered pair at a known positive additive distance. It does not supply a ternary multiple of the good value.

For the estimate, if $x_i=T^i z\ge M$ through $H$ and $q=Q_H(z)<3M$, then

\[
(3M-q)2^H x_H\le3M\,3^q z .
\]

At an odd input the inequality follows by charging the additive one in $2T(n)=3n+1$ against $3n\ge3M$. At an even input no charge is necessary. The upper hit gives $3^{j+Q_H(3^jz)}z\le2^H$. Combining the inequalities when $q\le M$ and $q\le j+Q_H(3^jz)+D$ would force $2M\le3\cdot3^D$. These are the kernel theorems `floor_budget`, `descent_at_supplied_hit` and `drop_or_exact_suffix`. [FirstCrossing.lean](FirstCrossing.lean)

## Why the first balance cannot itself be an equal-slope merger

Set $b_t=j+Q_t(3^jz)-Q_t(z)$ on a prefix where this signed expression stays nonnegative. At clock one the strict inequality $T(3^jz)<3^j Tz$ follows from the odd branches and $3^j>1$. At each subsequent step the nonnegative integer exponent updates by the difference of the two parity bits. The four ordinary branch identities preserve

\[
T^t(3^jz) < 3^{b_t} T^t z.
\]

Consequently the first zero of $b_t$ has strictly positive displacement on the lower arm. Any synchronous merger with equal total ternary exponents must first pass a clock with $Q_i(z)>j+Q_i(3^jz)$, and subsequently return to equality. This holds even when both inputs converge. For $z=23$, $j=1$ the first balance at clock 2 gives lower and upper values 53 and 52, the lower arm strictly overshoots at clock 3, and the arms meet at 20 at clock 5. [Proofs `strict_before_overshoot` and `meeting_requires_overshoot`](FirstCrossing.lean)

Even outside the cheap-hit hypotheses a genuine bad/good pair has unbounded cumulative odd-work surplus. If $x$ is positive and bad, all its states exceed one, so

\[
2^h T^h(x)\,2^{Q_h(x)}\le 7^{Q_h(x)}x.
\]

For any $s$, putting $k=7\cdot7^s x$ gives $Q_{2k}(x)>k+s$: the opposite inequality would give $8^k\le7^k7^s x$, while $7^k(k+7)\le7\cdot8^k$. Apply this after an actual hit on the upper arm. Each extra $2k$ clocks at one costs exactly $k$ odd steps. These extra clocks do not belong to the original supplied suffix. [Theorem `unbounded_after_supplied_hit`](FirstCrossing.lean)

## Converting an additive carry to a genuine ternary multiple

At a crossing $x=y+c$ the positive carry $c$ depends on the actual two traces. Suppose $T^h c=1$ with $p=Q_h(c)$ and write

\[
y=2^{h+2k}u,\qquad u\text{ odd},\qquad p+k=R+1 .
\]

Then $T^{h+2k}(x)=1+3^{R+1}u$ and its next step agrees with the next step from $3^R u$. Thus badness moves from $x$ to this actual ternary multiple. The upper arm uses only halvings during these $h+2k$ clocks. If the remaining supplied hit has length $h+2k+K$, exactly its last $K$ steps form the supplied hit from $u$, with every remaining upper odd input retained. The reference $c$ may have any actual hit of its own. No bounded catalogue of reference words or prior hitting clocks is imposed. This construction needs the displayed amount and parity of available halving time. It also needs an independent well-founded measure if used repeatedly. [Physical identity and certificate transfer](FirstCrossing.lean)

For an arbitrary physical lower unit $n$, a given odd $a$ works in an immediate equality $T(n)=T(3a)$ **if and only if** $n=9a+1$. Some integer $a$ works if and only if $n\equiv10\pmod{18}$. In particular if the desired multiple is $3^{R}u$ with $u$ the odd part on a specified upper suffix and $R\ge1$, the exact residual test is $n=1+3^{R+1}u$. This criterion places no bound on $R$. [CanonicalDeadline.lean](CanonicalDeadline.lean)

## A canonical upper first hit misses every such one-step orientation repair

Take $3\nmid z$, $H\ge9$ with $81z+271=2^H$. The triple first hits one at $H$ with three odd inputs. For every $i\le H$ and **every** $a\ge0$,

\[
T(T^i z)\ne T(3a).
\]

This all-clock, all-comparator conclusion applies in particular to the PR197 canonical rank-three family $H=18+162m$, $z=(2^H-271)/81\equiv17\pmod{48}$. Its source equation and the original finite-window physical height barrier are prior work. Here the exclusion concerns all one-successor repairs throughout the supplied hit. Members of this arithmetic family need not be defects. [PR197 at `156652e0`, family and original barrier](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean)

Indeed $z=161+256v$. The first even lower inputs occur at clocks 1, 3 and 6, all at $2\bmod3$. The lower arm then reaches $2^{H-7}-1$ at clock 7, takes $H-7$ odd steps, and ends at $3^{H-7}-1\equiv2\pmod3$. No lower state through this interval is $10\bmod18$. On its upper arm clock 8 gives $17+27v$, whose one odd step reaches $2^{H-9}$. All earlier upper values exceed one. These are kernel conclusions. At clock 5 the first equal-grade pair is $(y+1,y)$ with $y=8(17+27v)$, and the remaining upper hit uses one odd step. The carry $1$ hits one only at even clocks, whereas $v_2(y)=3$. The entire-prefix result rules out every alternative immediate successor repair even if the clock and the odd comparator are chosen after inspecting both traces. Several inverse odd steps, a later lower clock, a different upper witness, or an indirect directed path can still work. [All-parameter kernel proof](CanonicalDeadline.lean)

The same exact criterion gives an all-time consequence for the separately hypothesized bounded cycle of the least odd tripling disagreement. In that branch every maximal odd run is followed by a single even input. All phases are prime to three, and each even phase is the immediate image of an odd input and hence $2\bmod3$. Thus **no phase on any lap** has a common immediate successor with a tripled source. The known partner $3q=2s+1$ does merge with the minimum's trajectory using two further steps after the unequal initial odd runs. This is a longer comparison, consistent with the one-step impossibility. Neither statement establishes that the hypothetical cycle exists. [Cycle proof and precise clock costs](../cycle/README.md)

PR206's recurring 513-rank common block may lie strictly to one side of the prescribed bad exponent. Nothing in these pointwise estimates forces a change inside that block or gives a bound on the residual cost of a more general directed replacement. PR195's bounded-template exclusion concerns visits by a bounded number of repeated forward templates on a fixed tower. The first-balance estimate instead charges an actual pair of arbitrary words, and the canonical control treats every possible immediate multiplied comparator. Neither set of source results supplies the remaining pointwise return. [PR206 recurrence at `45a6a111`](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerRecurrence.lean) · [PR195 bounded templates at `4fd8af31`](https://github.com/GettysburgResearch/collatz/blob/4fd8af31c1ea525252b4d8f7411b5921dd447048/research/astra-global-closure-20261124/round11/formal/BOUNDED_TEMPLATE.md)

The first unsupported inference would identify the cheaper good suffix with a suitably related bad *multiple* in every case, or would bound the cost of a subsequent replacement without proving its arithmetic identity. The positive carry and the arbitrary later odd surplus alone imply neither conclusion. Both Lean modules import the existing local `MinimumFailure` and its `SourceDeletion` dependency. Every public theorem prints its axioms. The independent integer control checks finite representatives and both branches of the finite descent test. [Checker](check.py) · [Replay counts](../../../reports/astra-diagonal-closure-20261125/transport/finite.json)
