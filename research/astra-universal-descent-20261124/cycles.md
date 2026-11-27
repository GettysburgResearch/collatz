# Exact cycle cuts and a simultaneous obstruction to descent by cutting

**Status.** PROPOSED elementary theorems with proofs below. The universal positive-cycle obstruction is OPEN. We use the ordinary positive odd map sending odd x to (3x+1)/2^a, where a is the exact 2-adic valuation of 3x+1. All cuts below retain a nonempty proper portion of the itinerary.

## C5. A lower bound on the reduced denominator of any positive rational cycle

Take any primitive shortcut parity word of period A whose rational cyclic realization is positive. Let d be the reduced odd denominator of its minimum m. This is the true denominator **after** all cancellations: every phase has denominator d, by the unit argument of C3 (the full cycle denominator is coprime to 6). Let P(k) be its cyclic binary factor complexity. Put γ=1+log(2)/log(3/2).

**Exact finite bound.** Put e=d m, an ordinary positive integer. For every k and every pair of nonnegative integers s,t satisfying s+t=P(k)<A, one has

    2^(k+t) ≤ max(2^t(2^s−1)e, (3^t−2^t)(e+d)).                (C5.1)

All quantities in (C5.1) are integers. In particular, setting d=1 and comparing both entries with the left side is a rigorous exclusion test. The right side can be minimized over the P(k)+1 possible splits. No limit, roundoff, phase theorem, or corpus of known convergent starts enters this test.

**Logarithmic corollary.** For every k with P(k)<A, one has

    d(m+1) > (1/2) · 2^(k−P(k)/γ).

To prove it, scale to the distinct positive integers z_i=d x_i. The parity of z_i encodes the rational word because d is odd. The even map is z/2 and the odd map is (3z+d)/2. Two starts with the same k-bit word still differ by a multiple of 2^k, since the additive contributions cancel. Writing h=P(k), choose s=ceil(h/γ), t=h−s. The h+1 consecutive positions from −s to t around the minimum are distinct since h<A. Some pair produces the same k-bit factor, so the larger member is at least e+2^k, and is in particular strictly above 2^k. Backwards, z_{−j}≤2^j d m. Forwards, z_j+d≤(3/2)^j d(m+1). For the integer form these bounds hold for every split s+t=h, independently of the logarithmic choice. Subtract e from both upper bounds and multiply by 2^t to get (C5.1). For the chosen balanced split they also give

    2^k < d(m+1) max(2^s,(3/2)^t) ≤ 2 d(m+1) · 2^(h/γ).

The last bound follows from s≤h/γ+1 and t≤h(1−1/γ). This proves the claim. The ceiling factor can be avoided when checking a particular word, by minimizing max(2^s,(3/2)^(h−s)) over integral s.

Let p be the number of odd steps and Λ=A log 2−p log 3>0. The exact product formula on the positive rational cycle still gives m≤p/(3Λ). Therefore the entirely word-dependent bound

    d > 2^(k−P(k)/γ) / (2(1+p/(3Λ)))

applies at **every** scale with P(k)<A. A right side at least 1 excludes ordinary cyclic realization. In particular, under a polynomial lower bound for Λ and along scales log p=o(k), if P(k)≤(γ−δ)k for a fixed δ>0 and P(k)<A, then log_2 d ≥ (δ/γ)k−O(log p). High-complexity words, or words for which P(k)=A before such a scale exists, are the unsupported universal case.

## C1. The cut at a cycle minimum

For a word with positive exponents a_1,...,a_s, let A be their sum, U=2^A, V=3^s. Composing the affine maps gives F(x)=(Vx+B)/U with B positive and odd. Write D=U−V. If an ordinary segment goes from u to v<u, then D>0. Its unique periodic candidate y satisfies

    y=B/D=v−V(u−v)/D=u−U(u−v)/D.

Since gcd(D,V)=1, this is an integer precisely when D divides u−v. An integral candidate realizes the prescribed word exactly. Indeed, at every cyclic cut the rational fixed value has the form B_rot/D with odd numerator and odd denominator. Consecutive values obey the prescribed affine relations. Starting with an integer at one cut, each following quotient is an odd integer because it both has denominator dividing a power of two and has reduced odd denominator and odd numerator. These positive integers form a cycle.

In particular, every proper suffix ending at the global minimum m of a nontrivial primitive cycle, starting at u, has 0<y<m. If integral, y=1 exactly for the all-2 word. Since D is odd and u,m are odd, every successful cut also has

    m−y ≥ 2·3^s,        u−y ≥ 2·2^A.

