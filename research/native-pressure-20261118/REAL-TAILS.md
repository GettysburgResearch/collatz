# Real affine tails, subcritical moments and extreme jumps on integer fibres

For the canonical inverse walk from any fixed positive odd unit, let
a_i be the inverse exponents, S their sums and r(a)=3/2^a. Define

    B_i = (1/3) Σ_(m≥1) Π_(j=1)^m r(a_(i+j)).

This converges by the fixed-root strong physical law. On a two-sided iid
geometric sequence use the same series to define B, and denote by Σ the
joint law of B and its ternary affine series. Almost surely,

    log(max_(i≤q) B_i)/log q → 1,     max_(1≤i≤q) a_i/log₂q → 1.

The empirical joint law of (B_i,X_i in Z₃) converges weakly to Σ and,
for each 0<s<1, its real s-moment converges to E B^s. Both statements
hold with a fixed arithmetic cylinder as a bounded multiplier and the
corresponding stationary mean. The empirical first real moment tends to
infinity; for s≥1 one has log(Σ_(i≤q) B_i^s)/log q→s. These assertions
are under the fixed-root inverse law and its source-qualified first-
passage inputs. They concern real offsets along an integer inverse
path. The stationary joint law and its geometric coding are prior work.

[First-passage stabilization and the short logarithmic source](ITERATED-LOG-BOUND.md)
· [Stationary real and ternary affine law, §§1,8](https://rstation.ai/problems/collatz/papers/19/v2).

## Two adjacent incoming shells

Use a=1.001 and R_j=exp(a^j), L_j=log R_j. At a nonperiodic root the
last-below-R_j depth n_j satisfies n_j∼L_j/ℓ and
n_(j+1)−n_j∼(a−1)L_j/ℓ by the previous shell bounds, ℓ=log(4/3).
Events of the entire deterministic forward segment from Y_(R_(j+1))
to its first entry at R_(j−1) transfer from the short logarithmic
source at threshold R_(j+1), with probability bound C_t times the
proxy probability plus O_t(L_j^(−c)). This error is summable in j.
The identical dyadic coding with N=⌊L_(j+1)/20⌋ forward steps covers
both descending shells, since a²−ℓ/20<1/a². The probability of failing
to reach the inner endpoint or the bit budget is summable by the
preceding maximal calculation. Tests on the resulting valuation words
may be read in reverse: under iid Haar the reversed list of the N
letters also has the iid geometric law. A good event on that entire
list suffices for the stated observable properties of its subsegments.
Coding and partial summation on the source window add only O(exp(−cN)).
In particular, any probability O(L_j^(−δ)) for fixed δ>0 in these
tests is summable after transfer.

Fix 0<κ<ℓ. For iid letters a Chernoff bound on Σ log r(a) gives
probability O(exp(−c m)) for a length-m block with sum above −κm
(use E log r=−ℓ and the exponential moment near zero).
A union over O(N²) subintervals shows that all blocks of length at
least H_j=⌈A log L_j⌉ in a two-shell segment have log multiplier
≤−κm eventually almost surely, for sufficiently large fixed A.
Every origin n_(j−1)≤i≤n_j has room for a positive constant times
i additional inverse steps in that segment. For m larger than that
fixed fraction of i the global strong law
S_(i+m)−S_i=2m+o(m) holds uniformly as i→∞. Decrease κ slightly
if necessary. Consequently for every such origin, all m≥H_j satisfy
the same exponential decay. Up to an error O(exp(−κH_j)), B_i can
therefore be truncated after H_j letters, using data entirely inside
the two-shell segment.

## The largest exponent and the largest real tail

For each fixed ε>0, the chance some letter in the N-step proxy exceeds
(1+ε)log₂ L_j is O(L_j^(−ε)). Conversely any subinterval of length
at least c₀ L_j contains a letter above (1−ε)log₂ L_j except with
probability O(exp(−c L_j^ε)); for the simultaneous assertion split
the list into a fixed grid of blocks of length ⌊c₀ L_j/3⌋. The shell
[n_(j−1),n_j] has at least c₀ L_j letters eventually for sufficiently
small c₀. Transfer proves the exponent claim.

For s<1, s>0, strict concavity and E r=1 give θ_s=E r^s<1.
Subadditivity yields E B^s≤3^(−s)θ_s/(1−θ_s). Truncated series
in the proxy have that same uniform moment bound. Choosing s with
s(1+ε)>1 and taking a union over O(N) origins excludes truncated
values ≥L_j^(1+ε) eventually, by Markov and transfer. The deterministic
far-tail bound just proved controls the rest.

For the opposite inequality use the iid tilt P'(a)=r(a)2^(−a)=3/4^a.
Its mean log multiplier d'=log 3−(4/3)log 2 is positive. For 0<ε<1,
a block of m=⌊(1−ε/2)log L_j/d'⌋ letters has log product between
(1−3ε/4)log L_j and (1−ε/4)log L_j with tilted probability tending
to one. Undoing the tilt gives original probability at least
(1−o(1))L_j^(−1+ε/4). On success the final product divided by three
exceeds L_j^(1−ε) for large j, so the tail at the beginning of that
inverse block does too. Each fixed grid interval of length comparable
to L_j has order L_j/log L_j independent trials. Their simultaneous
failure has summable probability. Transfer and the grid argument give
a success inside each sufficiently high shell. Consecutive shell depths
have bounded ratios, so the two logarithmic maximum laws hold for
every q by monotonicity and a countable sequence ε↓0.

## Subcritical moments and joint empirical convergence

Denote the k-term truncation by B_i^(k). For 0<s<1 and any fixed k,
the s-th power of the omitted terms through H_j is bounded by

    Z_i=3^(−s) Σ_(k<m≤H_j) Π_(h=1)^m r(a_(i+h))^s.

Under iid letters its expectation is ≤C_s θ_s^k. Choose p>1 with
sp<1. Its L^p norm is bounded independently of H_j by Minkowski
and the convergent geometric sum of (E r^(sp))^(m/p).
For the N-letter iid proxy, sum over starts with H_j letters available.
With probability outside O_ε,s(L_j^(−δ) log L_j) for some δ>0,
the sum of the Z_i divided by N is at most C_s θ_s^k+ε. Indeed truncate
Z_i at N^(1/4); the expected omitted average is O(N^(−(p−1)/4)),
so use Markov. The clipped variables from starts separated by H_j
are independent, and the variance of their average is O(H_j N^(−1/2)).
Chebyshev proves the assertion. Only nonnegative terms occur, so this
whole-list bound controls any subsegment without conditioning on its
induced endpoints. In applying it to the inner inverse shell, the
outer shell supplies H_j additional letters beyond every desired
start. All of these starts and lookaheads occur before the end of
the N-step proxy when written in forward order.

Transfer, the exponential far-tail bound, and summation over geometric
shells show almost surely

    limsup_(q→∞) q^(−1) Σ_(i≤q) |B_i−B_i^(k)|^s ≤ C'_s θ_s^k.

For this summation the nonnegative total bound O(L_j)(C_s θ_s^k+ε)
also applies to an unfinished shell, and its L_j is comparable to q.
Take a countable intersection over k and ε↓0. For fixed k the truncated
series is bounded and its frequency averages have the iid limit by
finite-word genericity and tightness of the finite-word distribution.
The ternary coordinate of X_i modulo 3^d is determined by the next d
inverse letters using their exact affine formulas. Dyadic residues use
a bounded window on the other side. The preceding L^s error and the
iid truncation bound give the joint weak limit by testing bounded
Lipschitz functions and arithmetic cylinders. They also give convergence
of the s-moment with a cylinder multiplier, since
|x^s−y^s|≤|x−y|^s for nonnegative x,y. Rational exponents suffice
simultaneously; any intermediate s follows by weak convergence and
uniform integrability from a larger rational exponent below one.

Finally E B=∞ because E r=1 and every positive series term has
expectation 1/3. Bounded truncations imply divergence of the empirical
first moment. For s≥1 bound Σ B_i^s by (max B_i)^(s−u) Σ B_i^u for
u<1 and let u↑1. The matching logarithmic lower bound follows from
the maximum alone. A periodic start exits backwards from its cycle
after almost surely finite time as in the strong laws; the omission
of this finite prefix preserves the conclusions.
