# Final proposal: a quantitative loss estimate on the same ordinary sources

**Status: the proposed arithmetic estimate below is unproved.** Its sufficiency follows from the exact principal-source bookkeeping. It is more specific than asking for uniform integrability, which in this setting is already equivalent to the missing first-moment conclusion. The new fractional theorems do not imply this estimate.

## 1. A finite continuation loss, with future births accounted for

Fix the original slope $a=7/4$. Let $\mathcal M_n$ be the finite set of principal odd sources of accepted length-$n$ words, and put

$$
J_n=\sum_{m\in\mathcal M_n}\frac1m.
$$

For each such *same* source, continue its actual ordinary orbit through odd clock $2n$. Define the lost mass

$$
D_{n,2n}=\sum_{m\in\mathcal M_n}\frac1m\,
\mathbf1\{\exists j\in(n,2n]:4A_j(m)>7j\}.
$$

Every summand is a finite, decidable ordinary calculation. An old principal source stays principal as its dyadic modulus increases. It survives precisely when its continued prefix still passes the gate. New principal sources can appear, but the sibling reciprocal bound from PR201 bounds the new mass on the step from depth $r$ to depth $r+1$ by the original accepted-word probability, at most $\gamma^r$, where

$$
\gamma=\frac78\left(\frac76\right)^{3/4}<1.
$$

To check the factor: nonprincipal sibling sources have the form $m+2^{A+1}j$ with $j\ge1$. Their inverse sum is at most $2^{-A-1}\sum_j1/j\le2^{-A}$ over the permitted sibling indices. Summing this original word probability over accepted parents gives the asserted birth bound. Consequently

$$
J_{2n}\le J_n-D_{n,2n}+\frac{\gamma^n}{1-\gamma}. \tag{1}
$$

**Proposed quantitative target.** Prove that there are constants $c>0$ and $k_0$ such that

$$
\boxed{D_{2^k,2^{k+1}}\ge\frac{c}{k+1}J_{2^k}
\quad\text{for every }k\ge k_0.} \tag{2}
$$

This permits individual sources to survive a long time; it asks for a definite weighted loss across the whole finite retained population. It also keeps the source and gate coupled, unlike the failed marginal Holder route. It is a quantitative conjecture, not a consequence already supplied by the preceding papers.

Let $x_k=J_{2^k}$. Equations (1) and (2) give

$$
x_{k+1}\le\left(1-\frac{c}{k+1}\right)x_k+
\frac{\gamma^{2^k}}{1-\gamma}.
$$

After increasing $k_0$ so the factors are positive, their products are $O((j/k)^c)$. The weighted series of birth errors converges, giving $x_k=O(k^{-c})$. The existing principal-source dominated-convergence theorem then gives $J_n\to0$, hence Collatz. The implication is elementary; the unproved work is (2)'s arithmetic estimate. Abstract extinction alone does not force this rate: a population with only finite lifetimes can have reciprocal tail $1/\log(k+2)$. No strict logical separation from Collatz for this specific map is asserted.

Uniform integrability of $\mathbf1_{W_n}Z_n(0)$ is not offered as a smaller solved target. These random variables already tend to zero almost surely, since the permanent original-word gate has probability zero. Uniform integrability would therefore be equivalent to the missing first-moment vanishing.

## 2. Why varying the gate slope does not bridge the proven endpoint

For the arbitrary-slope theorem put

$$
\epsilon(a)=1-p_c(a)=-\log_2\gamma(a)
\sim\frac{(2-a)^2}{4\log2}\quad(a\uparrow2).
$$

At the certified endpoint the simultaneous-shell exponent is exactly $-\epsilon(a)n$ for *every* total division count $A$. Restricting to $A\le(7/4)n$ does not create a further exponential saving in that bound. Reweighting a fractional moment back to the first power can cost $2^{(7/4)\epsilon n}$, leaving a bound with factor $2^{(3/4)\epsilon n}$ before the polynomial losses. If $n\epsilon\to\infty$, smaller-power vanishing is compatible with permanent atoms. If $n\epsilon$ stays bounded, the old-gate fractional moment is comparable with the first trace, whose vanishing is precisely unresolved.

There is also an unconditional obstruction to uniform vanishing of the *broadening* centered gate itself. The actual odd orbit of $27$ reaches one after 41 odd departures and division total 70. Its exact gap word is

```text
12111122121121112311212111113111422431154
```

The first 41 prefixes have minimum margin $7j-4A_j=2$ and maximum slope $A_j/j=70/41$. Thereafter $A_j=2j-12$. The root independently regenerated this word using integer division. For $a_n=2-1/n$ and all sufficiently large $n$, its entire length-$n$ word passes $A_j\le a_nj$, and $27$ is its principal source. Since $p_c(a_n)=1-O(n^{-2})$, that single original-law centered contribution

$$
2^{-(1-p_c(a_n))(2n-12)}27^{-p_c(a_n)}\longrightarrow\frac1{27}.
$$

Thus a uniform centered extinction theorem as $a_n\uparrow2$ is false even for a source known to terminate. This example does not survive the original $7/4$ gate forever. It identifies exactly the error in changing the gate while trying to preserve the original conclusion.

## 3. An alternative escape-only target from rational closures

For a strict-supercritical shortcut trace with finite correction sum, fix a positive odd integer $m$. A possible arithmetic certificate is a positive primitive rational periodic continuation $z=b/d$ of one prefix of length $n$, in lowest terms with odd $d$, such that

$$
0<|b-md|<2^n. \tag{3}
$$

If that trace is the actual parity trace of $m$, parity coding instead forces $2^n\mid b-md$, contradicting (3). Every hypothetical escaping component supplies a strict-supercritical positive representative by the corrected-height minimizer. Thus existence of (3) for every such trace and every positive odd $m$, with one depth $n$ each, would exclude escape, while a separate cycle argument would still be needed.

No existence theorem of this kind is proved here. The constructed rational cycles have $d=2^{n+o(n)}$ and can approach a chosen real target, but no bound on the *product* $d|z-m|/2^n$ follows. A universal denominator-only saving is already false on broader trace families: the all-odd trace has dyadic source $-1$, and every positive compact rational matching its first $n$ bits satisfies $2^n\mid b+d$, hence $d\ge2^n/(M+1)$ when $0<z\le M$. Any successful denominator argument must retain the relevant positive ordinary information. Pointwise integrality at all fixed primes is also insufficient, as the final all-place construction shows.

This proposal records exact obligations for another attack. It adds no assumed axiom or completed universal Lean theorem.

[PR201 principal bookkeeping](https://github.com/GettysburgResearch/collatz/blob/807d67ab049f1646398d8ca8c20948cdc1d87742/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md) · [current first-power layer](pointwise/FIRST_POWER_BOUNDARY_LAYER.md) · [current joint-moment proof](pointwise/JOINT_GATE_FRACTIONAL_PRESSURE.md) · [full local rational construction](pointwise/ALL_PLACE_PRIMITIVE_CYCLE_APPROXIMATION.md).
