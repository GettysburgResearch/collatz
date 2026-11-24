# An explicit approximate Collatz coloring that survives the density and spectral screens

**PROPOSED written countermodel, not a counterexample to Collatz.** This diagnoses the loss of exact ordinary information in the averaged routes. There exists a binary function F on the positive integers, with BOTH colors of natural density 1/2, satisfying

    F(2n)=F(n) exactly,
    #{n<=X:F(3n)!=F(n)} = O(X/sqrt(log X)),
    #{n<=X:F(n+1)!=F(n)} = O(X/sqrt(log X)),
    #{n<=X:F(Tn)!=F(n)} = O(X/sqrt(log X)).

It can be required to equal 1 on ANY prescribed finite set of verified starts and all their dyadic multiples. It also satisfies the shell log-rotation and primitive discrepancy premises of the preceding automata, Fourier, and polynomial-phase decorrelation results. These estimates, even together with finite verification, cannot by themselves force F to be constant. The construction explicitly does NOT satisfy exact ordinary odd-edge invariance.

## 1. Slowly changing resonant waves

Let theta=log_2 3 mod1 and take a sequence of increasing odd convergent denominators k_i>=4 such that

    k_i^2 <= k_(i+1) <= C k_i^K,   ||k_i theta|| <= 1/k_i.        (1)

This uses the same fixed Diophantine input as PR146: ||q theta||>=c q^(-kappa) for q>=1. Consecutive convergent denominators Q,Q' obey Q'<=C Q^kappa. Choose the first denominator >=k_i^2; its upper bound is C k_i^(2 kappa). If it is even, choose the next one, necessarily odd since consecutive convergent denominators are coprime, with another polynomial cost. This constructs (1) for a fixed K (enlarged if necessary). Irrationality itself gives arbitrarily large denominators; the Diophantine input controls the growth between stages.

For integer binary shell depth J, define a binary circle function g_J(t). During the transition interval k_i<=J<=2k_i put s=(J-k_i)/k_i and

    H_J(t)=(1-s) cos(2*pi*k_i*t) + s cos(2*pi*k_(i+1)*t),
    g_J(t)=1_(H_J(t)>=0).

Between 2k_i and k_(i+1) hold the second wave fixed (s=1 from the preceding transition, or the initial s=0 of the next one). For the finitely many earlier depths use the first wave. All frequencies are odd, so the continuous function changes sign under t->t+1/2. It has only finitely many zeros (a nonzero trigonometric polynomial), hence the logarithmic circle mean of g_J is exactly 1/2.

The number of discontinuities of g_J is O(J^K), since a nonzero trigonometric polynomial of degree D has at most 2D roots on the circle (multiply its Laurent expression by z^D). Single-point equality conventions are also covered by that count.

We need a uniform small-ball estimate during a transition. For k<l, 0<=s<=1, and a>=0,

    measure{|(1-s)cos(2*pi*k*t)+s cos(2*pi*l*t)| <= a}
       <= C sqrt(a+k/l).                            (2)

Partition t into l equal periods of the faster cosine. Within each, the slower cosine varies by <=2*pi*k/l. Replace the slow coordinate by that of an independent uniform point in the SAME small interval and integrate. If the original sum is within a, then for all such replacements it is within a+2*pi*k/l. On averaging over the intervals, the slow phase has the uniform circle distribution (k integral) and is independent of the fast phase. At least one of the coefficients is >=1/2. Condition on the other independent cosine: the remaining cosine must lie in an interval of length O(a+k/l). The arcsine distribution gives interval probability at most C sqrt(length), by integrating its endpoint singularity (or the elementary cosine inverse estimate). This proves (2), also for coefficients zero or one.

During a transition the rotation t->t+theta changes H_J by at most C/k_i, by (1). Changing J by one changes H_J by at most 2/k_i. A change of sign in either test requires the original absolute value to be at most the corresponding bound. Equation (2) and k_(i+1)>=k_i^2 therefore give O(k_i^-1/2)=O(J^-1/2) for both L1 differences. In an idle interval the rotation error of the single wave is O(k_(i+1)^-1/2) (in fact O(1/k_(i+1))), and J<=k_(i+1); the consecutive-depth difference is zero there. Endpoint transitions agree exactly at shared endpoints. We conclude uniformly for large J,

    ||g_J(t+theta)-g_J(t)||_1 = O(J^-1/2),
    ||g_(J+1)-g_J||_1 = O(J^-1/2).                  (3)

