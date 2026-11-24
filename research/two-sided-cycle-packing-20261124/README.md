# Two-sided cycle packing, noncoprime norm certificates, and an integer shadow of the low scalar alphabet

24 November 2026. **PROPOSED written theorems. Collatz remains OPEN. LEAN VERIFICATION REQUIRED: the GPT-6.2 Extra High authoring environment has no Lean, Lake or Elan. The accompanying Lean file is candidate source only; no compiler/kernel/axiom audit has been performed.** See the exact proof scopes below.

Three attacks on the central obstacles are recorded separately. No independent subagents were available in this session; these are separate mathematical lines of attack by the author, not independent reviews.

## Source pins

- PR188, beed685ab713923191ae40c9559bf7400298d2d3, research/scalar-carry-cocycle-20261124/RESIDUE_NORM.md, RN1--RN3: full gcd norm for coprime clock counts and its explicit missing noncoprime extension.
- PR185, 2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d: polynomial residual vs full numerical gcd. PR178, 398b3a04da071e96362005792417bd5cf8cc6497, research/literature-push-20261123/arithmetic/FULL_NUMERICAL_SEPARATION.md: disjoint periodic packets, a different explicit family.
- PR177, 25bf9b95a9404998e8e55aa401773488cd3dd4b8, research/lean-exact-witness-global-20261121/construction-attacks-20261123/descent/TEMPLATE_SELECTION.md, TS5/TS6/TS14: uniform rational-center bound, source-qualified Matveev plus exact continued-fraction certificate. Only Section 3 below uses this input; the other results are elementary.
- PR183, 68345f60a4f757acb42a69a4ac95910f8ce26163: independent repeated-block classification; our Section 3 is an alternative for contracting dictionaries, not a substitute for arbitrary expanding atoms.
- PR182, f94a2ae1caba9a1857feda892ee1779695eea9d2, research/carry-tower-round10-20261123/ARITHMETIC_TOWER.md, eqs. (1)--(3): L/P alphabet, actual shifted coordinate and scalar 7/8. Latest PR182 dbe1860f7da36f2cc316b038d38a7fb8748dec2a and PR187 099058f3f2602a48e109c964899f0a9a2a223338 add fixed-source repetition. The shadow in Section 5 is not a repetition argument.
- PR173/184 forced dyadic band and exact ordinary mergers: Section 2's two-sided comparison provides a finite exact equality consumer; it does not establish coverage.
- Main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a. No global premise or custom axiom is installed.

## 1. Setup

Use the shortcut map T(x)=x/2 for even x, (3x+1)/2 for odd x. A word w of A shortcut bits with p ones at positions d_i (0<=i<p) has affine action

    2^A T_w(x)=3^p x+C_w,
    C_w=sum_i 3^(p-1-i) 2^d_i.

For a positive rational cycle with literal parity determined by the numerator over an odd denominator, the common reduced denominator d is coprime to 6: the closing equation has denominator 2^A-3^p, with p>0, and is coprime to 6. Every subsequent rational state has exactly that same reduced denominator, since multiplying a reduced numerator by 2^(-1) or 3 and adding a multiple of d preserves coprimality with d. An all-even positive cycle is impossible.

An equal future parity prefix of length L forces the difference of two integer numerators over the same odd d to be divisible by 2^L: subtract the affine equations and use gcd(3,2)=1. A common past parity suffix with s ones forces the current numerator difference to be divisible by 3^s: subtract its two actual affine equations and use the same coprimality. No probabilistic premise and no prescribed finite witnesses changing with a horizon are required.

## 2. Two-sided packing (TCP-1)

Consider a literal positive rational cycle, partitioned into blocks all having A bits and p ones. Put N=2^A, M=3^p, D=N-M>0. Positivity of D follows by multiplying the complete positive cycle identities (some odd step occurs). Write the blocks as a common prefix u of length l, variable middle v_j of length m and q ones, and common suffix w with s ones, with l+m+|w|=A. The middle odd count is fixed because the total counts are fixed. Empty prefix or suffix is allowed. Define

    G=2^l 3^s,
    Delta=max_j C_(v_j)-min_j C_(v_j).

Let r be the number of distinct block-boundary states (if the whole concatenation has primitive shortcut period rA, all r boundaries are distinct). Let n_j=d x_j be the integer boundary numerators.

**TCP-1.** For r>=2,

    d Delta >= D (r-1).                            (1)

