# Rigidity of ordinary affine shadows on the two-block language

**Scope: proposed written proofs.** This packet addresses the open residue in PR191 TCP-5. Let the accelerated odd map send a positive odd integer to the odd part of (3q+1). Let L and P be the *ordered* pairs of odd gaps (2,1) and (1,4). At odd block boundaries their exact maps satisfy

    8 q' = 9q+7       (L),       32 q' = 9q+5       (P).

Write N_L=8, N_P=32 and C_L=7, C_P=5. An alternative odd-to-odd block with exactly two odds and the same clock has carry 3+2^g, where g is its first gap. Thus the available carry sets are K_L={5,7} and K_P={5,7,11,19}.

PR191 at 37b3916633cd32a0c173b20bb18ec3a7ec290a63, research/two-sided-cycle-packing-20261124/README.md, TCP-5, gives the smaller shadow (60q+5)/83 on q=-7 modulo 83. The results below concern *uniform* rules on the unrestricted finite L/P language. No existence of an infinite positive ordinary L/P path is assumed. Rules valid only at states of one hypothetical orbit need not be uniform.

## Finite ordinary realization and coefficients

For any specified finite list of positive gaps with total clock A, word carry C and p odds, the input q is characterized by

    3^p q + C = 2^A modulo 2^(A+1).

Indeed the full equation fixes the final value as odd. Reducing at the first gap plus one bit shows its exact valuation, since the next odd position contributes an odd multiple of that power of two. Induction gives every remaining exact gap. The last gap is exact by the specified odd endpoint. The multiplier 3^p is invertible modulo 2^(A+1), giving infinitely many positive ordinary realizations. Adding 2^(A+1) to the source adds 2*3^p at the endpoint. Specifying additional finite letters before or after a marked edge still leaves infinitely many distinct ordinary inputs at that edge.

For a finite-context rule with affine assignments q ↦ a_s q+b_s and same-clock, same-odd-count output blocks, comparison on those realizations gives a_s=a_t across every allowed transition. Even if one is free to select among the allowed target words at each input, there are finitely many possible carries at that clock, hence one value occurs at infinitely many distinct inputs. The context graph of the unrestricted full binary language is strongly connected (append any desired history). Consequently the slope a is common and the associated carry is forced:

    C' = a C_i + N_i b_t - 9 b_s.                         (1)

This algebra describes necessary conditions for a uniformly available template. Equality of affine coefficients alone does not place a rational shadow on an actual integer path. Integrality of the shadow is imposed separately where used below.

## AR1. Fixed-size regrouping never removes the residue

Fix any k≥1. Give each word w of k original blocks *any* target odd-to-odd word with the same total clock and 2k odds. The target gaps can reorder the entire macro-word, including across original block boundaries. Suppose one affine map h(q)=a q+b, 0<a<1, satisfies all coefficient identities. If q and h(q) are integers, then 83 divides q+7.

**Proof.** Concatenating any two assigned targets produces a legal target of matching clock for each word of length n=2k. Its carry is odd because its first odd is at time zero and all remaining odd positions are positive. Put M=9^n. Two source words with a single P and all remaining letters L, differing by an adjacent LP/PL interchange, have the same N=2^A. The two-letter carries are 103 and 269. With j common L's before and n−2−j after, the absolute carry difference is

    166 · 8^j · 9^(n−2−j).

Composition of affine identities shows that the target difference equals a times the source difference. As both target carries are odd, their difference is even. Taking j=0 and j=n−2 shows that both 83a·8^(n−2) and 83a·9^(n−2) are integers. Bézout gives 83a∈Z, including n=2. Set U=83a. Then 1≤U≤82 and V=83b is an integer at any integer source with integral shadow.

On every original edge C_i≡7(9−N_i) mod 83. By composition, C_w≡7(M−N_w) for each word of length n. Multiplying the target identity C'_w=a C_w+(N_w−M)b by 83 now gives

    (V−7U)(N_w−M) = 0 modulo 83.

All-L and a word with one P have N's differing by a factor of four, so they cannot both equal M modulo 83. Hence V≡7U. Integrality of h(q) gives U(q+7)≡0. Primality of 83 and 1≤U≤82 finish the proof.

The conclusion holds for each k separately, with no bound on k. It allows arbitrary target odd counts *within* a macro-word, with total 2k odds. It does not quantify over source-dependent stopping times.

### Exact all-depth common divisor

More precisely, for every integer q and every k≥1 there is the identity

    gcd over |w|=k of |9^k q+C_w−N_w q| = gcd(166, q+7).

