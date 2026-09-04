# Route 2 — resonance charge forces a quantitative ordinary-source bound

**Status:** `T-ATR-201`, `L-ATR-202`, and `R-ATR-203` are **PROPOSED pending independent review**. The charge-controlled source bound is proved below; a universal charge budget is not. SC*, FC*, and Collatz remain open.

Use the exact map `R`, hard states `H`, integer rank `P`, and arithmetic charge `Q` proved in [Route 1](ROUTE_1_TRANSFER.md). The weight inequality there implies for every ordinary return `x -> y` with `x,y in H`:

\[
P(y)\le\frac12Q(y)P(x).
\tag{1}
\]

The charge belongs to the **endpoint** of the edge. It is not an average over possible parity words.

## 1. T-ATR-201: no-descent charge pressure

Let

\[
x_0=n,\ x_1=R(n),\ldots,x_r=R^r(n)\in H
\]

be one actual ordinary path. Iteration of (1) gives

\[
\boxed{P(x_r)\le2^{-r}P(n)\prod_{i=1}^r Q(x_i).}
\tag{2}
\]

If all these hard states satisfy `x_i>=n`, then

\[
\boxed{\prod_{i=1}^r Q(x_i)\ge\frac{2^r}{u(n)},
\qquad u(n)=\frac{2n+1}{3^{\nu_3(2n+1)}}.}
\tag{3}
\]

Indeed `P(x_r)>=2x_r+1>=2n+1`, while `P(n)/(2n+1)=u(n)`. Substitution into (2) proves (3).

In particular a least nonconvergent hard-state source, if one exists, must pay at least one asymptotic bit of cumulative charge per return:

\[
\liminf_{r\to\infty}\frac1r\sum_{i=1}^r\log_2Q(x_i)\ge1.
\tag{4}
\]

The least such source exists if Collatz fails because every nonconvergent orbit reaches `H`. Every subsequent hard state is also nonconvergent, so minimality supplies the required inequalities. This handles both nontrivial cycles and nonperiodic trajectories. It does **not** assert a positive density of resonant returns: rare very large charges can pay (4).

For a cycle of `r` hard-state returns, (2) instead gives the exact necessary condition `product Q(x_i)>=2^r`, with no initial-core factor.

## 2. A quantitative source-height theorem, not just an ambient count

Consider a shortcut segment of length `N` starting at `n in H`, with

\[
T^j(n)\ge n\qquad(0\le j\le N).
\tag{5}
\]

Fix `C>=1` and `1<=theta<2`. Suppose **every completed hard-return prefix** in this segment obeys

\[
\prod_{i=1}^s Q(x_i)\le C\theta^s.
\tag{6}
\]

Then

\[
\boxed{
N\le
\left(\left\lfloor\frac{\log(Cu(n))}{\log(2/\theta)}\right\rfloor+1\right)
\left(\lfloor\log_2(CP(n))\rfloor+2\right).}
\tag{7}
\]

### Proof

Equations (3) and (6) imply `(2/theta)^s<=Cu(n)` for every completed prefix, hence

\[
s\le\left\lfloor\frac{\log(Cu(n))}{\log(2/\theta)}\right\rfloor.
\tag{8}
\]

Moreover (2) and (6) give `P(x_s)<=CP(n)(theta/2)^s<=CP(n)`. Every hard-state source in the segment consequently has `2x_s+1<=CP(n)`. Route 1's explicit return-length bound makes each full return, including the full extension of the last unfinished return, at most `floor(log_2(CP(n)))+2` shortcut steps long. There are at most the number in (8) of completed returns, followed by at most one unfinished block. This proves (7). Since `n>=4`, the no-descent condition prevents an unnoticed terminal visit to 1 inside the segment.

For fixed `C,theta`, (7) is `O((log n)^2)`, using `u(n)<=2n+1` and `P(n)<(2n+1)^2`. Therefore the least source of a length-`N` segment satisfying **both** (5) and (6) is at least `exp(c sqrt(N))-1`, after adjustment of constants. A polynomial startup budget `C=P(n)^A` for fixed `A` still gives a quadratic logarithmic duration bound.

This is a genuine bound on **one ordinary source**. It is not a bound on the least source of all supercritical words unless (6) is proved for all those words. Only a terminal product bound would prove (8); the prefixwise hypothesis is needed to bound the intermediate heights and the unfinished block in (7).

## 3. How this interfaces with SC* and the first-crossing envelope

For a parity word with `j` steps and `q` odd steps,

\[
T^j(n)=\frac{3^q n+A_w}{2^j}=C_j n+E_w,
\qquad E_w\ge0.
\tag{9}
\]

All-prefix coefficient supercriticality implies (5). Thus (7) rules out all arbitrarily long all-supercritical realizations in the charge-controlled subclass. A universal budget (6), or a suitable substitute for the product of charges, would provide the missing quantitative fixed-source theorem.

