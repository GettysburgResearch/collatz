# A complete denominator or polynomially many near-dyadic phase pairs

**Proposed written theorem, with the logarithm input separated.** For a positive rational Syracuse cycle let \(p\) be its primitive odd period, \(q\) its complete reduced denominator, \(m,X\) its real odd minimum and maximum, \(R=X/m\), and \(\gamma=\log_2 3\). For \(0\le\kappa\le 1/50\), let \(K_\kappa\) count the **unordered pairs of distinct actual odd states** \(x<y\) on this one cycle for which, for some integer \(d\ge2\),
\[
               |\log_2(y/x)-d|\ \le\ p^{-\kappa}/\log p .               \tag{1}
\]
A pair is counted once. The exponents \(d\) can vary over the witnessed pairs.

Put \(e=2-\gamma,\ s=1-2e\), and set
\[
 \theta=\gamma^{-1}
 \max\{3(s+\gamma e)/5,\ 9s/16+5\gamma e/8\}
      =0.3197044778\ldots,\qquad a=1-3\theta .
\]
**Assume \(\mu(\gamma)\le3\).** If \(p\to\infty\) along any sequence with \(\limsup\log R/\log p\le w\) for some \(0\le w\le1/1000\), then
\[
 \boxed{\displaystyle
 \liminf\frac{\log(q(1+K_\kappa))}{\log p}\ \ge\
       \frac{a-(1-\theta)\kappa-0.89w}{1+a}.}                          \tag{2}
\]
In particular all subpolynomial real widths \(R=p^{o(1)}\) are included, with \(w=0\). For \(q=p^{o(1)}\), including \(q=1\), their near-dyadic pair exponents are at least \(0.03928052\ldots\) at \(\kappa=0\) and \(0.02620905\ldots\) at \(\kappa=1/50\). At the polynomial width allowance \(w=1/1000\) these exponents still exceed \(0.0384\) and \(0.0253\), respectively. For unrestricted widths this gives a disjunction: on the subsequence of ordinary cycles with \(R\le p^{1/1000}\) the stated pair counts are mandatory; the complementary cycles already have a polynomial excursion. For any fixed \(R<8\) only \(d=2\) can occur for all sufficiently large \(p\). Equation (2) permits many pairs sharing a state and supplies no cycle-existence assertion. It does not require the full native clock to be reduced, or the rational phases to follow sorted angular order.

