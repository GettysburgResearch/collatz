# Which rank moments survive an actual unsafe return?

**Status: PROPOSED, pending independent mathematical review.** For the enlarged unsafe return of PR #92, every fixed number of returns has the same class of bounded nondecreasing rank weights. Logarithmic moments survive. Every positive power moment can be destroyed even after any prescribed finite number of returns. The result gives no uniform loss of surviving mass.

## Operator and statement

Use the shortcut Collatz map on positive integers, killed at 1. For the maximal repeated-word acceleration A and moving rank R, let U consist of n>1 with R(A(n))>R(n). From u in U take one A step and then all consecutive steps at nonincreasing-rank sources until reaching U or 1. Write J for this total return. The killed forward mass operator on U is

    (K f)(y) = sum_{u in U : J(u)=y} f(u),   y in U.

Thus input and output are both projected onto U and every intermediate safe state is traversed physically. Killing below or at a fixed floor H>=1 at *any physical step* gives K_H on sources above H. With H=1 it gives K. For finite-valued nondecreasing phi:[1,infinity)->[1,infinity), use the norm sum_{u in U, u>H} phi(R(u)) |f(u)|. For every H and integer m>=1 the following are equivalent:

1. K_H^m is bounded on this weighted l¹ space.
2. There exists D with phi(t²)<=D phi(t) for all t>=1.

In particular, boundedness for even one positive iterate and one finite floor implies boundedness for every positive iterate and every finite floor with constants allowed to depend on the iterate. For positive inputs these are bounds on actual re-entry, valid again after each application.