At a first coefficient crossing `C_j<1`, a non-descending endpoint forces

\[
n\le\frac{E_w}{1-C_j}.
\tag{10}
\]

The older source-envelope program compares this upper bound with the least source of a supercritical prefix. The new interface is a source-dependent duration bound that can be compared to the actual envelope **when its charge hypothesis is established**. No claim is made that the bound already applies to every envelope candidate. Nor does qualitative finite stopping alone establish the required moving-box comparison.

There is also an exact endpoint constraint. Suppose a shortcut word begins and ends at hard states, comprises `r` returns, and ends at `s=n+d`. Put `h_0=nu_3(2n+1)` and `h_1=nu_3(2s+1)`. Then

\[
(2n+2d+1)^2
\le 2^{-r}\!\left(\prod_{i=1}^rQ(x_i)\right)
3^{h_1-h_0}(2n+1)^2.
\tag{11}
\]

If the coefficient on the right is less than 1, `d>=0` is impossible. At a first crossing, preserve the source convention

\[
A_w=(2^j-3^q)n+2^j d;
\tag{12}
\]

the endpoint convention instead has `3^q d`. Formula (11) is an additional arithmetic restriction on that **same** source and displacement; it is not a replacement for complete-denominator compatibility.

## 4. L-ATR-202: many endpoint carry jets are fixed by the finite word

The endpoint charges can sometimes be certified without knowing the initial ordinary high quotient. This is exact divisibility, not a fresh-parity assumption.

Let `w` have affine data `(j,q,A)`, so `s=(3^q n+A)/2^j`. Define

\[
Z=2A+2^j.
\]

If `h=nu_3(Z)<q`, then **every positive source realizing the word** has

\[
\nu_3(2s+1)=h.
\tag{13}
\]

If in addition `h>=1`, set

\[
W=2^{h+1}Z-3^h2^j.
\]

When `W!=0` and `nu_3(W)<q`, its second carry is fixed as well:

\[
\boxed{k(s)=\nu_3(W)-h.}
\tag{14}
\]

Here the endpoint is required to be in `H` before `Q(s)` is used.

### Proof

First,

\[
2s+1=\frac{2\,3^q n+Z}{2^j}.
\]

The first summand in the numerator is divisible by `3^q`; if the valuation of `Z` is smaller, the sum has exactly that valuation. Next multiply the expression defining the second carry by `2^j3^h`:

\[
2^j3^h\left(2^{h+1}\frac{2s+1}{3^h}-1\right)
=2^{h+2}3^q n+W.
\]

Again the stated strict valuation inequality freezes the numerator's valuation; subtracting the denominator valuation `h` proves (14). The integer `W` is automatically divisible by `3^h`. If either strict inequality fails, the jet is **unfrozen** and may depend on `n`; do not substitute the expected or generic valuation.

The checker finds 28,666 eligible source/word endpoint pairs in its fixed pilot and separately records 11,187 unfrozen pairs. These are regression counts, not a distribution theorem.

## 5. R-ATR-203: two attempted global budgets are false

I tested the simple candidate

\[
\prod_{i=1}^rQ(x_i)\le P(n)^A(3/2)^r.
\tag{15}
\]

It fails even at small ordinary sources.

For `A=1`, the path

```text
31 -> 121 -> 91 -> 103 -> 175
```

has

\[
\frac{\prod_{i=1}^4Q(x_i)}{(3/2)^4}
=\frac{129140163}{262144}>441=P(31).
\]

For `A=4`, the path

```text
121 -> 91 -> 103 -> 175 -> 445 -> 334 -> 283
    -> 319 -> 1822 -> 2308 -> 577 -> 433
```

has

\[
\frac{\prod_{i=1}^{11}Q(x_i)}{(3/2)^{11}}
=\frac{8862938119652501095929}{2199023255552}
>3486784401=P(121)^4.
\]

The first counterexample already lies in the relevant no-descent setting. The second refutes a budget proposed for all trajectories, but **does not** refute its restriction to no-descent prefixes: its first return `121 -> 91` descends. Neither example refutes every exponent `A`, every rate `theta<2`, or a better charge. In particular a no-descent-only budget with `A=4` remains undecided by these countertests. Neither tested global inequality may be used to instantiate (7).

## 6. Next missing inequality

The usable target is an **amortized resonant-excursion bound**, rather than a universal estimate on isolated incoming charges. Route 3 proves that arbitrarily large single charges can be repaid by adaptive physical blocks. Replacing the crude product in (2) by such a certified excursion budget may yield a much stronger source bound.

A successful next result should either bound that budget on every least-counterexample path, or show that a path violating it cannot satisfy the source/end and full-denominator constraints. Until then, this file proves a quantitative exclusion of a specified infinite subclass, not SC* or FC*.
