# Instantaneous joint arithmetic mixing at a supplied inverse root

Let X_q be the canonical inverse walk starting at a fixed positive odd
unit t. In the compact space E=Z₂^odd×Z₃,

    Law_t((X_q,X_q)) → ν = normalized odd dyadic Haar × μ             (1)

weakly as q→∞ along all depths. For every fixed block length the
distribution of the most recent inverse exponents converges in total
variation to that of independent positive geometric exponents. No
uniformity over moving initial roots is implicit in (1).

Extend the transfer to E by applying the inverse map
G_a(v,z)=((2^a v−1)/3,(2^a z−1)/3) with weight J_a=3·2^(−a) and
the usual ternary compatibility indicator. Write this operator as L_E.
It preserves the integral of nonnegative functions against
σ=normalized odd dyadic Haar × ternary Haar. Indeed the image of odd
dyadic Haar by v↦(2^a v−1)/3 is its normalization on the child cylinder
v₂(3x+1)=a, of probability 2^(−a). The change of variables on the
compatible ternary target cylinder has Haar factor 1/3. These two
factors cancel J_a, and the dyadic child cylinders partition odd
Haar up to the single point −1/3.

Let 0≤f≤1 be continuous and constant on dyadic classes of precision d
in its first coordinate. For any inverse word of length d the child
dyadic coordinate depends on the initial dyadic point with contraction
at least 2^(−d). Thus L_E^d(h f)(v,z) is a function k_f(z) of the
ternary point alone. It is nonnegative and lower semicontinuous: for
each word the compatible target cylinder is clopen, its ternary affine
inverse is continuous, and the nonnegative word sums increase from
finite subsums. Interpret 0 times +∞ as zero; a nonnegative continuous
factor times h is lower semicontinuous with that convention. Integral
preservation gives λ(k_f)=σ(h f).

For q≥d this gives L_E^q(hf)(t,t)=L^(q−d)k_f(t). The lower bound
(6) in the every-depth proof applies and gives

    liminf_q L_E^q(hf)(t,t) ≥ (3/2)h(t) σ(h f)=h(t)ν(f).

Zero integral is harmless because the left side is nonnegative.
Use the same inequality for 1−f and L_E^q h(t,t)=h(t) to get
convergence. Divide by h(t), which gives the actual inverse expectation
by the telescoping branch probabilities. Such f approximate arbitrary
continuous tests in sup norm, proving (1). The argument applies equally
to a finite positive-h ternary root with an arbitrary odd dyadic
coordinate and its normalized geometric inverse kernel.

A finite forward valuation word at the child is a clopen dyadic
cylinder; reading it from the reverse path reverses the order of the
most recent inverse letters. Its ν-mass is 2^(−sum a). For a fixed
block length these words form a countable partition with total limiting
probability one, giving total-variation convergence by truncation to
a finite subfamily. Fixed windows of joint states have their stationary
laws as well, since the earlier states are forward iterates of the final
one and each exceptional dyadic slice is ν-null.

For a fixed bounded path event B one also has
E_t[1_B f(X_q,X_q)]→P_t(B)ν(f) for continuous f. First condition on a
fixed finite path prefix and use (1) at its ordinary endpoint and
bounded convergence. Then approximate 1_B in L¹ by its conditional
expectations along the increasing finite-prefix sigma fields.

[Every-depth minorization and positive-test liminf](EVERY-DEPTH.md).
[Canonical walk and stationary product law](CANONICAL-RETURN.md).
