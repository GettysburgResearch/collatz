# Explicit slow terminating families beyond the published width-22 coefficient

For the shortcut clock $\tau$ to one and every sufficiently large real $X$, the positive integers in $[X,2X)$ include at least $X^{1/4750}$ terminating $m$ with $\tau(m)>14.92\log m$. They also include at least $X^{1/950}$ terminating $m$ with $\tau(m)>14.9\log m$. The two counts have separate thresholds. This consequence imports Wren's published width-22 certificate and Weaver's stationary transfer. Neither a regeneration of Wren's large original tables nor an effective initial octave is supplied here.

## Use all of the reported rational slack

Wren 154/v2, Section 2 and Table 1, use $D=q=10^6$, an integer bias divided by $D$, and an inverse step reward of zero or one. Across all 20,920,706,406 unit rows the minimum of $3Dq[r-569908/10^6+PV-V]$ was 90,000,000 in both of Wren's exact verifiers. The original certification deliberately retained thirty numerator units of reserve (Section 3.1). Therefore the same bias and policy satisfy the exact unscaled lower drift with
$$
 \theta=569908/10^6+90{,}000{,}000/(3Dq)=569938/10^6.
$$
This uses the integer slack rather than the reported floating gain bracket. Its span is $\Delta=13.537636$. Weaver 127, equations (41)–(45), regroup the run to the first odd action into a legal gap $e_\pi\le R=\lfloor\Delta/\theta\rfloor+1=24$. On the Haar tail of each supplied window the grouped bias satisfies $1-\theta e_\pi+\mathbb E V(DX)-V(X)\ge0$. [Wren 154/v2, §§2–3](https://rstation.ai/problems/collatz/papers/154/v2) · [Weaver 127, §11](https://rstation.ai/problems/collatz/papers/127/v1).

## Perturb by an alternate label

At each unit source exactly two of the six labels $1,\ldots,6$ are legal, since $2$ generates the units modulo nine and the two legal images require $2^e x\equiv4,7\bmod9$. Thus exactly eight of the labels $1,\ldots,24$ are legal. Choose the cheapest one different from $e_\pi$. Let $R'$ choose it with probability $999/1000$ and choose uniformly among the seven alternatives to $e_\pi$ with the remaining probability $1/1000$. The chosen alternate can occur in the latter choice as well. This kernel has conditional mean at most $6.018$, positive probability for every alternate and zero probability for the deterministic baseline. The full kernel $(1-\epsilon)D+\epsilon R'$ assigns positive probability to every legal label up to 24 and depends on at most 22 trits.

Under Weaver 127 Theorems 5–7 this full kernel has the finite-density stationary law used in (45), empirical convergence from integer one, positive real growth $g=A\log2-\log3$, and terminating octave counts with any $c<A/g$ and $\eta<\beta/g$. Here $A$ is the stationary mean gap and $\beta$ is the conditional label entropy. Integrating (45) and using stationarity gives
$$
 A\le A_+=(1-\epsilon+\epsilon\Delta)/\theta+6.018\epsilon.
$$
Indeed $(1-\epsilon)\mathbb E(DV-V)=\epsilon\mathbb E(V-R'V)\le\epsilon\Delta$. The event that the executed label is an alternate is exactly the perturbation coin, so at every row
$$
 \beta\ge h_2(\epsilon)=\epsilon\log(1/\epsilon)
                    +(1-\epsilon)\log(1/(1-\epsilon)).
$$
The ratio $A/(A\log2-\log3)$ decreases on the positive-growth domain and $g\le A_+\log2-\log3$. The exact rational bounds in `check_window_transfer.py` establish the strict inequalities $A_+>c(A_+\log2-\log3)>0$ and $h_2(\epsilon)>\eta(A_+\log2-\log3)$ for both rows.

| $\epsilon$ | $A_+$ exactly | $c$ | $\eta$ |
|---|---:|---:|---:|
| $1/575000$ | $143753991880721/81928587500000$ | $14.92$ | $1/4750$ |
| $1/100000$ | $25003991880721/14248450000000$ | $14.9$ | $1/950$ |

Wren's printed Corollary 2 supplied every coefficient strictly below $14.91663502526\ldots$, including the explicit pair $(14.9,1/50000)$. At that same coefficient the new count exponent is more than $52$ times as large. The $14.92$ coefficient exceeds the previously printed endpoint within this particular transfer. This is a comparison to the cited corollary. The scalar checker independently enumerates the 48 cap-24 row/baseline combinations and uses rational logarithm enclosures. Wren's original 89 GB all-row verification remains an external input.

For any fixed finite drift certificate of the same type, a positive perturbation supported on alternate labels gives $A_+(\epsilon)=1/\theta+O(\epsilon)$ and $\beta\ge h_2(\epsilon)$. Thus at coefficients $c=c_0-d$ approaching $c_0=(\log2-\theta\log3)^{-1}$ from below there is an attainable count exponent at least $k\,d\log(1/d)$ for some certificate-dependent $k>0$ and all sufficiently small $d>0$. Indeed choose $\epsilon$ a sufficiently small fixed multiple of $d$ in the smooth positive-growth expression for $A_+/(A_+\log2-\log3)$, and use the binary entropy lower bound. Separately, `STRICT_FINITE_WINDOW_IMPROVEMENT.md` proves that the optimum strictly exceeds every finite-window slope. Therefore Weaver's Corollary 12 even attains this individual $c_0$ with some positive count exponent, without calculating that exponent or attaining the universal limiting coefficient.
