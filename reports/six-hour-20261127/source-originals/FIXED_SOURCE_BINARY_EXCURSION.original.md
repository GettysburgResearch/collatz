# A fixed ordinary source exits a narrow binary critical corridor

Let an injective positive ordinary odd Collatz segment begin at A, have n accelerated edges with gaps in {1,2}, and satisfy
[
 \max_{0\le j\le n}(E_j-j\lambda)-\min_{0\le j\le n}(E_j-j\lambda)\le99/50,
 \qquad \lambda=\log_2 3 .
]
For every ε>0 it satisfies
[
 n\ll_ε (A+1)^{999/3000+ε}.
]
Consequently an actual nonrepeating ray from A has left this binary critical corridor by that many edges. This is an ineffective consequence of the integral fixed-place Subspace Theorem via Paper 145 Lemma 4. It requires no irrationality-exponent estimate, ternary anchor or cyclic closing argument.

To prove the statement, every subinterval coefficient 3^k/2^S is <4. A direct summation of the positive additive increments gives x_j≤4A+4j/3. Set Y=4(A+n+1). Each rotated length-b portion of the given segment has the same real-width cap at the fixed slope λ, even though its floor intercept may vary. At the proof's counting length b=O(log Y), the argument in §§1–4 of FOUR_BRIDGE_BINARY_CYCLE_BOUND.md counts all possible starting integers in [1,Y]. Only (2), the local width and the fixed slope were used there through the located bound. In particular it applies verbatim with d=1, θ=λ, and no end-to-start identification. Given any t>999/3000, choose its bridge parameter η small enough and absorb the logarithmic phase count to obtain O_t(Y^t) possible starts. Every member of the injective segment except the last b dates contributes one distinct start if n≥b. Thus n≪_t log(2Y)+Y^t. Choose t between 999/3000 and min(1,999/3000+ε). If n>A+1, this bounds n by an absolute constant depending on t. Otherwise it gives the stated power of A+1.

The cited PR206 ReturnOrbit gives excursions on much more general integral signed histories and polynomial dependence on width and denominator with an explicit horizon. The bound here is a narrower located-source exponent, under binary valuations, fixed real width and no repetition. Paper 145 already transfers its own broader canonical-height estimates to transient episodes. The two-ended ordinary controls in TWO_ENDED_LOCAL_INTEGER_CONTROLS.md show that at the shorter natural coding horizon log₃Y, genuine finite ordinary starting and ending states alone admit more than Y^{1/3} centers, including paths with no initial descent.