The proof of the intermediate tradeoff (7) is independent of the exponent-three input. That input is used below as the stated [log-ratio approximation theorem](https://arxiv.org/html/2610.28079v1#S11). The previous [two-grade rational denominator result](MATCHED_RATIONAL_DENOMINATORS.md) gives the stronger denominator exponent in the fixed band \(R<4\), where (1) is eventually impossible. The [three-grade ordered-grid argument](THREE_GRADE_SEPARATIONS.md) has a stronger factor-four exponent when the full grid is already known to be ordered. Here nonordered grids, large reduced denominators, and widths growing with \(p\) are allowed.

## Counting what a chain of binary native constraints costs

Consider columns of positive odd rational states on a common normalized calendar
\[
           2^{h_t}Y_{t+1,j}=3Y_{t,j}+C_{t,j},\qquad C_{t,j}\in\{1,2\},
 \qquad h_t+\log_2 C_{t+1,j}-\log_2 C_{t,j}\ge1 .
\]
The last inequality is the true positive native division count; it implies \(h_t\ge0\). Suppose a length-\(n\) record of the binary tags is a Sidon code, so equal coordinatewise integer sums identify the original unordered pair. Group the \(n\) rows into maximal consecutive blocks connected by edges \(h_t\le1\), among the first \(n-1\) edges. On an edge of winding one the bits are nondecreasing. An edge of winding zero requires a strict rise from zero to one. An \(l\)-vertex block with only weak rises admits \(l+1\) staircase configurations, including the singleton case. If a strict rise occurs, that entire block is forced, and two strict rises in one block would be impossible.

Let \(k=\#\{t<n-1:h_t=1\}+2\#\{t<n-1:h_t=0\}\). A weak block of length \(l\) contributes \(l-1\) constraints to \(k\), and a pinned block contributes \(l\). Let \(C\) be the sum of \(\log_2 d\) over the block alphabet sizes \(d\), using \(d=l+1\) at weak blocks and \(d=1\) at pinned ones. Let \(H\) be the corresponding sum of \((2-1/d)\log_2d\). Then
\[
 C\le n+(\gamma-2)k,\qquad H\le 3n/2+(5\gamma/3-3)k.                 \tag{3}
\]
For weak blocks these inequalities are equalities at \(l=1,2\). The functions \(\log_2(l+1)\) and \((2-1/(l+1))\log_2(l+1)\) are concave for \(l\ge1\); for the latter, the second derivative at \(x=l+1\), times \(x^3\ln2\), is \(3-2x-2\ln x<0\) for \(x\ge2\). The two secant-line bounds for \(l\ge2\) follow. For pinned blocks their right sides are positive even with \(k=l\). This proves (3).

For \(M\) words the [ordered suffix-difference entropy argument](MATCHED_SIDON_CODES.md) gives the following version for these varying alphabets:
\[
                 \log_2 M\le \max\{3C/5,\ 3H/8\}+O(\log(n+2)).         \tag{4}
\]
Put all alphabet sizes at least three first and choose the longest prefix whose total alphabet capacity in bits is at most \(\log_2(M/n^2)\). The case \(M\le n^2\) is immediate. The capacity differs from \(\log_2 M\) by \(O(\log n)\) since every alphabet has size at most \(n+1\). Coordinatewise unordered pairs of block symbols determine all constituent binary sums, so the code separates suffix ordered differences on pairs of distinct words sharing their prefix, exactly as in the binary-ternary proof. The entropy of the suffix output for a uniform same-prefix ordered pair is at least \(\log_2 M-O(\log n)\); use \(\Pr(\text{diagonal})\le n^{-2}\). Each suffix alphabet costs at most \((2-1/d)\log_2d\) in this output. If the prefix uses only nonbinary symbols, the removed cost is at least \(5/3\) times its bit capacity, yielding \(3H/8\) in (4). If it includes a binary symbol then all remaining symbols are binary (discard pinned sites); their difference entropy is at most \(3/2\) times remaining bit capacity, giving \(3C/5\). This proves (4) even for unbounded lengths of monotone blocks. Its homogeneous precursor is [Della Fiore–Dalai, Theorem 2.1](https://doi.org/10.1016/j.disc.2021.112751).

## The complete denominator and the true reduced grid

Let \(A=\sum a_t\) be the native division sum, \(g=\gcd(A,p)\), \(P=p/g,\ B=A/g,\ \rho=B/P\). Pass to a subsequence where the exponents of all positive quantities below converge, using extended values when necessary. Write
\[
 \beta=\lim\frac{\log q}{\log p},\quad \sigma=\lim\frac{\log m}{\log p},\quad
 \pi=\lim\frac{\log P}{\log p},\quad
 \delta=\lim\frac{\log(1+K_\kappa)}{\log p}.
\]
For now suppose \(\sigma>1+\kappa,\ \pi>\kappa\), all these exponents are finite, and \(P\) grows as a power of \(p\). The latter follows from \(\pi>\kappa\). These conditions will be established on the only nonautomatic branch of (2).

The [residue-fiber inversion theorem](RESIDUE_FIBER_INVERSIONS.md) gives at least \(g/h-1\) inversion triples, where \(h=\operatorname{ord}_q(3^P2^{-B})\le q\). Each is a true pair with \(y=2^d x+u,\ 0<3u<2^d-1\), \(u\) a positive odd integer. In particular \(d\ge3\), and \(0<\log_2(y/x)-d<1/(3m\ln2)\) independently of \(d\) and \(R\). For \(m\to\infty\) the exponent \(d\) is unique for each pair. Thus these triples give distinct pairs in (1), and
\[
                               1-\pi\le\beta+\delta.                    \tag{5}
\]

Build the [actual reduced-clock grid](REDUCED_CLOCK_SIX_SUMS.md) from the raw lifts \(\widetilde X_t=2^{E_t}x_t\), \(E_{t+1}=E_t+a_t\), now choosing \(L=4X\). The de-meaned error \(b_t=\log_2(\widetilde X_t/\widetilde X_0)-t\rho\) is \(p\)-periodic and \(O(p/m)\) on all integer dates. Take \(\tau B=k_0P+1\), \(1\le\tau\le P\), and \(F_t=\lfloor\log_2(\widetilde X_t/L)\rfloor\). With \(W=\lfloor Pp^{-\kappa}/(\log p)^5\rfloor\) and \(0\le j\le W\), put
\[
 Z_{t,j}=2^{-F_t-k_0j}\widetilde X_{t+j\tau},\qquad
 c_{t,j}=Z_{t,j}/x_{t+j\tau}.
\]
These are true \(p\)-periodic columns, with positive power-of-two tags \(c_{t,j}\) between one and \(O(R)\): the log of \(Z_{t,j}/L\) equals the base fractional angle plus \(j/P+b_{t+j\tau}-b_t\). In particular \(qZ_{t,j}\) are integers. Take an anchor \(t_*\) whose base angle tends to zero from above, which exists by the true rotation and \(m\to\infty\). At the \(P\) reduced ranks, the integer array \(qY_r=q2^{-F_{t_*}-k_0r}\widetilde X_{t_*+r\tau}\) has shape \(qL(2^{r/P}+o(1))\) uniformly. It is of polynomial height in \(P\), since \(qX=p^{O(1)}\) and \(\pi>0\). Integrality follows from \(L=4X\), so the dyadic multiple of a true phase is integral after scaling by \(q\), even at the endpoints. At each compact interior rank interval the normalized floor is exact, giving \(Z_{t_*+r\tau,j}=Y_{r+j}\) when \(r+j<P\).

Forbid \(d=|i-j|\in[1,W]\) if some row contains \(c_{t,i}/c_{t,j}\ge4\) or its reciprocal at least four. Its two physical states give (1), since their true log separation differs from the corresponding integer by at most \(W/P+O(p/m)<p^{-\kappa}/\log p\). These are distinct states. Different positive differences witness different unordered state pairs: the chronological separation is \(\pm d\tau\bmod p\), and reduction modulo \(P\) with \(\gcd(\tau,P)=1\) identifies \(d\) up to sign; all such \(d\) are less than \(P/2\). So at most \(K_\kappa\) positive differences are forbidden, irrespective of how many rows repeat a witness.

The graph on the \(W+1\) starts obtained by forbidding those differences has an independent set \(S\) of size at least \((W+1)/(2K_\kappa+1)\). At each actual native date divide all columns in \(S\) by the common minimum tag \(s_t=\min_{j\in S}c_{t,j}\). Their normalized tags are in \(\{1,2\}\), their normalized states times \(q\) are integers, and the adjusted winding is
\[
                      h_t=F_{t+1}-F_t+\log_2 s_{t+1}-\log_2s_t.
\]
The true native exponent on each column is \(h_t+\log_2 C_{t+1,j}-\log_2 C_{t,j}\ge1\). For a signed pair comparison of the normalized states, any zero propagates *integrality* around the full physical \(p\)-cycle because \(q\) is odd and \(h_t\ge0\). Every nonzero integer sign persists strictly since the signed digit forcing has absolute value at most two. Hence one zero forces all comparisons to vanish. Multiplying back by each \(s_t\) gives a nonzero polynomial comparison on four offsets annihilating the integer spatial array \(qY_r\) on a fixed interior interval. The [sparse integer recurrence theorem](SPARSE_RANK_RECURRENCES.md) excludes this: its degree is at most \(W\le P/(\log P)^5\), coefficient mass is bounded, and the array has the stated polynomial height and exponential shape. Thus pair sums are distinct at every temporal base for all sufficiently large cycles in this subsequence.

## Rate ledger

The initial normalized labels of \(S\) lie in an interval of length \(O(X(W/P+p/m))=O(Xp^{-\kappa})\). Each \(s_t\) is in \([1,O(R)]\), so the variation of its log between any two dates is at most \(\log_2 R+O(1)\). Take
\[
            n=\left\lceil\log_3(C_0 q X R p^{-\kappa})\right\rceil+4
\]
with an absolute sufficiently large \(C_0\). The raw total winding satisfies \(F_{t+n}-F_t=n\gamma+O(1+n/m)\), with lower bound \(n\gamma-1\) by the positive per-step corrections. Hence \(2^{\sum_{t<n}h_t}\) exceeds the absolute difference of the initial pair sums multiplied by \(q\). Equal coordinatewise binary tag sums imply that this integer difference is divisible by that power of two. It is zero, and the preceding paragraph identifies its unordered pair. The binary tag words on \(S\) are a Sidon code as required for (3)–(4).

Since \(k\ge\sum_{t<n-1}(2-h_t)\), the upper total winding estimate gives \(k\ge en-\log_2R-O(1+n/m)\). Use the negative coefficients in (3). At \(k=en\), (4) has coefficient \(\gamma\theta\) per date. The growth allowed by the extra \(\log_2 R\) in the deficit bound is at most
\[
 \max\{(3/5)(2-\gamma),\, (3/8)(3-5\gamma/3)\}\log_2 R
                                    <\tfrac14\log_2 R .
\]
The graph lower bound and the definitions of \(n,X\) now give
\[
       \pi-\kappa-\delta\ \le\
             \theta(\sigma+\beta-\kappa)+(2\theta+1/4)w.               \tag{6}
\]
Together with (5), the actual clock lower bound \(\rho-\gamma\gg_\epsilon P^{-\mu-\epsilon}\) for any irrationality-exponent input \(\mu\), and its upper bound \(1/(3m\ln2)\), this gives \(\sigma\le\mu\pi\) and the tradeoff
\[
 (1+a_\mu)\delta+(a_\mu+\theta)\beta
       \ \ge\ a_\mu-(1-\theta)\kappa-(2\theta+1/4)w,\qquad
                  a_\mu=1-\mu\theta,                                  \tag{7}
\]
when \(a_\mu\ge0\). Equation (6) itself does not assume that relation on \(\mu\). At \(\mu=3\), \(2\theta+1/4<0.89\); (7) implies (2) since \(a+\theta<1+a\).

## Why the remaining branches are covered

Put \(c_\kappa=[a-(1-\theta)\kappa]/(1+a)\). If \(\liminf\log q/\log p\ge c_\kappa\), (2) is immediate. To prove it subsequentially, it suffices to consider finite \(\beta\le c_\kappa\); larger limits are already sufficient. Since the \(p\) odd numerators are distinct and at most \(qX\), \(\sigma+\beta\ge1-w\). Thus \(m\) tends to infinity at least polynomially in \(p\). The actual clock and the logarithm input give bounded \(\sigma\le3\pi\) and \(\pi>0\), even before invoking the grid.

A short elementary source count improves the minimum enough for the fine cutoff (1). Set
\[
 N=\left\lceil(\log_2(qX)+\log_2R+3)/\gamma\right\rceil .
\]
For any native word of \(N\) odd steps on this cycle, its total division exponent lies between \(N\gamma-\log_2R\) and \(N\gamma+\log_2R+O(N/m)\) by the true positive drift. Its canonical dyadic cylinder therefore identifies at most one source numerator in \([1,qX]\), by the affine numerator formula modulo its full power of two. The number of compositions of length \(N\) into positive integers with total at most an integer \(U\) is \(\binom UN\). Choose \(U=\lceil N\gamma+\log_2R+C_1N/m\rceil\) for an absolute \(C_1\). Writing \(S=\sigma+\beta\) and \(w'=\lim(\log R)/\log p\le w\) on a further subsequence, the binomial entropy bound gives
\[
        1\le(S+3w')\,H_2\!\left(\frac{S+2w'}{\gamma(S+3w')}\right).
\]
Here \(S\ge1-w'\), and \(w'\le0.001\), so the entropy argument is at least \(0.63\). Its entropy is at most \(H_2(0.63)<0.951\). Consequently \(S\ge1/0.951-0.003>1.04852\). Over \(0\le\kappa\le0.02\), \(1+\kappa+c_\kappa\) increases and is less than \(1.04622\). Thus \(\sigma>1+\kappa\) and \(\pi\ge\sigma/3>\kappa\), exactly the earlier conditions. The finite exponents used in the grid follow also from \(K_\kappa\le p^2\). This finishes (2). When \(w=0\), the sharper preliminary lower bound on \(S\) is \(1/H_2(1/\gamma)=1.05268085\ldots\).

[Finite chain and slope controls](check_global_dyadic_pair_abundance.py) · [Finite receipt](global_dyadic_pair_abundance_controls.json)