Proof: all boundary numerators have the same residue modulo 2^l (common future prefix) and modulo 3^s (common past suffix, using the previous cyclic block). Thus their differences are divisible by G. The sorted r distinct numerators have span at least G(r-1). On the other hand their actual equations are

    N n_(j+1)=M n_j+d C_j.

At a boundary attaining the minimum, its predecessor is at least that minimum. Hence D n_min >= d C_min. Similarly D n_max <= d C_max. In composing u, v_j, w, the carry is

    C_j=3^(q+s) C_u + 2^l 3^s C_(v_j) + 2^(l+m) C_w.

Therefore C_max-C_min=G Delta exactly. Combining the span bounds and canceling G proves (1). If Delta=0, all boundaries coincide and r=1. In particular the entire conclusion is about the complete reduced denominator d, not a selected divisor or polynomial denominator.

A uniform explicit upper bound for Delta is

    Delta <= (2^(m-q)-1)(3^q-2^q).                 (2)

For q=0 or q=m the carry is constant. In general each odd position lies between i and m-q+i, so the carry lies between 3^q-2^q and 2^(m-q)(3^q-2^q). These extremal bounds are attained by the all-ones prefix and suffix.

### Complete adjacent-swap exclusion, arbitrary number of blocks

Take variable middle v in {10,01}. Their carries are 1 and 2, hence Delta=1. For any mixed literal rational cycle, d>=D(r-1). In particular no positive integer cycle of primitive period >A can use any arbitrary mixture of the two blocks u10w and u01w. For A>=3, D>1: if D=1 then 3^p=2^A-1=7 mod 8, impossible. For A=2 the only pair is 10 and 01, with fixed centers 1 and 2; a cycle cannot mix because each state already returns to itself after two steps. Thus even this small case has no mixed integer cycle. This result allows arbitrary common words, arbitrary order and number of switches, all clock gcds, and does not rely on polynomial cancellation or Baker bounds. It does not exclude a repeated single atom's own cycle.

More generally adjacent *odd-gap* swaps of a and a+k share a prefix through the smaller gap; after stripping that prefix and common suffix, their carry range is 2^k-1 (one odd position in the intervening k+1 bits). Therefore d(2^k-1)>=D(r-1). This covers both small and arbitrary k, with no conclusion if the bound permits d=1.

### Repeated multi-block factors (TCP-2)

If two distinct boundaries have the same next h complete blocks, then their common future prefix is at least hA+l (the additional l belongs to the next block). Their common past suffix still has s ones. Thus the same argument gives

    d Delta >= D 2^(hA).                           (3)

If their preceding k complete blocks also agree, the additional common past has kp ones, giving D 2^(hA)3^(kp) on the right. This is a finite two-sided ordinary comparison and retains the initial denominator. If at most K block types occur and r>K^h, pigeonhole ensures a repeated future h-block word and hence (3). The exponential denominator bound is independent of the number of polynomial factors that cancel.

For arbitrary fixed ordinary trajectories, not necessarily cyclic, the same congruence says that two states with the same L future bits and a common suffix with s prior odd steps coincide whenever their distance is strictly below 2^L 3^s. For two marked states in the same PR173 dyadic shell d0, the available width is at most 70*2^d0/(d0+1); the comparison may therefore use a smaller binary horizon if a shared ordinary suffix has been constructed. This is only a finite equality consumer, not a construction of a smaller-source partner.

## 3. Entire contracting dictionaries: no atom reuse at equal clocks (TCP-3)

This section uses the exact TS5 result from the pinned PR177 source, with its explicitly retained Matveev/continued-fraction dependency:

    C_w/(2^A-3^p) < (2/3)2^A                       (4)

for every contracting nonempty parity word (p=0 has center zero). It concerns any legal finite word's rational fixed center. We do not claim a new independent proof of the source-qualified input.

Consider a positive rational cycle partitioned into words all contracting, possibly with different counts and lengths. For an individual block the output is a strict convex combination of its input and its own center. The cyclic min/max argument gives

    min_w center(w) <= x_j <= max_w center(w)
    x_j < (2/3)2^Lmax,

where Lmax is the largest block length. Every repeated word of length L among distinct boundaries forces a numerator difference divisible by 2^L. If a given word occurs at h distinct boundaries, sorted differences imply

    h-1 < (2d/3) 2^(Lmax-L).                      (5)

For an integer cycle d=1, every maximal-length atom occurs at most once. When all words have the same length A, EVERY distinct atom occurs at most once, even if their odd counts vary. Thus any primitive positive integer cycle assembled from a finite contracting equal-clock dictionary of K words has at most K blocks and no repeated word. This improves the effective classification of this special all-contracting subcase: enumerate only cyclic orders of distinct atoms, retaining their exact full closing arithmetic, rather than arbitrary repetition exponents. For variable clocks (5) supplies a finite multiplicity cap for each word and a finite total cutoff. It does not cover mixed expanding/contracting dictionaries, which remain the key difficulty.

