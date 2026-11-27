# Integral rank residues and an exponential pair-spacing problem

**Written reduction in the bounded least-disagreement branch.** Let \(s,p,h\) be the ordinary minimum, least odd period and total halving count from the physical mask theorem. Put \(\lambda=h/p\) and \(d=12/25\). Take the unique dyadic \(M\) in \([p^2,2p^2)\) and write \(T=4s/M\). For all sufficiently large candidates there are absolute constants \(c,C>0\) such that
\[
 \#\{(r,j):0\le r,j<p,\ r\ne j,\
     \|T(2^{r/p}-2^{j/p})\|_{\mathbb R/\mathbb Z}\le C/p\}
 \ \ge\ c\,p^{26/25}/\log p. \tag{1}
\]
The height bound in the transfer note and the cited \(\mu(\log_2 3)\le3\) theorem put \(p^{14/23-o(1)}\le T\le p^{1+o(1)}\) along any unbounded sequence. The displayed lower bound is deterministic at the actual \(T\). The mean over a real interval is much smaller. We have no pointwise upper bound excluding (1). [Physical strip transfer](PHYSICAL_STRIP_TRANSFER.md) · [Chudnovsky, Theorem 11.1](https://arxiv.org/abs/2610.28079)

## Integral support and phase spacing

The normalized integers \(U_r\) satisfy \(4s\le U_r<8s\) and
\(\left|\log(U_r/(4s))-(r/p)\log2\right|\le\delta\), where \(\delta=h\log2-p\log3\le p/(3s)\). In particular
\[
 |U_r-4s\,2^{r/p}|\le C_0p
\]
uniformly at all ranks, since \(p/s\to0\). [Pinned rank estimate](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-global-closure-20261124/round13/cycle/README.md)

For a single input slope sufficiently close to \(\log_2 3\) and any \(K\ge1\), the population of allowed initial ordinary source residues modulo \(2^K\), taken over all cuts and layers of its mask, is at most
\[
 C_1(K+1)2^{dK}. \tag{2}
\]
In a block of 256 odd steps with mechanical clock \(S\), the checker counts all gap histories from one entrance layer with free terminal layer. Its maximum \(N_S\) over the 258 possible schedules and all entrance layers satisfies \(N_S^{25}<2^{12S}\) for both \(S=405,406\). All comparisons use integers. These schedules cover a single open neighborhood of the irrational slope by the finite phase-partition argument in the transfer note. For a longer fixed schedule, multiply the block bounds with free exits and use a constant factor for the last \(<256\) odd steps. The mechanical clock sums telescope. Select \(b=\lceil(K+4)/\lambda\rceil\) odd steps so every actual chronological duration is at least \(K\) and is \(K+O(1)\). There are \(O(b+1)\) possible schedules as the entrance rank varies and at most three initial layers. Each native word determines its starting residue modulo \(2^K\). Starting at an intermediate even shortcut costs a bounded factor, since there is at most one even input between consecutive odd ones. Finally \(U_r\) is \(1,2\), or 4 times a native odd phase, so (2), with another absolute constant, holds for the \(U_r\) as well. [Exact population transfer](check_rank_support.py) · [Replay](../../../reports/astra-sixhour-20261127/arithmetic/rank_support.json)

Set \(K=\log_2 M\). By Cauchy–Schwarz at least \(p^2/[C_1(K+1)M^d]-p\) ordered pairs of distinct ranks have \(U_r\equiv U_j\bmod M\). Every such pair satisfies (1) by the real phase estimate. This is the ordinary integrality input. For the upper range of \(T\), the logarithm-ratio estimate gives \(h/p-\log_2 3\gg_\epsilon p^{-3-\epsilon}\), while the cycle product bounds the same difference above by \(1/(3s\log2)\). The lower range comes from \(p\ll_\theta s^\theta\) for every \(\theta>23/60\).

## Average spacing and the remaining exceptional scale

For any fixed \(C>0,T_0\ge1\), average the left side of (1) over uniform \(T\in[T_0,2T_0]\). Its expectation is
\[
 O_C\bigl(p+(p/T_0)\log p\bigr). \tag{3}
\]
Indeed, for \(u=|2^{r/p}-2^{j/p}|\) the measure fraction singled out by that pair is \(O_C(p^{-1}[1+(T_0u)^{-1}])\), by covering \([T_0u,2T_0u]\) by unit periods. The mean value theorem gives \(u\ge(\log 2)|r-j|/p\). Summation gives (3). In particular for \(T_0\gg\log p\), the fraction of real scales supporting (1) is \(O(p^{-1/25}\log p)\). This does not exclude the one dyadic rational selected by a cycle.

## What a common prefix contributes

For two ordinary native sources \(x,y\) with the same next \(k\) parity bits, let \(m\) be the number of odd inputs in this common word and \(x',y'\) their endpoints. Then
\[
 x'-y'=3^m (x-y)/2^k .
\]
Their extensions through \(B\) more native bits therefore put
\[
 3^m (x-y)/2^k\bmod 2^B \ \in\ {\cal A}_B-{\cal A}_B,\qquad
 |{\cal A}_B-{\cal A}_B|\le C_2(B+1)^2\,2^{24B/25},
\]
where \({\cal A}_B\) is the union of ordinary source residues in (2), including even cuts. This restriction cancels the translation from the shared prefix exactly. For a fixed \(k\) all such \(m\) lie within an absolute constant of \(k/\lambda\). Moving both sources ahead one common odd edge multiplies their quotient difference by three after removing the remaining dyadic prefix, while reducing the remaining odd count by one. Hence the transformed quantity tested against \({\cal A}_B-{\cal A}_B\) stays the same. This prevents independent powers of three from being obtained by this single transport.
