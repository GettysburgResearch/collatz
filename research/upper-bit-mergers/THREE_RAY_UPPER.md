# An upper bound from the two ordinary parity words

Let $T(n)$ be the positive shortcut Collatz map. For $r\ge1$, in every interval of $N\ge2$ consecutive positive starts, the number for which $n$ and $3^r n$ never meet is at most
$$
 C N\min\left(1,\frac{r}{\sqrt{\log(2N)}}\right).
 \tag{1}
$$
The constant is absolute. In particular the permanent failures for tripling have zero upper Banach density. The same upper bound counts starts missing a common-clock meeting by $\lfloor\log_2 N\rfloor$ steps. The order of this finite-clock estimate for distant blocks is also forced by the elementary walk lower bound. A power-saving bound for permanent failures does not follow. [Lower bound and scope](THREE_RAY_CLOCKS.md)

**PROPOSED, self-contained derivation of a previously stated result.** Leen gives the canonical process and excursion method. Duran previously established qualitative coalescence by a separate argument. We give the full probability proof here so (1) can be checked without assuming their absorption theorem. [Leen, *Quantitative synchronization of Collatz trajectories*](https://doi.org/10.5281/zenodo.23268755) · [Duran's earlier argument](https://doi.org/10.5281/zenodo.23003524)

## The level and the physical time of a return

Orient the current arms as $X$ and $3^sX+D$, $s\ge0$. The parity of $X$ gives a fair bit on a complete binary block. After fixing that parity, the new base is an affine function with odd slope of the next unexposed binary parameter. Induction gives exactly one residue modulo $2^h$ for each length-$h$ sequence of bits. The following table gives $(s',D')$ on that bit. It follows by applying the two ordinary shortcut branches, swapping the arms in the last entry.

| Current condition | Bit 0 | Bit 1 |
|---|---|---|
| $D$ even | $(s,D/2)$ | $(s,(3D+1-3^s)/2)$ |
| $D$ odd, $s>0$ | $(s+1,(3D+1)/2)$ | $(s-1,(D-3^{s-1})/2)$ |
| $D$ odd, $s=0$ | $(1,(3D+1)/2)$ | $(1,(1-3D)/2)$ |

The state $(0,0)$ gives an actual meeting. Take it to be absorbing, and let $\tau$ be its first visit. At any positive level $j$, each odd offset gives a fair jump up or down one level. To control the intervening holding time put $e_j=v_2(3^j-1)$. When $0<v_2(D)<e_j$ both bits decrease this valuation by one. From valuation at least $e_j$, including $D=0$, at least one of the two bits takes it to $e_j-1$. Thus the conditional expected time up to and including the next jump is at most $e_j+2$. Here $e_j=1$ for odd $j$ and $e_j=2+v_2(j)$ for even $j$ by factoring $3^{2m}-1$ and successive squaring. In particular $\sum_{j<H}(e_j+2)\ll H$.

For the fair jump walk from $s>0$ killed at zero, the expected number of visits to $j$ is $2\min(s,j)$. The probability of ever reaching $j$ is $\min(1,s/j)$ by the elementary gambler's ruin formula. After a visit the probability of hitting zero before another visit is $1/(2j)$. These formulas follow by solving the linear hitting-probability recurrence on a finite interval and letting the upper endpoint increase. The walk hits zero almost surely. The holding bound shows that its physical return time $R$ is also almost surely finite. Killing instead on exiting $(0,H)$ for $H>s$ gives at most $2s$ expected visits to every intervening level, and the physical exit time has expectation $O(sH)$. The probability of exiting at $H$ is $s/H$. Consequently
$$
 \Pr(R>t)\ll s/H+sH/t\ll \min(1,s/\sqrt t)
$$
upon taking $H$ comparable to $\sqrt t$ when $\sqrt t>s+1$ and using the trivial bound otherwise. Integrating this tail up to $h$ gives $\mathbb E\min(1,R/h)\ll s/\sqrt h$ for $h\ge1$.

## Why the offsets at level zero stay controlled

Write $z=D/3^s$, $r_0=99/100$, and $W=r_0^s\sqrt{|z|}$. At positive levels the two multipliers on $z$ are $1/2$ and $3/2$, and the additive terms have absolute value at most one. At even offsets the level stays fixed. At odd offsets the smaller multiplier raises the level and the larger one lowers it. Using $\sqrt{|u+v|}\le\sqrt{|u|}+\sqrt{|v|}$ gives
$$
 \mathbb E(W'\mid s,D)\le W+C r_0^{s-1}.
$$
Indeed the two coefficients of $W$ in conditional expectation are $(1/\sqrt2+\sqrt{3/2})/2$ and $(r_0/\sqrt2+\sqrt{3/2}/r_0)/2$, both strictly below one. Stop at $R\wedge t$. The expected total additive cost before $R$ is at most
$$
 2C\sum_{j\ge1}j(e_j+2)r_0^{j-1}<\infty
$$
by the visit and holding bounds. Fatou's lemma now gives $\mathbb E\sqrt{|D_R|}\le W+C_1$, uniformly in the initial positive level and offset.

At an odd level-zero departure from $d$, the first new normalized offset is $d/2+1/6$ or $-d/2+1/6$. The next raw level-zero offset therefore has expected square-root magnitude at most $a\sqrt{|d|}+b$ with $a=r_0/\sqrt2<1$ and absolute $b$. At a nonzero even level-zero offset, each step replaces it by $d/2$ or $3d/2$. In either case its valuation decreases exactly one and its expected square-root magnitude contracts. Thus the subsequent coast to an odd offset preserves the same upper bound. Its length $v_2(|d|)$ is at most $C\sqrt{|d|}$.

For clarity consider the successive odd level-zero offsets with zero retained as a cemetery state. Choose $K$ with $c=a+b/K<1$, and stop at the first offset with square-root magnitude at most $K$. Outside that set the conditional expectation of the next square-root magnitude is at most $c$ times the present one. Discarding paths at their first entry, the expected magnitude on the surviving paths falls by at least this geometric factor each turn. Thus both the expected number of turns and the expected sum of their initial magnitudes up to entry are $O(1+\sqrt{|d|})$. The raw-return estimate implies the same bound on expected total coast length, including the coast terminating at entry.

Every odd offset in this finite set admits a finite absorbing word. At level zero choose zeros to remove any twos. For odd $|d|>1$, the word $01$ when $d\equiv3\pmod4$ or $11$ when $d\equiv1\pmod4$ returns to level zero with offset $(3d-1)/4$ or $-(3d+1)/4$, respectively, of strictly smaller magnitude. Offsets $1,-1$ absorb on $001,101$. Choose a maximum word length $l$ over the finite set. At each visit try the word for the current offset. The conditional success probability is at least $2^{-l}$. Failed trials end in a fixed finite set of states, so the preceding estimates bound the expected number of returns and the expected coast length to the next trial uniformly. The number of trials is dominated by a geometric variable. All these assertions use the ordinary finite-past conditioning of the fresh bits.

## Adding the elapsed times

Outside the trial words themselves, every positive-level excursion after the initial one starts at level one or at a bounded level following a failed trial. The number of such excursions has expectation $O(1+\sqrt{|D/3^s|})$, by the return-moment and boundary estimates. The expected number of all other boundary-phase steps, consisting of departures, coasts and trial words, has the same bound. For the first excursion from level $s$ use its separate $O(s/\sqrt h)$ truncated-time estimate. The inequality $\min(1,(u+v)/h)\le\min(1,u/h)+\min(1,v/h)$ lets us add these estimates, taking conditional expectation at the start of each excursion. The mean length of a complete excursion is not needed. We obtain
$$
 \Pr_{s,D}(\tau>h)\le\mathbb E_{s,D}\min(1,\tau/h)
 \ll \frac{1+s+\sqrt{|D/3^s|}}{\sqrt h}.
$$
At $(s,D)=(r,0)$ this gives (1) by exact binary residue counting. Any interval of $N$ starts is covered by at most two full blocks of consecutive integers of length $2^{\lfloor\log_2 N\rfloor}$. Each such block samples every binary history exactly once. The same proof applies to any block of $N$ terms of a positive arithmetic progression of odd common difference, since each full block still represents every binary class. The bounds allow arbitrary interval location.
