# Direct dissipation: an unconditional energy--moment inequality

**PROPOSED; self-audited. No pointwise pressure-decay proof is claimed.**
This is a second route within the continuation. Unlike PROOF.md D4, its
inequality requires NO simple-path packing estimate, no nonperiodicity
hypothesis, and no removal of repeated states. It uses the literal +1 term.

Use the same positive odd map and source weights as [PROOF.md](PROOF.md).
For each finite clock q put

    a_x = [J_q(x)/U^q(x)]^2,   t_x=U^q(x),
    E_q = sum_x a_x,
    D_q = sum_x a_x^2 t_x^2,
    delta_q = E_q-E_(q+1).

These E_q are the UNKILLED energies of PR143 PF-006, not Ebar_Q. All sums
range over all positive odd sources. Cycle visits are retained. The exact
product formula gives 0<a_x<=x^-2. The bounded R4 operator of PROOF.md D6
establishes D_q<infinity at each finite q. No all-time convergence is assumed.

## L1. The envelope supplies a nonlinear interpolation bound

For any family 0<=a_x<=x^-2 on positive odd x, with E=sum a_x>0,

    sum_x a_x^(4/3) >= (9/64)^(1/3) E^(5/3).             (1)

Proof. E<=pi^2/8<5/4. Take N=ceil(1/E). The tail beyond the first N odd
sources is less than 1/(4N)<=E/4, so the first N carry at least 3E/4.
Convexity gives sum a_x^(4/3)>=(3E/4)^(4/3)/N^(1/3).
Since N<=1/E+1<9/(4E), cubing the coefficient gives
(3/4)^4*(4/9)=9/64, proving (1). Zero entries are allowed; the same result
holds for any finite source bank by extending it with zeros.

## L2. Exact arithmetic loss dominates an inverse-height moment

For t>=1 set c(t)=3t/(3t+1). The following elementary identity proves the
needed uniform lower bound:

    16t(6t+1)-7(3t+1)^2=(t-1)(33t+7)>=0.

Therefore

    1-c(t)^2=(6t+1)/(3t+1)^2 >= 7/(16t).                 (2)

The constant 7/16 is attained at t=1. Define L_q=sum_x a_x/t_x. Literal
one-step multiplication of a_x by c(t_x)^2, followed by Tonelli, gives

    delta_q=sum_x a_x[1-c(t_x)^2] >= (7/16)L_q.           (3)

This is the actual finite-clock loss, not a statistical drift or an average
over freshly sampled sources. It remains valid on every positive cycle.

## L3. The direct finite-time dissipation inequality

For EVERY q>=0,

    delta_q^2 D_q >= (441/16384) E_q^5.                  (4)

Equivalently,

    E_q-E_(q+1) >= (21/128) E_q^(5/2)/sqrt(D_q).         (5)

Proof. Holder, with exponents 3/2 and 3, gives

    sum_x a_x^(4/3)
      =sum_x (a_x/t_x)^(2/3) (a_x^2 t_x^2)^(1/3)
      <= L_q^(2/3) D_q^(1/3).

Cube and use (1) to obtain L_q^2 D_q >= (9/64)E_q^5.
Combine with (3). The constant is (7/16)^2*(9/64)=441/16384.
Every sum is finite, or follows first for finite banks and then by monotone
limits; E_q>0 and D_q>0. This completes the all-source proof of (4).

The statement is quantitative but does NOT force delta_q to stay uniformly
positive: D_q can grow. That is precisely the remaining obstruction.

## L4. Integrated bound and a sufficient divergence criterion

Convexity of y^(-3/2) and (5) give

    E_(q+1)^(-3/2)-E_q^(-3/2) >= (63/256) D_q^(-1/2).

Summing yields the unconditional finite-clock estimate

    E_Q <= [E_0^(-3/2)+(63/256)sum_(q<Q)D_q^(-1/2)]^(-2/3),
    E_0=pi^2/8.                                           (6)

In particular the sufficient condition

    sum_(q>=0) D_q^(-1/2)=infinity                         (7)

would imply E_Q->0 and therefore F(t)->0. For the last implication alone,
no lower first-hit discount or orbit packing is needed: use PR143's
finite-prefix pressure certificate, or the elementary argument below.

Given epsilon>0, choose Q with E_Q<epsilon/2 and an odd X with
1/[2(X+1)]<epsilon/2. Let M be the largest odd state in the Q-step prefixes
of all odd x<=X. A target t>M, when first hit by such a source, is hit after
Q, so its normalized squared first-hit weight is at most a_x at clock Q.
The remaining x>X contribute less than the reciprocal-square tail. Thus
F(t)<epsilon. This is conditional on (7), not a construction of Q without it.

### Examples of sufficient hypotheses, NONE proved here

If D_q<=B(q+1)^2 for every q, (6) gives

    E_Q=O((log(Q+1))^(-2/3)).                             (8)

More generally, D_q=O((q+2)^2 (log(q+2))^2) still suffices, giving a bound
of order (log log Q)^(-2/3) at large Q. If D_q=O((q+1)^p) with p<2,
then (6) gives E_Q=O(Q^(-(2-p)/3)).

The packing-based D4 route has a stronger polynomial conditional rate for
the QUADRATIC hypothesis, namely Ebar_Q=O(Q^(-2/57)), and also permits any
pointwise exponent below 40/19. The direct loss route instead eliminates
that packing dependency entirely and controls the un-killed energy itself.
Neither route proves its moment hypothesis. A divergent reciprocal-moment
sum is a sufficient target; no equivalence or necessity is asserted.

## L5. Checks actually executed

The separate `dissipation.py` script reads the full 12-clock trace certificate
and checks (4) with the LOWER certified delta and D but the UPPER certified E,
using integer cross multiplication. All 12 consecutive clock pairs pass.
This is stronger finite evidence than checking a rounded approximate table.
The independently reconstructed trace intervals remain the evidence input;
the inequality proof above does not depend on those computed intervals.

The script also reconstructs un-killed finite-bank E, D and exact loss through
80 odd clocks for all 2,048 odd sources through 4095, using explicit shortcut
steps and 128-bit outward integer intervals. All 81 bank inequalities pass.
Every division and loss is retained after visits to 1. The interpolation is
applicable to a finite bank extended by zeros. Five direct corruptions are
rejected; this is not a new independent mathematical review.

Normal and optimized outputs agree. The all-clock statement (7) is OPEN.
The unconditional exponential bound D_q<(5/4)(432/85)^q does not prove (7).
A proof of pressure decay would still leave nontrivial positive cycle
exclusion as a separate problem.
