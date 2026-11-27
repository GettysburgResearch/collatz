# Near-optimal fixed-clock fibers of the full paired return law

24 November 2026. **PROPOSED written mathematics. Collatz remains OPEN.** This is a pointwise branching theorem on the *actual ternary-adic harmonic return law*, not a claim about every ordinary integer. The explicit exceptional-target quantifier is essential. The input is PR200's reverse-prefix domination, its stationary measure, and its source-qualified consequence of Tao's fine-scale mixing, frozen at 39918be724038ac550d77c7fc95d17e05251dfc6, continuation/REVERSE_RENEWAL.md. Section 5 below needs the fine-scale estimate; Sections 1–4 do not.

## 1. The exact inverse fiber at a common physical clock

Let T(x)=x/2 for even x and (3x+1)/2 for odd x. At a marked multiplier-five root both arms have ratio five, equal accumulated odd counts, and the next source input is odd. A dictionary block starts at such a mark, runs to its first positive equal-count ratio-five root, and consumes all subsequent zeros before the next odd bit (the sentinel, not consumed). With e shortcut clocks and p odd inputs, its map on the source is

    F_w(z) = (3^p z+C_w)/2^e.

The companion is 5 F_w(z) on its ordinary parity cylinder. The conditional binary-Haar word probability is 2^(-e); the initial odd bit is prescribed and the terminal odd sentinel is included in this probability. The source-qualified almost-sure return theorem in PR146 makes these probabilities a countable probability distribution. Every block has p>=1, and C_w is prime to 3. It is odd since the chronological first bit is odd.

An outermost-first iid sequence of these blocks defines an infinite affine composition. A finite prefix of that sequence has chronological parity word w obtained by reversing BLOCK order (not reversing the bits within each block). With total clocks e, odd count p, and chronological odd positions 0<=d_0<...<d_(p-1)<e, it has

    C_w = sum_(i=0)^(p-1) 3^(p-1-i) 2^(d_i),
    F_w(z) = (3^p z+C_w)/2^e,
    G = 2^e/3^p,
    beta_w = C_w/2^e.

A concatenated chronological word ending at a mark has a unique parse into dictionary blocks: scan from its first odd bit to the first equal-count ratio-five root, consume the intervening zeros up to the next odd bit, and repeat. Append the known terminal odd sentinel when parsing the last block. Thus every distinct complete word in this dictionary of concatenations has a unique outermost-first sequence prefix, and the probability of that sequence prefix is exactly 2^(-e), even when the number of blocks is not fixed.

For B>0 and a ternary unit q in U=Z_3^× define the finite multiplicity

    N_(e,p,B)(q) =
      #{distinct concatenated marked words w:
          |w|=e, odd(w)=p, beta_w<=B,
          q belongs to F_w(U)}.

This depends only on q modulo 3^(p+1). The image F_w(U) occupies exactly two unit residues at that precision, because the inverse (2^e q-C_w)/3^p must be an integer in Z_3^×. Define its exact harmonic fiber pressure as

    P_(e,p,B)(q) = N_(e,p,B)(q)/G.

Indeed choose a Haar-random tail in U and push it forward by every selected word with weight 2^(-e). The mass at each compatible fine cell contributed by one word is 2^(-e)/2, while normalized unit Haar mass of the cell is 1/(2*3^p). The density at that cell is therefore exactly N/G. This is a fixed-total and bounded-real-offset disintegration of the infinite harmonic transfer operator; it is not its stationary density.

### Ordinary attachment and an optimal upper bound

For a positive odd ordinary unit q>B, each counted word gives the integer

    x_w = (2^e q-C_w)/3^p = G(q-beta_w).

The image condition gives integer divisibility and a ternary unit; oddness follows from the odd C_w. Positivity follows from beta_w<=B<q. The first-arm parity word is the one attached to x_w: the complete affine formula of the word specifies its unique binary residue modulo 2^e (3^p is odd), and x_w is in that residue. On the finite binary cylinder, the companion starts at 5x_w and has the required ratio and counts at each mark. Therefore, literally,

    T^e(x_w)=q,       T^e(5x_w)=5q.

The terminal sentinel is legal because q is odd. All intermediate integers are positive. No appeal to a purely modular orbit or independent second arm is needed.

