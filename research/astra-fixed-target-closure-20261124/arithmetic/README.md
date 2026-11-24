# Companion denominators from the observed parity distribution

**PROPOSED written theorems.** On a primitive parity necklace, a positive fraction of its phases have pairwise different pasts of length only `log₃ q + O(1)`, where `q` is the *reduced denominator of the closed companion*. The fraction depends on the actual odd density. This gives an exponential denominator for uniformly bounded string attractors and a positive-entropy requirement on the limiting parity distribution whenever the denominator is polynomial. The same entropy obstruction applies to rational approximations of the actual companion of one fixed escaping source, under the height and agreement hypotheses below. No ordinary counterexample is assumed to exist.

## Closed words and their arithmetic

Let `e` be a primitive circular binary word of length `L`, with `p` ones and `τ=p/L`. Put `β=log₂(3/2)`. At `τ>β` the recurrence

\[
  2^{1+e_i} w_{i+1}=3w_i+e_i
\]

has a unique positive rational periodic solution. The composite map has slope `3^L/2^(L+p)<1` and a positive offset. At every rotation the closed-phase expression has denominator dividing `2^(L+p)−3^L`, which is prime to six. The reduced denominators of successive rotations divide one another around the circle and therefore equal a common `q`. A phase in the even branch must be even dyadically. A phase in the odd branch must be `1 mod 4` dyadically. Thus equal phases force equal future symbols. Primitivity makes all `L` phases distinct. These phases are `−D/3` for the periodic companion of PR182, so `D` too has reduced denominator `q`. This construction requires no physical integer realization. The physical fixed point has a different denominator.

Take `β<ρ<τ`, set `r=2^(β−ρ)<1`, `B=1/[4(1−r)]`, and take the least nonnegative `k` with `3^k>Bq`. Write `P_e(k)` for the number of different length-`k` factors of the periodically extended word. The following stronger finite inequality holds:

\[
 \frac{\tau-\rho}{1-\rho}\,L\ \le |G|\ \le
  \#\{\text{different length-}k\text{ pasts at phases in }G\}
  \le \min\!\left(P_e(k),\sum_{u\ge\lceil\rho k\rceil}\binom{k}{u}\right).       \tag{1}
\]

Here `G` is the set of phases `i` satisfying `Σ_{i−j≤t<i} e_t ≥ ρj` for every `j≥1`. The middle inequality is an equality. Full past words are retained, including their order.

**Record count.** Extend the centered partial sums to all integers by `S_i−S_(i−1)=e_(i−1)−ρ`. Their drift per lap is `Δ=(τ−ρ)L>0`. The maximum `M_i=max_{j≤i}S_j` exists and `M_(i+L)=M_i+Δ`. A strict increase of `M` marks a member of `G`, and each increase is at most `1−ρ`. Summing over a lap proves the first inequality. This is the cyclic record form of Pliss's lemma. The finite scan over a single lap can start at any strict record; all preceding heights are then accounted for by its starting maximum. [Alves, Bonatti and Viana, Lemma 3.1](https://w3.impa.br/~viana/out/mexpanding.pdf)

**Real bound and ternary injection.** At a marked phase the product of any `j` most recent companion slopes is at most `r^j`. Each step's additive offset is at most `1/4`. Summing the past affine expansion gives `0<w_i≤B`, since the remaining product times the bounded periodic starting phase tends to zero. For a fixed `k`-bit past `v` of weight `u`, the unrolled ordinary numerator recurrence gives

\[
     2^{k+u}(qw_i)=3^k(qw_{i-k})+qC_v,
\]

where the carry depends only on `v`. This determines the integer `qw_i` modulo `3^k`, and `0<qw_i≤Bq<3^k`. Since the companion phases are distinct, their marked pasts are distinct. Each such past also has at least `ρk` ones. This proves (1).

