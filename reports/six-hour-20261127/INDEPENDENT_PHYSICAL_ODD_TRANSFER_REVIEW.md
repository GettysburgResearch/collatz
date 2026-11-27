# Fresh audit of the unrestricted physical odd-occupation transfer

I reconstructed UNRESTRICTED_PHYSICAL_ODD_OCCUPATION.md (SHA-256 7862197b6a4d82a979ac7bb3cccf0a2716876554ed52edc8885df6e5ef31b166). The four rows hold with the stated full-denominator and large-period qualifications. The denominator condition and the counting inputs of each row remain needed as stated. This is written mathematics.

## Physical depth and the near-minimum census

With $d$ the cycle's common odd reduced denominator, shortcut parity of a rational state is parity of its integral numerator. In $n$ shortcut steps a fixed parity word fixes the initial numerator modulo $2^n$, by the affine identity and invertibility of $3^k$. Starting in $[s,Rs]$ and stopping after exactly $n$ steps keeps the terminal value at least $s$ and every odd emitter at least $s$, irrespective of excursions. The product identity therefore forces $k(\log_2 3+\log_2(1+1/(3s)))\ge n-\log_2 R$. The strict inequality $5\log_2 3<8$ leaves a uniform margin as $n,s\to\infty$ for this fixed $R$. For $n=\lfloor\log_2(Rds)\rfloor$ at most two representatives of each qualifying word lie in the numerator range. The binary tail bound at $5/8$ and $H_2(5/8)<24/25$ give the claimed $O_R((ds)^{24/25})$ independent of the full denominator. If the low population is at least $\kappa P$ and $d\le P^\delta$, distinctness first ensures $s\to\infty$ and the census then gives $P/s\ll P^{\delta-1/24}$.

The centered logarithmic correction on an arc of length $k$ is the sum of $u_t-\bar u$, where $u_t=\log_2(1+1/(3x_t))$. Its magnitude is at most $k(P-k)(\max u-\min u)/P$, by comparing the means on the arc and its complement. This gives the stated, slightly looser $P/(3s\ln2)$ uniform bound. Maximizing the physical log-ratio over the same terminal phases gives $\log_2(x_i/s)$. Thus dense physical low population under the small-denominator assumption forces uniform $o(1)$ approximation simultaneously at every phase. Strict thresholds $R<2^T$ then transfer the original strict density alternative without loss.

I reconstructed the new $R=3$ row against SPARSE_REAL_DEPTH_ALTERNATIVE.md. At $c=3/5$, a forced-zero-to-free transition crosses the wrap and has mechanical letter two, so the arbitrary-positive cap projection is admissible. Ternary equal-pair peeling gives $6^{(3/5)n+o(n)}<3^{(49/50)n}$ from $6^{30}<3^{49}$. The mask and intervening arbitrary grades cost $2^{b[H_2(\tau)+4\tau]}$ on the common original source modulus. With $(\eta,\tau,\delta)=(10^{-3},10^{-4},10^{-5})$ I obtain retained proportion $44999/50000$, separation slack $210977/300000000$, upper source exponent $123461/375125$ and contradiction slack $474076539/37512500000$. The strict physical threshold uses $3^5<2^8$. I found no gap in this transfer or the other three inherited real-depth rows.

## Earlier ordinary estimates also yield the four stated ordinary fractions

Weaver 181/v1 §§3–4, especially (6), (9)–(11), counts shortcut occupations with the published 2018 logarithmic input. Its referee explicitly proposes updating that input. In fact its source estimate and an elementary clock transfer recover the exact four *ordinary* fractions here, with the updated exponent three for the last two. The earlier localized estimate in this deduction invokes the fixed-place Subspace Theorem even for the first row. The present low-population census with a full variable denominator, the uniform real-depth conversion and the elementary first-row proof remain separate features.

Here is the clock transfer for an ordinary cycle of minimum $s\ge1$. Fix $h=Ks>s$. An eligible odd source $y$ is one with shortcut successor $T(y)>h$. Let $N$ count these sources. Put $V(x)=\max(0,\log_2(x/h))$ along the cyclic shortcut orbit. Each even departure $x\ge2h$ loses exactly one unit of $V$. Its losses sum to at most the positive increments of $V$. These occur only at eligible odd sources, each contributing at most one because $T(y)/y\le2$. Each even departure $h<x<2h$ ends a run strictly above $h$. The number of such departures is at most the number of entering odd sources $y\le h<T(y)$, since the orbit visits its minimum below $h$. The high odd departures and the entering odd sources are disjoint subsets of the eligible sources. Consequently the total number of shortcut departures above $h$ is at most $2N$. If $K=3R/2+1/1000$ and $s>500$, every eligible source satisfies $y>(2Ks-1)/3>Rs$. Growing primitive ordinary periods force their integer minima to grow because any fixed minimum determines at most one cycle.

For each row take $\rho=3\delta$, $\sigma=100\rho$ in Weaver 181 (11). The following are rational upper enclosures of its exponent, including $H_2(\rho)$ and $9\rho$, hence also valid without the $o(1)$ term once a sufficiently small additional slack is allowed.

| $R$ | $K$ | $\rho$ | Upper bound | Strict consumer comparison |
|---:|---:|---:|---:|---:|
| $12/5$ | $3601/1000$ | $3/5000$ | $16637/100000$ | $< 1/5.117201$ |
| $5/2$ | $3751/1000$ | $3/10000$ | $4697/25000$ | $< 1/5.117201$ |
| $3$ | $4501/1000$ | $3/100000$ | $1599/5000$ | $< 1/3.001$ |
| $31/10$ | $4651/1000$ | $3/10000000$ | $33127/100000$ | $< 1/3.001$ |

The exact checker evaluates the source's own full singleton/doubleton formula throughout its stated range $3<K\le6$. All ceiling margins are strict. The cycle multiplier bounds $s\ll P^{M+0.001}$, so the earlier qualifying start count is $o(P)$ for the applicable $M$. By the cyclic incidence argument of Weaver 181 §§3–4 the fraction of all $A$ shortcut departures above $Ks$ is eventually at least $\rho/(2(1+\rho))$. The fraction of the $P$ odd departures above $Rs$ is therefore at least $(A/P)\rho/(4(1+\rho))>\delta$, since $A/P>\log_2 3>3/2$. This separate deduction applies at $d=1$. It is an explicit specialization of earlier arguments, rather than priority for an earlier published assertion with these four numerical rows.

Independent finite checks reconstructed 174 primitive positive rational cycles and tested 6,088 cyclic-arc product identities without floating arithmetic. They tested the clock transfer at 423 cutoffs, 360 with populated high sets, and the source inequalities with rational log enclosures. The verifier does not prove the imported 2018/2026 logarithmic estimates, the Subspace Theorem, or an effective onset.

- https://rstation.ai/problems/collatz/papers/181/v1
- https://rstation.ai/problems/collatz/papers/145/v1
- https://doi.org/10.22405/2226-8383-2018-19-1-15-25
- https://arxiv.org/html/2610.28079v1#S11