Thus all suffixes of length s with 2·3^s ≥ m−1 are excluded from yielding a *nontrivial* smaller cycle. A proof that at least one remaining non-all-2 suffix has D dividing u−m would rule out nontrivial positive cycles by minimality.

## C2. Every proper cut can fail simultaneously under arbitrarily precise approximate closure

For every integer modulus M≥1, floor H, and real ε>0 there is one ordinary positive odd orbit segment with start u and endpoint v such that

* v>H is its strict minimum, v<u and 1−ε<v/u<1;
* v≡u mod M;
* no proper nonempty contiguous subword of the **cyclically arranged exponent word** has a positive integral periodic candidate at any cut.

The length can be arbitrarily large. In particular there can be no implication to a successful proper cut from ordinary realization, strict terminal minimality, congruence closure modulo an arbitrarily prescribed finite collection of moduli, and arbitrarily close relative endpoint agreement alone. The construction has a large final valuation. It makes no claim about countermodels subject to a uniform cap on the individual valuations.

**Arithmetic of the word.** Use i copies of exponent 1 and a final exponent b≥3, where i≥2. Write A=i+b, p=i+1, U=2^A, V=3^p, R=V/U<1. Since F_1(x)+1=(3/2)(x+1), the word acts as

    F(x) = R(x+1)−2^(1−b).

A proper cyclic subword containing b is a cyclic rotation of k copies of 1 followed by b, with 0≤k≤i−1. Its slope r=(2/3)^(i−k)R is strictly below 2/3. At the cut ending in b its fixed point is

    (r−2^(1−b))/(1−r).

The numerator is positive since 3^(k+1)>2^(k+1), and the quotient is strictly below 2. If any rotation has an integral positive fixed point, C1's realization argument makes this particular cut integral and therefore equal to 1. The orbit of 1 has only exponent 2, contrary to b≥3. A subword omitting b consists entirely of 1s and strictly increases every positive input. This proves the simultaneous assertion.

**Choosing the clocks.** Let M0 be the largest divisor of M coprime to 6. Choose L≥1 with 3^L≡2^L≡1 mod M0 (for M0=1 take L=1). Take i=Ln and A=L ceil((Ln+1) log_2(3)/L). The fractional parts of n log_2(3)+log_2(3)/L visit every open subinterval of (0,1) infinitely often, since log_2(3) is irrational (otherwise a positive power of 2 equals a positive power of 3). Choose them arbitrarily close to 1. Then A−(i+1)log_2(3) is strictly positive and arbitrarily small, R tends to 1 from below, and b=A−i tends to infinity. In particular R>1−ε. Moreover D=U−V≡−2 mod M0, is odd and is nonzero mod 3, so gcd(D,2M)=1.

**One ordinary lift.** Put B=V−2^(i+1) and choose an arbitrarily large positive integer u with Du≡B mod 2UM. Then

    U(F(u)−u)=B−Du

is divisible by 2UM, so v=F(u) is integral and v≡u mod 2M. The congruence implies D(u+1)≡U−2^(i+1) mod 2U, so 2^(i+1) divides u+1. The first i steps of exponent 1 are exact: after j≤i such steps, the value is 3^j(u+1)/2^j−1, an odd positive integer. The last step has exact exponent b because v is odd. Along this initial run the states strictly increase. Since F has slope R<1 and positive intercept, taking u sufficiently large gives H<v<u and v/u>R>1−ε. The endpoint is the strict minimum.

**Boundary.** The obstruction does not replace v=u by a new hypothesis implying exact closure. In this construction the discrepancy in absolute size grows with the choice of lift. The chosen modulus is fixed before the word is constructed. A cut proof that uses the full integer equation, word-dependent moduli, or stronger restrictions on cycle shape is left open. Even exclusion of all nontrivial positive cycles would leave divergent ordinary orbits to exclude.

## C3. Exactly closed rational cycles defeat every fixed finite collection of local integrality tests

Given the same M and H, the words in C2 may simultaneously be chosen so their **exact positive rational cycles** have strict minimum above H, are integral at every prime dividing M, and have unbounded reduced denominators. This also holds together with every assertion of C2 about the ordinary lifts. The rational cycle and the ordinary segment are different objects.

