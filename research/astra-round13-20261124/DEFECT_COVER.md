# Repeated shortcut words with unrestricted intervening defects

Let a primitive positive rational shortcut cycle of period A and p>0 odd steps be cut at k>=2 distinct positions into U V_1, ..., U V_k. The same nonempty shortcut bit word U occurs disjointly at all cuts. The defect words V_i are arbitrary, including empty. Write S=|U|, N=#ones(U), and let E,L be the total numbers of zero and one bits among all defects. The common reduced odd denominator is d. Set eta=1-3^p/2^A. Then

    d > (k-1)/k * eta * 2^N / max(2^E,(3/2)^L).           (1)

The blocks may have different lengths, counts, and signs of their real logarithmic gains. More generally k-1 in (1) may be replaced by r-1 when there are r>=2 distinct boundary states.

**Proof.** On shortcut bits the two affine maps are x/2 and (3x+1)/2. Full-period positivity with at least one odd step gives eta>0. Each reduced denominator divides 2^A-3^p by the closing identity at that rotation. Since p>0 and A>0, the period denominator is odd and nonzero modulo three. At a reduced state x=a/d, literal shortcut parity is the parity of a because d is odd. The next state is (a/2)/d for even a, or ((3a+d)/2)/d for odd a. Both displayed numerators are integers. Before division by two the respective numerators a and 3a+d are coprime to d, using gcd(a,d)=1 and gcd(3,d)=1. Division by two preserves this coprimality. Thus every next state has exactly the same reduced denominator d.

Put theta=3^N/2^S. The full slope is theta^k (3/2)^L 2^{-E}=1-eta. For every bit word with j odd bits, the intercept b obtained by starting at zero satisfies 0<=b<=(3/2)^j-1: even steps can only reduce b and an odd step carries B to 3B/2+1/2. Thus the intercept of U V_i is at most (3/2)^{N+L_i}, where L_i counts the odd defect bits in V_i.

At any boundary q, compose the k affine block maps for a full return. In eta q each summand is the intercept of one block times the slopes of the following h blocks, with 0<=h<k. Those h prefix slopes contribute theta^h. The current and following defects are disjoint, so their total allowance for odd-step slopes is at most (3/2)^L. Their even steps can only decrease this bound. Divide by 2^S to obtain for each summand an upper bound

    2^{-N} (3/2)^L theta^{h+1}
      <= 2^{-N} (3/2)^L max(1,theta^k)
      <= 2^{-N} max((3/2)^L,2^E).

It follows that eta q/2^S <= k 2^{-N} max((3/2)^L,2^E). On the other hand all boundary numerators are congruent modulo 2^S because their shared U affine equations subtract to 2^S times an integer numerator difference equal to 3^N times the original numerator difference. The sorted span of r distinct numerators is at least (r-1)2^S. Their maximum exceeds that span by positivity. Apply the analytic bound at the boundary attaining this maximum. Primitivity and distinct marked offsets give r=k. This proves (1), in fact strictly when r>=2.

**Effective arithmetic consequence.** Absolute effective constants a>0 and C>0 satisfy eta >= a (p+1)^{-C}. To check this input, set Lambda=A log 2-p log 3, strictly positive. If Lambda>=1 then eta>=1-exp(-1). Otherwise A<= (p log 3+1)/log 2. Apply Gouillon (2006), Corollary 2.3 with fixed positive multiplicatively independent rational inputs 2 and 3, positive integer exponents A,p, degree D=1, and fixed sufficiently large heights. Its coefficient bound h is O(1+log(p+1)) when A=O(p), giving the claim since 1-exp(-Lambda)>=Lambda/2 on (0,1). See [the primary paper, pp. 127–128](https://doi.org/10.5802/jtnb.537). No external floor computation enters.

In particular every nontrivial primitive ordinary cycle and every disjoint cover by copies of U with arbitrary intervening defects must satisfy

    N <= max(E, L log_2(3/2)) + C log_2(p+1) + O(1).

For the common-prefix gap lift (v,w_i), mark the starts of v. If v has N gaps, the literal U has N odd bits; each remaining defect consists of one odd bit followed by w_i-1 zeros. For a fixed nonconstant terminal seed of length k and arbitrary shared prefixes v, p=k(N+1), E=sum_i(w_i-1), L=k. If all boundary states coincided, following the same prefix v from that state would reach the identical odd state just before each terminal gap. Its unique outgoing accelerated gap would be every w_i, contrary to nonconstancy. Thus there are at least two distinct boundary states. Even if the presentation is imprimitive, (1) with r>=2 shows d grows at least as a fixed positive constant times 2^N/(N+1)^C. This rules out all sufficiently long such lifts over the integers, regardless of the top norm. The more general cover also applies when the defects have unbounded lengths, variable odd counts and no common last letter.

The inequality is a constraint on every supplied cover. There is no theorem here guaranteeing that arbitrary cycle words admit a cover with sufficiently few defects, and it gives no exclusion for an arbitrary escaping ordinary source. Locally, any single repeated short word can leave nearly all of the cyclic word inside the defects.

**Relation to internal sources.** PR191 37b3916633cd32a0c173b20bb18ec3a7ec290a63, TCP-1 through TCP-3, supplies the shared-prefix congruence and treats equal clocks or individually contracting dictionaries; the sum of affine intercepts above uses only full-period contraction. The specific eight-letter lift has a stronger all-length bound in HIGH_FLOOR_NORM.md. This theorem is a written argument, including the external two-log estimate; the finite exact checks do not establish the asymptotic statement.

**Checks.** cover_control.py enumerates every primitive positive shortcut necklace through period 12 and every disjoint placement of at least two copies of a nonempty U on it. It verifies the strict complete-denominator inequality by exact rational arithmetic for 95,474 covers on 585 necklaces; 36,606 covers contain both expanding and contracting blocks, and 60,881 have an empty defect. DefectCover.lean formalizes the literal shortcut intercept estimate for arbitrary bit lists and the finite rational aggregation step, each checked by Lean 4.34.1 with mathlib d13f23b723b8a846827a245b89c10fc7d3f11612 and warnings as errors. The compiler receipt records the axiom output. The cyclic expansion, congruence and invocation of Gouillon remain written proofs.
