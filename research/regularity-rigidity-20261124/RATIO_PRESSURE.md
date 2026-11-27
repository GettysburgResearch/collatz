# Exact first-return pressure for ordinary multiplier-five failures

**Status:** written proof + exact BigInt certificate in ratio_pressure.js and RATIO_CONTROLS.json. No Lean verification of the certificate or analytic arguments. All counts refer to actual integer trajectories.

Let C be the basin of 1, and let F={odd units q: q in C and 5q not in C}. PR157's GCM-002 and the subsequent PR146 constructions supply the source-qualified equivalence F empty iff Collatz. We prove that if F is nonempty then its count below X is >=c X^(1/9) for every sufficiently large X, and that the same exponent holds for disjoint fixed-length blocks of failed comparisons in every macroscopic interval (block elements need not all be odd units). The antecedent is never assumed proved or refuted.

## 1. First-return cylinders

Start with odd x=r+2^h t and track T^h(x)=a+3^p t and T^h(5x)=b+5*3^k t, where p,k count odd inputs. At h=1 start r=1,a=2,b=8,p=k=1. Refining by the next bit v=0,1 replaces r by r+2^h v and updates a,b by applying T to a+3^p v,b+5*3^k v; update p,k by their parities. This is an exact whole-cylinder identity, by the affine-lift lemma. Stop at the first positive h for which p=k and b=5a. Then, with C_w=2^h a-3^p r,

    2^h T^h(x)=3^p x+C_w,
    T^h(5x)=5T^h(x).

Every such cylinder is disjoint from every other first-return cylinder, since both counts and their equal-ratio equality depend only on the exposed low bits. In particular C_w is positive and prime to 3 because p>=1 and the endpoint after the last odd input is a ternary unit (later halvings preserve this). C_w is odd since r is odd.

The checker enumerates every first-return cylinder with h<=25 and each odd count <=7. Pruning larger counts is sound since counts only increase. It found 473 records, with counts by p=1,...,7 equal to 0,1,1,5,15,88,363. The maximum carry is 11,692,997.

## 2. Exact inverse children and the pressure certificate

For an odd unit q and record (r,h,p,C_w), every e>=h satisfying

    2^e q = C_w (mod 3^p), but NOT modulo 3^(p+1)

gives the integer x=(2^e q-C_w)/3^p, prime to 6. It lies in the cylinder r modulo 2^h, since the numerator of x-r is divisible by 2^h and 3^p is odd. Its h-step endpoint is 2^(e-h)q, and the paired endpoint is 5*2^(e-h)q. Further simultaneous halvings reach q and 5q. For positive x this preserves the ordered pair of convergence labels.

Use only e in [max(h,bitlength(3^p)+1),400]. If q>=Q=2 max C_w+3 then x>=1.5q and x<=G q, where G=2^e/3^p<=2^400. Each eligible child is distinct: x determines its first positive ratio-five return with equal counts, hence its record, and the odd part of T^h(x) determines its unique parent q. Then e is also determined.

For each p the discrete logarithm to base 2 modulo 3^(p+1) has full period R=2*3^p. If ell(q) is l and d=ell(C_w)-l modulo R, the admissible exponents are those congruent to d modulo R/3 but not d modulo R. This reduces ALL odd unit q to 2*3^7=4374 classes.

Let S=2^48. For each record and exponent the checker computes the integer lower weight

    w=floor(S*(3^p/2^e)^(1/9)),

by finding the floor ninth root of floor(S^9 * 3^p / 2^e). All operations are exact. The maximum bound and root search use only integer arithmetic. Summing w over the admissible pairs for each of the 4374 discrete-log classes gave

    min sum w = 312442229426789 > 281474976710656 = S.

See RATIO_CONTROLS.json. The code additionally replays every recorded cylinder at three lifts (1419 literal controls) and all eligible children for four large odd-unit targets (867 ordinary inverse controls). These are checks of the formulas, not statistical samples used to infer the uniform inequality. Thus the following inequality is certified for every odd unit q, before imposing the height floor:

    sum_{eligible children} G^(-1/9) > 1.

Zero lower-weight branches may be omitted, as in the checker.

## 3. Global tree counting without collisions

If a fixed failed q is below Q, first replace it by an actual larger odd-unit failed ancestor from the elementary ratio-five block A of PR146: A(x)=(9x+7)/64 for x=49 mod64, with both arms preserving the 5-ratio and equal odd counts in six clocks. Choose e>=6 with 2^e q=7 mod9 but not mod27; there are always such e by the order of 2 modulo27. Then x=(2^e q-7)/9 in that cylinder reaches q after additional common halvings and exceeds q. Iterate (or choose e sufficiently large) to obtain a fixed root q0>=Q. For successes use the fixed root q=1,5 both converging, then the same growth construction.

From q0 form the finite-branching tree of Section 2. Each edge strictly increases the value, each vertex has unique parent under the first-return-plus-odd-part decoder. Thus different vertices anywhere in this rooted tree are distinct (if depths differ, decoding the shorter path would force the root to be a strict descendant of itself). At every vertex distribute probability proportionally to G^(-s) with s=1/9; the uniform pressure implies each edge probability <=G^(-s). For a descendant x its path probability is at most (q0/x)^s, since x<=q0 times the product of the G's.

Let Gmax=2^400. Stop the first time the path reaches X/Gmax. For sufficiently large X, the root lies below this threshold. All stopped nodes are <=X, all >=X/Gmax, and termination occurs within a finite number of edges because each child grows by at least 1.5. Their probabilities sum to 1, while each probability is <=(q0 Gmax/X)^s. Hence there are >=(X/(q0 Gmax))^s distinct such nodes. Their two convergence labels are exactly the root labels. This proves the count for every sufficiently large cutoff.

