# The archimedean gap during a long unmatched native clock

Use the [signed affine line](SIMPLE_LINE_CYCLES_AND_SHADOWS.md) of a pair cylinder. At a given date orient the arms so that $B=3^jA-a$ with $j\ge0$ its true affine slope gap. Thus $a$ is a nonzero integer on an unmatched prefix, with $3\nmid a$ if $j>0$. Define
$$
                     \lambda=|A-3^{-j}B|=|a|/3^j .
$$
This number is independent of the representative of the source cylinder. At $j=0$ either ordering gives the same value.

**Proposed theorem.** On any native prefix of a positive odd ordinary $s$ and $3s$ unmerged through the ending date, of total odd grade $G$, the number of departure dates satisfying $\lambda\ge2^{-b}$ is at most
$$
                         (b+4)(G+1),\qquad b=0,1,2,\ldots .               \tag{1}
$$
Use the affine line after date zero for this count; date zero may also be included by setting $\lambda=0$. The same bound applies to the entire native word of any nonempty ordered adjacent return with combined grade $G$. More generally an arbitrary admissible entry contributes at most $\log_2^+\lambda_{\rm in}$ to the right hand side.

Put $W=\max(1,\lambda)$. A common even departure sends $\lambda$ to $\lambda/2$. All other departures have $W'\le2W$. In fact an up step has $\lambda'\le(\lambda+3^{-j-1})/2$, a down step has $\lambda'\le(3\lambda+1)/2$, and a common odd has $\lambda'\le(3\lambda+1-3^{-j})/2$. At level zero one can interchange the arms before a mixed step, with no cost to the potential. These are just the four native branch equations. Thus the total positive variation of $\log_2W$ is at most the number of active dates (at least one odd letter), hence at most $G$. Both base entries have $W=1$. Nonnegativity of the potential implies its total negative variation is at most $G$ as well.

There are at most $G$ common-even steps with $\lambda\ge2$, each subtracting exactly one from the potential. Within each maximal consecutive common-even interval, halving gives at most $b+1$ dates with $2^{-b}\le\lambda<2$. There are at most $G+1$ such intervals and at most $G$ active dates. Adding proves (1), with room at both endpoints.

For example, since $\lambda\ge3^{-j}$, (1) gives the low-slope occupation bound with $b=\lceil J\log_2 3\rceil$ whenever $j\le J$. If $k/(G\log(2+G))\to\infty$, then for every fixed $C>0$ a proportion tending to one of all native dates satisfies
$$
                      |A-3^{-j}B|<G^{-C}.
$$
At positive ordinary representatives, dividing this inequality by $A\ge1$ also gives a relative approximation to the ratio $3^j$. The approximation permits a large nonzero integer $a$ whenever $j$ itself is large.

## Consequences for the genuine scalar rational phases

Outside at most $O((G+1)\log(2+G))$ dates, the [common-run decomposition](SIMPLE_LINE_CYCLES_AND_SHADOWS.md) supplies a genuine native scalar rational phase $z=a/(3^j-1)$ with $j>0$. Its reduced odd denominator $q$ divides $3^j-1$. At every such date,
$$
                   |z|=\frac{\lambda}{1-3^{-j}}\le \tfrac32\lambda,
                   \qquad q\ge1/|z|.
$$
Consequently any family violating the uniform logarithmic upper bound spends a proportion tending to one of its entire native clock on scalar rational phases with $|z|<G^{-C}$ and $q>G^C$, for **every fixed** $C$. Quantitatively the selected scalar dates with $q\le Q$, for any $Q\ge1$, are at most $O((G+1)\log(2+Q))$ independently of denominators on all other dates, by (1) alone.

There is also a growing prime cutoff. Let $Y=\sqrt{\log_2(2+G)}$. For odd $q\mid3^j-1$ with $1\le j\le G+1$, its part supported on primes $\ell\le Y$ is at most
$$
                         j\,3^{Y^2}.                                     \tag{2}
$$
Indeed for each such $\ell\mid q$ put $e_\ell=\operatorname{ord}_\ell(3)\le\ell-1$. The odd-prime lifting identity gives $v_\ell(3^j-1)=v_\ell(3^{e_\ell}-1)+v_\ell(j)$ because $e_\ell\mid j$ and $\ell\nmid e_\ell$. Their first factors have product at most $3^{\sum_{\ell\le Y}(\ell-1)}\le3^{Y^2}$ and the second factors have product at most $j$. In particular (2) is polynomial in $G$. Thus along any superlogarithmic family, at a proportion tending to one of its native dates the genuine scalar denominator has part supported on primes **larger** than $\sqrt{\log_2(2+G)}$ exceeding $G^C$ for every fixed $C$. This statement counts prime powers with multiplicity. In the other direction, a family in which all retained scalar phases have denominators supported on a fixed finite set of primes has $k=O(G\log(2+G))$; its discarded common-run tails, balanced dates and mismatches already satisfy this bound. The estimates leave open the behavior of unrestricted scalar denominators.