**Dependencies.** The base checkout is `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The source PR is #92 at `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`. The [module and rank](../astra-three-routes/pass4/MOVING_GHOST_RANK.md) supply T-A3-901/902, the [plateau theorem](../astra-three-routes/pass5-spectrum-switch/PLATEAUS_AND_SOURCES.md) supplies T-A3-1052, and the [induced operator](../astra-three-routes/pass5-spectrum-switch/INDUCED_MASS.md) supplies the definition of J and the single-return obstruction R-A3-1004. The latter explicitly leaves fixed iterates open. The old source's [rank census](../astra-three-routes/pass5/RANK_MOMENTS.md), T-A3-1001, supplies summability in the full-support example below.

## The easy direction and a reusable input bound

The source gives n-1<=R(n)<=n² and A(n)+5<=(n+5)^3. On the safe leg rank cannot increase. Consequently a surviving return obeys

    R(J(u))+6 <= (A(u)+5)^2 <= (u+5)^6 <= (R(u)+6)^6.       (1)

In particular R(J(u))<=R(u)^8 for all sufficiently large R(u). Three applications of condition 2 bound the output/input weight ratio there. Bounded input rank leaves finitely many sources. Applying the triangle inequality and summing each surviving source exactly once proves boundedness for one return, hence all fixed powers. Floor killing only deletes paths.

For example, every finite moment of log(R+6) stays finite, with operator norm at most 6^p for weight [log(R+6)]^p, p>0. A slower weight gives a subexponential bound with an explicit horizon. For w(u)=1+log log(R(u)+6) and nonnegative f, (1) gives

    ||K_H^m f||_w <= ||f||_w + m log(6) ||f||_unweighted.     (2)

In particular its mass at endpoints of rank >=B is at most the right side divided by 1+log log(B+6). This tail is useful for a fixed return horizon. The bound increases with that horizon.

## Physical witnesses at every return depth

Let x be divisible by 3^7 and congruent to -17 modulo 2^{11(b+2)}, where b>=1 fixes the desired number of periods. The signed shortcut cycle based at -17 has the maximal modules

    -17  --11110-->  -41  --1110-->  -68  --00-->  -17.

Here 00 consists of two repetitions of the single even step. The two successive odd-run lengths are 4 and 3. A dyadic congruence at precision L supplies agreement on the first L shortcut parities, since the difference after j matched steps is the initial difference times an odd integer divided by 2^j. The extra two periods include the next mode, certifying maximality throughout the first b periods and the guard at their endpoint. For positive ordinary x the module-boundary values X_i,Y_i,Z_i satisfy

    X_0=x,       X_i+17 = (2187/2048)^i (x+17),
    Y_i+41 = (81/32)(X_i+17),     Z_i+68 = (27/16)(Y_i+41),
    X_{i+1}=Z_i/4.                                           (3)

All three phases tend uniformly to infinity with x over the available periods, since 2187/2048>1. All physical states exceed any fixed H for sufficiently large x. Indeed the positive odd steps increase, and each consecutive string of even steps is minimized at its endpoint.

To determine the actual rank compare the minimizing candidates a in {0,1,2} and additionally h=v3(2n+1) when h>=3, with z_a(n)=(3^a-2^{a+1})n+3^a-2^a. On a fixed ternary class where the indicated valuations are fixed, the rank has leading coefficient

    min_a (3^a-2^{a+1})² / 3^{v3(z_a(n))}

as a quadratic in the ordinary height (equivalently, as the minimum of the indicated quadratics). Here are all needed coefficients in candidate order, including the exceptional first Y phase:

| Phase | Class representative modulo 3^7 | h | Candidate leading coefficients |
| --- | --- | ---: | --- |
| X_i, i>=1 | -17 | 1 | 1, 1/9, 1/3 |
| Y_0 | 65/32 | 4 | 1, 1/3, 1/9, 2401/81 |
| Y_i, i>=1 | -41 | 4 | 1, 1/3, 1/9, 2401/243 |
| Z_i, i>=0 | -68 | 3 | 1, 1/3, 1/9, 121/729 |

A dyadic denominator is invertible modulo 3^7. Equation (3) gives the classes because Z_i+68 contains 3^7 and Y_0=(81x+65)/32. Every computed valuation in the table is less than seven, so substitution of the class representative is exact. In particular all displayed phases have R(n)/n² tending to 1/9, uniformly as n grows, since there are only four class rows. At X_0 the component R_0(x) gives R(x)<=x²/3^7. It follows from (3), with strict limiting margins, that X_i and Y_i are unsafe and Z_i is safe. In fact the regular successive rank ratios tend to (81/32)², (27/16)², and 1/16. At the initial transition the ratio has lower limit at least (81/32)² 3^7/9. Thus the *induced* return path reads

    X_0 -> Y_0 -> X_1 -> Y_1 -> ... -> X_b.                  (4)

The inequalities hold uniformly throughout the displayed finite shadow once x exceeds a single absolute threshold. This uses the same finite collection of height thresholds and X_i>=x at every phase. These finite ordinary sources need not coincide at differing depths.

## Necessity and persistent moment explosion

Fix m and choose b>=m. There is an arithmetic progression of even exponents e for which x=7*3^e satisfies the dyadic condition of (3). Indeed (-17)/7 is 1 modulo 8, and 9 generates the residues congruent to 1 modulo 8 at precision L=11(b+2). To see this, v2(9^{2^j}-1)=j+3 by successive squaring. Its order is therefore 2^{L-3}, the size of that group. Set e twice the resulting discrete logarithm modulo twice the order, taking e>=7. Along this progression x grows by a fixed multiplicative factor q_m. At x, R(x)<=7x. At the mth induced endpoint, (3) and the table give R(J^m x)>=c_m x² with c_m>0. In particular

    sup_{surviving x above H} R(J^m x)/R(x) = infinity        (5)

for every m and H. This avoids the floor along the entire shortcut path.

For a bounded K_H^m of norm M, apply the estimate to a point mass at x. Given sufficiently large t, take the last progression source with 7x<=t. Then x>t/(7q_m), so monotonicity gives phi(C_m t²)<=M phi(t), with C_m=c_m/(7q_m)^2. Eventually C_m t²>=t^{3/2}. Applying the resulting inequality twice gives phi(t²)<=phi(t^{9/4})<=M²phi(t). Bounded t are covered since phi is nondecreasing, finite and at least one. This proves necessity.

For the same full-support input f(u)=R(u)^{-2} on U above H, its first rank moment is finite by T-A3-1001. For every m>=1 **this same input** satisfies

    sum_y R(y) (K_H^m f)(y) = infinity.

Each of the infinitely many progression sources contributes at least c_m x²/(7x)² to the nonnegative sum. No hypothesis on multiplicity of an endpoint is necessary. This also makes the induced inverse inequality K_H^m(R^{-p})<=C R^{-p} impossible for any fixed C, m>=1 and p>0, by the single-source contribution to each output row and (5).

The operator in (2) has spectral radius exactly one on the complex weighted l¹ space for w. Its power norms are at most 1+m log(6) by (2) applied to |f|. For each fixed m, progression sources eventually have larger endpoint rank than initial rank. A point mass then gives power norm at least one. Taking mth roots proves the assertion. Thus this invariant space controls transport but cannot yield operator-norm exponential decay at any fixed floor.

## Remaining question

No proof here gives decay of the mass of a specific positive input as m tends to infinity. At each finite depth (4) uses changing sources. A weight exploiting information beyond the value of R, or a survivor-specific estimate averaged over actual inputs, could behave differently.

The [arithmetic replay](check.py) exercises the ordinary positive examples and computes the ternary table with exact fractions. The proof of the depth quantifier is the construction above.
