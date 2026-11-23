# Independent review: ordinary basin pressure packing

23 November 2026. Reviewer: global-cycle lane. This review reconstructs BP5--BP16 independently of the escape author and the coordinating author of the new sparse-minimum input.

**Verdict: VERIFIED at the written analytic scope below.** The result proves stronger necessary restrictions on one hypothetical escaping ordinary component. It does not establish the proposed Green lower comparison, exclude every escaping component, or settle positive cycles.

## Frozen sources

Main reviewed manuscript:

`research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/BASIN_PRESSURE_PACKING.md`

SHA256: `257443f6c0800ab42e9f08c79c1daebc4d97c894833add6941b46389778349d2`.

New sparse-minimum input:

`escape/SPARSE_BASIN_MINIMA.md`, SHA256 `65f1a0698cb3a17a8eb52ddab42f6b548be5bb921872f71c4d9cb00369ccbeec`.

That input was independently reconstructed in the separate [sparse-minimum review](REVIEW_SPARSE_BASIN_MINIMA.md). The present report uses its explicit uniform estimate `12 X^(799/800)`, not its optional sharper entropy version.

For the exact signed-cost direction I read the prior

`research/lean-exact-witness-global-20261121/universal-step-20261123/escape/BALANCED_INVERSE_TRANSPORT.md`, Section 4, equation (10),

at the parent checkpoint PR177 `2fbc5706d2caff5d1485247e5291374ff4885041`. Its SHA256 is `58f5af3b205fb1ac720593865ea2bcba60fa918c5432f0c1917a467edfa94b9b`.

No new execution or Lean audit is claimed by this analytic reconstruction. The finite Lean accounting and implementation receipts are separate evidence.

## 1. Exact pressure identities and ordinary domains

The pressure weight is positive and bounded by `1/n`, with a uniform positive reciprocal correction on the stated escaping component. Its exact forward relation is `r(n)=(3/2^a)r(Un)`. Nonperiodicity gives a unique hitting depth for each ancestor, so the all-depth inverse-word sum counts every ordinary predecessor once. Therefore `A_s(q)=r(q)^s Z_s(q)` is valid, and the Green function is finite because the entire component has mass at most `sum_n n^(-s)`.

The affine sibling identity gives `r(S^b q)=64^(-b)r(q)`. The predecessor sets of q_j increase, so their masses are at least the fixed positive `a_s=A_s(q_0)`. This proves BP4 with the displayed orientation: `beta_(j,b)=b_(j,b)/A_s(q_j) <= b_(j,b)/a_s`.

All unit-odd sibling predecessor sets are contained in the disjoint full shortcut basins from BM3. If a unit-pressure source below X belongs to one, that full basin's minimum is below X. The minimum itself need not be a unit and is not assigned a pressure weight. This is precisely the valid direction of the source-cutoff comparison.

## 2. Complete cutoff and rearrangement

For a finite family with every mass at least lambda, at most K(X) groups meet the integers up to X. Every remaining group's entire mass is contributed by sources above X. Disjointness makes the sum of those masses at most the full source tail. This proves BP5, including its positive-part convention. The integral upper bound is valid for integer X>=1 and s>1.

Applying this to every finite subset of a mass level set proves BP7 without first assuming the level set finite. A uniform finite cardinal bound on all its finite subsets establishes finiteness. Taking `X=ceil(lambda^(-1/(s+eta-1)))` at small lambda balances the terms and gives distribution exponent `eta/(s+eta-1)`. Inverting it yields

`kappa_s=(s+eta-1)/eta=1+(s-1)/eta`.

This exceeds s because eta<1 and s>1. Large masses are bounded by total component mass, so the finite initial portion is absorbed in the constant. The same rearrangement bound transfers to beta by BP4. There is no unjustified chronological ordering assertion: rearrangement and chronological indexing are kept distinct.

## 3. Dyadic concavity and the critical root

In shell `[2^k,2^(k+1))`, at most `12 (2^(k+1))^eta` basins receive any weight. The sum of all their weights is at most `2^(k(1-s))`, since there are exactly `2^k` possible integer sources and each has weight at most `2^(-ks)`.

For the finite nonzero shell list, concavity gives `sum_i b_(i,k)^p <= M_k^(1-p) (sum_i b_(i,k))^p` for 0<p<1. Substitution gives exactly the exponent in BP9:

