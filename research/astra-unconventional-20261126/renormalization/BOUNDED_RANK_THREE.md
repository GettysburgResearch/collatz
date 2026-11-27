# Three upper odd steps on the bounded bad-cycle branch

**PROPOSED written deduction with kernel-checked physical prefix tests.** Let $s$ be the least positive bad integer on the bounded branch, and $z$ the least canonical reverse disagreement. Direct trajectories take every positive integer below 25 to one within 14 shortcuts, so $s\ge25$. Write $r=v_3(s-1)$ for the descending run of exponent-two edges into the minimum. The cycle argument proves $2\le r\le5$ and
$$
        s\ge 1+(3/4)^r(z-1).
$$
The bound on $r$ uses $s\ge25$, which holds since the positive integers below 25 reach 1. The cycle squeeze also proves that $z$ is itself the on-cycle canonical witness when $4^r\mid z-1$. In particular this holds for every $z=17\bmod48$ at $r=2$. All other exclusions use the global floor together with the defining minimality of the canonical parent. [Bounded minimum, descending run and equality condition](../cycle/CANONICAL_FLOOR.md)

Suppose $3z$ has a first hit with three odd departures. The pinned rank-three restriction gives $6\le e\le48$, where $e$ counts even inputs between the second and third upper odds, and
$$
          81z+15+2^{e+2}=2^H,\qquad H\ge e+3.
$$
The following possibilities remain after applying the bounded-cycle floor. No row asserts existence of a bad source. [Prior exact shape and gap restriction](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/RANK_THREE_RESTRICTION.md)

| Run into $s$ | Remaining $e$ |
|---:|---|
|2|none|
|3|6|
|4|6|
|5|6|

## Actual contracting prefixes

Every positive canonical solution of the displayed upper shape has $H\ge18$. For $H<18$ it suffices to test $6\le e\le H-3$, the integral quotient and its class modulo 48; there are no solutions. With $D=2^{18}$ let $a_e$ be the representative of $-(15+2^{e+2})/81\bmod D$ in $[0,D)$. Here $84145\cdot81=1\bmod D$. Thus $z=a_e+Dt$ for some ordinary $t\ge0$. For $h\le18$, the first $h$ steps have the same odd count $p=P_h(a_e)$, and
$$
          T^h z=T^h a_e+3^p2^{18-h}t .
$$
At every populated table entry the two integer checks $4^rT^h a_e<3^r a_e$ and $4^r3^p<3^r2^h$ prove $T^h z<(3/4)^r z<s$ on the full unbounded row. This is impossible on the bad lower arm. Each entry gives $(h,p)$.

| $e$ | $r=2$ | $r=3$ | $r=4$ | $r=5$ |
|---:|---:|---:|---:|---:|
|6| | | | |
|7|9,5|10,5|10,5| |
|8|9,5| | | |
|9|9,5|11,6|12,6|12,6|
|10|9,5|11,6| | |
|11|9,5|11,6|13,7|14,7|
|12|9,5|11,6|13,7|18,10|
|13–48|9,5|11,6|13,7|15,8|

For $e\ge13$ the common fifteen binary bits are those of $-15/81$, whose word is $101011010101010$ (one denotes an odd input). The Lean module checks witnesses separately on every listed row, including both the constant and the unbounded coefficient. The finite replay independently prints each witness. [Kernel prefix and affine lift](RankThreeFloor.lean) · [exact checker](check_bounded_rank.py) · [ordinary receipt](../../../reports/astra-unconventional-20261126/renormalization/bounded-rank.json)

At $e=7$ there is a stronger witness outside the native lower prefix. The parent is $929+1024t$ for some $t\ge0$, since $81z+527=0\bmod1024$. Its tenth lower site is $221+243t$. One odd input sends $147+162t$ to that same site. Since $4^5(147+162t)<3^5(929+1024t)$, the visitor lies below $s$ at every allowable $r$. This eliminates the remaining $e=7$ entry with the actual positive visitor.

## A smaller canonical disagreement for gaps eight and ten

For $e=8,10$, use the leastness of the canonical parent as well as the global floor. The following rows are physical identities for every ordinary $t\ge0$. Each row takes $w=T^5z$ and then follows the ordinary orbit of $3w$.

| $e$ | $z$ | $w$ | $h$ | $T^h(3w)$ |
|---:|---|---|---:|---|
|8|$6561+8192t$|$5537+6912t$|8|$584+729t$|
|10|$109985+524288t$|$92801+442368t$|14|$12388+59049t$|

The upper power identity fixes the displayed binary class as soon as $H\ge13$ or $H\ge19$, respectively. Testing $e+3\le H<13$ or $e+3\le H<19$ gives no positive canonical solution in the respective exceptional range. Both lower five-step words use three odd inputs. The upper words use two and six. Direct lifting therefore gives the stated affine forms, with positive integer coefficients and endpoints. The constants and coefficients separately give $w<z$, $w=17\bmod48$ and $1024T^h(3w)<243z$. Thus $T^h(3w)<s$, so $3w$ is good. Since $w$ lies on the bad lower orbit, it would be a smaller canonical reverse disagreement, a contradiction. The Lean theorems `gap_eight` and `gap_ten` discharge both unbounded progressions using the supplied leastness and floor.

For an independent small-height check, the canonical solutions with $z<2^{40}$ in these gap families have $(e,H,z,\text{first lower hit})$ equal to $(6,18,3233,107)$, $(15,37,1696775585,191)$, $(16,22,48545,122)$, $(20,38,3393502625,108)$ and $(39,43,81445305761,168)$. To exhaust these, $2^{e+2}\le2^{H-1}$ gives $2^{H-1}\le81z+15$ and hence $H<49$. The prefix proof itself works at every size in its complete residue classes.

## The missing gap-six entry at run length two

Write $j=H-7$ and $M_j=2^j-1$. At $e=6$ the shape is $81z=2^{j+7}-271$, with $j=11\bmod162$ and $j\ge11$. The seven lower shortcuts reach $M_j$. Indeed $z=33+128t$ and $T^7z=22+81t$, giving $128T^7z=81z+143$. If $r=2$, the cycle squeeze puts $z$ on the bounded bad cycle, whose odd phases are at most $(16s+7)/3$. The odd point $M_j$ is therefore on that cycle, and $s\le M_j$. But for $M_j=31+32v$, five consecutive odd shortcuts reach $242+243v$, with $3(242+243v)>16M_j+7$. For $j\ge11$ their endpoint is still odd. This violates the cycle ceiling. Thus **the entire bounded run-length-two branch excludes a least canonical parent with upper rank three**. This argument does not place a general off-cycle minimum on the bounded cycle.

Even for $r=3,4,5$ a surviving gap-six source would make $M_j$ the **first bad Mersenne**. Indeed $s\ge1+(3/4)^5(z-1)=3M_j/8+11/32$, so $M_{j-2}=(M_j-3)/4$ and all smaller Mersenne values lie below $s$. The even-index $M_{j-1}$ merges with $M_{j-2}$. Moreover $3M_j$ merges with $M_{j-1}$, so $M_j$ is a smaller reverse disagreement of residue $31\bmod48$. This supplies the two actual labels, but gives no smaller canonical disagreement at $17\bmod48$. The fixed-word uniform quotient for this specific family already excludes one uniform below-parent canonical query from the two Mersenne source forms. [Even-index and tripled Mersenne links](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/MERSENNE_FRONTIER.md) · [uniform quotient and separate gap-six case](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/source-progress/UNIFORM_MERSENNE_QUOTIENT.md)
