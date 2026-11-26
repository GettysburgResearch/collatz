# Testing both physical endpoints after a long descent

**PROPOSED written theorem with an exact Lean-checked fiber inequality.** Use the ordinary positive shortcut map. Put $R=81^j$, take $7R\le x<8R$, and write $x=81m+r$, $0\le r<81$. The input measure counts these actual children, including their actual parent $m$. Write $a=\log_2(2/\sqrt3)$ and $d=\log_2 R$. Fix $0<\alpha<1$ and set
$$
 h=\lfloor(1-\alpha)d/a\rfloor,\qquad b=\lfloor\alpha d\rfloor .
$$
For $\alpha<1-a=\log_2\sqrt3$, $h$ alone exceeds the number of native independent binary digits by a positive multiple of $d$.

At clock $h$ orient the physical pair so its formal slopes in the original parent $m$ have the order $A,3^s A$. Write the actual values in this order as $z,3^sz+D$, with $D$ a signed integer. Break ties in favor of the parent arm. This definition uses the odd counts on the two paths, including the four factors of three in the initial child's slope. A test may prescribe a different set $B_{s,D}\subset\mathbb Z/2^b\mathbb Z$ for every profile, at every $R$. One may also include the orientation bit in the index.

**Transfer theorem.** If $|B_{s,D}|/2^b\le 2^{-\sigma b}$ for every profile, where $0<\sigma\le1$ is fixed, then
$$
 \#\{x\in[7R,8R): z\bmod 2^b\in B_{s,D}\}
       =O_{\alpha,\sigma}(R^{1-\delta})
       \tag{1}
$$
for some $\delta=\delta(\alpha,\sigma)>0$, independently of the family of tests. The same bound holds after intersecting with **any** set of original sources. Conditional on a source selection of size at least $R^{1-o(1)}$, the selected relative failure is $O(R^{-\delta+o(1)})$. There is no asserted relative bound after conditioning on a rarer selection of unspecified size. In particular (1) is an absolute bound on the actual roots of specified failed edges. It does not replace the transported binary input with a uniform random variable.