This sequence avoids the summable-variation rigidity route: its errors need not be summable.

## 2. Impose exact doubling on integers

For n>0 write n=2^v u, u odd, and let J0=floor(log_2 u), t=log_2(u/2^J0). Define F(n)=g_J0(t). This gives exact doubling invariance, not just an estimate.

On an integer shell [2^J,2^(J+1)) define the comparison label G_J(n)=g_J(log_2(n/2^J)). We claim

    #{n in shell: F(n)!=G_J(n)} = O(2^J/sqrt J).     (4)

For each valuation v<=J/2 the two functions to compare are g_(J-v) and g_J on the same mantissa t. By (3) their L1 difference is O(v/sqrt J). Their discrepancy set is a union of O(J^K) intervals and points. Under x=2^J 2^t, Lebesgue measure is at most C 2^J times its circle measure. Counting the progression n=2^v mod2^(v+1) on each interval adds at most O(J^K) error; the count is O(2^(J-v) v/sqrt J + J^K). Sum over v<=J/2 using sum v 2^-v<infinity. The remaining n divisible by 2^floor(J/2) number O(2^(J/2)+1). The polynomial discretization costs are negligible against 2^J/sqrt J. This proves (4).

The comparison label has at most O(J^K) adjacent changes on its shell. Each mismatch in (4) can introduce at most two additional changes. Include shell boundaries and sum dyadically to obtain the claimed O(X/sqrt(log X)) adjacent variation of F.

## 3. Approximate tripling and the actual shortcut edges

For n in shell J, the mantissa of 3n is t+theta modulo 1, and its shell depth is J+r with r in {1,2}. By (4), replacing F(n) and F(3n) with the respective comparison labels costs O(2^J/sqrt J) exceptional n (the map n->3n is injective, so count its exceptional outputs in the two shells). Replace g_(J+r) at the rotated mantissa by g_J, costing the same order by the consecutive-depth estimate (3) and interval counting. The rotation estimate in (3), again converted to integer count with O(J^K) interval boundary errors, gives O(2^J/sqrt J) further mismatches. This proves the tripling bound upon summing shells.

On even n, F(Tn)=F(n) exactly. On odd n, exact doubling gives F(Tn)=F(3n+1). A mismatch with F(n) requires a tripling mismatch at n or an adjacent change at 3n. Count the latter by injectivity of n->3n. This proves the stated shortcut-defect bound.

## 4. Actual natural density, and finite verification cannot repair the approximation

For a fixed interval I on the circle, approximate g_J invariance under the irrational rotation in (3) implies its integral on I tends to |I|/2, uniformly in I. For an elementary proof average 1_I along any fixed convergent grid of size Q; the discrepancy from its mean is O(1/Q), while replacing the original test by the rotation average costs O(Q/sqrt J). First choose a large convergent Q and then let J grow. The means of g_J are exactly 1/2. The weighted interval version with weight (log2)2^t follows by integration by parts. With the O(J^K) discretization error and (4), the natural count of each color on every subinterval of [2^J,2^(J+1)) is half its length plus o(2^J), uniformly in that subinterval. Geometric summation, first discarding a small initial proportion, shows each color of F has natural density 1/2.

Given a finite set S of positive integers, redefine F to be 1 on every dyadic ray with the same odd part as a member of S. This changes at most O_S(log X) labels up to X, preserves exact doubling, and alters each of the other three counts by O_S(log X): adjacent changes by at most twice the number of modifications, tripling by injectivity, and shortcut by its at-most-two inverse branches. Density 1/2 is preserved. In particular all starts below an arbitrarily supplied finite certified bound can have label 1.

The preceding spectral arguments use only the quantitative variation, doubling/rotation errors, and shell primitive discrepancy (for this model a power-log discrepancy follows from the same Diophantine argument). All of these hold here, including the new polynomial-phase result. Hence they cannot give full rigidity without an additional pointwise exact-graph inference, for instance a proof that a purported invariant color cannot support these slowly drifting resonant waves while satisfying every odd shortcut edge.

This function is NOT an invariant Collatz basin. It provides no ordinary positive counterexample, and does not refute any argument using the full exact pointwise equations rather than their averaged consequences. The construction is a diagnosis of the scope of the density and spectral screens, not a replacement for the open universal theorem.