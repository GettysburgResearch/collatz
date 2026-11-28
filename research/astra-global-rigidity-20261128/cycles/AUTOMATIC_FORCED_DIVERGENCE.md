# A binary-automatic force-divergent set and its exact growth rate

Vasilyev asks whether every force-divergent set contains an entire tail of an upward chain. The trureturing project already published a negative answer with a Lean proof, using doubly separated omissions chosen far along successive upward chains. Vasilyev’s own §6.5 uses two forced upward successors after any downward step for a periodic example. The construction here uses an explicit binary language. Its omitted vertices have positive lower density, every pure upward chain visits them with the same limiting frequency, and the map of the forced set itself has an explicit growth rate and bounded discrepancy in its count of downward steps. [Vasilyev, §7, Question 7.7](https://arxiv.org/html/2611.20344v2#S7.Thmtheorem7) · [trureturing, force-divergence refutation and Lean source](https://www.trureturing.org/research/vasilyev-2026-force-divergence-question-7-7/)

On positive integers put \(U(x)=\lceil3x/2\rceil\) and \(D(x)=\lceil x/2\rceil\). The map \(T_S\) takes the upward step exactly on \(S\). Set
\[
 H=\bigcup_{j\ge3}[4^j,5\cdot4^j/4)\cap\mathbb N,
 \qquad A=\mathbb N\setminus H.
\]
The base-two representations of elements of \(H\), written without leading zeros, have odd length at least seven and begin with 100. A finite automaton recognizes this language.

## Growth for all supersets

For \(h\) in the band with left endpoint \(B=4^j\), both \(D(h)\) and \(U(D(h))\) lie strictly between \(5B/16\) and \(B\). Indeed the first is at least \(h/2\), the second is at least the first, and the second is at most \((3h+5)/4<B\) since \(B\ge64\). The earlier bands end at or below \(5B/16\) and the later bands begin at or above \(B\). A downward departure under any \(T_S\), \(S\supseteq A\), therefore has two forced upward successors. Each three-step block has upward count at least two, giving \(8T_S^3(x)\ge9x\). All orbits of every such map tend to infinity. The local arithmetic, exclusion from all bands and uniform three-step bound are statements in [GuardedHoles.lean](GuardedHoles.lean).

## Frequency on every pure upward chain

For \(u_n=U^n(x)\), the normalized sequence \((2/3)^n u_n\) converges to a number \(K_x\in[x,x+1]\). Indeed \(u_{n+1}=3u_n/2+e_n\), where \(0\le e_n\le1/2\), and the normalized increments are bounded by a convergent geometric series. Hence
\[
 \log_4 u_n=n\log_4(3/2)+\log_4 K_x+o(1).
\]
The coefficient \(\log_4(3/2)\) is irrational by unique prime factorization. The fractional parts are equidistributed, as follows directly from the geometric sum for each nonzero integral Fourier mode and Weyl's criterion. An additive error tending to zero preserves these mode limits. Membership in \(H\) for \(u_n\ge64\) corresponds to the interval \([0,\log_4(5/4))\). For **every** positive \(x\), the upward-chain visit frequency is exactly \(\log_4(5/4)\), excluding a full upward tail in \(A\).

The lower and upper natural densities of \(H\) are \(1/12\) and \(4/15\). Each complete band has \(4^j/4\) integers. At \(B-1\) the count from the earlier bands is \(B/12+O(1)\), and at \(5B/4-1\) it is \(B/3+O(1)\). The fraction rises on each band and falls across each intervening gap.

## Exact dynamics for the map of the forced set

Start at any \(x\). Until the first visit to \(H\), the actual map \(T_A\) follows the pure upward chain, so this visit occurs in finite time. From a hole \(h\in[B,5B/4)\), put \(z_i=U^i(D(h))\). The next hole in the actual orbit is exactly one of the following.

| Condition | Next hole | Native steps | Band of the next hole |
| --- | --- | ---: | --- |
| \(4z_2<5B\) | \(z_2\) | 3 | \([B,5B/4)\) |
| \(4z_2\ge5B\) | \(z_5\) | 6 | \([4B,5B)\) |

The first two sites following \(h\) are protected by the preceding argument. We have \(9h/8\le z_2\le(9h+19)/8<4B\). In the second case \(z_2,z_3,z_4\in[5B/4,4B)\), since \(z_4\le(81h+211)/32<4B\). Finally \(z_5\ge(27/8)z_2\ge135B/32>4B\) and \(z_5\le(243h+665)/64<5B\). The inequalities at the two outer ends use \(B\ge64\). The half-open convention covers a hit at the upper boundary of the current band.

Write \(h_m\) for the successive holes, \(B_m\) for their band bases, and \(y_m=\log(h_m/B_m)\). Put
\[
 a=\log(9/8),\qquad b=\log(256/243).
\]
On a short return, \(B_{m+1}=B_m\) and \(h_{m+1}=(9/8)h_m+O(1)\). On a long return, \(B_{m+1}=4B_m\) and \(h_{m+1}=(243/64)h_m+O(1)\). Accordingly, the increments of \(y_m\) are \(a+O(1/h_m)\) and \(-b+O(1/h_m)\), respectively. Each return increases the hole value by a factor at least \(9/8\), so the errors sum absolutely. The values \(y_m\) all lie in the bounded interval \([0,\log(5/4))\). If \(L_m\) counts the long returns among the first \(m\), telescoping gives
\[
       a(m-L_m)-bL_m=O(1),
       \qquad L_m=\frac{a}{a+b}m+O(1).
\]
The actual clock from the first through the \((m+1)\)-st hole is \(3m+3L_m\). Each return has exactly one downward departure and the final incomplete return costs at most five steps. Thus the number \(d_n\) of downward departures among the first \(n\) steps from \(x\) satisfies
\[
 d_n=\frac{a+b}{3b+6a}\,n+O_x(1).
\]
Also \(B_m=B_0 4^{L_m}\), while the states within each return stay within constant factors of its initial hole. Consequently
\[
 \log(T_A^n(x))=\frac{a\log4}{3b+6a}\,n+O_x(1).
\]
The down-step frequency is approximately \(0.1968597201\), and the multiplicative growth factor is approximately \(1.2082736441\) per step. The explicit rate belongs to \(T_A\). The universal statement for every permitted superset is the three-step lower bound.

## Verification and attribution boundary

[GuardedHoles.lean](GuardedHoles.lean) proves the generic separated-hole guards, the concrete exclusion from all automatic bands, the every-three-step growth inequality, and the exact three-or-six-step return alternatives. The infinite-chain equidistribution and logarithmic telescoping above remain written proofs. The [finite controls](check_guarded_holes.py) independently compare the binary language with the band rule, check all actual first returns in the stated crop, and exercise arbitrary permitted gates for a finite separated-hole schedule. The corresponding [sparse construction](FORCED_DIVERGENCE_WITHOUT_CHAINS.md) expressly credits the prior trureturing answer to Question 7.7. Neither construction uses the ordinary Collatz branch rule.