Distinct words with fixed e,p have distinct carries: the least power of two dividing C_w recovers d_0, because 3^(p-1) is odd and the later terms have strictly larger binary valuation. Subtract that first term and repeat to recover every d_i. Thus the candidates x_w are distinct. Also, for fixed q the carries lie in [0,B 2^e] in one congruence class modulo 3^p. This gives the uniform bound

    N_(e,p,B)(q) <= 1+B G.                             (1)

Hence growth like G^(1-o(1)) is the optimal exponential order for a fixed-clock, bounded-offset fiber. For B=1/2 all positive odd ordinary units are eligible and the actual starts lie in [qG/2,qG].

## 2. Real and ternary stationary coordinates together

Take the iid outermost-first block sequence W_1,W_2,... with probability weights above. Let (E_j,P_j) be the cumulative physical and odd clocks through j blocks and let C_j be the carry of the chronological word W_j ... W_1. The ternary compositions contract by at least 1/3 per block, so they converge to Q in U, with the unique stationary law nu constructed in the preceding checkpoint.

Read the bits of W_1 backwards, then W_2 backwards, etc., into one infinite reverse stream v_1,v_2,... . Its finite-prefix law has the exact bound (S2) of the pinned REVERSE_RENEWAL.md:

    Prob(v_1...v_l = a fixed word) <= C(l+1)^2 2^(-l).

This is a source-qualified input established there via a killed relative-level martingale and sentinel parsing. It is not a statement of iid bits in reverse. Apply the elementary binomial Chernoff estimate to all reverse words with |sum v_i/l-1/2|>eta. The probability is <=C(l+1)^2 exp(-c eta^2 l). For each fixed rational eta>0 this is summable over l. By Borel-Cantelli,

    (sum_(i<=l) v_i)/l -> 1/2 almost surely.

In particular P_j/E_j ->1/2. The *same sample* has a finite nonnegative real coordinate

    beta_infty = sum_(i>=1) v_i 3^(sum_(r<i) v_r) 2^(-i).

Each sufficiently late nonzero summand is exponentially small, since log(2) - (1/2)log(3)>0. At a block boundary E_j the partial sum is exactly C_j/2^E_j, by the carry formula. These partial sums are nondecreasing to beta_infty. No equality is asserted between the real limit and the ternary-adic limit in their different embeddings.

Write nu_B for the subprobability law of Q restricted to beta_infty<=B. We will use B=1/2, not a target-dependent cutoff.

### Full support with a bounded real offset

The A block from PR146 is the first-return word 101000 on x=49 mod64, p=2, e=6, carry 7. Direct replay gives q=7 at the base and 5q=35 on the companion. Padding with zeros makes its marked block map F_e(z)=(9z+7)/2^e for every e>=6. For every q in U, some e in [6,23] satisfies 2^e q=7 mod9 but not mod27: two generates the units modulo 27 and exactly two of the three fine lifts of 7 mod9 differ from 7 mod27. Thus q has a legal inverse A branch in U with a bounded e, and the inverse can be iterated at arbitrary ternary precision.

In the real coordinate these chosen A maps have slope at most 9/64 and offset at most 7/64, so every length-t composition maps a real tail beta>=0 to a number at most

    7/55 + (9/64)^t beta.

Choose L<infinity with Prob(beta_infty<=L)>0. For any B>7/55 choose t0 so (9/64)^t0 L < B-7/55. Given any ternary unit cylinder q mod3^k, choose a sequence of t=max(t0,ceil(k/2)) A inverse branches from a representative q. Every ternary tail in U maps into that cylinder because each branch supplies two ternary digits. The iid prefix probability is at least 2^(-23t); its independent tail satisfies beta_infty<=L with fixed positive probability. Consequently

    nu_B(q+3^k Z_3) >= Prob(beta_infty<=L) 2^(-23 max(t0,ceil(k/2))) > 0.    (2)

In particular nu_(1/2) has strictly positive mass and full support on U. This lower bound is deliberately not close to Haar.

## 3. Almost-sure near-optimal fixed-total inverse fibers