The exponent improves the elementary two-child exponent beta=1/log2(2^23/9) in PR146. The theorem is conditional on a fixed failure; it does not infer a failure from the symbolic cylinder enumeration.

## 4. Local block transport at the same exponent

For any fixed M and dyadic residue, use the simultaneous paired synchronizer of PR146 FIVE_RETURN_IN_EVERY_CLASS (pinned in SOURCES.md): some fixed h,p,r,z give

    T^h(r+2^h t+i)=z+3^p t,
    T^h(5(r+2^h t+i))=5(z+3^p t), 0<=i<M

on a cylinder, with common equal odd counts. If needed append block A by prescribing the next six endpoint bits; this makes p>=1 and z a ternary unit. This imported finite-profile existence assertion is distinct from the unproved global implication.

With L=2*3^(p-1) and ell modulo 3^p as in LOCAL_BLOCKS.md, one inverse A-lift q'=(2^e q-7)/9 can be made congruent to r'=-7/8 modulo 3^p: choose e>=6 within one period of 2 modulo 3^(p+2) so that 2^e q=9r'+7 modulo that modulus. The right side is a unit, so such e exists. Choose the representative of r' modulo 3^p in that equation. The inverse is a positive odd unit for q large, q'>q, and retains the ratio-five comparisons by Section 3. Since 9r'+7=r' modulo 3^p,

    ell(q')=ell(q)+e (mod L),
    log2(q')=log2(q)+e-2 log2(3)+epsilon, |epsilon|=O(1/q).

Iterate a bounded number k of these inverse steps. Their total clock E_k is bounded; q_k<=K_N q. With y=2^b q_k, the simultaneous endpoints are attainable when b+E_k=ell(z)-ell(q) mod L. The irrational rotation -2 log2(3) modulo L gives a finite net, exactly as in LOCAL_BLOCKS.md, and places y in any prescribed macroscopic log interval for q between a fixed lower threshold and c0 X. Then x=r+2^h(y-z)/3^p places all M starts inside the desired [AX,BX]. The first endpoint y determines q_k as its odd part; q is one of boundedly many forward iterates of q_k, so multiplicity is bounded. Disjoint block selection loses at most 2M-1. Apply the tree counts in Section 3 to either fixed ordered label pair. This proves macroscopic thickening at exponent 1/9, and supplies the two colors needed by the robust automaticity theorem.

## 5. Exact harmonic obstruction to merely enlarging a finite dictionary

This is a separate structural calculation. On the ternary-adic units Z_3^× let mu denote normalized Haar measure. For any record (h,p,C_w) of the full first-positive-return prefix dictionary for odd starts, and e>=h, put

    L_w,e V(q)=1_admissible(q) (3^p/2^e) V((2^e q-C_w)/3^p),

where admissible requires the inverse in Z_3^× (the same mod 3^p, not mod 3^(p+1) test). For any nonnegative integrable V, the change of variables q=(3^p x+C_w)/2^e maps Z_3^× injectively into Z_3^× with Haar scaling 3^(-p). Therefore exactly

    integral L_w,e V dmu = 2^(-e) integral V dmu.

For ANY finite selected dictionary D, the sum of these factors is strictly less than 1: disjoint odd first-return cylinders have total conditional binary Haar mass sum_w 2^(1-h)<=1, and even keeping all e>=h gives sum_e 2^-e=2^(1-h). A finite dictionary misses an infinite positive exponent tail. Thus no nonzero nonnegative integrable V can satisfy sum_D L_w,e V>=V almost everywhere. This rules out reaching harmonic exponent 1 solely by enlarging finite first-return pressure certificates, even with an integrable state-dependent potential. It does not rule out a different dictionary or a nonintegrable/ordinary-source argument.

For the full dictionary, the almost-sure return theorem of PR146/PR171 (source-qualified) gives total mass 1. This describes a probability law of contracting affine maps on the ternary units, with branch probabilities 2^-e, and a natural stationary-density problem. We do not assert such a density exists or is positive at specified ordinary points. Tao's Syracuse random variable suggests an analogy, but its geometric/iid valuation law is not this first-return law, so his Fourier estimates cannot simply be imported.

The harmonic moment obstruction is sharper. Under the full branch law, h has the conditional odd-source first-return distribution, with tail comparable to h^-1/2 by PR146's pinned return-clock estimates. Conditional on the record, e=h+b, where b is geometric with P(b=j)=2^(-j-1). Hence moments of log^+(G) of order 0<s<1/2 are finite, since log^+G<=e log 2. For s>=1/2, use that the length-h source parity word under binary Haar is uniform conditional on its first odd bit. The event p>0.6h has exponentially small probability at each h by the binomial Chernoff bound; the first-return restriction only reduces it. Consequently its total h^s moment is finite. On remaining records, log G>=h(log 2-0.6 log 3)>0. The tail lower bound for h implies its s-moment diverges for every s>=1/2. Therefore

    sum_w sum_{e>=h} 2^-e (log^+G)^s = infinity, s>=1/2.

Applying the exact Haar change of variables and Tonelli, the corresponding log-moment transfer has infinite integral for every nonzero nonnegative integrable V. This is an obstruction to a finite-mean harmonic renewal proof, not an ordinary counterexample to Collatz. In particular neither the full stationary density, nor an upper bound on the full set F, nor an original-floor descent is proved by this calculation.

## Remaining central target

The new lower pressure and local block transport give quantitative consequences of a failure, not its impossibility. The harmonic identity explains why finite pressure alone cannot reach the density endpoint. The open path is a genuinely infinite ordinary-source-sensitive renewal or a rigidity argument supplying the required automatic approximation. PR146's zero-density estimates for tripling defects and for terminal first-return states are NOT assumed to upper-bound the full multiplier-five defect set.