For rational cycles with equal clock A, a repeated h-block word gives the stronger denominator condition

    d > (3/2)2^((h-1)A).                          (6)

The derivation uses the strict height bound and distinct numerator difference >=2^(hA). All statements here are conditional on the actual cyclic partition and the scoped proven input (4); no universal existence of such a partition is asserted.

## 4. Noncoprime residue-defect norm (TCP-4)

This attacks PR188 RN1's explicit missing extension. Consider ANY candidate cycle word of p>0 odd positions, length A, D=2^A-3^p>0. Write g=gcd(A,p), A=ga, p=gb, gcd(a,b)=1. Set X=2^a, Y=3^b. Choose Bezout integers u,v with bu-av=1. Rotate at an odd position minimizing e_i=b d_i-a i; this makes e_i>=0 for the rotated word, by periodicity of e along the cyclic indices. The integrality of the rational cycle and the complete reduced denominator are invariant under such rotation (Section 1).

For every divisor ell of g define

    D_ell=Y^phi(ell) Phi_ell(X/Y),
    R_ell=Z[W,T]/(Phi_ell(W), T^b-2 W^v),
    F=sum_i T^(e_i) W^(u i-v d_i),   H=(T-1)F.

Phi_ell is the cyclotomic polynomial. Negative W exponents are reduced modulo ell; W^ell=1 in the ring. R_ell is a free integer module of rank b phi(ell), using its two monic polynomial relations. Let J_ell be the integer determinant of multiplication by H on this module. All ring operations are finite and preserve exact integer coefficients. These definitions include ell=1 (W=1). Also D=prod_(ell|g) D_ell, each D_ell positive and coprime to 6.

**TCP-4. Full prime-power bound, without any coprimality of the factors D_ell:**

    gcd(C,D_ell) | J_ell,
    gcd(C,D) | prod_(ell|g) gcd(D_ell,J_ell).      (7)

Equivalently the complete reduced denominator is a multiple of

    prod_(ell|g) D_ell/gcd(D_ell,J_ell).           (8)

Proof: let m=gcd(C,D_ell)>1; 2 and 3 are invertible modulo m. In Z/mZ set w=X/Y, t=2^u 3^(-v). The Bezout identity gives

    t^b=2 w^v,   t^a=3 w^u,
    2=t^b w^(-v),   3=t^a w^(-u).

Since D_ell=0 mod m, Phi_ell(w)=0. Thus evaluation W->w,T->t is a ring homomorphism R_ell->Z/mZ. It gives

    F(t,w)=sum_i 2^(d_i)3^(-i)=3^(1-p) C=0 mod m.

The evaluation row on the free basis annihilates the multiplication matrix of H modulo m. Multiply by its integer adjugate; the coordinate for the constant basis element 1 yields m|J_ell. This works unchanged for composite m and prime powers, even if the norm is zero (then gcd(D_ell,0)=D_ell). To pass from factorwise gcds to (7), compare prime valuations: min(c,sum_i d_i)<=sum_i min(c,d_i). In particular repeated primes across cyclotomic factors are NOT discarded. The product on the right divides D, and (8) follows. For a nonintegral candidate, all estimates concern the complete reduced denominator of its actual rational cycle.

### Exact zero-norm classification

Over C, R_ell decomposes over zeta primitive ell-th roots and tau satisfying tau^b=2 zeta^v; these roots are simple. Set z=tau^a zeta^(-u), so z^b=2^a zeta^(-1), and the tau->z correspondence is a bijection since gcd(a,b)=1. The evaluated F is z^(1-p)Q(z), with Q(Z)=sum_i 2^(d_i) Z^(p-1-i). Since |tau|=2^(1/b)>1, tau-1 is never zero. Thus

    J_ell=0 iff Q and (2^a)^phi(ell) Phi_ell(Z^b/2^a)
                      have a common complex root. (9)

This exactly identifies the zero-norm obstruction in terms of structural polynomial cancellation; it is not an assertion that primitivity alone prevents that cancellation. For ell=1 the determinant is always nonzero: R_1=Z[T]/(T^b-2), and the reduced F has positive coefficients, is nonzero of degree <b. Eisenstein irreducibility applies. For g=1 this reduces to RN1 of PR188. For g>1 it supplies a nonzero principal certificate and all cyclotomic component certificates, including shared prime-power accounting.