Indeed, choose a nonempty open interval of slopes whose closure lies in (max(0,1−ε),1) and so close to 1 that R/(1−R)>H+1 throughout. The clock construction hits that interval infinitely often with i unbounded. For large i the exact fixed point y=(R−2^(1−b))/(1−R) exceeds H. It is the unique minimum because of the initial increasing run. Every phase is a rational number with denominator dividing D, hence integral at the primes of M. In fact every phase has the same reduced denominator: for each prime divisor of D both 2 and 3 are units, and applying (3x+1)/2^a preserves a negative valuation. Now gcd(B,D) divides U−2^p=2^p(2^(b−1)−1), and D is odd. Therefore the reduced denominator of y is at least

    D/(2^(b−1)−1) > (1−R)·2^p.

Here p=i+1 and 1−R is bounded away from zero on the chosen interval. This gives exponential denominator growth even though every prescribed finite set of primes sees exact cyclic integrality. The proof does not use any unproved bound on a linear form in logarithms.

## Exact full-cycle constraint on the suffix search

For an actual cycle of odd period p and total clock A, multiplication of the p one-step identities gives the exact inequality

    0 < A log 2 − p log 3
      = sum_i log(1+1/(3x_i)) ≤ p/(3m).

Suppose a phase bound ||p log_2 3|| ≥ c p^(−κ) is available for the relevant p, with c>0 and κ≥0. (The exact inequality above is independent of that input.) Then m ≤ p^(κ+1)/(3c log 2). Combining with C1, every nontrivial successful suffix of length s must satisfy

    2·3^s + 1 < m ≤ p^(κ+1)/(3c log 2).

Thus, **conditional on the stated numerical phase bound**, only logarithmically many suffix lengths can possibly supply a smaller cycle at the minimum. The phase bound alone does not make even one of those divisions exact. The repository's source-qualified phase discussion is in research/external/mazur-2026/natural-density-log-time.md.

## C4. Ordinary parity-factor complexity in both directions at the minimum

Here one letter is one **shortcut** step T, recording the parity of its input. Thus the primitive shortcut period of an odd cycle with total clock A is A. Let P(k) count distinct length-k parity factors of the infinite orbit, or of its periodic extension in the cycle case. For two starts x,x' producing an identical k-bit word with h odd steps, the affine formula gives

    2^k (T^k(x)−T^k(x')) = 3^h (x−x').

Consequently x≡x' mod 2^k. All distinct starts in an interval of width strictly less than 2^k have distinct k-bit factors. Moreover T(x)+1≤(3/2)(x+1), and every predecessor w of x satisfies w≤2x.

* For any **aperiodic ordinary positive orbit** from n, its starts are pairwise distinct. Whenever (3/2)^t(n+1)≤2^k the first t+1 starts are all less than 2^k. Hence P(k)≥t+1, and liminf P(k)/k≥log(2)/log(3/2)=1.70951… . In particular an integer orbit with eventual parity-factor complexity k+O(1) cannot diverge. The same bound applies on any aperiodic tail.
* For a **primitive positive cycle** with shortcut period A and minimum m, choose s,t≥0 such that 2^s m<m+2^k and (3/2)^t(m+1)−1<m+2^k. The starts from index −s to t lie in [m,m+2^k), so P(k)≥min(A,s+t+1). This also proves saturation P(k)=A whenever s+t+1≥A.
* In particular, for any sequence of such cycles and scales k with k→∞, log(m+1)=o(k), and k=o(A), the cycle inequality gives liminf P(k)/k≥1+log(2)/log(3/2)=2.70951… . Indeed s and t can be chosen respectively equal to k−O(log(m+1)+1) and k log(2)/log(3/2)−O(log(m+1)+1). Under a polynomial phase bound as above, every scale log(A)=o(k), k=o(A) qualifies. This excludes families with lower complexity at a qualifying scale. It does not supply a qualifying scale of low complexity on an arbitrary putative cycle.

The ordinary-map argument is analogous in method to the repository's centered-factor packet, research/integrated/factor-complexity/README.md. That packet has a different alphabet and induced dynamics. Its restrictions and its numerical bound are not used here.


### Formal and computational scope

CycleCore.lean proves the cut identities, the small-fixed-point bounds, and the integer packing comparison for two starts with an explicitly shared scaled shortcut word. The finite pigeonhole selection, the forward and backward envelopes, the rotation argument, and the logarithmic corollaries are proved in this note. The standalone cycle_check.py checks the three C2/C3 fixtures and every primitive positive binary cycle of periods 2 through 10 up to rotation for (C5.1), using exact integers and fractions.