`eta(1-p)+p(1-s)=eta-p(s+eta-1)`.

Subadditivity of the p-th power first applies to finite shell sums; monotone limits extend it to each basin. Tonelli then interchanges nonnegative sums. The resulting geometric series converges precisely in the displayed strict range, proving BP10 with its explicit constant. No negative term, tail atom, or conditional limit is dropped.

At p=1/s,

`eta-p(s+eta-1)=-(1-eta)(1-1/s)<0`.

Thus the critical s-th root is inside the proved range, not an unproved endpoint. Multiplying by `a_s^(-1/s)` through BP4 yields BP11 with exactly the stated denominator. Fixing sibling depth one removes only the constant factor 64. For s=2, `kappa_2=1599/799>2`, and BP12 genuinely strengthens ratio summability to square-root summability.

For p>=1, boundedness and total finite mass give summability directly. This does not change the strict lower threshold at `1/kappa_s`; no equality case there is claimed.

## 4. The new conditional Green comparison

One accelerated step obeys `U(q)+1 <= (3/2)(q+1)`, so `log(q_j+1)` grows at most linearly in j. The denominator in BP13 is consequently at most a fixed multiple of `(j+1)log(j+2)`. Its reciprocal series diverges. This uses an upper growth bound on the same ordinary ray, without a density or typical-orbit claim.

Taking the s-th root of HC-new gives a positive multiple of that divergent series, contradicting BP11. Thus the displayed comparison is a correct sufficient condition for escape exclusion. It remains explicitly unproved. The more general power condition `a<kappa_s` is also correct: choose p>1/kappa_s with ap<=1, so the lower comparison forces a divergent p-th-power series while BP10 gives convergence.

These conclusions concern the escape alternative. Positive periodic components are not ruled out by this argument.

## 5. Reciprocal minima and ordinary repair cost

For each positive integer minimum m_i,

`m_i^(-t)=t integral_1^infinity 1_(m_i<=X) X^(-t-1) dX`.

Tonelli and BM3 prove BP15 for every t>eta. Taking t=1 gives exactly `12/(1-799/800)=9600`. Any chosen actual ancestor n_i from a distinct sibling basin satisfies n_i>=m_i, so its reciprocal or t-th-power sum has the same upper bound. This uses no predecessor-population lower theorem.

An ordinary repair with `n_j=O((j+1)log(j+2))` would force a divergent reciprocal series. For polynomial height `O((j+1)^d)` with d<1/eta, choose t>eta with dt<=1 to obtain the same contradiction from BP15. The claim concerns a constructed ordinary ancestor in each distinct basin. Rational inverse leaves and finite congruence compatibility alone do not supply it.

## 6. Signed-cost orientation

For one physical inverse edge, `3n+1=2^e q` gives `2^e=3n/[q lambda(n)]`, with `lambda(n)=3n/(3n+1)`. Comparing the original and transported edge and multiplying over the full inverse path gives

`2^Delta=(q/q') (n'/n) Lambda(n,q)/Lambda(n',q')`.

For the actual word from q_j backward to the fixed q_0, this is exactly BP16 with `q'=S q_j`, `n=q_0`, and `n'=n'_j`. The original product includes the ancestors q_0 through q_(j-1), excluding the root q_j, consistent with the previous balanced-transport formula. No numerator/denominator product has been reversed.

For every positive q,

`1/85 <= q/(64q+21) <= 1/64`.

Together with correction products in `[c_*,1]`, this gives the explicit comparison

`(c_*/85)(n'_j/q_0) <= 2^Delta_j <= (1/(64c_*))(n'_j/q_0)`.

In particular `n'_j <= (85q_0/c_*) 2^Delta_j`. This is the direction needed to deduce

`sum_j 2^(-t Delta_j) <= (85q_0/c_*)^t 12t/(t-eta) < infinity`

from BP15. The transported ancestors lie in the distinct sibling basins, so they cannot be reused across j. Signed edge increments are retained, but no independence, centering, or cancellation law is assumed.

## Conclusion of the review

The complete cutoff, all-depth nonnegative sums, critical-root endpoint, reciprocal-minimum budget, and signed-cost consumer are all valid at the frozen scope. The strict improvement over generic partition bounds comes from the independently proved ordinary sparse-minimum theorem. The missing Green lower comparison and universal ordinary repair remain exposed. No correction is required for BP5--BP16.

