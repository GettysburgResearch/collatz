# Independent review: sparse ordinary predecessor-basin minima

23 November 2026. Reviewer: global-cycle lane. This is a fresh reconstruction of the new first-hit/counting argument, separate from the escape lane's review.

**Verdict: VERIFIED for BM3--BM15 at the exact written scope below.** The result counts distinct disjoint basins touched by low ordinary sources. It does not bound the population of an individual basin, prove the proposed Green lower comparison, or exclude escape.

## Exact source boundary

Reviewed new manuscript:

`research/lean-exact-witness-global-20261121/repo-synthesis-20261123/escape/SPARSE_BASIN_MINIMA.md`

SHA256: `65f1a0698cb3a17a8eb52ddab42f6b548be5bb921872f71c4d9cb00369ccbeec`.

For the coarse orbit count I read the resident `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-401, and reconstructed its cylinder calculation alongside the parent `HIGH_VARIANCE_ESCAPE.md`, HE2. The new manuscript pins the former to main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a` and the latter to owned PR177 `2fbc5706d2caff5d1485247e5291374ff4885041`.

For the sharper statement I fetched and read the full primary repository proof:

- PR182 commit `afe6f4d1a661b377c9daa4623bdd732ba478386b`;
- `research/whole-repo-round3-20261123/GLOBAL_ORBIT_COUNT.md`;
- Git blob `6881dc864f3b586958bd46d5c38b1c2524008565`;
- sections 1--5, including its exact source domain and scale recurrence.

No stronger external interval-compression theorem, predecessor-density estimate, random-parity law, or stationary distribution is imported by this review.

## 1. Every sibling and every shortcut basin

The root identity is exact: `3S(q)+1=64(3q+1)`, so `U(S^b q_j)=q_(j+1)` for every b>=1. A sibling root cannot equal any point q_i of the original injective odd ray: applying U would give `q_(i+1)=q_(j+1)`, hence i=j, while `S^b q_j>q_j`.

Two sibling roots can coincide only if their ray indices first agree after applying U, then their strictly increasing S-iterates have the same depth. Thus the pair labels `(j,b)` are unique. Starting from any sibling, its next odd point is on the original ray and every later odd point stays on that ray. All intermediate shortcut points before the next odd point are even. It therefore cannot reach any other sibling root, at any shortcut clock.

If one ordinary source belonged to two full shortcut basins, determinism would make their roots forward-comparable, contradicting the previous paragraph. This proves pairwise disjointness simultaneously for all j and b, rather than only at one fixed depth.

Every full basin has an attained positive integer minimum. For these odd roots the minimum is odd, since an even smaller source's first halving would still precede its root hit and remain in the same basin. A minimum may be divisible by three. The proof correctly keeps the full basin here and never treats that minimum as necessarily carrying unit-odd pressure mass.

## 2. The decisive first-hit inequality BM4

For any disjoint family of full basins, their minima are distinct. Split those below X according to whether `T^H(m)>=m`.

In the other part, let tau be the first visit to that basin's specified root. If tau>H, the actual state `T^H(m)` still reaches the root and hence remains in its full basin. Its being smaller than m contradicts the definition of m. Therefore tau<=H. This argument also includes tau=0, when the minimum itself is the root.

The elementary inequality `T^t(n)+1 <= (3/2)^t(n+1)` then puts the actual root below `(3/2)^H(X+1)`. Distinct basins give distinct charged roots. Hence BM4 counts each minimum either among the actual no-descent sources or among roots below the proved height.

The root visit is load-bearing. The argument would fail if it simply charged a small later state that need not have visited the specified root. The manuscript does not make that substitution. It also imposes no bound on the height of intermediate excursions.

## 3. Complete carry and the finite no-descent estimate

For any actual H-bit shortcut word the recurrence of its complete carry is either `C_(h+1)=C_h` or `C_(h+1)=3C_h+2^h`. Induction gives `0<=C_H<=3^H-2^H`, including H=0. Thus if the endpoint is at least its source but `3^p<2^H`, the positive integer `2^H-3^p` forces `n<=C_H<3^H`.

All other words have `3^p>=2^H`. From `3^5<2^8` this implies `p>=5H/8`. The parity-prefix bijection gives one residue modulo `2^H` per actual binary word, so each contributes at most `X/2^H+1` ordinary sources. Counting words is a finite arithmetic upper bound and assumes no independence.

