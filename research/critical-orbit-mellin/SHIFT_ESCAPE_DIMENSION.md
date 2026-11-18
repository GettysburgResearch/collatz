# Sharp ternary dimension of exceptional integer translates

**PROPOSED.** Write $h=H_2(p)$ for binary entropy at $p=\log2/\log3$. For $\alpha\in\mathbb Z_3$ let $\mathcal H_2(\alpha)$ be the sum of $J^2=(3^q/2^A)^2$ over its legal inverse valuation words, including the empty word. Given any function $g:\mathbb N\to[1,\infty)$ with $g(n)\ge n$, define
$$
 E_g=\{\alpha:\mathcal H_2(n+\alpha)\ge g(n)^2\ \text{for infinitely many positive integers }n\}.
$$
Then $\dim_{H,3}E_g=h=0.9499555\ldots$ in the usual ternary metric. The same dimension holds when the sum is replaced by the supremum of its individual terms. Thus even arbitrarily high spikes in the metric family persist on a set of known positive dimension. In contrast, for Haar-almost every shift the normalized pressure tends to zero. The result concerns all-word pressure on translated ternary targets; the ordinary first-hit pressure is a subobservable at positive odd targets.

### Frostman upper bound

For $u>0$ set $f(u)=u-\log_3(2^u-1)$, with minimizer $u_*=-\log_2(1-p)\in(1,2)$. Direct substitution gives $f(u_*)=h$. Suppose a probability measure $\nu$ on $\mathbb Z_3$ satisfies $\nu(B)\le K3^{-dq}$ for all depth-$q$ ternary balls, with $d>h$. Uniformly for integer $n$, every specified length-$q$ inverse word is legal at $n+\alpha$ on one such ball. Summing gives
$$
 \int \mathcal H_{u_*}(n+\alpha)\,d\nu(\alpha)
 \le K\sum_{q\ge0}\left(\frac{3^{u_*-d}}{2^{u_*}-1}\right)^q<\infty
$$
with bound independent of $n$. Since $u_*<2$, $\mathcal H_2^{u_*/2}\le\mathcal H_{u_*}$. Markov and $\sum n^{-u_*}<\infty$ show $\nu(E_g)=0$. Frostman's lemma on compact subsets of the Borel set $E_g$ implies $\dim_{H,3} E_g\le h$. The same argument at the countably many positive thresholds $\varepsilon n^2$ gives $\mathcal H_2(n+\alpha)/n^2\to0$ for $\nu$-almost every $\alpha$. [Frostman's lemma and the mass distribution principle](https://doi.org/10.1002/9781119942399)

### An inverse alphabet of dimension approaching h

Fix $1<b<\log_2 3$. Take block length $q$ large and total valuation $A=\lfloor bq\rfloor$, so each block has multiplier $J=3^q/2^A>1$. There is a family of at least $c_b\binom{A-1}{q-1}$ words with pairwise distinct legality cylinders. To verify this, condition iid geometric letters of mean $b$ on sum $A$, so their compositions are uniform. For some $0<\delta<1$,
$$
 \mathbb E[(2^a/3)^\delta]<1,
$$
since $\mathbb E\log(2^a/3)=b\log2-\log3<0$ and the moment exists near zero. The geometric local estimates $\sup_n\Pr(S_m=n)\ll_b m^{-1/2}$ and $\Pr(S_q=A)\gg_bq^{-1/2}$ follow from the negative-binomial formula and Stirling at its mode. The scaled inverse numerator $C/3^q$ is one third the sum of the suffix products of $2^{a_i}/3$. For each length $l<q$ its conditional $\delta$-moment is at most $O_b(\sqrt{q/(q-l)})\mathbb E[(2^a/3)^\delta]^l$ by the complementary-prefix local estimate. The sum of these bounds is uniform, by splitting at $q/2$. Thus a positive fraction have $C\le B_b3^q$. The [numerator injectivity argument](MINIMUM_TAIL.md) bounds multiplicity in each legality class on this fraction by $B_b+1$. Keep one word per such class; let their number be $M$.

### Nested integer shifts

Start at $n_1=1$. For each stage $j$, construct $k_j$ concatenated blocks at the shifted target $\alpha+n_j$. All parent cylinders from the previous stage share depth $qk_{j-1}$, with $k_0=0$. For $j\ge2$ set $n_j=n_{j-1}+2\cdot3^{qk_{j-1}}$. This makes every previously specified prefix legal at the new shifted target, since it is unchanged modulo the entire prefix modulus. Pick $k_j>k_{j-1}$ large enough that $J^{k_j}\ge j g(n_j)$. At each next block all $M$ children are available with distinct depth-$q$ relative cylinders: on a legal prefix the inverse map is an affine bijection from its ternary ball onto $\mathbb Z_3$, with a unit slope after removing its prefix scale. A change of stage changes the translation, but every parent still has precisely $M$ children. Each limiting $\alpha$ has a single legal word of multiplier at least $j g(n_j)$ at each of the odd times $n_j$.

The uniform branching measure assigns mass $M^{-k}$ to each retained ball at depth $kq$. Intermediate radii lose at most a fixed factor depending on $q$, so the mass distribution principle gives dimension at least $\log M/(q\log3)$. Letting $q\to\infty$ gives a lower bound $b H_2(1/b)\log2/\log3$ by Stirling, and then $b\uparrow\log_2 3$ gives $h$. This proves the lower bound even for the supremum of individual word weights.

### Relation to ordinary escape

If an ordinary odd orbit is nonperiodic, its distinct forward values $t_j$ tend to infinity. The [ordinary reciprocal-product bound](https://github.com/GettysburgResearch/collatz/blob/6bee3183ff7f29f2e20ca88ab94bc7745c1af602/research/novel-swarm-20261030/pass3/ORDINARY_BOUNDARY.md) implies that the word from its fixed initial source to $t_j$ has $J\ge c t_j$ for some fixed $c>0$. For every ordinary integer shift $m$, taking $n_j=t_j-m$ gives $\limsup_n\mathcal H_2(n+m)/n^2>0$. Hence a single ordinary escape puts every integer shift in the exceptional set for failure of normalized decay. That set also has dimension exactly $h$ by the preceding upper bound and construction. The dimension bound leaves the particular shift zero unresolved.
