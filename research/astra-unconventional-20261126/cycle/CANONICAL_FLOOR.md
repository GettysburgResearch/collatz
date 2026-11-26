# Canonical reverse disagreements on the bounded bad cycle

Write $C(n)$ when the ordinary positive integer $n$ reaches one under the shortcut map $T(2u)=u$, $T(2u+1)=3u+2$. Let $q$ be the least positive odd tripling disagreement in either direction. Assume the **bounded alternative** of the pinned minimum and excursion theorems. Then $C(q)$, $\neg C(3q)$, and $s=(3q-1)/2>1$ is the minimum of a nontrivial bad odd cycle. Every odd phase $x$ has $s\le x<8q$ and successor $x'$ determined by $2^a x'=3x+1$, with $a\in\{1,2\}$. The ceiling and integrality give $x\le(16s+7)/3$. The global floor theorem makes $s$ the least bad positive integer in every component, and the neighbor theorem gives $C(x-1),C(x+1),C(2x-1)$ at every phase. [Pinned minimum and orientation](https://github.com/GettysburgResearch/collatz/blob/26f070c38ad9edd21ed7dac6efaab6554550c2a3/research/astra-minimum-source-20261124/README.md) · [Pinned bounded alternative](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/README.md) · [Global floor and neighbor theorem](GOOD_NEIGHBORS.md)

Let $z$ be the least positive $17\bmod48$ source with $\neg C(z)$ and $C(3z)$. The theorem below produces a witness, so this minimum exists in the bounded alternative. This is the canonical orientation used by the quantitative return theorem. [Quantitative return](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/QUANTITATIVE_RETURN.md)

**Theorem.** The least unrestricted reverse disagreement is $s$. The bounded cycle contains a canonical reverse disagreement and
$$s\le z\le (16s+7)/3<8q.$$
In particular $16n<3z-7$ implies $C(n)$ for every positive integer $n$. If the cycle has $p$ odd phases and total clock $h$, then at least $h-p$ of its bad phases $x$ satisfy $C(3x)$. For $s\ge25$ it contains at least $(2h-3p)/4$ distinct canonical reverse disagreements, taking $p$ to be the fundamental odd period.

**Proof.** At any exponent-one phase $x$ one has $3x=2x'-1$, a good neighbor. The minimum $s$ has exponent one because an exponent-two successor $(3s+1)/4$ would be smaller. Thus $s$ is bad with $3s$ good, and all smaller positive integers are good.

Next start at a phase $x=x_0$ with exactly $r\ge2$ consecutive exponent-two edges until the next exponent-one edge at $x_r$. Since $x_r\equiv3\bmod4$ and $x_j-1=(3/4)^j(x-1)$ for $0\le j\le r$, one has
$$x_j=1+2\cdot4^{r-j}3^j u, \qquad u>0\text{ odd}.$$
The five ordinary shortcuts $3,5,8,4,2,1$ have two odd inputs. Since $3x\equiv3\bmod32$, the same five parity inputs give
$$T^5(3x)=1+27\cdot4^{r-2}u.$$
Indeed two starts differing by $32v$ follow those five parities with final difference $9v$. Each $1+4v$ reaches $1+3v$ in two shortcuts. Applying $r-2$ such pairs gives
$$T^{2r+1}(3x)=1+3^{r+1}u=(3x_r-1)/2=x_{r+1}-1.$$
The endpoint is good by the lower-neighbor theorem. There is also a four-clock merger independent of $r$. For two consecutive exponent-two edges $x,x_1,x_2$, the two odd shortcuts from $3x=4x_1-1$ reach $9x_1-1=4(3x_2-1)$, so $T^4(3x)=3x_2-1=T(2x_2-1)$. The last source is good by the neighbor theorem. Thus any phase with two exponent-two edges immediately ahead has a good triple. Together with the exponent-one cases this leaves at most the last phase in each maximal exponent-two run uncovered. There are at most $2p-h$ such runs, the number of exponent-one phases, proving the asserted count $p-(2p-h)=h-p$.

Multiplying the cycle equations gives $2^h=\prod_i(3+1/x_i)>3^p$, hence $2h>3p$. There are $h-p$ twos and $2p-h$ ones, so the twos outnumber the ones. The cycle has a one since twos strictly decrease. Choose the first phase $x$ of a maximal run of at least two twos. Its incoming exponent-one edge gives $2x=3v+1$, so $x\equiv2\bmod3$. Its outgoing run gives $x\equiv1\bmod16$ by the preceding formula. Hence $x\equiv17\bmod48$. Its triple is good and $x$ is bad. Therefore $s\le z\le x\le(16s+7)/3$. The global floor now proves the conclusion for $n$.

Finally a run of $r$ twos satisfies
$$(4/3)^r=(x-1)/(x_r-1)\le (16s+4)/(3s-3)<(4/3)^6 \quad(s\ge25).$$
Thus each run has length at most five. If $b$ counts the runs and $t$ the runs of length at least two, then $h-p\le b+4t$ and $b\le2p-h$. Every such long run starts at a distinct canonical witness, giving $t\ge(2h-3p)/4$. ∎

## The descending run into the global minimum

The edge entering $s$ has exponent two, since an exponent-one predecessor $(2s-1)/3$ would be smaller. Let $x$ start the maximal run of $r$ twos ending at $s$. The edge entering $x$ has exponent one. If $r=1$, its source would be $(8s-5)/9<s$, impossible. Thus $r\ge2$, and $x$ is one of the canonical witnesses just constructed. Its preceding edge gives $x\equiv2\bmod3$. Consequently
$$
r=v_3(s-1)=1+v_3(q-1),\qquad
s\le z\le x=1+(4/3)^r(s-1).
$$
Here $(s-1)/3^r=(x-1)/4^r\equiv1\bmod3$, so $(q-1)/3^{r-1}\equiv2\bmod3$. For $s\ge25$ one has $2\le r\le5$ and $243(z-1)\le1024(s-1)$.

There is a further rigidity at the least canonical reverse disagreement itself. If $4^r\mid z-1$, then $r$ successive ordinary two-step identities give
$$s\le T^{2r}z=1+(3/4)^r(z-1)\le1+(3/4)^r(x-1)=s.$$
The first inequality uses badness of $z$ and the global floor. Thus $z=x$, and $v_2(z-1)=2r+1$ by the minimum's exponent-one exit. In particular, when $v_3(q-1)=1$, the least canonical reverse disagreement is this actual cycle phase, since every $17\bmod48$ integer is one modulo sixteen. An off-cycle least canonical source must satisfy $v_2(z-1)<2r$.

The source-specific bound depends on the bounded bad cycle. It supplies no corresponding improvement to the first-crossing alternative, and it leaves the ordinary hit of the least canonical source unresolved. The Lean module proves the physical four-clock merger, extracts the length and unit parameter of the minimum's descending run from the bounded backward edges for $s\ge25$, and proves the strengthened canonical floor and divisibility squeeze under the displayed ordinary phase labels, global floor and canonical leastness. It also proves capture at length two from $27\nmid s-1$ and $z\equiv17\bmod48$. The positive fraction of all cycle phases and the identification of the pinned excursion alternative with these hypotheses are written arguments. [CanonicalFloor.lean](CanonicalFloor.lean)
