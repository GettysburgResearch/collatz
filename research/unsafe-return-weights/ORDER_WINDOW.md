# The multiplicative order sets a sharp merger-clock scale on guarded unsafe families

**Status: PROPOSED.** For all sufficiently large a let o_a be the order of 3/2 modulo d_a=3^a−2^{a+1}. There are explicit, nonempty ordinary source progressions in the genuine unsafe re-entry support whose minimum cheaper-merger clock ell(n) satisfies

    c o_a/a <= ell(n) <= C o_a/a,

with absolute constants. The lower bound applies to every positive witness on both arms. The upper bound constructs a truly nonaligned cheaper companion and both physical words. The construction selects a subprogression and does not prescribe a merger for every member of the initial ternary stratum.

## The exact lattice and intrinsic scale

Since (3/2)^a=2 and (3/2)^{a+1}=3 modulo d_a, we have exactly

    2^j3^k=1 mod d_a   iff   o_a divides a j+(a+1)k.         (1)

Let l_a be the least sup norm of a vector in this lattice outside the aligned line Z(−a−1,a). Then

    o_a/(2a+1) <= l_a <= o_a/(2a+1)+a+1.                    (2)

For the upper bound choose k congruent to o_a modulo a nearest to o_a/(2a+1), and set j=(o_a−(a+1)k)/a. Deviations in the two coordinates from the common real target are at most a/2 and (a+1)/2 respectively. The lower bound is the triangle inequality in (1). Consequently the [S-unit gcd theorem application](S_UNIT_RIGIDITY.md) implies o_a/a² tends to infinity.

Choose 0<=j<=a congruent to o_a modulo a+1, and put p=(o_a+a j)/(a+1). Then (j,−p) realizes determinant −o_a, p is asymptotic to o_a/a, and j=o(p). In particular 4^j<3^p for all large a. Set H=10(p+a)+10, and initially impose

    z_a(n)=3^H modulo 3^{H+1},          first three bits of n are 100.

These compatible CRT conditions ensure a uniquely minimizes at large n and raw 10 is a whole, misaligned first A module. It increases rank by the [forward precision theorem](SHORT_MERGERS.md), so this odd ternary-unit source is unsafe. For M<o_a/(2a+1), the two-arm precision condition applies by the choice of H. Every cheaper merger would need an exact root alignment in mode a, hence a lattice exponent vector with coordinates <=M in absolute value. By (1) this vector must be aligned. The [integrality argument](S_UNIT_RIGIDITY.md) then forces actual aligned repayment, impossible at an unsafe source. This proves the lower clock bound independently of any individual candidate.

## A cheap nonaligned affine companion

Take

    m=alpha_a+2^j 3^{-p}(n−alpha_a),
    2^j n=3^p m+b,          b=(3^p−2^j)c_a/d_a.

The congruence in (1) ensures b and m are integers (use z_a(n) divisible by 3^p and m=(2^j z_a(n)/3^p−c_a)/d_a). For sufficiently large positive n, m is positive and its a-component has rank exactly 4^j3^{-p}R(n)<R(n). The missing issue is physical merging. The following word compiler proves it on a subprogression with the required *linear* cost.

### A linear affine synchronizer

For any integer D>=0 and signed b_0, there is a computable dyadic class of y on which the positive pair (3^D y+b_0,y) merges at equal clocks of length O(D+log(2+|b_0|+3^D)). This sharpens the quadratic word-length estimate of ACS-002, PR #132 at `7687eec1ac364009d644cb8d015f1fe3b28730cc`, `research/astra-exit-merging/affine-completeness/PROOF.md`. Its equal-gap compiler and its bit lifting are used here; the preparatory valuation rule gives the improvement.

At d>0 a common even bit on the two arms halves an even intercept, and a common odd bit replaces it by (3b_0+1−3^d)/2. Set w_d=v2(3^d−1). If the intercept is nonzero of valuation at most w_d, halve it to odd. If it is zero or has larger valuation, use one common odd bit; the new valuation is exactly w_d−1, then halve to odd. This costs at most w_d steps total, including the case where the intercept is already odd. With an odd intercept prescribe y odd, so the first arm is even, reducing d to d−1 with intercept (b_0−3^{d−1})/2. The quantity |b_0|+3^d decreases over this whole block: the optional common odd step increases it by at most 3/2, common halvings do not increase it, and the final exponent reduction at least halves it.

For d odd, w_d=1. For d even, w_d=2+v2(d), by factoring 3^d−1 or repeated squaring. Summing the exponent reduction and preparation counts gives at most D+sum_{1<=d<=D} w_d <= 7D/2 steps. At d=0 the residual absolute gap g<=|b_0(original)|+3^D. An even g is halved by choosing the lower arm even. For g=1 modulo 4 greater than one choose the lower arm 1 modulo 4, giving new gap (3g+1)/4 in two steps. For g=3 modulo 4 choose the lower 2 modulo 4, giving (3g−1)/4 in two. At g=1 take the lower 4 modulo 8, yielding a merger in three steps. Every nonterminal update contracts g−1 by at least a factor 3/4, hence this last part costs O(log(2+g)). The finite chosen parity prescriptions are compatible: after each prefix changing the still-free high source bit changes the current lower parity by an odd multiple. Positivity follows for sufficiently large sources. For the worst case b_0=0 and D large, any equal-clock uniform merger must give the second arm D more odd steps than the first by comparing slopes, so at least D steps can be necessary.

### Applying it without paying for the large ternary precision

Choose an ordinary representative n_0 in the prescribed dyadic/ternary class and write n=n_0+2^K3^{H+1}t with K=3. Then m=m_0+2^{K+j}3^{H+1-p}t. The first K steps of n and first K+j steps of m are individually forced throughout this progression. Call their resulting states N and Y, odd counts q_N,q_Y, and constants C_N,C_Y. Their slopes in t are odd; d=p+q_N−q_Y>=0 for all large a. The intercept in the new chart (N,Y)=(3^dY+b',Y) is

    b'=(3^{q_N} b + 2^j C_N−3^d C_Y)/2^{K+j}.

Its bit length is O(p+j+K), independently of H: |b|<=5(3^p+2^j) and the word constants are bounded by 3^K or 3^{K+j}. Apply the linear synchronizer to this chart. Its chosen dyadic guard on Y pulls back through an odd slope to a nonempty class of t. The original clocks are therefore O(p+j+K)=O(o_a/a). This produces the upper bound while retaining the original source below neither a floor nor a fictitious change of parameter: every positive integer on the final subprogression is a separate physically verified instance. The initial state is in D_F for any fixed F once n is large; the displayed lower-rank merger uses raw positive paths.

The least sufficiently large positive lift can also be kept below exp(O(p+a)): the initial CRT modulus has that size, the further dyadic refinement costs O(p) bits, and the companion becomes positive beyond a threshold of comparable bit length. Conversely n>=3^H/|d_a|−5. Thus for these representatives ell(n) has order log n as well. The scale o_a/a singles out the arithmetic obstruction, rather than only a height bound.

The [replay](check_order.py) constructs both words and a positive ordinary lift, checks every raw bit, verifies the earlier clock exclusion by the exact modular order, and exercises the zero-intercept compiler guard.