For k=1 the two entries before taking absolute values are q+7 and 166−23(q+7). For k≥2 let G be the gcd on the left. Comparing the two one-P words at each end, as above with n=k, shows that G divides both 166·8^(k−2) and 166·9^(k−2), and hence 166. This also ensures some entry is nonzero. All entries have parity q+1, so 2 divides G exactly when 2 divides q+7. Modulo 83 each entry is (9^k−N_w)(q+7). Since not all N_w equal 9^k modulo 83, the prime 83 divides G exactly when it divides q+7. The integer 166 is square-free, proving equality. In particular every odd source outside the PR191 residue has common discrepancy divisor exactly 2 at *every* positive macro depth.

## AR2. Bounded past memory collapses to one letter

Let b_s depend on the past m letters, with m arbitrarily large but finite. The next original letter i appends to this history and drops the oldest. Require (1) with C'∈K_i on every edge. For positive a<1, exactly the following triples of coefficients are possible. A row lists (d a, d b_L, d b_P) for the specified d, where b_L and b_P correspond to the *last* original letter. A constant rule can be given a dummy letter of memory.

| d | d a | d b_L | d b_P |
|---:|---:|---:|---:|
| 83 | 60 | 5 | 5 |
| 83 | 61 | 12 | 12 |
| 83 | 63 | 26 | 26 |
| 83 | 67 | 54 | 54 |
| 747 | 572 | 269 | 103 |
| 747 | 724 | −161 | 5 |

**Memory reduction.** Two histories which differ only in their oldest letter have the same successor upon appending L. Since both L-carries are in {5,7}, their offset difference is 2e/9 with e in {−1,0,1}.

Suppose m≥2. Fix any length-(m−2) word v and take parents L L v and L P v. On appending t=L or P their successors are L v t and P v t. The two successor offset differences equal 2e_L/9 and 2e_P/9. Subtract (1) for the two parent histories using each letter, then subtract these two identities to eliminate the parent difference. The resulting equality of integers implies 9 divides 16e_L−64e_P. Equivalently e_L−4e_P is a multiple of nine. Its absolute value is at most five. Therefore e_L=e_P=0. Every pair of histories differing only in the oldest letter has this form as a successor pair. Dropping that letter preserves (1) and the argument inducts to m=1.

**Classification.** Put H=b_P−b_L. The duplicate L successors give H∈{0,±2/9}. Write X for the LL target carry, Y for the PP target carry (first letter denotes previous input). Then

    a=(Y+23X−23H)/166,    b_L=7a−X,    b_P=b_L+H.

Test X∈{5,7}, Y∈{5,7,11,19}, and the two other carries X−9H∈K_L and Y+9H∈K_P. Keeping 0<a<1 gives exactly the table. Substitution verifies every listed row's four coefficient identities. This is a classification of coefficient identities. For actual positive ordinary paths, any claimed shadow still has to be an integer at each boundary. In every row d is divisible by 83, the slope numerator is nonzero mod 83 and both intercept numerators are congruent to seven times the slope numerator modulo 83. Hence **any integral shadow at any integer source requires 83|q+7**, even with arbitrary finite past memory.

## AR3. Pure finite lookahead also collapses

Let the offset depend on the next m letters, including the current label. Same per-letter clock and odd count are assumed. For any pair of length-m contexts differing only in the last letter, prepending an L to their common prefix yields a common predecessor. The difference of its possible L-carries shows their offset difference lies in {0,±1/4}.

For m≥2 and a length-(m−2) word v, compare the two contexts L v L, L v P before the same newly appended letter t. Make the same comparison for P v L, P v P. In both comparisons the target difference is the same, between v L t and v P t. Let Δ_L and Δ_P be the two parent differences. In the first and second comparisons (1) takes the form 9Δ_L=8Δ_target−E_L and 9Δ_P=32Δ_target−E_P, respectively, for even carry differences E_L,E_P. Thus 9(4Δ_L−Δ_P) is even. Write Δ_i=e_i/4, where e_i∈{−1,0,1}. Then 8 divides 4e_L−e_P, so this quantity vanishes and e_L=e_P=0. All terminal-letter siblings agree, and induction reduces the lookahead to the current label.

At one letter H=b_P−b_L∈{0,±1/4}. With X,Y the two loop carries the same coefficient formula as in AR2 holds. The off-diagonal constraints here are X+8H∈K_L and Y−32H∈K_P. The four constant rows of AR2 survive, together with the sole nonconstant row

    (d, da, db_L, db_P) = (664, 513, 271, 437).

Again 83 divides the displayed denominators and both offsets agree with seven times the slope numerator modulo 83. Thus every such integral contraction still requires 83|q+7.

## AR4. Finite state and the actual residue

