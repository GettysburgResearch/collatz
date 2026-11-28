# Quantitative timed passage to an arbitrary odd floor

Write \(S(n)=n/2\) for even \(n\) and \(S(n)=(3n+1)/2\) for odd \(n\). Let \(V_R(n)\) be the first **odd** physical iterate at most \(R\), including the source, and let \(t_R(n)\) be its native shortcut time. Both take a cemetery value on failure. Put \(g=1-H_2(\log_3 2)+1/351\). For an absolute \(C\), every \(0<b<g\), and uniform positive \(n\le Z\), the following written consequence of Weaver 102 holds for \(2\le R\le Z\):
\[
             \Pr(t_R(n)>C\log(2Z))\ll_b R^{-b}.                       \tag{1}
\]
The constants are independent of both physical scales. The bound includes finite late arrivals and failures. Prior arbitrary-diverging-threshold theorems give logarithmic-time passage with a vanishing exceptional fraction. We use Weaver's quantitative native bad-stage and finite all-event first-landing estimates to keep a power of the requested floor without a factor growing in \(\log Z\). [Weaver, Paper 102, Theorem 1 (1)–(3), Input I (5)–(6), Lemma 3](https://rstation.ai/problems/collatz/papers/102) · [Prior logarithmic-time threshold results and comparisons](../TERMINAL_WINDOWS.md)

## Physical landing bounds at intermediate floors

Set \(r=999999/1000000\) and \(c=15/14\), the constants of Weaver's Input I. A positive integer \(v\) of binary rank \(j=\lfloor\log_2 v\rfloor\) is good if within \(\ell(j)\le cj\) shortcut steps it reaches a value at most \(2^{\lfloor rj\rfloor}\). The number of other integers of rank \(j\) is \(O((j+1)2^{(1-g)j})\). Bounded ranks are absorbed by increasing the constant.

