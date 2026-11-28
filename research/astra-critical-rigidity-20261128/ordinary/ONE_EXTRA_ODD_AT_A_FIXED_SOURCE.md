# One extra odd departure along one specified ordinary orbit

**Proposed, source-qualified written result.** The external analytic inputs are identified below; this note is not a Lean formalization.

Fix a positive integer \(x\). Let \(t_n\) be its \(n\)-th post-odd date, \(z_n=T^{t_n}x\), \(L_n=3^n/2^{t_n}\), and \(A_n=z_n/L_n-x\). Fix an eligible ordinary first mark \(N\not\equiv2\pmod3\), \(N\ge1\), and set \(q_N=(2N-1)/3\). At grade \(n+1\), count **only** the positive reduced rational sources which agree with this one ordinary integer for the first \(t_n\) dates and then first land exactly at \(N\). Denote their real-source counting measure by \(\Xi_{n,N}\). All the sources have precisely one more odd departure after the prescribed prefix.

On an eventually periodic orbit, \(\Xi_{n,N}\) vanishes on every fixed bounded positive interval for all large \(n\). On an aperiodic orbit, write \(A=\lim_n A_n\in(0,\infty)\). For every compactly supported continuous \(f\) on \((0,\infty)\),
\[
 \frac1K\sum_{n=1}^K\int f(r)\,d\Xi_{n,N}(r)
 \longrightarrow
 \frac1{\log2}\int_0^\infty \frac{f(r)}{A+r}\,dr.                        \tag{1}
\]
The same formula holds for indicators of fixed intervals \(I=(a,b)\), \(0\le a<b\). More specifically, the fraction of grades for which at least one such positive source lies in \(I\) tends to
\[
            \min\left(1,\log_2\frac{A+b}{A+a}\right).                     \tag{2}
\]
This gives a positive density for every specified ordinary mark, however narrow the source window, at the smallest possible positive additional grade. By contrast, without the added odd departure the signed preimage of fixed \(N\) approaches the negative real \(-A\). [Exact fixed-prefix fibre theorem](FIXED_ORDINARY_LANDING_FIBRES.md)

Indeed the sole remaining odd step is terminal. If \(H\ge0\) evens precede it, the state at \(t_n\) must be \(2^H q_N\). Reversing the fixed prefix gives exactly
\[
             r=2^H q_N/L_n-A_n,\qquad t=t_n+H+1 .                      \tag{3}
\]
Whenever \(r>0\), this has reduced denominator \(3^{n+1}\), the prescribed native bits, and first integer \(N\). This follows directly by the genuine inverse letters \(2y,(2y-1)/3\), starting at the nonintegral \(q_N\). Conversely every counted source has this form exactly once. On a periodic tail \(L_n\) decays exponentially; the dyadic cylinder requires \(|3^{n+1}r-3^{n+1}x|\ge2^{t_n}\), inconsistent with bounded \(r\). On an aperiodic ordinary orbit the known reciprocal summability yields \(z_n,L_n\to\infty\) and \(A_n\uparrow A\). For a bounded window in \([0,\infty)\), the restriction \(H\ge0\) is then automatic for all sufficiently late \(n\). [Garcia and Tal, Lemma 3 and Corollary 1](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf)

Write \(\gamma=\log_23\) and \(\theta_n=\{n\gamma\}\). With \(j\in\mathbb Z\), the real arrays in (3) are thus locally identical to
\[
                  r_{j,N}(\theta_n,A_n)=2^{j-\theta_n}q_N-A_n
\]
at late dates. Only boundedly many \(j\)'s enter a fixed bounded positive window, since \(A>0\). For any finite collection of eligible marks the whole vector of these point measures, tested by continuous compact functions, converges in empirical law to the same arrays \(r_{j,N}(\Theta,A)\), with a **single uniform** \(\Theta\in[0,1]\). The arrays are periodic as unlabelled sets at the circular boundary and depend continuously on the phase under these tests. This is equidistribution of the one irrational rotation \(n\gamma\), with a perturbation \(A_n\to A\). For interval indicators there are only finitely many exceptional boundary phases. Integrating the array over a uniform phase, with \(r+A=2^{j-\theta}q_N\), gives (1). The number of integer lattice indices in an interval of logarithmic length \(w=\log_2((A+b)/(A+a))\) is \(\lfloor w\rfloor\) or \(\lceil w\rceil\), giving (2). The limits also hold on any moving consecutive windows of grades whose lengths tend to infinity, by uniformity of irrational rotation in the initial phase and the negligible finite prefix.