**Theorem PF1.** For nu_B-almost every q, for every epsilon>0 there exist infinitely many (e,p), e->infinity and p/e->1/2, with

    N_(e,p,B)(q) >= G^(1-epsilon).

More precisely, along almost every joint sample with beta_infty<=B, the inequality holds at ALL sufficiently late renewal boundaries (E_j,P_j), for each fixed epsilon>0. Here B>0 is fixed. The conclusion is a pointwise statement on the stationary law, not an averaged entropy statement.

Proof. Fix e,p, with G>1. Call a fine unit residue r modulo 3^(p+1) bad if N_(e,p,B)(r)<G^(1-epsilon). Consider the event that Q has such a residue, beta_infty<=B, and some cumulative renewal boundary equals (e,p). The sampled prefix must be one of the N compatible words since its real offset is bounded by beta_infty. For each such r, every candidate word has prefix probability 2^(-e), with at most one parsing. We can drop the constraint on the future ternary/real tail, and sum over all 2*3^p fine unit residues. The union bound is

    Prob(bad boundary of type (e,p), beta_infty<=B)
       <= 2*3^p * G^(1-epsilon) * 2^(-e)
       = 2 G^(-epsilon).                             (3)

This is an exact counting and probability inequality; it does not divide by an unknown stationary density. For |p/e-1/2|<=1/20, log G>=c e with an absolute c>0. Thus the sum of the right side over all e and these p is finite (there are at most e+1 possible p). Almost surely there are only finitely many bad boundaries of balanced type. By Section 2 every late boundary is balanced. Take a countable intersection over epsilon=1/m, m>=2. Projection of the joint full-measure event gives the asserted nu_B statement. All limits keep the same sampled Q and its same real-coordinate bound. QED.

For B=1/2, define Good to be the set of q for which the limsup exponent of N along balanced types p/e->1/2 is one. Equivalently for all integers m>=2 and N>=1, some e>=N and |p/e-1/2|<=1/m have N>=G^(1-1/m) and G>1. Equation (1) ensures the exponent cannot exceed one. Each such existential condition is open (a union of clopen cylinders). PF1 and (2) show that each is dense. Thus Good is a dense G_delta of full nu_(1/2) measure. This does not imply that it contains any prescribed ordinary integer: a countable dense set may miss a dense G_delta entirely.

**Ordinary consumer.** If a fixed positive odd ordinary unit q belongs to Good, then for arbitrarily large cutoffs X=qG it has at least X^(1-o(1)) distinct positive odd unit sources in [X/2,X] with a single common physical clock for the paired landing (q,5q). This follows directly from Section 1, since q is FIXED and log q is constant. If q is an actual failed five-comparison, every one of these sources is also a failed comparison. No assertion that any failed q, or indeed every ordinary q, belongs to Good is made.

## 4. Why this advances the harmonic program

The preceding checkpoint established full stationary dimension but did not extract large physical inverse fibers at a fixed total clock and bounded real carry. PF1 proves the optimal logarithmic fiber exponent for typical Q under the correct joint harmonic law, and (2) shows the bounded-offset condition loses no open cylinder.

In terms of the exact pressure P=N/G the missing pointwise statement can now be written as

    for every fixed positive odd ordinary unit q:
    along arbitrarily large balanced (e,p),
    P_(e,p,1/2)(q) >= exp(-o(e)).                    (PT)

Equivalently, the normalized density of the actual bounded-offset, fixed-clock prefix law at the specified fine cell should not be exponentially small along all balanced scales. This is stronger and more specific than positivity of support, existence of a stationary density, or a lower bound for a stationary cylinder at q. Those latter bounds include overshooting words with many more odd inputs than the modulus can certify. PT controls the exact needed precision p+1 and the exact total e.

One possible source-preserving transfer would suffice for PT's ordinary branching consequence: for each fixed q, find at the same scales a paired ordinary ancestor q' (q',5q' land at q,5q) in a Good fine cell of a good type (e,p), with log q'=o(e). Then all N sources for q' have height <=q'G=exp(o(e))G and inherit the original pair labels. A change to arbitrary unrelated ordinary targets does not suffice. The available elementary A routing costs exponential ternary precision and does not supply this subexponential height.

