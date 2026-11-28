# A finite power gap bounds the floor of a real Collatz segment

The accompanying [CofactorDescent.lean](CofactorDescent.lean) proves an exact finite version of the [shifted cofactor argument](../broad/SHIFTED_COFACTOR_COLLISIONS.md). It uses the actual shortcut map and its actual iterates. It does not assert the existence of a repeated label or import a logarithmic-form theorem as an axiom.

Let $Z(x)=2x+1$, let $r$ be a segment length, and let $s$ count its odd inputs. Suppose that the endpoints have factorizations
$$
 Z(x)=q3^a,\qquad Z(T^r x)=q3^b,\qquad q>0.
$$
There is no need for the formal statement to assume that $q$ is prime to three: any supplied common factorization suffices. Actual equality of the labels obtained by removing powers of three is one way to supply these hypotheses. Put
$$
 P=2^r3^b,\qquad Q=3^{a+s}.
$$
For every nonempty segment, the kernel-checked `collision_power_gap` gives $Q<P$. If all its input states are at least $m$, `collision_floor` gives the explicit rational inequality
$$
 \boxed{\quad(2m+2)(P-Q)\le rP.\quad}
$$
In particular, for any supplied relative gap $Q\le(1-\eta)P$, with $\eta>0$, a clock satisfying $r<(2m+2)\eta$ forces an actual visit $T^j x<m$ for some $j<r$. This is `low_state_of_relative_gap`, not a statement about an auxiliary coefficient or a randomly selected path.

## Why the finite bound holds

At each input $z$ the exact branch identity is
$$
 2Z(Tz)=3^{z\bmod2}Z(z)+1.
$$
Write $A_z=3^{z\bmod2}Z(z)$ and $w_z=A_z/(A_z+1)$. Multiplication along the real segment telescopes to
$$
 \prod_{j<r}w_{T^jx}=Q/P.
$$
Each factor belongs to $(0,1)$. If $z\ge m$, its loss is $1-w_z\le1/(2m+2)$. The elementary product-loss inequality
$$
 1-\prod_{j<r}w_{T^jx}\le\sum_{j<r}(1-w_{T^jx})\le r/(2m+2)
$$
proves the displayed bound. The Lean development proves the actual branch identity, the product calibration and the loss estimate by finite induction, and then derives the low-state conclusion.

## Scope of the logarithmic consequence

On a positive segment with equal prime-to-three cofactors, the written argument shows $k=a+s-b$ is an integer with $0<k<r$. Its positive logarithmic gap is
$$
 r\log2-k\log3
 =\sum_{j<r}\log\left(1+\frac1{3^{T^jx\bmod2}Z(T^jx)}\right).
$$
The cited Bondareva–Luchin–Salikhov estimate therefore gives a polynomial floor bound of order $r^{5.116201}$, with an unevaluated absolute onset. This analytic estimate and the valuation-based construction of the common factorization remain in the written manuscript. The formal result above keeps the finite power gap explicit and needs neither of them.

The unresolved step is to force sufficiently early label collisions on every nonconvergent ordinary trajectory. A family of immediate siblings has equal labels at the same depth, so an argument using a branching family must also account for the two-arm alternative in the companion manuscript.
