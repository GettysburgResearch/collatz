# The Mersenne-to-Mersenne odd paths with one reset

Write \(M_m=2^m-1\) for \(m\ge1\). An odd Syracuse step with input \(y\) is division of \(3y+1\) by its exact power of two. Count a reset whenever the exponent exceeds one. This definition includes the step from 1 to 1.

**Kernel theorem.** Suppose a finite path from one positive Mersenne number to another has exactly one reset. Its entire odd itinerary is either \(1\to1\), with exponent 2, or \(3\to5\to1\), with exponents 1,4. This covers arbitrary path length, arbitrary reset exponents, and arbitrary nominal runs before or after the reset. [Lean source](MersenneReset.lean)

To see the physical reduction, any \(t\)-step run of exponent-one steps from \(x\) to \(z\) satisfies \(2^t(z+1)=3^t(x+1)\). No nonempty such run can terminate at a Mersenne number since its endpoint plus one would be divisible by three. Thus the reset is the final step. Its input has \(z\equiv1\pmod4\), so \(v_2(z+1)=1\). Comparing the exact dyadic powers in the previous identity gives \(t=m-1\) and \(z+1=2\cdot3^t\). A final reset of exponent \(b+1\) with endpoint \(M_k\) therefore gives
\[
   3^m+2^b=2^{b+k}+1,\qquad m,b,k\ge1.
\]

Reduction modulo 3 forces both \(b\) and \(k\) odd. If \(m\) is odd, reducing modulo 8 forces \(b=k=1\) and the equation then gives \(m=1\). For even \(m=2d\) put \(z=3^d\) and \(y=2^{(b+k)/2}\). The equation gives \(y^2-z^2=2^b-1>0\) and \(2^b\mid(z-1)(z+1)\). The two even neighbors of \(z\) differ by two, so their common power of two is exactly two. This implies \(2^b\le2(z+1)\), and \(y^2-z^2\le2z+1\), forcing \(y=z+1\). Reducing \(2^{(b+k)/2}=3^d+1\) modulo 8 gives \(d=1\). Substitution gives \((m,b,k)=(2,3,1)\). Both surviving physical itineraries occur, as witnessed in the same Lean file.

This classification gives the effective one-reset case of the fixed-rank finite-return phenomenon. Counts of two or more resets require other arguments; no complete finite list for such counts is claimed here. For a general source, one reset can involve an arbitrarily large exponent.
