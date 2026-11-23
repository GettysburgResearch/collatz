# Independent arithmetic review of the fixed-sibling adelic repair

23 November 2026. **VERIFIED WITH FIXES at the displayed written scope.**

Source: `research/lean-exact-witness-global-20261121/profound-step-20261123/repair/ADELIC_INTEGER_REPAIR.md`

Final SHA256: `cd2735741f0833f32f7707e31bb864452b9d2bead7cdaea7e35068a3922e5dc7`.

The arithmetic lane independently reconstructed AR1--AR13, including
the primitive denominator, all three local products, and the exact
Subspace-Theorem normalization. The author applied two requested fixes:
repetition indices now identify actual block boundaries q_(j+ell*r),
and the signed extrapolation is explicitly a sum of the periodic model's
tail, with no unproved bound on the actual nonperiodic real error.
No new computational run or formal compiler execution is claimed here.
The reviewer authored the related adaptive-lattice packet, not this repair
argument; shared prior dependencies retain their own evidence boundaries.

## 1. Actual rational pullbacks and limits

The complete odd-step identity is 3^j q_0+C_j=2^{A_j}q_j with
C_j/3^j=D_j. Applying its literal inverse affine expression to
64^b q_j+h_b gives

    y_j = 64^b q_0+(64^b-1)D_j+h_b z_j
        = q_0+h_b z_j(3q_j+1),

since 64^b-1=3h_b. The actual next edge gives the last expression in
AR2 with A_(j+1). Subtracting successive identities and using
3 z_(j+1)q_(j+1)=z_j(3q_j+1) proves AR3 exactly.

On the displayed injective escaping ray, the retained uniform product
and ordinary reciprocal bound imply sum z_i<infinity, hence z_j→0.
AR4 is then the actual real limit. The same D_j identity converges
2-adically to -q_0 since q_j is odd and A_j>=j. Substitution in AR2
gives the 2-adic limit q_0. These are distinct metric limits, not two
names for the same rational or algebraic number.

The pressure connection is correctly normalized: the positive product
identity gives q_0+D_infty=q_0/Lambda_infty(q_0), so
r(q_0)=1/(q_0+D_infty). Consequently L_1=q_0+63/r(q_0).
The old reciprocal and product bounds are dependencies, not newly proved
by this review.

## 2. Primitive reduction and both finite-place factors

For b>=1, the elementary odd-prime lifting identity gives
v_3(64^b-1)=2+v_3(b); dividing by three proves AR5. Since h_b is odd,
c_b is odd as well as a ternary unit.

For j>nu_b, multiplying AR2 by Q_j=3^(j-nu_b) gives exactly AR6.
Modulo three, its second summand is nonzero because c_b, 2 and
q_(j+1) are units. Therefore P_j is not divisible by three and the
pair (P_j,Q_j) is primitive. Its numerator difference is exactly
c_b 2^(A_(j+1))q_(j+1), whose two remaining factors are odd.
This proves the equality in binary precision and both ternary values
in AR7; no generic inequality is substituted for the exact valuation.

## 3. Reconstructed Subspace product and primary theorem

At infinity the product of the two forms is
Q_j^2(L_b-y_j). At two it is 2^(-A_(j+1)), because Q_j is odd.
At three it is 1/Q_j, since P_j is a ternary unit. Multiplying yields
precisely AR8: Q_j(L_b-y_j)2^(-A_(j+1)). The denominator place is
included and removes only one of the two real factors Q_j.

AR3 gives L_b-y_j=h_b sum_(i>=j+1) z_i. Its first positive term
therefore proves Pi_j>=h_b/3^(nu_b+1)=c_b/3. Finally
64^b-1>=63b and 3^v_3(b)<=b imply c_b>=7. This reconstructs AR9
for every upper sibling power. The same inequality with y_J in place
of L_b is a finite identity for J>=j+1; it does not turn the resulting
changing coefficient into a fixed-target Subspace application.

The reviewer read the primary Adamczewski--Bugeaud preprint,
[arXiv:math/0511674v1](https://arxiv.org/pdf/math/0511674), Section 4,
Theorem E on printed pages 7--8 and the periodic-completion construction
that follows. Retrieved primary references: `turn179554397view0` and
`turn179554397view1`.

Take its base field K=Q and m=2. The theorem allows algebraic coefficients
in the forms, so a provisionally algebraic real L_b is eligible without
introducing unaccounted conjugate places. All three displayed pairs of
forms have rank two. At every finite place a primitive integer vector
has max norm one; the global height is its Euclidean archimedean norm.
Thus the theorem's normalized product is Pi_j/H_j^2 and its required
inequality is exactly Pi_j<=H_j^(-epsilon). The uniform lower bound
7/3 prevents this inequality. Algebraicity of L_b itself remains an
additional unproved premise, correctly marked provisional in the source.

This checks the failure of the specified approximants and forms. It is
not a no-go theorem for arbitrary Subspace arguments, signed approximants,
new coefficient fields, or edited ordinary inverse words.

## 4. Signed extrapolation and physical block clocks

For r odd steps with total exact gap a, the corresponding shortcut word
has length a and r ones. Its complete affine data P=3^r,Q=2^a imply
D_(j+r)-D_j=z_j C/P, proving AR10. When Q<P, summing the repeated
periodic model gives z_j C/(P-Q), hence AR11. Equivalently the
extrapolant is (D_(j+r)-(Q/P)D_j)/(1-Q/P), a signed affine
combination of the two partial sums.

Adding q_0 and using AR1 gives AR12. The actual endpoint identity
P q_j+C=Q q_(j+r) gives

    (Q-P)q_j-C = Q(q_j-q_(j+r)),

which proves AR13. Along k literal repetitions, use the corrected
boundary indices j+ell*r. The block displacement is multiplied by P/Q
at each such boundary, and gcd(P,Q)=1 gives Q^k divisibility at the
initial boundary. Q-P is odd and not divisible by three, so no omitted
local factor is concealed in the extrapolant denominator.

This is precisely the adaptive source lattice. Its availability does
not bound the actual nonperiodic real approximation error or produce
an integer ancestor of the fixed sibling. The revised wording preserves
both limitations.

## Verdict and remaining scope

The final manuscript's finite identities and its specified mixed-place
obstruction are correct. The two local fixes repair an indexing ambiguity
and remove a potentially overstrong reading of the periodic extrapolation.
The example 75→113→85 consists of two accelerated odd steps (three
shortcut steps); it correctly shows that a different actual inverse word
can reach S(1)=85 despite nonintegral canonical pullbacks.

No universal integer repair, arbitrary-word selector, unrestricted cycle
exclusion, or Collatz proof follows. The analytic limiting arguments,
valuations and Subspace eligibility remain written mathematics; the
separate Lean algebra module is not represented here as formalizing those
external or infinite arguments.