Even PT by itself would not prove the full conjecture: it would give a near-linear lower counting exponent for actual failed comparisons, conditional on a failure. A genuinely opposing upper bound or a separate closure mechanism is still necessary. No such upper bound for the full failed-five set is imported from the tripling-defect estimates.

## 5. Quantitative abundance of fixed-total good fine types

**Theorem PF2 (with Tao input).** Fix B=1/2 and 0<delta<1. For every sufficiently large N there is an integer clock type (e,p) with

    N <= e <= 2 N^4,       |p/e-1/2| <= N^(-1/4),

such that at least

    c N^(-8) 3^(p+1-2(p+1)^delta)

distinct ternary unit residues r modulo 3^(p+1) each satisfy

    N_(e,p,1/2)(r) >= G^(1-N^(-1/3)).                (4)

In particular the number of favorable fine cells is 3^(p-o(p)) and their inverse multiplicity is G^(1-o(1)), both at a common physical and odd clock. Constants may depend on delta and the pinned probability estimates; there is no uniform lower bound at every fine residue.

Proof. Take the first cumulative marked boundary E_j>=N. It occurs at j<=N. By the pinned first-return tail plus geometric padding, the probability that any of the first N block lengths exceeds N^4 is O(N^-1), so except for that probability E_j<=N+N^4<=2N^4. The reverse-prefix likelihood bound and binomial Chernoff estimates give probability o(1) that any e>=N violates the stated balance (use the deviation N^-1/4, then sum C(e+1)^2 exp(-c e N^-1/2)). Equation (3) with epsilon=N^-1/3 similarly gives o(1) for a bad balanced boundary at any e>=N, since sum_(e>=N) O(e exp(-c e N^-1/3)) tends to zero. The event beta_infty<=B has fixed positive probability by (2). Thus for all large N there is mass bounded below by a positive constant of joint samples realizing a good selected boundary in the displayed finite range.

There are O(N^8) possible integer pairs (e,p). Choose one by pigeonhole whose corresponding event has probability >=c N^-8. Its projection is contained in the union of the good fine cells at k=p+1. The stationary law nu dominates the projected subprobability measure. By (F) in the frozen REVERSE_RENEWAL.md (which uses Tao's published fine-scale mixing for the ordinary iid Syracuse law through the reverse-domination theorem), cells having nu mass >3^(-k+2k^delta) have total nu mass O_(delta,A)(k^-A) for every A>0. Indeed their number is <=3^(k-2k^delta), exactly the thin-set threshold. Choose A>9, and note k>=N/3. Removing all heavy cells discards o(N^-8). The remaining cells each have mass at most 3^(-k+2k^delta). The claimed count follows by dividing their remaining projected mass by this bound. Equation (4) holds by construction. QED.

The same input shows Good has Hausdorff dimension one inside EVERY nonempty ternary open cylinder. In fact nu_B is nonzero there by (2) and is dominated by nu. The previous near-Haar upper cylinder bound holds nu_B-almost everywhere; restrict to a subset of positive nu_B mass with a uniform eventual bound nu(C_k)<=3^(-s k) for any fixed s<1. For a ball meeting this subset its restriction has mass bounded by the same estimate, since ternary cylinders of fixed depth partition U. The elementary mass distribution argument gives dimension >=s, and let s tend to 1. Good has full nu_B measure by PF1.

The large set of good cells in PF2 still need not include a fixed ordinary target, nor even the small-height paired ancestors of that target at the required precision. This is the exact residual gap. No priority assertion against the developing literature on fixed-total ordinary routing (e.g. rStation paper 37, Lemma 11 and Theorem D) is made: that source gives one-arm pointwise routes, not the ratio-five paired fiber estimate PT.

## 6. Executed exact controls

See controls.js and CONTROLS.json. The finite replay enumerated all first-return cylinders through clock 15, padded by 0–3 zeros, and concatenated one or two blocks through total clock 24. It checked the unique marked parse, recovered every parity word from its carry, checked the reverse-real-offset identity, verified exact fine-residue incidence and the upper bound (1), and replayed selected whole-word ordinary inverses to both supplied endpoints at the same clock. The controls are not empirical evidence for the asymptotic conclusion (which follows from (3) and the stated probability inputs). The finite Lean candidate is separate and has not been compiled.