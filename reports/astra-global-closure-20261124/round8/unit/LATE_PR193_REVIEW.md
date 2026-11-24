# Independent review of PR193’s repeated ordered descent

**Verdict.** At PR193 commit **fbe870ec44239e6b6c753bab9d1c7537acfff701**, the repeated descent is supported by the written argument conditional on PR146’s symbolic absorption estimate. It supplies actual smaller representatives of both ordered components on the stated fraction of each conditioned row. A sufficiently large least directed failure necessarily misses the first good checkpoint. [PR193 head proof](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/head/README.md) · [PR146 absorption proof](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md)

### Proof and verification

For fixed $s,r\ge0$, the input pair is $(n,3^s n+r)$ on $2^d\le n<2^{d+1}$. Each $L\le d^{3/5}$ low-bit residue has relative exception at most $e^{-d^{.01}}$. The terminal unit $u\le 2^{d^{.99}}$ satisfies $u\sim n$ and $3u\sim3^s n+r$, with possibly different physical clocks. Each of the $\lfloor\log(d)/12\rfloor$ stages places the next exponent between $.80D$ and $.85D$. In the two grade orders, the inverse denominator $3$ or $9$ places the correct arm at its old state. The other lift state has residual grade gap at most nine. Conditional on the original $t$ low bits, the smaller-grade record is odd-affine in the unrevealed quotient. Its next bits form the complete grid required for symbolic absorption. I checked the use of that grid estimate and retain its pinned native remaining-time theorem as an input.

At a good checkpoint the affine error is at most $E_i=e^{4\lambda_i}$, with $\lambda_{i+1}=8\lambda_i$. For fixed clock, branch, grade, inverse exponent $k$ and source and target dyadic heights $X,Y$, the interval of possible parents of one child contains at most $O(E_i2^kX/(2^L Y))$ admissible parents. The additive endpoint is absorbed by $Y\le X^{.85}$ and $L=o(\log X)$. Every child lies in the single residue $q_0u\equiv-1\bmod 2^k$ for the chosen denominator, so the child exception estimate costs at most $Y2^{-k}e^{-\lambda_{i+1}}$ possible children. Multiplication cancels $2^k$. The clock and parameter menus cost a polynomial in $d$, absorbed by the remaining $e^{-4\lambda_i}$. The shrinking stages use this conditional count in the forced residue.

Independent Lean 4.34.1 replay of **OrderedLanding.lean** passed with warnings as errors. All eight printed inventories contain only **propext** and **Quot.sound**. The verified declarations cover the ordinary lifts, menus and finite synchronous nonmeeting. The probability bound and repeated-transfer induction are written arguments. The reviewed head proof SHA-256 is **78977a273b4e3dff70d602d69b0ce30c36ce235694cc108d055e7cd727f4ac1f**.

### Pointwise contractions at two explicit ternary centers

Let $C$ be the positive basin of one. A forward failure means $u\in C,\ 3u\notin C$ for a positive odd ternary unit $u$. A reverse failure means $u\notin C,\ 3u\in C$. Given any positive $Y$ with $3^h\mid Y+1$, $h\ge1$, the positive $z=2^h(Y+1)/3^h-1$ follows $h$ odd steps to $Y$ and satisfies $z<(2/3)^hY$.

| Failure at $u$ | Prescribed ternary center $\beta$ | Actual bad target $Y$ reached from $z$ | New unit failure $v$ |
|---|---|---|---|
| Reverse | $-1$, $h=v_3(u+1)$ | $Y=u$ | Reverse, $v\le(2351/123)z$ |
| Forward | $-1/8$, $h=v_3(8u+1)$ | $Y=16u+1$, $T^5Y=T(3u)$ | Forward, $v\le(167/27)z$ |

For the forward row the five successive states are $24u+2,\ 12u+1,\ 18u+2,\ 9u+1,\ (9u+1)/2$. The final halving uses odd $u$. Since $Y+1=2(8u+1)$, the all-odd inverse applies. In both rows $z$ lies in the supplied bad component. The last column uses the round-seven directed paths and guarantees the indicated basin orientation of $v$. [Round-seven paths](../../../../research/astra-global-closure-20261124/round7/head/README.md)

PR193’s single-stage sparse criterion uses $\max\{v_2(3u+1),v_2(9u+1)\}\ge cH(u)$ and $3^{v_3(u-\beta)}\ge cH(u)$, with $H(u)=\sqrt{\log(2+u)/\log\log(16+u)}$. At the corresponding center in the table, every sufficiently large failing input therefore yields
$$
v\ll u\,H(u)^{-\log_3(3/2)}.
$$
Both binary alternatives qualify. This pointwise consequence is elementary. Premise M enters PR193’s separate deduction that failures must occur arbitrarily high on these sparse inputs if universal convergence fails. The smaller $v$ can be outside the sparse set. [PR193 prescribed residues and sparse criterion](https://github.com/GettysburgResearch/collatz/blob/fbe870ec44239e6b6c753bab9d1c7537acfff701/research/astra-prescribed-closure-20261124/head/PRESCRIBED_RESIDUES.md)

For any fixed coarse ternary unit class modulo $3^a$, PR193’s simultaneous word theorem can also steer the final representative into one chosen extension modulo $3^\ell$, with $3^\ell\asymp d^{.30}$. To construct the extension for either failure direction, use the round-eight inverse prefix with $p=a$ in reverse or $p=a+2$ forward, $A\le4p$, followed by $b=\ell-a$ all-odd inverse steps. This gives $z/Q<(2/3)^b2^A/3^p$, with $Q=u$ or $Q=(9u+1)/2<5u$. A covered source with the specified failure orientation consequently yields a failure $v\ll_a u\,d^{-.30\log_3(3/2)}$. This composition uses the simultaneous-word exception $e^{-d^{.01}/2}$, the actual bad vertex and the selected direction. [Round-eight ternary steering](../../../../research/astra-global-closure-20261124/round8/unit/README.md)

### A least failure and the paired estimates

If $n$ is a least unit failure in one direction, put $n_0=3n$ forward or $n_0=n$ reverse. Every bad vertex $y$ satisfies $y\ge n/K$, with $K$ the corresponding constant in the table. On the bad arm the round-eight physical product bound gives
$$
\frac{P_t(n_0)}t\ge\log_3 2-
 \frac{\log_3(Kn_0/n)}t-\log_3(1+K/(3n)).
$$
At every first-stage checkpoint $3d/4\le t\le7d/8$, this approaches $0.630929\ldots$ from below as the candidate height grows. PR193 requires both counts to be within $L/2+d^{.60}$ of $t/2$. A sufficiently large least failure violates that gate at **every** such checkpoint. Uniformity over $L\le d^{.60}$ bits leaves $2^{d-L}$ parents per cell. The bound supplies no shrinking stage at that prescribed source. [Critical-profile controls](../../../../research/astra-global-closure-20261124/round8/unit/CRITICAL_PROFILES.md)

Round-eight P1/P3 give many nearby sources sharing exact endpoints and counts. PR193 gives ordered component representatives at subpower height. Under P2’s H, F and cut premises, the flow survives discarding the PR193 exceptional source edges, since their total directed capacity is bounded by a constant times $\sum_d d^{5/4}e^{-d^{.01}/2}<\infty$. The surviving source edges can carry the new representative as a label. Their capacities are measured at the original sources, and multiple sources may give the same representative. [Paired estimates](../../../../research/astra-global-closure-20261124/round8/paired/README.md)
