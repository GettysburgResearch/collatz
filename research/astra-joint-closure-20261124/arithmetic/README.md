# Full entropy after finite local cycle tests

**PROPOSED, written proof.** For the shortcut map on rationals with odd denominator, even and odd mean the parity of the reduced numerator. We construct positive rational cycles that satisfy arbitrary compatible finite local tests and an arbitrarily large lower bound on **every** phase. We also force arbitrarily specified factors into their reduced denominators. The number of distinct primitive cycles retains the full exponential rate of near-critical parity words. No constructed cycle is an integer cycle.

The classical word-to-rational-cycle formula is in J. C. Lagarias, [The set of rational cycles for the 3x+1 problem](https://matwbn.icm.edu.pl/ksiazki/aa/aa56/aa5614.pdf), Acta Arith. 56 (1990), 33–53. Its Theorem 2.1 credits the integer-cycle precursor to Böhm and Sontacchi; its primitive rotation count is also classical. The full modular branch group away from 6 was determined by K. Monks, K. G. Monks, K. M. Monks and M. Monks, [Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph](https://arxiv.org/abs/1204.3904). Our finite translation argument is included for completeness. The contribution here is simultaneous prescribed local behavior, forced cancellation and noncancellation, arbitrarily large real minimum, and retention of the critical entropy with bounded length overhead. The comparison with the full-denominator obligation is to [the project research map](../../../docs/RESEARCH_MAP.md) and PR188 at `f0e3cd96bab2d23791998bb92a86bf7ff2d51d4d`. This is an obstruction to a proof strategy, not an assertion of priority in the rational-cycle literature.

## Theorem

Fix a finite binary prefix P, a modulus M coprime to 6, a residue r modulo M, a unit u modulo 3^b (omit when b=0), and an integer E>1 coprime to 6M. One may also prescribe a factor J of the cancelled part, with every prime of J dividing M. Fix B>0 and epsilon>0. Put a=log(2)/log(3) and H(a)=-a log(a)-(1-a)log(1-a), using natural logarithms.

There is a constant C depending only on these fixed data with the following property. For every sufficiently large n there are exp(n H(a)+o(n)) distinct primitive positive rational cycles of periods L in [n,n+C] satisfying all the following conditions. The exponential rate is an upper bound as well as a lower bound.

* At one phase the parity itinerary begins with P, its reduced denominator is coprime to M and its residue modulo M is r, and its reduction modulo 3^b is u.
* Each phase exceeds B, and its reduced denominator is divisible by E. At every rotation the unreduced denominator and affine numerator both contain J, so the inspected factors may actually occur and cancel.
* For s odd steps in the primitive period, 0 < L log 2 - s log 3 < epsilon.

C has no claimed efficient bound. It can grow with tests, floor and precision. Prefixes can encode arbitrary 2-adic neighborhoods. For a fixed parity prefix of length h the actual initial residue modulo 2^h is unique by the inverse branch maps y ↦ 2y and y ↦ (2y-1)/3. Their linear factors have 2-adic valuation one, and reversing branches recovers every initial value in that cylinder. A positive rational cycle cannot have a phase divisible by 3: an odd step resets the value to a unit, and halving preserves this. Thus the unit condition has dynamical content.

## Proof

**Local return map.** Write G0(x)=x/2, G1(x)=(3x+1)/2. On residues modulo any N coprime to 6 these are affine permutations. Their word semigroup is a group, since inverse generators are positive powers in a finite group. It contains all translations: G1∘G0 and G0∘G1 have the same slope and their intercepts differ by 1/4. Composing the first with the inverse of the second gives a translation by the additive generator 1/4.

Take t>0 with 2^t=1 modulo EJ, and set d=2^(-t). For each prime power ell^m exactly dividing M let v=v_ell(2^t-1), and replace ell^m by ell^(m+v), obtaining a lifted modulus M'. Take N=M'E. By the Chinese remainder theorem choose c congruent to (1-d)r modulo M' and to 1 modulo E. The element F(x)=dx+c belongs to the word group, by composing G0^t with the translation by c.

At modulus 3^b use a fixed *terminal* suffix S. When b>0, take b ones followed by j zeros with -2^(-j)=u modulo 3^b. Such a j exists: 2 has order 2⋅3^(b-1), because v_3(4^(3^k)-1)=k+1 by factoring successive cubes (the second factor has valuation exactly one). G1(x)+1=(3/2)(x+1), so S sends every 3-integral input to u modulo 3^b. For b=0 take S empty.

**Free middle and correction.** Insert after P any n-bit word W having exactly floor(an) ones. For the permutation represented by PW choose a correction word V so PWVS represents F modulo N. The existence is the group property applied to the prescribed F and the known PW and S. Choose V from a fixed finite set of representatives, since only finitely many permutations occur. Thus its length is bounded independently of n and W.

For a word U set delta(U)=length(U) log 2 - weight(U) log 3. For the current PWVS, delta lies in a fixed compact interval I since 0≤delta(W)<log 3 and P,S,V have bounded lengths. Let k be a common multiple of the orders of G0 and G1 modulo N. Insert, just before S, zero and one runs of lengths ki and kj, respectively. This preserves the return map modulo N. The change in delta is iA-jD for A=k log 2 and D=k log(3/2). Their ratio is irrational by unique factorization. The set of these changes with i,j nonnegative is dense in the real line: jD modulo A is dense with arbitrarily large j, and i then adjusts the integer part. Choose 0<eta≤epsilon with exp(eta)-1≤1/(3B). For each z in I some such shift puts z in (0,eta). The corresponding open intervals cover compact I, so a finite set of shifts works uniformly. All padding lengths are therefore bounded independently of n. The completed words U have lengths in [n,n+C] and 0<delta(U)<eta. Their W substrings occur at one fixed offset, so different W produce different words for a fixed n.

**Physical realization.** The return is (3^s x+A_U)/2^L with positive integer A_U for s>0. Every cyclic rotation has a positive intercept as well. Because delta>0, the unique rational fixed point x=A_U/(2^L-3^s) is positive, with denominator prime to 6. Formal phase points are fixed points for rotations by conjugation, hence all lie in that same ring. At each step the numerator 3x+1 or x must be even in the 2-local ring for the next phase to be in it, so the itinerary actually follows every indicated parity. All local actions above consequently apply.

Write d_U=3^s/2^L and c_U=A_U/2^L. Since the return transformation equals F modulo N, d_U=d and c_U=c in that ring of residues (evaluate at 0 and 1). At ell^m exactly dividing M we have v_ell(1-d_U)=v because the slope agrees to precision m+v, and c_U-(1-d_U)r vanishes to the same precision m+v. Division by 1-d_U shows x=r modulo ell^m with x integral there. At each prime power p^e exactly dividing E, 1-d_U vanishes modulo p^e and c_U is a p-unit; thus v_p(x)≤-e. Also J divides 2^L-3^s since 1-d_U vanishes modulo J. At primes of J, x is integral and both branches preserve integrality, so J divides every rotation's affine numerator. Both branch maps preserve a negative p-adic valuation for p coprime to 6, so E divides the reduced denominator at every phase. The terminal suffix returns to x, giving its claimed ternary residue.

Over the cycle, multiplying consecutive ratios gives

    exp(delta(U)) = product over odd phases y of (1+1/(3y)).

The smallest phase must be odd, since halving a positive even phase gives a smaller phase. Its factor alone implies min(y) ≥ 1/[3(exp(delta(U))-1)] > B. This step uses every phase of the **same** rational cycle.

**Sharp rate and primitive periods.** The number of middle words is binom(n,floor(an))=exp(nH(a)+o(n)) by Stirling. Among all lengths in [n,n+C], at most O_C(n 2^((n+C)/2)) words are proper powers, by counting all possible roots of length at most half the full length. Their exponent is strictly smaller: 1/2<a<2/3 follows from 3<4 and 8<9, and H(a)≥H(2/3)>(log 2)/2. Each remaining word has primitive period and each cycle accounts for at most n+C rotations. Conversely every counted cycle has a word of length L in that interval with s=aL+O_epsilon(1). The binomial bound at these weights gives exp(nH(a)+o(n)) as an upper bound.

## Consequence and remaining global question

Even with a fixed source cylinder, arbitrary simultaneous congruences at any fixed list of primes, a near-critical coefficient, primitivity and an arbitrarily high floor throughout the cycle, full entropy persists among rational witnesses that fail whole-denominator divisibility. Diagonalizing over finite place sets gives positive rational periodic points converging at every finite prime to any specified ordinary integer prime to 3 while their real minima tend to infinity. Here convergence at a prime means eventual integrality and agreement to each fixed precision; the bad prime can move with the place set.

The theorem does not prescribe a fixed ordinary initial value and does not rule out tests with a word-dependent prime, modulus, height or precision. The missing ordinary step is to show that each nontrivial positive candidate actually has an uncancelled prime factor in its full denominator. Choosing such a factor while constructing other words gives no such assertion about a supplied word. No inference from rational periodicity to the dyadic companion's membership in Z[1/3] is made.


## Fixed-source height and the quantifier that prevents closure

For comparison, take the *unextended* length-h itinerary of one fixed ordinary n. Let y_h=T^h(n), C_h=3^s/2^h and D_h=2^h-3^s. From A_h=D_h n+2^h(y_h-n) and oddness of D_h, its canonical rational periodic point has reduced denominator

    b_h = |D_h| / gcd(|D_h|, |y_h-n|).

If n lies on an infinite distinct orbit, the reviewed [orbitwise reciprocal bound](../../integrated/orbitwise-boundaries/README.md) implies that V_h=y_h/C_h=n times the product of 1+1/(3y_i) over the odd phases i<h tends to a finite V>0. Distinct positive integer values tend to infinity, hence C_h tends to infinity. Thus

    b_h/2^h ≥ |1-C_h|/|y_h-n| → 1/V   (the limit is for the right-hand side).

For an eventually periodic orbit the endpoints stay bounded, and the coefficient tends to zero by the positive correction product over one period. Off exact return clocks the same inequality gives a positive lower bound independent of h for all sufficiently large h. At an exact return b_h=1. This reconstructs the physical-height conclusion already present in [PR195, round 6 at ef3496b5](https://github.com/GettysburgResearch/collatz/blob/ef3496b577ed7525d5e0c82a9b782819457403d5/research/astra-global-closure-20261124/round6/arithmetic/README.md); it is not a new fixed-source theorem.

An attempted application would recover a return using a subsequence of unextended prefixes with b_h=o(2^h). For a nonperiodic source this is impossible by the estimate, including for a transient source that really reaches 1. Convergence instead requires finding a tail that returns to the trivial cycle. Our CRT correction and padding add actual bits to a *word* without proving that the same n supplies those bits. The freedom to complete arbitrary middle words, even at full entropy, therefore cannot create the needed low-height actual tail. PR195's unrestricted counting result bounds the number with small reduced denominator by Y exp(o(L)) for denominator ≤Y. Combined with our lower bound this also shows that, in the family here, discarding all reduced denominators ≤exp((H(a)-gamma)n) for any fixed gamma>0 leaves the same exponential rate. This last statement uses PR195's source-qualified counting bound, not an independent proof of it. [PR195, complete-gcd counting](https://github.com/GettysburgResearch/collatz/blob/ef3496b577ed7525d5e0c82a9b782819457403d5/research/astra-global-closure-20261124/closing/cycles/README.md)


## Checks

[FiniteCycleTests.lean](FiniteCycleTests.lean) verifies four finite algebraic statements: the branch-swap translation, generation of translation by one, the outside-factor implication for an integer presentation, and cancellation at the lifted local modulus. [check_cycle.py](check_cycle.py) replays a primitive 184-step rational witness at residue 157 modulo 180. Every phase exceeds 48, the full cancelled factor is 5, and the reduced denominator is divisible by 7. The universal word construction and entropy estimate are written proofs. [Execution record](../../../reports/astra-joint-closure-20261124/arithmetic/EXECUTION.md)
