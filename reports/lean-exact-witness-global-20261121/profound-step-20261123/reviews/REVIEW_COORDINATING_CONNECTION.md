# Arithmetic reconstruction of the coordinating connection

23 November 2026. **VERIFIED at the stated written scope.**

Source: `research/lean-exact-witness-global-20261121/profound-step-20261123/COMMON_DISPLACEMENT_AND_FREE_ENERGY.md`

Exact SHA256: `867cca98da500a7b1be5c24e9185ac877b56c508be2a7da12436e9f3b0046abb`.

The arithmetic lane independently reconstructed CF1--CF4, CF7--CF9 and
the new explicit finite upper certificate CF7-F in this coordinating
manuscript. The reviewer authored the separate adaptive-lattice dependency;
this review is not described as independent revalidation of that imported
theorem. No new numerical census or compiler execution is claimed here.

## 1. Actual clocks and the common displacement

From the exact odd step 2^{a_(j+1)}q_(j+1)=3q_j+1, multiplication by
2^{A_j}/3^{j+1} gives z_(j+1)q_(j+1)=z_jq_j+z_j/3. Summation proves
CF1 with A_0=0 and the displayed index range.

A block containing r odd steps has P=3^r and Q=2^a, where a is the
sum of those exact valuations. Its ordinary shortcut parity word has
exactly r ones and length a. The complete relation
Q q_(j+r)=P q_j+C gives z_(j+r)=(Q/P)z_j and
D_(j+r)-D_j=z_j C/P. Thus CF2 retains the distinct clocks r and a.

CF1 gives H_j+q_0=z_j q_j+z_j C/(P-Q). Bringing the terms to one
denominator proves CF3, including its sign. Q-P is odd because a>=1
and r>=1; 3^j is a 2-adic unit. Multiplicativity of the valuation
therefore proves CF4 whenever the integer displacement is nonzero.

Repeating the same accelerated gap block k times repeats its literal
shortcut word k times. Hence Q^k divides ((Q-P)q_j-C) by the complete
repetition identity and gcd(P,Q)=1. The extrapolant's additional binary
precision is exactly this source lattice. At zero displacement, the
legal block fixes q_j and H_j=-q_0; the paper correctly treats that
case before taking a valuation.

For a reduced center c/d, the raw displacement is a signed gcd multiple
of d q_j-c. That gcd is odd since Q-P is odd, so reducing the rational
center preserves this 2-adic valuation. A change of center still incurs
the adaptive cross-carry; CF3 cancels none of that cost.

## 2. Finite trial optimization and its effective upper certificate

The retained exact compiler relation CF5 implies pointwise

    exp(-V(n)) nu_q(n) = 64^s r(Phi(n))^s / A_s(q).

For nonempty finite F these weights sum to Z_F=64^s B_F/A_s(q)>0.
After normalization to tau_F, direct expansion gives

    E_sigma V + KL(sigma || nu_q)
      = KL(sigma || tau_F) - log Z_F.

The equality uses the original full nu_q, not its conditional restriction
to F. All its terms on F are positive. The minimum at tau_F proves CF7,
including the negative sign on s log 64. F={n} gives CF8. The balanced
compiler is bijective, so the image sum has no collision multiplicity.
The exact optimizer still depends on infinite weights, as the final
manuscript correctly states.

The explicit finite trial avoids that dependence. Let
W_F=sum_{n in F} Phi(n)^(-s) and sigma_F(n)=Phi(n)^(-s)/W_F. Substituting
CF5 directly into its objective gives

    objective = sum sigma_F log sigma_F + log A_s(q)
                - s log 64 - s sum sigma_F log r(Phi(n)).

Using r(Phi(n))>=c_*/Phi(n), the logarithms of Phi(n) cancel the
corresponding ones in log sigma_F. The resulting upper bound is
log A_s(q)-s log(64c_*)-log W_F. Finally r(n)<=1/n gives
A_s(q)<=zeta(s)<=1+1/(s-1)=s/(s-1), proving precisely CF7-F for
this explicit finite trial, and hence for the infimum. Its right side
requires only actual finite transported sources and known constants.
Its desired scale still requires constructing enough such finite mass.

CF6 is consistent with the same reconstruction: increasing finite
exhaustions give Z_F increasing to R_s(q), and their optima converge to
-log R_s(q). The older construction of r, its uniform c_* bound and
finite s-mass remain exact pinned pressure dependencies; this review
does not independently reprove that entire older construction.

## 3. The conditional closing consumer

With the expressly positive finite g(j), CF6 and the supplied CF9
trial imply -log R_s(q_j)<=C+s log g(j), and consequently
R_s(q_j)^(1/s)>=exp(-C/s)/g(j). Summing over I contradicts the retained
root summability when the displayed reciprocal sum diverges. This proves
the consumer but constructs none of the missing trials. The unchanged
component and fixed sibling are retained throughout.

Adding a constant to V scales its partition function while leaving the
normalized tilted law unchanged. The final text identifies this as an
abstract normalization control, not another actual compiler with a
nonzero empty-address cost. Its separate anchored probability control
has partition t^2+t(1-t^2)=t+t^2-t^3, as stated. Neither control is
asserted to realize an escaping ordinary orbit.

## Verdict boundary

No algebraic error was found in the reviewed formulas. The accelerated
and shortcut normalizations and the signs agree with actual finite
ordinary identities. This verdict covers the coordinating deductions
and their precise relationship to the adaptive source lattice. It does
not certify all external hypotheses in Section 4, construct a new
arithmetic approximation or lower Green estimate, select paid macros
universally, or prove Collatz or the residue-512 implication. Those
obligations remain explicitly open.