Take a floor \(Q=2^k\) and a next rank \(k'\) with \(\lfloor rk\rfloor\le k'<k\). An odd \(v\le Q\) already at most \(2^{k'}\) costs zero steps. Any higher good \(v\le Q\) physically crosses \(2^{k'}\) within \(ck\) steps. Strip the powers of two from that crossing state using at most \(k\) more physical steps. The first odd crossing of \(2^{k'}\) costs at most \((c+1)k\). Let \(A_Q\) be the complete set of odd \(v\le Q\) failing this time bound, including infinite times. Summation of the rank counts gives \(|A_Q|\ll(k+1)Q^{1-g}\), uniformly in \(k'\).

Weaver's finite Theorem 1 gives, from **each** uniform odd octave \([Y,2Y)\), \(Y\ge Q\),
\[
 \Pr(V_Q\in A_Q\text{ or }V_Q=\dagger)
 \ll \exp(C_1\sqrt{\log Q})\big(|A_Q|/Q+Q^{-g}\big)
 \ll_b Q^{-b}.                                                        \tag{2}
\]
This uses the original first landing at each floor, with the original source law.

For clarity (2) transfers to a uniform all-positive prefix through \(Z\ge Q\). On odd inputs at most \(U\), \(U\ge Q\), partition the range above \(Q\) into octaves with left endpoints \(Q,2Q,\ldots\), majorizing the last partial octave by its full count. The total count of exceptional odd inputs is \(O_b(UQ^{-b})\), since below \(Q\) only \(A_Q\) can be exceptional. For all-positive inputs write \(n=2^d v\), \(v\) odd. For \(U_d=Z/2^d\ge Q\) sum this bound to get \(O_b(ZQ^{-b})\). For \(U_d<Q\) use \(\min(U_d,|A_Q|)\); these sum to \(O(|A_Q|(1+\log Q))=O_b(Q^{1-b})\), also when \(A_Q\) is empty. Initial divisions by two preserve the landing label.

Take \(k_0=\lceil\log_2 Z\rceil\), \(l=\lfloor\log_2 R\rfloor\), and, while \(k_i>l\), set \(k_{i+1}=\max(l,\lfloor rk_i\rfloor)\). At \(Q_0=2^{k_0}\) the odd part of each source lands immediately; its probability of being bad obeys the same bound by enlarging the prefix to \(Q_0\le2Z\). Subsequent floors \(Q_i\le Z\) obey (2) under the original prefix. The union of the exceptions has probability \(O_b(\sum_{k\ge l}2^{-bk})=O_b(R^{-b})\), because the integer ranks strictly decrease. On the complement the passage times between successive odd floors telescope along the same ordinary path, allowing immediate landings at several consecutive floors. Their sum is \(O(\sum_{i:k_i>l} k_i)=O(k_0/(1-r))\), since before the final step the ranks decrease by a factor at most \(r\). Initial divisions to the first odd state cost at most \(k_0\). Crossing \(2^l\) suffices for crossing \(R\), proving (1).

## A native clock window with finitely many terminal times

Write \(L=\log Z,\ H=L^{1/3},\ a=\log 2,\ \kappa=\tfrac12\log(4/3)\). Assume \(H\) large and \(\log(2R)\le H/2\). For \(1\le B\le\sqrt L\), uniformly in \(Z,R\),
\[
 \Pr_Z\big(t_R\notin[\kappa^{-1}L-CB\sqrt L,\ \kappa^{-1}L+CB\sqrt L]\big)
 \ll_{b,A} R^{-b}+H^{-A}+ e^{-c_2 B^2}.                              \tag{3}
\]
An infinite clock is outside this interval.

Use the fair auxiliary log-size walk \(L_j=L-ja+\log3\,\mathrm{Bin}_j\) with iid Bernoulli increments in its count, and \(\mathcal T=\inf\{j:L_j\le H\}\). Given the walk through \(\mathcal T\), choose a fresh integer \(m\) uniform through \(e^{L_\mathcal T}\in[e^H/2,e^H]\). In total variation the original \((t_R,V_R)\) differs from \((\mathcal T+t_R(m),V_R(m))\) by \(O_A(H^{-A})\). To verify uniformity in the floor, use the [complete native signed transfer](../phase2/NATIVE_BINOMIAL_TRANSFER.md) and its [integer first-clock version (3)](../phase3/NATIVE_CLOCK_ATOMS.md). On an original octave \([U,2U)\) above \(R\) choose \(h=\lfloor c_0\log(U/R)\rfloor\) physical steps with \(c_0\) small. Every state through \(h\) is at least \(U2^{-h}>R\), so the whole vector is obtained by sending the true endpoint \(z\) to \((h+t_R(z),V_R(z))\). The signed starting-trit bound after \(h\) is \(O_A((1+\log(U/R))^{-A})\). For a source prefix at scale \(e^x\), \(x>\log R\), drop starts below \(\sqrt{e^xR}\) and sum the rest with geometric octave weights. In the direct first-step recurrence both branches shift the clock by one. Odd boundary coordinates \(n\le R\) cost \(O(R/e^x)\). The full-vector residual has norm \(O_A((1+x-\log R)^{-A})\) whenever \(x\ge\log R+2\). Above the stopping line this is uniformly \(O_A((1+x)^{-A})\). Sum these errors with the unit-strip occupation bound (5) of the native transfer, first stopping at a finite horizon, then letting it tend to infinity. The fair walk has negative drift. This proves the asserted TV estimate.

The fair passage \(\mathcal T\) has both tails \(O(e^{-c_2B^2})\) about \((L-H)/\kappa\) at width \(CB\sqrt L\) for \(B\le\sqrt L\). For the early tail use the maximal Hoeffding bound on centered partial sums up to the first proposed date. For the late tail use the one-time bound at the last proposed date on the event of no crossing. Both dates are \(O(L)\); a negative early date has empty event. Round dates at a bounded additive cost. At the stopped height (1) gives \(t_R(m)\le C'H\) outside probability \(O_b(R^{-b})\), uniformly in the random cutoff. Since \(H\le\sqrt L\), this proves (3).

For each positive odd target \(y\), let \(\tau_y(n)\) be its first physical visit. For finite \(\tau_y(n)\) and finite \(t_R(n)\),
\[
 \tau_y(n)-t_R(n)\ \in\
 \{\tau_y(v): v\le R,\ v\text{ odd},\ \tau_y(v)<\infty\}
 \ \cup\ \{-t_R(y):t_R(y)<\infty\}.                                   \tag{4}
\]
If the target is reached after the first floor entry, the remaining first time is \(\tau_y(V_R(n))\). If reached before, the segment from its first visit to the floor has exactly \(t_R(y)\) steps. Equality of the dates gives zero. The argument applies on cycles as well. There are at most \(R+1\) centers in (4). Their magnitudes can be arbitrarily large; (3) controls the common added clock without a maximum total stopping time for the first \(R\) integers.

[FirstHitClockCentres.lean](FirstHitClockCentres.lean) proves the first-visit shift, uniqueness, two temporal orders, and signed-center formula from finite orbit composition. The [exact ordinary control](check_first_clock_centres.py) checks both temporal orders, each observed product mark, and integer spacing at each fixed clock/grade pair. The analytic inputs to (1)–(3) are written source-qualified deductions.