For a counted source at its genuine date \(t\), the exact identity
\[
                       3^n 2^{-t}=\frac{q_N}{2(r+A_n)}
\]
gives the empirical limit of its rescaled reciprocal-time mass, with density \(q_N/(2(\log2)(A+r)^2)\) in place of the density in (1). This is a different sampling regime from the [full fixed-mark renewal profile](FIXED_TARGET_RENEWAL_PROFILE.md). All dates in (1) refer to prefixes of the **same** underlying ordinary integer \(x\).

## A polynomial real approximation at convergent scales

There is an absolute \(\eta\in(0,1)\) from Garcia and Tal's orbit sparsity with the following consequence. Fix \(r_0>0\) and eligible \(N\). For every sufficiently large convergent denominator \(Q\) of \(\gamma\), in **every** interval of \(O_{x,r_0,N}(Q^{2-\eta}\log(2Q))\) consecutive post-odd grades (with a sufficiently large choice of constant) there is an \(n\) and an actual source counted by \(\Xi_{n,N}\) with
\[
                           |r-r_0|\ll_{x,r_0,N}1/Q.                      \tag{4}
\]
In particular choose \(n\) in a block whose starting index is comparable to this interval length. Along a sequence \(n\to\infty\) the error is \(O(n^{-1/(2-\eta)+o(1)})\). Choosing \(r_0=x\) additionally gives \(|r-x|_2\le2^{-t_n}\) by the true prefix. Thus both real and dyadic distances tend to zero along actual first preimages of one and the same ordinary mark, with just one further odd step.

Here are details uniform over the start of the grade block. The aperiodic orbit visits each interval of \(M\) consecutive positive integers in at most \(C M^{1-\eta}\log(2M)\) states, by Garcia and Tal's fundamental lemma. It follows, using the dyadic partition of \((Q,\infty)\), that the full orbit has at most \(C Q^{1-\eta}\log(2Q)\) states of height at most \(Q\), and
\[
                  \sum_{z_n>Q}1/z_n\ll Q^{-\eta}\log(2Q).                \tag{5}
\]
All post-odd states are distinct. Moreover \(A_n-A_{n-1}=1/(2L_n)=(x+A_n)/(2z_n)\). Hence the increment of \(\log_2(A_n+r_0)\) is \(O_{x,r_0}(1/z_n)\). Divide the supplied interval into disjoint groups of \(Q\) successive grades. Discard groups containing any \(z_n\le Q\), at most \(C Q^{1-\eta}\log(2Q)\) groups. Of the remaining groups, at most \(C_{x,r_0}Q^{1-\eta}\log(2Q)\) have phase correction variation greater than \(1/Q\), by (5). At least one group remains if the interval constant is sufficiently large.

On this group \(Q\) consecutive unperturbed phases \(n\gamma\) form a \(2/Q\)-net of the circle: a convergent \(a/Q\) satisfies \(|\gamma-a/Q|<Q^{-2}\), and \(j a/Q\), \(0\le j<Q\), runs over its full grid. Freezing the correction at the first grade thus supplies some \(n\) for which
\[
      \big\|\,n\gamma+\log_2(A_n+r_0)-\log_2 q_N\,\big\|\le 3/Q.
\]
Take the nearest integer after replacing \(n\gamma\) by \(\log_2 L_n=n\gamma-t_n\). It is nonnegative for large \(Q\), since \(L_n=z_n/(x+A_n)>Q/(x+A)\) on the group. Equation (3) now gives (4) by exponentiation. This uses no irrationality-measure estimate. If a bound \(\mu(\gamma)\le\mu_0\) is assumed, successive convergent denominators satisfy \(Q_{\rm next}\le Q^{\mu_0-1+o(1)}\); (4) then gives an error \(K^{-1/((2-\eta)(\mu_0-1))+o(1)}\) in each interval of \(K\) grades, as \(K\to\infty\). Formula (4) needs only the stated aperiodicity of the specified positive integer trajectory. The existence of such a trajectory remains open.