For `τ−ρ` bounded away from zero at fixed `ρ>β`, a bound `P_e(k)≤A k^d` with fixed `A,d>0` gives `log q ≫ L^(1/d)` for large `L`. In particular a circular string attractor is a set of marked positions such that every length-`j` factor has an occurrence crossing one of those positions, for `1≤j≤L`. With `γ` such positions there are at most `γj` possible factors, by specifying the crossed position and its offset. For `j>L` the same inequality follows from `P_e(j)≤L`. Thus (1) gives `log q ≥ (log 3)(τ−ρ)L/[(1−ρ)γ]−O_ρ(1)`. This uses neither a substitution dictionary nor a factorization of the clock or carry. [Kempa and Prezza, string attractors](https://arxiv.org/abs/1710.10964)

## What a polynomial denominator forces in a limiting law

Consider any sequence of the preceding primitive necklaces with `L→∞`, `τ≥τ₀>ρ>β`, and `log q ≤ (K+o(1)) log L` for a finite `K>0`. Let `μ_L` be the uniform law of the `L` shifts on the two-sided binary full shift. For **each** weak limit `μ` of this sequence there is a stationary probability `ν` satisfying

\[
 c\nu\le\mu,\qquad \nu([1])\ge\rho,\qquad h(\nu)\ge \frac{\log3}{K},
 \qquad c=\frac{\tau_0-\rho}{1-\rho}.                                           \tag{2}
\]

Measure domination holds on all Borel sets, and metric entropy uses natural logs. For ergodic `μ`, necessarily `ν=μ`. For any `μ`, block entropy concavity gives `h(μ)≥c h(ν)`. In particular **a zero-entropy limiting law forces `log q/log L→∞` along that convergent subsequence**. This applies even when the language of the support has high complexity. It concerns varying necklaces: the entropy of each individual periodic measure is zero.

To prove (2), choose a marked endpoint uniformly and let `σ_L` be the law of the shift starting at the beginning of its `k`-bit past. Its initial `k`-block entropy is precisely `log |G|` by (1). Put `ν_L=k⁻¹ Σ_{j=0}^{k−1}(shift^j)_*σ_L`. Every summand is bounded by `μ_L/c`. Also `ν_L([1])≥ρ`. The packing bound gives `2^k≥cL`, hence `k→∞`. Any further weak limit `ν` is stationary by telescoping the shifts, is dominated as claimed, and has the stated one-bit frequency.

For fixed `m≤k`, split the initial `k`-block after each possible offset `0,…,m−1` into disjoint `m`-blocks and two end pieces. Joint entropy is at most the sum of block entropies, and the end pieces cost at most `2m log 2` for each offset. Summing offsets counts each whole interior `m`-block once. Add the missing nonnegative block entropies and use concavity on the `k` shifted laws to obtain

\[
 \frac{1}{k}\log |G|\le \frac{1}{m}H_m(\nu_L)+\frac{2m\log 2}{k}.
\]

At fixed `m`, `H_m` is continuous on the full shift. Since `k=log q/log 3+O_ρ(1)`, the left side has liminf at least `log(3)/K`. Take the infimum of `H_m(ν)/m` over `m`. If `μ` is ergodic, stationarity and the convex decomposition of `μ` coming from `cν≤μ` force `ν=μ`. This is the finite-alphabet block argument underlying the variational principle, applied to arithmetic marks. [Misiurewicz, pp. 147–157](https://www.numdam.org/article/AST_1976__40__147_0.pdf)

## Consequences for the shortcut Collatz map

For a primitive **positive ordinary** cycle of `T(x)=x/2` on evens and `(3x+1)/2` on odds, let `m` be its minimum. Multiplying its physical factors gives

\[
     0<L\log2-p\log3=\sum_{e_i=1}\log(1+1/(3x_i))\le p/(3m).
\]

Along every sequence of primitive positive cycles with `L→∞`, the minima tend to infinity: each finite collection of starting integers belongs to only finitely many cycles. Consequently `τ→α=log 2/log 3`. For every fixed `ρ∈(β,α)`, (1) and the elementary binomial bound `Σ_{u≥ρk} binom(k,u) ≤ exp(kH(ρ))`, with `H(t)=−t log t−(1−t) log(1−t)`, give

\[
     \liminf\frac{\log q}{\log L}\ge\frac{\log 3}{H(\alpha)}=1.6684596861\ldots.      \tag{3}
\]

Indeed the binomial bound follows by weighting the terms with the Bernoulli parameter `ρ>1/2`, and (3) follows by taking `ρ↑α`. A sequence with polynomial `q` must also satisfy (2) for each `ρ<α`, with `τ₀` strictly between `ρ` and `α`. These are restrictions at the *complete primitive lap*, whereas escape-only nonvanishing arguments can fail at that lap.

The same (1)–(3) apply to periodic closures of long prefixes of a **single fixed injective positive orbit**. For such an orbit `x_i→∞`. The physical identity `log x_L = log n + p_L log 3−L log 2 + Σ_{e_i=1}log(1+1/(3x_i))` shows `liminf p_L/L≥α`, since its final sum is `o(L)` and `x_L≥1`. Every sufficiently long prefix is primitive. Otherwise it is a power with root length `t≤L/2`, so the first `L−t` parities agree from `n` and `x_t`. Subtracting their affine rows gives `2^(L−t) | x_t−n`, a nonzero difference of magnitude at most `(n+1)(3/2)^t`. This bounds `t` and then `L`. The denominator in this prefix assertion belongs to the periodic closure, which may change with `L`.

The actual dyadic scalar, without periodizing its prefixes, is treated separately in [ACTUAL_APPROXIMATION.md](ACTUAL_APPROXIMATION.md).

## Controls, dependencies and missing inference

The baseline PR193 denominator screen already packs **all** bounded companion phases by the coarse terminal inequality `u≥βk−O(1)` and obtains the exponent `log 3/H(β)=1.618844867…` with a logarithmic improvement. Its rational-approximation theorem applies to every positive source and every wrong rational without an occupation hypothesis. The present new input is positive-frequency selection at any strict slope below the word average, with **every suffix** controlled. It preserves the actual catalog and, under a polynomial denominator, yields a dominated positive-entropy invariant law. PR195's escape cancellation estimate and PR203's obstruction to using Northcott on algebraic tails concern other quantities. [PR193, frozen denominator and trial comparison](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/arithmetic/README.md) · [PR182, frozen companion criterion](https://github.com/GettysburgResearch/collatz/blob/234fd2ece3a17c8950dce452291198705b4e6e60/research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md) · [PR195, fixed-source algebraic cancellation](https://github.com/GettysburgResearch/collatz/blob/ef3496b577ed7525d5e0c82a9b782819457403d5/research/astra-global-closure-20261124/round7/arithmetic/ALGEBRAIC.md) · [PR203, conjugate heights](https://github.com/GettysburgResearch/collatz/blob/3f2c89f12b057b8bb8655bd6fc794c772aa8b65d/research/mixed-adic-basin-density-20261124/companion_obstruction.md)

Primitivity is necessary. Repeating `11100` arbitrarily many times retains the companion phase `333/13` and its complete reduced denominator `13`, while the unreduced lap grows. The physical phase at the same cut is `19/5`. As a separate near-critical obstruction, put `p=⌊αL−√L⌋` and take the primitive circular word `1^p 0^(L−p)` for large `L`. Its two run ends form a circular attractor. Thus its closed companion denominator grows exponentially even though its word laws converge to the zero-entropy mixture of the two constant sequences. Its physical fixed point at the displayed cut is positive and below one, since it equals `(3^p−2^p)/(2^L−3^p)` and `3^p/2^L≤3^(−√L)`. These are rational physical cycles; finite positive ordinary realizations of their prefixes supply no integral closed lap. A large companion denominator is compatible with the denominator's raw exponential upper bound. No polynomial upper bound for `q` on ordinary nontrivial cycles, no unavoidable low-entropy law there, and no exclusion of the physical full divisor is known here.

[CompanionPacking.lean](CompanionPacking.lean) checks the affine numerator recurrence, same-past equality below the ternary modulus, the catalog injection, and the signed finite record-increment count. The cyclic extension, real product bounds, entropy argument, actual-orbit reductions and unbounded conclusions are written mathematics. [check.py](check.py) exercises the complete phase arithmetic, all record suffixes on a full lap, and the packing/primitive boundary with exact integers and fractions.
