# Independent review of the first-crossing cycle bound and the smaller-merger obstruction

**Cycle verdict.** The unbounded one-lap reduction and carry envelope are **VERIFIED, written**. The numerical conclusion is **VERIFIED with the identified finite census as a dependency**. Each hypothetical nontrivial positive cycle has a contiguous first coefficient-crossing word containing at least 47,468 odd inputs and at least 75,235 shortcut steps. The ordinary census is a completed external computation in this review. I independently recomputed the envelope maximum and replayed the two reported extremal starting values.

**Merger verdict.** The source-fixed odd-count obstruction, the explicitly descending arithmetic subprogression, and the stated fixed-basin consequences are **VERIFIED, written**. The lower bounds quantify over all successful smaller-source histories at the specified $n$ and $b$.

## Frozen sources and evidence

| Source | Git blob | SHA-256 |
|---|---|---|
| `CYCLE_CLOSURE.md` | `5ee14f4b92eb764444d13eddfefa50d6be1149ec` | `3bc5953b10af0f7a979ba3ad15579bfa557499c52baf5c1a3fbdf1bf70842231` |
| `CyclePacking.lean` | `1623eca9961e595179875f3d1da39f8ef0031669` | `db704e854e95fbfca1c2f8438c368b8b2250a1268fda60e6deb867f18240851d` |
| `check_first_crossing.py` | `67a3ddbb9dd8c929d59ee47fb4b4798408497e75` | `593257a2ab62468bad78b5e3054d5eb42be7d56443750ae993a3f0e1189238a3` |
| `check_ordinary_descent.cpp` | `e9f10d5bc77f86008dde3aae16015ab5f45b9902` | `ad7e60ba6d6f4f618ef2af7f9a2f992c5a371bb9b899c00fcaddd63a0d52c4b4` |
| `first-crossing-envelope.log` | `a81b7a9da6a75512e76a20ac89bec8d8dd15b0a4` | `1dee2eddaa2e2951145037ba7f36ddc3d983dbed62002ed267c3f4b9de262e5d` |
| `ordinary-206178386.log` | `5c4bee6aaddeb904bd45cce1685dab90797edb78` | `cd62ed751945e20926222b47d17a4af59c875ad850db26159564bad78e191302` |
| `cycle-lean.log` | `b75b3d2372acafc2a28aad572d1e44c52d4cfd38` | `ace8b0a6c6d354b3d03b7d883705674997eb8c5717d621e369b003196b9b6a8c` |
| `GLOBAL_CLOSURE_ATTEMPT.md` | `b8d235cce661af99af8ca2558f584509b3927609` | `455c4d0737fb0f93823ab68f103fa74457a59bd642b4aefb6826048916218860` |

The fixed-basin consequence also uses `QUANTITATIVE_GLUING.md`, blob `6e82806280af8933dc80decf3ed0286a48029c33`.

## Cycle proof

The positive shortcut cycle has a nonzero carry because some step must be odd. Its full product $c=3^p/2^n$ is strictly less than one by the affine closing equation. For the partial products $h(t)$ at times $0,\ldots,n-1$, equality at two different times would give a positive power of two equal to a nonnegative power of three. Choose the unique minimum $h(r)$. After rotation to $r$, each unwrapped proper-prefix product is at least one, and each wrapped proper-prefix product is $c h(t)/h(r)>c$ because $t<r$. The final product $c$ is therefore strictly less than every proper-prefix product. From each mark, take the first subsequent strict decrease below its value. The endpoint always qualifies, so these marks finish at exactly the end of this lap.

For any atom with $p>0$, its last step must be even. Thus its length is $L_p=\lfloor\log_2 3^p\rfloor+1$. The zero-weight atom is the single even step and has center zero. The zero-based position $d_i$ of the $i$-th one, numbering from zero, is at most $\lfloor\log_2 3^i\rfloor$ by applying the proper-prefix condition immediately before that bit. Every carry summand increases with its corresponding position. All the largest positions fit simultaneously in a word of length $L_p$, since they increase by at least one, and an intervening prefix of weight $i$ has length at most $\lfloor\log_2 3^i\rfloor$. Thus $E_p$ is the maximal syntactic carry. At a largest boundary $X$, its preceding boundary $y\le X$ gives $(2^{L_p}-3^p)X\le C_w\le E_p$ for a represented atom. This argument applies even if the cycle boundary states repeat.

**Independent integer check.** Set $B=206178386$ and $D_p=2^{L_p}-3^p$. The termwise inequality $3E_p\le p3^p$ shows that a floor at least $B$ is possible only when $p3^p\ge3BD_p$. I tested this necessary inequality with exact integers for every $0\le p\le47467$. The only survivors were 15,601, 31,202 and 46,803. Evaluating the defining sum $\sum_i3^{p-1-i}2^{\lfloor\log_2(3^i)\rfloor}$ in reverse order gives the respective floors **206,178,386**, **206,173,806** and **206,172,280**. Direct integer comparison also gives $2^{75234}\le3^{47468}<2^{75235}$.