**Application to actual missed mergers.** Fix $0<\rho\le1$ and a finite set $K$ of canonical pair states each admitting an absorbing binary word of length at most $L\ge1$. Through the $b$ clocks following $h$, count visits to $K$ at input times $0,\ldots,b-1$ of this continuation. Only $O_{\alpha,\rho,K}(R^{1-\delta'})$ original roots have at least $\rho b$ such visits and still have no physical meeting through clock $h+b$. This also bounds the corresponding portion of the **forever-failed** head edges. The physical meeting here allows independent clocks, because counted absorption supplies one permitted witness. No hypothesis requires the pair to be previously unresolved. It may be imposed by intersection, with the preceding absolute or relative bounds.

## Physical fibers

For a single ordinary arm $n$ in a fixed interval $[cR,CR]$, let $p_i$ be the number of odd inputs before time $i$, and $A_i=3^{p_i}/2^i$. If every input before $t$ is at least $M>0$, multiplying the real step ratios gives
$$
 1\le \frac{T^tn}{A_t n}
     \le (1+1/(3M))^t.                                      \tag{2}
$$
This includes all positive additive corrections. Its division-free upper bound and the same-endpoint comparison below are proved in [PostDescentFibers.lean](PostDescentFibers.lean). If two sources $n,n'$ reach the same endpoint at time $t$ with the same odd count, then $n\le(1+1/(3M))^t n'$ provided the prefix of $n'$ stays above $M$. Thus for $t=O(d)$, $M\gg d$, a fixed endpoint in the selected population comes from at most
$$
 O\big((t+1)(1+tR/M)\big)                                     \tag{3}
$$
sources. Indeed for each odd count every such source lies within $CR[(1+1/(3M))^t-1]=O(tR/M)$ of the smallest one, and there are at most $t+1$ counts. For the parent of a head child, each parent represents at most 81 children. The original source selection may be arbitrary in this calculation.

## A self-contained finite-stage orbit envelope

For every fixed $0<\eta<\alpha/4$, apart from $O(R^{1-c_*})$ actual head sources, **both** arms satisfy
$$
 c R2^{-ai}R^{-\eta}\le T^i n\le C R2^{-ai}R^\eta
 \quad(0\le i\le h).                                           \tag{4}
$$
Constants may depend on the fixed parameters. This is a fixed-altitude instance of Inselmann's stronger Theorem 2.18. We give the short argument to make the exceptional exponent and ordinary multiplicities available for (1). It suffices to prove (4) for a single arm ranging through $[c_0R,C_0R]$ with $c_0>0$ fixed. The child arm ranges in such an interval and the parent has multiplicity at most 81.

Let $k=\max(1,\lceil 2(1-\alpha)/(a\alpha)\rceil)$, $t_i=\lfloor ih/k\rfloor$ for $0\le i\le k$. Write $v_i=1-at_i/d$ and $l_i=t_i-t_{i-1}$. Each block has $l_i\le\alpha d$ for all sufficiently large $R$, and $v_i\ge\alpha$ throughout. Set $e_k=\eta$, $e_{i-1}=e_i^2/200$ for $2\le i\le k$, and $e_0=0$. We may take
$$
                    c_*(\alpha,\eta)=e_1^2/16.                 \tag{5}
$$
Prove the envelope up to $t_i$ with tolerance $e_i$ by induction, starting with the original position at $t_0=0$. A new block is bad if at any $1\le j\le l_i$ the difference of its odd count from $j/2$ exceeds $(e_i/4)d$. On the full block of $2^{l_i}$ binary residues the parity word is uniformly distributed. To recall the elementary bijection, after fixing a word of length $j$, the current state on its lifts is affine in the remaining high quotient with odd coefficient $3^{p_j}$, so its two next parities each occur once among the two binary lifts. Hoeffding's inequality and a union bound give relative bad mass at most
$$
         2l_i\exp(-2(e_i d/4)^2/l_i)
          \le 2l_i R^{-e_i^2/(8\log 2)} .
$$
Here and below $\log$ is natural unless its base is displayed. Before this block, (4) with tolerance $e_{i-1}$ supplies the floor $M\gg R^{v_{i-1}-e_{i-1}}$ and the terminal upper bound $Y\ll R^{v_{i-1}+e_{i-1}}$. Bound the number of bad endpoint integers up to this upper bound by covering it with complete residue periods. Since $2^{l_i}\le R^\alpha\le R^{v_{i-1}}$, this costs $O(R^{v_{i-1}+e_{i-1}})$ times the full-grid relative mass. Formula (3) bounds each endpoint's original multiplicity by $O((1+d)^2 R^{1-v_{i-1}+e_{i-1}})$. The new exceptions therefore number
$$
 O\big((1+d)^3 R^{1+2e_{i-1}-e_i^2/(8\log 2)}\big)
          =O(R^{1-e_i^2/16}).
$$
This calculation also works when $t_0=0$, where the multiplicity is one.

On every remaining block the affine multiplier through its first $j$ steps lies between $2^{-aj}R^{-(\log_2 3)e_i/4}$ and $2^{-aj}R^{(\log_2 3)e_i/4}$. Nonnegativity of the additive correction gives the lower envelope first, including the uniform new floor $\gg R^{\alpha-e_i}$ on block inputs, because $e_{i-1}+(\log_2 3)e_i/4<e_i$. Apply (2) with this floor to get the upper envelope: its correction factor is at most two for all sufficiently large $R$. Constants may grow by two at each of the fixed $k$ stages. The fixed union of exceptional counts is $O(R^{1-e_1^2/16})$. This proves (4) with the advertised exponent.

[Inselmann, *An approximation of the Collatz map and a lower bound for the average total stopping time*, arXiv:2402.03276v3, Theorem 2.18 and Definition 2.6](https://arxiv.org/pdf/2402.03276v3). The cited version is the August 13, 2024 preprint. Its stated star-density means existence of a positive exponent depending on tolerance, without supplying a headline numerical rate. Its Theorem 3.3 also controls single-arm odd counts. The full scalar envelope at the critical clock $d/a$ also follows from the finite-stage proof. For a prescribed $0<\epsilon<1$, run it first at altitude $\alpha=\epsilon/10$ and tolerance $\eta<\alpha/4$. At most $\alpha d/a+O(1)$ clocks remain, the desired lower envelope is already at most one up to a fixed constant, and $T^t(n)+1\le(3/2)^t(n+1)$ bounds every remaining endpoint by $O(R^{\alpha+\eta+\alpha\log_2(3/2)/a})=O(R^{\epsilon/2})$, since $\log_2(3/2)/a<3$. The rounding and fixed-annulus constants are absorbed by the exponent slack. This is an alternative proof of a known scalar result. The paired transfer below still needs a positive altitude for its multiplicity bound.

## The paired restart

On the good population, (4) supplies a floor $M\gg R^{\alpha-\eta}$ for every pre-$h$ state and upper endpoint $Y\ll R^{\alpha+\eta}$ for each arm. Write $p,q$ for the parent and child counts. The two *ideal* endpoints, expressed using the same parameter $m$, are
$$
 A m=3^p2^{-h}m,\qquad A'm=3^{q+4}2^{-h}m.
$$
The two physical endpoints differ from these ideals by relative $O(h/M+1/R)$, by (2) and $x=81m+r$. Order the ideal slopes to get the exact ratio $3^s$, where $s=|p-q-4|\le h+4$. Both slopes times $m$ are $O(Y)$, as are the physical endpoints. Therefore
$$
   |D|=|z_{\rm other}-3^s z|
        \ll Y(h/M+1/R)\ll (1+h)R^{2\eta}.                    \tag{6}
$$
For example, multiplying the lower-slope endpoint's relative error by its larger slope gives an absolute error controlled by the *larger* ideal value, which was already $O(Y)$. This is why no uncontrolled factor $3^s$ occurs in (6).

There are $O((1+h)^2 R^{2\eta})$ tagged profiles, including orientation. For each profile at most $O(R^{\alpha+\eta}2^{-\sigma b})$ positive integers $z\le Y$ represent bad residues, by a complete-period covering; $2^b\le R^\alpha$. Even with the extra restrictions on the pair, each such $z$ has at most $O((1+h)^2 R^{1-\alpha+\eta})$ original head children by (3) on the selected arm and its fixed source multiplicity. Summing gives
$$
 O\big(R^{1-c_*}+(1+d)^4R^{1+4\eta-\alpha\sigma}\big).       \tag{7}
$$
For example take $\eta=\alpha\sigma/16$ and
$\delta=\min\{c_*(\alpha,\eta),\alpha\sigma/2\}$ in (1). A fixed prefactor in the grid estimate $C_0 2^{-\sigma b}$ only changes the implied constant. This method gives an upper bound at the resolution of power-sparse tests and does not identify individual residue probabilities. The estimate for a restricted set follows by inclusion **before** dividing by its original cardinality. A rare permanent-failure selection cannot be treated as a fresh grid.

## Visits and ballistic increments

On a fixed canonical profile $Y=3^s Z+D$, the next base parity is fair on the two binary lifts, with an odd coefficient on the remaining quotient even when orientation switches. This is the exact binary realization in [PR 146, THREE_RAY_UPPER.md, frozen at f431078244e868dc699fad011044f0d5e7f76437](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md). Every residue has a sufficiently large positive lift with both arms positive even for a negative signed offset $D$. The full-grid model is applied **only** to counting the residues defining $B_{s,D}$.

At a visit to $K$ with at least $L$ bits remaining, try the state's absorbing word, padding its trial to $L$ clocks. Skip to the next visit after the trial. On the event of $\rho b$ visits without absorption, at least $\lfloor\rho b/L\rfloor-1$ nonoverlapping trials occur: each trial removes at most $L$ visit times, and fewer than $L$ final times are ineligible. Each complete trial succeeds conditionally with probability at least $2^{-L}$. Iterating the conditional bounds proves a full-grid upper fraction $O(2^{-\sigma b})$, with
$$
           \sigma=-\frac{\rho}{L}\log_2(1-2^{-L})>0 .
$$
This applies to arbitrarily large entering profiles. It does not assert that the pair visits $K$ sufficiently often. In particular the surviving fair level excursions may spend few steps there. Using (7) gives the advertised contribution to genuine failed edges. Its explicit exponent (5) is below $0.16$ throughout this argument. An estimate of the low-occupation remainder and an adequate total count are needed for the $0.84$ global closing criterion.

A second example applies to the signed difference in the odd counts of the two original labeled arms. Given a canonical full-grid history, both arms' next parities are fair, since either base parity and the other arm's parity have odd coefficients. The difference increment has conditional mean zero and absolute value at most one, even if the orientation changes. A maximal Azuma bound gives $2\exp(-v^2 b/2)$ for a change of size at least $v b$ anywhere in the next $b$ clocks, for fixed $0<v\le1$. Equation (7) transfers this with $\sigma=v^2/(2\log2)$. On a true color-discordant edge a positive limiting lower speed can force such growth eventually. No upper bound on the onset time follows here. All clocks $h+b$ in this theorem are below $d/a$ up to bounded rounding, and all constants are for fixed $\alpha$. The sources that start ballistic separation much later are not counted by the ballistic test. Neither consumer proves a fresh conditional law on a rare basin, or universal convergence.

## Earliest possible clocks for the independent-patch test

Fix $0<\alpha<1$ and let the first arm be uniform on any $S_R\subset[cR,CR]$ of cardinality $R^{1-o(1)}$. Uniformly in a second independent arm, with any law, the probability that the first arm at **any** clock $0\le i\le h$ meets the second arm at **any nonnegative clock whatsoever** is $O(R^{-c})$ for some fixed $c>0$. To see this, the number of distinct values of any one full ordinary orbit below $Y$ is $O(Y^{0.98})$, uniformly in the orbit. Here is the one-block version of the range argument in [PR 146, PREFIX_REPRESENTATIVES.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/PREFIX_REPRESENTATIVES.md). Put $l=\lceil\log_2Y\rceil$. The normalized affine intercept formula gives $T^ln\le(4/3)3^p$ for $n\le Y$, where $p$ is its odd count: the normalized additive terms are $2^{i-l}/3^{p_{i+1}}$ with $p_{i+1}\ge1$. For $p\le3l/5$ this gives $O(Y^{(3/5)\log_2 3})$ possible endpoints; for larger $p$ the binary word count is $O(Y^{H_2(3/5)})$, with $H_2$ the binary entropy. Both exponents are below $0.98$. On any nonrepeating orbit, $T^l$ is injective on its states. On an eventually periodic orbit, deleting at most the last $l$ states before entering the cycle makes that restriction injective as well, since the other preperiod states still map to distinct preperiod states and the cycle permutes itself. This proves the asserted uniform bound, including the extra $l$ values.

Now fix the second orbit and take $\eta=\alpha/400$ in (4). At each $i\le h$, set $v=1-ai/d\ge\alpha$. The full list of possible target values on that orbit below the first arm's envelope is $O(R^{0.98(v+\eta)})$. Each individual target has at most $O((1+d)^2 R^{1-v+\eta})$ admissible first origins by (3) using the floor through this $i$. Their product saves at least $0.02\alpha-1.98\eta>0$ in the exponent. Sum over $O(1+d)$ clocks, add the $O(R^{1-c_*})$ exceptional first origins and divide by $|S_R|$. The bound is independent of the second orbit, so averaging preserves it. When both independent samples have the stated size and comparable scales, apply the result in both directions: a macroscopic collision cannot typically be certified with either arm still at the precritical clocks above, regardless of the other's deadline. The sampling law here differs from the deterministic $81m+r,m$ pair. The result permits arbitrarily late collisions in the independent-patch criterion.