The weighted binomial sum is correct:

`B_H <= (8/3)^H (3/5)^(5H/8)`.

Raise the proposed base comparison with `2^(31/32)` to the 32nd power. The result is exactly `2^65 < 3^12 5^20`. I checked this integer inequality independently; its positive margin is `13788675091106287393`. This proves BM8 and BM10 with the displayed constants. The empty horizon H=0 is harmless: its loose upper bound still covers every positive source up to X.

## 4. The explicit all-sibling power saving

The inherited orbit estimate applies to the one injective odd ray, not to its predecessor basins. Its elementary proof uses exact gap cylinders modulo `2^(A+1)`, the full positive affine remainder, and injectivity at one common odd clock. The displayed constants give `4Y^(39/40)` uniformly in the ray. I reconstructed the two valuation lanes and their rho/sigma comparison; no external density input is needed.

The exact iterate formula `S^b(q)=64^b q+(64^b-1)/3` puts the b-th sibling root above `64^b q`. Summing the orbit count over b>=1 gives a convergent geometric factor less than one. Terms with `Y/64^b<1` contribute zero. Hence BM12 counts all siblings without a logarithmic loss.

For `H=floor(log_2(X)/25)`, the four bounds in BM13 are valid. Their exponents are respectively `8/125`, `799/800`, `31/800`, and root-height exponent `128/125`. Applying the orbit count to that last height gives exactly

`(39/40)(128/125)=624/625`.

The dominant exponent exceeds this by `7/20000`. Since X>=1, the sum of coefficients is bounded by `1+2^(1/32)+1+8<12`. Therefore the claimed uniform bound `12 X^(799/800)` is correct for every real X>=1, including the small-X regime where H=0.

## 5. Sharper entropy exponent and logarithmic factor

I reconstructed the pinned PR182 argument on its stated domain: a forward-invariant positive odd set with injective U. Reading the same number of odd steps at all low sources makes the high-total-clock endpoints inject into the same set below X/2. The low-total-clock contribution is the exact finite binomial tail, with critical slope `alpha=log_3 2`. Stirling and the bounded ratio of consecutive upper-tail terms give the square-root logarithmic denominator. Iterating the scale inequality preserves a uniform constant over the actual injective ray.

Summing that root count over sibling depths preserves the logarithmic factor: where `Y/64^b>=sqrt(Y)`, all logarithmic denominators are comparable to `sqrt(log Y)` and the geometric numerator sum converges; the remaining depths contribute only `O(Y^(theta/2))`.

For the no-descent contribution the exact cutoff is `ceil(alpha H)`. Its upper-tail count is `O(2^(theta H)/sqrt(1+H))`, since rounding changes the entropy exponent by a bounded amount. With

`c=(1-theta)/(1-theta+theta a)`, `a=log_2(3/2)`,

both leading exponents equal

`eta=1-c(1-theta)=theta(1+ca)`.

The carry exponent `c log_2(3)` and one-lift exponent `c theta` are strictly lower. This is not dependent on trusting rounded decimals: `alpha<2/3` gives `theta>H_2(2/3)>5/6`, while `a>1/2`; these bounds imply `(1-theta)^2<a(2theta-1)`, which is exactly the nontrivial carry-exponent comparison. The one-lift comparison follows from `0<c<1` and `0<a<1`.

An independent numerical evaluation, used only as an explanatory check, gives theta approximately `0.9499555271883305`, c approximately `0.08261806202043359`, and eta approximately `0.9958654226414656`. The exact formula defines the theorem. The stronger claim BM15, including its square-root logarithmic saving, is supported by the pinned elementary source proof and the new first-hit argument.

## 6. Scope and consumer

I also checked consistency with the companion pressure-packing consumer: a basin touched by a unit-odd ancestor below X has full shortcut minimum below X, even if the minimum itself is divisible by three. This is exactly the direction needed to use BM3 in the source cutoff. It introduces no assertion about how many ancestors lie inside one basin.

The stronger pressure exponent and critical-root summability therefore have a valid unconditional sparse-minimum input. Their infinite pressure construction and analytic limits are separate written scopes, and the proposed ordinary Green lower comparison remains open. This report does not claim new Lean execution or proof of those omitted universal premises.

No correction was needed at the reviewed manuscript hash.