The census code tests the inclusive interval $2,\ldots,B$, counts $B-1$ starting values, checks the odd multiplication against $(2^{64}-2)/3$ before computing it, keeps every state positive, and exits with failure at the step cap. The input guard prevents the outer-loop increment from wrapping. Its completion receipt reports descent of all 206,178,385 starts. Arbitrary-precision spot replays reproduced the 376-step first descent from 63,728,127 and the post-step peak 1,638,950,788,059,290 from 120,080,895. I inspected the receipt and program without rerunning that large census. Strong induction now makes every positive state at most $B$ converge to 1. If all the atoms had $p\le47467$, a boundary of the proposed nontrivial cycle would lie in this interval. This proves the claimed inclusive lower bounds on one atom.

The Lean output lists 21 declarations with at most the usual `propext`, `Classical.choice`, and `Quot.sound`. Its `firstCrossing_center_bound` accepts a supplied cyclic partition with legal edges. Its general height inequality, first-crossing length, upper carry envelope, literal transition lemmas and equal-length pair-of-words bound match their stated uses. The one-lap construction, simultaneous attainment of the extremal positions and the 206-million-start census are written or computational steps outside the module. I inspected the final formal source and receipt. The separate PR191 source-review table has its own attribution and review boundary.

## Merger proof

Since $n+1$ is divisible by $2^b$, its first $b$ inputs are odd and $T^b(n)+1=(3/2)^b(n+1)$. The all-odd upper envelope for $T^a(x)+1$ forces $a>b$ when $x<n$. Split the competing history after $D=a-b$ steps. If its final $b$ steps have $p_2$ odd inputs and carry $C$, then

$$
T^D(x)=3^kn+m,\qquad k=b-p_2,\qquad
m=(3^b-2^b-C)/3^{p_2}\in[0,3^k)\cap\mathbb Z .
$$

Here $C\le3^b-2^b$, and the endpoint equality gives integrality. If its first $D$ inputs contain $p_1\le k+v_3(n)$ odds, then $J=3^kn/3^{p_1}$ is an integer. The signed integer $x_0=x-2^D J$ shares those $D$ parities and maps to $m$. Negative integers stay negative, so $x_0\ge0$. At zero all these parities are even, forcing $x\ge n$. Otherwise $3^{p_1}\le3^{p_1}x_0\le2^Dm<2^D3^k$, which gives $x=x_0+(2^D3^k/3^{p_1})n>n$. This also covers $b=0$, $k=0$, and $m=0$. Hence $p_a(x)=p_1+p_2>b+v_3(n)$ and $a>b+v_3(n)$.

For $H\ge1$, the simultaneous classes $2^H\mid n+1$, $3^H\mid n$ rule out every merger with both clocks at most $H$. For the stricter class put $s=\lceil H\log_2(3/2)\rceil$. Its next $s$ inputs are even because $3^H(n+1)/2^H-1$ is a multiple of $2^s$. At $H+d$ with $d<s$ the coefficient $3^H/2^{H+d}>1$. At $d=s$, the integer $2^{H+s}-3^H$ is positive and $n\ge3^H>3^H-2^H$, giving strict descent. The first descent is exactly $H+s$, so $H+1\le\tau(n)\le\lceil H\log_2 3\rceil$. CRT gives a least positive source below $2^{H+s}3^H<2\cdot9^H$, yielding the global obstruction to $o(\log n)$ even on sources having a supplied smaller merger.

For each **fixed** $H$, the basin exponent comparison transfers to that residue class. In a **fixed** eligible target basin the separate explicit construction gives $3^H\le n_H\le(t+1)2^{2\cdot3^{2H-1}}$. The latter proves a failure of $o(\log\log n)$ along its designated sources. No uniform bound in $H$ follows from fixed-cylinder exponent invariance. As an independent bounded check, all 1,774 smaller mergers with $n\le511$, $a,b\le12$, and the required initial congruence satisfied the odd-count inequality. The predicted exact first descent was reproduced for the least CRT source at each $H=1,\ldots,32$.

The final merger source adds a finite-control section. I reran its ordinary Python control with assertions enabled. The output exactly reproduced 7,413 smaller mergers, 16 with both parameters positive, 360 constructed descending sources and 20 prescribed-basin sources. The checker has Git blob `cb702379420d7a578f2bf5fd29c6245e6ee12707` and the matching output has blob `b4bd106d09f4bdfc8c5432728eff9b1bd4d5e1d3`.

The outstanding global steps are to exclude the remaining cycle weights, to control nonperiodic positive orbits, or to construct a smaller ordinary merger for every required source.