If any D_ell fails to divide J_ell, the word cannot close at an integer. The remaining global challenge is to bound the nonzero norms or refine the zero components after exact polynomial cancellation. No uniform strict saving is claimed; the expression can be vacuous for individual words. The norm extension is an all-clock arithmetic identity, not a universal exclusion.

## 5. A smaller ordinary shadow of an exact low-phase script (TCP-5)

Use PR182's actual two-odd-step alphabet L=(2,1), P=(1,4):

    L(q)=(9q+7)/8,  P(q)=(9q+5)/32,
    8*4^s(q'+7)=9(q+7)+166s, s in {0,1}.

On any actual positive ordinary infinite L/P tail, divisibility of q+7 by 83 is invariant in both directions along every edge (83 is coprime to 2 and 3). Suppose 83|q_0+7. Define the exact integer shadow

    y_j=(60 q_j+5)/83 = 60(q_j+7)/83-5.

All y_j are positive odd integers. Direct substitution gives

    L'(y)=(9y+5)/8,
    P'(y)=(9y+5)/32.

These are literal odd-map blocks L'=(1,2), P'=(1,4): y and y' odd and the corresponding full affine equation imply y=3 mod4, first gap one, and the second gap is respectively two or four. No shadow trajectory is merely symbolic. Because every shadow block begins with gap one, it cannot reach 1 (whose gap is two forever). This constructs an actual smaller nonconvergent source without assuming the original was periodic.

Let q_* be the minimum over the original block boundaries, which exists by ordinary well-ordering. Every original odd state, including intermediates, is at least (3q_*+1)/4, whereas

    (60q_*+5)/83 < (3q_*+1)/4.

Thus a tail satisfying 83|q+7 cannot contain the global least positive nonconverger at any of its odd states. This comparison is with the original tail minimum, not an arbitrary earlier source preceding that tail. For an original positive integer cycle it produces another positive integer cycle with strictly smaller minimum (the conjugacy is injective at boundaries and both maps are actual).

If an L/P cycle consists of r blocks and S paid blocks, its complete clock is A=3r+2S and odd count p=2r. Closing the shifted recurrence gives

    (2^A-9^r)(q+7)=166 times an integer.

Therefore, if 83 does not divide 2^A-9^r, the shadow applies. If the globally least nonstandard positive cycle has this alphabet throughout, it MUST satisfy

    83 | 2^(3r+2S)-9^r,
    2S=59r mod 82.

For the congruence, 2 has order 82 mod83 (2^41=-1 and 2 not equal -1), and 9=2^62 mod83. In particular r must be even; writing r=2t gives S=18t mod41. This excludes that alphabet with odd block period from the global-minimum cycle search, not from all cycle existence. The smaller cycle is not asserted to have the original scalar 7/8, so this cannot be used at the least element of the 7/8 level set without another argument. Arbitrary larger carry excursions and the 83-nonzero residue class remain open.

## 6. Scope and next closing steps

TCP-1--2 are full denominator bounds for arbitrary cyclic schedules with equal counts and two-sided common words. TCP-3 gives a general no-reuse result for contracting equal-clock dictionaries using the pinned TS5 result. TCP-4 resolves the algebraic extension of RN1 to noncoprime clocks, including the exact zero-norm boundary. TCP-5 gives a genuine smaller ordinary shadow in one nontrivial scalar alphabet, including a minimum-cycle obstruction. None of these statements asserts Collatz.

The main next targets are (a) force a useful common-word partition on an arbitrary hypothetical cycle or obtain a norm saving on at least one surviving factor in TCP-4; (b) generalize the shadow construction across changing scalar-carry types while preserving the global minimum comparison; (c) use two-sided equality to construct a smaller ordinary source at a forced band, not just test supplied histories. No universal selector, universal triadicity, or critical collision upper bound has been produced here.

## 7. Validation and formalization

The written arguments in Sections 1--2, 4--5 are elementary; Section 3 uses the exact external-source-qualified bound from PR177 TS5. The separate Lean draft covers finite spread/carry inequalities and the integer-shadow algebra, with group Bezout identities as a finite core of the norm construction. The full cycle decomposition, determinant, asymptotic implications and actual scalar construction are written proofs, not new Lean-verified theorems.

**No Lean executable was available.** Compile the candidate file with Lean 4.34.1 / Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612 and warnings as errors, inspect every print-axioms output, fix failures, independently reconstruct the written statements, and record exact checked head. No repository integrity check or external independent review was run.
