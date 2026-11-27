# Paid ordinary mergers for each of the first 512 delayed parents

**Exact finite computation with a kernel-checked transport theorem.** For every integer $1\le k\le512$, set $b=18k$, $m=12\cdot2^b-1$, $H=b+4$, $M_t=2^t-1$ and $P_t=3^t-1$. Under the ordinary shortcut map $T$, the records give an exponent gap $g$ and suffix length $j>0$ satisfying
\[
 T^{H+j}P_m=T^{H+j}P_{m-g},\qquad
 Q_{H+j}(P_{m-g})=g+Q_{H+j}(P_m).
\]
Every record has $11\le g\le4803$, $1\le m-g<m$ and $g\ge3$. Thus every record pays for a strictly earlier source under the two general leastness implications at $81z+271=128\cdot2^m$. Combining the full ascents, the meeting clocks from $M_m$ and $M_{m-g}$ are $m+H+j$ and $m-g+H+j$, respectively. The original $z$ takes seven more initial clocks to $M_m$. Consequently none of these 512 preassigned $z$ can be the least canonical reverse disagreement.

The kernel proves the universal inference from a passing finite record to $G(z)$, where $G$ denotes ordinary reachability of one. Python independently verifies the existence hypotheses for each of the 512 rows. The formal file does not evaluate the complete table. PR 192 previously supplied paid comparisons for the first thirty parameters on this very cofactor-one family. The present computation extends the consecutive verified range through 512. The [valuation-window theorem](POST_VALUATION_WINDOW.md) explains why a fixed suffix budget cannot close every subsequent parameter by this mechanism. [Transport theorem](DelayedBatch.lean) · [Complete finite records, clocks and grades](DELAYED_BATCH_CONTROLS.json) · [Reproducer](check_delayed_batch.py) · [Prior thirty parents](https://github.com/GettysburgResearch/collatz/blob/ed7a6fe30b8602407f77855ceb74ce0489ce9c10/research/astra-unconventional-20261126/descent/PAID_DELAY_REPAIRS.md)

| $k$ | Earlier exponent gap $g$ | Suffix $j$ | Total postpeak clock $H+j$ | Native and earlier odd counts |
|---:|---:|---:|---:|:---|
| 1 | 11 | 48 | 70 | 24, 35 |
| 2 | 21 | 64 | 104 | 31, 52 |
| 3 | 31 | 128 | 186 | 54, 85 |
| 80 | 341 | 70,576 | 72,020 | 35,650, 35,991 |

The $k=80$ row has the largest suffix and total clock in this certificate. The listed times are successful witnesses and need not be earliest.

## Independent replay from the ordinary exponential source

The only per-parameter inputs are $q=g+1$ and $j$. The checker reconstructs $m,H$, the earlier exponent, and the two legal words. Define $U_b=(3^{12\cdot2^b}-1)/2^{b+4}$. To obtain the residue of the earlier power modulo $2^{H+j}$ use
\[
 R=\left[(1+2^H U_b)\,3^{-q}\right]_{2^{H+j}}.
\]
This is $3^{m-g}\bmod2^{H+j}$ by the original positive source formula. The two replayed starts $R-1$ and $3^gR-1$ are positive. At each block the low twelve bits determine the physical shortcuts, and the nonnegative high quotient is transported by the exact power of three. The final short block uses its exact remaining length.

For each trajectory and each word block the verifier updates the full signed carry $C$. Starting from $x=A-1$ it also checks the complete integer identity $2^h T^h(x)=3^{Q_h(x)}A+C$ at the final $h=H+j$. The two complete carries agree, the two physical endpoints agree, and the earlier grade exceeds the native grade by exactly $g$. These are integer equalities before reduction. They imply equality at the full positive powers by the parity-cylinder lift. The gap-four theorem supplies $G(M_{m-g})$ under leastness, and the actual merger returns $G(M_m)$ and $G(z)$. [Leastness bridge](OFFSET_FOUR.md)

For efficiency, set $a=\min(b,\max(1,\lfloor\sqrt j\rfloor))$, $u=U_a$ and $n=2^{b-a}$. The calculation of $u$ uses the elementary squaring recurrence modulo $2^j$. If $a<b$, direct binomial expansion gives
\[
 U_b=\sum_{i=1}^{n} \binom{n-1}{i-1}
       \frac{2^{(a+4)(i-1)}u^i}{i}.
\]
For $i\ge2$, the available power of two after division by $i$ has exponent at least $(a+3)(i-1)$. Terms above the implemented cutoff vanish modulo $2^j$. Since $n$ is a power of two, updating the odd coefficient $\binom{n-1}{i-1}$ to the next one uses $(n-i)/i$ with equal binary valuations in numerator and denominator whenever $i<n$. Only an odd inverse is used. The reproducer cross-checks this implementation against direct modular powering at six small controls.

The discovery search propagated the signed states of $3^{-q}-1$ to clock $H$, merged identical compensated affine states, and tested continuations at the native unit. The verifier uses neither these signed states nor the search's visited endpoints and grades. The 512 rows do not supply a decreasing transition from an arbitrary subsequent $k$.
