# Logarithmic strengthening of the critical-height defect

**PROPOSED, elementary addendum to forward-inverse-defect/PROOF.md.**
This proves a stronger necessary growth condition on an escaping ordinary
orbit. Its closing inequality is a sufficient hypothesis, not a proved
bound and not an equivalent reformulation of Collatz.

Use the same W, and put
\[
 \ell=\log_2 3,\qquad c_*={3\over\log_2(3/2)},\qquad
 Z(n)=W(n)-c_*\log_2(n+1).
\]
The parent proof establishes, for the actual gap g=v_2(3n+1),
\[
 Z(U(n))\ge Z(n)+(c_*-5)(g-1)-c_*\eta(n,g),\qquad
 \eta(n,g)=\log_2\!\left(1+{2^g-2\over3(n+1)}\right).
 \tag{1}
\]
Here eta=0 when g=1 and 0<=eta<1 for every actual positive-integer edge.

**Theorem.** Every escaping positive odd ordinary orbit whose W values
remain finite satisfies
\[
 \liminf_{k\to\infty}
 {Z(n_k)\over\ln\ln n_k}
 \ \ge\ {c_*-5\over\ln\ell}
 \ =0.2790812603\ldots .                                  \tag{2}
\]
Natural logarithms are used in the denominator. If W becomes infinite,
it stays infinite, so the corresponding extended inequality is immediate.

Fix 0<epsilon<c_*-5. Uniformly over all actual gaps and all sufficiently
large n, (1) gives
\[
 Z(U(n))-Z(n)\ge(c_*-5-\epsilon)(g-1).                     \tag{3}
\]
To prove the uniformity, choose G with epsilon(G-1)>=c_*.
For g>=G use eta<1. For the finitely many 2<=g<G, eta(n,g)->0
uniformly as n->infinity. The g=1 inequality is exact at every n.

Discard the finite initial segment before an escaping orbit stays above
this floor. Let r_k count its exponents greater than one through time k.
Summing (3) gives
\[
 Z(n_k)\ge Z(n_0)+(c_*-5-\epsilon)r_k.                     \tag{4}
\]

It remains to compare r_k with height without any statistical assumption.
Set
\[
 B(n)=\log_2(n+1)-1>0\quad(n>1).
\]
A run of s consecutive exponent-one edges obeys
\[
 n_s+1=(3/2)^s(n+1).
\]
Oddness of its endpoint gives s<=v_2(n+1)-1<=B(n).
Consequently
\[
 B(n_s)=B(n)+s\log_2(3/2)\le\ell B(n).                   \tag{5}
\]
Any edge with g>=2 decreases n (weakly at n=1), hence decreases B(n).
There are at most r_k+1 exponent-one runs, including a final incomplete
run. Applying (5) separately to each gives
\[
 B(n_k)\le\ell^{r_k+1}B(n_0),\qquad
 r_k\ge{\ln B(n_k)\over\ln\ell}-1-{\ln B(n_0)\over\ln\ell}.
 \tag{6}
\]
Combining (4) and (6), dividing by ln ln n_k, and using n_k->infinity
proves the lower bound (c_*-5-epsilon)/ln ell. Let epsilon decrease to
zero to obtain (2).

## A weaker sufficient closing estimate

Together with the parent's nontrivial-cycle implication, either of the
following bounds on all positive odd ordinary ternary units would prove
Collatz:
\[
 W(n)\le c_*\log_2(n+1)+o(\ln\ln n)
\]
(as an eventual upper bound, with finite W also at the remaining finitely
many units), or, for some fixed
\[
 \alpha<{c_*-5\over\ln\ell},
\]
\[
 W(n)\le c_*\log_2(n+1)+\alpha\ln\ln(n+e)+C
 \qquad\text{for all positive odd ordinary ternary units}.
\]
These formulas allow larger error terms than adding only a constant to
c_* log_2(n+1). This comparison of right-hand sides does **not** make the
existential global closing statements logically weaker. As proved in the
[closure boundary note](CLOSURE_BOUNDARY.md), each of these global bounds
implies Collatz and W(1)<infinity; conversely those two assertions give
W(n)<=5 log_2 n+W(1)+1 on every positive odd ordinary unit, and hence all
the displayed bound shapes. Finiteness at the finitely many small inputs
is included in the first asymptotic formulation above.

All these equivalent global closing statements remain unproved. Neither
Haar-almost-everywhere control of W nor the rational density construction
provides any of them.

### A rational coefficient with exact certification

The concrete bound
\[
 W(n)\le c_*\log_2(n+1)
       +{1\over4}\ln(1+\log_2(n+1))+C
 \tag{7}
\]
on every positive odd ordinary ternary unit is sufficient. It would make
the upper limit of Z(n_k)/ln ln n_k at most 1/4 on any escape, contradicting
(2). It also implies finiteness at every potential cycle state, so the
parent's cycle argument applies.

No floating-point comparison is needed for the strict inequality:
3^41<2^65 implies c_*>41/8, while 3^5<2^8 implies ell<8/5.
The elementary exponential series gives e>8/3>64/25, hence
ln(8/5)<1/2. Therefore
\[
 {c_*-5\over\ln\ell}>{1/8\over1/2}=1/4.
\]
Equation (7) remains OPEN; the addendum establishes only that it is a
sufficient closing bound and identifies the quantified growth it would
contradict.

### Audit of the parent's explicit positive-gain floor

The choice M=56*2^43 and gain 1/16 in the parent proof is correct.
The integer comparisons 3^41<2^65 and 3^7>2^11 yield
41/8<c_*<21/4. For g>=44, eta<1 gives a gain greater than
43/8-21/4=1/8. For 2<=g<=43 and n>=M, use
log_2(1+x)<=2x to obtain
\[
 c_*\eta(n,g)<{7\over2}{2^{43}\over n+1}<1/16.
\]
The positive first term (c_*-5)(g-1)>1/8 then leaves gain greater
than 1/16. The asymptotically sharp coefficient in (2) uses the separate
epsilon-dependent floor from (3), not this coarse fixed floor.