Consider a nonempty finite set of states, with total transitions s↦L(s),P(s). Suppose each edge satisfies (1) with its prescribed clock and allowed carry. We require a fixed slope 0<a<1; on a strongly connected state graph, the ordinary cylinder hypothesis above suffices to force this slope. If 83a is an integer, an affine value y=aq+b_s can be integral at an integer q **only** if 83 divides q+7.

**Proof.** Set x_s=7a−b_s. The L coefficient identity says

    9 x_s − 8 x_L(s) ∈ {5,7}.

Every path of L transitions eventually cycles in a finite graph. On its cycle of length d, each x has denominator dividing 9^d−8^d, by summing the affine equations around the cycle. This denominator is odd. Backwards along the initial segment, x_s=(c+8x_L(s))/9, so all x_s have odd reduced denominators. Iteration of the same equations gives x_s as a weighted average of the future carries, since the remainder is bounded by a constant times (8/9)^j and tends to zero. Thus every x_s belongs to [5,7]. Neither step assumes that the infinite symbolic L path is a positive Collatz orbit.

Let U=83a, an integer between 1 and 82. At an integral anchor, z_s=83x_s=U(q+7)−83y is an integer. From 8z_L(s)=9z_s−83c and the odd reduced denominator of z_L(s) we deduce that z_L(s) is also an integer. Along this deterministic state sequence z is therefore an integer in [415,581], and modulo 83 is multiplied by 9/8=53. The residue 53 has order 82 since 53^41=−1 and 53^2=70 modulo 83 and 41 is prime. If z_s is nonzero modulo 83, some iterate has residue 1, and its successor has residue 53. Their only possible values are z∈{416,499} and z'∈{468,551}. But (9z−8z')/83 takes only the values 0,−8,9,1 on these four pairs, disjoint from {5,7}. This contradiction gives 83|z_s, and hence 83|q+7.

**One commuting diamond suffices to force the slope condition.** If P(L(s))=L(P(s)) at even a single state, compare the LP and PL words from s. Their clocks and end states agree, and their source carries differ by 166. Their target carries are odd. The affine constant terms give 166a equal to the difference between these target carries, so 83a is an integer. The preceding argument applies to the entire model with that common slope. In particular offsets depending on the actual residue (q+7) mod 83 do have a closed diamond: L and P act by the commuting units 9/8 and 9/32. This rules out a uniform same-clock contraction on *any* nonzero residue in the full nonzero-residue state model, even though those residues are a different class of information from finitely many preceding or following labels. It does not eliminate nonzero-residue infinite **ordinary orbits**. A genuinely orbit-specific and nonuniform construction may still escape this obstruction.

## AR5. Every finite causal state machine has the same obstruction

Let S be any nonempty finite set with total transitions L,P:S→S. Require the per-letter coefficient law (1) at every state and for both possible next inputs, with C'∈K_i and a common real slope 0<a<1. There is no commutation, synchronizing-word, or bounded-memory assumption. If some state s has y=aq+b_s integral for an integer q, **83 divides q+7**. In particular arbitrary finite causal storage cannot give a uniform integral affine repair on the nonzero classes.

1. **Lattice at an integral anchor.** Put x_s=7a−b_s as in AR4. That proof using the L edges alone shows x_s is rational with odd reduced denominator and 5≤x_s≤7 for every state. The two complete transition equations are

       8 x_L(s) = 9 x_s − c_L,
       32 x_P(s) = 9 x_s + 166a − c_P.

   The P equation implies 166a has odd reduced denominator. Write a=A/B in lowest terms with B>0. Hence B=2^u B₀, where u∈{0,1} and B₀ is odd. At an integral anchor x_s=a(q+7)−y, so the reduced denominator of x_s divides B₀. Put F=166aB₀=166A/2^u, an integer. Along any subsequent L or P path, z=B₀x remains integral: 8z' or 32z' is integral by the edge law and z' has odd reduced denominator. We may restrict to states reachable from this anchor.

2. **Fractional part identifies the offset.** If two reachable x values differ by a nonzero integer, interchange them to make the difference h positive. The interval bound gives h=1 or 2. The difference at their two L successors is also integral, since eight times that difference is the integer 9h−δ_L and the difference has odd reduced denominator. Here δ_L∈{0,±2}. If h=1 then 9h−δ_L is 7,9 or 11, impossible. If h=2, compare P successors. Their difference is integral by the same argument; 32 times that difference is 18−δ_P in [4,32] because |δ_P|≤14. It must equal 32, giving a successor pair differing by one, already impossible. Thus congruent x values modulo one are equal as rationals.

3. **Mixed clocks generate a translation on the prime-to-three quotient.** Write B₀=3^e D with gcd(D,6)=1. On z modulo D the transitions are the two permutations

       f(z)=9z/8,           g(z)=(9z+F)/32.

   Denominators here mean inverses in the finite residue ring. The compositions f∘g and g∘f have equal linear coefficient and constants 9F/256 and 8F/256. Their quotient as permutations is translation by F/256. Inverses of the two generators are positive powers on this finite set. Consequently every residue in the additive coset of the original z modulo gcd(F,D) is reachable by some positive word, even if transitions on S itself are not invertible. Every such word can be fed to the same original state thanks to totality.

   Since gcd(A,B)=1 and F is exactly 83A or 166A, gcd(F,D) is either one or 83, even when 83 squared divides D. If it is 83 and 83 does not divide q+7, the initial z=B₀a(q+7)−B₀y is nonzero mod 83: multiply by 2^u to read 2^u z≡A(q+7) mod 83. The f action modulo 83 multiplies by the generator 53, so its positive powers reach every nonzero coset modulo 83. Translations as above fill each of those cosets modulo D.

4. **Exclude every D>1 outside the residue.** Suppose 83 does not divide q+7. The accessible z modulo D then include all residues if gcd(F,D)=1, and all classes nonzero modulo 83 otherwise. Append h copies of L, with 2h≥e. This kills the component of z modulo 3^e because 8z'≡9z mod 3^e on L. On the D-component, the same append operation is a permutation preserving the accessible set just described. Specifically choose the pre-L residue z≡4·3^e·(8/9)^h modulo D. When 83 divides D this is nonzero modulo 83. After L^h the new z is divisible by 3^e and z/3^e≡4 modulo D. We obtain a state whose x has fractional part 4/D. Necessarily D≥5.

   In fact no such state exists for any odd D>4. Write x=5+v+4/D with v∈{0,1}. By the L equation, 8D x_L(s)=9D x−D c_L is an integer, and x_L(s) has odd reduced denominator, so this integer is divisible by 8. Thus (5+v−c_L)D+4≡0 mod 8. Since D is odd, 5+v−c_L must be 4 modulo 8. Its four possible values are −2,−1,0,1. This contradiction forces D=1.

5. **The remaining 3-primary states reduce to AR2.** Now B₀=3^e. Modulo B₀ the transition at each letter is z↦9z/N_i+constant, with N_i=8 or 32 invertible. Fix h≥1 with 2h≥e. For every word w of length h the final residue z mod B₀ is independent of the initial state, since its coefficient has numerator 9^h. By step 2 the final x is determined by this residue. Thus every word w defines one offset b_w=7a−x_w after reading w, independent of the reachable starting state. For each extension by t, reading wt gives the same offset as reading the last h letters of wt, so these b_w satisfy (1) on the full h-past state graph. This constructs the bounded-memory rule needed for AR2 without assuming an actual infinite positive ordinary script. Its classification says the reduced denominator of a contains 83 in every strict-contraction row. But B=2^u 3^e in this case, a contradiction.

This covers arbitrary finite deterministic *causal input states*, which always accept both next letters. It does not cover a predictor whose preloaded future letters can forbid the next input, a rule defined only on one orbit, or changing clocks. A finite machine with a different slope per state also has constant slope throughout any component reachable from an anchor, provided the full affine edge identities or the uniform ordinary-lift condition hold at every edge.

## Scope of the obstruction

PR191's residue is optimal in the classes described above. The first new missing ingredient for this route is a smaller-source construction on a nonzero class modulo 83, or an argument forbidding an infinite ordinary nonzero-class L/P path. These proofs do not eliminate an obstruction by reselecting a source at every finite horizon. They leave open combined two-sided windows, infinite-state constructions, variable clocks, source-sensitive rules outside the uniform affine hypotheses above, and other carry alphabets. No conclusion on the least global nonconverger follows without ordinary realization and descent on the uncovered cases.

An exact stress family works at every finite horizon k≥1. Start at q=2·8^k−7. After j≤k copies of L, the actual positive odd boundary is q_j=2·9^j·8^(k−j)−7. All k edges have precisely the prescribed two valuations, and q+7 is a power of two, so the residue guard fails at every one of those boundaries. More generally the ordinary-lift cylinder above meets *every* residue modulo 83 by CRT, even after prescribing an arbitrary finite mix of L and P. These are different sources for different horizons, and the argument proves no positive infinite exceptional orbit.


## Execution scope

MemoryShadow.lean proves every step of the bounded-past coefficient classification from the definition Legal through integralShadowResidue. ResidueOrbit.lean checks the forbidden fraction, integer differences, translation numerator and order computations used in AR4–5. AR1's all-depth gcd identity, AR3's general lookahead induction, and AR5's full finite-automaton deduction have written proofs here. They are not claimed as full Lean theorems. Commands, version pins, initial failed build, final axiom output and limited replay coverage are recorded under reports/astra-global-closure-20261124/audit.
